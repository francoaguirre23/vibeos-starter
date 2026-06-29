---
name: vcos-calibrate
description: Update the confidence tier of MINDSET principles based on evidence that they were applied and held (or were reversed) in real work.
---

# VCOS Calibrate

> **Ownership:** Operator ritual — human-invoked, runs inside `/vcos-review`. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill to make principles self-correcting. Today every MINDSET line is a flat assertion with equal weight. Calibration adds a confidence tier to each principle based on how often it was applied and whether it held — so battle-tested principles outrank speculative ones, and principles that keep getting violated get flagged as possibly wrong.

This is the difference between a MINDSET that only grows and one that knows which of its own beliefs are load-bearing.

## Confidence Tiers

| Tier | Meaning | Entry condition |
|------|---------|-----------------|
| **Provisional** | Just promoted; believed but barely tested | Default for any newly promoted principle (≥2 evidence sources) |
| **Established** | Applied and held across multiple real decisions | Applied and held in ≥3 distinct **projects** (not sessions within one project), 0 unexplained reversals |
| **Core** | Load-bearing; expensive to be wrong about | Established + repeatedly relied on + no reversals over a sustained period |
| **Contested** | Has been violated or reversed; under review | Any principle with ≥1 reversal that contradicts it |

A reversal drops a principle one tier and marks it `Contested` until reviewed. A `Contested` principle is a strong signal to rewrite or retire it.

**Distinct projects, not sessions** (clarified after the first calibration run): the bar is ≥3 distinct *projects*, because multiple sessions within one project all test the principle against the same conditions. A principle with many applications all from a single project is strong evidence within that context but has not been validated across contexts.

**Single-project-dependency flag:** when ≥80% of a principle's applications come from one project, mark it with `†` in the Tier cell (e.g., `Established †`). This signals "well-tested, but only in one context" — so broad validation is never overclaimed. The flag clears once a second project exercises the principle. On the first run most Established tiers will carry `†` because one project dominates the portfolio; that is expected and honest.

The `†` flag is a prompt to seek breadth, not a discount of depth. A dense, long-running project that produced many distinct lessons across different lanes is stronger single-project evidence than a thin one — the flag says "validate this in a second context when one arrives," not "trust this less." Depth earns the tier; breadth removes the flag.

## The Calibration Section

Calibration data lives in a `## Calibration` section at the bottom of each MINDSET.md — keeping the principle prose clean while co-locating the evidence in one file. Format:

```
## Calibration
<!-- Maintained by /vcos-calibrate. Do not hand-edit counts. Last run: YYYY-MM-DD -->

| Principle (short ref) | Tier | Applied | Reversed | Last validated |
|-----------------------|------|---------|----------|----------------|
| Ship the smallest useful version first | Established | 4 | 0 | 2026-06 |
| Check "what if it's empty or wrong" before shipping | Provisional | 2 | 0 | 2026-06 |
```

Principles not yet in the table are treated as Provisional.

## When to use

- Inside the biweekly `/vcos-review` (see `MAINTENANCE_CADENCE.md`), batched across all MINDSETs
- When `/vcos-session-close` reports calibration is due
- Immediately after a STANCE entry records a principle being reversed (catch Contested early)

## Context Requirement

- The MINDSET.md being calibrated (project or persona) and its current `## Calibration` section
- The STANCE logs that provide evidence: `projects/*/project cognitive layer/STANCE.md`
- For persona calibration: STANCE entries tagged with that `[persona-name]`

**Confidentiality gate:** check each project's classification in `projects/INDEX.md` (see `standards/CONFIDENTIALITY.md`). Evidence from **NDA** projects is excluded entirely. Evidence from **Confidential** projects may inform counts, but any reference written to a shared/tracked file (the ledger, a report) must use a neutral handle ("a confidential project") — never the project name or specifics. Unclassified projects are treated as NDA (excluded).

## Inputs

- A target scope: one persona, one project, or "all" for a full batch
- STANCE evidence since the last calibration run

## Process

1. **Identify applications.** Read STANCE entries since the last run. For each, ask: did this decision apply one of the MINDSET's principles? Match by domain and intent, not exact wording. Count an application.

2. **Identify reversals.** Look for STANCE entries tagged `[Mistake]` or decisions that were later undone. If a reversal contradicts a principle, count it against that principle.

3. **Recompute tiers** using the entry conditions above. Promote principles that crossed a threshold; demote and mark `Contested` any with new reversals.

4. **Update the Calibration section** of the MINDSET with new counts, tiers, and the run date. Do not touch the principle prose itself.

5. **Surface the review list.** Report any principle now `Contested` — these need a human decision: rewrite, narrow the scope, or retire via `/vcos-consolidate`.

## Required output

- Updated `## Calibration` section in each target MINDSET — applied directly
- **Append each new Contested principle as a Pending item in `global cognitive layer/review_queue.md`** — with what/why/decision-needed (rewrite/retire/keep)/recommendation/source
- A calibration report: tier changes (promotions and demotions), new Contested principles, principles with the most applications (your load-bearing set)
- Updated `last calibrated` date in the maintenance ledger

## Checks before finalizing

- [ ] Principle prose was not edited — only the Calibration section
- [ ] Every tier change traces to specific STANCE evidence
- [ ] Reversals correctly produced Contested flags
- [ ] Contested principles are surfaced for human review, not silently changed
- [ ] Counts are cumulative, not reset each run
