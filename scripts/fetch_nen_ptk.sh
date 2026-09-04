#!/usr/bin/env bash
# fetch_nen_ptk.sh — NEN předběžné tržní konzultace -> the asks ledger.
#
# ══ WHAT THIS FEED IS ════════════════════════════════════════════════════════
# A Czech public buyer that cannot yet write a specification runs a market
# consultation (§33 ZZVZ): it publishes the need, names itself, and asks the
# market how the thing could be done — BEFORE the specification and before any
# money. A named owner, a stated problem, no budget: an ASK
# (docs/superpowers/specs/2026-09-03-asks-ledger-design.md). One record per
# NEN P-series procedure that IS a consultation.
#
# ══ WHY A COUNTER WALK AND NOT THE BULK, AND NOT THE LISTING ═════════════════
# Measured 2026-09-03 (route report):
#   * The ISVZ open-data ZIPs that scripts/fetch_nen.sh reads carry ZERO of
#     these — 0 `N006/YY/P…` ids in VZ-07-2026 and VZ-08-2026, and
#     `druh_zadavaciho_postupu` has no consultation value at all. The bulk is
#     not a slower route to this feed; it is not a route.
#   * The site's own listing is ordered by LAST publication, so a "stop when
#     older than SINCE" walk over it silently misses records.
#   * P-numbers ARE sequential per year (P00000001 on 2026-01-09 …
#     P00000205 on 2026-09-02, one gap). So the counter walk below is complete
#     by construction, and a missing number answers an honest HTTP 404 — no
#     login-page ambiguity to disentangle. ~25 P-records a month, ~20 of them
#     true consultations.
#
# ══ CRAWL DELAY: WE OBEY IT ══════════════════════════════════════════════════
# nen.nipez.cz/robots.txt sets `Crawl-delay: 10` for `User-agent: *`. That is
# the site's stated rate for everyone, we are everyone, so there is a `sleep 10`
# between EVERY request this script makes — detail pages and buyer pages alike.
# A full 2026 backfill is therefore ~50 minutes of mostly sleeping, and that is
# the correct cost. robots.txt also disallows `/file*`; the consultation's
# attachments live there and THIS SCRIPT NEVER FETCHES THEM. Document names
# would be nice; a disallowed path is not ours to take.
#
# ══ WHAT IS CUT, AND WHERE ═══════════════════════════════════════════════════
# The detail object carries a named civil servant with a work mailbox and a
# phone (osobaJmeno/Prijmeni/Email/Telefon/Mobil/Fax/Funkce/TitPred/TitZa/
# DalsiInfo). nen_ptk_extract.FIELDS is an ALLOWLIST over the meta JSON — a
# denylist over `osoba*` would protect us from the fields NEN ships today and
# fail silently on the one it ships next quarter. The buyer page is read for
# exactly one key, `ico`; it also holds a bank account and a second mailbox.
# Raw bodies stay under .fetch/ as MODE-A evidence (data/raw is gitignored and
# pruned at 28 days); only the allowlisted payload is durable.
#
# Both MODE-A guards, the drop rules and the fold live in
# scripts/nen_ptk_extract.py so nen_ptk_contract_selftest.py drives the SAME
# entry points this script does (the tacr/nen_extract shape).
#
# Usage: scripts/fetch_nen_ptk.sh [outdir] [year ...]   <-- outdir is $1
#   NENPTK_MAX=25   stop after N detail fetches (a smoke run; default: no cap)
#   NENPTK_START=1  first P-number to walk (default 1)
#   NENPTK_MISSES=5 consecutive 404s that end a year's walk (default 5)
set -uo pipefail   # no -e: one failed page must not kill the walk
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
shift 2>/dev/null || true
# Extra argv years, the fetch_nku.sh shape. Default is the CURRENT year only:
# P-numbers restart each January, so last year's walk is a backfill someone
# asks for, never a thing a weekly run should re-crawl at 10s a page.
YEARS="${*:-$(date +%Y)}"
HERE="$(cd "$(dirname "$0")" && pwd)"
EXTRACT="$HERE/nen_ptk_extract.py"

UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run; columns are the fetch-side
# half of the `fetch_log` schema (§2.3). Verbatim from fetch_nku.sh — the
# manifest is a cross-file contract, not a place for local taste.
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

  # ── the MACHINE seam ── <raw>/.fetch/receipts.jsonl ─────────────────────────
  # The true status, byte count and transfer time exist ONLY here, at fetch
  # time. Field names are db.py's FETCHLOG_FIELDS. Lives in a subdirectory so
  # normalize.py's payload scan (isfile only) can never mistake it for a feed.
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

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS / W_CT.
parse_w() { # "<http_code> <size_download> <time_total> <content_type>"
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_CT="${4:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

command -v jq >/dev/null 2>&1 || { echo "fetch_nen_ptk: jq is required" >&2; exit 2; }
[ -f "$EXTRACT" ] || { echo "fetch_nen_ptk: $EXTRACT missing" >&2; exit 2; }

BASE="${NENPTK_BASE:-https://nen.nipez.cz/verejne-zakazky/detail-zakazky}"
SUBJ_BASE="${NENPTK_SUBJ_BASE:-https://nen.nipez.cz/registr-zadavatelu/detail-subjektu}"
# robots.txt Crawl-delay for User-agent: * — see the header. Overridable only
# so the offline selftest and a rerun against cached bodies do not sleep.
DELAY="${NENPTK_DELAY:-10}"
MAX="${NENPTK_MAX:-0}"          # 0 = no cap; a smoke run sets e.g. 25
START="${NENPTK_START:-1}"
MISS_LIMIT="${NENPTK_MISSES:-5}"

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
OUT="$OUTDIR/nenptk-consultations.jsonl"
# RAW originals live under .fetch/ — NOT in the outdir root. normalize.py
# groups every file carrying the feed's filename token into ONE feed and parses
# them all with the same contract, so .html beside the .jsonl would be a parse
# violation. `nenptk` is the token to register; see the note at the bottom.
RAWD="$OUTDIR/.fetch/nenptk"; mkdir -p "$RAWD"

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""
PAGES=0; HITS=0; MISSES=0; MODEA=0; SUBJ_OK=0; SUBJ_FAIL=0
TMPD="${TMPDIR:-/tmp}/nenptk.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT
GOOD="$TMPD/good.list"; : > "$GOOD"
ICOMAP="$TMPD/icos.json"; printf '{}' > "$ICOMAP"

# One buyer is fetched ONCE per run. 21 distinct buyers over 32 sampled
# records, so the cache is most of the subject-page cost, and at 10s a request
# "most of" is minutes.
ico_of() { # zadavatelID -> echoes the IČO ("" when unresolved)
  sid="$1"
  case "$sid" in ''|*[!0-9]*) echo ""; return ;; esac
  # PRESENCE, not truthiness. An unresolvable buyer is cached as "" a few lines
  # below, and `.[$k] // ""` cannot tell that apart from "never seen" — so the
  # old truthiness test re-fetched the same broken page, at 10s a go, once per
  # record that buyer owns, while the comment claimed the opposite. `has($k)`
  # is the question actually being asked.
  if jq -e --arg k "$sid" 'has($k)' "$ICOMAP" >/dev/null 2>&1; then
    jq -r --arg k "$sid" '.[$k] // ""' "$ICOMAP" 2>/dev/null
    return
  fi
  sraw="$RAWD/nenptk-subjekt-$sid.html"
  sleep "$DELAY"
  parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -o "$sraw" \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                  "$SUBJ_BASE/$sid" 2>/dev/null || true)"
  TOT_MS=$((TOT_MS + W_MS))
  ico=""
  if [ "$W_CODE" = "200" ]; then
    TOT_BYTES=$((TOT_BYTES + W_BYTES))
    # MODE-A on the buyer page too: a 200 that is not a subject object yields
    # no IČO rather than a plausible-looking wrong one.
    ico="$(python3 "$EXTRACT" ico "$sraw" --sid "$sid" 2>/dev/null)"
    case "$ico" in CONTRACT*|*[!0-9]*) ico="" ;; esac
  fi
  if [ -n "$ico" ]; then SUBJ_OK=$((SUBJ_OK + 1)); else SUBJ_FAIL=$((SUBJ_FAIL + 1)); fi
  jq -c --arg k "$sid" --arg v "$ico" '. + {($k): $v}' "$ICOMAP" > "$ICOMAP.n" 2>/dev/null \
    && mv "$ICOMAP.n" "$ICOMAP"
  echo "$ico"
}

# ── THE WALK ─────────────────────────────────────────────────────────────────
for year in $YEARS; do
  case "$year" in ''|*[!0-9]*) echo "skip non-numeric year '$year'"; continue ;; esac
  yy="$(printf '%s' "$year" | tail -c 3)"; yy="${yy#"${yy%??}"}"   # 2026 -> 26
  n="$START"; miss=0
  echo "== walking N006-$yy-P… from $(printf 'P%08d' "$n") (stop after $MISS_LIMIT consecutive 404s)"
  while [ "$miss" -lt "$MISS_LIMIT" ]; do
    if [ "$MAX" -gt 0 ] && [ "$PAGES" -ge "$MAX" ]; then
      echo "   NENPTK_MAX=$MAX reached — stopping the walk early (smoke run)"
      break
    fi
    p="$(printf 'P%08d' "$n")"; ref="N006-$yy-$p"; kod="N006/$yy/$p"
    raw="$RAWD/nenptk-$ref.html"
    [ "$PAGES" -eq 0 ] || sleep "$DELAY"   # robots.txt Crawl-delay: 10
    parse_w "$(curl -fsSL -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                    -A "$UA" -o "$raw" \
                    -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                    "$BASE/$ref" 2>/dev/null || true)"
    LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS)); PAGES=$((PAGES + 1))
    n=$((n + 1))

    if [ "$W_CODE" = "404" ]; then
      # An honest absence: the number was never assigned, or the year is done.
      miss=$((miss + 1)); MISSES=$((MISSES + 1)); continue
    fi
    if [ "$W_CODE" != "200" ]; then
      echo "FAILED $ref (HTTP $W_CODE)"; ERRS="$ERRS $ref:HTTP-$W_CODE"; miss=0; continue
    fi
    # ── MODE-A GUARD ── a login page, a maintenance notice or the shell NEN
    # serves for a nonexistent number all arrive as HTML; the last one even
    # carries an initialReduxState meta with `object: null`. Stored as a
    # payload any of them would read as a healthy empty record. The guard wants
    # the meta, the "Druh zadávacího postupu" tile, and an object whose `kod`
    # is the one we asked for. The refused body stays under .fetch/ as evidence
    # and is NEVER handed to the fold.
    if ! g="$(python3 "$EXTRACT" guard "$raw" --kod "$kod" 2>&1)"; then
      echo "REFUSED $ref — MODE-A: $g"
      echo "        first 120 bytes: $(head -c 120 "$raw" | tr -d '\n')"
      MODEA=$((MODEA + 1)); ERRS="$ERRS $ref:mode-a"; miss=0; continue
    fi
    miss=0; HITS=$((HITS + 1)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
    printf '%s\n' "$raw" >> "$GOOD"
    echo "OK  $ref  $(printf '%s' "$g" | tr '\t' ' ')  ($W_BYTES bytes)"

    # The IČO hop, once per buyer. Done inside the walk (not after it) so the
    # cache is warm for the next record of the same buyer and a partial run
    # still resolves what it fetched.
    sid="$(python3 "$EXTRACT" buyer "$raw" 2>/dev/null)"
    case "$sid" in ''|CONTRACT*|*[!0-9]*) ;; *) ico_of "$sid" >/dev/null ;; esac
  done
done

# ── MECHANICAL EXTRACTION -> one JSONL payload ───────────────────────────────
# Only bodies that passed their guard are handed over. The drop rules
# (`Průzkum trhu` is a price check, not a consultation; a popis under
# MIN_POPIS states no need; no buyer means no owner) live in the extractor and
# are counted BY REASON — a bare total would say "a fifth vanished" and not why.
N=0; DROPPED=0
if [ -s "$GOOD" ]; then
  # The guarded bodies are handed over BY LIST FILE, not by word-splitting
  # `$(cat …)`: $OUTDIR is argv, a smoke run may well point it at a path with a
  # space in it, and an unquoted expansion would silently split one body into
  # two nonexistent paths.
  if summary="$(python3 "$EXTRACT" fold --out "$TMPD/rows.jsonl" \
                  --ico-map "$ICOMAP" --paths-from "$GOOD" 2>&1)"; then
    jf() { printf '%s' "$summary" | jq -r "$1"; }
    N="$(jf .consultations)"; DROPPED="$(jf .dropped)"
    echo "    extracted: $(jf .pages) guarded page(s) -> $N consultation(s) from $(jf .buyers) buyer(s);" \
         "$DROPPED dropped, $(jf .no_ico) without an IČO"
    jf '.dropped_by_reason | to_entries[] | "      dropped \(.value)× \(.key)"'
    jf '.dropped_detail[] | "        " + .'
  else
    echo "    extract failed: $summary"; ERRS="$ERRS extract:python-failed"
  fi
fi
case "$N" in ''|*[!0-9]*) N=0 ;; esac
if [ "$N" -gt 0 ]; then mv "$TMPD/rows.jsonl" "$OUT"; fi

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
echo "== nen-ptk: $PAGES page(s) walked — $HITS detail(s), $MISSES 404(s), $MODEA refused;" \
     "buyers resolved $SUBJ_OK ok / $SUBJ_FAIL unresolved -> $N consultation(s), $DROPPED dropped"
if [ "$N" -eq 0 ]; then
  if [ "$HITS" -eq 0 ] && [ "$MODEA" -eq 0 ] && [ -z "$ERRS" ]; then
    # Every number 404'd and nothing else went wrong. On 2 January that is the
    # honest state of the world, not a broken feed: the year's counter has not
    # started. §7.2 step 0 — an expected absence, which must not move the feed
    # toward BROKEN.
    mf nen-ptk skipped "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
       "no P-record published yet this year ($MISSES consecutive 404s)"
    echo "    nothing published yet — expected absence, not a failure"
    exit 0
  fi
  # Bytes that arrived and yielded nothing is the yield=zero anomaly — an
  # error, so the feed cannot read LIVE while landing nothing.
  mf nen-ptk error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: zero consultations from $HITS detail page(s)${ERRS:+ —$ERRS}"
  exit 1
elif [ -n "$ERRS" ]; then
  mf nen-ptk ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf nen-ptk ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT"
exit 0

# ── FOR THE ORCHESTRATOR: THE FILENAME TOKEN ─────────────────────────────────
# The payload is `nenptk-consultations.jsonl`. normalize.py's FILE_FEED_TOKENS
# is FIRST-MATCH-WINS, and this name CONTAINS the existing `nen` token — so
# ("nenptk", "nen-ptk") MUST be registered ABOVE ("nen", "nen"), or every row
# of this feed is parsed under the bulk NEN contract and filed against the
# wrong registry row. Checked 2026-09-03: `nenptk-consultations.jsonl` matches
# none of the tokens listed above `nen` (hlidac, smlouvy, czechcrunch, cc-cz,
# vestbee, suggest, shoptet, upgates, veklep, tacr, hack, nku, sukl, mpsv,
# ares, coi, hys), and the raw bodies live under .fetch/ where the payload scan
# cannot see them.
