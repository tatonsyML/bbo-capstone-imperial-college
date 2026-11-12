"""Protect GitHub Markdown anchors and links in historical notebook Markdown."""
from __future__ import annotations

import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
CHECKER = runpy.run_path(str(ROOT / "tests" / "check_internal_links.py"))
check = CHECKER["check"]
heading_anchors = CHECKER["heading_anchors"]


def test_missing_anchor_and_notebook_link_fail_then_pass(tmp_path, capsys):
    home = tmp_path / "README.md"
    home.write_text("# The project\n\n## Repeat\n\n## Repeat\n")
    note = tmp_path / "archive" / "notes.md"
    note.parent.mkdir()
    note.write_text("[correct](../README.md#the-project)\n"
                    "[duplicate](../README.md#repeat-1)\n"
                    "[wrong](../README.md#the-project-in-plain-english)\n")
    book = tmp_path / "journey" / "round_06" / "history.ipynb"
    book.parent.mkdir(parents=True)
    book.write_text(json.dumps({
        "cells": [{"cell_type": "markdown",
                   "source": ["# Notebook\n",
                              "[wrong](../../../../notebooks/Final.ipynb)\n"]},
                  {"cell_type": "code",
                   "source": ["[not a link](missing.txt)\n"]}],
    }))
    assert check(tmp_path) == 1
    output = capsys.readouterr().out
    assert "MISSING HEADING ANCHOR" in output
    assert "OUTSIDE REPOSITORY" in output
    note.write_text(note.read_text().replace(
        "#the-project-in-plain-english", "#the-project"))
    book.write_text(book.read_text().replace(
        "../../../../notebooks/Final.ipynb", "../../notebooks/Final.ipynb"))
    dest = tmp_path / "notebooks"
    dest.mkdir()
    (dest / "Final.ipynb").write_text(json.dumps({
        "cells": [{"cell_type": "markdown", "source": ["# Final\n"]}],
    }))
    assert check(tmp_path) == 0


def test_duplicate_anchors_ignore_fenced_examples(tmp_path):
    file = tmp_path / "README.md"
    file.write_text("# The project\n## Trial & error\n## Trial & error\n"
                    "~~~md\n# Hidden heading\n~~~\n")
    headings = heading_anchors(file)
    assert {"the-project", "trial--error", "trial--error-1"} <= headings
    assert "hidden-heading" not in headings


def test_round6_notebook_code_reads_saved_tables(monkeypatch):
    notebook = ROOT / "journey/round_06/Capstone_BBO_Module17_Week6.ipynb"
    content = json.loads(notebook.read_text(encoding="utf-8"))
    code_cells = [c for c in content["cells"] if c["cell_type"] == "code"]
    assert len(code_cells) == 1
    original = "".join(code_cells[0]["source"])
    assert "root/'journey/round_06/results'" in original
    assert "submissions/stage_2/" not in original
    markdown = "\n".join("".join(c["source"]) for c in content["cells"]
                         if c["cell_type"] == "markdown")
    assert "../../notebooks/Capstone_Final_Walkthrough.ipynb" in markdown

    # Run the archived CSV-loading cell, replacing only its display function,
    # to test the data paths without requiring IPython in core CI.
    assert original.count("from IPython.display import display") == 1
    frames = []
    executable = original.replace(
        "from IPython.display import display",
        "display = lambda table: frames.append(table)")
    monkeypatch.chdir(ROOT)
    exec(compile(executable, str(notebook), "exec"), {"frames": frames})
    assert len(frames) == 2
    assert all(not f.empty for f in frames)
