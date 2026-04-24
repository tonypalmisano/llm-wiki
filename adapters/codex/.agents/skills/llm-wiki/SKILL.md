---
name: llm-wiki
description: Maintain a persistent Markdown LLM Wiki. Use when the task involves ingesting raw sources, updating wiki pages, answering from the wiki, saving syntheses, or linting a Markdown knowledge base.
---

# LLM Wiki Agent Skill for Codex

This skill defines a reusable workflow for maintaining an LLM-generated Markdown wiki.

## When to activate

Activate this skill when the user asks to:

- build or initialize an LLM Wiki;
- ingest documents or notes into a persistent wiki;
- update `index.md`, `log.md`, entity pages or concept pages;
- answer questions from an existing wiki;
- lint a Markdown knowledge base;
- convert a useful answer into a wiki synthesis page.

## Expected structure

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

## Workflow

### Init

Create missing directories and starter files. Do not overwrite existing files.

### Ingest

Process one source at a time. Create a source page, update relevant wiki pages, refresh index, append log entry, and report changes.

### Query

Search the wiki before answering. Use `index.md` as the routing file. Cite the wiki/source files used. Save durable answers only if requested.

### Lint

Run structural checks with `scripts/check_wiki.py` when available, then perform semantic checks manually.

## Rules

- Treat raw sources as immutable.
- Never fabricate citations.
- Preserve contradictions and uncertainty.
- Keep edits small and reviewable.
- Update `index.md` and `log.md` whenever the wiki changes.
