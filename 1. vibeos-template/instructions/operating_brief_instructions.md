# OPERATING_BRIEF Instructions

## Purpose
Guide the creation or update of an Operating Brief — the canonical planning artifact for
Eng Ops projects (org transitions, process redesigns, executive analyses, strategic
initiatives, operating-model work). It is to Eng Ops work what the Build Packet is to
software: the place the problem, the decision, and the rollout get framed.

## Use This When
- the project's deliverable is a decision, framework, analysis, or operating change — not a tool
- you are framing a build-vs-buy, a restructuring, a transition, a standard, or a cadence
- a leadership-facing decision needs options, tradeoffs, owners, and follow-through

If the project builds software, use `build_packet_instructions.md` instead.

## Inputs
- Raw problem notes, exec context, interview/discovery inputs
- Existing `docs/operating_brief.md` if one exists
- `docs/project_context.md` and the project STANCE

## Required Output
A concise, decision-oriented brief that a busy senior audience can act on.

## Required Sections
- Title
- Owner
- Confidentiality
- Situation
- The Decision(s) To Be Made
- Options & Tradeoffs
- Recommendation (or "framing only")
- Stakeholders & Owners (including named seam owners)
- Constraints & Risks (with assumptions labeled)
- What "Done" Looks Like
- Follow-Through & Cadence
- Out Of Scope
- Open Questions
- Links
- Next Step

## Rules
- Lead with the decision, not the background — this is a decision brief, not a report
- Every brief must name a decision; a brief with no decision is a status update
- Name owners and seam owners explicitly — unowned hand-offs stall and relitigate
- Surface assumptions, risks, and tradeoffs; visible gaps beat hidden ones
- Keep options honest — show the real downside of the recommended path
- Design follow-through so the decision isn't relitigated
- Keep it tight; prefer clarity over completeness
- If NDA/confidential, note handling constraints and keep specifics out of shared indexes

## Relationship To Other Artifacts
- `project_context.md` — durable vision/goal/constraints (the standing context)
- `operating_brief.md` — the active decision being framed (this file)
- `STANCE.md` — the running log of decisions made as the work progresses
- If executing the decision requires a tool, create a Build sub-slice with its own `build_packet.md`

## Multi-Brief SOP
When a project spawns a materially different decision (new phase, new pillar):
- preserve the current `operating_brief.md`
- create a new named file under `docs/operating_briefs/`
- track which is current (mirror the build_packet_index pattern)

## Safety Checks
- Anything private stays in the project; don't copy it into shared indexes
- No individual comp/leveling or personnel-sensitive detail unless the project explicitly requires it and handling is noted
- If risk or sensitivity is unclear, default conservative
