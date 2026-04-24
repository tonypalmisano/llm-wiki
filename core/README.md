# Core LLM Wiki Workflow

This folder contains the agent-independent LLM Wiki method.

The core workflow does not require OpenClaw, Claude Code, Codex, OpenCode or memory-wiki. It only requires file access to a Markdown workspace.

`core/` is the canonical source for the workflow. Adapter packages may vendor copies of templates and scripts so they can be installed independently.

## Expected vault structure

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

## Operations

- `init`: create the vault structure.
- `ingest`: read one raw source, create a source page, update relevant pages, update index and log.
- `query`: answer from the wiki first; optionally save answer as synthesis page.
- `lint`: inspect health of the wiki.
- `compile`: refresh index-like derived pages if needed.

## Frontmatter rule

Content pages under `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/` and `wiki/questions/` should use frontmatter.

Control files may omit frontmatter:

- `wiki/WIKI.md`
- `wiki/AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`
