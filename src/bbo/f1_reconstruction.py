"""Retrospective F1 reconstruction using this repository's own observations.

A two-component Gaussian-modulated cosine *model family* was proposed in
separately recovered working code. Its original derivation and authorship
have not been independently established. This experiment does not claim
to discover that family blindly or access the undisclosed programme oracle.

The six coefficients are fitted to the TEN course-provided F1 inputs and
scores in data/all_observations.csv. THIRTEEN personal portal returns
(rounds 1--13) are then checked without being used for coefficient fitting.
No peer data or external examples are fetched or used.

The starting guess is informed by the already proposed model family and
is not an uninformed global search; other solutions outside this basin
are not ruled out.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares


@dataclass(frozen=True)
class F1Parameters:
    minor_amplitude: float = 1.0
    major_amplitude: float = 2.0
    minor_centre: float = 0.5 - np.pi / 40.0
    major_centre: float = 0.55 + np.pi / 40.0
    decay: float = 1600.0
    frequency: float = 40.0

    @classmethod
    def from_array(cls, values: np.ndarray) -> "F1Parameters":
        return cls(*map(float, values))

    def as_array(self) -> np.ndarray:
        return np.array([
            self.minor_amplitude, self.major_amplitude,
            self.minor_centre, self.major_centre,
            self.decay, self.frequency,
        ], dtype=float)


# Published here as an explicit reference hypothesis, not as authenticated
# source coefficients for the undisclosed oracle.
REFERENCE = F1Parameters()


def predict(x: np.ndarray, params: F1Parameters = REFERENCE) -> np.ndarray:
    """Evaluate two separable Gabor-type components at shape (n, 2)."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 2 or x.shape[1] != 2:
        raise ValueError("F1 expects a two-column input matrix.")
    value = np.zeros(len(x), dtype=float)
    for amplitude, centre in (
        (params.minor_amplitude, params.minor_centre),
        (params.major_amplitude, params.major_centre),
    ):
        delta = x - centre
        value += (
            amplitude
            * np.exp(-params.decay * np.sum(delta * delta, axis=1))
            * np.cos(params.frequency * delta[:, 0])
            * np.cos(params.frequency * delta[:, 1])
        )
    return value


def load_own_observations(root: Path | None = None):
    """Read F1, separating initial samples (round 0) from personal portal returns."""
    root = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    path = root / "data" / "all_observations.csv"
    with path.open(newline="", encoding="utf-8") as stream:
        rows = [row for row in csv.DictReader(stream) if row["function"] == "1"]
    if len(rows) != 23:
        raise ValueError(f"Expected 23 F1 observations; found {len(rows)}")
    x = np.array([[float(r["x1"]), float(r["x2"])] for r in rows])
    y = np.array([float(r["output"]) for r in rows])
    initial = np.array([r["round"] == "0" for r in rows], dtype=bool)
    if int(initial.sum()) != 10 or int((~initial).sum()) != 13:
        raise ValueError("Expected 10 supplied F1 rows and 13 personal evaluations.")
    if any(r["source"] != ("course_initial" if b else "personal_portal")
           for r, b in zip(rows, initial)):
        raise ValueError("F1 observation provenance does not match the expected flags.")
    return x, y, initial


def fit_initial_only(x: np.ndarray, y: np.ndarray) -> F1Parameters:
    """Fit the six coefficients in the *already proposed* family.

    Non-zero scores range over hundreds of orders of magnitude. Log-magnitude
    residuals avoid allowing the single largest score to dominate the fit.
    Signs are checked separately after fitting. The informed starting guess
    and bounds restrict this to a local structural test, not blind discovery.
    """
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.shape != (10, 2) or y.shape != (10,):
        raise ValueError("Fit requires precisely the ten initial F1 observations.")
    if np.any(y == 0):
        raise ValueError("Log-magnitude fitting requires non-zero initial outputs.")

    start = np.array([1.0, 2.0, 0.42, 0.63, 1500.0, 40.0])
    lower = np.array([0.01, 0.01, 0.30, 0.55, 500.0, 20.0])
    upper = np.array([10.0, 10.0, 0.50, 0.70, 3000.0, 60.0])

    def residual(coefficients):
        estimate = predict(x, F1Parameters.from_array(coefficients))
        return np.log(np.maximum(np.abs(estimate), 1e-300)) - np.log(np.abs(y))

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
    """Check held-out personal evaluations without rounding or floor tolerance."""
    predictions = predict(x, params)
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
    x, y, initial = load_own_observations()
    fitted = fit_initial_only(x[initial], y[initial])
    result = validate_held_out(x[~initial], y[~initial], fitted)
    print("Fit source: 10 course-supplied F1 observations only")
    print("Model family: informed by separately recovered code; not blind discovery")
    for name, value in vars(fitted).items():
        print(f"{name}: {value:.16g}")
    print(f"Later portal evaluations checked: {result['count']}")
    print(f"Recorded zero outputs matched: {result['zero_count']}")
    print(f"Max held-out nonzero relative error: {result['max_relative_error_nonzero']:.3e}")
    print(f"Max held-out absolute error: {result['max_absolute_error']:.3e}")
    candidate = np.array([[0.628540, 0.628540]])
    print(f"Predicted six-decimal candidate score: {predict(candidate, fitted)[0]:.16f}")


if __name__ == "__main__":
    main()
