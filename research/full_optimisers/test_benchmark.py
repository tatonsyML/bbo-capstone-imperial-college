"""Unit tests that do not require installing official HEBO or BoTorch.

These tests check the capstone-specific logic, not algorithm performance.
The full engines must be installed to execute the comparison itself.
"""
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchmark import (TurboState, build_f8_simulator, f8_design,
                       simulated_f8_score, portal_point, portal_text, compare_f8)

ROOT = Path(__file__).resolve().parents[2]


def test_f8_original_40_predict_thirteen_returned_points():
    x, y, coef, meta = build_f8_simulator(ROOT)
    assert x.shape == (40, 8)
    assert y.shape == (40,)
    assert meta["held_out_points"] == 13
    assert meta["max_holdout_error"] < 2e-14
    assert abs(simulated_f8_score(coef, np.array([.10,.15,.13,.15,.8,.5,.2,.6])) - 10) < 1e-12


def test_simulated_f8_score_returns_python_float():
    """Avoid deprecated NumPy array-to-scalar conversion."""
    _, _, coefficients, _ = build_f8_simulator(ROOT)
    query = np.array([.10, .15, .13, .15, .8, .5, .2, .6])
    assert type(simulated_f8_score(coefficients, query)) is float


def test_f8_design_has_seventeen_features():
    assert f8_design(np.zeros((3, 8))).shape == (3, 17)


def test_success_streak_expands_the_trust_region():
    state = TurboState(dim=8, best_value=5)
    for value in (6, 7, 8):
        state.update(value)
    assert state.length == 1.6
    assert state.success_counter == 0


def test_failure_streak_shrinks_the_trust_region():
    state = TurboState(dim=8, best_value=5)
    for _ in range(8):
        state.update(4)
    assert state.length == 0.4
    assert state.failure_counter == 0


def test_portal_rounding_and_bounds():
    point = portal_point(np.array([1.01, -.2, .1234567]))
    assert portal_text(point) == "0.999999-0.000000-0.123457"


def test_comparison_fails_without_both_runs(tmp_path):
    with pytest.raises(FileNotFoundError):
        compare_f8(tmp_path)


def test_comparison_rejects_unfair_budgets(tmp_path):
    a = pd.DataFrame([{"engine": "hebo", "seed": 0, "step": 1,
                        "SIMULATED_best": 9.9, "duplicate": False}])
    b = pd.DataFrame([{"engine": "turbo", "seed": 0, "step": k,
                        "SIMULATED_best": 9.9, "duplicate": False} for k in (1,2)])
    a.to_csv(tmp_path / "f8_simulation_hebo.csv", index=False)
    b.to_csv(tmp_path / "f8_simulation_turbo.csv", index=False)
    with pytest.raises(ValueError, match="Budget mismatch"):
        compare_f8(tmp_path)
