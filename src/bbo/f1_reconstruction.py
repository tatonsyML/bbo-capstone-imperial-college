"""Retrospective F1 reconstruction using this repository's own observations.

A two-component Gaussian-modulated cosine *model family* was proposed in
separate working code. Its original derivation and authorship
have not been independently established. This experiment does not claim
to discover that family blindly or access the undisclosed programme oracle.

The six coefficients are fitted to the TEN course-provided F1 inputs and
scores in data/all_observations.csv. THIRTEEN personal portal returns
(rounds 1--13) are then checked without being used for coefficient fitting.
No peer data or external examples are fetched or used.

The starting guess is informed by the already proposed model family and
is not an uninformed global search; other solutions outside this basin
are not ruled out.

The proposed family sums two Gaussian envelopes multiplied by cosine
modulations. It supports narrow peaks, near-zero returns and oscillatory
sign changes. Log-magnitude fitting is used because F1 responses span
many orders of magnitude; signs and exact-zero returns are tested
separately from relative magnitudes.

The 13 later portal values are held out from the ten-point coefficient
fit, but this is not an unbiased search over all possible functional
families or a reproduction of the historical Round 11 selector.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


@dataclass(frozen=True)
class F1Parameters:
    """Six coefficients of the proposed two-component response model.

    The amplitudes determine component heights, centres locate peaks,
    the decay controls their narrowness and the frequency controls the
    cosine oscillation on each axis. These defaults are a reference
    hypothesis, not authenticated source-code constants.
    """

    minor_amplitude: float = 1.0
    major_amplitude: float = 2.0
    minor_centre: float = 0.5 - np.pi / 40.0
    major_centre: float = 0.55 + np.pi / 40.0
    decay: float = 1600.0
    frequency: float = 40.0

    @classmethod
    def from_array(cls, values: np.ndarray) -> "F1Parameters":
        """Convert the optimiser's ordered six coefficients into named fields."""
        return cls(*map(float, values))

    def as_array(self) -> np.ndarray:
        """Return coefficients in the order used by the nonlinear fit."""
        return np.array([
            self.minor_amplitude, self.major_amplitude,
            self.minor_centre, self.major_centre,
            self.decay, self.frequency,
        ], dtype=float)


# Published here as an explicit reference hypothesis, not as authenticated
# source coefficients for the undisclosed oracle.
REFERENCE = F1Parameters()


def predict(x: np.ndarray, params: F1Parameters = REFERENCE) -> np.ndarray:
    """Predict scores for two-input vectors using the proposed F1 family.

    x has shape (n, 2); params supplies component amplitudes, centres,
    decay and frequency. Returns one predicted score per input row.

    Each response term multiplies an exp(-decay * squared-distance)
    envelope by two cosine factors. This can create extremely narrow
    signal regions and numerical underflow far from either peak.
    Predictions are *model* values, never new course-portal evaluations.
    """
    x = np.asarray(x, dtype=float)
    if x.ndim != 2 or x.shape[1] != 2:
        raise ValueError("F1 expects a two-column input matrix.")
    # A small and a large Gaussian-modulated component contribute to the
    # final score. This is a hypothesis about the shape, not an oracle call.
    value = np.zeros(len(x), dtype=float)
    for amplitude, centre in (
        (params.minor_amplitude, params.minor_centre),
        (params.major_amplitude, params.major_centre),
    ):
        # Both input axes share the reference centre in each term.
        # The Gaussian envelope is local; cosines permit sign changes.
        delta = x - centre
        value += (
            amplitude
            * np.exp(-params.decay * np.sum(delta * delta, axis=1))
            * np.cos(params.frequency * delta[:, 0])
            * np.cos(params.frequency * delta[:, 1])
        )
    return value


def load_own_observations(root: Path | None = None):
    """Load 10 initial F1 records and 13 personal returned evaluations.

    Returns X with shape (23, 2), y with shape (23,), and a Boolean
    initial-row mask. Source flags and record counts are validated to
    prevent leakage of later portal results into the training split.
    """
    root = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    path = root / "data" / "all_observations.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = [row for row in csv.DictReader(stream) if row["function"] == "1"]
    if len(rows) != 23:
        raise ValueError(f"Expected 23 F1 observations; found {len(rows)}")
    x = np.array([[float(r["x1"]), float(r["x2"])] for r in rows])
    y = np.array([float(r["output"]) for r in rows])
    # Only mask-True rows enter coefficient fitting; the other thirteen
    # measured results are reserved for the later numerical check.
    initial = np.array([r["round"] == "0" for r in rows], dtype=bool)
    if int(initial.sum()) != 10 or int((~initial).sum()) != 13:
        raise ValueError("Expected 10 supplied F1 rows and 13 personal evaluations.")
    if any(r["source"] != ("course_initial" if b else "personal_portal")
           for r, b in zip(rows, initial)):
        raise ValueError("F1 observation provenance does not match the expected flags.")
    return x, y, initial


def fit_initial_only(x: np.ndarray, y: np.ndarray) -> F1Parameters:
    """Fit an already proposed six-parameter family on ten initial rows.

    Require exactly X shape (10, 2), y shape (10,), and nonzero targets.
    Compare log(abs(prediction)) with log(abs(observation)) to balance
    values separated by hundreds of orders of magnitude; a 1e-300
    numerical floor prevents taking log(0). Sign agreement must be
    checked separately because magnitude fitting discards signs.

    Optimisation uses informed parameter bounds and starting values,
    so this is a local hypothesis test rather than blind equation
    discovery. Return fitted F1Parameters only after convergence, sign
    and relative-error checks against those ten observations.
    """
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.shape != (10, 2) or y.shape != (10,):
        raise ValueError("Fit requires precisely the ten initial F1 observations.")
    if np.any(y == 0):
        raise ValueError("Log-magnitude fitting requires non-zero initial outputs.")

    # Informed initial coefficients and finite bounds restrict the
    # solver to the chosen family, not all possible hidden formulas.
    start = np.array([1.0, 2.0, 0.42, 0.63, 1500.0, 40.0])
    lower = np.array([0.01, 0.01, 0.30, 0.55, 500.0, 20.0])
    upper = np.array([10.0, 10.0, 0.50, 0.70, 3000.0, 60.0])

    def residual(coefficients):
        """Log-magnitude discrepancy; prediction signs are checked later."""
        estimate = predict(x, F1Parameters.from_array(coefficients))
        return np.log(np.maximum(np.abs(estimate), 1e-300)) - np.log(np.abs(y))

    # Jacobian-based scaling and tight tolerances resolve a very narrow
    # response pattern without letting a single large return dominate.
    result = least_squares(
        residual, start, bounds=(lower, upper),
        x_scale="jac", max_nfev=3000,
        ftol=1e-13, xtol=1e-13, gtol=1e-13,
    )
    fitted = F1Parameters.from_array(result.x)
    estimate = predict(x, fitted)
    if not result.success or np.any(np.sign(estimate) != np.sign(y)):
        raise AssertionError("Local optimisation failed or yielded incorrect signs.")
    if np.max(np.abs(estimate / y - 1.0)) > 1e-10:
        raise AssertionError("The proposed family did not explain the ten starting rows.")
    return fitted


def validate_held_out(x: np.ndarray, y: np.ndarray, params: F1Parameters) -> dict:
    """Validate predictions on the thirteen untouched personal F1 returns.

    Check numerical zero exactly, sign agreement on nonzero scores and
    relative errors without the fitting-time log floor. Report both
    maximum nonzero relative error and maximum absolute error.
    Successful held-out prediction supports the specified *family*;
    it does not certify the hidden source over all possible inputs.
    """
    predictions = predict(x, params)
    # A relative error is undefined when actual y=0, so zero returns
    # must pass a separate check rather than being divided through.
    nonzero = y != 0
    if not np.all(predictions[~nonzero] == 0):
        raise AssertionError("A recorded zero was not reproduced as zero.")
    if np.any(np.sign(predictions[nonzero]) != np.sign(y[nonzero])):
        raise AssertionError("A non-zero output sign was not reproduced.")
    relative = np.abs(predictions[nonzero] / y[nonzero] - 1.0)
    max_relative = float(np.max(relative)) if len(relative) else 0.0
    if max_relative > 1e-10:
        raise AssertionError(f"Held-out relative error too high: {max_relative:.3e}")
    return {
        "count": len(y),
        "zero_count": int((~nonzero).sum()),
        "max_relative_error_nonzero": max_relative,
        "max_absolute_error": float(np.max(np.abs(predictions - y))),
    }


def main() -> None:
    """Display the ten-record fit and held-out thirteen-score comparison."""
    x, y, initial = load_own_observations()
    fitted = fit_initial_only(x[initial], y[initial])
    result = validate_held_out(x[~initial], y[~initial], fitted)
    print("Fit source: 10 course-supplied F1 observations only")
    print("Model family: informed by separate working code; not blind discovery")
    for name, value in vars(fitted).items():
        print(f"{name}: {value:.16g}")
    print(f"Later portal evaluations checked: {result['count']}")
    print(f"Recorded zero outputs matched: {result['zero_count']}")
    print(f"Max held-out nonzero relative error: {result['max_relative_error_nonzero']:.3e}")
    print(f"Max held-out absolute error: {result['max_absolute_error']:.3e}")
    # The reported R11 point was already submitted historically: this
    # prints its reconstructed score, not another portal measurement.
    candidate = np.array([[0.628540, 0.628540]])
    print(f"Predicted six-decimal candidate score: {predict(candidate, fitted)[0]:.16f}")


if __name__ == "__main__":
    main()
