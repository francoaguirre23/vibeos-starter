# VibeOS Persona System

Personas are named specialists you can talk to. Each one has a distinct lens — the questions it asks — and a clear lane. You invoke a persona when you want that kind of thinking applied to your work. Personas are shared across all projects and never copied in; they live here in `0. vibeos-global/personas/` and are referenced by path.

This starter ships with three personas — a minimal, broadly useful set that covers the whole arc of getting something done: **frame it, make it, check it.**

---

## The Three-Archetype Starter Set

| Persona | Archetype | Invoke when |
|---------|-----------|-------------|
| **Ada (Chief of Staff)** | Orchestrator — frame & route | Your request is fuzzy, spans several things, or you're not sure who should own it. Start here. |
| **Sam (Tech Lead)** | Maker — build & sanity-check | A plan is ready and it's time to make something: code, a document, or a process. Sam also gives a light "does this hang together?" read. |
| **Robin (Reviewer)** | Critic — review & advise | Something's been made and you want a fresh, skeptical look: what might break, what's missing, what's unclear. |

A typical loop: **Ada** frames your request and routes it → **Sam** builds it → **Robin** reviews it → **Ada** pulls the pieces back into one answer.

These three are deliberately generic and friendly. They work whether you're technical or not. Add your own specialists on top of them (see below).

---

## The 4-File Persona Structure

Every persona folder contains exactly four files:

- `PERSONA.md` — the authoritative role definition: role, lens, when to invoke, what you produce, handoffs, what you never do, output style, and what to read first.
- `MINDSET.md` — the persona's durable principles, accumulated over time. Updated only by promoting patterns from SIGNALS, never edited mid-work. Starts empty.
- `SIGNALS.md` — a staging area for emerging patterns worth watching, before they earn a place in MINDSET. Each entry is source-tagged. Starts empty.
- `STARTER_PROMPT.md` — a self-contained, portable version of the persona you can paste into any tool (ChatGPT, Codex, Cursor, Claude) with no file access required.

`PERSONA.md`, `MINDSET.md`, and `SIGNALS.md` are the source of truth. `STARTER_PROMPT.md` is the portable interface — handy, but not a replacement for the full set.

For the full conventions (folder naming, required sections, promotion rules), see `0. vibeos-global/standards/PERSONA_STANDARD.md`.

---

## The Cognitive Layer, in Brief

VibeOS keeps two tracks of accumulated learning:

- **Per-project track** — what happened on a given build, captured in each project's `STANCE.md` (decision log) → `SIGNALS.md` (recurring patterns) → `MINDSET.md` (distilled lessons).
- **Per-persona track** — how each specialist thinks and improves over time, captured in the persona's own `SIGNALS.md` → `MINDSET.md`.

The two tracks inform different things and stay separate. Patterns rise from observation (SIGNALS) to durable principle (MINDSET) only once they've earned it. Source-tag every SIGNALS entry: `[self]` for something you noticed, or `[persona-name]` for a specialist pattern you accepted.

The shipped personas start with empty MINDSET and SIGNALS files — fresh instances with no principles yet. They fill in as you use them.

---

## Adding Your Own Persona

Run `/vibeos-new-persona` to scaffold a new specialist. It creates the numbered folder, the four files, and a routing wrapper following the standard. Then fill in `PERSONA.md` with the role's lens and lane, and let its MINDSET and SIGNALS grow as you work.

When adding a persona, give it a clear lane that doesn't overlap the ones you already have. If two personas could both own the same decision, the boundary isn't clear yet — sharpen it before you ship.
