"""Guard the published, explicitly simulated official-engine benchmark snapshot."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_hebo_turbo"


def read(filename):
    with (RESULTS / filename).open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def test_official_engines_have_balanced_simulation_budgets():
    rows = read("f8_simulation_comparison.csv")
    assert len(rows) == 6
    assert {(r["engine"], int(r["seed"])) for r in rows} == {
        (engine, seed) for engine in ("hebo", "turbo") for seed in (0, 1, 2)
    }
    assert all(int(r["evaluations"]) == 12 for r in rows)
    assert all(int(r["duplicate_queries"]) == 0 for r in rows)
    assert all(0 < float(r["SIMULATED_regret_to_model_peak"]) < 10 for r in rows)
    assert all(float(r["SIMULATED_final_best"]) < 10 for r in rows)


def test_published_simulator_inputs_and_versions_are_explicit():
    row, = read("f8_oracle_validation.csv")
    assert row["initial_points"] == "40"
    assert row["held_out_points"] == "13"
    assert float(row["max_holdout_error"]) < 2e-14
    versions = {
        engine: {r["package"]: r["version"]
                 for r in read(f"versions_{engine}.csv")}
        for engine in ("hebo", "turbo")
    }
    assert versions["hebo"]["HEBO"] == "0.3.6"
    assert versions["turbo"]["botorch"] == "0.18.1"
    source = (ROOT / "research" / "full_optimisers" / "README.md").read_text()
    assert "post-capstone simulations only" in source
    assert "none of these scores is a new course-portal evaluation" in source
