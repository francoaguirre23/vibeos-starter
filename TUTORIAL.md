# Day 1 with VibeOS

This is the written companion to the `/vibeos-tutorial` skill. Either one walks you through the same first session. By the end you'll have framed a real task, watched a teammate do it, gotten a second opinion, and — the payoff — seen the team's memory fill up on its own.

It takes about 15 minutes. We'll use a made-up example so you can follow along without any real project: **planning a weekend trip**.

## Before you start

Make sure you've done the three setup steps from the README: cloned the repo, run `bash scripts/setup_machine.sh`, and run `/vibeos-init`. If `/vibeos-init` finished, you're ready.

## Step 1 — Meet Ada and frame the task

Always start with Ada, your Chief of Staff. She takes a fuzzy idea and turns it into something the team can actually act on.

Type:

```
@ada I want to plan a weekend trip but I haven't thought it through. Help me figure out what I'm actually deciding.
```

Ada won't run off and book flights. She'll ask the kind of questions that sharpen a vague wish into a clear task — who's going, what "a good weekend" means to you, what the budget and the must-dos are, and what the smallest useful first version looks like (maybe just a one-page plan for a single weekend, not a whole itinerary).

When you've answered, Ada hands you back a crisp restatement: the goal, who it's for, and what "done" means. Something like *"A simple one-page plan for a two-day trip within driving distance, under a set budget, with one anchor activity per day."*

## Step 2 — Hand off to Sam to make it

Ada decides this needs making, not critiquing, so she routes it to Sam, the Tech Lead and maker. You can let Ada hand off, or call Sam yourself:

```
@sam Here's the framed task from Ada. Draft the one-page weekend plan.
```

Sam produces the actual thing — a tidy draft plan with the two days laid out, the anchor activities, a rough budget line, and a couple of notes where he made a judgment call. Sam also does a light sanity check as he goes, so what comes back is coherent, not just a first guess.

## Step 3 — Get Robin's second opinion

Before you call it done, bring in Robin, the Reviewer. Robin's whole job is "what might break, what's missing."

```
@robin Take a look at Sam's weekend plan. What did we miss?
```

Robin reads the plan against what it's supposed to do and flags the gaps: no rain backup for the outdoor day, the budget didn't include gas, one activity might be closed on Mondays. None of this is a rewrite — it's the stuff you'd kick yourself for forgetting. You fold in the fixes you care about.

## Step 4 — Close the session and watch the memory fill

Here's the part that makes VibeOS more than a fancy chat. Run:

```
/vcos-session-close
```

This reads back over the session and captures it into the team's memory — the **cognitive layer**. You'll see entries appear that you didn't have to write yourself:

- A few lines land in **STANCE** (the decision log), like:
  - `[Decision] Scoped the trip to one weekend within driving distance to keep the first plan simple.`
  - `[Decision] Chose one anchor activity per day rather than packing the schedule.`
  - `[Mistake] First draft budget left out travel costs; added a gas/transport line after Robin's review.`
- If a pattern recurred, it gets staged in **SIGNALS** — for example, a note that *the first draft tends to underestimate cost, so check for missing line items.*

Open the project's `project cognitive layer/` folder and look: STANCE has real entries now. That's the whole loop working. You framed something, made it, reviewed it, and the team wrote down what it learned — automatically.

## What just happened

In one short session you used all three teammates the way they're meant to be used — Ada to frame and route, Sam to make, Robin to catch what's missing — and you ended with `/vcos-session-close`, the one ritual that keeps the memory growing.

Do this a few times and the difference shows up on its own: next time you plan something, the team already knows to check for missing costs and to scope small first. It starts from your earned judgment instead of a blank page.

## Where to go from here

- Start a real project with `/new-vibeos-project`.
- Read **[COGNITIVE_LAYER_101.md](COGNITIVE_LAYER_101.md)** to understand the memory you just watched fill.
- Peek at **[examples/sample-project/](examples/sample-project/)** to see a finished project's memory.
- When you've got a few projects going, explore the advanced rituals (`/vcos-review`, `/vcos-synthesize`) — but there's no rush. For now, just keep closing your sessions.
