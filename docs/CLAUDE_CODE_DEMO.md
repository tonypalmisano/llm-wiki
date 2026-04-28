# Claude Code Demo Workflow

This walkthrough explains how to test LLM Wiki with Claude Code in a fresh demo project.

Claude Code can use an LLM Wiki skill installed under:

```text
.claude/skills/llm-wiki/
```

## 1. Create a fresh demo project

Create a project outside this repository:

```bash
mkdir llm-wiki-claude-code-demo
cd llm-wiki-claude-code-demo
```

## 2. Copy the Claude Code skill

From this repository, copy:

```text
adapters/claude-code/.claude/skills/llm-wiki
```

into the demo project:

```text
<demo-project>/.claude/skills/llm-wiki
```

For example:

```bash
mkdir -p .claude/skills
cp -R /path/to/llm-wiki/adapters/claude-code/.claude/skills/llm-wiki .claude/skills/llm-wiki
```

## 3. Initialize the vault

Ask Claude Code:

```text
Use the llm-wiki skill to initialize an LLM Wiki here.
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
  concepts/
  entities/
  syntheses/
  questions/
```

## 4. Add an example source

Save this text as:

```text
raw/inbox/example-source.md
```

```md
# Example source

Temporary retrieval can answer a question by fetching fragments from raw documents each time.

LLM Wiki uses a persistent Markdown wiki instead: source pages, concept pages, synthesis pages, links and logs can accumulate across sessions.

This gives future LLM agents a durable knowledge layer to inspect and extend.
```

## 5. Ingest with a natural prompt

Ask Claude Code:

```text
Use the llm-wiki skill to ingest raw/inbox/example-source.md.
```

Expected behavior:

- create or update a source page under `wiki/sources/`;
- create or update concept pages under `wiki/concepts/`;
- create entity pages under `wiki/entities/` when useful;
- update `wiki/index.md`;
- append to `wiki/log.md`;
- leave the raw source unchanged.

## 6. Create a durable synthesis

Ask:

```text
What are the durable takeaways from the wiki so far?
```

Then ask:

```text
Save that as a synthesis.
```

Expected behavior:

- create or update a synthesis page under `wiki/syntheses/`;
- include review metadata and human review signals where possible;
- update `wiki/index.md`;
- append to `wiki/log.md`.

## 7. Run a wiki health check

Ask Claude Code:

```text
Use the llm-wiki skill to run a wiki health check.
```

Expected behavior:

- inspect structural wiki health;
- report missing files, broken links or orphan content pages;
- report synthesis review warnings separately from structural problems.
