"""Positive Hartmann-6 hypothesis for capstone Function 7.

This formula represents a reconstructed mathematical family, not a copy of the
official oracle source. The coefficients are those recorded by the project's
earlier structural investigation/visualisation. The test below checks all
published personal + course observations. It is retrospective, NOT a claim
that all parameters were known before each historic round.
"""
from __future__ import annotations

import numpy as np
from .evidence_audit import read_csv, root_path

A = np.array([
    [10, 3, 17, 3.5, 1.7, 8],
    [0.05, 10, 17, 0.1, 8, 14],
    [3, 3.5, 1.7, 10, 17, 8],
    [17, 8, 0.05, 10, 0.1, 14],
], dtype=float)
P = np.array([
    [0.1312, 0.1696, 0.5569, 0.0124, 0.8283, 0.5886],
    [0.2329, 0.4135, 0.8307, 0.3736, 0.1004, 0.9991],
    [0.2348, 0.1451, 0.3522, 0.2883, 0.3047, 0.6650],
    [0.4047, 0.8828, 0.8732, 0.5743, 0.1091, 0.0381],
], dtype=float)
ALPHA = np.array([1.0, 1.2, 3.0, 3.2], dtype=float)


def f7_hypothesis(x):
    """Predict F7 values for an (n, 6) matrix of inputs."""
    x = np.atleast_2d(np.asarray(x, dtype=float))
    if x.shape[1] != 6:
        raise ValueError("F7 requires six numeric coordinates.")
    # Broadcasting compares each candidate with four Hartmann reference centres.
    difference = x[:, None, :] - P[None, :, :]
    distances = np.sum(A[None, :, :] * difference**2, axis=2)
    return np.sum(ALPHA[None, :] * np.exp(-distances), axis=1)


def validate_recorded_f7(root=None):
    """Compare with 30 initial + 13 personal observed scores.

    This is a numerical consistency test, not an unbiased validation set:
    the original construction and parameter-selection history is separate.
    """
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
    for key, value in validate_recorded_f7().items():
        print(f"{key}: {value}")
