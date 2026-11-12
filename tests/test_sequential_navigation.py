"""Guard sequential reader navigation across all function and round stories.

Every long page has an identical navigation line directly after its title
and again at its end. Boundary pages return to the sequence index instead
of wrapping from the last experiment to the first.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _navigation_line(page: Path, prefix: str) -> str:
    text = page.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.startswith(prefix)]
    assert len(lines) == 2, f"Expected header and footer navigation: {page}"
    assert lines[0] == lines[1], f"Header/footer mismatch: {page}"
    assert text.splitlines()[2] == lines[0], f"Navigation not beside title: {page}"
    assert text.strip().splitlines()[-1] == lines[0], f"Navigation missing at end: {page}"
    return lines[0]


def test_functions_form_a_bidirectional_eight_page_sequence():
    for n in range(1, 9):
        path = ROOT / f"functions/F{n}/README.md"
        nav = _navigation_line(path, "**Function navigation (")
        assert f"({n}/8)" in nav
        assert "[All eight functions](../README.md)" in nav

        if n == 1:
            assert "Previous:" not in nav
        else:
            assert f"[← Previous: F{n-1}](../F{n-1}/README.md)" in nav

        if n == 8:
            assert "Next:" not in nav
        else:
            assert f"[Next: F{n+1} →](../F{n+1}/README.md)" in nav

    index = (ROOT / "functions/README.md").read_text(encoding="utf-8")
    assert "[Start with Function 1](F1/README.md)" in index


def test_rounds_form_a_bidirectional_thirteen_page_sequence():
    for n in range(1, 14):
        path = ROOT / f"journey/round_{n:02d}/README.md"
        nav = _navigation_line(path, "**Round navigation (")
        assert f"({n}/13)" in nav
        assert "[All thirteen rounds](../README.md)" in nav

        if n == 1:
            assert "Previous:" not in nav
        else:
            assert (
                f"[← Previous: Round {n-1}](../round_{n-1:02d}/README.md)"
                in nav
            )

        if n == 13:
            assert "Next:" not in nav
        else:
            assert f"[Next: Round {n+1} →](../round_{n+1:02d}/README.md)" in nav

    index = (ROOT / "journey/README.md").read_text(encoding="utf-8")
    assert "[Start at Round 1](round_01/README.md)" in index
