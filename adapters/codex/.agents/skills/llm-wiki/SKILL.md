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

## Natural prompt workflows

The user should not need to specify internal wiki paths for standard operations. Infer the correct locations from the LLM Wiki workflow.

When the user says "ingest this source" or gives an equivalent natural prompt:

1. Treat raw sources as immutable and never modify them.
2. Create or update source pages under `wiki/sources/`.
3. Create or update concept pages under `wiki/concepts/`.
4. Create or update entity pages under `wiki/entities/` when useful.
5. Create synthesis pages under `wiki/syntheses/` when the user asks to save durable answers or lasting analysis.
6. Always update `wiki/index.md`.
7. Always append an entry to `wiki/log.md`.
8. Report changed files, citations used and unresolved uncertainties.

Example user prompts and expected behavior:

- "Ingest this source: raw/inbox/article.md" means read the raw file, create or update the relevant source/concept/entity pages, update `wiki/index.md`, append to `wiki/log.md`, and leave the raw file unchanged.
- "Add these notes to the wiki" means identify the source material, route it into the standard wiki directories, update the index and log, and ask only if the source path is ambiguous.
- "What does the wiki say about this topic?" means read `wiki/index.md`, inspect relevant pages, answer with wiki/source citations, and do not create a synthesis unless asked.
- "Save that as a synthesis" means create or update a durable page under `wiki/syntheses/`, include review metadata when possible, update `wiki/index.md`, and append to `wiki/log.md`.
- "Run a wiki check" means run the local checker when available and summarize both structural problems and review warnings.

## Rules

- Treat raw sources as immutable.
- Never fabricate citations.
- Preserve contradictions and uncertainty.
- Keep edits small and reviewable.
- Update `index.md` and `log.md` whenever the wiki changes.
