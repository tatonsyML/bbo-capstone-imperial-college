"""Keep recovered portal evidence and public documentation consistent.

The Markdown path checker cannot detect statements or charts that contradict
authoritative observations. This test specifically protects the F7 R11 fix.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_INPUT = [
    "0.233000", "0.128000", "0.522000",
    "0.276000", "0.310000", "0.667000",
]


def test_f7_round11_verified_across_data_and_gallery():
    with (ROOT / "data/all_observations.csv").open(encoding="utf-8", newline="") as fh:
        data = list(csv.DictReader(fh))
    f7 = [r for r in data if int(r["function"]) == 7]
    assert len(f7) == 43
    row = next(r for r in f7 if int(r["round"]) == 11)
    assert row["input_status"] == "confirmed"
    assert [row[f"x{i}"] for i in range(1, 7)] == EXPECTED_INPUT
    assert abs(float(row["output"]) - 3.278967926227992) < 1e-14

    manifest = json.loads((ROOT / "results/figures/gallery_manifest.json").read_text())
    item = next(r for r in manifest if r["function"] == 7)
    assert item["observationsPlotted"] == len(f7)

    generator = (ROOT / "results/figures/build_visual_gallery.mjs").read_text()
    assert "if(!row.Input) continue" not in generator
    assert "Verified portal record missing input" in generator


def test_no_known_stale_r11_f7_claims_in_active_documentation():
    paths = [
        "docs/methods.md",
        "journey/round_11/README.md",
        "journey/round_12/README.md",
        "journey/round_13/README.md",
    ]
    obsolete = [
        "the exact r11 input on f7 is missing",
        "r11 f7 has no preserved input",
        "r11 f7 input is missing from the preserved evidence",
        "this gap is flagged, not filled with a guessed point",
    ]
    for name in paths:
        text = (ROOT / name).read_text(encoding="utf-8").lower()
        for phrase in obsolete:
            assert phrase not in text, f"Stale statement in {name}: {phrase}"


def test_all_13_rounds_are_in_historical_code_inventory():
    text = (ROOT / "journey/CODE_AVAILABILITY.md").read_text(encoding="utf-8")
    for round_number in range(1, 14):
        assert f"| {round_number} |" in text
    assert "exact" in text.lower()
    assert "not" in text.lower()
