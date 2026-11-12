"""Model-based acquisition functions for *maximising* black-box scores.

A Gaussian Process supplies a predictive mean (mu) and uncertainty (sigma)
for candidate inputs. Acquisition scores order those *unobserved* inputs
before a costly evaluation; they are not measured outcomes.

Inputs mu, sigma and the observed incumbent (best) must use the SAME
target scale. In this project, that is sometimes a transformed output
scale, not the raw portal score. Large EI, PI or UCB values do not
establish that a candidate is a true optimum.

Each function accepts scalars or NumPy-compatible arrays and returns
scores which can be used to rank candidates. The three acquisitions
measure different things and their raw numerical values must not be
treated as interchangeable.
"""
from __future__ import annotations
import numpy as np
from scipy.stats import norm


def expected_improvement(mu, sigma, best, xi=0.0):
    """Calculate EI: E[max(Y - best - xi, 0)] under a Gaussian prediction.

    Parameters
    ----------
    mu, sigma : array-like
        GP predictive mean and standard deviation, both on its fitted scale.
    best : float
        Highest *observed* response on that same scale.
    xi : float
        Additional required improvement over the incumbent; positive values
        favour candidates promising a larger gain and may encourage exploration.

    Returns
    -------
    numpy.ndarray
        Expected positive improvement. This is a forecasted decision score,
        never an observed gain.

    Implementation
    --------------
    For normal predictive Y, z=(mu-best-xi)/sigma and
    EI=(mu-best-xi)*Phi(z) + sigma*phi(z). A tiny sigma floor avoids division
    by zero, including at previously evaluated locations. The floor is a
    numerical device, not a statement of real observation noise.
    """
    mu = np.asarray(mu, float)
    # The variance floor stabilises z at nearly deterministic predictions;
    # it is not evidence that evaluations themselves are noisy.
    sigma = np.maximum(np.asarray(sigma, float), 1e-12)
    # EI rewards both the chance of beating the incumbent and the size of the gain.
    improvement = mu - best - xi
    z = improvement / sigma
    return improvement * norm.cdf(z) + sigma * norm.pdf(z)


def probability_improvement(mu, sigma, best, xi=0.0):
    """Return P(Y > best + xi) under the GP's Gaussian prediction.

    Parameters match expected_improvement. PI considers *whether* a gain
    occurs, ignoring its possible size. A large PI thus need not imply the
    most valuable next experiment. Its result lies in [0, 1] and is a
    model-based probability, not a measured success rate.
    """
    sigma = np.maximum(np.asarray(sigma, float), 1e-12)
    # Unlike EI, PI measures the likelihood of any gain, not how large it might be.
    return norm.cdf((np.asarray(mu, float) - best - xi) / sigma)


def upper_confidence_bound(mu, sigma, beta=1.96):
    """Rank candidates with mu + beta*sigma.

    Parameters
    ----------
    mu, sigma : array-like
        Predicted response and standard deviation on a common GP target scale.
    beta : float
        Non-negative exploration weight by convention. Increasing beta
        rewards uncertainty more strongly; this helper does not enforce
        the convention or adapt beta over successive portal evaluations.

    Unlike EI and PI, UCB is not a probability or expected gain. Its value
    should only be compared with other UCB scores from a compatible fit.
    """
    # Raising beta increases the value assigned to uncertain, untested regions.
    return np.asarray(mu, float) + float(beta) * np.asarray(sigma, float)
