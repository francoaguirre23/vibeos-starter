# The Cognitive Layer, in plain words

The thing that makes a VibeOS team different from a fresh chat every time is its memory. Most AI tools forget everything the moment you close the window. VibeOS keeps a small, structured memory that grows as you work — so the team remembers what you decided, notices when something keeps coming up, and turns that into lasting know-how.

That memory is called the **cognitive layer**. It has three levels, and they build on each other.

## The three levels

Think of it as a funnel. Lots of small notes go in the top; a few durable principles come out the bottom.

**STANCE — the decision log.**
This is the running notebook. Every time the team makes a real choice ("we'll keep the trip to one weekend," "we decided not to include a contact form"), it gets jotted down here, one line at a time. STANCE is append-only: you add to it, you don't rewrite history. It is the raw material for everything above it.

**SIGNALS — the patterns.**
When the same kind of note shows up in STANCE more than once, it graduates to SIGNALS. This is where "we keep doing X" gets named. A signal isn't a one-off decision; it's a tendency the team has noticed about how this work actually goes.

**MINDSET — the durable principles.**
At the end of a project (or a big chunk of one), the strongest signals get distilled into MINDSET: short, durable rules of thumb the team will carry forward. This is the team's earned judgment. It's small on purpose — a handful of principles you'd actually want to keep.

```
  decisions you make        →   STANCE     (jot it down, one line each)
        ↓  when it recurs
  patterns the team notices  →   SIGNALS    (name the tendency)
        ↓  at a milestone
  judgment worth keeping     →   MINDSET    (a few durable principles)
```

## Three places it lives

The same three levels exist in a few scopes, each useful for a different reason:

- **Per project** — what you learned building this particular thing. Lives with the project.
- **Per teammate** — how a given persona tends to work (Robin's nose for what breaks, Sam's build habits). This is why your teammates feel like they have a point of view that sharpens over time.
- **Global** — the lessons that turned out to be true across several projects. These rise up only after a pattern has proven itself more than once, so the global layer stays trustworthy rather than cluttered.

## Why it compounds

Each project doesn't start from zero. It starts from everything the team already figured out. Decisions become patterns, patterns become principles, and principles quietly steer the next piece of work. The more you use it, the less you have to re-explain — and the better the team's instincts get. That's the whole point: judgment that accumulates instead of evaporating.

## If you do one thing, do this

You do not have to manage any of this by hand. There is one ritual that keeps it alive:

> **`/vcos-session-close`** — run it at the end of a work session.

That single command reads what just happened, captures the decisions into STANCE, and nudges patterns upward when they recur. It even works when your tool can't touch files — you can paste in what you did and it'll do the capture for you. If you adopt no other habit, adopt this one. The memory only compounds if something feeds it, and this is that something.

## The advanced stuff (later)

Once you have a few projects under your belt, a second set of rituals kicks in to keep the memory sharp instead of just big. You don't need these on Day 1 — they become useful once there's enough history to be worth tending:

- **`/vcos-review`** — a periodic check-in that surfaces anything needing your judgment.
- **`/vcos-calibrate`** — marks how confident the team is in each principle, based on whether it actually held up.
- **`/vcos-synthesize`** — spots lessons that recur across projects and proposes promoting them to the global layer.
- **`/vcos-consolidate`** — tidies up: merges near-duplicates and retires stale notes, archiving rather than deleting.

Ignore those until you feel the need. For now: work with your team, and close each session with `/vcos-session-close`. The rest takes care of itself.
