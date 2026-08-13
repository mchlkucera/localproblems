#!/usr/bin/env bash
# fetch_ted.sh — TED Search API v3, no auth. CZ place of performance.
# Usage: scripts/fetch_ted.sh [YYYYMMDD-since] [outdir]
# Writes one JSON per CPV group into outdir (default data/sources/<today>/).
set -euo pipefail

SINCE="${1:-$(date -v-60d +%Y%m%d 2>/dev/null || date -d '60 days ago' +%Y%m%d)}"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${2:-data/sources/$TODAY}"
mkdir -p "$OUTDIR"

API="https://api.ted.europa.eu/v3/notices/search"
FIELDS='["publication-number","publication-date","notice-title","buyer-name","buyer-city","classification-cpv","notice-type","form-type","contract-nature","estimated-value-lot","estimated-value-cur-lot","estimated-value-glo","estimated-value-cur-glo","total-value","total-value-cur","deadline-receipt-tender-date-lot"]'

# CPV groups relevant to the register (keep in sync with problem categories)
# bash 3.2 compatible: "key:cpv-list" pairs
CPV_GROUPS="it:72* 48*
health:85*
bizserv:79*
energy:09* 65*
construction:71*"

echo "$CPV_GROUPS" | while IFS=: read -r key cpv; do
  out="$OUTDIR/ted-$key.json"
  echo "== $key (CPV $cpv) since $SINCE"
  page=1
  : > "$out.tmp"
  while :; do
    resp=$(curl -s -m 60 -X POST "$API" -H "Content-Type: application/json" -d "{
      \"query\": \"(place-of-performance IN (CZE)) AND (publication-date >= $SINCE) AND (classification-cpv IN ($cpv))\",
      \"fields\": $FIELDS, \"limit\": 250, \"page\": $page }")
    n=$(printf '%s' "$resp" | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('notices',[])))" 2>/dev/null || echo 0)
    printf '%s\n' "$resp" >> "$out.tmp"
    total=$(printf '%s' "$resp" | python3 -c "import json,sys; print(json.load(sys.stdin).get('totalNoticeCount',0))" 2>/dev/null || echo 0)
    echo "   page $page: $n notices (total $total)"
    [ "$n" -lt 250 ] && break
    page=$((page+1))
    [ "$page" -gt 60 ] && break   # safety
  done
  # merge pages into one array
  python3 - "$out.tmp" "$out" <<'PY'
import json, sys
notices = []
for line in open(sys.argv[1]):
    line = line.strip()
    if not line: continue
    try: notices += json.loads(line).get('notices', [])
    except json.JSONDecodeError: pass
json.dump({"fetched": len(notices), "notices": notices}, open(sys.argv[2], 'w'), ensure_ascii=False)
print(f"   -> {sys.argv[2]}: {len(notices)} notices")
PY
  rm -f "$out.tmp"
done
