---
name: vcos-spec
description: Turn raw notes or problem statements into a concise VCOS Build Packet draft.
---

# VCOS Spec Skill

> **Ownership:** Sam (Tech Lead) · **Mode:** auto-run (domain skill). See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill when you need to turn messy notes into a first-pass Build Packet.


## Context Requirement
Before performing this workflow:
- Read PROJECT_CONTEXT.md
- Confirm current phase and constraints
  
## Inputs
- Raw notes, bullets, chat excerpts, or a problem statement
- Optional existing Project Context or prior Build Packet sections

## Process
1. Identify who is affected, what is happening, and why it matters.
2. Draft the Build Packet sections in order.
3. Keep the MVP small and safe.
4. Mark assumptions clearly when information is missing.
5. Prefer read-only or human-in-the-loop first slices.

## Required output
Write a Build Packet draft in the project's `docs/build_packet.md` with these sections:
- Title, Owner, Date
- Problem Summary (incl. frequency / impact, current workaround)
- Users & Workflow (current + desired)
- Success Metrics (metric, baseline, target)
- MVP Scope (in / out of scope)
- Acceptance Criteria (Given / When / Then)
- Inputs & Outputs
- UI / UX Notes
- Architecture Decision
- Data Sources
- Edge Cases & Failure Scenarios
- Test Plan stub
- Deployment Plan stub
- Version Ladder (v1 / v2 / later)
- Open Questions & Assumptions

## Checks before finalizing
- The MVP is small enough to build in a few days.
- If any sensitive data is in play, it's noted.
- Acceptance criteria are testable.

## GAPS section (append to every output)

After the Build Packet draft, always append a `## GAPS` section with three parts:

**Signals that are thin or missing:**
List any sections where the input was insufficient to be confident — e.g., no clear user defined, success metrics guessed, data source unconfirmed. Be specific about what is missing and why it matters.

**Lenses with low coverage:**
Flag any angle that wasn't fully thought through due to missing input — e.g., "data flow unclear — source schema unknown" or "no one has looked at how this fails."

**What would sharpen this spec:**
Give 2-3 concrete questions or inputs that would most improve the output — e.g., "Confirm what data this touches" or "Clarify whether this runs on a schedule or on-demand — affects the deployment plan."

Keep the GAPS section under 10 lines. Its purpose is to make the spec's confidence level visible, not to block progress.
