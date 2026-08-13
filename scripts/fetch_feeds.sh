#!/usr/bin/env bash
# fetch_feeds.sh — RSS + yc-oss fetches. No auth.
# Usage: scripts/fetch_feeds.sh [outdir]
set -uo pipefail   # no -e: one failed feed must not kill the rest

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/sources/$TODAY}"
mkdir -p "$OUTDIR"

fetch() { # name url
  if curl -sL -m 60 "$2" -o "$OUTDIR/$1"; then
    echo "OK  $1 ($(wc -c < "$OUTDIR/$1" | tr -d ' ') bytes)"
  else
    echo "FAILED $1 <- $2"
  fi
}

fetch feed-czechcrunch.xml "https://cc.cz/feed/"
fetch feed-vestbee.xml     "https://www.vestbee.com/blog/rss.xml"
fetch yc-all.json          "https://raw.githubusercontent.com/yc-oss/api/main/companies/all.json"
