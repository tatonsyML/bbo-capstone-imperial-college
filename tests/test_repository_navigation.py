"""Protect the public repository's compact navigation and original evidence."""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {
    ".github", "archive", "data", "docs", "functions", "journey",
    "notebooks", "research", "results", "scripts", "src", "tests",
}
DOCS = {
    "docs/methods.md", "docs/reconstruction.md", "docs/visualisations.md",
    "docs/gp_replay.md", "notebooks/README.md",
}
REMOVED = ("methods", "reconstruction", "visualisations", "final")


def test_twelve_organised_source_folders():
    for directory in FOLDERS:
        assert (ROOT / directory).is_dir(), directory
    for old in REMOVED:
        assert not (ROOT / old).exists(), f"Old redundant top-level directory: {old}"

    # Validate the actual *tracked* Git tree, excluding pytest caches and local
    # virtual environments which may appear when running tests.
    if (ROOT / ".git").exists():
        output = subprocess.check_output(
            ["git", "-C", str(ROOT), "ls-files", "-z"]
        ).decode("utf-8")
        tracked = {
            part.split("/", 1)[0]
            for part in output.split("\0") if "/" in part
        }
        assert tracked == FOLDERS, (tracked - FOLDERS, FOLDERS - tracked)


def test_research_entry_points_remain_present():
    homepage = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "## The project" in homepage
    assert "## Why black-box optimisation matters" in homepage
    assert "**Author:** [Tamer El-Tonsy](https://github.com/tatonsyML)" in homepage
    assert (
        "[Questions and corrections]"
        "(https://github.com/tatonsyML/bbo-capstone-imperial-college/issues)"
    ) in homepage
    assert "## Eight functions, eight investigations" in homepage

    for filename in DOCS:
        assert (ROOT / filename).is_file(), filename
    for function in range(1, 9):
        directory = ROOT / f"functions/F{function}"
        for filename in ("README.md", "observations.csv",
                         "selection_history.csv", "progress.svg"):
            assert (directory / filename).is_file(), f"{directory}/{filename}"
        assert not (directory / "model_runs").exists()
    for number in range(1, 14):
        assert (ROOT / f"journey/round_{number:02d}/README.md").is_file()


def test_original_round12_code_is_not_moved_or_duplicated():
    original = ROOT / "journey/round_12/original"
    portable = ROOT / "journey/round_12/portable"
    for filename in (
        "review_round12.py", "robust_and_warp.py", "tpe_local.py",
        "trust_region_ts.py",
    ):
        assert (original / filename).is_file()
        assert (portable / filename).is_file()
        assert not (ROOT / "src/bbo" / filename).exists()


def test_shared_gp_replay_and_artifact_only_notebook_workflow():
    guide = (ROOT / "docs/gp_replay.md").read_text(encoding="utf-8")
    assert "scripts/replay_surrogates.py" in guide
    notebook_guide = (ROOT / "notebooks/README.md").read_text(encoding="utf-8")
    assert "downloadable workflow artifact" in notebook_guide
    assert "does **not** commit output files" in notebook_guide


def test_removed_document_paths_do_not_reappear_in_public_navigation():
    pages = [
        ROOT / "README.md",
        ROOT / "journey/README.md",
        ROOT / "functions/README.md",
        ROOT / "notebooks/README.md",
        *sorted((ROOT / "docs").glob("*.md")),
    ]
    disallowed = (
        "methods/README.md", "reconstruction/README.md",
        "visualisations/README.md", "final/README.md",
    )
    for page in pages:
        source = page.read_text(encoding="utf-8")
        for path in disallowed:
            assert path not in source, (page.relative_to(ROOT), path)
