#!/bin/bash
# VibeOS cognitive-load watch. Your team reads whole MINDSET/SIGNALS files each session;
# that works great small and degrades as they grow. This watches the size ceilings and
# prints a WATCH line when a file is big enough that it's worth tidying. It only informs —
# it never blocks — and pairs naturally with /vcos-consolidate. Run it inside /vcos-review.

cd "$(dirname "$0")/../.." || exit 0

watch=0
check() { # path, ceiling, label
  [ -f "$1" ] || return 0
  n=$(wc -l < "$1" | tr -d ' ')
  if [ "$n" -gt "$2" ]; then
    echo "WATCH: $3 is $n lines (ceiling $2) — $1"
    watch=1
  fi
}

# Global layer
check "0. vibeos-global/global cognitive layer/GLOBAL_MINDSET.md" 120 "GLOBAL_MINDSET"
check "0. vibeos-global/global cognitive layer/GLOBAL_SIGNALS.md" 250 "GLOBAL_SIGNALS"

# Per-persona MINDSETs (consolidate aims to keep these under ~100; watch at 120 so there's room to act)
while IFS= read -r -d '' f; do
  check "$f" 120 "Persona MINDSET ($(basename "$(dirname "$f")"))"
done < <(find "0. vibeos-global/personas" -name "MINDSET.md" -print0 2>/dev/null)

# Total always-loaded read surface (identity + global layer)
total=$(cat "0. vibeos-global/SOUL.md" "0. vibeos-global/USER.md" \
  "0. vibeos-global/global cognitive layer/GLOBAL_MINDSET.md" \
  "0. vibeos-global/global cognitive layer/GLOBAL_SIGNALS.md" 2>/dev/null | wc -l | tr -d ' ')
if [ "$total" -gt 800 ]; then
  echo "WATCH: always-loaded layer is $total lines (ceiling 800) — every session pays this on start"
  watch=1
fi

if [ "$watch" -eq 0 ]; then
  echo "ok: cognitive layer within ceilings — nothing to tidy yet"
else
  echo "ACTION: a WATCH fired — the first response is /vcos-consolidate (merge near-duplicates, retire stale entries)"
fi
exit 0
