"""Keep the public research structure navigable without prescribing editorial prose."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]


def test_round_and_function_stories_exist():
    journey = ROOT / "journey/README.md"
    index = ROOT / "functions/README.md"
    assert journey.is_file() and index.is_file()
    assert (ROOT / "archive/round_10/README.md").is_file()
    for round_number in range(1, 14):
        page = ROOT / f"journey/round_{round_number:02d}/README.md"
        assert page.is_file(), page
        assert len(page.read_text(encoding="utf-8")) > 200, page
    for function in range(1, 9):
        assert (ROOT / f"functions/F{function}/README.md").is_file()


def test_function_rounds_have_inputs_results_and_source_links():
    for function in range(1, 9):
        body = (ROOT / f"functions/F{function}/README.md").read_text(
            encoding="utf-8"
        )
        sections = re.findall(r"<details>(.*?)</details>", body, flags=re.DOTALL)
        assert len(sections) == 13, function
        for round_number, content in enumerate(sections, 1):
            title = re.search(r"<summary><strong>Round (\d+)\b", content)
            assert title is not None and int(title.group(1)) == round_number
            assert re.search(r"\*\*Submitted input:\*\*\s*`[^`]+`", content)
            assert re.search(r"\*\*Actual portal (?:result|output):\*\*", content)
            assert "before → after" in content
            assert re.search(r"\]\((?:\.\./|[a-zA-Z])", content)
        assert (ROOT / f"functions/F{function}/selection_history.csv").is_file()


def test_preserved_forecasts_are_recorded_as_predictions_not_outputs():
    for function in range(1, 9):
        path = ROOT / f"functions/F{function}/selection_history.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        assert len(rows) == 13, function
        assert all(row["actual_output"] for row in rows), function
        for row in rows:
            if row["pre_result_forecast"]:
                assert row["forecast_provenance"], (function, row["round"])


def test_earlier_decisions_do_not_quote_later_return_as_prior_knowledge():
    """Guard specific historical chronological errors without fixing prose."""
    for function, current, future_score in (
        (3, 11, "-0.0226526646178297"),
        (3, 12, "-0.0037530969187192596"),
        (4, 10, "0.7304594213260924"),
        (6, 11, "-0.03751864724436928"),
        (7, 10, "3.278967926227992"),
        (7, 11, "3.3223680113931557"),
    ):
        text = (ROOT / f"functions/F{function}/README.md").read_text(
            encoding="utf-8"
        )
        section = re.findall(r"<details>(.*?)</details>", text, flags=re.DOTALL)[current - 1]
        assert future_score not in section, (function, current, future_score)
