"""Fit F8 from 40 course observations and test later returns; verify F5 corner."""
from __future__ import annotations
import csv
from pathlib import Path
import numpy as np

F8_C = np.array([.10,.15,.13,.15,.80,.50,.20,.60], dtype=float)
F8_W = np.array([2,1,3,1,.5,1,2,.1], dtype=float)
F5_B = np.array([7.5,16,40,120], dtype=float)

def design_matrix(x):
    x = np.atleast_2d(np.asarray(x, dtype=float))
    if x.shape[1] != 8:
        raise ValueError("F8 needs eight coordinates")
    return np.column_stack([np.ones(len(x)), x, x*x])

def load_f8(root=None):
    root = Path(root) if root else Path(__file__).resolve().parents[2]
    path = root / "data/accumulated/function_8/observations_through_week12.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 52:
        raise ValueError(f"Expected 52 rows, found {len(rows)}")
    x = np.array([[float(r[f"x{i}"]) for i in range(1,9)] for r in rows])
    y = np.array([float(r["output"]) for r in rows])
    initial = np.array([r["is_initial"].lower() == "true" for r in rows])
    if initial.sum() != 40 or (~initial).sum() != 12:
        raise ValueError("Expected exactly 40 initial and 12 held-out rows")
    return x, y, initial

def recover_f8(root=None):
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
