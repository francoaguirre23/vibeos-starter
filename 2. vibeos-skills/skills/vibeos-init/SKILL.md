---
name: vibeos-init
description: Turnkey first-run setup wizard — interview the user, write their identity card, generate starter personas, and scaffold their first project.
---

# VibeOS Init

> **Ownership:** Operator ritual (human-invoked, first run) · **Mode:** confirm. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

This is the warm welcome. Run it once, right after someone clones the starter. By the end they have an identity card, a small team of personas tailored to them, and their first project scaffolded and ready. Keep the tone friendly and unhurried — this is a setup wizard, not a form.

## When to use

- The very first time someone opens a fresh VibeOS workspace.
- `0. vibeos-global/USER.md` does not exist yet, or only has placeholder content.
- Someone wants to re-onboard or reset their setup from scratch.

## Context Requirement

Before starting, skim so the welcome lands in the right voice and shape:
- `0. vibeos-global/SOUL.md` — the operating principles and voice to echo.
- `0. vibeos-global/USER.template.md` — the shape of the identity card you will write. If it does not exist, treat the section list in Step 2 as the shape.
- The shipped example personas under `0. vibeos-global/personas/` — Ada (Chief of Staff), Sam (Tech Lead), Robin (Reviewer) — as archetypes to adapt.

## Inputs

- The user's answers to a short interview (gathered in Step 1).
- The shipped persona archetypes.
- The `vibeos-new-persona` flow (followed in Step 3).
- The bootstrap script.

## Process

### Step 1 — Interview (a few friendly questions)

Ask these in plain language, one or two at a time so it feels like a conversation, not a survey:

1. What do you do? (role, the kind of work you spend your days on)
2. Are you working solo, or with a team?
3. What do you want help building or deciding right now? (the thing on your mind)
4. Which tool are you using to run this? (Claude Code, Codex, Cursor, something else)

Reflect their answers back in a sentence so they know you heard them. If an answer is thin, ask one gentle follow-up — don't interrogate.

### Step 2 — Write their identity card

Write the answers into `0. vibeos-global/USER.md`, following the shape of `USER.template.md`. If the template is missing, use these sections:
- **Who you are** — role and the work you do
- **Solo or team** — and if a team, who/what it is
- **What you're focused on** — the current goal or decision
- **Tool** — what they're running VibeOS in
- **Working style** — anything they mentioned about how they like to work (optional)

Keep it short and human. Show them the draft and let them adjust before saving.

### Step 3 — Generate 1–3 starter personas

Tailor a small team to their answers by following the `vibeos-new-persona` flow for each one (or by adapting the three shipped archetypes — Ada the orchestrator, Sam the maker, Robin the critic):
- Solo builders usually want a maker and a critic, plus an orchestrator if work is fuzzy.
- People doing planning or decision work usually want an orchestrator and a critic first.
- Pick names and roles that fit their world. Confirm each one with them before creating files.

For each persona, produce the full file set and the routing wrapper exactly as `vibeos-new-persona` describes.

### Step 4 — Scaffold their first project

Turn the thing from question 3 into a real project. Pick the type:
- **engops** — the deliverable is a decision, doc, process, or analysis.
- **build** — the deliverable is software.

Then run the bootstrap:
```sh
bash "0. vibeos-global/scripts/bootstrap_vibeos_project.sh" "<project name>" engops|build
```

Tell them what got created and where, and suggest the natural next move (talk to their orchestrator persona, or try `/vibeos-tutorial` for a guided first lap).

## Required output

- `0. vibeos-global/USER.md` written from the interview.
- 1–3 tailored personas, each with a complete file set and routing wrapper.
- One scaffolded project under `projects/`.
- A short, friendly wrap-up: what exists now, and the single best next step.

## Checks before finalizing

- USER.md reads like a real person, not a placeholder.
- Every generated persona has PERSONA.md, MINDSET.md, SIGNALS.md, STARTER_PROMPT.md, and a routing wrapper.
- The first project scaffolded without errors.
- Nothing was created the user didn't confirm.
- The wrap-up names exactly one clear next step.
