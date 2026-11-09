"""Historical capstone optimisers: HEBO-inspired and TuRBO-style challengers.

These small functions document mechanisms explored around Round 10.
They are NOT the full reference HEBO/TuRBO implementations. Those appear in
benchmarks/full_optimisers/ and were added for post-capstone comparison.

Workflow: fit -> score candidates -> select one -> submit to portal -> observe.
This module stops at selection; it NEVER invents a portal return.
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
    """Compare kernels and acquisition functions on identical Sobol points.

    Why: with very few black-box observations, trusting one GP/acquisition
    can overstate confidence. This exploratory committee keeps candidate
    evaluation identical for RBF and two Matérn alternatives.

    It is a simplified, HEBO-*inspired* mechanism, not HEBO itself.
    Returns three model-specific suggestions, NOT three measured scores.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    dimension = X.shape[1]

    # Use the SAME legal candidate pool for every model, making ranking
    # differences attributable to the surrogate rather than random samples.
    candidate_pool = qmc.Sobol(
        d=dimension, scramble=True, seed=seed
    ).random_base2(n_power)
    candidate_pool = np.clip(candidate_pool, 1e-6, 0.999999)

    rows = []
    for kernel in ("RBF", "Matern15", "Matern25"):
        # Yeo–Johnson handles both positive and negative responses. Its fitted
        # transform must be inverted before displaying predicted raw scores.
        gp, transformation, transformed_y = fit_gp(
            X, y, kernel, "yeo-johnson", seed=seed
        )
        mean, uncertainty = gp.predict(candidate_pool, return_std=True)
        incumbent = float(transformed_y.max())

        scores = np.vstack([
            expected_improvement(mean, uncertainty, incumbent),
            probability_improvement(mean, uncertainty, incumbent),
            upper_confidence_bound(mean, uncertainty, beta=1.96),
        ])

        # Acquisition values have incompatible units. Rank NORMALISATION
        # avoids comparing the raw EI, PI and UCB numbers directly.
        ranks = np.vstack([
            np.argsort(np.argsort(s)) / (len(s) - 1) for s in scores
        ])
        # A lower quartile rewards candidates scoring well consistently
        # across the three acquisition rules, rather than a single spike.
        robust_rank = np.quantile(ranks, 0.25, axis=0)
        winner = int(np.argmax(robust_rank))
        rows.append({
            "kernel": kernel,
            "candidate": portal_string(candidate_pool[winner]),
            "robust_rank": float(robust_rank[winner]),
            "predicted_mean": float(
                inverse_mean([mean[winner]], transformation)[0]
            ),
            "transformed_sd": float(uncertainty[winner]),
        })
    return pd.DataFrame(rows)


def turbo_style_candidate(X, y, length=0.20, seed=900):
    """Choose local EI candidate inside a fixed incumbent-centred box.

    This implements *one* idea from TuRBO, namely restricted local sampling.
    It lacks full trust-region adaptation and restarts. See the separate
    BoTorch-based TuRBO-1 benchmark for those mechanisms.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    dimension = X.shape[1]

    # Centre on the strongest ACTUAL observation, not the GP's own forecast.
    incumbent_location = X[int(np.argmax(y))]
    lower, upper = trust_region_bounds(incumbent_location, length)

    # Sobol points fill the local box more evenly than ordinary random draws.
    unit_points = qmc.Sobol(
        d=dimension, scramble=True, seed=seed
    ).random_base2(15)
    candidate_pool = scale_to_box(unit_points, lower, upper)

    gp, transformation, transformed_y = fit_gp(
        X, y, "Matern25", "yeo-johnson", seed=seed
    )
    mean, uncertainty = gp.predict(candidate_pool, return_std=True)

    # EI gives credit both to high mean and to uncertainty worth testing.
    score = expected_improvement(mean, uncertainty, float(transformed_y.max()))
    winner = int(np.argmax(score))
    return {
        "candidate": portal_string(candidate_pool[winner]),
        "predicted_mean": float(
            inverse_mean([mean[winner]], transformation)[0]
        ),
        "ei_transformed": float(score[winner]),
    }


def official_hebo_suggest(X, y):
    """Legacy optional adapter to the real HEBO package.

    HEBO is written as a MINIMISER; the sign change below converts our
    maximisation objective. The post-capstone comparison has a more
    complete warm-start/feedback loop at benchmarks/full_optimisers/.
    """
    try:
        from hebo.design_space.design_space import DesignSpace
        from hebo.optimizers.hebo import HEBO
    except ImportError as exc:
        raise RuntimeError("Install HEBO to use official_hebo_suggest") from exc

    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    columns = [f"x{i + 1}" for i in range(X.shape[1])]
    space = DesignSpace().parse([
        {"name": name, "type": "num", "lb": 0.0, "ub": 0.999999}
        for name in columns
    ])
    optimiser = HEBO(space)
    optimiser.observe(pd.DataFrame(X, columns=columns), -y)
    suggestion = optimiser.suggest(n_suggestions=1)
    return suggestion[columns].to_numpy(float)[0]
