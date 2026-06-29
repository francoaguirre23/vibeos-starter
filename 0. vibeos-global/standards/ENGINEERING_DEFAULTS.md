# Engineering defaults (only if you build software)

Sensible defaults for when a VibeOS project produces code. If you're using VibeOS for
non-code work (planning, writing, decisions), you can skip this file entirely.

These are defaults, not rules. If you're working inside an existing codebase or team, follow
*their* conventions first — these only fill the gap when there's no established standard.

## The one principle

**Build the smallest thing that solves the problem, and make it hard to break.**

Everything below is a way of applying that.

## Build the smallest shape first

Most things don't need to be an app. Walk up this ladder and stop at the first rung that works:

1. A script
2. A command-line tool
3. A small web app or API
4. A multi-user service

Prefer read-only before write-heavy. Prefer manual-first before fully automated while you're
still building trust. Add persistence, accounts, and deployment only when the work actually
needs them — not because you might want them later.

## Before you add anything

Before reaching for a new library, service, or abstraction, ask in order:

1. Does this need to exist right now?
2. Does something already in the project cover it?
3. Does the language's standard library cover it?
4. Does a tool you already installed cover it?
5. Only then: build the smallest version that works.

Never strip out validation, basic security, or data-loss protection in the name of "smaller."

## Language and tools

There's no required stack. Pick what you (or your assistant) know well and what fits the job.
A common, friendly default is **Python** for scripts, automation, and small APIs — it's readable,
widely supported, and quick to iterate on. If you're already in a JavaScript/TypeScript world,
stay there. The right choice is the one you'll be able to maintain.

Whatever you pick: use an auto-formatter so you never argue about style, and lean on the
community-standard tooling for that language rather than inventing your own.

## Testing

If the code matters enough to keep, it's worth a little testing.

- Test the riskiest logic first.
- A few focused tests beat a giant suite you won't maintain.
- Don't rely only on "I clicked it and it worked" for code you'll depend on.

## Data and storage

- Identify the source of truth for any data.
- Prefer the simplest storage that works: no storage → local files → a small local database
  (like SQLite) → a shared database only when multiple people or processes truly need it.
- If you're handling anyone's personal or sensitive data, slow down and treat it carefully
  (see the "Keeping things private" standard).

## Security, in plain language

You don't need a formal security review for most small projects. You do need to keep a few
basics in mind:

- Never put passwords, keys, or tokens directly in your files — use a `.env` file (gitignored).
- Give a tool the least access it needs to do its job.
- Be cautious with anything that can delete or overwrite data — prefer previewing before doing.

## Delivery basics

When you ship something to others, include:

- A `README.md` — what it is, how to run it, who to ask.
- Clear run steps.
- The tests, if there are any.

That's enough for the vast majority of what you'll build. Heavier practices (formal architecture
reviews, CI coverage gates, reference architectures for authenticated multi-user apps) are real
and useful once you're working at team scale — treat them as an advanced layer you adopt when you
actually get there, not a Day-1 requirement.
