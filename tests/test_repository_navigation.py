"""Check reader entry points and the original reproducible research structure."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {
    ".github", "archive", "data", "docs", "functions", "journey",
    "notebooks", "research", "results", "scripts", "src", "tests",
}


def test_organised_source_folders():
    for directory in FOLDERS:
        assert (ROOT / directory).is_dir(), directory
    if (ROOT / ".git").exists():
        tracked = set()
        listing = subprocess.check_output(
            ["git", "-C", str(ROOT), "ls-files", "-z"]
        ).decode("utf-8")
        for item in listing.split("\0"):
            if "/" in item:
                tracked.add(item.split("/", 1)[0])
        assert tracked == FOLDERS


def test_research_entry_points_and_original_data_remain():
    for name in (
        "README.md", "DATASHEET.md", "MODEL_CARD.md",
        "USAGE_AND_PERMISSIONS.md", "LICENSE", "CITATION.cff",
        "data/all_observations.csv", "notebooks/Capstone_Final_Walkthrough.ipynb",
        "docs/methods.md", "docs/reconstruction.md",
        "docs/visualisations.md", "docs/gp_replay.md",
        "docs/historical_replay.md", "archive/round_10/README.md",
    ):
        assert (ROOT / name).is_file(), name
    for function in range(1, 9):
        for file in ("README.md", "observations.csv", "selection_history.csv", "progress.svg"):
            assert (ROOT / f"functions/F{function}/{file}").is_file()
    for n in range(1, 14):
        assert (ROOT / f"journey/round_{n:02d}/README.md").is_file()


def test_original_and_portable_round12_implementations_preserved():
    for filename in (
        "review_round12.py", "robust_and_warp.py", "tpe_local.py",
        "trust_region_ts.py",
    ):
        assert (ROOT / "journey/round_12/original" / filename).is_file()
        assert (ROOT / "journey/round_12/portable" / filename).is_file()
        assert not (ROOT / "src/bbo" / filename).exists()


def test_distinct_replay_routes_and_notebook_workflow_remain():
    assert (ROOT / "scripts/replay_surrogates.py").is_file()
    assert (ROOT / "scripts/historical_replay.py").is_file()
    assert (ROOT / ".github/workflows/notebook-25-3.yml").is_file()


def test_retired_process_documents_are_not_linked_from_active_guides():
    retired = (
        "EVIDENCE_RULES.md", "VERIFIED_FACTS.md",
        "WEEKLY_SUBMISSION_EVIDENCE.md", "function_datasheets.md",
    )
    for filename in retired:
        assert not (ROOT / "docs" / filename).exists()
    pages = [
        ROOT / "README.md", ROOT / "functions/README.md",
        ROOT / "journey/README.md", ROOT / "notebooks/README.md",
        *sorted((ROOT / "docs").glob("*.md")),
    ]
    for page in pages:
        content = page.read_text(encoding="utf-8")
        for filename in retired:
            assert filename not in content, (page, filename)
