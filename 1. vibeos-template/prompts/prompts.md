# PROMPTS

Reusable prompts for this project. Each points at the instruction file that guides the output.

## BUILD_PACKET (the plan)
Use when framing what you're going to build or make.

Prompt:
Create or update BUILD_PACKET.md.

Follow:
../instructions/build_packet_instructions.md

---

## CURRENT STATUS OVERVIEW
Use before a major regroup or before scoping the next phase.

Prompt:
Create a current-status overview so a fresh session can pick up the project efficiently.

Follow:
../instructions/current_status_overview_instructions.md

---

## STANCE Update (High Frequency)
Use during any session after a meaningful decision.

Prompt:
Update STANCE.md.

Follow:
../project cognitive layer/0. stance_instructions.md

---

## SIGNALS Extraction (Medium Frequency)
Use at end of session or after multiple STANCE updates.

Prompt:
Update SIGNALS.md from STANCE.md.

Follow:
../project cognitive layer/0. signals_instructions.md

---

## MINDSET Proposal (Low Frequency)
Use after SIGNALS accumulate, typically at a project milestone.

Prompt:
Propose updates to MINDSET.md from SIGNALS.md.

Follow:
../project cognitive layer/0. mindset_instructions.md

---

## IMPLEMENTATION PLAN
Use before coding (if the project produces code).

Prompt:
Create a step-by-step implementation plan from BUILD_PACKET.md.

---

## TEST GENERATION
Use during validation (if the project produces code).

Prompt:
Generate test cases from BUILD_PACKET.md and the code.
