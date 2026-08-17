# Start VibeOS in Claude Code

First, orientation, because there are two different places you'll type things:

1. **Your computer's terminal**: a plain window for typing commands to your computer (on Mac it's the "Terminal" app). You only need it briefly, to get the files, and you can skip it entirely if you download the ZIP.
2. **Claude**: the chat inside Claude Code. This is where you do everything else. You can even ask Claude to run the setup command for you, so you barely touch the terminal.

## Step 1: Get the kit onto your computer

Pick one:

- **No terminal (easiest):** open the repository's page on GitHub (the link you were given), click the green "Code" button, choose "Download ZIP", and unzip it (double-click). You now have a folder named `vibeos-starter`, probably in your Downloads. Move it wherever you keep projects.
- **If you're comfortable in a terminal:** open the Terminal app and run this (it goes in the terminal, not to Claude), using the repository link you were given:
  ```
  git clone https://github.com/OWNER/vibeos-starter.git
  ```
  Replace `OWNER` with the account that hosts the link you were given. "git" is just the standard tool for downloading code folders like this one. It creates the `vibeos-starter` folder wherever your terminal currently is.

Either way, the goal is the same: a folder called `vibeos-starter` sitting on your computer.

## Step 2: Open that folder in Claude Code

"The folder" is the `vibeos-starter` folder from step 1. Open it in Claude Code the same way you normally start Claude Code on a project:

- If you launch Claude Code from a terminal with the `claude` command, first move into the folder, then start it:
  ```
  cd ~/Downloads/vibeos-starter
  claude
  ```
  (`cd` means "change directory", so this moves into the folder, then `claude` starts Claude Code there. Adjust the path if the folder is somewhere other than Downloads.)
- If you use the Claude Code app or the editor extension, just open the `vibeos-starter` folder as your project.

The moment it opens, you are talking to Claude. Everything below is a chat message to Claude, not a terminal command.

## Step 3: Paste this as your first message to Claude

```
You're in the VibeOS starter kit. Read CLAUDE.md and README.md so you understand it.
Then set me up: run `bash scripts/setup_machine.sh`, then read and execute
"2. vibeos-skills/skills/vibeos-init/SKILL.md" to run the first-run wizard, and walk me
through creating my first project. Explain what you're doing and keep it hands-on.
```

You do not run those commands yourself anywhere. Claude runs them for you, asks you a few questions, and starts your first project.

## Step 4: Restart Claude Code once

Setup created a hidden `.claude/` folder that registers the `@teammates` and `/skills` menus. Those appear on a fresh session, not mid-session. So after the wizard finishes, quit Claude Code and reopen the same folder. Now `@ada`, `@sam`, `@robin`, and the `/` commands all show up. Before that restart you don't need them, just talk to Claude in plain words.

## Using it, and the one habit

- Start anything by talking to `@ada` (she frames what you want and hands it to `@sam` to build or `@robin` to review).
- End each working session with `/vcos-session-close`. That single habit is what makes the team's memory build up instead of resetting.

## If something snags

Copy the whole error, paste it into the Claude chat, and ask Claude to fix it. Almost always it's a missing tool or being in the wrong folder, and Claude can sort it out.

## Want the full picture?

- `README.md` — what VibeOS is and the first 15 minutes.
- `TUTORIAL.md` — a guided Day 1.
- `COGNITIVE_LAYER_101.md` — how the team's memory works and why it compounds.
- `TOOL_GUIDE.md` — using it in Codex, Cursor, or a plain chat window instead of Claude Code.
