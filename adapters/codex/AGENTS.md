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

## Path conventions

The user should not need to specify internal paths for standard LLM Wiki operations. Infer the correct wiki locations from the workflow:

- source pages go under `wiki/sources/`;
- concept pages go under `wiki/concepts/`;
- entity pages go under `wiki/entities/` when useful;
- durable saved answers and analyses go under `wiki/syntheses/`;
- open questions go under `wiki/questions/` when they need durable tracking;
- every meaningful wiki change updates `wiki/index.md`;
- every meaningful wiki change appends to `wiki/log.md`;
- raw sources are never modified.

If the user gives a natural prompt such as "ingest this source" or "save that as a synthesis", use these conventions automatically instead of asking the user to name internal paths.

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
