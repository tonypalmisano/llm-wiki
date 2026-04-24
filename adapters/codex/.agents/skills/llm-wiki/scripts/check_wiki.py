#!/usr/bin/env python3
"""
Naive LLM Wiki health check.

This is intentionally simple and dependency-free.
It checks basic Markdown vault hygiene:
- required files;
- broken wikilinks outside fenced code blocks;
- content pages missing frontmatter;
- orphan content pages.
"""

from pathlib import Path
import re
import sys

def slug_to_candidates(link: str):
    clean = link.split("|")[0].strip()
    if clean.endswith(".md"):
        return [clean]
    return [clean + ".md", clean.replace(" ", "-").lower() + ".md"]

def strip_fenced_code_blocks(text: str) -> str:
    stripped = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines():
        marker = line.lstrip()[:3]
        if marker in {"```", "~~~"}:
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            stripped.append("")
            continue

        stripped.append("" if in_fence else line)

    return "\n".join(stripped)

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    wiki = root / "wiki"
    required = [wiki / "WIKI.md", wiki / "AGENTS.md", wiki / "index.md", wiki / "log.md"]
    special_pages = {"WIKI.md", "AGENTS.md", "index.md", "log.md"}
    problems = []

    for path in required:
        if not path.exists():
            problems.append(f"MISSING required file: {path}")

    pages = list(wiki.rglob("*.md")) if wiki.exists() else []
    page_names = {p.name for p in pages}
    page_rel = {str(p.relative_to(wiki)) for p in pages}

    inbound = {p: 0 for p in pages}
    link_re = re.compile(r"\[\[([^\]]+)\]\]")

    for p in pages:
        text = p.read_text(encoding="utf-8", errors="ignore")
        rel = str(p.relative_to(wiki))
        is_special_page = rel in special_pages
        if not is_special_page and not text.startswith("---"):
            problems.append(f"NO FRONTMATTER: {p}")
        link_text = strip_fenced_code_blocks(text)
        for m in link_re.finditer(link_text):
            link = m.group(1)
            candidates = slug_to_candidates(link)
            exists = any(c in page_names or c in page_rel for c in candidates)
            if not exists:
                problems.append(f"BROKEN LINK in {p}: [[{link}]]")
            else:
                for target in pages:
                    if target.name in candidates or str(target.relative_to(wiki)) in candidates:
                        inbound[target] += 1

    for p, count in inbound.items():
        rel = str(p.relative_to(wiki))
        if rel not in special_pages and count == 0:
            problems.append(f"POSSIBLE ORPHAN: {p}")

    if problems:
        print("LLM Wiki health check: issues found")
        for problem in problems:
            print("-", problem)
        return 1

    print("LLM Wiki health check: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
