# Changelog

## 0.4.2 draft

- Prepared OpenClaw adapter documentation for future ClawHub publication.
- Added package-level README for the OpenClaw skill.
- Added ClawHub publishing notes.
- Added OpenClaw memory-wiki backend notes.

## 0.4.1 draft

- Added documentation for optional PDF ingestion with OpenDataLoader PDF.
- Documented the `raw/converted/` convention for derived PDF artifacts.
- Documented how page/bounding-box metadata can support claim source references.

## 0.4.0 draft

- Added structured claim metadata for synthesis pages.
- Added a claim table to the synthesis template.
- Checker now reports claim-level review warnings.

## 0.3.0 draft

- Added lightweight human review signals for synthesis pages.
- Added review metadata fields to synthesis templates.
- Checker now reports review warnings separately from structural errors.

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
