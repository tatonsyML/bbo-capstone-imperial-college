"""Final 279-row dataset validation and source chronology."""
from pathlib import Path
import csv
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def test_full_inventory():
    data = pd.read_csv(ROOT / "data/all_observations.csv")
    assert len(data) == 279
    assert (data.source == "course_initial").sum() == 175
    assert (data.source == "personal_portal").sum() == 104
    assert data.output.notna().all()
    assert all(len(data[(data.function == f) & (data['round'] > 0)]) == 13 for f in range(1, 9))

def test_all_portal_inputs_verified_including_f7_r11():
    data = pd.read_csv(ROOT / "data/all_observations.csv")
    assert (data.input_status == "confirmed").all()
    for function, dim in {1:2,2:2,3:3,4:4,5:4,6:5,7:6,8:8}.items():
        rows = data[data.function == function]
        assert rows[[f"x{i}" for i in range(1, dim+1)]].notna().all().all()
    row = data[(data.function == 7) & (data["round"] == 11)].iloc[0]
    np.testing.assert_allclose(
        row[[f"x{i}" for i in range(1, 7)]].astype(float).to_numpy(),
        [0.233, 0.128, 0.522, 0.276, 0.310, 0.667], rtol=0, atol=1e-15)
    assert abs(float(row["output"]) - 3.278967926227992) < 1e-14

def test_final_best_scores_derived_from_all_observations():
    data = pd.read_csv(ROOT / "data/all_observations.csv")
    report = pd.read_csv(ROOT / "results/current_best_after_week13.csv")
    actual = data.groupby("function")["output"].max().sort_index()
    expected = report.set_index("Function")["Final_Best"].sort_index()
    np.testing.assert_allclose(actual.to_numpy(), expected.to_numpy(), atol=1e-12)


def test_csv_header_families_follow_documented_conventions():
    """Different CSV products retain deliberate, stable, case-sensitive headers."""
    def columns(path):
        with (ROOT / path).open(encoding="utf-8", newline="") as stream:
            return next(csv.reader(stream))

    canonical = [
        "function", "round", "stage", "source", "sequence_in_stage",
        "is_initial", "input_status",
        *(f"x{i}" for i in range(1, 9)), "output",
    ]
    assert columns("data/all_observations.csv") == canonical

    ledger = columns("functions/F1/selection_history.csv")
    assert ledger[:4] == [
        "round", "submitted_input", "actual_output", "input_status"
    ]
    for fn in range(1, 9):
        assert columns(f"functions/F{fn}/observations.csv") == canonical
        assert columns(f"functions/F{fn}/selection_history.csv") == ledger

    portal = ["Function", "Round", "Input", "Output", "Input_Status"]
    for path in ("data/portal_rounds_11_12.csv", "data/portal_rounds_13.csv"):
        assert columns(path) == portal

    assert columns("data/accumulated/history_through_week13.csv") == [
        "Function", "Stage", "Input", "Output", "Best_so_far", "New_best"
    ]
    report = columns("results/current_best_after_week13.csv")
    assert report[0] == "Function"
    assert "Final_Best" in report and "Best_Input" in report
