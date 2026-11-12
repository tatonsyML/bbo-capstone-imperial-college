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

    assert "## Appendix A. Function-specific data profiles" in datasheet
    assert datasheet.count("### F") == 8
    assert "## Appendix B. Module 25 template coverage" in datasheet

    for function in range(1, 9):
        link = f"functions/F{function}/README.md"
        assert f"]({link})" in datasheet, link
        assert f"### F{function} ·" in datasheet
        assert f"](functions/F{function}/observations.csv)" in datasheet
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


def test_datasheet_strategy_outcomes_match_canonical_measurements():
    """Eight concise profiles contain measured best vectors and evidence limits."""
    import re

    datasheet = (ROOT / "DATASHEET.md").read_text(encoding="utf-8")
    with (ROOT / "data/all_observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        all_rows = list(csv.DictReader(handle))

    for function, dimensions in enumerate(DIMS, start=1):
        heading = f"### F{function} ·"
        section = datasheet.split(heading, 1)[1].split(
            f"### F{function + 1} ·" if function < 8 else "**Scope:**", 1
        )[0]
        assert section.count("**Optimisation strategy and outcome:**") == 1
        assert "**Confidence:**" in section and "global" in section.lower()
        assert "local" in section.lower()
        assert ("explor" in section.lower() or "region" in section.lower())

        measured = [
            row for row in all_rows
            if int(row["function"]) == function
            and row["source"] == "personal_portal"
        ]
        best = max(measured, key=lambda row: Decimal(row["output"]))
        expected_input = "-".join(
            f'{Decimal(best[f"x{i}"]):.6f}' for i in range(1, dimensions + 1)
        )
        assert f"**Best measured input:** `{expected_input}`" in section
        found_output = re.search(r"\*\*Best measured output:\*\* `([^`]+)`", section)
        assert found_output is not None, function
        assert Decimal(found_output.group(1)) == Decimal(best["output"])


def test_all_eight_function_profiles_explicitly_answer_restart_question_5_4():
    """Require eight separate retrospective improvements, not just a coverage claim."""
    datasheet = (ROOT / "DATASHEET.md").read_text(encoding="utf-8")
    assert "**Template question 5.4 — If you restarted, what would you do differently?**" in datasheet
    assert datasheet.count("**If I restarted:**") == 8

    # Distinct evidence from each function prevents a generic boilerplate
    # paragraph from silently replacing its actual research-specific lesson.
    required_clues = (
        ("near-zero", "signal"),
        ("Round 9", "competing regions"),
        ("final-round", "local"),
        ("0.659", "tiny"),
        ("boundary", "repeat"),
        ("sensitivity", "interactions"),
        ("Hartmann-6", "prospective"),
        ("quadratic", "vertex"),
    )
    for function, clues in enumerate(required_clues, start=1):
        section = datasheet.split(f"### F{function} ·", 1)[1].split(
            f"### F{function + 1} ·" if function < 8 else "**Scope:**", 1
        )[0]
        assert section.count("**If I restarted:**") == 1, function
        lesson = section.split("**If I restarted:**", 1)[1].strip()
        assert 20 <= len(lesson.split()) <= 100, function
        for clue in clues:
            assert clue in lesson, (function, clue)



def test_datasheet_question_2_4_classifies_apparent_function_behaviour():
    """Check all eight evidence-qualified answers and model/oracle distinctions."""
    datasheet = (ROOT / "DATASHEET.md").read_text(encoding="utf-8")
    assert "**Template question 2.4 — Does the function appear unimodal, multimodal, noisy or smooth?**" in datasheet
    assert datasheet.count("**Apparent function behaviour (question 2.4):**") == 8

    for function in range(1, 9):
        section = datasheet.split(f"### F{function} ·", 1)[1].split(
            f"### F{function + 1} ·" if function < 8 else "**Scope:**", 1
        )[0]
        assert section.count("**Apparent function behaviour (question 2.4):**") == 1
        description = section.split(
            "**Apparent function behaviour (question 2.4):**", 1
        )[1].split("**Optimisation strategy and outcome:**", 1)[0]
        for category in ("**Unimodal or multimodal:**", "**Smooth:**", "**Noisy:**"):
            assert description.count(category) == 1, (function, category)
        assert 40 <= len(description.split()) <= 115, function
        assert any(term in description.lower() for term in (
            "unverified", "unknown", "cannot", "not proved",
            "not establish", "do not establish", "not proof",
            "not authenticated"
        )), function

    # Particularly important: an apparently sensitive surface is not
    # necessarily a random one, and a retrospective equation is not
    # authenticated source code.
    f6 = datasheet.split("### F6 ·", 1)[1].split("### F7 ·", 1)[0]
    f8 = datasheet.split("### F8 ·", 1)[1].split("**Scope:**", 1)[0]
    assert "not necessarily a discontinuity" in f6
    assert "not proved globally unimodal" in f8


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


def test_model_card_follows_mitchell_and_course_template():
    """One model card reports nine Mitchell sections and four course fields."""
    card = (ROOT / "MODEL_CARD.md").read_text(encoding="utf-8")
    sections = (
        "Model Details",
        "Intended Use",
        "Factors Affecting Performance",
        "Metrics",
        "Evaluation Data",
        "Training Data",
        "Quantitative Analyses",
        "Ethical Considerations",
        "Caveats and Recommendations",
    )
    for number, name in enumerate(sections, start=1):
        assert f"## {number}. {name}" in card, name

    for text in (
        "**Input:**",
        "**Output:**",
        "**Model Architecture:**",
        "## Module 25 template coverage",
        "results/figures/progress.svg",
        "40 initial F8 observations",
        "13 later F8 returns",
        "Mitchell, M.",
        "Model Cards for Model Reporting",
        "Trade-offs",
    ):
        assert text in card, text

    assert card.count("| [F") >= 8
    assert "DATASHEET.md" in card
    assert "functions/README.md" in card
    assert "notebooks/Capstone_Final_Walkthrough.ipynb" in card


def test_readme_links_the_research_without_imposing_an_editorial_word_count():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required = (
        "functions/README.md",
        "journey/README.md",
        "DATASHEET.md",
        "MODEL_CARD.md",
        "notebooks/Capstone_Final_Walkthrough.ipynb",
        "USAGE_AND_PERMISSIONS.md",
    )
    for target in required:
        assert f"]({target})" in readme, target
    assert "Gaussian Process" in readme
    assert "8 functions" in readme.lower()
    assert "## Non-technical summary" in readme
    summary = readme.split("## Non-technical summary", 1)[1].split("**Technical scope:**", 1)[0]
    assert 85 <= len(summary.split()) <= 115


def test_datasheet_avoids_official_scenario_attribution():
    """The original brief did not establish real-world function scenarios."""
    text = (ROOT / "DATASHEET.md").read_text(encoding="utf-8")
    assert "did not provide authoritative real-world descriptions" in text
    assert "verified scenario-to-function mapping" in text
    assert "illustrative analogy" in text
    assert "not a verified official description" in text
    assert "programme FAQ says function descriptions" not in text
