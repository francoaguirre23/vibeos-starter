#!/usr/bin/env bash
# Confidentiality verification — fail-closed audit of project classifications.
# See standards/CONFIDENTIALITY.md. Run manually or inside /vcos-review.
# Exit 0 = clean. Exit 1 = action needed (unclassified projects or an NDA leak).

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GLOBAL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_ROOT="$(cd "$GLOBAL_DIR/.." && pwd)"
PROJECTS_DIR="$WORKSPACE_ROOT/projects"
INDEX="$PROJECTS_DIR/INDEX.md"
SHARED_LAYER="$GLOBAL_DIR/global cognitive layer"
OS_INDEX="$WORKSPACE_ROOT/OS_INDEX.md"

problems=0
valid="Public Internal Confidential NDA"

echo "=== VibeOS confidentiality check ==="

if [[ ! -f "$INDEX" ]]; then
  echo "FAIL: classification registry not found: $INDEX"
  exit 1
fi

# Parse the registry table. Columns: | Folder | Name | Confidentiality | ... |
# awk fields (-F'|'): $2=folder, $3=name, $4=confidentiality. Trim spaces/**.
# Emit "folder<TAB>conf<TAB>name" for data rows only (skip header + separator).
parse_index() {
  awk -F'|' '
    /^\|/ {
      f=$2; c=$4; n=$3
      gsub(/^[ \t]+|[ \t]+$/, "", f)
      gsub(/^[ \t]+|[ \t]+$/, "", c)
      gsub(/^[ \t]+|[ \t]+$/, "", n); gsub(/\*/, "", n)
      gsub(/^[ \t]+|[ \t]+$/, "", n)
      if (f=="" || f=="Folder" || f ~ /^-+$/) next
      print f "\t" c "\t" n
    }
  ' "$INDEX"
}

# 1. Every project folder must have a valid classification row in INDEX.
echo ""
echo "-- Project classifications (fail-closed: unlisted/invalid = NDA) --"
for d in "$PROJECTS_DIR"/*/; do
  name="$(basename "$d")"
  row="$(parse_index | awk -F'\t' -v n="$name" '$1==n {print; exit}')"
  if [[ -z "$row" ]]; then
    echo "  FLAG  $name — not in INDEX registry → treated as NDA (classify it)"
    problems=$((problems+1)); continue
  fi
  conf="$(printf '%s' "$row" | cut -f2)"
  if [[ " $valid " != *" $conf "* ]]; then
    echo "  FLAG  $name — invalid/blank classification '$conf' → treated as NDA"
    problems=$((problems+1))
  else
    echo "  ok    $name — $conf"
  fi
done

# 2. NDA codenames must not appear in the shared cognitive layer or OS_INDEX.
#    (Confidential projects may be named; only their specifics are banned — a
#     synthesis-time rule this check cannot enforce mechanically.)
echo ""
echo "-- Shared-layer naming ban (NDA codenames must not appear) --"
nda_names="$(parse_index | awk -F'\t' '$2=="NDA" {print $3}')"
if [[ -z "$nda_names" ]]; then
  echo "  (no NDA codenames registered)"
else
  while IFS= read -r cn; do
    [[ -z "$cn" ]] && continue
    hits="$(grep -rilF "$cn" "$SHARED_LAYER" "$OS_INDEX" 2>/dev/null || true)"
    if [[ -n "$hits" ]]; then
      echo "  FLAG  '$cn' named in shared layer:"
      while IFS= read -r h; do [[ -n "$h" ]] && echo "        $h"; done <<< "$hits"
      problems=$((problems+1))
    else
      echo "  ok    '$cn' — not named in shared layer"
    fi
  done <<< "$nda_names"
fi

echo ""
if [[ "$problems" -eq 0 ]]; then
  echo "PASS — all projects classified; no NDA codenames in the shared layer."
  exit 0
else
  echo "ACTION NEEDED — $problems issue(s). Unclassified projects are treated as NDA (excluded from git + synthesis) until resolved."
  exit 1
fi
