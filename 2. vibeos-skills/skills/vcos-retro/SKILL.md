---
name: vcos-retro
description: Close-out ritual — run a short structured retro at a project close or milestone (intended vs actual, surprises, what we'd do differently, grounded in STANCE), then distill the project's SIGNALS into a real MINDSET with a simple calibration table.
---

# VCOS Retro

> **Ownership:** Operator ritual — you invoke it at a project close or a major milestone. It is not auto-run by a teammate; it maintains the memory, so it stays in your hands. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Projects that close without a retro leave their lessons stranded in STANCE entries nobody rereads. This ritual does two things in one pass: it runs a short, structured retro at the moment of close, and it turns the project's recurring SIGNALS into a real MINDSET — the durable principles layer the starter otherwise never fills in. It is self-contained: the retro and the distillation happen here, in one skill.

## When to use

- A project is wrapping up ("we're calling this done", "this is shipped").
- A project passes a major milestone and you want to capture what it taught you.
- The project's SIGNALS have piled up but its MINDSET is still empty or a stub.

This ritual is non-blocking. If you would rather not do the full pass now, capture a one-line "retro pending" note and move on — nothing here should hold up the close itself.

## Context Requirement

Before starting, read:
- The project's context and brief (`docs/project_context.md` or `PROJECT_CONTEXT.md`) — the original goal, phase, and constraints.
- The project's `STANCE.md` and `SIGNALS.md` — the evidence of what actually happened. These are read-only inputs; do not rewrite them.
- The project's current `MINDSET.md` — what, if anything, is already distilled.
- The MINDSET format in `1. vibeos-template/project cognitive layer/0. mindset_instructions.md`, so the distilled output matches the standard shape.

## Process

1. **Reconstruct intent.** From the project context and brief: what was this meant to do, for whom, by when, at what scope?
2. **Reconstruct reality.** From STANCE, SIGNALS, and what actually shipped: what happened, what shipped, what got cut, what took longer than expected.
3. **Run the four retro questions**, grounding each answer in STANCE evidence rather than memory (cite the entries):
   - What was intended vs what happened?
   - What surprised us?
   - What would we do differently next time?
   - What does the evidence in STANCE actually support? (separate a felt lesson from an evidenced one.)
4. **Write the retro.** Keep it short (≤40 lines) as `docs/retro.md`, or a `## Retro` section in the project context for a small project. Note the close date and the final phase.
5. **Distill SIGNALS into MINDSET.** In the same pass, turn the recurring patterns into durable principles:
   - **Cluster** STANCE entries and SIGNALS by meaning, not wording. Ignore one-offs unless they are clearly high-confidence.
   - **Distill** each cluster with ≥2 occurrences (or one high-confidence pattern) into one short, general, evidence-backed principle. Sort into the standard sections: Decision Heuristics, Build Preferences, Risk Profile, Anti-Patterns.
   - **Build a simple calibration table** — one row per principle: Principle · Confidence (Provisional / Established / Core) · Times applied · Times reversed · Source. New principles start Provisional.
   - **Flag global candidates.** If a principle looks general beyond this project, mark it under `## Open Promotions → Global MINDSET`. Do not write to the global layer here — `/vcos-synthesize` picks these up later.
6. **Propose, then apply.** Show the drafted retro and MINDSET, then write them on confirmation. STANCE and SIGNALS are never rewritten.

## Required output

- `docs/retro.md` (or a `## Retro` section): intended vs actual, surprises, a do-differently list, and the STANCE evidence each point rests on.
- An updated project `MINDSET.md`: distilled principles in the standard sections, plus the simple calibration table.
- Any principle general enough for the global layer flagged under `## Open Promotions → Global MINDSET`.
- A one-paragraph summary: how many principles were distilled, from how much evidence, and what was flagged for promotion.

## Checks before finalizing

- [ ] Every do-differently point and every principle traces to STANCE/SIGNALS evidence, or is marked as unevidenced opinion.
- [ ] The retro stays ≤40 lines and the MINDSET stays ≤100 lines — condense wording, not evidence.
- [ ] The calibration table is present and all new principles start Provisional.
- [ ] Nothing was written to STANCE, SIGNALS, or the global layer directly (retro and MINDSET are propose-then-apply; STANCE and SIGNALS stay read-only).
- [ ] The close was not blocked — "retro pending" is a valid outcome if you chose to defer.
