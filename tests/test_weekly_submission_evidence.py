"""Regression checks for clear public research narratives and portal evidence."""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_all_rounds_have_readable_public_summaries():
    journey = (ROOT / "journey/README.md").read_text(encoding="utf-8")
    assert "# Development journey | 13 returned rounds" in journey
    for n in range(1, 14):
        page = ROOT / f"journey/round_{n:02d}/README.md"
        content = page.read_text(encoding="utf-8")
        assert "## How I approached this round" in content
        assert "Capstone Project.docx" not in content
        assert f"](round_{n:02d}/README.md)" in journey


def test_all_function_investigations_remain_linked():
    index = (ROOT / "functions/README.md").read_text(encoding="utf-8")
    for n in range(1, 9):
        assert f"](F{n}/README.md)" in index
        assert (ROOT / f"functions/F{n}/README.md").exists()


def test_week11_clustering_remains_explained():
    page = (ROOT / "journey/round_11/README.md").read_text(encoding="utf-8")
    diagnostic = (ROOT / "research/diagnostics/clustering/README.md").read_text(encoding="utf-8")
    assert "## Clustering analysis and visualisation" in page
    assert "255 observations through Round 10" in page
    assert "DBSCAN" in diagnostic
    assert "modelled values remain separate" in diagnostic


def test_week13_f8_intention_is_not_mislabelled_a_portal_query():
    page = (ROOT / "journey/round_13/README.md").read_text(encoding="utf-8")
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


def test_week12_showcases_methods_not_file_recovery_process():
    """Do not reintroduce internal archive/recovery narration in public guides."""
    public_pages = [
        ROOT / "journey/round_12/README.md",
        ROOT / "journey/README.md",
        ROOT / "docs/methods.md",
        ROOT / "notebooks/README.md",
    ]
    internal_phrases = [
        "recovered original",
        "recovered round 12",
        "recovered week 12",
        "recovered modelling scripts",
        "source snapshot dated",
        "added to this repository on",
        "git creation dates",
        "verification at recovery",
        "additional historical methods awaiting source verification",
    ]
    for page in public_pages:
        content = page.read_text(encoding="utf-8").lower()
        for phrase in internal_phrases:
            assert phrase not in content, (page.relative_to(ROOT), phrase)

    round12 = (ROOT / "journey/round_12/README.md").read_text(encoding="utf-8")
    assert "## Week 12 modelling and optimisation code" in round12
    for script in ("review_round12.py", "robust_and_warp.py",
                   "tpe_local.py", "trust_region_ts.py"):
        assert f"](original/{script})" in round12
    assert "new personal best" in round12
    guide = (ROOT / "notebooks/README.md").read_text(encoding="utf-8")
    assert "../journey/round_12/README.md#week-12-modelling-and-optimisation-code" in guide
