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
