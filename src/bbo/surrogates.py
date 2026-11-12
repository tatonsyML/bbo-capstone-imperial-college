"""Gaussian Process surrogates and response-scale transformations.

The unknown eight capstone objectives produce scores with different
magnitudes, including tiny, negative and very large values. Fit a model
to one function at a time using observed inputs and scores. A target
transform sometimes improves numerical conditioning, but the original
recorded scores are never overwritten.

The GP predictive mean/standard deviation belong to its *training target
scale*. The inverse_mean helper converts a predicted location to raw
score units for readability. With nonlinear transformations, that is
not the exact posterior mean or a calibrated raw-scale confidence band.

Historical replay callers must fit transformations using ONLY the
observations known by the chosen round; using later portal returns would
leak future information into an earlier decision.
"""
from __future__ import annotations

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, Matern, WhiteKernel
from sklearn.preprocessing import PowerTransformer


def transform_y(y, mode="raw"):
    """Transform training scores before fitting a GP.

    Parameters
    ----------
    y : array-like
        Observed scores from one objective function, not model suggestions.
    mode : {'raw', 'yeo-johnson', 'signed-log'}
        raw returns unchanged values and no transformation object.
        yeo-johnson estimates a power transform and standardises the output,
        accommodating both positive and negative responses.
        signed-log maps sign(y)*log(1+abs(y)), then standardises manually.

    Returns
    -------
    (target, mapping)
        Transformed one-dimensional array and everything inverse_mean
        needs to express GP locations back on the raw score scale.

    Fit the transform ONLY to the data available at the model's training
    cut-off; otherwise later portal results would contaminate evaluation.
    """
    y = np.asarray(y, float).reshape(-1)
    # Preserve raw output when a scale transform is unnecessary.
    if mode == "raw":
        return y, None
    if mode == "yeo-johnson":
        # Unlike an ordinary log, this supports zero and negative scores.
        transformer = PowerTransformer(method="yeo-johnson", standardize=True)
        return transformer.fit_transform(y[:, None]).ravel(), transformer
    if mode == "signed-log":
        # Keep the sign of negative rewards while compressing extreme
        # magnitudes (especially relevant to F1 and F5 model comparisons).
        transformed = np.sign(y) * np.log1p(np.abs(y))
        mu = float(transformed.mean())
        # Avoid division by zero when the transformed training scores
        # happen to be constant; this does not manufacture variation.
        sd = float(transformed.std() or 1.0)
        return (transformed - mu) / sd, ("signed-log", mu, sd)
    raise ValueError(f"Unknown transform: {mode}")


def inverse_mean(z, transform):
    """Map transformed GP predictive locations back to raw score units.

    Parameters
    ----------
    z : array-like
        Predicted locations (usually means) from a model fitted in the
        transformed target space.
    transform : None, sklearn PowerTransformer or signed-log tuple
        Representation produced by transform_y on training observations.

    Returns one-dimensional raw-scale predicted locations. Because
    E[g^{-1}(Z)] is generally not g^{-1}(E[Z]), this does NOT provide
    an exact raw-scale posterior expectation or uncertainty interval.
    """
    z = np.asarray(z, float).reshape(-1)
    if transform is None:
        return z
    if isinstance(transform, PowerTransformer):
        return transform.inverse_transform(z[:, None]).ravel()
    # Undo manual signed-log standardisation before its signed expm1.
    _, mu, sd = transform
    q = z * sd + mu
    return np.sign(q) * np.expm1(np.abs(q))


def fit_gp(X, y, kernel="Matern25", transform="yeo-johnson", seed=0, restarts=4):
    """Fit one anisotropic (ARD) Gaussian Process to observed data.

    Parameters
    ----------
    X : array-like, shape (n_observations, n_dimensions)
        Previously evaluated inputs; no future or synthetic labels.
    y : array-like, shape (n_observations,)
        Corresponding measured portal scores.
    kernel : {'RBF', 'Matern15', 'Matern25'}
        RBF assumes a particularly smooth response; Matérn 1.5/2.5
        accommodate rougher functions. Each input dimension has its own
        fitted lengthscale, letting the model express different sensitivity.
    transform : {'raw', 'yeo-johnson', 'signed-log'}
        Training-target representation selected by transform_y.
    seed : int
        Reproducible GP hyperparameter optimiser seed.
    restarts : int
        Additional optimiser starts, reducing (not eliminating) dependence
        on a single fitted hyperparameter solution.

    Returns
    -------
    model, fitted_transform, transformed_target
        Model predicts on the transformed scale. Acquisition functions
        must compare its predictions with max(transformed_target).

    The kernel is signal_variance*base_ARD + WhiteKernel. The latter
    permits learned observation noise but does not establish that the
    private objective itself is stochastic. Fitting is neither a proof
    of a global optimum nor a recreation of any missing historical script.
    """
    X = np.asarray(X, float)
    y = np.asarray(y, float).reshape(-1)
    target, fitted_transform = transform_y(y, transform)
    dimensions = X.shape[1]

    # RBF is infinitely differentiable; Matérn ν=1.5 and ν=2.5
    # encode weaker smoothness assumptions. ARD supplies a separate
    # lengthscale for each input axis in every kernel below.
    if kernel == "RBF":
        base = RBF(np.ones(dimensions), (1e-3, 10.0))
    elif kernel == "Matern15":
        base = Matern(np.ones(dimensions), (1e-3, 10.0), nu=1.5)
    elif kernel == "Matern25":
        base = Matern(np.ones(dimensions), (1e-3, 10.0), nu=2.5)
    else:
        raise ValueError(f"Unknown GP kernel: {kernel}")

    # A signal-amplitude kernel scales the covariance; WhiteKernel
    # represents observation-noise uncertainty, learned inside these
    # explicit bounds rather than declared as a known physical fact.
    covariance = (
        ConstantKernel(1.0, (1e-3, 1e3)) * base
        + WhiteKernel(1e-4, (1e-8, 1.0))
    )
    model = GaussianProcessRegressor(
        kernel=covariance, normalize_y=False,
        n_restarts_optimizer=restarts, random_state=seed,
    )
    # Training uses the original evaluated X and the *training-only*
    # transformed target. No new objective evaluations occur here.
    model.fit(X, target)
    return model, fitted_transform, target
