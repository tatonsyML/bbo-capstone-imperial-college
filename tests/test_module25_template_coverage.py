"""Verify coverage of the supplied Imperial Module 25 project templates."""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = (
    "Function overview",
    "Nature and evolution",
    "Optimisation strategy",
    "Data handling and preprocessing",
    "Weekly iteration and learning",
    "Performance and confidence",
    "Ethical and practical considerations",
)
STARTING = (10, 10, 15, 30, 20, 20, 30, 40)
DIMS = (2, 2, 3, 4, 4, 5, 6, 8)


def test_main_datasheet_maps_template_and_links_complete_function_stories():
    """Dataset lifecycle lives once; function-level research stays in eight stories."""
    datasheet = (ROOT / "DATASHEET.md").read_text(encoding="utf-8")
    assert "29 questions" in datasheet
    assert "Gebru et al. (2021)" in datasheet
    for number, heading in enumerate((
        "Motivation",
        "Composition",
        "Collection Process",
        "Preprocessing, Cleaning and Labelling",
        "Uses",
        "Distribution",
        "Maintenance",
    ), start=1):
        assert f"## {number}. {heading}" in datasheet

    assert "## Appendix A. Function-specific dataset notes" in datasheet
    assert "## Appendix B. Module 25 template coverage" in datasheet
    assert "If you restarted" in datasheet

    for function in range(1, 9):
        link = f"functions/F{function}/README.md"
        assert datasheet.count(f"]({link})") >= 2, (function, link)
        assert f"| **F{function}** |" in datasheet
        assert f"({STARTING[function-1]}, {DIMS[function-1]})" in datasheet
        assert f"({STARTING[function-1]},)" in datasheet

        story = (ROOT / link).read_text(encoding="utf-8")
        assert "## Understanding this function" in story
        assert "## Weekly development" in story
        assert story.count("<summary><strong>Round ") == 13, function
        assert "selection_history.csv" in story
        assert "## Visual analysis" in story
        assert (
            "## Lessons to carry forward" in story
            or "## What this function taught me" in story
        )


def test_all_eight_function_stories_preserve_canonical_best_results():
    """Score and exact six-decimal vector stay authoritative in function pages."""
    with (ROOT / "data/all_observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    for function, dimensions in enumerate(DIMS, start=1):
        personal = [
            row for row in rows
            if int(row["function"]) == function
            and row["source"] == "personal_portal"
        ]
        assert len(personal) == 13
        best = max(personal, key=lambda row: Decimal(row["output"]))
        story = (ROOT / f"functions/F{function}/README.md").read_text(
            encoding="utf-8"
        )
        result_row = next(
            line for line in story.splitlines()
            if line.startswith("| `") and "**`" in line
        )
        cells = [cell.strip() for cell in result_row.strip("|").split("|")]
        documented_score = Decimal(cells[1].replace("**", "").replace("`", ""))
        assert documented_score == Decimal(best["output"]), function

        expected_vector = "-".join(
            f'{Decimal(best[f"x{i}"]):.6f}'
            for i in range(1, dimensions + 1)
        )
        documented_vector = cells[3].replace("`", "")
        assert documented_vector == expected_vector, function


def test_model_card_has_explicit_template_fields_graph_and_evaluation():
    model = (ROOT / "MODEL_CARD.md").read_text(encoding="utf-8")
    for label in (
        "**Inputs:**",
        "**Outputs:**",
        "**Model architecture:**",
        "## 5. Trade-offs and decisions",
        "## 6. Performance:",
        "## 7. Evaluation methods and quantitative validation",
        "## 8. Assumptions, limitations and potential failure modes",
        "results/figures/progress.svg",
        "40 initial F8 observations",
        "13 later F8 returns",
    ):
        assert label in model, label


def test_readme_has_roughly_hundred_word_public_explanation_and_hyperparameters():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    plain = readme.split("## The project\n", 1)[1].split(
        "**Technical scope:**", 1
    )[0]
    length = len(plain.split())
    assert 90 <= length <= 110, length
    for text in (
        "## Models and hyperparameter choices",
        "## Eight functions, eight investigations",
        "## What the experiments taught me",
        "## Data, documentation and reuse",
        "[Dataset datasheet and function-specific data notes](DATASHEET.md)",
    ):
        assert text in readme
