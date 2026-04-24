# Vault Structure Schema

```text
raw/
  inbox/       # newly added sources
  processed/   # sources already processed
  assets/      # downloaded images and attachments

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

## Naming conventions

- File names should be lowercase kebab-case.
- Page titles should be human-readable.
- Prefer `[[wikilinks]]` between pages.
- Keep source pages traceable to raw files.

## Frontmatter conventions

Content pages in `sources/`, `entities/`, `concepts/`, `syntheses/` and `questions/` should include YAML frontmatter.

Control files may omit frontmatter:

- `WIKI.md`
- `AGENTS.md`
- `index.md`
- `log.md`
