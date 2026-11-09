"""Validate function-first ledgers against the unaltered source data."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = {1: 2, 2: 2, 3: 3, 4: 4, 5: 4, 6: 5, 7: 6, 8: 8}
INITIAL = {1: 10, 2: 10, 3: 15, 4: 30, 5: 20, 6: 20, 7: 30, 8: 40}


def read(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_function_observations_partition_canonical_without_changes():
    canonical = read(ROOT / "data" / "all_observations.csv")
    assert len(canonical) == 279
    for function in range(1, 9):
        observed = read(ROOT / "functions" / f"F{function}" / "observations.csv")
        expected = [r for r in canonical if int(r["function"]) == function]
        assert observed == expected
        assert sum(int(r["round"]) == 0 for r in observed) == INITIAL[function]
        assert sum(int(r["round"]) > 0 for r in observed) == 13


def test_round_histories_match_only_known_pre_round_scores():
    for function in range(1, 9):
        rows = read(ROOT / "functions" / f"F{function}" / "observations.csv")
        ledger = read(ROOT / "functions" / f"F{function}" / "selection_history.csv")
        assert [int(r["round"]) for r in ledger] == list(range(1, 14))
        for rec in ledger:
            r = int(rec["round"])
            selected = next(item for item in rows if int(item["round"]) == r)
            before = [item for item in rows if int(item["round"]) < r]
            complete = [
                item for item in before
                if all(item[f"x{i}"] for i in range(1, DIMENSIONS[function] + 1))
            ]
            coordinates = "-".join(
                selected[f"x{i}"] for i in range(1, DIMENSIONS[function] + 1)
            ) if selected["input_status"] == "confirmed" else ""
            assert rec["submitted_input"] == coordinates
            assert rec["actual_output"] == selected["output"]
            assert int(rec["scores_available_before"]) == len(before)
            assert int(rec["usable_pairs_before"]) == len(complete)
            assert float(rec["best_observed_before"]) == max(
                float(x["output"]) for x in before
            )
            assert float(rec["best_observed_after"]) == max(
                float(x["output"]) for x in before + [selected]
            )
            assert rec["is_new_best"] == str(
                float(selected["output"]) >
                max(float(x["output"]) for x in before)
            ).lower()


def test_missing_f7_r11_coordinates_not_inferred():
    rows = read(ROOT / "functions" / "F7" / "selection_history.csv")
    assert rows[10]["round"] == "11"
    assert rows[10]["input_status"] == "missing_input"
    assert rows[10]["submitted_input"] == ""
    assert rows[10]["actual_output"] == "3.27896792623"
    assert rows[11]["scores_available_before"] == "41"
    assert rows[11]["usable_pairs_before"] == "40"


def test_replay_excludes_unknown_coordinates_and_future_returns():
    from scripts.replay_surrogates import load_before_round
    X, y, omitted, earlier = load_before_round(7, 12)
    assert X.shape == (40, 6)
    assert len(y) == 40
    assert len(earlier) == 41
    assert omitted == 1
    x1, y1, omitted1, _ = load_before_round(1, 1)
    assert x1.shape == (10, 2)
    assert len(y1) == 10
    assert omitted1 == 0


def test_replay_refits_and_labels_an_unscored_proposal():
    """Smoke-test the full GP fitting route on a cheap pre-round snapshot."""
    from scripts.replay_surrogates import replay

    report = replay(
        function=2, round_number=9, kernel="Matern25",
        acquisition="EI", restarts=0, seed=909, n_power=4,
        beta=1.96, xi=0.0,
    )
    assert report["provenance"] == "RETROSPECTIVE_COUNTERFACTUAL_NOT_ORIGINAL_SUBMISSION"
    assert report["earlier_observed_scores"] == 18
    assert report["usable_training_pairs"] == 18
    assert len(report["learned_ard_lengthscales"]) == 2
    assert report["logged_submission_retrospective_prediction"] is not None
    suggestion = report["NEW_UNOBSERVED_counterfactual_candidate"]
    assert suggestion["real_portal_score"] is None
    assert len(suggestion["coordinates"]) == 2
    assert all(0 <= x <= 0.999999 for x in suggestion["coordinates"])
