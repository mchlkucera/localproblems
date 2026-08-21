#!/usr/bin/env bash
# fetch_smlouvy.sh — registr smluv, the OFFICIAL bulk dump. No auth, no key.
#
# Usage: scripts/fetch_smlouvy.sh [YYYY-MM-DD-since] [outdir]
#   ARGV SHAPE: $1 = SINCE (ISO date), $2 = outdir.
#   This is the ted/hlidac/nen shape ($1 SINCE, $2 outdir), NOT the
#   feeds/suggest/reddit/nku shape ($1 outdir). Declared here because
#   fetch_all.sh REFUSES a key with no declared argv shape, and because a
#   dispatcher that guesses hands this script a directory path as its
#   since-date and gets a silently wrong window back (§5.3).
#
# ══ WHY THIS SOURCE EXISTS ALONGSIDE hlidac ══════════════════════════════════
# We already fetch registr smluv THROUGH Hlídač státu. This fetches it from the
# publisher. Three measured reasons, 2026-08-21:
#
#  1. BOTH PARTIES, IN THE PAYLOAD. Every <zaznam> carries <subjekt> (the public
#     body that published it) AND <smluvniStrana> (the counterparty), each with
#     an <ico>. Census over one full daily dump (dump_2026_08_19.xml, 4,026
#     contracts): buyer IČO on 99.9%, counterparty IČO on 97.2%, checksum-valid
#     on 96.3%, and BOTH SIDES RESOLVED ON 97.1%. That is the entity graph.
#  2. NO LICENCE STRINGS. Hlídač's free tier is CC BY 3.0 with mandatory
#     attribution and withheld endpoints. This is the state's own open data.
#  3. NO PAGE CAP. Hlídač's API page is FIXED AT 25 and fetch_hlidac.sh caps at
#     4 pages x 25 = 100 contracts per query, so it sees a few hundred contracts
#     a run against a corpus of thousands a DAY. One dump file is the whole day.
#
# It does NOT replace hlidac: Hlídač adds full-text search, classification and
# `issues` flags this dump has none of. This gets coverage; that gets judgement.
#
# ══ THE TWO FAILURE MODES, AND THE SEPARATE GUARD FOR EACH ═══════════════════
# MODE A — good transfer, wrong body. Guarded by THE PUBLISHER'S OWN SHA1. The
#   index at https://data.smlouvy.gov.cz/ ships <hashDumpu algoritmus="sha1">
#   and <velikostDumpu> for every dump it lists. We verify both after download.
#   VERIFIED 2026-08-21: dump_2026_08_19.xml, published sha1
#   ea70711268d85b070d9d7a02daa90414e62c6da4, 5,010,141 bytes — byte-exact
#   match. This is a NATIVE source contract, not a shape heuristic: a proxy
#   error page, a truncated transfer and a silently-regenerated file are all
#   caught, and none of them would fail a "does it look like XML" check.
# MODE B — silent absence. Guarded by THE INDEX ITSELF, which is the list of
#   what SHOULD exist. A date inside the requested window that the index lists
#   and we produced no records for is reported as an anomaly on the manifest
#   row; the health view reads it from there. A shape contract cannot see this
#   and the hash cannot either — a file that was never fetched has no bytes to
#   check.
# Neither guard substitutes for the other. The hash proves the bytes we got are
# the bytes they published; the index proves we asked for every day we should.
#
# ══ EXPECTED ABSENCE IS NOT FAILURE ══════════════════════════════════════════
# The publisher lags. MEASURED on 2026-08-21 the newest daily dump was
# 2026-08-19 — today's file does not exist yet, and neither did yesterday's. A
# window whose days are all still unpublished exits `skipped` (ok=1,
# parse_method=none), which must NOT move the feed toward BROKEN (§7.2 step 0).
# A fetcher that called that an error would cry wolf every single run.
set -uo pipefail   # no -e: one bad day must not kill the rest of the window
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
SINCE="${1:-$(date -v-3d +%Y-%m-%d 2>/dev/null || date -d '3 days ago' +%Y-%m-%d)}"
OUTDIR="${2:-data/raw/$TODAY}"
CACHE="${SMLOUVY_CACHE:-data/raw/.cache}"
INDEX_URL="https://data.smlouvy.gov.cz/"
FEED_KEY="smlouvy"
MAX_DAYS="${SMLOUVY_MAX_DAYS:-7}"   # a real cap, reported when it bites
mkdir -p "$OUTDIR" "$CACHE"

TMPD="${TMPDIR:-/tmp}/smlouvy.$$"
mkdir -p "$TMPD"

# ── run manifest ── identical schema to scripts/fetch_ted.sh ─────────────────
# One appended row per REGISTRY FEED KEY per run; columns map 1:1 onto the
# fetch_log DDL (docs/architecture-v3.md §2.3).
#   result=ok      -> fetch_log.ok = 1
#   result=skipped -> fetch_log.ok = 1, parse_method='none'. EXPECTED ABSENCE.
#   result=error   -> fetch_log.ok = 0, `error` non-empty.
MANIFEST="$OUTDIR/manifest.md"
RUN_ID="${RUN_ID:-$(date -u +%Y-%m-%dT%H%M)}"
mf() { # feed_key result http bytes items ms started_at raw_path error
  if [ ! -f "$MANIFEST" ]; then
    { printf '# run manifest — %s\n\n' "$TODAY"
      printf 'Fetch-side rows consumed by `python3 scripts/db.py fetchlog data/raw/%s`.\n' "$TODAY"
      printf 'Columns map 1:1 onto the `fetch_log` DDL (docs/architecture-v3.md §2.3).\n'
      printf '`result`: `ok` (ok=1) · `skipped` (ok=1, parse_method=none — expected absence,\n'
      printf '§7.2 step 0, never counts as a failure) · `error` (ok=0).\n\n'
      printf '| run_id | feed_key | result | http | bytes | items | ms | started_at | raw_path | error |\n'
      printf '|---|---|---|---|---|---|---|---|---|---|\n'
    } > "$MANIFEST"
  fi
  printf '| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n' \
    "$RUN_ID" "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" \
    "$(printf '%s' "${9:-}" | tr '\n|' '  ' | cut -c1-200)" >> "$MANIFEST"

  # ── the MACHINE seam ── <raw>/.fetch/receipts.jsonl ────────────────────────
  # The true status code, byte count and transfer time exist ONLY here, at fetch
  # time. normalize.py must never infer them (it once synthesized
  # `http_status = 200 if nbytes > 0`, which cannot tell a 404 from a 403 from a
  # feed that never ran). Field names are exactly db.py's FETCHLOG_FIELDS.
  # Lives in a SUBDIRECTORY so normalize.py's isfile-only payload scan cannot
  # mistake it for a feed payload.
  if command -v jq >/dev/null 2>&1; then
    mkdir -p "$OUTDIR/.fetch"
    jq -nc --arg run_id "$RUN_ID" --arg feed_key "$1" --arg result "$2" \
           --arg http "$3" --arg bytes "$4" --arg items "$5" --arg ms "$6" \
           --arg started "$7" --arg raw "$8" --arg err "${9:-}" \
      '{run_id:$run_id, feed_key:$feed_key, started_at:$started,
        finished_at:(now|todateiso8601),
        http_status:(if ($http|length)==0 or $http=="000" then null else ($http|tonumber) end),
        bytes:(if ($bytes|length)==0 then null else ($bytes|tonumber) end),
        items_fetched:(if ($items|length)==0 then null else ($items|tonumber) end),
        items_kept:null,
        yield_anomaly:null,
        parse_method:(if $result=="skipped" then "none" else null end),
        runtime_ms:(if ($ms|length)==0 then null else ($ms|tonumber) end),
        ok:(if $result=="error" then 0 else 1 end),
        error:(if ($err|length)==0 then null else $err end),
        raw_path:(if ($raw|length)==0 then null else $raw end),
        result:$result}' >> "$OUTDIR/.fetch/receipts.jsonl" 2>/dev/null
  fi
}

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS.
# `set --` rebinds only THIS function's positional params, so callers are safe.
parse_w() { # "<http_code> <size_download> <time_total>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
TOT_ITEMS=0; TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""; NOTES=""

# ── 1. the index, CONDITIONAL ── a quiet day costs one request ───────────────
# ~1.2 MB and regenerated only when a dump is (re)built, so If-None-Match is
# worth a round trip. -f is kept for >=400; 304 is tested explicitly because -f
# would turn a 304 into a failure and 304 is the SUCCESS case here.
IDX="$TMPD/index.xml"
ETAG_F="$CACHE/smlouvy-index.etag"
COND=""
[ -f "$ETAG_F" ] && COND="$(cat "$ETAG_F" 2>/dev/null)"
parse_w "$(curl -fsSL -m 120 --retry 3 --retry-delay 5 \
                ${COND:+-H "If-None-Match: $COND"} \
                -o "$IDX" --remove-on-error -D "$TMPD/index.h" \
                -w '%{http_code} %{size_download} %{time_total}' \
                "$INDEX_URL" 2>/dev/null || true)"
LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

if [ "$W_CODE" = "304" ]; then
  # The index is byte-identical to last run: no dump has been (re)generated, so
  # there is genuinely nothing new to fetch. ok=1, parse_method=none.
  echo "== smlouvy: index 304 Not Modified — no new or regenerated dump since last run."
  mf "$FEED_KEY" skipped 304 0 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "304 Not Modified (If-None-Match) on the dump index"
  exit 0
fi
# THE `code = 200` TEST IS NOT REDUNDANT WITH -f. --fail only trips at HTTP>=400,
# so a 3xx served as the terminal response passes -f untouched — which is exactly
# how a login/interstitial page gets stored as a payload (§7.1 receipt 2).
if [ "$W_CODE" != "200" ]; then
  echo "== smlouvy: index FAILED (HTTP $W_CODE)"
  mf "$FEED_KEY" error "$W_CODE" 0 0 "$TOT_MS" "$STARTED" "$OUTDIR" "index:HTTP-$W_CODE"
  exit 1
fi
TOT_BYTES=$((TOT_BYTES + W_BYTES))
grep -i '^etag:' "$TMPD/index.h" 2>/dev/null | tail -1 | tr -d '\r' | awk '{print $2}' > "$ETAG_F" 2>/dev/null || true
echo "== smlouvy: index OK ($W_BYTES bytes)"

# ── 2. which daily dumps the index says exist inside our window ──────────────
# The index is NOT sorted by date (it groups by day-of-month across years), so
# this selects and sorts rather than tailing. Emits: date<TAB>url<TAB>sha1<TAB>bytes
python3 - "$IDX" "$SINCE" "$TODAY" "$MAX_DAYS" > "$TMPD/want.tsv" <<'PY' || ERRS="$ERRS index:unparseable"
import sys, xml.etree.ElementTree as ET
idx, since, today, cap = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
N = "{http://portal.gov.cz/rejstriky/ISRS/1.2/}"
root = ET.parse(idx).getroot()
rows = []
for d in root:
    den = d.findtext(N + "den")
    if den is None:            # a MONTHLY dump (72-110 MB). Never fetched here.
        continue
    iso = "%04d-%02d-%02d" % (int(d.findtext(N + "rok")), int(d.findtext(N + "mesic")), int(den))
    if since <= iso <= today:
        rows.append((iso, d.findtext(N + "odkaz") or "",
                     (d.findtext(N + "hashDumpu") or "").strip().lower(),
                     d.findtext(N + "velikostDumpu") or "0"))
rows.sort()
for r in rows[-cap:]:
    print("\t".join(r))
PY

WANT=$(grep -c . "$TMPD/want.tsv" 2>/dev/null || echo 0)
if [ "$WANT" -eq 0 ]; then
  # EXPECTED ABSENCE. The publisher lags by a day or two; a window of days it
  # has not published yet is not a fault, and calling it one would fire an alarm
  # on most runs forever (§7.2 step 0).
  echo "== smlouvy: index lists no daily dump in [$SINCE .. $TODAY] — nothing published yet."
  mf "$FEED_KEY" skipped "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "no daily dump published in window $SINCE..$TODAY (publisher lag)"
  exit 0
fi
echo "== smlouvy: $WANT daily dump(s) in [$SINCE .. $TODAY]"

# ── 3. fetch, VERIFY AGAINST THE PUBLISHER'S HASH, convert ───────────────────
# HERE-STRING, not `cat … | while`: a piped while runs in a SUBSHELL, so every
# total accumulated below would be discarded when the loop ended and the
# manifest row would always read 0 items. bash 3.2 has no `mapfile`.
MISSING=""
while IFS="$(printf '\t')" read -r dday durl dsha dsize; do
  [ -n "${dday:-}" ] || continue
  xmlf="$TMPD/dump-$dday.xml"
  out="$OUTDIR/smlouvy-$dday.jsonl"

  parse_w "$(curl -fsSL -m 300 --retry 3 --retry-delay 5 \
                  -o "$xmlf" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total}' \
                  "$durl" 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))
  if [ "$W_CODE" != "200" ]; then
    echo "   $dday: FAILED (HTTP $W_CODE)"
    ERRS="$ERRS $dday:HTTP-$W_CODE"; MISSING="$MISSING $dday"
    continue
  fi
  TOT_BYTES=$((TOT_BYTES + W_BYTES))

  # MODE A GUARD. The publisher signed these bytes; we check them. A mismatch
  # is an ERROR and the file is NOT converted — a wrong body that transferred
  # perfectly is the failure a status code can never show.
  got_sha="$(shasum -a 1 "$xmlf" 2>/dev/null | awk '{print $1}')"
  got_size="$(wc -c < "$xmlf" | tr -d ' ')"
  if [ -n "$dsha" ] && [ "$got_sha" != "$dsha" ]; then
    echo "   $dday: SHA1 MISMATCH (published $dsha, got $got_sha) — not converted"
    ERRS="$ERRS $dday:sha1-mismatch"; MISSING="$MISSING $dday"
    continue
  fi
  if [ "$dsize" != "0" ] && [ "$got_size" != "$dsize" ]; then
    echo "   $dday: SIZE MISMATCH (published $dsize, got $got_size) — not converted"
    ERRS="$ERRS $dday:size-mismatch"; MISSING="$MISSING $dday"
    continue
  fi

  # XML -> JSONL in the HLÍDAČ ITEM SHAPE, so scripts/normalize.py's existing
  # extract_hlidac reads it unchanged (EXTRACTORS maps `smlouvy` to it). This is
  # transformation, not judgement: no filtering, no scoring, no field invention.
  n=$(python3 - "$xmlf" "$out" <<'PY' || echo 0
import json, sys, xml.etree.ElementTree as ET
src, dst = sys.argv[1], sys.argv[2]
N = "{http://portal.gov.cz/rejstriky/ISRS/1.2/}"

def party(el):
    return {"nazev": (el.findtext(N + "nazev") or "").strip(),
            "ico": (el.findtext(N + "ico") or "").strip(),
            "datovaSchranka": (el.findtext(N + "datovaSchranka") or "").strip(),
            "adresa": (el.findtext(N + "adresa") or "").strip()}

n = 0
with open(dst, "w", encoding="utf-8") as fh:
    for _, z in ET.iterparse(src, events=("end",)):
        if z.tag != N + "zaznam":
            continue
        sm = z.find(N + "smlouva")
        if sm is None:
            z.clear(); continue
        # platnyZaznam=0 marks a record the publisher has INVALIDATED. Kept and
        # flagged rather than dropped: a withdrawn contract is a fact about the
        # buyer, and silently discarding it would make the dump's own count
        # disagree with ours for no recorded reason.
        ident = z.find(N + "identifikator")
        subs = sm.findall(N + "subjekt")
        item = {
            # `identifikator` as a dict is exactly what the Hlídač API returns
            # and what extract_hlidac's get_first/isinstance branch expects.
            "identifikator": {"idSmlouvy": (ident.findtext(N + "idSmlouvy") if ident is not None else "") or "",
                              "idVerze": (ident.findtext(N + "idVerze") if ident is not None else "") or ""},
            "odkaz": (z.findtext(N + "odkaz") or "").strip(),
            "predmet": (sm.findtext(N + "predmet") or "").strip(),
            "datumUzavreni": (sm.findtext(N + "datumUzavreni") or "").strip(),
            "cisloSmlouvy": (sm.findtext(N + "cisloSmlouvy") or "").strip(),
            "hodnotaBezDph": sm.findtext(N + "hodnotaBezDph"),
            "hodnotaVcetneDph": sm.findtext(N + "hodnotaVcetneDph"),
            "platnyZaznam": (z.findtext(N + "platnyZaznam") or "").strip(),
            "casZverejneni": (z.findtext(N + "casZverejneni") or "").strip(),
            # <subjekt> is the PUBLISHING public body (exactly one, on 4,026 of
            # 4,026 records measured) and <smluvniStrana> the counterparties
            # (1 on 96.8%, up to 6). They map onto platce/prijemce because that
            # is the same distinction registr smluv draws — NOT because the
            # payer flag says so: <platce> is ABSENT on 2,551 of 4,026 subjekt
            # elements and on ALL 4,169 smluvniStrana elements, so a fetcher
            # that keyed off it would mis-role two thirds of the corpus.
            "platce": party(subs[0]) if subs else None,
            "prijemce": [party(e) for e in sm.findall(N + "smluvniStrana")],
        }
        fh.write(json.dumps(item, ensure_ascii=False) + "\n")
        n += 1
        z.clear()
print(n)
PY
)
  case "$n" in ''|*[!0-9]*) n=0; ERRS="$ERRS $dday:convert-failed"; MISSING="$MISSING $dday" ;; esac
  echo "   $dday: $W_BYTES bytes, sha1 OK -> $out ($n contracts)"
  TOT_ITEMS=$((TOT_ITEMS + n))
  sleep 1
done < "$TMPD/want.tsv"

# MODE B GUARD, reported not inferred: days the index SAID exist that produced
# nothing. Silence is the failure a shape contract cannot see.
[ -n "$MISSING" ] && NOTES="index listed$MISSING but produced no records"
if [ "$WANT" -ge "$MAX_DAYS" ]; then
  NOTES="${NOTES:+$NOTES · }coverage: capped at $MAX_DAYS day(s) (SMLOUVY_MAX_DAYS)"
fi

if [ -n "$ERRS" ]; then
  mf "$FEED_KEY" error "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" \
     "day failures:$ERRS${NOTES:+ · $NOTES}"
else
  # An `ok` row can still carry a note: the run succeeded AND under-covered.
  mf "$FEED_KEY" ok "$LAST_CODE" "$TOT_BYTES" "$TOT_ITEMS" "$TOT_MS" "$STARTED" "$OUTDIR" "$NOTES"
fi
echo "== smlouvy: $TOT_ITEMS contracts from $WANT day(s), $TOT_BYTES bytes"
