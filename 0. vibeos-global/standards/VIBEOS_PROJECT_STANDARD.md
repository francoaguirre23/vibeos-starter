# VibeOS Project Standard

Canonical operating standard for the VibeOS workspace.

This document defines:
- the standard workspace layers
- the canonical project container and project folder structure
- required vs optional project artifacts
- naming conventions
- deprecated patterns that should be cleaned up over time

This is the source of truth for internal VibeOS conformance work.

## Design Goals

- Keep global framework assets separate from project-local state
- Make every project structurally predictable
- Preserve cognitive-layer continuity across projects
- Minimize ambiguity about where instructions, prompts, and outputs belong
- Prefer one canonical path for each concept

## Workspace Layers

The workspace is split into three framework layers, a canonical project
container, and project folders.

### `0. vibeos-global`

Purpose:
- shared framework assets used by all projects
- never copied wholesale into a project

Contains:
- `personas/`
- `global cognitive layer/`
- `scripts/`
- `standards/` — all framework-level standards (project standard, engineering defaults, conformance checklist, hygiene policy, etc.)

Must not contain:
- project-specific specs
- project runtime code
- project output artifacts

Persona note:
- persona folders may include `STARTER_PROMPT.md` as a portable invocation
  layer for tool-agnostic use
- those files complement, but do not replace, `PERSONA.md`, `MINDSET.md`, and
  `SIGNALS.md`

### `1. vibeos-template`

Purpose:
- canonical scaffold used to create new VibeOS projects

Contains:
- empty or starter versions of required project docs
- starter cognitive-layer files
- starter instruction files
- starter prompts

Rule:
- this folder must reflect the current canonical project standard exactly
- any drift here will propagate into future projects

### `2. vibeos-skills`

Purpose:
- canonical skill definitions for all VibeOS workflows
- tool-agnostic — used by Codex natively and dispatched to by Claude Code commands

Contains:
- `skills/vibeos-init/SKILL.md`
- `skills/vcos-spec/SKILL.md`
- `skills/vcos-build/SKILL.md`
- `skills/vcos-memory/SKILL.md`
- `skills/vcos-session-close/SKILL.md`
- additional `vibeos-*` / `vcos-*` skills listed in `OS_INDEX.md` and
  `0. vibeos-global/SKILLS_CHEATSHEET.md`

Rule:
- skill content is canonical — tools dispatch to these files, never copy them
- Claude Code commands in `.claude/commands/` read these files directly
- Codex invokes these files natively
- this is an accelerator layer, not the core project scaffold

### `projects/`

Purpose:
- canonical container for active VibeOS projects
- keeps framework layers separate from active work

Contains:
- one folder per active VibeOS project

Rule:
- new VibeOS projects should be created here by default
- root-level project folders are legacy drift once migration is complete

### Claude Code Integration (`.claude/`)

Purpose:
- thin routing layer connecting Claude Code to the canonical VibeOS framework

Contains:
- `agents/` — one file per persona, pointing to `0. vibeos-global/personas/`
- `commands/` — one file per skill, dispatching to `2. vibeos-skills/skills/`

Rule:
- agent and command files must not duplicate content from persona or skill files
- `.claude/` is a routing layer only; all content stays in canonical locations
- `.claude/` is generated from the path-agnostic `routing/` source by
  `scripts/setup_machine.sh`

### Routing Source (`routing/`)

Purpose:
- path-agnostic source files used to generate `.claude/` for the local machine

Contains:
- `agents/` — one file per persona with `{{VIBEOS_ROOT}}` placeholders
- `commands/` — one file per skill with `{{VIBEOS_ROOT}}` placeholders

Rule:
- update `routing/` first when adding or renaming a persona or skill
- run `scripts/setup_machine.sh` to regenerate `.claude/`
- do not hand-edit `.claude/` as the durable source of truth

### Project Folders

Purpose:
- one folder per project, initiative, tool, or scoped workstream

Rule:
- canonical project folders live under `projects/`
- project folders should conform to the canonical structure below
- project-specific code, docs, prompts, and outputs live here

### Subproject Folders

Purpose:
- self-contained apps, tools, analyses, or workstreams that belong to a parent
  project but have their own setup, runtime, deployment, or operating context

Use a subproject when:
- the work is materially part of a parent project's strategy or operating system
- the artifact has its own files, setup, deployment, cache, runbook, or lifecycle
- creating a separate top-level project would split context without adding
  ownership clarity

Do not use a subproject for:
- one-off docs or outputs that fit naturally under `docs/`
- alternate trackers that would compete with the parent project source of truth
- workstreams that have become strategically independent; promote those to a
  top-level project instead

Rule:
- subprojects live inside the parent project root
- every subproject must include `SUBPROJECT_CONTEXT.md`
- runnable or deployed subprojects should also include `README.md`
- subprojects inherit strategic context from the parent; they do not duplicate
  the full parent VibeOS scaffold unless promoted to a top-level project
- decisions that affect the parent project, user promise, scope, risk, or
  ownership are logged in the parent `project cognitive layer/STANCE.md`

## Canonical Project Structure

Every VibeOS project should use this structure unless there is a strong reason not to.

```text
projects/
  [project-name]/
  START_HERE.md
  README.md                         optional but recommended
  docs/
    project_context.md
    build_packet.md
    security.md
    tdd.md
    stance.md                       legacy/history only when present
    ...                             project-specific docs allowed
  instructions/
    build_packet_instructions.md
    security_instructions.md
    tdd_instructions.md
    stance_instructions.md
    signals_instructions.md
    mindset_instructions.md
  project cognitive layer/
    STANCE.md
    SIGNALS.md
    MINDSET.md
    0. stance_instructions.md
    0. signals_instructions.md
    0. mindset_instructions.md
  prompts/                          optional but recommended
  skills/                           optional, project-local only
  src/                              optional, for implementation projects
  tests/                            optional, required when code exists
  scripts/                          optional
  config/                           optional
  ui/                               optional
  out/                              optional, generated local outputs
  [subproject-name]/                optional, for scoped child apps/tools/workstreams
    SUBPROJECT_CONTEXT.md
    README.md                       required when runnable/deployed
    ...                             subproject-specific code, docs, scripts, outputs
```

## Project Types And Their Canonical Artifact

VibeOS projects are one of two types. The type determines the canonical planning artifact.

- **Decision / process project** (the default — plans, analyses, process changes, strategy, and
  any work where the deliverable is a decision or a document rather than software). Canonical
  artifact: **`docs/operating_brief.md`**. A `build_packet.md` is not required (add one only if a
  build sub-slice appears).
- **Build project** (the deliverable is software). Canonical artifact: **`docs/build_packet.md`**.

A project may start as a decision/process project and spawn a build sub-slice; in that case it
gains a build_packet for that slice without losing its operating_brief.

## Required Project Artifacts

These files or folders are part of the canonical minimum unless the project is intentionally nonstandard.

Required (all projects):
- `START_HERE.md`
- `docs/project_context.md`
- the canonical planning artifact for the project type:
  - Decision / process → `docs/operating_brief.md`
  - Build → `docs/build_packet.md`
- `instructions/`
- `project cognitive layer/`

Required within `instructions/`:
- `build_packet_instructions.md`
- `security_instructions.md`
- `tdd_instructions.md`
- `stance_instructions.md`
- `signals_instructions.md`
- `mindset_instructions.md`

Required within `project cognitive layer/`:
- `STANCE.md`
- `SIGNALS.md`
- `MINDSET.md`
- `0. stance_instructions.md`
- `0. signals_instructions.md`
- `0. mindset_instructions.md`

## Recommended Project Artifacts

Recommended:
- `README.md` for setup, run, and artifact orientation
- `prompts/` when the project uses repeatable operator prompts
- `skills/` when the project includes reusable project-local operating routines
- `src/` and `tests/` for implementation-heavy projects
- `config/` when governance or runtime rules should be externalized
- `SUBPROJECT_CONTEXT.md` inside any subproject folder

## Subproject Context Standard

`SUBPROJECT_CONTEXT.md` is the required orientation file for a subproject. It is
small by design. It should answer only what a future session needs in order to
work on the subproject without losing the parent project's context.

Required coverage (not necessarily literal headings):
- Parent project and links to parent `docs/project_context.md` and STANCE
- Purpose, audience, owner, and current status
- In scope / out of scope
- Source systems, data stores, deployments, and required secrets/configuration
- Setup / run / deploy path, or link to the README section that covers it
- Open decisions, known risks, and promotion criteria

Subproject context rules:
- read the parent project context first, then the subproject context
- keep parent strategy in the parent context; keep app/tool mechanics in the
  subproject context
- do not create a nested `project cognitive layer/` by default
- if a subproject needs its own recurring cadence, independent roadmap, or
  standalone cognitive layer, promote it to a top-level VibeOS project

## Canonical Naming Rules

### Folder Names

Canonical:
- `instructions`
- `project cognitive layer`
- `docs`
- `prompts`
- `skills`
- `src`
- `tests`
- `scripts`
- `config`
- `out`

Do not introduce alternate names for the same concept.

### Project Names

Preferred:
- human-readable names are allowed
- spaces are allowed
- use one stable project folder name only

Avoid:
- duplicate encoded variants such as `%20`
- parallel folders that differ only by punctuation, spacing, or casing
- temporary suffixes unless they reflect intentional versioning such as `v2`

### File Names

Canonical cognitive-layer files:
- `STANCE.md`
- `SIGNALS.md`
- `MINDSET.md`

Canonical instruction files:
- `[topic]_instructions.md`

Canonical top-level entrypoint:
- `START_HERE.md`

## Source-of-Truth Rules

### Project State

Primary source of truth:
- `docs/project_context.md`
- `docs/build_packet.md`
- `project cognitive layer/STANCE.md`
- `project cognitive layer/SIGNALS.md`
- `project cognitive layer/MINDSET.md`

Legacy:
- `docs/stance.md` may be preserved for historical continuity, but it is not the working source of truth once `project cognitive layer/STANCE.md` exists

Subprojects:
- parent project context remains the strategic source of truth
- `SUBPROJECT_CONTEXT.md` is the local operating source of truth for a
  subproject's setup, deployment, cache, and runtime mechanics
- parent STANCE remains the decision log for cross-cutting decisions

### Global State

Primary source of truth:
- `0. vibeos-global/global cognitive layer/GLOBAL_SIGNALS.md`
- `0. vibeos-global/global cognitive layer/GLOBAL_MINDSET.md`
- `0. vibeos-global/personas/`

### Prompts

Rule:
- prompts should point only to canonical instruction paths
- prompts must not reference folders that do not exist in the canonical scaffold

## Standard Division Of Responsibility

### Global Layer

Owns:
- persona definitions
- global mindset and signals
- bootstrap scripts
- framework standards

### Template Layer

Owns:
- the default shape of a new project
- starter project docs and instructions
- canonical relative links for generated projects

### Project Layer

Owns:
- project-specific context
- project-specific design and security decisions
- project-local outputs, code, prompts, and scripts
- subproject folders and their `SUBPROJECT_CONTEXT.md` files

### Subproject Layer

Owns:
- local implementation mechanics for a scoped child app/tool/workstream
- setup, deployment, cache, and operational runbook details
- subproject-specific code, scripts, and generated outputs

Does not own:
- parent strategic context
- global standards or persona definitions
- a separate cognitive layer unless promoted to top-level project

## Deprecated Patterns

These patterns are now considered drift and should be remediated over time.

Deprecated:
- `project instructions/` as the canonical folder name
- prompts that reference `../instructions/...` when the template uses a different folder name
- duplicate URL-encoded project folders such as `%20` variants
- stray virtualenv or cache directories committed or preserved as structural folders
- multiple sibling folders created accidentally from broken shell quoting or malformed commands

Examples of cleanup candidates:
- duplicate encoded folder variants
- stray `.venv`, `node_modules`, `.pytest_cache`, and `__pycache__` directories outside expected local-project use
- malformed folders like isolated words or symbols created by accidental command parsing

## Conformance Levels

### Level 1: Canonical

The project:
- uses the standard folder names
- includes all required artifacts
- keeps links aligned with canonical paths
- cleanly separates project state from global state

### Level 2: Acceptable With Drift

The project:
- is structurally recognizable
- remains usable
- has minor naming or linking inconsistencies
- does not yet create operational risk

### Level 3: Needs Remediation

The project:
- has broken references
- contains duplicate or ambiguous structure
- mixes global and local concepts
- includes obvious residue that obscures the real project state

## Immediate Framework Decisions

These decisions are now recommended as framework defaults:

1. `instructions/` is the canonical project instruction folder name.
2. `project instructions/` should be treated as deprecated and migrated.
3. `project cognitive layer/STANCE.md` is the live project decision log.
4. `docs/stance.md` is legacy-only when retained.
5. Each project should have exactly one stable root folder.
6. Generated or derived project artifacts should stay inside the project folder, typically under `out/` when appropriate.
7. Subprojects are allowed inside a parent project when they have their own
   operating mechanics, but they must have `SUBPROJECT_CONTEXT.md` and inherit
   strategic context from the parent.

## Next Remediation Targets

After adopting this standard, the next internal ops steps should be:

1. Align `1. vibeos-template` with this structure.
2. Update bootstrap generation so new projects are canonical on creation.
3. Add a conformance checklist or validator script.
4. Clean up existing workspace drift project by project.
