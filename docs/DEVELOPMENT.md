# Development

This document keeps the operational and development notes for the LLM Wiki repository.

## Repository Structure

The first prototype was an OpenClaw skill only:

```text
skills/llm_wiki/SKILL.md
```

The current repository separates the shared workflow from agent-specific adapters:

```text
core/                         # Agent-independent method, templates, scripts
adapters/openclaw/             # OpenClaw skill adapter
adapters/claude-code/          # Claude Code skill adapter
adapters/codex/                # Codex Agent Skill + AGENTS.md guidance
adapters/opencode/             # OpenCode AGENTS.md + command files
examples/demo-vault/           # Small demo vault
docs/                          # Design notes, migration guide, development notes
scripts/                       # Repository consistency checks
```

## Core Is Canonical

`core/` is the canonical workflow source. It contains the agent-independent method, templates, schemas and health-check script.

Adapter packages may contain vendored copies of templates and scripts so they can be installed independently. Use `scripts/check_sync.py` to detect drift between canonical core files and vendored adapter copies.

## Adapter Installation

### OpenClaw

```bash
cp -R adapters/openclaw/skills/llm_wiki /path/to/workspace/skills/llm_wiki
```

Then restart or open a new session and invoke:

```text
/llm_wiki init .
/llm_wiki ingest raw/inbox/example.md
/llm_wiki query What changed?
/llm_wiki lint
```

### Claude Code

```bash
mkdir -p .claude/skills
cp -R adapters/claude-code/.claude/skills/llm-wiki .claude/skills/llm-wiki
```

Invoke:

```text
/llm-wiki
```

or ask Claude Code to use the LLM Wiki skill.

### Codex

Codex supports both persistent project guidance via `AGENTS.md` and reusable Agent Skills via `SKILL.md`.

```bash
cp adapters/codex/AGENTS.md ./AGENTS.md
mkdir -p .agents/skills
cp -R adapters/codex/.agents/skills/llm-wiki .agents/skills/llm-wiki
```

Codex scans `.agents/skills` for repository-scoped skills. Use the skill explicitly when needed, or rely on the description for implicit activation.

### OpenCode

```bash
cp adapters/opencode/AGENTS.md ./AGENTS.md
mkdir -p .opencode/commands
cp adapters/opencode/.opencode/commands/*.md .opencode/commands/
```

Then invoke commands such as:

```text
/llm-wiki-init
/llm-wiki-ingest raw/inbox/example.md
/llm-wiki-query What are the main open questions?
/llm-wiki-lint
```

## Repository Checks

```bash
python3 -m py_compile core/scripts/check_wiki.py
python3 core/scripts/check_wiki.py examples/demo-vault
python3 scripts/check_sync.py
```

## Sync Checker

`scripts/check_sync.py` verifies that selected vendored adapter files match their canonical files in `core/`.

It currently checks:

- `check_wiki.py` copies in OpenClaw, Claude Code and Codex adapters;
- `WIKI.md` copies used by OpenClaw and Codex;
- Markdown templates vendored into OpenClaw and Claude Code adapters.

The script is intentionally dependency-free and only reports drift. It does not rewrite files.

## Safety Principles

- Never modify raw sources.
- Never invent citations.
- Do not overwrite human-authored notes without explicit instruction.
- Prefer small, reviewable edits.
- Log every ingest, query saved as page, and lint pass.
- Treat third-party skills and scripts as untrusted before review.

## OpenClaw And ClawHub

OpenClaw is the first adapter intended for separate publication on ClawHub.

For ClawHub publication, keep the local folder as:

```text
adapters/openclaw/skills/llm_wiki
```

Publish with the slug:

```text
llm-wiki
```

Do not publish from this repository automatically. Review the adapter package before publishing.

## Licensing Notes

This repository is licensed under MIT.

ClawHub currently publishes submitted skills under MIT-0. If the OpenClaw adapter is published to ClawHub, treat that published skill package as MIT-0 while the repository remains MIT.

## Related Documents

- `docs/DESIGN_NOTES.md`
- `docs/MIGRATION_FROM_V0_1.md`
