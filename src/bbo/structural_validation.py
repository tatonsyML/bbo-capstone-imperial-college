"""Validate interpretable mathematical reconstructions for F8 and F5.

F8 uses an additive quadratic model with 17 coefficients: an intercept,
eight linear effects and eight squared effects. Fit it using ONLY the
40 course-provided starting observations and evaluate predictions on the
13 subsequent portal returns without using them for parameter estimation.

A full-rank design is necessary for identifying those 17 coefficients.
The fitted vertex and curvature weights follow from elementary calculus,
but a proved maximum of the *fitted equation* does not prove that the
undisclosed objective has the same global maximum or form.

F5 uses a different, interacting power-sum formula reconstructed AFTER
the Round 10 boundary decision. The function f5_at evaluates that
retrospective hypothesis; it did not generate the original query.

The two checks read canonical measured data or supplied coefficients
without invoking a hidden evaluation service or adding observations.
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
    """Construct the 17-column F8 additive quadratic regression basis.

    Accepts one length-eight point or an (n, 8) matrix and returns
    [1, x1,...,x8, x1**2,...,x8**2] per row. Interaction terms are
    intentionally absent, so the model is separable across dimensions.
    That assumption aids interpretability but must be checked against
    observations rather than presumed true of the hidden function.
    """
    x = np.atleast_2d(np.asarray(x, dtype=float))
    if x.shape[1] != 8:
        raise ValueError("F8 needs eight coordinates")
    # The exact column order matches recover_f8's intercept, linear
    # coefficient slice [1:9] and quadratic slice [9:17].
    return np.column_stack([np.ones(len(x)), x, x*x])

def load_f8(root=None):
    """Load 53 measured F8 points, preserving their initial/holdout split.

    Returns (X, y, initial_mask) with 40 True and 13 False rows. The
    published is_initial field defines which scores the regression may
    train on. The later 13 observations remain available only for the
    retrospective holdout error calculation.
    """
    root = Path(root) if root else Path(__file__).resolve().parents[2]
    path = root / "data/accumulated/function_8/observations_through_week13.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 53:
        raise ValueError(f"Expected 53 rows, found {len(rows)}")
    x = np.array([[float(r[f"x{i}"]) for i in range(1,9)] for r in rows])
    y = np.array([float(r["output"]) for r in rows])
    # A source-provided flag, not the order of CSV rows, controls the
    # split. Training on later portal returns would inflate accuracy.
    initial = np.array([r["is_initial"].lower() == "true" for r in rows])
    if initial.sum() != 40 or (~initial).sum() != 13:
        raise ValueError("Expected exactly 40 initial and 13 held-out rows")
    return x, y, initial

def recover_f8(root=None):
    """Fit F8's 17 coefficients on initial data and assess later returns.

    Least squares is applied to the forty initial points only; a
    full-column-rank check prevents claiming a uniquely identified fit
    when the basis has redundant columns. The subsequent thirteen actual
    scores are held out, and maximum absolute prediction error is reported.

    For fitted terms a_j*x_j + b_j*x_j**2:
      centre_j = -a_j/(2*b_j),
      curvature weight_j = -b_j,
      peak = intercept - sum_j(a_j**2/(4*b_j)).

    Negative quadratic coefficients make the recovered additive model
    concave. Its stationary point is an analytical model maximum, not
    a certified optimum of the undisclosed black-box source.

    Returns rank, centre, weights, fitted maximum, sample counts and
    maximum absolute holdout error as dictionary fields.
    """
    x, y, initial = load_f8(root)
    # Only the original 40 rows determine the coefficient vector.
    # Rank 17 means the chosen 17-column design is identifiable; it
    # does not establish that the real source equation is quadratic.
    coefficients, _, rank, _ = np.linalg.lstsq(design_matrix(x[initial]), y[initial], rcond=None)
    if rank != 17:
        raise ValueError(f"F8 initial design has rank {rank} instead of 17")
    # Score the thirteen future inputs using the *already fitted* model.
    # Their actual returned y values enter only the following error metric.
    prediction = design_matrix(x[~initial]) @ coefficients
    # The derivative of a_j*x_j+b_j*x_j² vanishes at -a_j/(2*b_j).
    # Each fitted -b_j is a curvature/penalty weight for that coordinate.
    linear, quadratic = coefficients[1:9], coefficients[9:17]
    centre = -linear/(2*quadratic)
    weights = -quadratic
    peak = float(coefficients[0] - np.sum(linear*linear/(4*quadratic)))
    return dict(rank=int(rank), centre=centre, weights=weights,
                maximum=peak, initial_count=int(initial.sum()),
                holdout_count=int((~initial).sum()),
                max_holdout_error=float(np.max(np.abs(prediction-y[~initial]))))

def f5_at(x):
    """Evaluate the F5 power-sum model at four supplied coordinates.

    For each power k=1..4 calculate sum_j(4*x_j)**k, subtract the
    corresponding F5_B target, square and add the four penalties with
    coefficient 0.01. The power sums couple all four coordinates, unlike
    the additive F8 model.

    The caller must ensure legal portal bounds: only the input shape is
    validated here. This is a retrospective *modelled* score and does
    not call the unknown F5 objective or reproduce its R10 decision.
    """
    x = np.asarray(x, dtype=float)
    if x.shape != (4,):
        raise ValueError("F5 needs four coordinates")
    # Squared deviations from each target produce a non-negative
    # modelled score; the original portal values remain separate data.
    return float(.01*np.sum((np.array([np.sum((4*x)**k) for k in range(1,5)])-F5_B)**2))

def main():
    """Print and numerically check the F8 40/13 split and F5 corner score."""
    r = recover_f8()
    print("F8 design rank:", r["rank"], "/17")
    print("Initial observations:", r["initial_count"], "held-out portal queries:", r["holdout_count"])
    print("Fitted centre:", np.array2string(r["centre"], precision=12))
    print("Fitted weights:", np.array2string(r["weights"], precision=12))
    print("Fitted maximum:", f'{r["maximum"]:.15f}')
    print("Max later-output absolute error:", f'{r["max_holdout_error"]:.3e}')
    print("F5 at permitted corner:", f'{f5_at(np.full(4,.999999)):.12f}')
    # Guard the published model parameters, held-out agreement and the
    # legal F5 corner. Tests validate arithmetic, not private source code.
    np.testing.assert_allclose(r["centre"], F8_C, rtol=0, atol=1e-12)
    np.testing.assert_allclose(r["weights"], F8_W, rtol=0, atol=1e-12)
    assert abs(r["maximum"]-10) < 1e-12
    assert r["max_holdout_error"] < 2e-14
    assert abs(f5_at(np.full(4,.999999))-8662.405001248297) < 1e-9

if __name__ == "__main__":
    main()
