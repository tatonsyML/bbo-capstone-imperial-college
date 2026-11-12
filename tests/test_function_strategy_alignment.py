"""Check all 104 function decisions against their documented round evidence.

Presentation may be standardised, but observations, historical decisions and
their published provenance must not change. Any new claims about optimisation
methods should remain consistent with the chronological journey.
"""
from __future__ import annotations

import csv
import re
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = (2, 2, 3, 4, 4, 5, 6, 8)
FIELDS = (
    "**Why this input:**",
    "**Approach considered:**",
    "**Submitted input:**",
    "**Actual portal result:**",
    "**Best observed before → after:**",
    "**What I learnt:**",
    "**Code and data:**",
)


def _round_entries(function: int) -> list[str]:
    story = (ROOT / f"functions/F{function}/README.md").read_text(
        encoding="utf-8"
    )
    entries = re.findall(r"<details>(.*?)</details>", story, re.DOTALL)
    assert len(entries) == 13, function
    return entries


def _line_value(entry: str, label: str) -> str:
    match = re.search(r"^" + re.escape(label) + r"\s*(.+)$", entry, re.MULTILINE)
    assert match is not None, f"Missing {label}"
    return match.group(1).strip()


def test_all_function_rounds_have_identical_evidence_fields():
    """Each function has 13 ordered decisions with an approach, not an invented score."""
    for function in range(1, 9):
        for round_number, entry in enumerate(_round_entries(function), 1):
            assert re.search(
                rf"<summary><strong>Round {round_number}\b", entry
            ), (function, round_number)
            for field in FIELDS:
                assert entry.count(field) == 1, (function, round_number, field)
            positions = [entry.index(field) for field in FIELDS]
            assert positions == sorted(positions), (function, round_number)
            assert (
                f"../../journey/round_{round_number:02d}/README.md" in entry
            ), (function, round_number)
            assert "**Decision context:**" not in entry
            assert "**Evaluation:**" not in entry
            assert "**Actual portal output:**" not in entry
            assert "**What changed for the next round:**" not in entry
            assert "**Approach:**" not in entry
            assert _line_value(entry, "**Approach considered:**")


def test_story_inputs_and_outputs_match_all_104_real_portal_results():
    """No editing of decision narratives can alter submitted vectors or returned scores."""
    with (ROOT / "data/all_observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        portal = {
            (int(row["function"]), int(row["round"])): row
            for row in csv.DictReader(handle)
            if row["source"] == "personal_portal"
        }
    assert len(portal) == 104

    for function, dimension in enumerate(DIMENSIONS, 1):
        for round_number, entry in enumerate(_round_entries(function), 1):
            observed = portal[(function, round_number)]
            chosen = _line_value(entry, "**Submitted input:**")
            match_input = re.search(r"`([^`]+)`", chosen)
            assert match_input is not None
            # Do not split on e-06 in scientific notation.
            coordinates = [
                Decimal(value)
                for value in re.split(r"(?<![eE])-", match_input.group(1))
            ]
            actual_coordinates = [
                Decimal(observed[f"x{i}"]) for i in range(1, dimension + 1)
            ]
            assert coordinates == actual_coordinates, (function, round_number)

            score = _line_value(entry, "**Actual portal result:**")
            match_score = re.search(r"`([^`]+)`", score)
            assert match_score is not None
            assert Decimal(match_score.group(1)) == Decimal(
                observed["output"]
            ), (function, round_number)


def test_early_strategy_evolution_matches_chronological_rounds():
    """Preserve source-supported policy differences rather than copying generic labels."""
    kappas = ("3.0", "2.5", "2.0", "1.0", "1.0", "1.0", "2.0", "1.5")
    for function, kappa in enumerate(kappas, 1):
        round_two = _round_entries(function)[1]
        assert f"κ={kappa}" in round_two, function

    method_terms = (
        "Maximin exploration",
        "Global Expected Improvement",
        "Local predicted-mean optimisation",
        "Local Expected Improvement",
        "Local Expected Improvement",
        "Local Expected Improvement",
        "Local Expected Improvement",
        "Local Expected Improvement",
    )
    for function, term in enumerate(method_terms, 1):
        round_three = _round_entries(function)[2]
        assert term.lower() in round_three.lower(), function

    chronology = (ROOT / "journey/round_03/README.md").read_text(
        encoding="utf-8"
    ).lower()
    for term in ("maximin", "global expected improvement", "predicted-mean", "local expected improvement"):
        assert term in chronology


def test_genuine_pre_result_evidence_and_retrospective_caveats_remain():
    """Retain landmark forecasts without crediting a different optimiser or later intent."""
    f2 = _round_entries(2)
    f7 = _round_entries(7)
    f8 = _round_entries(8)
    assert "0.7305023346561939" in f2[8]
    assert "0.5055255161847483" in f2[8]
    assert "HEBO-inspired" in f2[9] and "TuRBO-style" in f2[9]
    assert "3.32236801" in f7[11] and "**Pre-result forecast:**" in f7[11]
    assert "17-coefficient" in f8[9] and "**Pre-result forecast:**" in f8[9]
    assert "repeated" in f8[12].lower()
    assert "distinct" in f8[12].lower()

    # The final reflection proposed a distinct F8 move, but the portal did
    # not evaluate one: both submissions used the same eight coordinates.
    r10 = _line_value(f8[9], "**Submitted input:**")
    r13 = _line_value(f8[12], "**Submitted input:**")
    assert r10 == r13
    round_13 = (ROOT / "journey/round_13/README.md").read_text(
        encoding="utf-8"
    )
    assert "submitted the same vertex" in round_13


def test_f5_chemical_yield_is_a_working_analogy_not_a_verified_course_scenario():
    """Keep the function and chronological accounts aligned on provenance."""
    f5_round_one = _round_entries(5)[0]
    chronological = (ROOT / "journey/round_01/README.md").read_text(
        encoding="utf-8"
    )
    for account in (f5_round_one, chronological):
        assert "chemical yield" in account
        assert "working analogy" in account
        assert "not verified as the programme's official F5 scenario" in account
        assert "peak" in account

    # No official descriptions have been recovered for the other functions.
    datasheet = (ROOT / "DATASHEET.md").read_text(encoding="utf-8")
    assert "unverified in this repository" in datasheet
