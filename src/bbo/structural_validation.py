"""Reproduce F8 from 40 starting points and check 13 later observations.

F8 basis: intercept + eight linear + eight quadratic terms (17 parameters).
F5 reconstructed power-sum equation was identified *after* the R10 query.
This code does not claim access to any hidden source implementation.
"""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np

# Expected F8 vertex c in 10 - sum(w[j] * (x[j] - c[j])**2).
F8_C = np.array([.10,.15,.13,.15,.80,.50,.20,.60], dtype=float)
# Positive F8 curvature weights; x3 weight is 30 times x8 weight.
F8_W = np.array([2,1,3,1,.5,1,2,.1], dtype=float)
# F5 power-sum targets: 0.01*sum_k((sum_j((4*x[j])**k)-b[k])**2).
F5_B = np.array([7.5,16,40,120], dtype=float)

def design_matrix(x):
    """Build 17 F8 regression columns."""
    x = np.atleast_2d(np.asarray(x, dtype=float))
    if x.shape[1] != 8:
        raise ValueError("F8 needs eight coordinates")
    return np.column_stack([np.ones(len(x)), x, x*x])

def load_f8(root=None):
    """Load the original 40 and later 13 portal scores."""
    root = Path(root) if root else Path(__file__).resolve().parents[2]
    path = root / "data/accumulated/function_8/observations_through_week13.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 53:
        raise ValueError(f"Expected 53 rows, found {len(rows)}")
    x = np.array([[float(r[f"x{i}"]) for i in range(1,9)] for r in rows])
    y = np.array([float(r["output"]) for r in rows])
    initial = np.array([r["is_initial"].lower() == "true" for r in rows])
    if initial.sum() != 40 or (~initial).sum() != 13:
        raise ValueError("Expected exactly 40 initial and 13 held-out rows")
    return x, y, initial

def recover_f8(root=None):
    """Fit 40 points and independently predict the later 13."""
    x, y, initial = load_f8(root)
    coefficients, _, rank, _ = np.linalg.lstsq(design_matrix(x[initial]), y[initial], rcond=None)
    if rank != 17:
        raise ValueError(f"F8 initial design has rank {rank} instead of 17")
    prediction = design_matrix(x[~initial]) @ coefficients
    linear, quadratic = coefficients[1:9], coefficients[9:17]
    centre = -linear/(2*quadratic)
    weights = -quadratic
    peak = float(coefficients[0] - np.sum(linear*linear/(4*quadratic)))
    return dict(rank=int(rank), centre=centre, weights=weights,
                maximum=peak, initial_count=int(initial.sum()),
                holdout_count=int((~initial).sum()),
                max_holdout_error=float(np.max(np.abs(prediction-y[~initial]))))

def f5_at(x):
    """Evaluate the retrospectively recovered F5 equation at legal coordinates."""
    x = np.asarray(x, dtype=float)
    if x.shape != (4,):
        raise ValueError("F5 needs four coordinates")
    return float(.01*np.sum((np.array([np.sum((4*x)**k) for k in range(1,5)])-F5_B)**2))

def main():
    r = recover_f8()
    print("F8 design rank:", r["rank"], "/17")
    print("Initial observations:", r["initial_count"], "held-out portal queries:", r["holdout_count"])
    print("Recovered centre:", np.array2string(r["centre"], precision=12))
    print("Recovered weights:", np.array2string(r["weights"], precision=12))
    print("Fitted maximum:", f'{r["maximum"]:.15f}')
    print("Max later-output absolute error:", f'{r["max_holdout_error"]:.3e}')
    print("F5 at permitted corner:", f'{f5_at(np.full(4,.999999)):.12f}')
    np.testing.assert_allclose(r["centre"], F8_C, rtol=0, atol=1e-12)
    np.testing.assert_allclose(r["weights"], F8_W, rtol=0, atol=1e-12)
    assert abs(r["maximum"]-10) < 1e-12
    assert r["max_holdout_error"] < 2e-14
    assert abs(f5_at(np.full(4,.999999))-8662.405001248297) < 1e-9

if __name__ == "__main__":
    main()
