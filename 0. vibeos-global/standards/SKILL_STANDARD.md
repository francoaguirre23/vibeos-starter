# VibeOS Skill Standard

Canonical structure and conventions for VibeOS skills.

This document defines what a skill is, how it is structured, and how it is wired across tools. Use it when adding a new skill or auditing existing ones.

Complements:
- `CLAUDE_CODE_INTEGRATION.md` — how skills become `/commands` in Claude Code

## What a Skill Is

A skill is a reusable workflow definition — a structured prompt that guides a repeatable VibeOS task (spec a build packet, run a conformance check, close a session, etc.).

Skills are **tool-agnostic and canonical**. The single source of truth for each skill is its `SKILL.md` in `2. vibeos-skills/skills/`. Tools dispatch to that file — they never copy its content.

## Folder and File Naming

```
2. vibeos-skills/skills/[skill-name]/
  SKILL.md
  agents/openai.yaml
```

Rules:
- `skill-name` is lowercase, hyphen-separated, and matches the `name` in frontmatter
- One folder per skill, containing `SKILL.md` and `agents/openai.yaml` (the Codex/OpenAI interface descriptor: `display_name`, `short_description`, `default_prompt`)
- The command/skill name is consistent across tools (Codex skill name == Claude Code command name)

## SKILL.md Structure

### Frontmatter (required)

```
---
name: skill-name
description: One sentence describing what the skill does and when to use it.
---
```

### Body sections

| Section | Required? | Purpose |
|---------|-----------|---------|
| Title + one-line intro | Yes | What the skill is |
| `## When to use` | Recommended | Concrete triggers |
| `## Context Requirement` | Yes | What to read first — project context, standards, cognitive files. This is where a skill points at the standards folder or specific source-of-truth files. |
| `## Inputs` | Yes | What the skill consumes |
| `## Process` | Yes | Numbered, ordered steps |
| `## Required output` | Yes | What the skill must produce |
| `## Checks before finalizing` | Yes | A checklist that gates completion |

## Durability Principle

Skills should reference **folders and source-of-truth files**, not enumerate items that change.

- Good: "read all files in `0. vibeos-global/standards/`"
- Fragile: listing each standard file by name (breaks when a standard is added)

This keeps skills durable as the framework grows.

## Cross-Tool Dispatch

Each skill is invoked the same way across tools:
- **Codex** — invokes the `SKILL.md` natively
- **Claude Code** — a thin command at `.claude/commands/[skill-name].md` reads and executes the canonical `SKILL.md`

The Claude Code command is always a one-liner dispatcher:
```
Read and execute the skill defined at:
{{VIBEOS_ROOT}}/2. vibeos-skills/skills/[skill-name]/SKILL.md

$ARGUMENTS
```

No skill content is duplicated into the command file.

## Persona Ownership & Auto-Run Policy

Skills fall into two classes:

- **Domain skills** are owned by a persona and listed in that persona's `PERSONA.md` under
  "Skills in your lane". (Wrappers in `routing/` → `.claude/agents/` stay thin and just load
  `PERSONA.md`, and `.claude/` is regenerated from `routing/` via `scripts/setup_machine.sh` —
  so ownership lives in `PERSONA.md`, never hand-edited into the wrapper.) When the persona is
  active and a request clearly matches, it runs the skill itself:
  - *(auto)* — the persona runs it without being asked and states what it ran. Auto-run is
    limited to skills that **produce a draft or analysis in the current work** with no side
    effects on the shared or global cognitive layer.
  - *(confirm)* — the persona offers first. Used for skills that **write multiple files** or
    are otherwise heavy.
- **Operator rituals** are never auto-run by a persona. They maintain the system and are
  invoked by the human — on cadence (`/vcos-review` and the skills it orchestrates) or at
  session close (`/vcos-session-close`). This preserves the human-in-control principle.

The full ownership map lives in `0. vibeos-global/SKILLS_CHEATSHEET.md`.

## Adding a New Skill — Checklist

- [ ] Create `2. vibeos-skills/skills/[skill-name]/SKILL.md` with frontmatter and required sections
- [ ] Reference standards/source-of-truth by folder or file, not by enumerating volatile lists
- [ ] Create the thin dispatcher at `.claude/commands/[skill-name].md` (and the `routing/commands/` source it is generated from)
- [ ] Add `agents/openai.yaml` (`display_name`, `short_description`, `default_prompt`) so the skill surfaces in Codex/OpenAI tooling
- [ ] Add the skill to the skills table in `OS_INDEX.md` and workspace `CLAUDE.md`
- [ ] If the skill produces or refreshes other artifacts (e.g., index rows, STARTER_PROMPTs), say so explicitly in the Process section
- [ ] Classify it: **domain skill** (assign an owner persona + auto/confirm mode, and wire the owner's `PERSONA.md` + `.claude/agents/` wrapper) or **operator ritual** (cadence-invoked). Record it in `SKILLS_CHEATSHEET.md`

## Current Skills

| Skill | Category |
|-------|----------|
| `vibeos-init` | Setup (first-run wizard) |
| `vibeos-new-persona` | Setup (add a teammate) |
| `vibeos-tutorial` | Setup (guided Day 1) |
| `new-vibeos-project` | Workspace |
| `vcos-spec` | Spec → Build pipeline |
| `vcos-build` | Spec → Build pipeline |
| `vcos-memory` | Memory & quality |
| `vcos-session-close` | Memory & quality |
| `vcos-status` | Analysis |
| `vcos-meeting-context` | Context intake — load a notetaker transcript as framed session context |
| `vcos-retro` | Memory & quality (close-out ritual) |
| `vcos-review` | Compounding (cognitive layer maintenance) — advanced |
| `vcos-calibrate` | Compounding (cognitive layer maintenance) — advanced |
| `vcos-synthesize` | Compounding (cognitive layer maintenance) — advanced |
| `vcos-consolidate` | Compounding (cognitive layer maintenance) — advanced |
| `vcos-simplify-review` | Review (Robin) — advanced |
