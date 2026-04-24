# Changelog

## 0.2.1

- Aligned the wiki checker with the vault schema: special control files may omit frontmatter, and wikilinks inside fenced code blocks are ignored.
- Added the missing `wiki/AGENTS.md` template.
- Updated the demo vault so it passes the structural health check.
- Moved the Codex skill adapter to the repo-scoped `.agents/skills/llm-wiki` layout.
- Added OpenClaw ClawHub metadata and documented the `llm-wiki` publish slug.
- Added `scripts/check_sync.py` to detect drift between canonical core files and vendored adapter copies.
- Restored the full MIT license text.

## 0.2.0

- Reorganized project from OpenClaw-only skill to agent-agnostic multi-adapter package.
- Added shared `core/` workflow and templates.
- Added OpenClaw adapter.
- Added Claude Code adapter.
- Added Codex Agent Skill adapter plus `AGENTS.md` guidance.
- Added OpenCode adapter with custom command files.
- Added demo vault.
- Added migration guide from the v0.1 ZIP.
