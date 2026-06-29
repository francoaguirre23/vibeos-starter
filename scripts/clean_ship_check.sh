#!/usr/bin/env bash
# Clean-ship gate for a VibeOS workspace.
# Fails (exit 1) if anything personal, confidential, or machine-specific is present.
# Run before publishing or pushing anywhere public:
#
#   bash scripts/clean_ship_check.sh
#
# This tracked file carries ONLY generic patterns — it deliberately names no people,
# companies, or projects, so the gate itself never leaks the vocabulary it protects.
# Add your own private terms (names, codenames, company words) in a LOCAL, GITIGNORED
# place so they never ship:
#   * a file: scripts/clean_ship_denylist.local  (one regex per line; '#' comments ok)
#   * or env: CLEAN_SHIP_EXTRA_PATTERNS="acme|projectx|jane\.doe"
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
fail=0
SELF="scripts/clean_ship_check.sh"
DENYLIST_FILE="scripts/clean_ship_denylist.local"

echo "=== VibeOS clean-ship check ==="

# 1. Forbidden files/dirs must be absent (local-only, never shipped)
while IFS= read -r p; do
  [ -z "$p" ] && continue
  echo "  FAIL  forbidden present: $p"; fail=1
done < <(
  { [ -e "0. vibeos-global/USER.md" ] && echo "0. vibeos-global/USER.md"; } ;
  { [ -e "projects" ] && echo "projects/"; } ;
  find . \( -name '.env' -o -name '.env.*' -o -name '*.mcp.json' \) -not -path '*/.git/*' -not -path '*/.claude/*' 2>/dev/null
)

# 2a. Generic patterns — safe to ship, reveal nothing. High-signal, low false-positive:
#     absolute home paths, private-key blocks, common cloud/token credential formats.
GENERIC='(/Users/|/home/[a-z]|/root/)|-----BEGIN [A-Z ]*PRIVATE KEY-----|AKIA[0-9A-Z]{16}|xox[baprs]-[0-9A-Za-z-]{10,}|gh[pousr]_[0-9A-Za-z]{20,}'

# 2b. Your private terms — loaded from a gitignored file and/or env var. Nothing
#     sensitive lives in this tracked script; the real vocabulary stays local.
EXTRA=""
if [ -f "$DENYLIST_FILE" ]; then
  EXTRA="$(grep -vE '^[[:space:]]*(#|$)' "$DENYLIST_FILE" 2>/dev/null | paste -sd '|' - || true)"
fi
if [ -n "${CLEAN_SHIP_EXTRA_PATTERNS:-}" ]; then
  EXTRA="${EXTRA:+$EXTRA|}$CLEAN_SHIP_EXTRA_PATTERNS"
fi

PATTERNS="$GENERIC"
[ -n "$EXTRA" ] && PATTERNS="$PATTERNS|$EXTRA"

# Scan all text files (grep -I skips binary). Exclude generated/gitignored dirs, the
# scanner itself, and the private denylist (which legitimately holds the terms).
hits="$(grep -rIniE "$PATTERNS" . 2>/dev/null \
  | grep -v '/.git/' | grep -v '/.claude/' | grep -v '/__pycache__/' \
  | grep -v "$SELF" | grep -v "$DENYLIST_FILE" || true)"
if [ -n "$hits" ]; then
  echo "  FAIL  forbidden content found:"; echo "$hits" | sed 's/^/        /' | head -50; fail=1
else
  echo "  ok    no forbidden content patterns"
fi

if [ -z "$EXTRA" ]; then
  echo "  note  no private denylist loaded — add $DENYLIST_FILE (gitignored) or set"
  echo "        CLEAN_SHIP_EXTRA_PATTERNS to also catch your own names and codenames."
fi

echo ""
if [ "$fail" -eq 0 ]; then
  echo "PASS — clean to ship."
  exit 0
else
  echo "ACTION NEEDED — resolve the above before publishing. Git history is permanent; fix before the first push."
  exit 1
fi
