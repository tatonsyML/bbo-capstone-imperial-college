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
        assert len(re.findall(r"^\*\*Code and data:", body,
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


def test_function_rounds_are_reader_first_and_preserve_experiments():
    """Every round should prioritise experiment, result and useful code links."""
    for function in range(1, 9):
        body = (ROOT / f"functions/F{function}/README.md").read_text(
            encoding="utf-8"
        )
        blocks = re.findall(r"<details>\s*<summary><strong>Round (\d+).*?</details>",
                            body, flags=re.DOTALL)
        assert [int(n) for n in blocks] == list(range(1, 14)), function
        assert body.count("**Code and data:**") == 13, function
        for phrase in (
            "Source discipline:",
            "**Provenance:**",
            "early-round attribution partly retrospective",
            "No separate candidate-generator source authenticated",
            "No authenticated standalone Round 7 selector",
            "the original selection script is not available",
            "all eight match portal inputs",
            "Next-round audit of Week 7 forecasts",
        ):
            assert phrase not in body, (function, phrase)
        assert body.count("selection_history.csv") == 1, function
        round_contents = re.findall(r"<details>(.*?)</details>", body,
                                    flags=re.DOTALL)
        assert len(round_contents) == 13
        for round_number, block in enumerate(round_contents, 1):
            assert "**Submitted input:**" in block, (function, round_number)
            assert ("**Actual portal result:**" in block
                    or "**Actual portal output:**" in block), (function, round_number)
            assert "**Code and data:**" in block, (function, round_number)
            assert "Best " in block and "before → after:" in block, (function, round_number)
            if function in (1, 3, 4, 5, 6, 7):
                assert "**Why this input:**" in block
                assert "**What I learnt:**" in block
                assert ("**Approach:**" in block
                        or "**Approach considered:**" in block)
            else:
                assert "**Decision context:**" in block
                assert "**Evaluation:**" in block
                assert "**What changed for the next round:**" in block


def test_no_future_results_in_earlier_round_explanations():
    """A later portal return must not be presented as an earlier decision."""
    def round_block(function, round_number):
        body = (ROOT / f"functions/F{function}/README.md").read_text(
            encoding="utf-8"
        )
        chunks = re.findall(r"<details>(.*?)</details>", body,
                            flags=re.DOTALL)
        return chunks[round_number - 1]

    for function, current, next_result in (
        (3, 11, "-0.0226526646178297"),
        (3, 12, "-0.0037530969187192596"),
        (4, 10, "0.7304594213260924"),
        (6, 11, "-0.03751864724436928"),
        (7, 10, "3.278967926227992"),
        (7, 11, "3.3223680113931557"),
    ):
        assert next_result not in round_block(function, current), (
            function, current, next_result
        )
    assert "Week 12 repeat reproduced" not in round_block(4, 11)
    assert "the original selection script is not available" not in round_block(7, 11)
