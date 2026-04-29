# ClawHub Publishing Notes

These notes prepare the OpenClaw adapter for possible future ClawHub
publication. Do not publish automatically.

## Candidate Skill Folder

Publish this folder:

```text
adapters/openclaw/skills/llm_wiki
```

## Intended Slug

Use this ClawHub slug:

```text
llm-wiki
```

The local folder uses `llm_wiki` for OpenClaw workspace compatibility, while the
public package slug should be URL-friendly.

## Licensing

The main repository remains MIT licensed.

ClawHub-published skills are subject to ClawHub MIT-0 publication terms. Treat
the published skill package as MIT-0 while the repository remains MIT.

Do not add license terms to the skill package that conflict with ClawHub MIT-0
publication.

## Pre-Publish Checklist

Before publishing, inspect:

- `adapters/openclaw/skills/llm_wiki/SKILL.md`
- `adapters/openclaw/skills/llm_wiki/README.md`
- `adapters/openclaw/skills/llm_wiki/scripts/`
- `adapters/openclaw/skills/llm_wiki/templates/`

Verify:

- no secrets are included;
- no remote code is downloaded or executed;
- no dependencies are installed automatically;
- memory-wiki remains optional;
- plain Markdown fallback remains documented;
- scripts are dependency-free and reviewable;
- templates contain no private project data;
- the homepage points to `https://github.com/tonypalmisano/llm-wiki`;
- the intended slug is `llm-wiki`.

Run local repository checks:

```bash
python3 core/scripts/check_wiki.py examples/demo-vault
python3 scripts/check_sync.py
```

## Example Commands To Verify

ClawHub CLI commands can change. Verify current ClawHub documentation before
running any publish command.

Possible command shapes may look like:

```bash
clawhub skill validate adapters/openclaw/skills/llm_wiki
clawhub skill publish adapters/openclaw/skills/llm_wiki --slug llm-wiki
```

Treat these as examples only. Do not run them until they are checked against the
current ClawHub CLI docs.
