# LLM Wiki

> A Markdown-first workflow for building persistent, LLM-maintained knowledge bases.

## What is LLM Wiki?

LLM Wiki is an agent-agnostic workflow for turning raw sources into a persistent Markdown wiki maintained by LLM agents.

Instead of treating each prompt as a temporary retrieval session, LLM Wiki gives agents a durable workspace: raw inputs stay immutable, while the wiki accumulates source pages, entity pages, concept pages, syntheses, questions, links and logs.

The core workflow is plain Markdown. Agent-specific adapters translate that workflow into native formats for tools such as OpenClaw, Claude Code, Codex and OpenCode.

## Why it matters

Most RAG workflows retrieve fragments at query time. That is useful, but the model starts over repeatedly: it finds relevant chunks, answers the immediate question and leaves little durable structure behind.

LLM Wiki is designed for knowledge that compounds. Each ingest can create or update durable pages. Each useful answer can become a synthesis. Contradictions and uncertainty are preserved instead of being silently overwritten. A chronological log records how the knowledge base changed.

The result is a persistent layer of organized knowledge that future agents can inspect, extend and audit.

## How it works

```text
raw sources → LLM-maintained wiki → persistent synthesis
```

1. Add raw material under `raw/`.
2. Ask an LLM agent to ingest one source at a time.
3. The agent creates or updates Markdown pages under `wiki/`.
4. The agent updates `wiki/index.md` and appends to `wiki/log.md`.
5. Durable answers can be saved back into the wiki as synthesis pages.

## Core Ideas

- Markdown-first: the knowledge base remains readable, portable and Git-friendly.
- Agent-agnostic: the method is independent of any one coding agent or LLM tool.
- Source-traceable: wiki pages should point back to raw sources and source pages.
- Cumulative: useful answers, concepts and contradictions become durable knowledge.
- Auditable: changes are reflected in an index and chronological log.

## Repository Layout

```text
core/                 # Agent-independent workflow, templates, schema and checks
adapters/             # Agent-specific packaging
examples/demo-vault/  # Small working demo vault
docs/                 # Design, migration and development notes
scripts/              # Repository consistency checks
```

For adapter installation, development checks and ClawHub publication notes, see [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md).

## Adapters

LLM Wiki currently includes starter adapters for:

- OpenClaw
- Claude Code
- Codex
- OpenCode

OpenClaw is the first adapter intended for separate publication on ClawHub. `memory-wiki` remains an optional advanced OpenClaw backend, not a required dependency.

## Demo

A minimal demo vault is included in [`examples/demo-vault/`](examples/demo-vault/).

Run the structural health check with:

```bash
python3 core/scripts/check_wiki.py examples/demo-vault
```

## Status

Version: 0.2.1 draft  
Scope: multi-agent starter package

## Roadmap

Planned for later versions:

- richer OpenClaw memory-wiki integration;
- structured claim metadata;
- generated reports and dashboards;
- a dedicated CLI;
- CI checks and release automation.

## Author

LLM Wiki is developed by Tonino Palmisano, publishing as Tony Palmisano on GitHub.

Professional project by XIDOA — Tonino Palmisano.

## Attribution

If you use this project in your own work, attribution is appreciated:

LLM Wiki by Tony Palmisano — https://github.com/tonypalmisano/llm-wiki

## License

This repository is licensed under the MIT License.

Copyright (c) 2026 Tonino Palmisano.

ClawHub currently publishes submitted skills under MIT-0. If the OpenClaw adapter is published to ClawHub, treat that published skill package as MIT-0 while the repository remains MIT.
