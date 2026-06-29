---
name: vcos-review
description: The biweekly review routine — run the due maintenance, collect everything needing human judgment into the review queue, and present it for decisions.
---

# VCOS Review

> **Ownership:** Operator ritual — human-invoked, never auto-run by a persona · biweekly cadence. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

The one ritual to remember. Runs every two weeks. It does the maintenance labor, gathers everything that needs your judgment into a single queue, and walks you through the decisions — so nothing waits silently in a proposal block or a Contested flag you forget to check.

This is the human-facing front end of the compounding layer. The mechanisms (`/vcos-calibrate`, `/vcos-synthesize`, `/vcos-consolidate`) generate the work; this routine surfaces the judgment calls.

## When to use

- Biweekly (the default cadence — see `MAINTENANCE_CADENCE.md`)
- When `/vcos-session-close` reports the review is due
- Any time the review queue has accumulated and you want to clear it

## Context Requirement

- `0. vibeos-global/global cognitive layer/review_queue.md` — the inbox
- `0. vibeos-global/global cognitive layer/maintenance_ledger.md` — cadence state
- `0. vibeos-global/standards/MAINTENANCE_CADENCE.md` — run order and gates

## Process

### Step 0 — Confidentiality check (gate)
Run `0. vibeos-global/scripts/check_confidentiality.sh`. It verifies every project is classified in the INDEX registry (fail-closed: unclassified = treated as NDA) and that no NDA codename appears in the shared layer. If it reports ACTION NEEDED, add each flagged item to the review queue and do NOT let synthesis read an unclassified project as if it were Internal. See `standards/CONFIDENTIALITY.md`.

### Step 1 — Run the due maintenance
Check the ledger. Run whatever is due, in order:
- **Always (biweekly):** `/vcos-calibrate scope:all` then `/vcos-synthesize`
- **If quarter-due:** `/vcos-consolidate scope:all` (propose mode)

Each mechanism respects the confidentiality gate (excludes Confidential/NDA/unclassified projects) and appends any human-judgment items to `review_queue.md` rather than burying them in its own output. (Direct, non-judgment work — calibration tier updates, GLOBAL_SIGNALS staging — is applied automatically.)

### Step 2 — Compile the queue
Read `review_queue.md`. Confirm every Pending item has: what it is, why it's there, the decision needed, a recommendation, and its source. Add anything the maintenance run surfaced that isn't there yet.

### Step 3 — Present for decision
Walk the user through each Pending item, one at a time, newest/highest-impact first. For each: state the decision needed and your recommendation, and get a call. Batch trivial/informational items ("no decision needed") into a single acknowledgement.

### Step 4 — Apply decisions
For each resolved item, do the work the decision implies:
- Adopt a proposal → fold into GLOBAL_MINDSET (and mark GLOBAL_SIGNALS adopted)
- Confirm a consolidation → apply the merge, archive the removed entries
- Rewrite/retire a Contested principle → edit the persona MINDSET
- Then move the item to the Resolved section of the queue with the decision + date.

### Step 5 — Update state
- Update `maintenance_ledger.md` run rows and dates.
- Leave genuinely-not-yet-actionable items (e.g. "watching for a 2nd project") in Pending with a note.

## Required output

- Maintenance run completed (calibrate + synthesize, consolidate if due)
- Every Pending queue item either resolved-and-applied or explicitly carried forward with a reason
- Updated review_queue (Resolved section grows; Pending shrinks to only genuinely-waiting items)
- Updated maintenance ledger

## Checks before finalizing

- [ ] Due maintenance ran in the correct order (calibrate → synthesize → consolidate)
- [ ] Every judgment item was presented, not silently applied
- [ ] Applied decisions actually landed in the target files
- [ ] Resolved items moved to Resolved with decision + date
- [ ] Nothing destructive happened without an explicit decision
- [ ] Ledger updated

## Note on automation

This routine is designed to be scheduled. Use `/schedule` to run it biweekly: it will run the maintenance and prepare the queue, then present the decisions next time you're in a session (the judgment gates stay human). If not scheduled, `/vcos-session-close` reminds you when it's due — but scheduling is what removes the "I'll forget" problem.
