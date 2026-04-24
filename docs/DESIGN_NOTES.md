# Design Notes

## Why multi-agent?

The LLM Wiki concept is agent-agnostic. OpenClaw is the first target, but the same workflow can be translated to Claude Code, Codex and OpenCode.

## Why keep `core/` separate?

The core should not depend on one agent's packaging format. This makes the method easier to test, document and reuse.

Adapter packages may contain vendored copies of core templates or scripts so each adapter can be installed independently. The canonical source remains `core/`; use `scripts/check_sync.py` to detect drift.

## Why not depend on memory-wiki?

OpenClaw memory-wiki is useful and should be supported as an advanced backend, but LLM Wiki should also work as plain Markdown.

## Publication strategy

- Publish the GitHub repository as multi-agent.
- Publish the OpenClaw adapter to ClawHub with slug `llm-wiki`, even though the local folder remains `llm_wiki`.
- Publish or document the Claude/Codex/OpenCode adapters separately according to each ecosystem.
