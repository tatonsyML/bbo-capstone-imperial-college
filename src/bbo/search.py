"""Candidate generation and legal-domain utilities for capstone models."""
from __future__ import annotations
import numpy as np
from scipy.stats import qmc


def portal_string(x):
    """Format a proposed input as the course's six-decimal dash-separated text."""
    # Formatting a candidate for submission never evaluates the hidden function.
    return "-".join(f"{float(value):.6f}" for value in x)


def sobol_points(d, n_power=15, seed=0):
    """Reproducible low-discrepancy pool; 2**n_power input points."""
    candidates = qmc.Sobol(d=d, scramble=True, seed=seed).random_base2(n_power)
    # Keep generated locations inside the six-decimal portal domain.
    return np.clip(candidates, 1e-6, 0.999999)


def trust_region_bounds(center, length):
    """Restrict search around a measured incumbent, respecting portal bounds.

    This static box is NOT the full adaptive TuRBO trust-region mechanism.
    """
    # A fixed local search box is clipped at the permitted coordinate boundaries.
    centre = np.asarray(center, float)
    return np.maximum(0.0, centre - length / 2), np.minimum(
        0.999999, centre + length / 2
    )


def scale_to_box(unit_points, lower, upper):
    """Map Sobol points from [0,1]^d into a chosen feasible local box."""
    unit = np.asarray(unit_points, float)
    lo = np.asarray(lower, float)
    hi = np.asarray(upper, float)
    return lo + (hi - lo) * unit
