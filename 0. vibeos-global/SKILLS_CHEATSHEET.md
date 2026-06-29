# VibeOS Skills — Cheat Sheet

One place to see every shipped skill: who owns it, when it should fire, and whether it runs on its own or waits for you. If you can't remember what exists, start here.

## How skills run
- **Domain skills** belong to a teammate. When you're working with that teammate and a request clearly matches, they run the *(auto)* ones themselves and tell you what they did. The *(confirm)* ones they offer first, since those write multiple files.
- **Your rituals** are yours to invoke. They tend the system and are never auto-run by a teammate.
- Auto-run only ever means "produce a draft or analysis in the current work." Nothing that changes the shared memory runs without your sign-off.

## Setup & team-building
| Skill | Owner | When | Mode |
|-------|-------|------|------|
| `/vibeos-init` | you | first run — get oriented and ready | you invoke |
| `/vibeos-tutorial` | you | a guided Day 1 walkthrough | you invoke |
| `/vibeos-new-persona` | you | adding a new teammate | you invoke |
| `/new-vibeos-project` | you | starting a new project — scaffold + register it | you invoke |

## Doing the work (teammate-owned)
| Skill | Owner | Fires when | Mode |
|-------|-------|-----------|------|
| `/vcos-spec` | Ada (→ Sam) | a fuzzy problem needs framing into a plan | auto |
| `/vcos-build` | Sam | a plan needs turning into small, ordered steps | auto |
| `/vcos-status` | Ada | you need a compact snapshot of where a project stands | auto |
| `/vcos-memory` | Sam, Robin | logging decisions to STANCE and promoting recurring patterns to SIGNALS | confirm |

## Keeping the memory alive (you — on cadence)
| Skill | When |
|-------|------|
| `/vcos-session-close` | **end of every work session — the one ritual to keep.** Captures decisions and lessons back into the cognitive layer |

## Advanced — later
Once you have a few projects, these keep the memory sharp instead of just big. Skip them on Day 1.
| Skill | When |
|-------|------|
| `/vcos-review` | periodic check-in — runs due upkeep and presents anything needing your judgment |
| `/vcos-calibrate` | inside review — mark each principle's confidence from real evidence |
| `/vcos-synthesize` | inside review — promote patterns that recur across projects to the global layer |
| `/vcos-consolidate` | inside review — merge near-duplicates and retire stale entries (archived, not deleted) |

## Notes
- **Tool-agnostic:** in Claude Code, Codex, and Cursor these are slash commands; in a plain chat tool the teammate performs the same workflow inline from its starter prompt.
- The auto-run policy lives in `standards/SKILL_STANDARD.md`. Ownership lives in each persona's `PERSONA.md` ("Skills in your lane").
