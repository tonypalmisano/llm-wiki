# OpenCode Demo Workflow

This walkthrough explains how to test LLM Wiki with OpenCode in a fresh demo project.

OpenCode uses:

- `AGENTS.md`
- `.opencode/commands/*.md`

OpenCode is command-oriented, while Codex and Claude Code are more skill and natural-prompt oriented.

## 1. Create a fresh demo project

Create a project outside this repository:

```bash
mkdir llm-wiki-opencode-demo
cd llm-wiki-opencode-demo
```

## 2. Copy OpenCode project guidance

From this repository, copy:

```text
adapters/opencode/AGENTS.md
```

into the demo project:

```text
<demo-project>/AGENTS.md
```

For example:

```bash
cp /path/to/llm-wiki/adapters/opencode/AGENTS.md ./AGENTS.md
```

## 3. Copy OpenCode commands

From this repository, copy:

```text
adapters/opencode/.opencode/commands/*.md
```

into the demo project:

```text
<demo-project>/.opencode/commands/
```

For example:

```bash
mkdir -p .opencode/commands
cp /path/to/llm-wiki/adapters/opencode/.opencode/commands/*.md .opencode/commands/
```

## 4. Initialize the vault

Run:

```text
/llm-wiki-init
```

Expected result:

- initialized `raw/` and `wiki/` structure;
- `wiki/WIKI.md`;
- `wiki/AGENTS.md`;
- `wiki/index.md`;
- `wiki/log.md`;
- page folders under `wiki/`.

## 5. Add an example source

Save this text as:

```text
raw/inbox/example-source.md
```

```md
# Example source

Temporary retrieval can answer a question by fetching fragments from raw documents at query time.

LLM Wiki turns useful knowledge into a persistent Markdown wiki with source pages, concept pages, synthesis pages, links and a chronological log.

This helps knowledge compound across agent sessions.
```

## 6. Ingest the source

Run:

```text
/llm-wiki-ingest raw/inbox/example-source.md
```

Expected behavior:

- create or update a source page under `wiki/sources/`;
- create or update concept pages under `wiki/concepts/`;
- create entity pages under `wiki/entities/` when useful;
- update `wiki/index.md`;
- append to `wiki/log.md`;
- leave the raw source unchanged.

## 7. Query the wiki

Run:

```text
/llm-wiki-query Why is LLM Wiki different from temporary retrieval?
```

Expected behavior:

- read the wiki before answering;
- cite relevant wiki/source pages;
- create synthesis pages under `wiki/syntheses/` when durable answers are saved;
- update `wiki/index.md` and `wiki/log.md` for saved wiki changes.

## 8. Lint the wiki

Run:

```text
/llm-wiki-lint
```

Expected behavior:

- report structural problems separately from human review warnings;
- identify missing files, broken links or orphan content pages;
- surface synthesis pages that may deserve human review.
