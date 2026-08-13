#!/usr/bin/env bash
# fetch_hlidac.sh — Hlídač státu smlouvy API (registr smluv; catches sub-TED-threshold contracts).
# Needs HLIDAC_TOKEN or HLIDAC_STATU_TOKEN in env (run via: direnv exec . scripts/fetch_hlidac.sh).
# Usage: scripts/fetch_hlidac.sh [YYYY-MM-DD-since] [outdir]
set -euo pipefail

SINCE="${1:-$(date -v-70d +%Y-%m-%d 2>/dev/null || date -d '70 days ago' +%Y-%m-%d)}"
TODAY="$(date +%Y-%m-%d)"
OUTDIR="${2:-data/sources/$TODAY}"
mkdir -p "$OUTDIR"

HLIDAC_TOKEN="${HLIDAC_TOKEN:-${HLIDAC_STATU_TOKEN:-}}"
if [ -z "$HLIDAC_TOKEN" ]; then
  echo "FAILED: HLIDAC_TOKEN / HLIDAC_STATU_TOKEN not set (get a free key at hlidacstatu.cz/api)" >&2
  exit 1
fi

API="https://api.hlidacstatu.cz/api/v2/smlouvy/hledat"

# bash 3.2 compatible: "key|query" pairs; date-range keeps results current
QUERIES='nis2|"kybernetická bezpečnost"
energycom|"komunitní energetika" OR "energetické společenství"
stavebni|"portál stavebníka" OR "stavební řízení"
ehealth|"nemocniční informační systém" OR ehealth
watermeter|"smart metering" OR "chytré vodoměry" OR vodoměrů
eudi|"digitální identita" OR edoklady
it-large|oblast:it AND cenaSDph:>10000000'

echo "$QUERIES" | while IFS='|' read -r key q; do
  full="($q) AND datumUzavreni:[$SINCE TO *]"
  out="$OUTDIR/hlidac-$key.json"
  curl -sG -m 60 "$API" \
    --data-urlencode "dotaz=$full" \
    --data-urlencode "razeni=0" \
    --data-urlencode "strana=1" \
    -H "Authorization: Token $HLIDAC_TOKEN" > "$out"
  n=$(python3 -c "import json;d=json.load(open('$out'));print(d.get('total','ERR'))" 2>/dev/null || echo PARSE-ERR)
  echo "== $key: total $n -> $out"
  sleep 3   # free-tier rate limit
done
