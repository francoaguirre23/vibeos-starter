---
name: vcos-meeting-context
description: Load meeting notes/transcript from any notetaker into the session as correctly-framed context. Calibrates speaker attribution to what the source actually supports (e.g. Granola = no external attribution; Fathom/Zoom = trust named speakers), separates reliable signal from unreliable, and treats AI summaries as fallible inferences. Optional capture to STANCE. Produces no artifact by default.
---

# VCOS Meeting Context

> **Ownership:** Operator ritual — human-invoked when you bring meeting notes or a transcript into a session as context. Auto-detect (non-blocking): if pasted content looks like a notetaker export, offer to run this before reasoning over it. The load is automatic once invoked; any STANCE capture is confirm-first. See `0. vibeos-global/SKILLS_CHEATSHEET.md`.

The point of this skill is not to produce a document. It is to make meeting notes become trustworthy context for the rest of the session, framed so nobody (you or the assistant) misuses them. The one thing that varies by source is how much you can trust "who said what," so this skill picks a **source profile** up front and sets the attribution rule to match. Everything else (provenance, reliable-vs-unreliable split, absorbing the notes, optional capture) is the same for every source. This means you never hand-type the caveat again, and you never over-trust or under-trust a source by accident.

## When to use

- You are pasting or linking meeting notes into a session as background: a notetaker export (summary, action items, transcript), or human/manual notes.
- You want the notes treated as context without spending the session re-explaining their limits.
- Any source where speaker attribution reliability is worth pinning down before you reason over it.

## Auto-detect trigger (non-blocking)

If pasted content looks like a meeting export (a summary / action-items block, or a running transcript), offer to run this skill first. Never block: if the person says use it as-is, proceed but still declare the source profile and honor its attribution rule.

## Context Requirement

- The notes themselves: summary, action items, and/or transcript, pasted inline or in an accessible doc. Partial input is fine; note what is missing.
- If a doc link is given and your tool can open it, read it; otherwise ask for the text to be pasted.
- If working inside a project: `docs/project_context.md` and `project cognitive layer/STANCE.md` (only if the optional capture in step 6 is taken).

## Inputs

- Raw meeting content (summary, action items, transcript, or notes — any subset).
- The source tool if known (Granola, Fathom, Zoom, Gong, Otter, Fireflies, human notes, etc.).
- Optional metadata you provide: meeting name, date, your-side attendees, purpose.

## Process

1. **Identify the parts and the source.** Locate the summary, action items, and transcript within the input, and determine which tool produced it. Note any part that is absent. If the source is not stated, infer it from the format; if still unclear, ask one question (see the profiles below).

2. **Pick the source profile — this sets the attribution rule.** Match the source to one profile and state which one is in force:

   | Profile | Typical sources | Attribution rule for the session |
   |---------|-----------------|----------------------------------|
   | **No external diarization** | Granola (single external channel) | Strict. The external side is always "external participant(s)" / "them." Never attribute a statement to a named individual on the external side, even when implied. Your/host side may be "us" (first person only where unambiguous). |
   | **Named diarization** | Fathom, Zoom, Gong, Fireflies, Otter with named speakers | Attribute to the labeled speaker — that is reliable. Do not infer beyond the labels. Still treat the transcript as fallible (transcription errors, crosstalk). |
   | **Unnamed diarization** | "Speaker 1 / 2 / 3" labels, no names | Attribute to the distinct speaker label. Do not map a label to a real person without your confirmation. |
   | **Human / manual notes** | notes a person typed, a written recap | Carry attributions as the note-taker's secondhand claim, not verbatim. Reliability is tied to the writer. |
   | **Unknown** | format not recognized | Ask once: "does this source label individual speakers, and by name?" Default to the strictest matching profile until answered. |

3. **Fix provenance and install the rule.** Record for the session: the source tool, its profile, and the attribution rule above. Any claim that exceeds what the profile supports (e.g. naming an external speaker under Granola) is unsupported by this source — say so plainly rather than inferring.

4. **Separate reliable from unreliable signal.**
   - **Always fallible (label as inference):** the AI-generated summary and action items. They are a model's reading of the call, useful but not ground truth — flag where they may over-reach.
   - **Reliable:** what the transcript records was discussed, decisions stated plainly, commitments made by your side, topics and questions covered. Under a named-diarization profile, who said what is also reliable.
   - **Unreliable for this source:** anything the profile can't support — under Granola, which external individual said or wanted anything, the number of distinct external speakers, and any specific external person's tone or intent.

5. **Absorb, then confirm briefly.** Hold the full notes as live context for the rest of the session. Do **not** paste them back or rewrite them. Give a short confirmation only — roughly 4 to 7 lines: meeting label and date if known, the source and its profile (one line), your side vs the other side, the handful of reliable points that matter (key decisions, action items, open questions), and one line stating the attribution rule now in force. Then stop and let the person continue.

6. **Optional capture (confirm first).** If a project is active and any decisions, action items, or open questions belong in its record, offer to append them to `project cognitive layer/STANCE.md`, each tagged with the source and profile (e.g. `[meeting: <name/date>, Granola — external attribution unverifiable]`, or `[meeting: <name/date>, Fathom — speakers named]`). Only write on an explicit yes. If any of it is private or sensitive, keep it in the project and don't copy it into shared indexes.

## Required output

No artifact by default. The deliverable is state, not a document:

- The notes are loaded as session context.
- A short (4–7 line) load confirmation, naming the source, its profile, and the attribution rule in force.
- A standing rule for the rest of the session: honor the profile's attribution rule, treat the AI summary/action items as fallible inferences, and flag any claim that exceeds what the source supports.

Only produce a written pack, cleaned transcript, or extraction if the person asks for one.

## Checks before finalizing

- The source profile was declared, and the attribution handling matches it (e.g. under Granola, no external individual is named anywhere; under named diarization, speakers are attributed to their labels and not beyond).
- Provenance is stated: which tool, and its diarization profile.
- The AI summary and action items are flagged as fallible inferences, not ground truth.
- The reliable vs unreliable split is explicit, not implied.
- Nothing is invented beyond what the notes actually contain.
- The full transcript was not dumped back at the person; the confirmation stayed short.
- If capture to STANCE happened, every entry carries the source+profile tag, and it was done only on explicit confirmation.
