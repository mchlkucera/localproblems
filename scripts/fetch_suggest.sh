#!/usr/bin/env bash
# fetch_suggest.sh — Google Suggest pain-miner (CZ). No auth.
# Ported from the demand-signals project (src/ingesters/google_suggest.py):
# feed pain-phrased prefixes, record the autocompletions — live consumer
# search pain the institutional demand sources (NKÚ, ombudsman, ČOI) can't see.
# Rate care: ~1 req/1.5s (the endpoint tolerates ~50/min).
# Usage: scripts/fetch_suggest.sh [outdir]
set -uo pipefail   # no -e: one failed query must not kill the rest

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/sources/$TODAY}"
mkdir -p "$OUTDIR"
OUT="$OUTDIR/suggest-pain.jsonl"
: > "$OUT"

# Register-adjacent CZ seeds (edit freely; keep the list boring and concrete).
SEEDS="datová schránka|stavební povolení|účetnictví|faktura|dotace|pojišťovna|banka|exekuce|energie|fotovoltaika|tepelné čerpadlo|e-shop|lékař|nemocnice|úřad|katastr|daňové přiznání|živnost|hypotéka|nájem|školka|důchod|recyklace|vodárna"

# Pain phrasings — the prefix IS the filter: complaints, failures, workarounds.
# (Lesson from demand-signals: pain language, never engagement metrics.)
PATTERNS="proč je %s tak|%s nefunguje|alternativa k %s|%s problém|jak zrušit %s|%s zkušenosti"

n=0
echo "$SEEDS" | tr '|' '\n' | while IFS= read -r seed; do
  echo "$PATTERNS" | tr '|' '\n' | while IFS= read -r pat; do
    q="$(printf "$pat" "$seed")"
    enc="$(printf '%s' "$q" | jq -sRr @uri)"
    resp="$(curl -s -m 20 "https://suggestqueries.google.com/complete/search?client=firefox&hl=cs&ie=utf-8&oe=utf-8&q=$enc")"
    if [ -n "$resp" ]; then
      printf '%s' "$resp" | jq -c --arg q "$q" --arg d "$TODAY" \
        '{query: $q, date: $d, completions: (.[1] // [])} | select(.completions | length > 0)' >> "$OUT" 2>/dev/null
      n=$((n+1))
    else
      echo "FAILED suggest: $q"
    fi
    sleep 1.5
  done
done

echo "OK  suggest-pain.jsonl ($(grep -c . "$OUT" | tr -d ' ') queries with completions)"
