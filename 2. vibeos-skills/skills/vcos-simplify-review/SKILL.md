---
name: vcos-simplify-review
description: Review a diff, file, or project slice for unnecessary complexity, reuse opportunities, and over-engineering — and produce a plain delete / shrink / reuse list. Use when the question is "is this heavier than it needs to be?"
---

# VCOS Simplify Review

> **Ownership:** Robin (Reviewer lane) — advanced/optional, not a Day-1 skill. **Mode:** analysis only; Robin flags what could be cut and never edits without asking. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this when the question is not "is it correct?" but "is it heavier than it needs to be?" It is a focused complexity review: what can be deleted, shrunk, or replaced with something that already exists. It sits alongside a normal review — it does not replace one.

## When to use

- A change feels overbuilt: too abstract, too many moving parts, too many new dependencies.
- A project needs a "what can we delete?" pass.
- A plan, draft, file, or slice of a repo may be doing more than the current need justifies.
- Before adding a new dependency, framework, abstraction, or layer — check whether it's needed at all.

## Context Requirement

Before starting, read:
- The request and the exact thing being reviewed — the diff, file, folder, or artifact.
- For code: the callers and the surrounding patterns, before suggesting any cut. A change in the wrong place is still a change.
- If working inside a project: the relevant plan or brief, so a "simplification" doesn't quietly erase something that was actually asked for.
- Keep correctness, security, data-loss prevention, and accessibility out of scope for deletion — those are protected (see below).

## The minimum viable change ladder

Before recommending new code or new complexity, stop at the first rung that holds:

1. Does this need to exist at all for the current goal?
2. Does the project already have a helper, component, pattern, or artifact that covers it?
3. Does the language's standard library cover it?
4. Does the platform or browser already provide it?
5. Does something already installed cover it?
6. Can the same result come from a small local change instead?
7. Only then: keep or build the smallest version that works.

## Inputs

- **Target:** the diff, file, folder, artifact, or repo slice under review.
- **Scope:** over-engineering only, unless you ask for a broader look.
- **Optional:** anything that must not change — an API contract, a data shape, a design direction, a commitment already made.

## Process

1. **Bound the review.** Name the target and say what is out of scope.
2. **Trace before cutting.** For code, follow the callers and the real flow. For docs, find the source of truth and the current decision.
3. **Walk the ladder.** Prefer deleting, reusing, or leaning on the standard library / platform / installed tools before adding new code.
4. **Protect safety.** Do not propose removing input validation, error handling that prevents data loss, security controls, accessibility basics, tests that guard real logic, or anything explicitly required. If something looks heavy but protects one of these, call it out as protected — don't cut it.
5. **Produce the list.** For each finding, one line: what to cut or replace, where, and what replaces it. Rank by impact.
6. **Mark deliberate shortcuts.** If a simplification has a known ceiling (it works now but won't scale later), name the ceiling and the trigger that would mean it's time to upgrade.

## Required output

- **Scope:** one line naming what was reviewed and what was out of scope.
- **Findings:** one line each — what to cut/shrink/reuse, where, and the replacement. Tag each as `delete`, `shrink`, or `reuse`.
- **Protected:** anything that looks heavy but should stay because it guards correctness, security, data, accessibility, or an explicit requirement.
- **Net effect:** a rough count of files, dependencies, or sections that could be removed or avoided.
- **Recommendation:** apply now, backlog, or leave as-is.

If nothing meaningful can be simplified, say so plainly: it's already lean, ship it.

## Checks before finalizing

- [ ] The review never treated correctness, security, accessibility, or data-loss protection as removable complexity.
- [ ] Each finding names a concrete replacement, or says plainly that nothing replaces it.
- [ ] Every suggestion is grounded in something actually inspected, not assumed.
- [ ] Any deliberate shortcut has a named ceiling and an upgrade trigger.
- [ ] The output is a review, not an edit — nothing was changed without being asked.
