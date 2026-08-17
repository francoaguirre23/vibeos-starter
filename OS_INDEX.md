# VibeOS OS Index
<!-- Master inventory of personas, skills, standards, and the cognitive layer. -->

> **VibeOS is an operating system for running a team with AI.** Named teammates, a shared memory that compounds across projects, and repeatable skills — all plain Markdown and tool-agnostic.

<!--
MAINTENANCE — update this file when a persona, skill, or standard is added, renamed, or retired.
When you update this file, also update CLAUDE.md (personas and skills tables).
The /vcos-session-close ritual will prompt this check.
-->

---

## Personas

Invoke with `@handle` in Claude Code, Codex, or Cursor — or paste a persona's `STARTER_PROMPT.md` into any plain chat tool. Always start with Ada.

| Persona | Role | Invoke when |
|---------|------|-------------|
| `@ada` | Chief of Staff — orchestrator; the one you talk to first | A request is fuzzy or tangled; you don't know where to start |
| `@sam` | Tech Lead — maker, with a light sanity check | Something needs to get built or drafted |
| `@robin` | Reviewer — "what might break, what's missing" | You want a fresh pair of eyes before you ship |

Add a teammate with `/vibeos-new-persona`.

---

## Skills

Invoke with `/skill-name`.

### Active — the everyday set
| Skill | Invoke when |
|-------|-------------|
| `/vibeos-init` | First-run setup wizard — get oriented and ready |
| `/vibeos-tutorial` | Guided Day 1 walkthrough |
| `/vibeos-new-persona` | Add a new teammate |
| `/new-vibeos-project` | Start a new project with full scaffold and registration |
| `/vcos-spec` | Frame a problem into a plan |
| `/vcos-build` | Turn a plan into ordered steps |
| `/vcos-memory` | Capture decisions and patterns into the cognitive layer |
| `/vcos-meeting-context` | Load a meeting transcript (Granola, Fathom, Zoom…) as framed context — calibrates who-said-what to the source |
| `/vcos-session-close` | **The one ritual to keep** — end-of-session capture into memory |
| `/vcos-status` | A compact snapshot of where a project stands |
| `/vcos-retro` | Close-out ritual — a short retro plus distilling SIGNALS into a MINDSET |

### Advanced — later, once you have a few projects
Keep the memory sharp instead of just big. Not needed on Day 1.
| Skill | Invoke when |
|-------|-------------|
| `/vcos-review` | Periodic check-in; surfaces anything needing your judgment |
| `/vcos-calibrate` | Mark how confident the team is in each principle, from real evidence |
| `/vcos-synthesize` | Promote lessons that recur across projects to the global layer |
| `/vcos-consolidate` | Merge near-duplicates and retire stale entries (archived, not deleted) |
| `/vcos-simplify-review` | Review a diff, file, or slice for unnecessary complexity — a delete/shrink/reuse list (Robin) |

---

## Cognitive Layer

### Promotion flow

```
Session work
    ↓ append
Project STANCE          ← real-time decision log
    ↓ when recurring
Project SIGNALS         ← pattern staging area
    ↓ at a milestone
Project MINDSET         ← distilled, durable principles

(same shape per persona, and globally)

Project MINDSET         ← when the same pattern appears across projects
    ↓ propose  (/vcos-synthesize)
GLOBAL_SIGNALS → GLOBAL_MINDSET
```

The one ritual that keeps this alive is `/vcos-session-close`. Friendly primer: `COGNITIVE_LAYER_101.md`.

### Key files

| File | Location | Purpose |
|------|----------|---------|
| STANCE.md | `projects/[name]/project cognitive layer/` | Append-only decision log |
| SIGNALS.md | `projects/[name]/project cognitive layer/` | Recurring pattern staging |
| MINDSET.md | `projects/[name]/project cognitive layer/` | Distilled project principles |
| GLOBAL_SIGNALS.md | `0. vibeos-global/global cognitive layer/` | Cross-project pattern staging |
| GLOBAL_MINDSET.md | `0. vibeos-global/global cognitive layer/` | Synthesized cross-project principles |

---

## Standards

Kept standards live in `0. vibeos-global/standards/`.

| File | Purpose |
|------|---------|
| `PERSONA_STANDARD.md` | Structure and conventions for personas |
| `SKILL_STANDARD.md` | Structure and conventions for skills |
| `CLAUDE_CODE_INTEGRATION.md` | How personas and skills wire into Claude Code |
| `CONFIDENTIALITY.md` | Keeping projects local and the shared layer clean |
| `MAINTENANCE_CADENCE.md` | How the cognitive layer compounds and stays sharp over time |
| `VIBEOS_PROJECT_STANDARD.md` | How a project should be set up and run |
| `ENGINEERING_DEFAULTS.md` | Default engineering decisions and constraints |
| `MODEL_TIER_PARITY.md` | Getting a lower-tier model to operate like the top tier (capability elicitation) |

---

## Your projects

_Your projects live under `projects/` (gitignored, local) and are not tracked in this framework repo. Add a row here per project as you create them, or let `/new-vibeos-project` manage it._

| Project | Status | Notes |
|---------|--------|-------|
| _(none yet — create one with `/new-vibeos-project`)_ | | |

A read-only sample lives in `examples/sample-project/` so you can see a finished one.
