# Current Status Overview Instructions

## Purpose
Create a compact, PRD-prep overview that explains the current state of a project so a PRD-focused GPT can efficiently draft the next build packet for a new phase, major feature, or version slice.

This is not a new build packet.
It is a handoff summary for planning the next build packet well.

Default downstream persona:
- @sam (your maker persona)

## Use This When
- the project has gotten more complex
- you are considering a `v2+` or major feature PRD
- you want to preserve the original build packet and create a new one
- you need a GPT to understand current state before drafting the next PRD

## Inputs
- `docs/project_context.md`
- `docs/build_packet.md`
- any files in `docs/build_packets/` if they exist
- `docs/build_packet_index.md` if it exists
- `project cognitive layer/STANCE.md`
- `project cognitive layer/SIGNALS.md`
- `project cognitive layer/MINDSET.md`
- relevant TDD / security docs if they materially affect the next slice

## Required Output
Create a concise “Current Status Overview” with enough context for a PRD-focused GPT to write the next build packet.

## Output Format

# Current Status Overview

## Project Identity
- project name
- what the project is
- who it serves

## Current Active Slice
- current active build packet
- current phase / version / major surface being worked on
- what is actively in scope right now

## What Already Exists
- major capabilities, deliverables, or decisions already in place
- what has already been built, defined, or proven
- what should be treated as stable context

## What Has Changed Since The Original PRD
- new constraints
- new opportunities
- changed scope boundaries
- new integrations, risks, or workflow complexity

## Open Tensions
- what is unclear
- what is overloaded in the current planning surface
- where a fresh PRD may be justified

## Recommended Next PRD Slice
- proposed name for the new build packet
- what that build packet should cover
- what it should explicitly not cover

## Inputs The PRD GPT Should Treat As Source Of Truth
- list the exact files that matter for the next PRD

## Preservation Rules
- which older build packets must remain intact
- what historical context should be preserved instead of rewritten

## Rules
- keep it concise and operational
- optimize for handoff clarity, not completeness
- distinguish stable context from proposed next-slice changes
- do not rewrite history to make the project look cleaner than it was
- call out ambiguity explicitly
- if a new build packet is not actually warranted, say so clearly

## Recommended Handoff

After creating this overview, hand it to @sam (your maker persona) with instructions to do one of two things:
- run a short PRD-prep interview if the next slice is still fuzzy
- draft the next build packet if the slice is already clear enough

Suggested handoff:

```text
You are the maker persona for this project.

Use the Current Status Overview plus the referenced source files to determine
whether the next slice is clear enough for direct PRD drafting.

If it is not clear enough:
- summarize the slice in 2-3 sentences
- ask 2-3 high-signal questions per round
- stop after at most 3 rounds

If it is clear enough:
- draft the next build packet as a clean, minimal, buildable PRD
- preserve the existing root build packet
- use the proposed slice file named in the overview
```
