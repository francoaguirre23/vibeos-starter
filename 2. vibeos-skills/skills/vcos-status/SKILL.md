---
name: vcos-status
description: Produce a compact current-status overview of a project — what it is, what exists, what changed, open tensions, and the recommended next slice.
---

# VCOS Status

> **Ownership:** @ada · **Mode:** auto-run (domain skill). See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill to generate a fast, operational snapshot of where a project stands right now. It answers "what is the state of this project?" and sets up a clean handoff to @sam (or run `/vcos-spec`) for the next slice when one is warranted.

This is not a new build packet — it is a handoff summary for planning the next one well.

## When to use

- You want a quick read on where a project is
- The project has grown complex and you are considering a `v2+` or major-feature PRD
- You want to preserve the original build packet and create a new one
- Before handing the project to @sam or another persona who needs current state

## Context Requirement

Follow the project's own instruction file, which is the source of truth for format:
- `instructions/current_status_overview_instructions.md` (project-local)

Read these inputs:
- `docs/project_context.md`
- the canonical planning artifact: `docs/operating_brief.md` (Eng Ops) or `docs/build_packet.md` (Build)
- for Build projects, any files in `docs/build_packets/` and `docs/build_packet_index.md` if they exist
- `project cognitive layer/STANCE.md`, `SIGNALS.md`, `MINDSET.md`
- relevant TDD / security docs if they materially affect the next slice

## Process

1. Read the inputs above and the project's `current_status_overview_instructions.md`.
2. Produce the Current Status Overview in the format that instruction file defines:
   - Project Identity
   - Current Active Slice
   - What Already Exists
   - What Has Changed Since The Original PRD
   - Open Tensions
   - Recommended Next PRD Slice
   - Inputs The PRD GPT Should Treat As Source Of Truth
   - Preservation Rules
3. If a new build packet is not actually warranted, say so clearly.

## Required output

A concise Current Status Overview following the project's instruction format, optimized for handoff clarity over completeness.

## Checks before finalizing

- [ ] Distinguishes stable context from proposed next-slice changes
- [ ] Does not rewrite history to make the project look cleaner than it was
- [ ] Calls out ambiguity explicitly
- [ ] Names the exact source-of-truth files for the next PRD
- [ ] States clearly if no new build packet is warranted

## Recommended handoff

After creating the overview, hand it to @sam (or run `/vcos-spec`) to either run a short PRD-prep interview (if the next slice is still fuzzy) or draft the next build packet directly (if the slice is clear).
