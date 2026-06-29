# VibeOS Persona Standard

Canonical structure and conventions for VibeOS personas.

This document defines what a persona is, what files it must contain, how it is named, and how it is wired into the tools that use it. Use it when adding a new persona or auditing existing ones.

Complements:
- `personas/README.md` — the persona system overview and cognitive layer architecture
- `CLAUDE_CODE_INTEGRATION.md` — how personas become `@agents` in Claude Code

## What a Persona Is

A persona is a named specialist archetype with a distinct lens, operating boundary, and accumulated craft knowledge. Personas can be invoked at any point in a build — they are not phase-gated.

Personas are **shared and never copied** into projects. They live in `0. vibeos-global/personas/` and are referenced by absolute path.

## Folder Naming

Each persona lives in a numbered folder:
```
[number]. [Name] ([Role])/
```

Examples: `0. Ada (Chief of Staff)`, `1. Sam (Tech Lead)`, `2. Robin (Reviewer)`

Rules:
- The number is a stable ID — do not renumber existing personas when adding new ones
- New personas take the next available number
- The human-readable name and role in parentheses must match the persona's identity in `PERSONA.md`

## Required Files

Every persona folder must contain exactly these four files:

| File | Purpose | Source of truth? |
|------|---------|-----------------|
| `PERSONA.md` | Full role definition: role, lens, when to invoke, what you produce, handoffs, MECE boundary, what you never do, output style, context to read | Yes — authoritative role definition |
| `MINDSET.md` | Durable specialist principles and heuristics, accumulated across projects. Updated only via SIGNALS promotion. ≤100 lines. | Yes — authoritative principles |
| `SIGNALS.md` | Emerging role-specific patterns worth watching or promoting. Each entry source-tagged. | Yes — staging layer |
| `STARTER_PROMPT.md` | Portable, self-contained bootstrap prompt for tools that cannot read files (ChatGPT, Claude.ai, or any chat-only tool). Embeds a MINDSET snapshot. | No — portable interface, not authoritative |

## PERSONA.md Required Sections

- **Role** — who the persona is and what they own
- **Lens** — the questions they ask when they look at a problem
- **When to invoke** — concrete triggers
- **What you produce** — outputs
- **Handoffs** — who they defer to and when
- **MECE Boundary** — what they own vs. adjacent personas (prevents lane overlap)
- **What you never do** — hard boundaries
- **Output style** — format and tone
- **Context to read before starting** — onboarding files

## MINDSET.md Rules

- Stable principles only — update exclusively via SIGNALS promotion, never direct edits mid-work
- Keep ≤100 lines
- Organize into thematic sections (Decision Heuristics, Risk Profile, Anti-Patterns, etc.)
- A promoted principle should be backed by evidence in SIGNALS before it lands here

## SIGNALS.md Rules

- Staging layer between observation and durable principle
- Promote to MINDSET when: Confidence = High, Scope = Clearly general, Evidence spans ≥2 projects
- Every entry includes: Pattern, Type (Heuristic / Preference / Risk Pattern / Anti-Pattern), Source (`[self]` or `[persona-name]`), Evidence, Confidence, Scope
- Flag promotion-ready entries with `→ Eligible for MINDSET promotion`

## STARTER_PROMPT.md Rules

- Fully self-contained — no file references, no dependencies
- Embeds: role summary, how-you-think, what-you-produce, what-you-never-do, output style, and a dated MINDSET snapshot
- Header carries a `Last updated` date comment
- **Must be refreshed when MINDSET.md changes** — this is a step in `/vcos-memory`
- Treated as the portable interface, not a replacement for the full file set

## Adding a New Persona — Checklist

- [ ] Create `[next-number]. [Name] ([Role])/` folder
- [ ] Write `PERSONA.md` with all required sections
- [ ] Write `MINDSET.md` (may start with seed principles)
- [ ] Write `SIGNALS.md` (may start empty with the standard header)
- [ ] Write `STARTER_PROMPT.md` with a dated MINDSET snapshot
- [ ] Add a thin agent wrapper at `.claude/agents/[name].md` (see CLAUDE_CODE_INTEGRATION.md)
- [ ] Add the persona to `personas/README.md` quick reference and invocation order
- [ ] Add the persona to the persona tables in `OS_INDEX.md` and workspace `CLAUDE.md`
- [ ] Log the addition in `PERSONA_AND_INSTRUCTION_AUDIT.md`

## MECE Discipline

Personas must have non-overlapping ownership. When adding a persona, explicitly define its MECE boundary against the personas whose lanes are closest. If two personas could both own a decision, the boundary is not yet clear — resolve it before shipping the persona.
