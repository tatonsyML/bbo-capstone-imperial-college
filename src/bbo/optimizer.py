"""Small HEBO-inspired and TuRBO-style candidate-selection experiments.

Purpose
-------
These functions demonstrate ideas investigated during the capstone, particularly
around Round 10. They accept *observed* input/output pairs, fit predictive
models and propose unobserved candidate inputs. They do not call the course
portal or assign any real objective value to a suggestion.

Two distinct experimental strategies
------------------------------------
* hebo_inspired_committee: fit several GP kernels to the same observations,
  compare EI/PI/UCB acquisition rankings over one common Sobol candidate pool,
  and choose a robustly ranked suggestion for each kernel. This is inspired by
  combining alternative models and acquisition rules; it is NOT official HEBO.
* turbo_style_candidate: restrict a GP/EI search to a fixed box around the
  best *measured* input, borrowing only the local-search idea from TuRBO.
  It has no feedback-driven trust-region expansion, contraction or restarts.

The optional official_hebo_suggest adapter uses the actual HEBO library for a
single suggestion; it is not the full evaluated feedback loop. A separate
post-capstone benchmark under research/full_optimisers/ implements official
HEBO and an adaptive BoTorch TuRBO-1 comparison, with explicitly labelled
simulated feedback.

Common workflow: observed X/y -> GP fit -> score unseen candidates -> suggest.
Historical portal returns and post-capstone simulations remain separate.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import qmc

from .surrogates import fit_gp, inverse_mean
from .acquisition import (
    expected_improvement,
    probability_improvement,
    upper_confidence_bound,
)
from .search import portal_string, trust_region_bounds, scale_to_box


def hebo_inspired_committee(X, y, seed=100, n_power=15):
    """Suggest one candidate per kernel using a HEBO-inspired committee.

    Parameters
    ----------
    X : array-like, shape (n_observations, n_dimensions)
        Inputs already evaluated by the portal.
    y : array-like, shape (n_observations,)
        Corresponding *measured* scores; higher is better.
    seed : int
        Scrambling seed for the shared Sobol pool and repeatable GP fits.
    n_power : int
        Generate 2**n_power potential inputs for each model to rank.

    How it works
    ------------
    1. Draw ONE Sobol pool, shared by all surrogate models. Holding candidates
       fixed makes differences in the results attributable to the models.
    2. Fit separate RBF, Matérn-1.5 and Matérn-2.5 Gaussian Processes using
       Yeo–Johnson-transformed measured targets.
    3. Score every candidate using Expected Improvement (EI), Probability of
       Improvement (PI) and Upper Confidence Bound (UCB). EI and PI compare
       against the best measured *transformed* target.
    4. Convert each acquisition's scores to ranks on [0, 1], where higher is
       preferable; combine them through the lower quartile (25th percentile).
       This favours candidates that are reasonably strong across acquisition
       rules rather than exceptional under only one.
    5. For each GP kernel, suggest the highest-ranking candidate. The returned
       'predicted_mean' is transformed back onto the original score scale,
       but the 'transformed_sd' remains on the GP target scale.

    Returns
    -------
    pandas.DataFrame
        Three rows (one per kernel) containing suggested six-decimal portal
        inputs, acquisition-consensus ranks and MODEL predictions. No proposed
        candidate has been evaluated by this function.

    Scope
    -----
    This is a deliberately small, HEBO-*inspired* comparison, not the full
    HEBO algorithm or its model/optimisation portfolio. The candidates are
    model suggestions, never new observations or guaranteed improvements.
    """
    # Work with numeric copies of the supplied observations. No portal calls
    # or updates to the historical evaluation record occur in this function.
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    dimension = X.shape[1]

    # Stage 1: evaluate the same candidate coordinates under every GP kernel.
    # A scrambled Sobol sequence provides broad, repeatable coverage of the
    # input box; unlike ordinary random sampling it is low-discrepancy.
    # Using one pool avoids confounding model choice with different test points.
    candidate_pool = qmc.Sobol(
        d=dimension, scramble=True, seed=seed
    ).random_base2(n_power)
    # The optimiser works in the course's legal coordinate range.
    # Clipping here does not mean we have observed the resulting points.
    candidate_pool = np.clip(candidate_pool, 1e-6, 0.999999)

    rows = []
    # Stage 2: test alternative assumptions about response smoothness.
    # RBF favours smoother functions; Matérn 1.5/2.5 permit rougher behaviour.
    # These are independent fits to the SAME measured X and y, not a vote
    # against real portal outcomes.
    for kernel in ("RBF", "Matern15", "Matern25"):
        # Yeo–Johnson can transform negative, zero and positive targets.
        # The fitted transform is learned from observed y only. Both GP
        # predictions and acquisition scores below use this transformed scale.
        gp, transformation, transformed_y = fit_gp(
            X, y, kernel, "yeo-johnson", seed=seed
        )
        # Stage 3: predict (without observing) a mean and standard deviation
        # for each point in the common pool. The incumbent must be the best
        # ACTUAL training score on the same transformed scale.
        mean, uncertainty = gp.predict(candidate_pool, return_std=True)
        incumbent = float(transformed_y.max())

        # EI values possible gain, PI values its likelihood, and UCB trades
        # predicted score against uncertainty (here beta=1.96). These three
        # acquisition scores are different quantities, NOT directly additive.
        scores = np.vstack([
            expected_improvement(mean, uncertainty, incumbent),
            probability_improvement(mean, uncertainty, incumbent),
            upper_confidence_bound(mean, uncertainty, beta=1.96),
        ])

        # Stage 4: turn each acquisition into ordinal preference ranks.
        # argsort(argsort(.)) assigns 0 to the lowest score and N-1 to the
        # highest; division maps this to [0, 1]. Ties are not given a special
        # statistical treatment, so the result is a heuristic, not a
        # calibrated probability or comparable uncertainty estimate.
        ranks = np.vstack([
            np.argsort(np.argsort(s)) / (len(s) - 1) for s in scores
        ])
        # Using the 25th percentile instead of the average penalises a
        # candidate that one acquisition rule ranks poorly. With three rules,
        # this offers a conservative consensus; it is not an official HEBO
        # ensemble or a formal robust-optimisation guarantee.
        robust_rank = np.quantile(ranks, 0.25, axis=0)
        # Stage 5: one unobserved proposal for EACH GP kernel, not three new
        # evaluations. A later human/portal decision is still required.
        winner = int(np.argmax(robust_rank))
        rows.append({
            "kernel": kernel,
            "candidate": portal_string(candidate_pool[winner]),
            "robust_rank": float(robust_rank[winner]),
            # Undo the training transform for an interpretable predicted
            # location. For nonlinear transforms this is NOT the exact
            # posterior expectation E[y] on the original response scale.
            "predicted_mean": float(
                inverse_mean([mean[winner]], transformation)[0]
            ),
            # Preserve the scale explicitly: this sigma is in transformed
            # GP target units, not the units of the original portal score.
            "transformed_sd": float(uncertainty[winner]),
        })
    return pd.DataFrame(rows)


def turbo_style_candidate(X, y, length=0.20, seed=900, n_power=15):
    """Suggest an EI-maximising candidate in a fixed, incumbent-centred box.

    Parameters
    ----------
    X : array-like, shape (n_observations, n_dimensions)
        Previously evaluated inputs within the permitted numerical domain.
    y : array-like, shape (n_observations,)
        Real observed scores; larger is better.
    length : float, default 0.20
        Total side length of the candidate box in each coordinate, *before*
        clipping at the domain edges. It is not learned or updated from results.
    seed : int, default 900
        Seed for reproducible Sobol candidates and GP fitting.
    n_power : int, default 15
        Number of local trial inputs is 2**n_power.

    Procedure
    ---------
    1. Find the input with the highest *observed* y.
    2. Build a box of width 'length', centred on that incumbent and clipped
       to [0, 0.999999] along each dimension.
    3. Spread Sobol candidate points inside this box.
    4. Fit a Matérn-2.5 Gaussian Process with a Yeo–Johnson target transform,
       then score local points by Expected Improvement relative to the
       best measured transformed target.
    5. Return the highest-EI candidate and its model predictions, WITHOUT
       making a portal query or assigning any observed output.

    Returns
    -------
    dict
        'candidate' is six-decimal submission text, 'predicted_mean' is the
        inverse-transformed GP location and 'ei_transformed' is acquisition
        value on the transformed target scale.

    Difference from full TuRBO
    --------------------------
    This reproduces ONLY its notion of searching near an incumbent. It does
    not adapt the box after successes/failures, use GP lengthscale-weighted
    box widths, maintain a success/failure counter, perform Thompson
    sampling, or restart. Full TuRBO-1 is a separate post-capstone
    implementation under research/full_optimisers/.
    """
    # Existing measured data are the only observations available here.
    # Neither a GP prediction nor a pending candidate is added to training.
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    dimension = X.shape[1]

    # Stage 1: choose the best REAL input in y as the centre. Starting from
    # the GP's predicted maximum instead would compound modelling error.
    incumbent_location = X[int(np.argmax(y))]
    # Stage 2: restrict exploration to a fixed local box. Near a boundary
    # the box is truncated rather than expanded or re-centred elsewhere.
    # The box will NOT adapt to feedback: this is not complete TuRBO.
    lower, upper = trust_region_bounds(incumbent_location, length)

    # Stage 3: draw 2**n_power reproducible Sobol points in the unit cube.
    # Low-discrepancy sampling gives more even trial coverage than naive
    # independent uniform draws under the same candidate budget.
    unit_points = qmc.Sobol(
        d=dimension, scramble=True, seed=seed
    ).random_base2(n_power)
    # Map unit-cube points into the measured incumbent's local box.
    # These are only possible future submissions, not evaluated points.
    candidate_pool = scale_to_box(unit_points, lower, upper)

    # Stage 4: fit a single ARD Matérn-2.5 GP. The Yeo–Johnson transform
    # handles positive, zero and negative scores using observed training y.
    # The uncertainty and acquisition values below remain on that scale.
    gp, transformation, transformed_y = fit_gp(
        X, y, "Matern25", "yeo-johnson", seed=seed
    )
    mean, uncertainty = gp.predict(candidate_pool, return_std=True)

    # Stage 5: EI favours predicted gains while also rewarding uncertainty.
    # Compare against the best OBSERVED transformed output, not the GP's
    # own largest predicted value. EI is a model-based ranking, not a promise.
    score = expected_improvement(mean, uncertainty, float(transformed_y.max()))
    winner = int(np.argmax(score))
    # Return an unscored suggestion. The portal score, if one is later
    # observed, must be recorded separately before fitting another model.
    return {
        "candidate": portal_string(candidate_pool[winner]),
        # Inverse-transforming the predicted location aids interpretation,
        # but is not the exact posterior mean under a nonlinear transform.
        "predicted_mean": float(
            inverse_mean([mean[winner]], transformation)[0]
        ),
        # Transformed-scale EI is not an expected score gain in raw units.
        "ei_transformed": float(score[winner]),
    }


def official_hebo_suggest(X, y):
    """Ask the *official* HEBO package for one unscored suggestion.

    This optional compatibility adapter is distinct from the hand-built
    committee above. It creates HEBO's continuous-variable design space,
    supplies previously observed data, then asks the library for one point.

    HEBO's optimisation convention is minimisation. The capstone convention
    is maximisation, so -y is passed to HEBO's observe() method. Without
    this sign conversion it would seek *worse* portal scores.

    This function does not submit a query or execute a complete feedback
    loop; it assumes that X and y already contain authentic observations.
    For official-engine benchmarking with simulated feedback, see
    research/full_optimisers/benchmark.py.
    """
    # Import on demand: the lightweight historic experiment should still
    # run without installing HEBO and its potentially conflicting dependencies.
    try:
        from hebo.design_space.design_space import DesignSpace
        from hebo.optimizers.hebo import HEBO
    except ImportError as exc:
        raise RuntimeError("Install HEBO to use official_hebo_suggest") from exc

    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    # HEBO uses named design variables; each has the same legal numeric
    # range as the capstone portal's input coordinates.
    columns = [f"x{i + 1}" for i in range(X.shape[1])]
    space = DesignSpace().parse([
        {"name": name, "type": "num", "lb": 0.0, "ub": 0.999999}
        for name in columns
    ])
    optimiser = HEBO(space)
    # Critical sign convention: negating observed scores turns our
    # maximisation problem into HEBO's expected minimisation problem.
    # This uses REAL supplied outcomes, not model-simulated feedback.
    optimiser.observe(pd.DataFrame(X, columns=columns), -y)
    # A suggested coordinate has no true objective value until evaluated.
    suggestion = optimiser.suggest(n_suggestions=1)
    return suggestion[columns].to_numpy(float)[0]
