# AGENTS.md — LLM Wiki Project Guidance for Codex

This repository uses the LLM Wiki workflow.

## Working agreement

When asked to work on a knowledge base:

1. Use the `llm-wiki` skill when available.
2. Treat `raw/` as immutable source material.
3. Maintain generated knowledge under `wiki/`.
4. Update `wiki/index.md` and `wiki/log.md` after meaningful changes.
5. Never invent citations.
6. Preserve uncertainty and contradictions.
7. Prefer small, reviewable edits.

## Preferred commands

```bash
python3 core/scripts/check_wiki.py .
```

## Repository structure

```text
core/                # shared method
adapters/            # agent-specific packaging
examples/demo-vault/ # sample vault
```
