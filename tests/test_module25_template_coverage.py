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


def test_each_function_addresses_seven_datasheet_template_sections():
    text = (ROOT / "docs/function_datasheets.md").read_text(encoding="utf-8")
    assert text.count("\n## Function ") == 8
    for function in range(1, 9):
        start = f"\n## Function {function}\n"
        section = text.split(start, 1)[1].split("\n## Function ", 1)[0]
        for label in GROUPS:
            assert f"**{label}:**" in section, (function, label)
        shape = f"({STARTING[function-1]}, {DIMS[function-1]})"
        assert shape in section, (function, shape)
        assert f"../functions/F{function}/selection_history.csv" in section


def test_all_eight_best_outputs_and_vectors_match_canonical_evidence():
    text = (ROOT / "docs/function_datasheets.md").read_text(encoding="utf-8")
    with (ROOT / "data/all_observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    for function, dimensions in enumerate(DIMS, start=1):
        section = text.split(f"\n## Function {function}\n", 1)[1].split(
            "\n## Function ", 1
        )[0]
        personal = [
            row for row in rows
            if int(row["function"]) == function
            and row["source"] == "personal_portal"
        ]
        assert len(personal) == 13
        best = max(personal, key=lambda row: Decimal(row["output"]))
        assert best["output"] in section, (function, best["output"])
        vector = "(" + ", ".join(
            f'{Decimal(best[f"x{i}"]):.6f}'
            for i in range(1, dimensions + 1)
        ) + ")"
        assert vector in section, (function, vector)


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
        "docs/function_datasheets.md",
    ):
        assert text in readme
