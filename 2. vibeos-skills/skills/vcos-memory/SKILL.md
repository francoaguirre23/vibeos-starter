---
name: vcos-memory
description: Maintain the VCOS memory layer by updating STANCE, SIGNALS, and MINDSET artifacts.
---

# VCOS Memory Skill

> **Ownership:** Operator ritual — human-invoked on demand to log decisions/patterns. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill when project decisions, mistakes, or repeated patterns should be captured.

## Context Requirement
Before performing this workflow:
- Read PROJECT_CONTEXT.md
- Confirm current phase and constraints

## Inputs
- Recent decisions, bugs, constraints, or behavioral patterns
- Current STANCE, SIGNALS, and MINDSET contents
- The rule files for each memory layer

## Cost discipline (run this cheaply)

- **Model tier.** Run on a mid or high tier, not the top tier — capture and promotion are light. Apply the `MODEL_TIER_PARITY` operating block.
- **Fresh, small context.** Run this in its own short session (or early), not at the tail of a long working thread, or the whole accumulated context gets re-billed. Capture from a brief recap of the decisions, not the full transcript.
- **Scope to the active project.** Read only the relevant project's STANCE/SIGNALS/MINDSET, not the whole workspace.
- **Don't double-run.** `/vcos-session-close` already performs this capture. Run one or the other, not both.

## Process
1. Append only to STANCE for high-signal project events.
2. Promote recurring patterns into SIGNALS when they generalize.
3. Propose MINDSET updates only when evidence is strong.
4. Keep each entry short and specific.
5. Do not rewrite long history.

## Required output
- Updated STANCE entries when appropriate
- SIGNALS entries for recurring patterns
- Proposed MINDSET updates, never direct edits

## Checks before finalizing
- STANCE stayed project-specific.
- SIGNALS captured only recurring or general patterns.
- MINDSET was not edited directly.
- If a persona MINDSET was updated → regenerate that persona's STARTER_PROMPT.md.
- If a persona or skill was added, renamed, or removed → update OS_INDEX.md and CLAUDE.md in the workspace root.

## STARTER_PROMPT.md Refresh

When a persona's MINDSET.md is updated, regenerate that persona's STARTER_PROMPT.md.

Location: `0. vibeos-global/personas/[name]/STARTER_PROMPT.md`

The STARTER_PROMPT.md is a self-contained snapshot used in tools without file access
(ChatGPT, Claude.ai, or any chat-only tool). It must stay in sync with MINDSET.md or it drifts.

Refresh trigger: any MINDSET promotion that adds, removes, or materially changes a principle.
Update the `Last updated` date in the file header when regenerating.


## PROJECT_CONTEXT.md Management

Always:
- Read PROJECT_CONTEXT.md at the start of any task
- Use it to understand:
  - current goal
  - current phase
  - key decisions
  - constraints

Update PROJECT_CONTEXT.md when:
- A major decision is made
- The current phase changes
- New constraints appear
- A key lesson is learned

Rules:
- Keep it concise (≤100 lines)
- Do not log everything (STANCE handles that)
- Only include high-signal context needed to continue work