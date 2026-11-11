"""Prevent recurrence of contradictory portal records or stale F7 claims."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bbo.evidence_audit import F7_R11_INPUT, F7_R11_SCORE, audit_portal_history
from bbo.f7_reconstruction import validate_recorded_f7

ROOT = Path(__file__).resolve().parents[1]


def test_every_submitted_point_matches_the_canonical_observations():
    facts = audit_portal_history()
    assert facts["total_observations"] == 279
    assert facts["portal_returns"] == 104
    assert facts["confirmed_f7_r11"] == F7_R11_INPUT
    assert facts["f7_r11_score"] == str(F7_R11_SCORE)


def test_f7_reconstructed_model_matches_43_observations():
    result = validate_recorded_f7()
    assert result["records"] == 43
    assert result["max_absolute_error"] < 3e-14


def test_no_current_document_can_reintroduce_f7_r11_missing_claim():
    # Historical archives may accurately describe an *earlier* incomplete
    # snapshot. Current guides/round summaries must cite the recovery.
    documents = [
        ROOT / "README.md",
        ROOT / "DATASHEET.md",
        ROOT / "MODEL_CARD.md",
        *sorted((ROOT / "docs").glob("*.md")),
        *sorted((ROOT / "final").glob("*.md")),
        *sorted((ROOT / "journey").glob("round_*/README.md")),
        *sorted((ROOT / "functions").glob("F*/README.md")),
    ]
    bad = re.compile(
        r"(?i)(?:R11|round 11|week 11).{0,90}F7.{0,110}"
        r"(?:input|coordinate|vector).{0,60}(?:missing|unavailable|not preserved|unknown)"
        r"|F7.{0,80}(?:R11|round 11|week 11).{0,80}"
        r"(?:input|coordinate|vector).{0,60}(?:missing|unavailable|not preserved|unknown)"
    )
    for page in documents:
        assert not bad.search(page.read_text(encoding="utf-8")), (
            f"Stale recovered-data claim in {page.relative_to(ROOT)}"
        )


def test_final_notebook_has_no_stale_claims_or_broken_local_links():
    path = ROOT / "notebooks/Capstone_Final_Walkthrough.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    markdown = "\n".join(
        "".join(cell["source"]) if isinstance(cell["source"], list)
        else cell["source"]
        for cell in notebook["cells"] if cell["cell_type"] == "markdown"
    )
    assert "0.233000-0.128000-0.522000-0.276000-0.310000-0.667000" in markdown
    assert "3.278967926227992" in markdown
    assert "R11 F7 input remains unavailable" not in markdown
    assert "R11 F7 input remains missing" not in markdown
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", markdown):
        uri = urlsplit(raw.strip())
        if not uri.path or uri.scheme or uri.netloc:
            continue
        location = (path.parent / unquote(uri.path)).resolve()
        assert location.exists(), f"Broken notebook Markdown link: {raw}"
