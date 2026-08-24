# Session Skills Overview (session-start + session-close)

Replication brief for the two thread-hygiene skills. They are a pair: **close** (capture) → open a new thread → **start** (rehydrate). This is what lets threads stay short without losing continuity. See `THREAD_HYGIENE.md` for why.

## `vcos-session-close` — end-of-session write-back

**Purpose:** capture what a session learned into the cognitive layer before it evaporates. The forcing function that keeps STANCE/SIGNALS/MINDSET current.

**When:** end of any substantive session; before switching projects; after work in a tool that cannot write files (paste a recap into a file-capable tool and run it there).

**Inputs:** the session's decisions/mistakes/patterns; the active teammate if any; the project's `project_context.md` + STANCE/SIGNALS/MINDSET.

**Process:**
1. Append to project `STANCE.md` — one entry per high-signal event, ≤3 lines, tagged by type (`[Decision]`/`[Heuristic]`/`[Constraint]`/`[Mistake]`/`[Conflict]`/`[Preference]`/`[Observation]`) and source (`[self]` or `[teammate]`); mark `[Recurring]` if seen ≥2×.
2. Promote recurring patterns to the right `SIGNALS.md` (project vs teammate).
3. Update `project_context.md` only on a major change (phase/constraint).
4. Flag MINDSET-eligible patterns (don't edit MINDSET here; that's `/vcos-memory`).
5. Update `projects/INDEX.md` + `OS_INDEX.md` rows if phase/status changed.
6. Report review status (is `/vcos-review` due, queue backlog?).

**Guardrails:** STANCE is append-only; never edit MINDSET directly; capture must land in canonical files.

## `vcos-session-start` — open-of-session rehydrate

**Purpose:** pick up an existing project in a fresh thread by loading its durable state, so the new thread starts sharp instead of inheriting a long compacted one. The open-of-session counterpart to session-close, and the enabler of thread hygiene.

**When:** opening a fresh thread on a project you've worked before; returning after time away; right after closing a long thread. **Not** for creating a project (route to `/new-vibeos-project`).

**Inputs (read only the target project):** `project_context.md`, recent `STANCE.md` (last ~20–30 entries), `SIGNALS.md`, `MINDSET.md`.

**Process:**
1. Identify the project; if it doesn't exist, stop and route to `/new-vibeos-project`.
2. Rehydrate the files above (durable files are truth, not stale thread history).
3. Produce a **compact orientation**: project + phase (1 line); where it stands (3–5 bullets from latest STANCE); open loops/tensions; 1–3 governing MINDSET/SIGNALS items; one recommended next slice.
4. Hand off to `/vcos-status` for the fuller snapshot; don't start work until the user picks the slice.
5. Do not modify the cognitive layer (capture is session-close's job).

**Guardrails:** resume-only (never scaffold); read only the target project, not the whole workspace; a thread is not a project; keep the orientation under a screen (if it's growing, you're re-deriving instead of rehydrating).
