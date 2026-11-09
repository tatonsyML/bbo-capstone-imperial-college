"""Final 279-row dataset validation and source chronology."""
from pathlib import Path
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

def test_missing_f7_input_not_reconstructed():
    data = pd.read_csv(ROOT / "data/all_observations.csv")
    missing = data[data.input_status == "missing_input"]
    assert len(missing) == 1
    row = missing.iloc[0]
    assert int(row["function"]) == 7
    assert int(row["round"]) == 11
    assert abs(float(row["output"]) - 3.27896792623) < 1e-12
    assert row[[f"x{i}" for i in range(1, 7)]].isna().all()

def test_final_best_scores_derived_from_all_observations():
    data = pd.read_csv(ROOT / "data/all_observations.csv")
    report = pd.read_csv(ROOT / "results/current_best_after_week13.csv")
    actual = data.groupby("function")["output"].max().sort_index()
    expected = report.set_index("Function")["Final_Best"].sort_index()
    np.testing.assert_allclose(actual.to_numpy(), expected.to_numpy(), atol=1e-12)
