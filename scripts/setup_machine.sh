#!/usr/bin/env bash
# Regenerates the machine-local .claude/ routing layer from the committed,
# path-agnostic routing/ source. Run once after cloning, and again whenever
# routing/ changes upstream.
#
#   bash scripts/setup_machine.sh
#
# It stamps this machine's absolute workspace path into every persona and
# command file, replacing the {{VIBEOS_ROOT}} placeholder. .claude/ is
# generated output and is gitignored; routing/ is the source of truth.

set -euo pipefail

# Repo root = parent of the directory holding this script.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SRC="$ROOT/routing"
DEST="$ROOT/.claude"

if [ ! -d "$SRC" ]; then
  echo "error: $SRC not found. Run this from inside the VibeOS workspace." >&2
  exit 1
fi

echo "Workspace root: $ROOT"
echo "Generating .claude/ from routing/ ..."

mkdir -p "$DEST/agents" "$DEST/commands"

count=0
for sub in agents commands; do
  for f in "$SRC/$sub"/*.md; do
    [ -e "$f" ] || continue
    # Use | as the sed delimiter; ROOT contains / but never |.
    sed "s|{{VIBEOS_ROOT}}|$ROOT|g" "$f" > "$DEST/$sub/$(basename "$f")"
    count=$((count + 1))
  done
done

# Stamp the hooks settings template (SessionStart status + Stop session-close nudge), if present.
if [ -f "$SRC/settings.template.json" ]; then
  sed "s|{{VIBEOS_ROOT}}|$ROOT|g" "$SRC/settings.template.json" > "$DEST/settings.json"
  echo "Wrote .claude/settings.json (session hooks)."
fi

echo "Done. Wrote $count routing files into .claude/"
