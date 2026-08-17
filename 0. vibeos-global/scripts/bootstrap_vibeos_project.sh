#!/bin/zsh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GLOBAL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_ROOT="$(cd "$GLOBAL_DIR/.." && pwd)"
TEMPLATE_DIR="$WORKSPACE_ROOT/1. vibeos-template"
PROJECTS_DIR="$WORKSPACE_ROOT/projects"

usage() {
  cat <<'EOF'
Usage:
  bootstrap_vibeos_project.sh "Project Name" [type]
  bootstrap_vibeos_project.sh /absolute/path/to/project [type]

type (optional): engops | build   (default: engops)
  engops → canonical artifact is docs/operating_brief.md (org/process/analysis/decisions)
  build  → canonical artifact is docs/build_packet.md (for software)

What it does:
  1. Creates the project folder if needed
  2. Copies the VibeOS template scaffold into it
  3. Keeps the canonical artifact for the project type; prunes the other
  4. Replaces [Project Name] placeholders in all copied files
  5. Writes START_HERE.md and CLAUDE.md pointing at the canonical artifact
  6. Verifies shared global files and the project cognitive layer
  7. Removes .DS_Store files

Note: personas are global and shared — they are NOT copied into the project.
      Relative project names are created under: projects/
EOF
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

TARGET_INPUT="$1"
PROJECT_TYPE="${2:-engops}"
# normalize type
PROJECT_TYPE="$(printf '%s' "$PROJECT_TYPE" | tr '[:upper:]' '[:lower:]' | tr -d ' -_')"
if [[ "$PROJECT_TYPE" == "build" ]]; then
  PROJECT_TYPE="build"
else
  PROJECT_TYPE="engops"
fi

if [[ "$TARGET_INPUT" = /* ]]; then
  PROJECT_DIR="$TARGET_INPUT"
else
  PROJECT_DIR="$PROJECTS_DIR/$TARGET_INPUT"
fi

PROJECT_NAME="$(basename "$PROJECT_DIR")"
SIGNALS_FILE="$GLOBAL_DIR/global cognitive layer/GLOBAL_SIGNALS.md"
MINDSET_FILE="$GLOBAL_DIR/global cognitive layer/GLOBAL_MINDSET.md"
PERSONAS_DIR="$GLOBAL_DIR/personas"
STANCE_INSTRUCTIONS="$PROJECT_DIR/instructions/stance_instructions.md"
PROJECT_SIGNALS_INSTRUCTIONS="$PROJECT_DIR/instructions/signals_instructions.md"
PROJECT_MINDSET_INSTRUCTIONS="$PROJECT_DIR/instructions/mindset_instructions.md"
SIGNALS_INSTRUCTIONS="$PROJECT_DIR/project cognitive layer/0. signals_instructions.md"
MINDSET_INSTRUCTIONS="$PROJECT_DIR/project cognitive layer/0. mindset_instructions.md"

# Verify global resources
if [[ ! -d "$TEMPLATE_DIR" ]]; then
  echo "Template folder not found: $TEMPLATE_DIR" >&2
  exit 1
fi
if [[ ! -f "$SIGNALS_FILE" ]]; then
  echo "Global signals file not found: $SIGNALS_FILE" >&2
  exit 1
fi
if [[ ! -f "$MINDSET_FILE" ]]; then
  echo "Global mindset file not found: $MINDSET_FILE" >&2
  exit 1
fi
if [[ ! -d "$PERSONAS_DIR" ]]; then
  echo "Global personas folder not found: $PERSONAS_DIR" >&2
  exit 1
fi

# Create project and copy template
mkdir -p "$PROJECTS_DIR"
# Fail-closed: never overwrite an existing, non-empty project. The template copy
# below is followed by type-based pruning (rm -f), which would be destructive if
# pointed at an existing project. Set VIBEOS_FORCE=1 to overwrite intentionally.
if [[ -d "$PROJECT_DIR" && -n "$(ls -A "$PROJECT_DIR" 2>/dev/null)" ]]; then
  if [[ "${VIBEOS_FORCE:-0}" != "1" ]]; then
    echo "error: target already exists and is non-empty: $PROJECT_DIR" >&2
    echo "       refusing to overwrite. Use a new name, or set VIBEOS_FORCE=1 to overwrite intentionally." >&2
    exit 1
  fi
  echo "warning: VIBEOS_FORCE=1 set — overwriting existing $PROJECT_DIR" >&2
fi
mkdir -p "$PROJECT_DIR"
cp -R "$TEMPLATE_DIR/." "$PROJECT_DIR/"
find "$PROJECT_DIR" -name '.DS_Store' -delete

# Prune to the canonical artifact for the project type
if [[ "$PROJECT_TYPE" == "engops" ]]; then
  CANONICAL_ARTIFACT="docs/operating_brief.md"
  CANONICAL_DESC="Operating Brief — situation, the decision, options/tradeoffs, owners, follow-through"
  rm -f "$PROJECT_DIR/docs/build_packet.md" \
        "$PROJECT_DIR/docs/build_packet_index.md" \
        "$PROJECT_DIR/docs/tdd.md" \
        "$PROJECT_DIR/docs/security.md" \
        "$PROJECT_DIR/docs/design_brief.md" \
        "$PROJECT_DIR/instructions/build_packet_instructions.md" \
        "$PROJECT_DIR/instructions/tdd_instructions.md" \
        "$PROJECT_DIR/instructions/security_instructions.md" \
        "$PROJECT_DIR/instructions/design_brief_instructions.md"
  cat > "$PROJECT_DIR/prompts/prompts.md" <<EOF
# PROMPTS — $PROJECT_NAME

Decision/process project. The canonical planning artifact is \`docs/operating_brief.md\`, not a
Build Packet. If the decision requires software, spin a build sub-slice with its own
\`build_packet.md\`.

## OPERATING BRIEF (the plan)
Use during SPEC / DESIGN to frame the decision and rollout.

Prompt:
Create or update OPERATING_BRIEF.md — situation, decisions to be made, options/tradeoffs,
owners, follow-through, and open questions.

Follow:
../instructions/operating_brief_instructions.md

---

## CURRENT STATUS OVERVIEW
Use before a major regroup or before scoping the next phase.

Prompt:
Create a current-status overview so a fresh session can pick up the project efficiently.

Follow:
../instructions/current_status_overview_instructions.md

---

## STANCE Update (High Frequency)
Use during any session after a meaningful cross-cutting decision.

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
Use after SIGNALS accumulate, typically at project milestones.

Prompt:
Propose updates to MINDSET.md from SIGNALS.md.

Follow:
../project cognitive layer/0. mindset_instructions.md
EOF
else
  CANONICAL_ARTIFACT="docs/build_packet.md"
  CANONICAL_DESC="Build Packet — problem, scope, acceptance criteria, architecture"
  rm -f "$PROJECT_DIR/docs/operating_brief.md" \
        "$PROJECT_DIR/instructions/operating_brief_instructions.md"
fi

# Replace [Project Name] placeholders. Escape sed-special chars in the replacement.
ESCAPED_NAME=$(printf '%s\n' "$PROJECT_NAME" | sed -e 's/[\/&]/\\&/g')
find "$PROJECT_DIR" -name '*.md' | while read -r f; do
  sed -i '' "s/\[Project Name\]/$ESCAPED_NAME/g" "$f"
done

# Verify the always-required project files
for required in \
  "$PROJECT_DIR/docs/project_context.md" \
  "$PROJECT_DIR/$CANONICAL_ARTIFACT" \
  "$STANCE_INSTRUCTIONS" \
  "$PROJECT_SIGNALS_INSTRUCTIONS" \
  "$PROJECT_MINDSET_INSTRUCTIONS" \
  "$SIGNALS_INSTRUCTIONS" \
  "$MINDSET_INSTRUCTIONS"; do
  if [[ ! -f "$required" ]]; then
    echo "Missing required project file: $required" >&2
    exit 1
  fi
done

# Write START_HERE.md with resolved absolute paths
cat > "$PROJECT_DIR/START_HERE.md" <<EOF
# $PROJECT_NAME — VibeOS Project

Type: $PROJECT_TYPE
Generated by bootstrap. Do not edit the paths section manually.

---

## Global Paths (shared across all projects)

Personas:
  $PERSONAS_DIR/

Global Cognitive Layer:
  $GLOBAL_DIR/global cognitive layer/GLOBAL_SIGNALS.md
  $GLOBAL_DIR/global cognitive layer/GLOBAL_MINDSET.md

---

## Session Start Prompt

Paste at the start of any Cursor / Claude session for this project:

\`\`\`
You are [Persona Name] for the $PROJECT_NAME project.

Before doing substantive work, complete persona onboarding by reading the
project's core context files in addition to your persona files.

Read (global — shared across all projects):
- $PERSONAS_DIR/[name]/PERSONA.md
- $PERSONAS_DIR/[name]/MINDSET.md
- $PERSONAS_DIR/[name]/SIGNALS.md

Read (project-local):
- $PROJECT_DIR/docs/project_context.md
- $PROJECT_DIR/$CANONICAL_ARTIFACT
- $PROJECT_DIR/project cognitive layer/STANCE.md
- $PROJECT_DIR/project cognitive layer/SIGNALS.md
- $PROJECT_DIR/project cognitive layer/MINDSET.md

[Your task or question]
\`\`\`

---

## Project Files

| File | Purpose |
|------|---------|
| docs/project_context.md | Vision, current goal, constraints, open questions |
| $CANONICAL_ARTIFACT | $CANONICAL_DESC |
| project cognitive layer/STANCE.md | Real-time decision log (append during sessions) |
| project cognitive layer/SIGNALS.md | Pattern staging area (promote from STANCE) |
| project cognitive layer/MINDSET.md | Distilled lessons (fill at end of project) |

EOF

# Write CLAUDE.md for Claude Code integration
cat > "$PROJECT_DIR/CLAUDE.md" <<EOF
# $PROJECT_NAME — VibeOS Project ($PROJECT_TYPE)

## Context Files

Read these at the start of every session:

| File | Purpose |
|------|---------|
| docs/project_context.md | Vision, current goal, constraints, open questions |
| $CANONICAL_ARTIFACT | $CANONICAL_DESC |
| project cognitive layer/STANCE.md | Real-time decision log (append during sessions) |
| project cognitive layer/SIGNALS.md | Pattern staging area (promote from STANCE when ≥2x) |
| project cognitive layer/MINDSET.md | Distilled lessons (fill at project end) |

## Global Resources

Personas:
  $PERSONAS_DIR/

Global Cognitive Layer:
  $GLOBAL_DIR/global cognitive layer/GLOBAL_MINDSET.md
  $GLOBAL_DIR/global cognitive layer/GLOBAL_SIGNALS.md

## Available Commands

| Command | When to use |
|---------|-------------|
| /vcos-spec | Turn raw notes or a problem into a plan (Build Packet) |
| /vcos-build | Turn a plan into small, ordered steps |
| /vcos-memory | Capture decisions to STANCE, promote patterns to SIGNALS |
| /vcos-session-close | End-of-session capture into the cognitive layer |
| /vcos-status | A compact snapshot of where the project stands |

## Available Personas

@ada (Chief of Staff — frame & route), @sam (Tech Lead — make), @robin (Reviewer — check).
Add more with /vibeos-new-persona.

Suggested flow for this project type ($PROJECT_TYPE):
EOF

if [[ "$PROJECT_TYPE" == "engops" ]]; then
  cat >> "$PROJECT_DIR/CLAUDE.md" <<'EOF'
@ada (frame the decision and options) → @sam (draft the plan or artifact) → @robin (what might break / what's missing) → @ada (pull it together). Spin a Build sub-slice only if a tool is needed.
EOF
else
  cat >> "$PROJECT_DIR/CLAUDE.md" <<'EOF'
@ada (frame the problem and scope) → @sam (build it, with a quick sanity check) → @robin (review before you ship) → @ada (wrap up). Use /vcos-spec and /vcos-build to structure the work.
EOF
fi

cat <<EOF
Project ready: $PROJECT_DIR
Type: $PROJECT_TYPE
Canonical artifact: $CANONICAL_ARTIFACT

Template copied from:
  $TEMPLATE_DIR
[Project Name] replaced with: $PROJECT_NAME

Global references confirmed:
  $SIGNALS_FILE
  $MINDSET_FILE
  $PERSONAS_DIR  (shared — not copied)

Session start files written:
  $PROJECT_DIR/START_HERE.md
  $PROJECT_DIR/CLAUDE.md
EOF
