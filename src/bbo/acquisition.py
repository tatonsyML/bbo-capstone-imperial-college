"""Acquisition scores for maximising an unknown black-box objective.

The GP supplies the predicted mean and standard deviation. An acquisition
function ranks *candidate inputs*, but does not observe their true outcomes.
"""
from __future__ import annotations
import numpy as np
from scipy.stats import norm


def expected_improvement(mu, sigma, best, xi=0.0):
    """Expected positive improvement over the current observed incumbent.

    Smaller xi favours exploiting a predicted high score; larger xi requires
    more improvement and often promotes exploration. Sigma is clipped to
    prevent division by zero at already explored locations.
    """
    mu = np.asarray(mu, float)
    sigma = np.maximum(np.asarray(sigma, float), 1e-12)
    # EI rewards both the chance of beating the incumbent and the size of the gain.
    improvement = mu - best - xi
    z = improvement / sigma
    return improvement * norm.cdf(z) + sigma * norm.pdf(z)


def probability_improvement(mu, sigma, best, xi=0.0):
    """Probability that a GP prediction improves on the incumbent."""
    sigma = np.maximum(np.asarray(sigma, float), 1e-12)
    # Unlike EI, PI measures the likelihood of any gain, not how large it might be.
    return norm.cdf((np.asarray(mu, float) - best - xi) / sigma)


def upper_confidence_bound(mu, sigma, beta=1.96):
    """Exploration/exploitation score = predicted mean + beta × uncertainty."""
    # Raising beta increases the value assigned to uncertain, untested regions.
    return np.asarray(mu, float) + float(beta) * np.asarray(sigma, float)
