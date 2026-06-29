# VibeOS Maintenance Cadence

How the cognitive layer maintains and compounds itself over time.

The capture mechanisms (STANCE → SIGNALS → MINDSET) record what is learned. The maintenance mechanisms make that learning *compound, calibrate, and stay sharp* instead of just accumulating. This standard defines the cadence, the run order, and how it runs as automatically as possible.

## The One Ritual: Biweekly Review

There is one thing to remember: **`/vcos-review`, every two weeks.** It is the human-facing front end of the whole maintenance layer. It runs the due mechanisms, gathers everything that needs your judgment into a single queue, and walks you through the decisions. Everything else is plumbing behind it.

This design exists because scattered "needs your review" items (proposals in one file, Contested flags in another, consolidation candidates in a third) get forgotten. One routine, one inbox, one cadence.

## The Mechanisms (run by the review)

| Skill | Mechanism | What it does | When it runs |
|-------|-----------|-------------|--------------|
| `/vcos-calibrate` | **Confidence** | Updates each principle's confidence tier from applied/reversed evidence in STANCE | Biweekly (inside `/vcos-review`) |
| `/vcos-synthesize` | **Compounding** | Finds patterns recurring across project + persona MINDSETs and proposes them to the global layer | Biweekly (inside `/vcos-review`) |
| `/vcos-consolidate` | **Distillation** | Merges near-duplicates, retires stale entries, archives everything removed | Quarterly (inside `/vcos-review` when quarter-due) |

These build on the per-session capture layer (`/vcos-memory`, `/vcos-session-close`) which runs every session.

## Run Order

When the review runs more than one mechanism, this order — each feeds the next:

```
1. /vcos-calibrate    → know which principles are load-bearing vs Contested
2. /vcos-synthesize   → bubble up the calibrated, proven principles to GLOBAL
3. /vcos-consolidate  → prune duplicates and retire Contested/unused (quarterly)
```

Calibrate first so synthesis promotes proven principles and consolidation knows what to retire.

## The Review Queue (the inbox)

`0. vibeos-global/global cognitive layer/review_queue.md` is the single inbox for everything awaiting human judgment. Each mechanism **appends its judgment items here** rather than burying them in its own output. Non-judgment work (calibration tier updates, GLOBAL_SIGNALS staging) is applied automatically; only the decisions land in the queue.

`/vcos-review` presents the Pending items, you decide, and resolved items move to the Resolved section with the decision and date. The queue is the durable memory of "what was decided and when."

## The Maintenance Ledger (cadence state)

`0. vibeos-global/global cognitive layer/maintenance_ledger.md` records last-run dates and what each run produced. It answers "is the review due?" Any tool can read it. `/vcos-session-close` reads it to remind you.

## Automation: Pull + Push

### Pull (default — no infrastructure)
`/vcos-session-close` ends every session by checking the ledger and reporting whether the biweekly review is due. You run `/vcos-review` when prompted. Works in any file-capable tool, no daemon. Degrades gracefully — skip one and the next session still flags it.

### Push (recommended — removes the "I'll forget" problem)
Schedule the review so it runs itself. Use `/schedule` (requires the remote account connection):

- **Biweekly — "VibeOS review"**
  Prompt: *"Open the VibeOS workspace and run /vcos-review. Run the due maintenance (calibrate + synthesize; consolidate if quarter-due), apply all non-judgment updates directly, and append everything needing my decision to review_queue.md. Then present the Pending queue items to me with a recommendation for each. Do not apply anything destructive or anything entering GLOBAL_MINDSET without my confirmation. Update the maintenance ledger."*
  Cadence: every two weeks.

The routine does the labor on schedule; the judgment gates still wait for you. This is the difference between "I have to remember to maintain it" and "it maintains itself and asks me when it needs a call."

## Human Judgment Gates (never automated away)

Even at full push automation, these wait for a human decision in the review:
- Promotion into `GLOBAL_MINDSET.md` — always a proposal
- Retirement or merge of an active SIGNALS/MINDSET entry — confirm before apply
- Rewriting or retiring a `Contested` principle — human decides

Automation moves the labor, not the judgment.

## Cadence Summary

| Cadence | What runs |
|---------|-----------|
| Every session | `/vcos-memory`, `/vcos-session-close` (the latter flags if review is due) |
| **Biweekly** | **`/vcos-review`** → calibrate → synthesize → present the queue |
| Quarterly | `/vcos-consolidate` runs inside the review when quarter-due |
| On skill/persona change | Update OS_INDEX + CLAUDE.md |
