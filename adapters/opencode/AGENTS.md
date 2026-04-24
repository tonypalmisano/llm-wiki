# AGENTS.md — LLM Wiki Guidance for OpenCode

Use this project as an LLM Wiki workspace.

## Rules

- `raw/` contains immutable sources.
- `wiki/` contains generated/maintained Markdown pages.
- Update `wiki/index.md` and `wiki/log.md` after every meaningful operation.
- Do not invent citations.
- Preserve contradictions and uncertainty.
- Prefer small patches.

## Main workflows

Use the custom commands in `.opencode/commands/`:

- `/llm-wiki-init`
- `/llm-wiki-ingest <source>`
- `/llm-wiki-query <question>`
- `/llm-wiki-lint`
