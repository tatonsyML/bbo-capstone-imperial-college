"""Gaussian Process regression and output transformations for capstone challengers."""
from __future__ import annotations

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, Matern, WhiteKernel
from sklearn.preprocessing import PowerTransformer


def transform_y(y, mode="raw"):
    """Put heterogeneous objective scales into a GP-friendly representation.

    Important: transformation parameters are fitted ONLY on training y.
    Reusing a transform estimated from future portal returns would leak data.
    """
    y = np.asarray(y, float).reshape(-1)
    if mode == "raw":
        return y, None
    if mode == "yeo-johnson":
        # Unlike an ordinary log, this supports zero and negative scores.
        transformer = PowerTransformer(method="yeo-johnson", standardize=True)
        return transformer.fit_transform(y[:, None]).ravel(), transformer
    if mode == "signed-log":
        transformed = np.sign(y) * np.log1p(np.abs(y))
        mu = float(transformed.mean())
        sd = float(transformed.std() or 1.0)
        return (transformed - mu) / sd, ("signed-log", mu, sd)
    raise ValueError(f"Unknown transform: {mode}")


def inverse_mean(z, transform):
    """Express transformed GP predictions on the original scoring scale.

    This is an inverse transform of the predicted location, not an exact
    calculation of E[y] for a nonlinear transform.
    """
    z = np.asarray(z, float).reshape(-1)
    if transform is None:
        return z
    if isinstance(transform, PowerTransformer):
        return transform.inverse_transform(z[:, None]).ravel()
    _, mu, sd = transform
    q = z * sd + mu
    return np.sign(q) * np.expm1(np.abs(q))


def fit_gp(X, y, kernel="Matern25", transform="yeo-johnson", seed=0, restarts=4):
    """Fit an ARD GP using one lengthscale per input coordinate.

    RBF assumes a very smooth response; Matérn 1.5/2.5 permit less smoothness.
    An additional WhiteKernel models observational noise. These are model
    assumptions, not properties established for all eight hidden functions.
    """
    X = np.asarray(X, float)
    y = np.asarray(y, float).reshape(-1)
    target, fitted_transform = transform_y(y, transform)
    dimensions = X.shape[1]

    if kernel == "RBF":
        base = RBF(np.ones(dimensions), (1e-3, 10.0))
    elif kernel == "Matern15":
        base = Matern(np.ones(dimensions), (1e-3, 10.0), nu=1.5)
    elif kernel == "Matern25":
        base = Matern(np.ones(dimensions), (1e-3, 10.0), nu=2.5)
    else:
        raise ValueError(f"Unknown GP kernel: {kernel}")

    covariance = (
        ConstantKernel(1.0, (1e-3, 1e3)) * base
        + WhiteKernel(1e-4, (1e-8, 1.0))
    )
    model = GaussianProcessRegressor(
        kernel=covariance, normalize_y=False,
        n_restarts_optimizer=restarts, random_state=seed,
    )
    model.fit(X, target)
    return model, fitted_transform, target
