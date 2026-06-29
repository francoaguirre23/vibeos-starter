---
name: vcos-session-close
description: End-of-session ritual — capture decisions, patterns, and lessons from any session (including non-file-capable tools) back into the cognitive layer.
---

# VCOS Session Close

> **Ownership:** Operator ritual — human-invoked at the end of a work session. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill at the end of any working session to capture what was learned before it evaporates. This is the write-back ritual that keeps the cognitive layer current — especially important after sessions in tools that cannot write files (ChatGPT, Claude.ai, or any chat-only tool).

## When to use

- At the end of any substantive VibeOS session
- After a session in a non-file-capable tool, run this in Codex or Claude Code to commit what was learned
- Before switching projects or closing out a work block
- The `/loop` or a Stop hook may prompt this automatically

## Context Requirement

Before performing this workflow:
- Read `docs/project_context.md` (or `PROJECT_CONTEXT.md`) to confirm current goal and phase
- Read the project's current STANCE.md, SIGNALS.md, and MINDSET.md
- If a specialist persona was active, note which one (decisions get tagged with `[persona-name]`)

## Inputs

- What happened this session: decisions made, mistakes corrected, patterns noticed, conflicts resolved
- For sessions in other tools: a plain-language recap of the session, which you translate into structured entries
- The active persona(s), if any

## Process

1. **Append to project STANCE.md** — one entry per high-signal event. Keep each ≤3 lines. Tag type ([Decision], [Heuristic], [Constraint], [Mistake], [Conflict], [Preference], [Observation]) and source ([self] or [persona-name]). Mark `[Recurring]` if the pattern has appeared ≥2x.

2. **Promote recurring patterns to SIGNALS** — if a STANCE pattern has recurred, stage it in the right SIGNALS file:
   - Project-specific pattern → project `SIGNALS.md`
   - Persona craft pattern → `0. vibeos-global/personas/[name]/SIGNALS.md`
   Include: pattern, type, source, evidence, confidence, scope.

3. **Update PROJECT_CONTEXT.md if needed** — only when a major decision, phase change, or new constraint occurred. Keep it ≤100 lines.

4. **Flag MINDSET promotions** — if a SIGNALS pattern is now High confidence, Clearly general, and seen in ≥2 contexts, flag it `→ Eligible for MINDSET promotion`. Do not edit MINDSET directly here — that is the `/vcos-memory` promotion step.

5. **Update the project INDEX row** — if the project's phase or status changed, update its row in `projects/INDEX.md` and the summary row in `OS_INDEX.md`.

6. **Report review status (pull-based automation).** Read `0. vibeos-global/global cognitive layer/maintenance_ledger.md` and `review_queue.md`. Report:
   - Whether the **biweekly `/vcos-review`** is due (days since last run)
   - How many items are sitting in the review queue's Pending section
   If the review is due or the queue has Pending items, prompt the user to run `/vcos-review`. That one routine runs the due maintenance (calibrate → synthesize, consolidate if quarter-due) and walks through the decisions. See `MAINTENANCE_CADENCE.md`.

## Required output

- Updated STANCE entries (the session log)
- New or updated SIGNALS entries for any recurring patterns
- A short summary: what was decided, what was learned, what is flagged for promotion, what changed in the index
- A review status line: is `/vcos-review` due, and how many items are in the queue's Pending section

## Checks before finalizing

- [ ] STANCE entries are append-only — no history rewritten
- [ ] Each entry is short, specific, and source-tagged
- [ ] Patterns promoted to SIGNALS only when genuinely recurring or general
- [ ] MINDSET was not edited directly (flagged only)
- [ ] PROJECT_CONTEXT updated only if a high-signal change occurred
- [ ] Index rows updated if phase/status changed
- [ ] Review status reported (is /vcos-review due; how many Pending queue items)

## Note for non-file-capable tools

If this session happened in ChatGPT, Claude.ai, or any chat-only tool: paste the session recap into Codex or Claude Code and run this skill there. The discipline is tool-agnostic — the capture must land in the canonical files, which only file-capable tools can write.
