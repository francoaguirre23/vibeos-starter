---
name: vcos-session-start
description: Pick up an EXISTING project in a fresh thread — rehydrate its durable state (project_context + cognitive layer + open loops) into a compact orientation, so a new thread starts sharp instead of inheriting a long, compacted one. The open-of-session counterpart to /vcos-session-close. NOT for creating a new project (use /new-vibeos-project for that).
---

# VCOS Session Start

> **Ownership:** Your ritual — run it at the top of a fresh thread on an existing project. Pairs with `/vcos-session-close` (the end-of-session capture). See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this to resume a project in a **new** thread. The point is thread hygiene: instead of keeping one thread running for a project's whole life (which auto-compacts repeatedly and loses fidelity), you close the old thread and open a fresh one that rehydrates the project's durable state from files. The cognitive layer, not the old conversation, is the source of truth.

This is **not** `/new-vibeos-project`. It assumes the project already exists on disk. If the project has no folder yet, stop and point the user to `/new-vibeos-project`.

## When to use

- Opening a fresh thread on a project you've worked before (the standard move after closing a long thread).
- Returning to a project after time away and needing to reload where it stands.
- Any time the current thread has already auto-compacted once — close it, then run this in a new thread.

## Context Requirement

Before orienting, read (only for the target project — do not sweep the whole workspace):
- `projects/<project>/docs/project_context.md` (or `PROJECT_CONTEXT.md`) — what this project is, its phase, constraints.
- `projects/<project>/project cognitive layer/STANCE.md` — the recent decision log (the last ~20–30 entries are usually enough; note the latest dated entry).
- `projects/<project>/project cognitive layer/SIGNALS.md` and `MINDSET.md` — the patterns and distilled principles that should shape the work.
- Resolve the target from the argument, else the cwd, else ask which project.

## Process

1. **Identify the project** and confirm its folder exists. If it does not, stop and route to `/new-vibeos-project`.
2. **Rehydrate** the files above. Prefer the durable files over any stale thread history.
3. **Produce a compact orientation** (see Required output). Keep it short — this is a launch pad, not a report.
4. **Name the next slice** — hand off to `/vcos-status` if the user wants the fuller snapshot. Do not start doing the work until the user picks the slice.
5. **Do not modify** the cognitive layer here. Capture is `/vcos-session-close`'s job at the other end.

## Required output

A short orientation block:
- **Project + phase** — one line.
- **Where it stands** — 3–5 bullets from the latest STANCE entries and project_context (most recent decisions, what exists, what changed).
- **Open loops / tensions** — anything unresolved the last thread left hanging.
- **Governing principles** — 1–3 relevant MINDSET/SIGNALS items to keep in view.
- **Recommended next slice** — one move, routed to a teammate.

Total: well under a screen. If it's growing long, you're re-deriving instead of rehydrating.

## Checks before finalizing

- [ ] The project already exists; this was a resume, not a new-project scaffold.
- [ ] Only the target project's files were read, not the whole workspace.
- [ ] The orientation is compact (project + phase, ≤5 status bullets, open loops, ≤3 principles, one next slice).
- [ ] No cognitive-layer files were edited (capture belongs to `/vcos-session-close`).
- [ ] Durable files were treated as source of truth over any stale thread history.
