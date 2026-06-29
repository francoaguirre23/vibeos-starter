# Global SIGNALS Instructions

## Purpose
Maintain GLOBAL_SIGNALS.md as the cross-project staging layer between
completed project MINDSETs and the Global MINDSET.

This is the holding area for patterns that look general enough to belong
in the Global MINDSET but have not yet been confirmed across ≥2 projects.
It is not a permanent file — entries either get promoted or quietly expire.

---

## When to Use
- After completing a project and distilling its project MINDSET
- When a project MINDSET entry is flagged in "Open Promotions → Global MINDSET"
- When reviewing patterns across multiple completed projects
- Before a periodic Global MINDSET review (quarterly or after a cluster of projects)

## Inputs
- Project MINDSET.md files — specifically the "Open Promotions → Global MINDSET" section
- Persona MINDSET files — if a pattern has crossed from specialist craft into general behavior

## Required Output
Append candidate entries to GLOBAL_SIGNALS.md using the format below.

---

## Entry Format

Pattern:
<short distilled statement — one clear idea>

Type:
Heuristic / Anti-pattern / Preference / Risk pattern

Source:
[self] or [persona-name] — who originated this pattern

Evidence:
- Project: <name> — <1 line from that project MINDSET or SIGNALS>
- Project: <name> — <1 line from that project MINDSET or SIGNALS>

Confidence:
Low / Medium / High

Scope:
Likely general / Clearly general

---

## Rules

- Append only — do not edit or delete past entries
- Every entry must have evidence from at least one completed project MINDSET
- Do not include project-specific constraints or tool-specific behavior
- Keep entries concise — one pattern per entry, ≤5 lines of evidence
- Do not duplicate patterns already in GLOBAL_MINDSET.md

---

## Promotion Criteria → Global MINDSET

Eligible for promotion to GLOBAL_MINDSET.md if ALL of the following are true:

- Confidence = High
- Scope = Clearly general
- Evidence spans ≥2 project MINDSETs (not just SIGNALS or STANCE)
- Not tied to a specific tool, system, team, or one-off constraint
- Still feels true when you imagine a project you haven't done yet

If only one project supports it, leave it here and revisit after the next project.

---

## How to Promote

Do NOT edit GLOBAL_MINDSET.md directly.

1. Identify entries here that meet all promotion criteria above.
2. Write a formal proposal using the format in global_mindset_instructions.md.
3. Review the proposal — does it feel true across contexts, not just one?
4. Apply only the ones that pass that test.
5. Remove or archive the promoted entry from GLOBAL_SIGNALS.md.

---

## What NOT to Include

- Raw STANCE log entries from any project
- Tool-specific behavior or stack decisions
- Patterns tied to a single team, client, or project constraint
- Patterns you hope are true but haven't seen repeat
- Anything already captured in GLOBAL_MINDSET.md
