"""Check chronological research claims and preserved original implementations."""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def observations(function):
    with (ROOT / "data/all_observations.csv").open(
        newline="", encoding="utf-8"
    ) as file:
        return [row for row in csv.DictReader(file)
                if int(row["function"]) == function
                and row["source"] == "personal_portal"]


def test_each_round_and_function_has_an_explorable_record():
    for n in range(1, 14):
        page = ROOT / f"journey/round_{n:02d}/README.md"
        assert page.is_file()
    for f in range(1, 9):
        assert (ROOT / f"functions/F{f}/README.md").is_file()
        assert (ROOT / f"functions/F{f}/selection_history.csv").is_file()


def test_f7_round11_and_round12_are_measured_not_inferred():
    rows = {int(row["round"]): row for row in observations(7)}
    assert len(rows) == 13
    assert "-".join(f"{Decimal(rows[11][f'x{i}']):.6f}" for i in range(1, 7)) == (
        "0.233000-0.128000-0.522000-0.276000-0.310000-0.667000"
    )
    assert Decimal(rows[11]["output"]) == Decimal("3.278967926227992")
    assert Decimal(rows[12]["output"]) == Decimal("3.3223680113931557")


def test_f8_final_repeat_is_not_a_distinct_query():
    rows = {int(row["round"]): row for row in observations(8)}
    for earlier in (10, 11, 12):
        assert [Decimal(rows[earlier][f"x{i}"]) for i in range(1, 9)] == [
            Decimal(rows[13][f"x{i}"]) for i in range(1, 9)
        ]
        assert Decimal(rows[earlier]["output"]) == Decimal("10")
    assert Decimal(rows[13]["output"]) == Decimal("10")


def test_round11_clustering_sources_and_round12_modelling_scripts_survive():
    assert (ROOT / "research/diagnostics/clustering/clustering_audit.py").is_file()
    assert (ROOT / "journey/round_11/README.md").is_file()
    for name in ("review_round12.py", "robust_and_warp.py",
                 "tpe_local.py", "trust_region_ts.py"):
        for folder in ("original", "portable"):
            assert (ROOT / f"journey/round_12/{folder}/{name}").is_file()
    assert (ROOT / "journey/round_12/original/week12_original_assets.zip").is_file()


def test_historical_material_is_archived_without_losing_original_submissions():
    base = ROOT / "archive/round_10"
    for name in (
        "component_21_1/submission.md",
        "component_21_1/alternate_draft.md",
        "component_21_2/datasheet.md",
        "component_21_2/model_card.md",
        "component_21_2/decision_log.md",
        "supplementary/datasheet_week9_snapshot.md",
        "supplementary/model_card_week9_snapshot.md",
    ):
        assert (base / name).is_file(), name
