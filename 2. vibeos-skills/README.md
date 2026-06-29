# VibeOS Skills

This folder contains canonical skill definitions for the VibeOS workflow.
Skills are tool-agnostic — used by Codex natively and dispatched to by Claude Code commands.

## Structure
Each skill lives at `skills/<skill-name>/` and contains:
- `SKILL.md` — the canonical workflow definition (the single source of truth)
- `agents/openai.yaml` — the Codex/OpenAI interface descriptor

## Canonical inventory
Do not maintain a skill list here (it goes stale). The authoritative, always-current
inventory lives in:
- `OS_INDEX.md` — skills grouped by category
- `0. vibeos-global/SKILLS_CHEATSHEET.md` — skill → owner → trigger → mode
- `0. vibeos-global/standards/SKILL_STANDARD.md` — structure, ownership policy, and the Current Skills table

## Rule of thumb
- Skills = reusable workflow instructions
- Repo docs = live project state and outputs
- Never copy skill content into tool-specific files — reference the canonical `SKILL.md` instead
