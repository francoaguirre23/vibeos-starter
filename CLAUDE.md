# VibeOS Workspace

VibeOS is an operating system for running a team with AI. It gives you named teammates you can talk to, a shared memory that compounds across projects, and a set of repeatable skills — all plain Markdown, tool-agnostic, and yours to extend.

New here? Start with the [README](README.md), then the [TUTORIAL](TUTORIAL.md). Run `/vibeos-init` to set yourself up.

<!-- MAINTENANCE: When a persona or skill is added, renamed, or retired — update the tables
     in this file AND OS_INDEX.md. The /vcos-session-close ritual will prompt this check. -->

## Workspace Structure

- `0. vibeos-global/` — Shared framework: personas, global cognitive layer, standards, scripts
- `1. vibeos-template/` — Project scaffold (copied into new projects; never used directly)
- `2. vibeos-skills/` — Canonical skill definitions (used by all tools; never copy content from here)
- `routing/` — Tool-agnostic agent/command routing (the source `.claude/` is generated from)
- `projects/` — Your projects (gitignored, local; created via `/new-vibeos-project`)
- `examples/` — A read-only sample project showing what "done" looks like

## Personas (your teammates)

Invoke with `@handle`. Each persona reads its own definition before responding, so it shows up in character. Always start with Ada.

| Teammate | Role | Invoke when |
|----------|------|-------------|
| `@ada` | Chief of Staff — orchestrator; the one you talk to first | A request is fuzzy or tangled; you don't know where to start. Ada frames it and routes it. |
| `@sam` | Tech Lead — maker, with a light sanity check | Something needs to get built or drafted. |
| `@robin` | Reviewer — "what might break, what's missing" | You want a fresh pair of eyes before you ship. |

Add a teammate with `/vibeos-new-persona`.

## Skills

Type `/` to see them. Not sure which to reach for? See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

### Active — the everyday set
| Skill | When to use |
|-------|-------------|
| `/vibeos-init` | First-run setup wizard — get oriented and ready |
| `/vibeos-tutorial` | Guided Day 1 walkthrough |
| `/vibeos-new-persona` | Add a new teammate |
| `/new-vibeos-project` | Start a new project with full scaffold and registration |
| `/vcos-spec` | Frame a problem into a plan |
| `/vcos-build` | Turn a plan into ordered steps |
| `/vcos-memory` | Capture decisions and patterns into the cognitive layer |
| `/vcos-meeting-context` | Load a meeting transcript (Granola, Fathom, Zoom…) as framed context — calibrates who-said-what to the source |
| `/vcos-session-start` | Pick up an existing project in a fresh thread — rehydrate its memory into a compact orientation (pairs with `/vcos-session-close`) |
| `/vcos-session-close` | **The one ritual to keep** — end-of-session capture into memory |
| `/vcos-status` | A compact snapshot of where a project stands |
| `/vcos-retro` | Close-out ritual — a short retro plus distilling SIGNALS into a MINDSET |

### Advanced — later, once you have a few projects
These keep the memory sharp instead of just big. You don't need them on Day 1.
| Skill | When to use |
|-------|-------------|
| `/vcos-review` | Periodic check-in; surfaces anything needing your judgment |
| `/vcos-calibrate` | Mark how confident the team is in each principle |
| `/vcos-synthesize` | Promote lessons that recur across projects to the global layer |
| `/vcos-consolidate` | Tidy up: merge near-duplicates, retire stale entries (archived, not deleted) |
| `/vcos-simplify-review` | Review a diff, file, or slice for unnecessary complexity — a delete/shrink/reuse list (Robin) |

## Identity Layer

Two short files anchor every session. Read them first:

- `0. vibeos-global/SOUL.md` — VibeOS operating principles, voice, and design philosophy
- `0. vibeos-global/USER.md` — your role, context, and working style (machine-local; created during setup)

## Cognitive Layer (the team's memory)

Three levels, building on each other, per project:

- `STANCE.md` — append-only decision log (updated in real time)
- `SIGNALS.md` — recurring patterns (promoted from STANCE when something repeats)
- `MINDSET.md` — distilled, durable principles (filled at a milestone, from SIGNALS)

The same shape exists per teammate and globally. The forcing function that keeps it alive is `/vcos-session-close`. Full primer: [COGNITIVE_LAYER_101.md](COGNITIVE_LAYER_101.md).

## How to start

1. `bash scripts/setup_machine.sh` — stamps your machine path, generates `.claude/`.
2. `/vibeos-init` — the first-run wizard.
3. `@ada` — say what you're trying to do.

Create a project anytime with `/new-vibeos-project "My Project"`.
