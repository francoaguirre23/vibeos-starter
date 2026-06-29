---
name: vibeos-new-persona
description: Interview the user, then create a new standard-conformant persona with a full file set and routing wrapper.
---

# VibeOS New Persona

> **Ownership:** Operator ritual (human-invoked) · **Mode:** confirm. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this to add a new specialist to the team — a named lens you can hand work to. The skill interviews the user, then writes a persona that follows the persona standard and is wired in so it can be invoked.

## When to use

- The user wants a new persona (a maker, a critic, an orchestrator, a domain specialist).
- A recurring kind of work keeps coming up and deserves its own dedicated lens.
- During first-run setup (`vibeos-init`) when generating the starter team.

## Context Requirement

Before starting, read:
- `0. vibeos-global/standards/PERSONA_STANDARD.md` — the folder naming, required files, and required sections. This is the source of truth for the shape of a persona.
- The shipped example personas under `0. vibeos-global/personas/` — Ada (Chief of Staff), Sam (Tech Lead), Robin (Reviewer) — for tone and structure to match.

## Inputs

- The user's answers to a short interview (gathered in Step 1).
- The existing personas folder (to pick the next folder number and avoid lane overlap).

## Process

### Step 1 — Interview

Ask, in plain language:
1. **Role** — who is this persona and what do they own?
2. **Lens** — what questions does this persona ask when they look at a problem?
3. **When to invoke** — what kind of request should reach for them?
4. **Boundaries** — what does this persona never do, and where do they hand off to others?

Confirm a name and a short handle (lowercase, e.g. `robin`) before writing anything.

### Step 2 — Create the persona folder

Pick the next available folder number (do not renumber existing personas). Create:
`0. vibeos-global/personas/<N. Name (Role)>/`

with these four files, following PERSONA_STANDARD:
- **PERSONA.md** — all required sections: Role, Lens, When to invoke, What you produce, Handoffs, MECE Boundary, What you never do, Output style, Context to read.
- **MINDSET.md** — blank to start. Header plus a "Fresh instance — no principles yet." line and an empty Calibration table.
- **SIGNALS.md** — blank to start. Header plus a "Fresh instance — no signals staged yet." line and the source-tag note.
- **STARTER_PROMPT.md** — a self-contained portable prompt embedding the role, lens, what-you-produce, what-you-never-do, and output style.

### Step 3 — Wire the routing wrapper

Create `routing/agents/<handle>.md` using the `{{VIBEOS_ROOT}}` placeholder pattern so the workspace stays portable:
```
---
name: <handle>
description: <one sentence — role and when to invoke>
---

You are <Name>, the <Role> operating within the VibeOS framework.

Before responding, read your persona files:
- {{VIBEOS_ROOT}}/0. vibeos-global/personas/<N. Name (Role)>/PERSONA.md
- {{VIBEOS_ROOT}}/0. vibeos-global/personas/<N. Name (Role)>/MINDSET.md
- {{VIBEOS_ROOT}}/0. vibeos-global/personas/<N. Name (Role)>/SIGNALS.md

If working within a project, also read:
- docs/project_context.md
- project cognitive layer/STANCE.md
- project cognitive layer/SIGNALS.md
- project cognitive layer/MINDSET.md

Follow the role, lens, operating principles, and output format defined in PERSONA.md.
```

The wrapper holds no persona content — it only points at the canonical files.

### Step 4 — Confirm and orient

Tell the user: the persona name and handle, where the folder lives, and how to invoke it (`@<handle>` in tools that support it). Note that if their tool generates a local routing layer from `routing/`, they may need to regenerate it for the new handle to appear.

## Required output

- A persona folder with PERSONA.md, MINDSET.md, SIGNALS.md, STARTER_PROMPT.md.
- A `routing/agents/<handle>.md` wrapper using `{{VIBEOS_ROOT}}`.
- A short orientation: name, handle, location, how to invoke.

## Checks before finalizing

- The folder is named `<N. Name (Role)>` with the next free number.
- PERSONA.md has every required section, including a clear MECE Boundary against the closest existing personas.
- MINDSET.md and SIGNALS.md start blank with the standard headers.
- STARTER_PROMPT.md is fully self-contained (no file references).
- The routing wrapper uses `{{VIBEOS_ROOT}}` and contains routing only, no persona content.
