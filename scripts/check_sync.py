#!/usr/bin/env python3
"""
Check that vendored adapter copies match the canonical core files.

This is intentionally dependency-free. It does not build or rewrite anything;
it only reports drift.
"""

from pathlib import Path
import hashlib


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add_pair(pairs, canonical: str, vendored: str) -> None:
    pairs.append((ROOT / canonical, ROOT / vendored))


def main() -> int:
    pairs = []

    for vendored in [
        "adapters/openclaw/skills/llm_wiki/scripts/check_wiki.py",
        "adapters/claude-code/.claude/skills/llm-wiki/scripts/check_wiki.py",
        "adapters/codex/.agents/skills/llm-wiki/scripts/check_wiki.py",
    ]:
        add_pair(pairs, "core/scripts/check_wiki.py", vendored)

    for vendored in [
        "adapters/openclaw/skills/llm_wiki/templates/WIKI.md",
        "adapters/codex/.agents/skills/llm-wiki/references/WIKI.md",
    ]:
        add_pair(pairs, "core/WIKI.md", vendored)

    for template in sorted((ROOT / "core/templates").glob("*.md")):
        for adapter_templates in [
            "adapters/openclaw/skills/llm_wiki/templates",
            "adapters/claude-code/.claude/skills/llm-wiki/templates",
        ]:
            add_pair(
                pairs,
                str(template.relative_to(ROOT)),
                f"{adapter_templates}/{template.name}",
            )

    problems = []
    for canonical, vendored in pairs:
        if not canonical.exists():
            problems.append(f"MISSING canonical file: {canonical.relative_to(ROOT)}")
            continue
        if not vendored.exists():
            problems.append(f"MISSING vendored copy: {vendored.relative_to(ROOT)}")
            continue
        if digest(canonical) != digest(vendored):
            problems.append(
                f"DRIFT: {vendored.relative_to(ROOT)} differs from {canonical.relative_to(ROOT)}"
            )

    if problems:
        print("LLM Wiki sync check: issues found")
        for problem in problems:
            print("-", problem)
        return 1

    print("LLM Wiki sync check: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
