# OpenClaw memory-wiki Backend Notes

LLM Wiki is Markdown-first and agent-agnostic. OpenClaw `memory-wiki` is an
optional OpenClaw-native backend for users who want deeper OpenClaw integration.

memory-wiki is not a required dependency. Plain Markdown fallback remains the
default portable behavior.

## What Integration Means

In LLM Wiki, memory-wiki integration means adapter-level backend selection inside
the OpenClaw skill.

It does not mean:

- replacing the core Markdown workflow;
- making memory-wiki mandatory;
- duplicating memory-wiki internals;
- changing non-OpenClaw adapters;
- changing the core checker or templates.

The OpenClaw adapter may use memory-wiki commands when available, but it should
preserve the visible LLM Wiki contract: raw sources, wiki pages, index, log,
syntheses, review signals and claim metadata.

## Backend Modes

### Plain Markdown fallback

Disclosure:

```text
Backend: plain Markdown fallback
```

Use this mode when:

- memory-wiki is unavailable;
- the user wants a portable Markdown vault;
- OpenClaw commands are missing, ambiguous or insufficient;
- compatibility with Git, Obsidian or other agents is the priority.

This is the default mode.

### OpenClaw memory-wiki backend

Disclosure:

```text
Backend: OpenClaw memory-wiki
```

Use this mode when:

- memory-wiki is available;
- the user wants OpenClaw-native behavior;
- the requested operation maps cleanly to memory-wiki commands.

Useful OpenClaw commands may include:

```bash
openclaw wiki status
openclaw wiki init
openclaw wiki ingest <path-or-url>
openclaw wiki compile
openclaw wiki lint
openclaw wiki search <query>
openclaw wiki get <page>
```

Verify command availability in the user's installed OpenClaw version before
depending on specific command behavior.

### Hybrid compatibility mode

Use hybrid mode when memory-wiki helps with search, compile, status or ingest,
but the visible LLM Wiki vault still needs Markdown interoperability.

In hybrid mode, the adapter should:

- use memory-wiki only for operations it clearly supports;
- keep `wiki/index.md` and `wiki/log.md` understandable;
- preserve LLM Wiki page conventions;
- preserve synthesis review signals and claim metadata;
- report which backend handled each meaningful operation.

## Always Available In Plain Markdown

The following must remain available without memory-wiki:

- vault initialization;
- source ingest from Markdown or raw files;
- source pages under `wiki/sources/`;
- concept pages under `wiki/concepts/`;
- entity pages under `wiki/entities/`;
- synthesis pages under `wiki/syntheses/`;
- question pages under `wiki/questions/`;
- `wiki/index.md`;
- `wiki/log.md`;
- synthesis review metadata;
- structured claim metadata;
- local structural checks.

## When memory-wiki Is Available

The OpenClaw adapter should:

1. Determine whether memory-wiki commands are available.
2. Use memory-wiki only if the user wants OpenClaw-native behavior or the task
   clearly benefits from it.
3. Disclose:

   ```text
   Backend: OpenClaw memory-wiki
   ```

4. Preserve LLM Wiki safety rules:
   - never modify raw sources;
   - never invent citations;
   - preserve uncertainty;
   - log meaningful operations.
5. Preserve or restore LLM Wiki-visible artifacts where needed:
   - index;
   - log;
   - source traceability;
   - synthesis review metadata;
   - claim metadata.

## When memory-wiki Is Not Available

The OpenClaw adapter should:

1. Continue without asking the user to install memory-wiki.
2. Disclose:

   ```text
   Backend: plain Markdown fallback
   ```

3. Operate directly on Markdown files.
4. Use bundled templates and scripts when available.
5. Report that memory-wiki was not used, but do not treat that as an error.

## Fallback Behavior

Fall back to plain Markdown mode when:

- `openclaw wiki status` or equivalent commands are unavailable;
- a memory-wiki command fails;
- command behavior is ambiguous;
- output does not preserve LLM Wiki conventions;
- the user requests portable Markdown behavior;
- using memory-wiki would bypass review signals or claim metadata.

Fallback should be explicit and non-fatal:

```text
Backend: plain Markdown fallback
Reason: OpenClaw memory-wiki command was unavailable.
```

## Risks

- Duplicating memory-wiki internals inside the LLM Wiki skill.
- Conflicting ownership between memory-wiki-generated pages and direct Markdown
  edits.
- Making users think memory-wiki is required.
- Weakening LLM Wiki's agent-agnostic positioning.
- Bypassing synthesis review signals or structured claim metadata.
- Depending on OpenClaw command behavior that may change across versions.
- Producing output that the local Markdown checker cannot inspect.

## Out Of Scope

- Installing OpenClaw or memory-wiki.
- Reimplementing memory-wiki storage, search, compile or lint internals.
- Requiring memory-wiki in CI.
- Changing core templates or checker behavior.
- Changing Codex, Claude Code or OpenCode adapters.
- Automatic migration between plain Markdown and memory-wiki storage.
- Certifying truth or resolving contradictions automatically.

The intended integration path is documentation and OpenClaw adapter guidance
first. Code should only be added after memory-wiki behavior is verified against a
real installed OpenClaw version.
