# Thread Hygiene

Short rules for keeping thread quality high when working VibeOS projects.

## Why it matters

A thread's quality degrades as its context grows: the model attends less reliably to buried facts (context rot), long chats get auto-compacted into lossy summaries, and every turn re-bills the accumulated context. The VibeOS cognitive layer (`project_context.md` + STANCE/SIGNALS/MINDSET) is externalized memory — it exists so threads can stay short and disposable. A long-running thread skips that advantage and is lower-fidelity than the files it should be reading.

## The loop

1. **One thread per work session or distinct sub-task** — not one thread per project for its whole life.
2. **Open with `/vcos-session-start`** — rehydrate the project's durable state into a compact orientation instead of scrolling old history.
3. **Close with `/vcos-session-close`** — capture decisions/patterns back to STANCE/SIGNALS while the context is still coherent.
4. **Start fresh** — new thread, rehydrate again.

## When to cut a thread

- At a natural task boundary, or
- After the first auto-compaction, whichever comes first.

Do not wait for the hard context cap. Your most important work then happens in the most-degraded, most-expensive window, and `/vcos-session-close` ends up summarizing an already-summarized context.

## A thread is not a new project

A fresh thread on existing work is a **new session on the same project**, not a new project. Do not scaffold a new `projects/<name>/` folder per thread — that fragments the project's `project_context` and cognitive layer, which is the whole thing thread hygiene is trying to preserve.

Sub-work on an existing project (analysis, planning, a single feature) → open a thread on that project and run `/vcos-session-start "<project>"`. Capture back to its STANCE/SIGNALS. No new folder.

## Archiving

Keeping old threads pinned or foldered in your client is fine — idle threads cost nothing and don't affect a new thread's quality. The rule is just: read from the cognitive layer, not the old thread.
