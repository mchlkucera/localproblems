#!/usr/bin/env bash
# fetch_hlidac.sh — Hlídač státu API (smlouvy + VZ). Needs HLIDAC_TOKEN env var.
# Usage: scripts/fetch_hlidac.sh [outdir]
set -euo pipefail

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/sources/$TODAY}"
mkdir -p "$OUTDIR"

HLIDAC_TOKEN="${HLIDAC_TOKEN:-${HLIDAC_STATU_TOKEN:-}}"
if [ -z "$HLIDAC_TOKEN" ]; then
  echo "FAILED: HLIDAC_TOKEN / HLIDAC_STATU_TOKEN not set (get a free key at hlidacstatu.cz/api)" >&2
  exit 1
fi

# recent large IT contracts (smlouvy) — icoPlatce filter left broad, sorted new-first
curl -s -m 60 "https://api.hlidacstatu.cz/api/v2/smlouvy/hledat?dotaz=oblast:it%20AND%20cenaSDph:%3E5000000&razeni=2&strana=1" \
  -H "Authorization: Token $HLIDAC_TOKEN" > "$OUTDIR/hlidac-smlouvy-it.json"
echo "-> $OUTDIR/hlidac-smlouvy-it.json"
