# VibeOS

VibeOS is a starter kit for running a small team made of AI teammates. You get named specialists you can talk to, a shared memory that gets smarter as you work, and a handful of simple commands — all plain Markdown, so it works with whatever coding assistant you already use (Claude Code, Codex, Cursor).

Clone it, run one setup command, and you have a working team in a few minutes.

## The first 15 minutes

By the end of your first sitting you will have: talked to your Chief of Staff, framed a real task, watched a teammate do the work, and seen the team's memory fill up on its own. Nothing to configure beyond the setup step. If you only read one thing after this, read **[TUTORIAL.md](TUTORIAL.md)** — it walks you through that exact 15 minutes.

## Setup (3 steps)

1. **Clone** this repo.
2. **Run** `bash scripts/setup_machine.sh` — this stamps your machine's path into the routing layer and generates the `.claude/` folder your tool reads.
3. **Run** `/vibeos-init` in your assistant — a short first-run wizard that gets you oriented and ready to go.

That's it. You're ready to work.

New to repos, or setting this up straight from Claude Code? See **[START_IN_CLAUDE_CODE.md](START_IN_CLAUDE_CODE.md)** for the click-by-click version.

## Your starter team

Three teammates ship with the kit. You always start with Ada.

| Teammate | Role | Talk to them when |
|----------|------|-------------------|
| `@ada` | Chief of Staff — the orchestrator | You have a fuzzy idea and don't know where to start. Ada frames it and routes it. |
| `@sam` | Tech Lead — the maker | Something needs to get built or drafted, with a light sanity check along the way. |
| `@robin` | Reviewer — the second pair of eyes | You want to know what might break or what's missing before you ship. |

Want more teammates later? Run `/vibeos-new-persona` to add one.

## Where your work lives

Your actual projects live under `projects/`. That folder is local to your machine and is never synced through this kit, so your work stays yours. Create a new project with `/new-vibeos-project`.

## The one habit that makes it compound

As you work, the team keeps a memory: decisions, recurring patterns, and durable lessons. The thing that fills it is a single end-of-session ritual: **`/vcos-session-close`**. Do that one thing and the team gets sharper every time. The friendly primer is **[COGNITIVE_LAYER_101.md](COGNITIVE_LAYER_101.md)**.

## Where to go next

- **[TUTORIAL.md](TUTORIAL.md)** — your guided Day 1 (the written version of `/vibeos-tutorial`).
- **[COGNITIVE_LAYER_101.md](COGNITIVE_LAYER_101.md)** — how the team's memory works and why it compounds.
- **[TOOL_GUIDE.md](TOOL_GUIDE.md)** — using VibeOS in Claude Code, Codex, Cursor, or even a plain chat window.
- **[CLAUDE.md](CLAUDE.md)** — the full workspace guide.
- **[examples/sample-project/](examples/sample-project/)** — a tiny finished project so you can see what "done" looks like.
