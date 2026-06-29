# Using VibeOS in your tool

VibeOS is plain Markdown, so it doesn't care much which assistant you use. The two building blocks are the same everywhere:

- **Personas** — your teammates. You call one with `@` and their handle: `@ada`, `@sam`, `@robin`.
- **Skills** — the repeatable commands. You call one with `/` and its name: `/vibeos-init`, `/vcos-session-close`, and so on.

Below is how that plays out in each tool, plus a path for when your tool can't read files at all.

## Works in your tool

| Tool | Talk to a teammate | Run a skill | Reads project files? |
|------|--------------------|-------------|----------------------|
| Claude Code | `@ada` | `/vcos-session-close` | Yes |
| Codex | `@ada` | `/vcos-session-close` | Yes |
| Cursor | `@ada` | `/vcos-session-close` | Yes |
| Plain chat (ChatGPT, Claude.ai, etc.) | paste a starter prompt | describe what you want | No — use the paste-in path below |

## Claude Code

This is the most turnkey path. When you ran `bash scripts/setup_machine.sh` during setup, it generated a `.claude/` folder that wires the personas and skills directly into Claude Code.

- Type `@ada` (or `@sam`, `@robin`) to bring in a teammate. They read their own definition first, so they show up in character.
- Type `/` to see the available skills, then pick one — `/vibeos-init` to get started, `/vcos-session-close` to wrap up.
- If you ever add or rename teammates, just re-run the setup script to regenerate `.claude/`.

## Codex

Same two moves: `@handle` for a teammate, `/skill` for a command. Codex reads the repo's files, so your teammates can see your project context and the cognitive layer the same way they do in Claude Code. Point it at the cloned folder and you're set.

## Cursor

Cursor also reads the repo directly. Use `@ada` to summon a teammate in the chat panel and `/skill-name` to run a skill. Because Cursor has your project open, teammates can read the project's context and memory files as they work.

## No file access? Paste a starter prompt

If you're in a plain chat window that can't open files — ChatGPT, Claude.ai, or any other — you can still use any teammate. Every persona ships with a self-contained **STARTER_PROMPT.md** that bundles their whole personality and approach into one block of text.

1. Open the persona's folder under `0. vibeos-global/personas/`.
2. Copy the contents of their `STARTER_PROMPT.md`.
3. Paste it as your first message in the chat. The assistant now behaves as that teammate.

In this mode the assistant can't write to your memory files, so when you finish, run the capture by hand: describe what you decided and ask it to summarize the decisions and lessons the way `/vcos-session-close` would, then paste that summary into your project's STANCE the next time you're in a file-aware tool.

## A note on the two name styles

You'll see two prefixes on skills: `/vibeos-*` (setup and team-building helpers like `/vibeos-init` and `/vibeos-new-persona`) and `/vcos-*` (the working rituals like `/vcos-spec` and `/vcos-session-close`). They behave identically — the prefix is just a hint about what family the skill belongs to.
