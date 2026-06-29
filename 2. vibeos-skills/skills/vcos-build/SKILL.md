---
name: vcos-build
description: Turn a Build Packet and design into a small implementation plan and code changes.
---

# VCOS Build Skill

> **Ownership:** Sam (Tech Lead) · **Mode:** auto-run (domain skill). See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill when you are ready to implement the MVP in small steps.

## Quick sanity check
Before you start, take a beat — this is a prompt to think, not a stop sign:
- Is the spec clear enough to build from? If big questions are still open, it's usually worth nailing them down first.
- Any obvious risk or anything sensitive in play (real personal data, credentials, anything you'd hate to leak)? If so, keep that in mind as you go.

If something feels shaky, it's fine to loop back and tighten the spec before building. Otherwise, go.

## Context Requirement
Before performing this workflow:
- Read PROJECT_CONTEXT.md
- Confirm current phase and constraints

## Inputs
- Build Packet
- Optional architecture note
- Existing repo structure
- One narrow change at a time

## Process
1. Restate the MVP and the exact step to implement.
2. Break work into small, ordered tasks.
3. Touch only the files needed for the current step.
4. Add or update tests for any changed logic.
5. Keep logging and error handling explicit for external calls.

## Required output
- Quick Summary
- Implementation Plan
- Files & Modules
- Test & Verification Plan

## Checks before finalizing
- Change is narrow and reviewable.
- Tests cover the main behavior.
- No new secrets or broad permissions are introduced.
- The repo stays aligned with the current Build Packet.
