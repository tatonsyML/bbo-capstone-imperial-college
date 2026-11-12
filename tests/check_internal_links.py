"""Validate local Markdown paths, GitHub heading anchors, and notebook Markdown links.

Code cells and fenced examples are not inspected. External URLs are excluded.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MD_LINK = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
HTML_LINK = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']')
FENCE = re.compile(r'^\s{0,3}(\x60{3,}|~{3,})')
ATX = re.compile(r'^\s{0,3}#{1,6}(?:[ \t]+|$)(.*?)\s*$')
SETEXT = re.compile(r'^\s{0,3}(?:={2,}|-{2,})\s*$')
EXPLICIT_ID = re.compile(
    r'<(?:a|span|h[1-6])\b[^>]*?\b(?:id|name)\s*=\s*["\']([^"\']+)["\']',
    re.IGNORECASE,
)
INLINE_LINK = re.compile(r'!?\[([^\]]*)\]\([^)]+\)')
INLINE_REFERENCE = re.compile(r'!?\[([^\]]+)\]\[[^\]]*\]')
HTML_TAG = re.compile(r'<[^>]+>')


def markdown_cells(document: Path) -> list[str]:
    if document.suffix.lower() == ".ipynb":
        notebook = json.loads(document.read_text(encoding="utf-8"))
        return [
            "".join(cell.get("source", []))
            if isinstance(cell.get("source", []), list)
            else str(cell.get("source", ""))
            for cell in notebook.get("cells", [])
            if cell.get("cell_type") == "markdown"
        ]
    return [document.read_text(encoding="utf-8")]


def outside_fences(source: str) -> str:
    output = []
    active_char = None
    active_length = 0
    for line in source.splitlines():
        match = FENCE.match(line)
        if active_char is None:
            if match:
                active_char, active_length = match.group(1)[0], len(match.group(1))
                output.append("")
            else:
                output.append(line)
        elif match and match.group(1)[0] == active_char and len(match.group(1)) >= active_length:
            active_char = None
            output.append("")
        else:
            output.append("")
    return "\n".join(output)


def github_slug(title: str) -> str:
    title = html.unescape(title.strip())
    title = INLINE_LINK.sub(r"\1", title)
    title = INLINE_REFERENCE.sub(r"\1", title)
    title = HTML_TAG.sub("", title)
    title = re.sub(r"[^\w\s-]", "", title.lower())
    return re.sub(r"\s", "-", title.strip())


def heading_anchors(document: Path) -> set[str]:
    found = set()
    used = {}
    for cell in markdown_cells(document):
        lines = outside_fences(cell).splitlines()
        for index, line in enumerate(lines):
            found.update(html.unescape(key) for key in EXPLICIT_ID.findall(line))
            match = ATX.match(line)
            if match:
                title = re.sub(r"\s+#+\s*$", "", match.group(1))
            elif index + 1 < len(lines) and SETEXT.match(lines[index + 1]) and line.strip():
                title = line
            else:
                continue
            slug = github_slug(title)
            count = used.get(slug, 0)
            used[slug] = count + 1
            found.add(f"{slug}-{count}" if count else slug)
    return found


def inspect_link(document: Path, raw: str, root: Path, cache: dict):
    raw = raw.strip().split(' "', 1)[0].split(" '", 1)[0]
    raw = raw.strip("<>").strip()
    if not raw:
        return None
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc or parts.path.startswith("//"):
        return None
    path = unquote(parts.path)
    if not path or path == ".":
        target = document.resolve()
    elif path.startswith("/"):
        target = (root / path.lstrip("/")).resolve()
    else:
        target = (document.parent / path).resolve()
    if not target.is_relative_to(root):
        return f"OUTSIDE REPOSITORY: {raw}"
    if not target.exists():
        return f"MISSING FILE: {raw}"
    if not parts.fragment:
        return None
    anchor_document = target / "README.md" if target.is_dir() else target
    if anchor_document.suffix.lower() not in (".md", ".ipynb"):
        return None
    if not anchor_document.is_file():
        return f"MISSING ANCHOR DOCUMENT: {raw}"
    if anchor_document not in cache:
        cache[anchor_document] = heading_anchors(anchor_document)
    fragment = unquote(parts.fragment)
    if fragment not in cache[anchor_document]:
        return f"MISSING HEADING ANCHOR: {raw}"
    return None


def check(root: Path = ROOT) -> int:
    root = root.resolve()
    markdowns = sorted(root.rglob("*.md"))
    notebooks = sorted(root.rglob("*.ipynb"))
    cache = {}
    broken = []
    total = 0
    for document in [*markdowns, *notebooks]:
        for source in markdown_cells(document):
            visible = outside_fences(source)
            for regex in (MD_LINK, HTML_LINK):
                for match in regex.finditer(visible):
                    url = match.group(1)
                    issue = inspect_link(document, url, root, cache)
                    if issue is None and (url.startswith(("http://", "https://", "mailto:"))):
                        continue
                    total += 1
                    if issue:
                        broken.append((document.relative_to(root), issue))
    for path, issue in broken:
        print(f"BROKEN {path}: {issue}")
    print(
        f"Checked {total} internal links in {len(markdowns)} Markdown files "
        f"and {len(notebooks)} notebooks; {len(broken)} broken."
    )
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(check())
