# VibeOS Model Tier Parity Standard

How to get a lower-tier model (say, Opus) to operate as closely as possible to the strongest tier (Fable). The practice has a name: **capability elicitation**, using prompting and scaffolding to pull a model's best work out of it instead of accepting its default effort.

Use this when running a persona or skill on a model below the top tier, or when a result feels shallower than it should.

Complements:
- `0. vibeos-global/SOUL.md` (the operating principles this doc operationalizes)
- `PERSONA_STANDARD.md` (where the drop-in add-on gets wired into personas)

## The premise: the gap is judgment, not knowledge

A lower-tier model usually knows the same facts as the top tier. What it does less reliably is the *judgment work*: planning before acting, checking its own output, holding every constraint in view over a long task, and being honest about what it is unsure of. The top tier does these on its own. A lower tier does them when you make the structure explicit.

So parity is not about a magic prompt. It is about forcing the behaviors a strong model self-generates. Most of the gap closes with scaffolding. The last slice does not, and this doc is honest about that (see "When to just use Fable").

## Lever zero: feed it the right context

The seven levers below shape how the model works. Before any of them applies, check what you gave it. Most "the model is being dumb" failures are actually missing context, and a lower tier is worse at inferring what you did not say. So say it.

- **Give it the relevant facts, files, and definitions up front** instead of letting it guess. In VibeOS this is the session-start ritual: personas read `project_context.md`, the canonical artifact, and STANCE before substantive work.
- **One task per prompt.** Bundled asks degrade a weaker model fastest; split them.
- **Keep the context clean.** A long session full of dead ends degrades output (the failure is called **context rot**: accumulated clutter crowding out the signal). When a session gets muddy, restart fresh with a clean summary of decisions so far. STANCE makes that restart cheap.

## The seven levers

Each lever names the symptom you see in a weaker model, the technique, a drop-in prompt line, and the VibeOS mechanism that already supports it.

| # | Symptom in the weaker model | Lever | VibeOS hook |
|---|------------------------------|-------|-------------|
| 1 | Jumps straight to output, misreads the ask | **Plan before acting** | "Smallest safe experiment"; `/vcos-build` ordered plan |
| 2 | Shallow reasoning, misses the non-obvious | **Think before answering** | raise reasoning effort; extended thinking |
| 3 | Confident but wrong; no self-check | **Adversarial self-verify** | `@robin` reviewer lens |
| 4 | Drops constraints on big tasks | **Decompose into checkable steps** | skills as decomposition; the spec → build pipeline |
| 5 | Forgets earlier decisions late in a task | **Externalize memory** | STANCE / SIGNALS cognitive layer |
| 6 | Hides assumptions, states guesses as fact | **Surface assumptions + calibrated confidence** | "Make the invisible visible" |
| 7 | Vague or inconsistent format | **Give a worked example + output template** | persona output contracts |

### 1. Plan before acting
Make it state the plan and get a check before it executes. A weaker model that plans first reads the problem more carefully.
> "Before doing anything, restate the goal in one line, list the steps you will take, and flag the riskiest assumption. Wait for my confirmation on anything hard to reverse."

### 2. Think before answering
Give it room to reason, and turn the reasoning dial up for hard problems. On Claude, that means raising **reasoning effort** (how much the model deliberates before responding) or using extended thinking. Cheap and high-leverage.
> "Think this through step by step before you answer. Show the reasoning that changes the conclusion, not filler."

### 3. Adversarial self-verify
The single highest-value move. After a first answer, make the model attack its own work as a skeptic. A weaker model rarely does this unprompted, and it catches most of the errors that separate it from the top tier.
> "Now review that answer as an adversary trying to prove it wrong. List every way it could be incorrect or incomplete, then give a corrected version. Default to 'this is wrong' and make it earn 'correct.'"

Two upgrades when the stakes are high. First, verify in a **fresh context**: a model re-reading its own answer in the same session inherits the assumptions that produced the error, so paste the work (not the reasoning behind it) into a new session, or hand it to a second persona (`@robin` exists for exactly this). Second, verify against **ground truth** wherever it exists: run the code, check the number, click the link. Execution is evidence; self-review is opinion.

### 4. Decompose into checkable steps
Break the task into small pieces with a verifiable result at each step. Smaller steps mean fewer dropped constraints and a clear place to catch a mistake. This is the "smallest safe experiment" principle applied to the model's own process.
> "Split this into the smallest ordered steps. Do one at a time. After each, state what you produced and how you know it is correct before moving on."

### 5. Externalize memory
On long tasks a weaker model loses the thread. Have it write decisions and constraints to a durable place and re-read them, rather than trusting them to stay in context. This is exactly what the VibeOS cognitive layer is for.
> "Keep a running list of the decisions made and constraints still in force. Restate it before each major step and update it as things change."

### 6. Surface assumptions and calibrated confidence
Force it to separate what it knows from what it is guessing, and to attach a confidence level. **Calibration** means the stated confidence matches the real hit rate: when it says 90%, it should be right about 90% of the time. Weaker models tend to be overconfident, so asking for calibrated confidence exposes the soft spots.
> "Mark each claim as Known, Inferred, or Guess. Give a confidence percentage on the conclusion and name what would change it."

### 7. Give a worked example and an output template
Show one example of the quality and shape you want (**few-shot prompting**, meaning you provide worked examples in the prompt), plus a fixed output structure. A weaker model matches a concrete template far more reliably than it follows an abstract instruction.
> "Match this format exactly: [template]. Here is one example done to the standard I want: [example]."

## The escalation ladder

Spend the cheapest intervention that gets you to parity. Climb only when the result is still short. Each rung costs more time or money than the one below it.

| Rung | Intervention | Cost | Use when |
|------|--------------|------|----------|
| 0 | Fix the context: right inputs, one task, clean session | ~free | Before anything else |
| 1 | Add the drop-in block below to the prompt | ~free | Default, always |
| 2 | Raise reasoning effort / add a think step | low | Reasoning-heavy tasks |
| 3 | Add an adversarial verify pass (fresh session when wrong is costly) | low | Anything where being wrong is costly |
| 4 | Decompose into a multi-step skill run | medium | Large or multi-part work |
| 5 | Multi-sample: generate 3 answers, pick or merge the best | medium-high | High-stakes, wide solution space |
| 6 | Route the task to Fable | highest | The gap still shows after 0 to 5 |

Rule of thumb: rungs 0 to 3 close most of the everyday gap and cost almost nothing. If you find yourself needing rung 5 often for a given task type, that is a signal the task belongs on Fable.

## Drop-in add-on block (copy-paste)

This is the portable piece. Paste it into any persona prompt, skill run, or a fresh chat in any tool when running below the top tier. It bundles the highest-value levers into one block.

```
OPERATING STANDARD (run at full effort):
0. Get the context first. If information you need is missing, name it and ask
   instead of guessing.
1. Plan first. Restate the goal in one line, list your steps, flag the riskiest
   assumption. Pause before anything hard to reverse.
2. Think before answering. Reason through the parts that change the conclusion.
3. Self-verify as an adversary. Before you finalize, attack your own answer,
   list how it could be wrong, then correct it. Default to "wrong until proven."
   Verify against reality (run it, check it) whenever ground truth exists.
4. Work in small checkable steps. After each, say what you produced and how you
   know it holds.
5. Track decisions and constraints in a running list; restate it before big steps.
6. Separate Known / Inferred / Guess. Give calibrated confidence and name what
   would change it.
7. Match the requested format exactly. If none is given, propose a clean one first.
Scale this ritual to the stakes: a trivial ask needs only 2 and 3.
Surface assumptions, risks, and open questions explicitly. Do not hide uncertainty.
```

## Persona integration

Two ways to apply this, from lightest to most wired-in:

1. **Ad hoc.** Paste the drop-in block at the top of a persona or skill run when you are on a lower tier. Zero framework changes.
2. **Standing.** Append the drop-in block (or a reference to this standard) to each persona's `STARTER_PROMPT.md` so it travels with the persona into any tool. Regenerate starter prompts via `/vcos-memory` after adding it. Do this only for the personas that carry the heaviest judgment load (`@ada`, `@sam`, `@robin`) if you want to keep prompts lean.

VibeOS already does the structural half of this work: personas prime a role, skills decompose, the cognitive layer externalizes memory, and "make the invisible visible" forces assumptions into the open. This standard names the model-behavior half so a lower tier gets the same discipline the framework already assumes.

## Anti-patterns

- **"Think harder" with nothing concrete.** Vague exhortation does little. Name the specific behavior (plan, verify, decompose).
- **Over-prompting.** Stacking ten instructions on a trivial task wastes effort and can degrade output. Match the scaffolding to the difficulty (the block's own "scale to the stakes" line exists for this).
- **Skipping the verify pass to save time.** It is the cheapest high-value rung. Cutting it is where lower-tier errors slip through.
- **Treating scaffolding as a guarantee.** It narrows the gap; it does not erase it. Keep the honest limit in view.

## When to just use Fable

Scaffolding buys back consistency, not headroom. For a small class of tasks the top tier is simply the right tool and the effort of elicitation is not worth it:

- Novel reasoning with no template to anchor on, where the answer quality depends on raw depth
- Long-horizon tasks where small judgment errors compound faster than verify passes can catch them
- Work where being subtly wrong is expensive and you cannot afford the residual gap
- Work you have no way to verify yourself: no ground truth to check and no expertise to judge it, so you would be trusting the output blind

For those, route to Fable and move on. Knowing when to stop climbing the ladder is itself part of operating well.
