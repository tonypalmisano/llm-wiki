# Codex Demo Workflow

This walkthrough captures the successful Codex demo flow for using LLM Wiki with natural prompts.

## 1. Create a new demo project

```bash
mkdir llm-wiki-codex-demo
cd llm-wiki-codex-demo
```

## 2. Copy Codex project guidance

From this repository:

```bash
cp /path/to/llm-wiki/adapters/codex/AGENTS.md ./AGENTS.md
```

## 3. Copy the Codex skill

```bash
mkdir -p .agents/skills
cp -R /path/to/llm-wiki/adapters/codex/.agents/skills/llm-wiki .agents/skills/llm-wiki
```

Codex should now be able to discover the `llm-wiki` skill from the project.

## 4. Initialize the vault

Ask Codex:

```text
Use the llm-wiki skill and initialize an LLM Wiki vault here.
```

Expected result:

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

## 5. Add a source

Create or copy a Markdown source into `raw/inbox/`, for example:

```text
raw/inbox/example-source.md
```

## 6. Ingest with a natural prompt

Ask Codex:

```text
Use llm-wiki and ingest this source: raw/inbox/example-source.md
```

Expected behavior:

- create or update a source page under `wiki/sources/`;
- create or update concept pages under `wiki/concepts/`;
- create or update entity pages under `wiki/entities/` when useful;
- update `wiki/index.md`;
- append to `wiki/log.md`;
- leave the raw source unchanged.

The user should not need to specify these internal paths.

## 7. Create a synthesis with a natural prompt

Ask a question that should produce durable analysis:

```text
What are the main takeaways from the wiki so far?
```

Then ask:

```text
Save that as a synthesis.
```

Expected behavior:

- create or update a synthesis page under `wiki/syntheses/`;
- include review metadata when possible;
- update `wiki/index.md`;
- append to `wiki/log.md`.

## 8. Run the checker

If this repository's checker is available in the demo project, run:

```bash
python3 core/scripts/check_wiki.py .
```

If only the Codex skill was copied, use the vendored checker:

```bash
python3 .agents/skills/llm-wiki/scripts/check_wiki.py .
```

Codex should summarize structural problems separately from human review warnings.
