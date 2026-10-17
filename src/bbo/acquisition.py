from __future__ import annotations
import numpy as np
from scipy.stats import norm


def expected_improvement(mu, sigma, best, xi=0.0):
    mu=np.asarray(mu,float); sigma=np.maximum(np.asarray(sigma,float),1e-12)
    imp=mu-best-xi; z=imp/sigma
    return imp*norm.cdf(z)+sigma*norm.pdf(z)


def probability_improvement(mu, sigma, best, xi=0.0):
    sigma=np.maximum(np.asarray(sigma,float),1e-12)
    return norm.cdf((np.asarray(mu,float)-best-xi)/sigma)


def upper_confidence_bound(mu, sigma, beta=1.96):
    return np.asarray(mu,float)+float(beta)*np.asarray(sigma,float)
