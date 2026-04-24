# Migration from the OpenClaw-first ZIP

The v0.1 ZIP was useful as a first working prototype, but it mixed the core LLM Wiki method with the OpenClaw delivery format.

## Old structure

```text
skills/llm_wiki/
  SKILL.md
  templates/
  scripts/
  examples/
codex-prompts/
README.md
```

## New structure

```text
core/
  WIKI.md
  templates/
    AGENTS.md
  scripts/
  schemas/

adapters/
  openclaw/
  claude-code/
  codex/
  opencode/

examples/
docs/
```

## Mapping

| v0.1 item | v0.2 location |
|---|---|
| `skills/llm_wiki/SKILL.md` | `adapters/openclaw/skills/llm_wiki/SKILL.md` |
| `skills/llm_wiki/templates/*` | `core/templates/*` and copied into selected adapters when useful |
| `skills/llm_wiki/scripts/check_wiki.py` | `core/scripts/check_wiki.py`; adapter copies may reference or include it |
| `codex-prompts/implement-local.md` | replaced by `adapters/codex/AGENTS.md` and `adapters/codex/.agents/skills/llm-wiki/SKILL.md` |
| root README | expanded to multi-agent README |

## Practical rule

Keep the OpenClaw adapter as the publishable ClawHub package, but keep the public GitHub repo multi-agent.

For v0.2.1 and later, `core/` is the canonical workflow source. Adapter copies are vendored for installability and should be checked with `python3 scripts/check_sync.py`.
