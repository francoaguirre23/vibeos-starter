---
name: new-vibeos-project
description: Create a new VibeOS project with full scaffold, index registration, and orientation files.
---

# New VibeOS Project

> **Ownership:** Operator ritual (human-invoked when starting a new project) · **Mode:** confirm. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill to create a new project inside the VibeOS workspace.

## Context Requirement

Before performing this workflow, read all files in the global standards folder:
`0. vibeos-global/standards/`

These standards govern how new projects should be structured, what defaults apply, and how workspace hygiene is maintained. Read them — they are the source of truth for the decisions in this skill.

## Inputs

- **Project folder name** — the name of the folder under `projects/` (e.g., `my new project`)
- **Brief description** (optional) — one-line description of what the project is. If not provided, ask before proceeding.
- **Domain** (optional) — `engops` or `build`. If not provided, infer from context or ask.

## Process

### Step 1 — Run the bootstrap script

First decide the project TYPE:
- **engops** (decisions, docs, process redesigns, analyses, strategic work) → canonical artifact: `docs/operating_brief.md`. This is the default.
- **build** (the deliverable is software) → canonical artifact: `docs/build_packet.md`.

Then run the bootstrap with the type:
```sh
bash "0. vibeos-global/scripts/bootstrap_vibeos_project.sh" "<Project Folder Name>" <engops|build>
```

This will:
1. Create the project folder under `projects/`
2. Copy the template scaffold and keep the canonical artifact for the type, pruning the other
3. Replace `[Project Name]` placeholders in all copied markdown files
4. Write `START_HERE.md` and `CLAUDE.md` pointing at the canonical artifact
5. Verify global resources and the project cognitive layer
6. Remove stray system files

### Step 2 — Add to projects/INDEX.md

Append a new row to the Active Projects table in `projects/INDEX.md`:
```
| <folder name> | <brief description> | <domain> | <type> | <primary personas> | SPEC | New — scaffold created |
```

- **Type**: infer from domain (Script, CLI tool, Internal tool, Process redesign, Strategic initiative, Analysis, etc.)
- **Primary Personas**: suggest based on domain and type, but confirm with the user — your personas (e.g., Ada, Sam, Robin) or whichever ones fit.
- **Phase**: always starts at `SPEC`
- **Status**: always starts as `New — scaffold created`

### Step 3 — Add to OS_INDEX.md

Append a new row to the Active Projects summary table in `OS_INDEX.md`:
```
| <folder name> | <brief description> | <domain> | SPEC |
```

### Step 4 — Apply defaults guidance

Based on the domain and what the user described, give a little initial guidance from `ENGINEERING_DEFAULTS.md`:

**For build projects:**
- Recommend the default build shape (script → CLI → lightweight web app → service)
- Note the default language and tooling
- Note the frontend stance (no frontend unless genuinely needed)
- Note data/storage defaults (no persistence → local files → small database)
- Note the simple default: least privilege, read-only first, keep sensitive data in mind early

**For engops projects:**
- Note that the primary output is usually a document, process, or analysis — not software
- Recommend starting with `/vcos-spec` or talking to your orchestrator persona (e.g., Ada) to frame the problem
- Note that defaults still apply if any tooling is built as part of the project

### Step 5 — Fill project_context.md

Open `docs/project_context.md` in the new project and prompt the user to fill in at minimum:
- Vision (1–3 sentences)
- Current Goal
- Current Phase (should be SPEC)

If the user gave enough context in their request, draft these for their review.

### Step 6 — Confirm and orient

Report back:
- Project folder created under `projects/`
- Domain and type
- INDEX.md updated: yes
- OS_INDEX.md updated: yes
- Defaults applied: `<summary of key defaults for this project type>`
- Next steps:
  - Fill `docs/project_context.md` and the canonical planning artifact (`docs/operating_brief.md` for engops, `docs/build_packet.md` for build)
  - Talk to your orchestrator persona (e.g., Ada) or run `/vcos-spec` to start framing
  - For build projects: bring in your maker persona (e.g., Sam) for the implementation plan, and your critic (e.g., Robin) for a review pass

## Required output

- A scaffolded project under `projects/` with the canonical artifact, cognitive layer, instructions, `START_HERE.md`, and `CLAUDE.md`
- A new row in `projects/INDEX.md` and a summary row in `OS_INDEX.md`
- A short orientation report: folder, domain, applied defaults, next steps

## Checks before finalizing

- [ ] Bootstrap script completed without errors
- [ ] The project's `CLAUDE.md` exists
- [ ] The project's `START_HERE.md` exists
- [ ] `docs/project_context.md` exists
- [ ] Canonical planning artifact exists: `docs/operating_brief.md` (engops) **or** `docs/build_packet.md` (build)
- [ ] The project cognitive layer exists (STANCE.md, SIGNALS.md, MINDSET.md)
- [ ] The `instructions/` folder exists with its instruction files
- [ ] New row added to `projects/INDEX.md`
- [ ] New row added to `OS_INDEX.md`
