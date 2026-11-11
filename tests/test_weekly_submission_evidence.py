"""Regression checks for clear public research narratives and portal evidence."""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_all_thirteen_rounds_present_research_decisions_without_internal_footnotes():
    audit = (ROOT / "docs/WEEKLY_SUBMISSION_EVIDENCE.md").read_text(encoding="utf-8")
    assert "# Research decisions across thirteen rounds" in audit
    assert "Capstone Project.docx" not in audit
    assert "52-page" not in audit
    for n in range(1, 14):
        page = ROOT / f"journey/round_{n:02d}/README.md"
        text = page.read_text(encoding="utf-8")
        assert "## How I approached this round" in text, str(page)
        assert "52-page private" not in text
        assert "*Source: the author" not in text
        assert "Capstone Project.docx" not in text
        assert f"[{n}](../journey/round_{n:02d}/README.md)" in audit


def test_all_eight_function_narratives_are_cross_checked():
    audit = (ROOT / "docs/WEEKLY_SUBMISSION_EVIDENCE.md").read_text(encoding="utf-8")
    for n in range(1, 9):
        assert f"[F{n}](../functions/F{n}/README.md)" in audit
        assert (ROOT / f"functions/F{n}/README.md").exists()


def test_week11_clustering_reflection_and_later_code_are_separate():
    page = (ROOT / "journey/round_11/README.md").read_text(encoding="utf-8")
    diagnostic = (ROOT / "research/diagnostics/clustering/README.md").read_text(
        encoding="utf-8"
    )
    assert "DBSCAN investigation examined" in page
    assert "rebuilt **retrospectively**" in page
    assert "original Week 11 submission describes applying DBSCAN" in diagnostic
    assert "not the verified original Round 11 candidate generator" in diagnostic


def test_week13_f8_intention_is_not_mislabelled_a_portal_query():
    audit = (ROOT / "docs/WEEKLY_SUBMISSION_EVIDENCE.md").read_text(encoding="utf-8")
    page = (ROOT / "journey/round_13/README.md").read_text(encoding="utf-8")
    assert "distinct near-optimum F8 query" in audit
    assert "submitted R13 input repeated" in audit
    assert "considered a **small distinct F8 step**" in page
    assert "**submitted the same vertex**" in page

    with (ROOT / "data/all_observations.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    f8 = {
        int(r["round"]): r for r in rows
        if r["function"] == "8" and r["source"] == "personal_portal"
    }
    for earlier in (10, 11, 12):
        coordinates = [Decimal(f8[earlier][f"x{i}"]) for i in range(1, 9)]
        submitted = [Decimal(f8[13][f"x{i}"]) for i in range(1, 9)]
        assert coordinates == submitted
        assert Decimal(f8[earlier]["output"]) == Decimal("10")
    assert Decimal(f8[13]["output"]) == Decimal("10")


def test_recovered_f7_r11_input_remains_confirmed():
    with (ROOT / "data/all_observations.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    record = next(r for r in rows if r["function"] == "7" and r["round"] == "11")
    assert "-".join(f"{Decimal(record[f'x{i}']):.6f}" for i in range(1, 7)) == (
        "0.233000-0.128000-0.522000-0.276000-0.310000-0.667000"
    )
    assert Decimal(record["output"]) == Decimal("3.278967926227992")
