---
name: vcos-synthesize
description: Cross-project and cross-persona synthesis — find patterns that recur across MINDSETs and propose them up to the global cognitive layer.
---

# VCOS Synthesize

> **Ownership:** Operator ritual — human-invoked, runs inside `/vcos-review`. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill to make the cognitive layer compound. It reads across all project and persona MINDSETs, finds patterns that recur in two or more places, and proposes them to the global layer. This is the mechanism that turns separate project brains into a single accumulating intelligence.

Without this, lessons stay siloed in the project or persona where they were learned. With it, a pattern that proves true across the portfolio becomes part of the organization's durable identity.

## When to use

- Inside the biweekly `/vcos-review` (see `MAINTENANCE_CADENCE.md`)
- After 2+ projects reach a milestone or close
- When `/vcos-session-close` reports synthesis is due
- Any time you suspect a lesson is no longer project-specific

## Context Requirement

**Confidentiality gate (read first):** read the classification registry in `projects/INDEX.md` and `standards/CONFIDENTIALITY.md`. **Exclude from the synthesis corpus any project classified Confidential, NDA, or unclassified** (fail-closed). Never name an NDA project in GLOBAL_SIGNALS, GLOBAL_MINDSET, or the ledger — use a neutral handle. Only Internal and Public projects feed synthesis.

Read the synthesis source set (Internal/Public projects only):
- `projects/*/project cognitive layer/MINDSET.md` for projects classified Internal or Public
- Every `0. vibeos-global/personas/*/MINDSET.md`
- Current `0. vibeos-global/global cognitive layer/GLOBAL_SIGNALS.md` and `GLOBAL_MINDSET.md`
- `0. vibeos-global/global cognitive layer/global_signals_instructions.md` and `global_mindset_instructions.md` for promotion rules

## Inputs

- The full set of project + persona MINDSETs (the synthesis corpus)
- The current global layer (to avoid re-proposing what already exists)

## Process

1. **Build the corpus.** Collect every principle from every project MINDSET and persona MINDSET. Note where each came from (which project, which persona).

2. **Cluster by meaning, not wording.** Group principles that express the same underlying truth even if phrased differently. Example: "ship the smallest useful version first" and "cut scope before quality when time is tight" are the same cluster.

3. **Score each cluster:**
   - **Reach** — how many distinct projects AND personas it appears in
   - **Generality** — Project-specific / Likely general / Clearly general
   - **Consistency** — does it hold across different project types, or only one kind of work?

4. **Apply the promotion bar.** A cluster is eligible for GLOBAL when it appears in ≥2 distinct projects (project track) OR ≥2 distinct personas (specialist track), is Clearly general, and is consistent across contexts.

5. **Stage, then propose:**
   - Add eligible clusters to `GLOBAL_SIGNALS.md` with full evidence (every source listed).
   - For clusters already staged in GLOBAL_SIGNALS that now have ≥2 project MINDSETs behind them, write a **proposal** to add them to `GLOBAL_MINDSET.md` — never edit GLOBAL_MINDSET directly. Follow `global_mindset_instructions.md`.

6. **Report the synthesis** — what was found, what was staged, what is proposed for GLOBAL_MINDSET, and what clusters are close but not yet over the bar (so the next run knows what to watch).

## Required output

- New/updated entries in `GLOBAL_SIGNALS.md` (staging) with complete cross-source evidence — applied directly
- **Append each GLOBAL_MINDSET proposal as a Pending item in `global cognitive layer/review_queue.md`** (do not edit GLOBAL_MINDSET directly) — with what/why/decision-needed/recommendation/source
- A synthesis report: promoted, staged, watching
- Updated `last synthesized` date in the maintenance ledger

## Checks before finalizing

- [ ] Clusters are grouped by meaning, not surface wording
- [ ] Every staged signal lists all its sources (projects + personas)
- [ ] GLOBAL_MINDSET was proposed to, never directly edited
- [ ] Patterns below the bar are recorded as "watching," not dropped
- [ ] Maintenance ledger updated with run date
