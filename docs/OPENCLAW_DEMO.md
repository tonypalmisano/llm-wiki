# OpenClaw Demo Workflow

This walkthrough explains how to install and test the OpenClaw adapter in a fresh OpenClaw workspace.

## 1. Create a fresh demo workspace

Create a workspace outside this repository:

```bash
mkdir llm-wiki-openclaw-demo
cd llm-wiki-openclaw-demo
```

## 2. Copy the OpenClaw skill

From this repository, copy:

```text
adapters/openclaw/skills/llm_wiki
```

into the demo workspace:

```text
<workspace>/skills/llm_wiki
```

For example:

```bash
mkdir -p skills
cp -R /path/to/llm-wiki/adapters/openclaw/skills/llm_wiki skills/llm_wiki
```

## 3. Start or restart OpenClaw

Start or restart OpenClaw from the demo workspace so the workspace skill is discovered.

If OpenClaw provides a skills list command in your version, use it to verify that `llm_wiki` is available.

## 4. Initialize the vault

Use the slash command:

```text
/llm_wiki init .
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

## 5. Add an example source

Save this text as:

```text
raw/inbox/example-source.md
```

```md
# Example source

Temporary RAG-style retrieval can answer a question by fetching relevant fragments from raw documents at query time.

LLM Wiki uses a different pattern: an LLM incrementally builds a persistent Markdown wiki with source pages, concept pages, synthesis pages, links, contradictions and a chronological log.

This makes the knowledge base easier to inspect, revise and extend across sessions.
```

## 6. Ingest the source

Use a slash command:

```text
/llm_wiki ingest raw/inbox/example-source.md
```

You can also use a natural prompt, for example:

```text
Use llm_wiki and ingest raw/inbox/example-source.md into the wiki.
```

Expected behavior:

- create or update a source page under `wiki/sources/`;
- create or update concept pages under `wiki/concepts/`;
- create or update entity pages under `wiki/entities/` when useful;
- update `wiki/index.md`;
- append to `wiki/log.md`;
- leave the raw source unchanged.

## 7. Query the wiki

Use:

```text
/llm_wiki query Why is LLM Wiki different from temporary RAG-style retrieval?
```

Expected behavior:

- read `wiki/index.md`;
- inspect relevant source, concept or synthesis pages;
- answer with wiki/source citations;
- preserve uncertainty when evidence is incomplete.

If the answer has durable value, ask OpenClaw to save it:

```text
Save that answer as a synthesis.
```

Expected behavior:

- create or update a synthesis page under `wiki/syntheses/`;
- include review metadata when possible;
- update `wiki/index.md`;
- append to `wiki/log.md`.

## 8. Lint the wiki

Use:

```text
/llm_wiki lint
```

Expected behavior:

- report structural problems separately from human review warnings;
- structural problems indicate vault hygiene issues such as missing files, broken links or orphan content pages;
- review warnings indicate synthesis pages that may deserve human review.

## Backend mode

OpenClaw `memory-wiki` is optional.

If available, it can be used as an advanced backend. Otherwise, the OpenClaw skill operates in plain Markdown fallback mode using the `raw/` and `wiki/` structure described above.
