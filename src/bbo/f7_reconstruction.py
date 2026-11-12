"""Positive Hartmann-6 hypothesis for capstone Function 7.

This formula represents a reconstructed mathematical family, not a copy of the
official oracle source. The coefficients are those recorded by the project's
earlier structural investigation/visualisation. The test below checks all
published personal + course observations. It is retrospective, NOT a claim
that all parameters were known before each historic round.

The positive Hartmann-6 hypothesis sums four exponentially weighted
components. Each component measures a weighted squared distance from
a six-dimensional reference centre. Larger returned values are better,
consistent with the capstone's maximisation objective, unlike many
standard Hartmann-6 benchmark conventions.

The original prospective Round 12 prediction is documented separately
in the historical research. This module checks the proposed model
retrospectively against all 43 published observations, not against new
independent samples. Agreement cannot authenticate the undisclosed
function globally.
"""
from __future__ import annotations

import numpy as np
from .evidence_audit import read_csv, root_path

# A[k, j]: component k's sensitivity to errors in coordinate j.
# Larger positive weights make a given dimension's peak narrower.
A = np.array([
    [10, 3, 17, 3.5, 1.7, 8],
    [0.05, 10, 17, 0.1, 8, 14],
    [3, 3.5, 1.7, 10, 17, 8],
    [17, 8, 0.05, 10, 0.1, 14],
], dtype=float)
# P[k, :] contains the six-coordinate centre for component k.
# These are parameters of a proposed family, not original oracle source.
P = np.array([
    [0.1312, 0.1696, 0.5569, 0.0124, 0.8283, 0.5886],
    [0.2329, 0.4135, 0.8307, 0.3736, 0.1004, 0.9991],
    [0.2348, 0.1451, 0.3522, 0.2883, 0.3047, 0.6650],
    [0.4047, 0.8828, 0.8732, 0.5743, 0.1091, 0.0381],
], dtype=float)
# Positive component amplitudes, matching the maximisation convention.
ALPHA = np.array([1.0, 1.2, 3.0, 3.2], dtype=float)


def f7_hypothesis(x):
    """Evaluate the reconstructed positive Hartmann-6 family.

    Parameters
    ----------
    x : array-like of shape (n, 6), or a single six-number vector
        Candidate inputs. Each candidate is evaluated by the *model*.

    Returns
    -------
    numpy.ndarray
        One predicted score per candidate. A prediction is not a returned
        portal score, nor proof of identity with the hidden function.

    Mathematical form
    -----------------
    For each of four components k, compute
        d_k(x) = sum_j A[k,j] * (x[j] - P[k,j])**2.
    Combine them as sum_k ALPHA[k] * exp(-d_k(x)).
    Broadcasting the candidate rows against four component centres
    avoids per-row Python loops and preserves the six input dimensions.
    """
    x = np.atleast_2d(np.asarray(x, dtype=float))
    if x.shape[1] != 6:
        raise ValueError("F7 requires six numeric coordinates.")
    # Shapes: (n, 1, 6) - (1, 4, 6) -> (n, 4, 6), one difference
    # vector per candidate and component centre. Larger A weights
    # penalise deviation more strongly before the exponential decay.
    difference = x[:, None, :] - P[None, :, :]
    distances = np.sum(A[None, :, :] * difference**2, axis=2)
    # Sum the four positive weighted responses for each candidate.
    # No observations are appended and no private portal call occurs.
    return np.sum(ALPHA[None, :] * np.exp(-distances), axis=1)


def validate_recorded_f7(root=None):
    """Compare the reconstructed family with all 43 recorded F7 outcomes.

    root optionally selects a repository or isolated fixture directory.
    Load 30 course-provided plus 13 personal observations, predict their
    stored vectors, and require a maximum absolute error at most 3e-14.

    Returns a dictionary with record count, worst discrepancy, R11 and
    R12 model predictions, and the actual R12 return. Round identifiers
    are read from source records rather than inferred from array positions.

    This is a record-consistency test of a reconstructed model family, not
    a fresh held-out sample proving predictive performance everywhere.
    The originally documented pre-result R12 forecast is distinct from
    this later fit/validation procedure.
    """
    # Use the canonical 43 known F7 outcomes. Model-generated values or
    # peer observations are never added to this source record.
    rows = [
        r for r in read_csv(root_path(root) / "data" / "all_observations.csv")
        if int(r["function"]) == 7
    ]
    if len(rows) != 43:
        raise AssertionError(f"Expected 43 F7 observations; found {len(rows)}")
    x = np.array([[float(r[f"x{i}"]) for i in range(1, 7)] for r in rows])
    actual = np.array([float(r["output"]) for r in rows])
    # This checks a published record, not independent performance on new inputs.
    predicted = f7_hypothesis(x)
    max_error = float(np.max(np.abs(predicted - actual)))
    if max_error > 3e-14:
        raise AssertionError(f"F7 model no longer reproduces records: {max_error:g}")
    # Do not assume that the round number equals a zero-based row offset:
    # the initial 30 observations precede the personal results.
    r11 = next(i for i, r in enumerate(rows) if r["round"] == "11")
    r12 = next(i for i, r in enumerate(rows) if r["round"] == "12")
    return {
        "records": len(rows),
        "max_absolute_error": max_error,
        "round11_predicted": float(predicted[r11]),
        "round12_predicted": float(predicted[r12]),
        "round12_actual": float(actual[r12]),
    }


if __name__ == "__main__":
    # This entry point prints a numerical comparison; it performs no
    # portal evaluation and does not change the published data.
    for key, value in validate_recorded_f7().items():
        print(f"{key}: {value}")
