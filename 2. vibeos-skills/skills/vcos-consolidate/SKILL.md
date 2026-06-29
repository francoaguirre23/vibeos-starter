---
name: vcos-consolidate
description: Distill SIGNALS and MINDSET — merge near-duplicates, retire stale entries, and collapse redundancy, archiving everything removed so nothing is lost.
---

# VCOS Consolidate

> **Ownership:** Operator ritual — human-invoked, runs quarterly inside `/vcos-review`. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

Use this skill to keep the cognitive layer sharp instead of bloated. Append-only is correct for STANCE (it is a log). It is wrong for SIGNALS and MINDSET over time — they accumulate near-duplicates and stale entries until signal drowns in volume. Consolidation distills.

Core rule: **consolidation never deletes — it archives.** This respects the framework's "do not rewrite history" principle. Anything removed from an active file moves to an `_archive/` companion with a reason and date, so the trail is preserved and reversible.

## When to use

- On a quarterly cadence (see `MAINTENANCE_CADENCE.md`)
- When a SIGNALS file has grown past roughly 20-25 entries and is hard to scan
- When `/vcos-session-close` reports consolidation is due
- After a large promotion batch (like a multi-persona harvest) leaves redundancy behind

## Context Requirement

- The target SIGNALS.md and/or MINDSET.md files (project, persona, or global)
- The matching `## Calibration` data if present (Contested principles are retirement candidates)
- `WORKSPACE_HYGIENE_POLICY.md` for the archive-don't-delete discipline

## Inputs

- A target scope: one file, one persona/project, or "all" for a full pass
- Calibration data (to know which principles are Contested or unused)

## Process

1. **Find near-duplicates.** Within a file, identify entries that say the same thing in different words. Merge them into the single clearest statement, preserving the union of their evidence.

2. **Find stale entries.** Flag entries that are:
   - superseded by a later, better entry
   - `Contested` in calibration with no path to recovery
   - tied to a project or context that no longer exists
   - never applied (0 applications over multiple calibration cycles)

3. **Collapse redundancy across tiers.** If a SIGNALS entry has already been promoted to MINDSET, the SIGNALS version can be archived — its job is done.

4. **Propose the consolidation.** Present a before/after: what merges into what, what gets archived and why. Consolidation is propose-then-apply — do not silently rewrite. Get confirmation for anything that removes or merges an active entry.

5. **Apply and archive.** On confirmation:
   - Rewrite the active file with merged/retained entries
   - Move every removed entry to `_archive/<filename>_archive.md` in the same folder, with a one-line reason and the date
   - Keep MINDSET ≤100 lines as the standard requires

6. **Report** what was merged, retired, and archived, and the new entry count per file.

## Required output

- **Append merge/retirement proposals as Pending items in `global cognitive layer/review_queue.md`** — anything that removes or merges an active entry waits for confirmation there
- On confirmation: distilled SIGNALS/MINDSET files (clearer, shorter, no lost evidence)
- `_archive/` entries for everything removed, with reason + date
- A consolidation report: merges, retirements, archive location, new counts
- Updated `last consolidated` date in the maintenance ledger

## Checks before finalizing

- [ ] Nothing was deleted — everything removed is in `_archive/` with a reason
- [ ] Merged entries preserve the union of their evidence
- [ ] Active-entry removals/merges were confirmed before applying
- [ ] STANCE files were NOT consolidated (they are append-only history)
- [ ] MINDSET stays ≤100 lines
- [ ] Maintenance ledger updated with run date
