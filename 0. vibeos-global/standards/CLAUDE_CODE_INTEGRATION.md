# Claude Code Integration Standard

How VibeOS is wired into Claude Code. Defines the `.claude/` routing layer, the agent and command patterns, and how to add new ones.

Complements:
- `PERSONA_STANDARD.md` — persona file structure
- `SKILL_STANDARD.md` — skill file structure

## Core Principle: Routing Layer Only

`.claude/` is a **thin routing layer with no content of its own**. Every file in it points to a canonical source elsewhere in the workspace. This guarantees one source of truth per concept, so updates made in Codex are seen by Claude Code and vice versa — there is no "Claude version" and "Codex version" of any persona or skill that can drift.

`routing/` is the path-agnostic source for `.claude/`. It uses `{{VIBEOS_ROOT}}`
placeholders so the workspace can be cloned or moved. Run `scripts/setup_machine.sh`
to stamp the local absolute path into `.claude/`.

```
Routing source:
routing/
  agents/        ← path-agnostic persona routers with {{VIBEOS_ROOT}}
  commands/      ← path-agnostic skill routers with {{VIBEOS_ROOT}}

.claude/
  agents/        ← generated local persona routers
  commands/      ← generated local skill routers
```

Rule: if content lives in `routing/` or `.claude/`, it is a bug. Content lives in personas, skills, and standards. `routing/` and `.claude/` only route.

## Agents (Personas)

Each persona has a thin agent source file at `routing/agents/[name].md`, which
generates `.claude/agents/[name].md`:

```
---
name: [name]
description: [one sentence — role and when to invoke]
---

You are [Name], the [Role] operating within the VibeOS framework.

Before responding, read your persona files:
- /absolute/path/to/0. vibeos-global/personas/[N. Name (Role)]/PERSONA.md
- /absolute/path/to/.../MINDSET.md
- /absolute/path/to/.../SIGNALS.md

If working within a project, also read:
- docs/project_context.md
- docs/build_packet.md
- project cognitive layer/STANCE.md
- project cognitive layer/SIGNALS.md
- project cognitive layer/MINDSET.md

Follow the role, lens, operating principles, and output format defined in PERSONA.md.
```

The agent file holds no persona content — it instructs Claude to read the canonical files. Invoked as `@name`.

## Commands (Skills)

Each skill has a thin command source file at `routing/commands/[skill-name].md`,
which generates `.claude/commands/[skill-name].md`:

```
Read and execute the skill defined at:
/absolute/path/to/2. vibeos-skills/skills/[skill-name]/SKILL.md

$ARGUMENTS
```

The command file holds no skill content — it dispatches to the canonical `SKILL.md`. Invoked as `/skill-name`.

## Workspace CLAUDE.md

The workspace root `CLAUDE.md` is auto-loaded by Claude Code on every session. It carries:
- Workspace structure
- The commands table (mirrors `OS_INDEX.md` skills)
- The personas/agents table (mirrors `OS_INDEX.md` personas)
- Cognitive layer summary
- Portable persona prompt guidance
- How to create a new project

It is an orientation surface, not a content store — the detailed definitions live in personas, skills, and standards.

## Project-Level CLAUDE.md

The bootstrap script writes a `CLAUDE.md` into each new project with resolved absolute paths to the project's context files, global resources, available commands, and personas. This is auto-loaded when Claude Code opens inside that project folder.

## Naming Consistency Across Tools

The same name is used everywhere:
- Persona: folder `0. Ada (Chief of Staff)`, agent `@ada`, starter prompt `Ada`
- Skill: folder `vcos-spec`, command `/vcos-spec`, Codex skill `vcos-spec`

No tool-specific name variants.

## Adding to the Integration Layer

When a persona is added (see `PERSONA_STANDARD.md`):
- [ ] Add `routing/agents/[name].md` thin wrapper
- [ ] Run `scripts/setup_machine.sh` to regenerate `.claude/agents/[name].md`

When a skill is added (see `SKILL_STANDARD.md`):
- [ ] Add `routing/commands/[skill-name].md` thin dispatcher
- [ ] Run `scripts/setup_machine.sh` to regenerate `.claude/commands/[skill-name].md`

In both cases:
- [ ] Update the relevant table in `OS_INDEX.md` and workspace `CLAUDE.md`
- [ ] Confirm the file contains only routing, no content

## Maintenance Trigger

Whenever a persona or skill is added, renamed, or retired, update:
1. The `routing/` source file (agent or command), then regenerate `.claude/`
2. `OS_INDEX.md` (personas or skills table)
3. Workspace `CLAUDE.md` (personas or commands table)

The `/vcos-memory` and `/vcos-session-close` skills prompt this check at end-of-session.
