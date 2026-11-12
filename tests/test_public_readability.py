"""Keep the public BBO narrative focused on experiments, not file restoration."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_thirteen_round_pages_have_no_repeated_editorial_disclaimers():
    for round_number in range(1, 14):
        page = ROOT / f"journey/round_{round_number:02d}/README.md"
        body = page.read_text(encoding="utf-8")
        assert "About this account" not in body, page
        assert "52-page" not in body, page
        assert "## Verified results, methods and original evidence" not in body, page
        assert "## My reasoning at the time" in body, page
        assert "## How I approached this round" in body, page
    journey = (ROOT / "journey/README.md").read_text(encoding="utf-8")
    assert "draws on my research notes" in journey
    assert "identified separately from forecasts" in journey


def test_function_pages_do_not_repeat_absence_of_numerical_forecasts():
    for function_number in range(1, 9):
        page = ROOT / f"functions/F{function_number}/README.md"
        body = page.read_text(encoding="utf-8")
        assert "52-page" not in body, page
        assert "**How to read the evidence:**" not in body, page
        assert "no value has been invented" not in body.lower(), page
        assert "Broad modelling discussion is not represented" not in body, page
        assert "**Question and context:** **Historical evidence:**" not in body, page
        assert body.count("<details>") == body.count("</details>") == 13
        assert len(re.findall(r"^\*\*(?:Code and evidence|Supporting material):", body,
                              flags=re.MULTILINE)) == 13
        assert not any(
            "…" in line
            for line in body.splitlines() if line.startswith("<summary>")
        ), page


def test_real_forecasts_and_source_guidance_remain_available():
    intro = (ROOT / "functions/README.md").read_text(encoding="utf-8")
    assert "**Forecasts and evidence:**" in intro
    assert "source evidence audit" in intro
    for function in (2, 3, 5, 7):
        page = (ROOT / f"functions/F{function}/README.md").read_text(
            encoding="utf-8"
        )
        assert "**Forecast preserved before the Round 8 return:**" in page
    f8 = (ROOT / "functions/F8/README.md").read_text(encoding="utf-8")
    assert "**Prospective GP-kernel predictions:**" in f8
    for function in (1, 2, 3, 4, 5, 6, 7, 8):
        assert (ROOT / f"functions/F{function}/selection_history.csv").is_file()
