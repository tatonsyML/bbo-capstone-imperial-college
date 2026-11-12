"""Candidate-space helpers shared by the GP optimisation experiments.

Every dimension uses the capstone's six-decimal submission range
[0, 0.999999]. Proposed vectors have not been evaluated by the portal.
The Sobol generator is repeatable for a fixed seed but remains a *sample*
of the search space, not a guarantee of finding the maximum.

The local bounding-box utilities implement only a static trust-region
idea. They are not a complete TuRBO optimiser and never update the
region in response to real new evaluation feedback.
"""
from __future__ import annotations
import numpy as np
from scipy.stats import qmc


def portal_string(x):
    """Render a numeric candidate in the portal's dash-separated format.

    Coordinates are formatted to six decimal places in their supplied
    order. This helper neither clips nor validates the input vector and
    never assigns a portal result; callers are responsible for bounds.
    """
    # Formatting a candidate for submission never evaluates the hidden function.
    return "-".join(f"{float(value):.6f}" for value in x)


def sobol_points(d, n_power=15, seed=0):
    """Generate a scrambled Sobol candidate pool of shape (2**n_power, d).

    Parameters
    ----------
    d : int
        Number of input coordinates for the selected function.
    n_power : int
        The base-two exponent used by Sobol random_base2. A power-of-two
        count preserves useful balance properties of the Sobol sequence.
    seed : int
        Scrambling seed, enabling repeatable comparison between methods.

    The generated pool is clipped into the six-decimal coordinate domain.
    The coordinates are still *unobserved* suggestions, not portal scores.
    """
    # A single seeded low-discrepancy design limits differences caused by
    # random candidate draws when comparing acquisition functions or kernels.
    candidates = qmc.Sobol(d=d, scramble=True, seed=seed).random_base2(n_power)
    # Keep generated locations inside the six-decimal portal domain.
    return np.clip(candidates, 1e-6, 0.999999)


def trust_region_bounds(center, length):
    """Return coordinate-wise bounds for a fixed-width local search box.

    centre : array-like
        Normally the best *observed* vector, not a modelled optimum.
    length : float
        Full side length, before clipping to the legal [0, 0.999999] domain.

    Returns a pair of NumPy lower/upper vectors. A box at a domain edge
    loses width on the clipped side. This helper does not shift the box
    back towards the interior, weight axes by GP lengthscales, count
    improvements, expand/shrink on feedback or restart. It is NOT TuRBO.
    """
    # A fixed local search box is clipped at the permitted coordinate boundaries.
    centre = np.asarray(center, float)
    return np.maximum(0.0, centre - length / 2), np.minimum(
        0.999999, centre + length / 2
    )


def scale_to_box(unit_points, lower, upper):
    """Affinely map unit-cube candidates into a chosen local box.

    Each coordinate uses lower + (upper-lower)*unit_point. Arrays
    broadcast across candidate rows. This preserves the original order
    and does not evaluate or score any of the mapped locations.
    """
    unit = np.asarray(unit_points, float)
    lo = np.asarray(lower, float)
    hi = np.asarray(upper, float)
    return lo + (hi - lo) * unit
