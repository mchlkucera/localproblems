#!/usr/bin/env bash
# fetch_reddit.sh — Reddit demand search via RSS (CZ subreddits). No auth.
# Ported from the demand-signals project; REWORKED 2026-08-15: Reddit now 403s
# all public .json endpoints regardless of UA, but .rss serves fine with a
# descriptive UA. Rate limit is tight (~1 req then 429) — curl --retry with a
# 35s delay honors it; keep sleeps generous.
# Usage: scripts/fetch_reddit.sh [outdir]
set -uo pipefail   # no -e: one failed fetch must not kill the rest

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/sources/$TODAY}"
mkdir -p "$OUTDIR"
UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

SUBS="czech Brno Prague czechia"
QUERIES="nefunguje|problém|byrokracie|proč neexistuje"

rfetch() { # outfile url
  code="$(curl -s -m 60 --retry 3 --retry-delay 35 -A "$UA" -o "$OUTDIR/$1" -w '%{http_code}' "$2")"
  if [ "$code" = "200" ]; then
    echo "OK  $1 ($(wc -c < "$OUTDIR/$1" | tr -d ' ') bytes)"
  else
    echo "FAILED $1 (HTTP $code)"
  fi
  sleep 10
}

for sub in $SUBS; do
  rfetch "reddit-$sub-new.rss" "https://www.reddit.com/r/$sub/new.rss"
  echo "$QUERIES" | tr '|' '\n' | while IFS= read -r q; do
    enc="$(printf '%s' "$q" | jq -sRr @uri)"
    rfetch "reddit-$sub-q-$(printf '%s' "$q" | tr ' ' '_' | tr -cd '[:alnum:]_').rss" \
      "https://www.reddit.com/r/$sub/search.rss?q=$enc&restrict_sr=1&sort=new&t=year"
  done
done
