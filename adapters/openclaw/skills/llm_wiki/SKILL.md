---
name: llm_wiki
description: Maintain a Markdown-first LLM Wiki knowledge base from immutable raw sources. Use for /llm_wiki init, ingest, query, lint, compile, and for persistent wiki maintenance workflows. If OpenClaw memory-wiki is available, prefer it as an advanced backend; otherwise operate directly on Markdown files.
version: 0.2.1
homepage: https://github.com/tonypalmisano/llm-wiki
license: MIT-0
---

# LLM Wiki Skill for OpenClaw

You are maintaining a persistent, compounding Markdown knowledge base.

## When to use

Use this skill when the user asks to:

- initialize an LLM Wiki vault;
- ingest a document into a wiki;
- update entity, concept, source or synthesis pages;
- answer a question from the wiki;
- save an answer back into the wiki;
- lint or health-check a wiki;
- prepare the wiki for Obsidian or Git.

## Backend selection

Before acting, determine the available backend.

### Preferred backend: OpenClaw memory-wiki

If `openclaw wiki status` or equivalent tooling is available and the user wants OpenClaw-native behavior, use the memory-wiki backend when appropriate.

Useful commands may include:

```bash
openclaw wiki init
openclaw wiki status
openclaw wiki ingest <path-or-url>
openclaw wiki compile
openclaw wiki lint
openclaw wiki search <query>
openclaw wiki get <page>
```

### Fallback backend: plain Markdown

If memory-wiki is not available, operate directly on files:

```text
raw/
  inbox/
  processed/
  assets/

wiki/
  WIKI.md
  AGENTS.md
  index.md
  log.md
  sources/
  entities/
  concepts/
  syntheses/
  questions/
```

## Commands

### `/llm_wiki init [path]`

Create the vault structure. Copy templates if available. Do not overwrite existing files without asking or creating a backup.

### `/llm_wiki ingest <source-path>`

1. Read the source.
2. Create or update a source page under `wiki/sources/`.
3. Extract entities, concepts, claims and contradictions.
4. Update relevant entity and concept pages.
5. Update `wiki/index.md`.
6. Append to `wiki/log.md`.
7. Report changed files.

### `/llm_wiki query <question>`

1. Read `wiki/index.md`.
2. Locate relevant wiki pages.
3. Read source pages when evidence is needed.
4. Answer with citations to wiki/source pages.
5. If the answer is durable, ask whether to save it as a synthesis page unless the user already requested saving.

### `/llm_wiki lint`

Check for:

- broken links;
- orphan pages;
- stale claims;
- contradictions;
- missing source references;
- pages missing frontmatter;
- index/log inconsistency.

Use `scripts/check_wiki.py` if available, but also reason semantically about the wiki.

### `/llm_wiki compile`

Refresh derived pages such as index, dashboards, topic maps, and summary tables.

## Strict rules

- Never modify raw sources.
- Never invent citations.
- Preserve uncertainty.
- Prefer small, reviewable edits.
- Log every meaningful operation.
- If a new source contradicts an old claim, mark the contradiction rather than silently overwriting it.
