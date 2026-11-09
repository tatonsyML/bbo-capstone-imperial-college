"""Check local Markdown links throughout the project, including assessed copies.

Only path existence is checked: fragment anchors may differ in GitHub's
rendering and are deliberately ignored to avoid false positive warnings.
External URLs and anchors referring to the same document are also skipped.
"""
from __future__ import annotations

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MD_LINK = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
HTML_LINK = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']')


def target_for(markdown: Path, raw: str) -> Path | None:
    # Strip optional Markdown link titles while preserving ordinary URLs.
    raw = raw.strip().split(' "', 1)[0].split(" '", 1)[0]
    raw = raw.strip("<>").strip()
    if not raw or raw.startswith("#"):
        return None
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc:
        return None
    path = unquote(parts.path)
    if not path or path.startswith("//"):
        return None
    if path.startswith("/"):
        # GitHub Markdown repo-root links with a leading slash are ambiguous.
        return ROOT / path.lstrip("/")
    return (markdown.parent / path).resolve()


def check() -> int:
    missing = []
    total = 0
    documents = list(ROOT.rglob("*.md"))
    for page in documents:
        content = page.read_text(encoding="utf-8")
        # Ignore fenced-code blocks, where link syntax can be an example.
        active, lines = False, []
        for line in content.splitlines():
            if line.lstrip().startswith(("~~~", "```")):
                active = not active
                continue
            if not active:
                lines.append(line)
        source = "\n".join(lines)
        for expr in (MD_LINK, HTML_LINK):
            for match in expr.finditer(source):
                url = match.group(1)
                target = target_for(page, url)
                if target is None:
                    continue
                total += 1
                if not target.exists():
                    missing.append((page.relative_to(ROOT), url, target))
    for page, link, target in missing:
        print(f"MISSING {page}: {link} -> {target}")
    print(f"Checked {total} internal links in {len(documents)} Markdown files; {len(missing)} broken.")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(check())
