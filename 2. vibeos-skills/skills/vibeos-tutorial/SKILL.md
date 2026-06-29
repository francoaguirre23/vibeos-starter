---
name: vibeos-tutorial
description: A guided Day-1 walkthrough the assistant runs live — make a few small decisions, watch them land in the cognitive layer, and feel the compounding loop once.
---

# VibeOS Tutorial

> **Ownership:** Operator ritual (human-invoked) · **Mode:** confirm. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

This is a hands-on first lap, run live with the user. The goal is to make the compounding loop tangible exactly once: you make a couple of small decisions, you watch them get captured, and you see the system get a little smarter. Keep it to about 10–15 minutes and keep the tone encouraging. It's a throwaway exercise — nothing here has to be useful work.

## When to use

- Right after first-run setup, when someone wants to actually feel how VibeOS works.
- Any time someone says "show me what this thing does."

## Context Requirement

Before starting, skim:
- `0. vibeos-global/SOUL.md` — so the walkthrough echoes the right voice.
- The shipped Ada persona under `0. vibeos-global/personas/` — Ada is the orchestrator you'll talk to in the demo.

## Inputs

- A few minutes of the user's attention and a willingness to make small, low-stakes decisions.

## Process

### Step 1 — Set expectations (30 seconds)

Tell them: "We're going to build a tiny throwaway project, make two or three small decisions, and then watch those decisions get captured so the system remembers them next time. About ten minutes. Nothing here is real work."

### Step 2 — Create a tiny throwaway project

Scaffold a small practice project:
```sh
bash "0. vibeos-global/scripts/bootstrap_vibeos_project.sh" "Tutorial Sandbox" engops
```
Show them the folder that appears under `projects/` and point out the project cognitive layer (STANCE, SIGNALS, MINDSET) — explain in one line that this is where the project's memory lives.

### Step 3 — Talk to Ada

Invoke the orchestrator persona (Ada) and pose a small, made-up question — something like "help me decide what to name a weekend side project." Let Ada frame it and offer a couple of options. This shows how a persona thinks, not just answers.

### Step 4 — Make 2–3 small decisions

Walk them through a few tiny calls (pick an option, set a constraint, choose a next step). Keep each one quick. Narrate lightly: "That's a decision — watch where it goes."

### Step 5 — Show the decisions landing in STANCE

Open the project's `STANCE.md` and show the decisions written there. Make the point plainly: the system just remembered what you decided, so you won't have to re-explain it next session.

### Step 6 — Run the session-close ritual and show the layer fill

Run `/vcos-session-close`. Then open the cognitive layer and SHOW what changed — point at the entries that got captured and explain, in one or two sentences, how patterns promote upward over time (STANCE → SIGNALS → MINDSET) so the system compounds. This is the payoff moment; let it land.

### Step 7 — Wrap up

Congratulate them. Tell them they can delete the Tutorial Sandbox project whenever they like. Point them at one real next step — usually starting a real project or talking to a persona about actual work.

## Required output

- A throwaway `projects/Tutorial Sandbox/` project.
- A short live conversation with Ada and 2–3 captured decisions.
- Visible entries in the project's STANCE and, after session-close, in the cognitive layer.
- A friendly wrap-up naming one real next step.

## Checks before finalizing

- The whole thing stayed light and ran in roughly 10–15 minutes.
- The user actually saw a decision land in STANCE.
- The user saw the cognitive layer change after `/vcos-session-close`.
- It was clear the sandbox is disposable.
- The walkthrough ended with one concrete next step.
