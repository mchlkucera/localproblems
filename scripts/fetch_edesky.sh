#!/usr/bin/env bash
# fetch_edesky.sh — eDesky.cz municipal noticeboard `záměr` documents -> the
# asks ledger.
#
# ══ WHAT THIS FEED IS ════════════════════════════════════════════════════════
# A Czech municipality that means to ACQUIRE something — buy a plot,
# commission a plan, place a small-scale contract, carry out a project —
# posts that intention on its official noticeboard as a `záměr` before any
# tender exists. A named owner (the desk), a stated intention, sometimes a
# sum: an ASK (docs/superpowers/specs/2026-09-03-asks-ledger-design.md).
# eDesky.cz aggregates 6,346 noticeboards behind a keyed API
# (docs/sources-unconventional-2026-09-04.md §B). One record per document
# whose TITLE carries an intention to acquire.
#
# ══ THE TERMS — READ THIS BEFORE THE FIRST PUBLIC RUN ═════════════════════════
# The sign-up form (edesky.cz/uzivatel/sign_up, Wayback 2026-05-11) makes the
# registrant tick "Souhlasím se Všeobecnými obchodními podmínkami". Those
# terms (edesky.cz/vop, Wayback 2026-06-11; provider ADOL Monitor s.r.o.,
# IČO 02214377) say, in VI:
#   1.   data obtained from the service may not be passed to third parties,
#        paid or free; use is for the client's OWN purposes only;
#   4.e) the client may not PUBLISH the outputs (data) in any way, share
#        them, or otherwise let a third party use them;
#   4.g) nor include the service or its parts in own or third-party products;
#   5.   contractual penalty 100,000 CZK per breach;
#   6.   the provider may covertly watermark the data.
# A public, append-only register on GitHub IS publication. So this script
# REFUSES to write into data/raw/ until data/feeds.json carries an `edesky`
# row with `access.verdict: allowed` — which the orchestrator writes only on
# the strength of the provider's WRITTEN consent (VI.4 names written
# permission as the route; info@edesky.cz is the contact both the README and
# the /api page give). A private measurement run into a scratch directory
# ($TMPDIR/…) is VI.1 own-use and is allowed; nothing from it may be
# published. The gate reads the registry's own field rather than inventing
# one (CLAUDE.md: a rule enforced by prose is not enforced).
#
# ══ THE API, MEASURED FROM ITS ONLY SPECIFICATION ═════════════════════════════
# github.com/edesky/edesky_api — apiary.apib + documents.xsd (last commit
# 2017-01-29; the endpoint answered 401 "nepřihlášen, použijte svůj API klíč
# … edesky.cz/uzivatel/edit" on 2026-09-04, so it is alive). The site's own
# /api page sits behind an Anubis proof-of-work gate, and its 2025-11-15
# Wayback copy adds only "Jedná se o testovací provoz" — a beta.
#   GET /api/v1/documents?api_key=…&keywords=záměr&search_with=sql
#       &created_from=YYYY-MM-DD&include_texts=1&order=date&page=N
#   * `keywords` is REQUIRED and there is NO document-category filter — the
#     only category the API has is the DESK's (samosprava | instituce). So
#     the query is the word and the kind is read off the title, in
#     scripts/edesky_extract.py, both ways (§39 disposals, EIA notices and
#     permit proceedings dropped; pořídit / koupit / pronajmout / zadat /
#     realizovat kept), counted by reason.
#   * `search_with=sql` matches the word in the document NAME (a substring,
#     so záměru / záměry match too); `es` is fulltext with inflection and
#     would also return every document whose BODY mentions a záměr.
#   * `created_from` is when eDesky LOADED the document; 200 documents a
#     page; <meta><page total_pages=N> says how many pages exist.
#   * `include_texts=1` returns each attachment's OCR text, PERCENT-ENCODED.
#
# ══ THE KEY NEVER TRANSITS THIS SHELL ═════════════════════════════════════════
# The API takes the key as a QUERY PARAMETER — its design, not ours. So the
# fetch_hlidac.sh shape is used with --expand-url instead of --expand-header:
# `with-secrets` decrypts the vault and execs ONE allow-listed command; curl
# imports EDESKY_API_KEY itself with --variable and expands {{EDESKY_API_KEY}}
# into the URL, and -G appends the --data-urlencode parameters after it
# (measured 2026-09-05 with a placeholder: `…?api_key=<v>&keywords=z%c3%a1m
# %c4%9br&search_with=sql&…`). No process we control ever holds the value.
# The -w receipt deliberately carries NO %{url_effective}. And because the
# API ECHOES the key and the registrant's mailbox back in <meta> (measured on
# the published 2015 sample), the downloaded body is REDACTED by the guard
# before it is stored under .fetch/, and the un-redacted download is
# truncated the moment the guard returns — refused bodies included.
#
# ══ RATE ═════════════════════════════════════════════════════════════════════
# edesky.cz/robots.txt disallows only /attachments/ (never fetched here) and
# sets `Request-rate: 10/10s` for Seznambot only. VOP VI.4(d) forbids
# deliberately overloading the portal. EDESKY_DELAY seconds between pages,
# default 2; a 14-day window is a handful of pages.
#
# Usage: scripts/fetch_edesky.sh [outdir]          <-- outdir is $1
#   EDESKY_DAYS=14         window: documents loaded in the last N days
#   EDESKY_SINCE=DATE      explicit created_from (overrides EDESKY_DAYS)
#   EDESKY_KEYWORDS=záměr  the search word
#   EDESKY_SEARCH_WITH=sql sql (word in the NAME) | es (fulltext, inflected)
#   EDESKY_PAGES=10        page cap (200 documents a page; a smoke run sets 1)
#   EDESKY_DELAY=2         seconds between page requests
set -uo pipefail   # no -e: one failed page must not kill the walk
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/.." && pwd -P)"
EXTRACT="$HERE/edesky_extract.py"
FEEDS="$REPO/data/feeds.json"

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

command -v jq >/dev/null 2>&1 || { echo "fetch_edesky: jq is required" >&2; exit 2; }
[ -f "$EXTRACT" ] || { echo "fetch_edesky: $EXTRACT missing" >&2; exit 2; }

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
DAYS="${EDESKY_DAYS:-14}"
SINCE="${EDESKY_SINCE:-$(date -v-"${DAYS}"d +%Y-%m-%d 2>/dev/null || date -d "$DAYS days ago" +%Y-%m-%d)}"

# ── ACCESS GATE ── the terms, enforced ───────────────────────────────────────
# data/raw/ is the public path: what lands there is normalized, appended to a
# public ledger and deployed. The registry's own `access.verdict` for this
# feed decides whether that is permitted (see the header); anything but
# `allowed` refuses the public path and leaves a manifest row, so db.py
# health shows the feed BLOCKED rather than silent. A scratch outdir is a
# private measurement run and passes with a banner.
VERDICT=""
[ -f "$FEEDS" ] && VERDICT="$(jq -r '.feeds[] | select(.key=="edesky") | (.access.verdict // "unset")' "$FEEDS" 2>/dev/null | head -1)"
[ -n "$VERDICT" ] || VERDICT="unregistered"
PUBLIC=0
case "$(cd "$OUTDIR" && pwd -P)" in "$REPO/data/raw"|"$REPO/data/raw/"*) PUBLIC=1 ;; esac
if [ "$PUBLIC" -eq 1 ] && [ "$VERDICT" != "allowed" ]; then
  mf edesky error 000 0 0 0 "$STARTED" "" \
     "blocked by the provider's terms: edesky.cz VOP VI.1 and VI.4(e) forbid passing on or publishing API output; data/feeds.json access.verdict for edesky is '$VERDICT', not 'allowed' (needs the provider's written consent). A private measurement run into a scratch outdir is VOP VI.1 own-use and still permitted."
  echo "BLOCKED: data/feeds.json access.verdict for 'edesky' is '$VERDICT' — the public path" >&2
  echo "         data/raw/ needs 'allowed', recorded on the provider's WRITTEN consent." >&2
  echo "         See the header of this script. A run into \$TMPDIR/… is still allowed." >&2
  exit 1
fi
if [ "$VERDICT" != "allowed" ]; then
  echo "== access: verdict '$VERDICT' — PRIVATE measurement run (VOP VI.1 own-use);"
  echo "   nothing under $OUTDIR may be published or appended to a ledger."
fi

# ── SECRET HANDLING ── the fetch_hlidac.sh shape, --expand-url variant ───────
# The probe is fetch_hlidac.sh's token_present(), verbatim in doctrine: it
# reads curl's MESSAGE, not its exit code, and names each outcome by its own
# evidence. 'lpnoscheme://' is an unsupported protocol ON PURPOSE — curl
# parses options and expands variables BEFORE touching the network, so
# presence resolves with ZERO transmission of the secret to anywhere.
#   "variable expansion failure" -> the name is genuinely not in the vault
#   "not supported"              -> expansion SUCCEEDED, then curl rejected
#                                   the bogus scheme: the name exists
#   anything else                -> INCONCLUSIVE, reported as such
# DELIBERATELY NO -f ON THIS ONE CURL: it never makes a request, so -f
# cannot change any outcome. Every curl that fetches a payload carries -f.
token_present() { # NAME -> 0 only on POSITIVE EVIDENCE the vault holds it.
  probe_out="$(with-secrets --dir "$REPO" -- curl -sS --variable "%$1" \
                 --expand-header "H: {{$1}}" 'lpnoscheme://x' 2>&1)"
  case "$probe_out" in
    *"variable expansion failure"*) return 1 ;;
    *"not supported"*)              return 0 ;;
    *) PROBE_BROKEN=1
       echo "== auth probe INCONCLUSIVE for \$$1: with-secrets never reached curl." >&2
       echo "   Not evidence of absence — the probe itself did not run." >&2
       return 1 ;;
  esac
}

TOKEN_VAR=""
PROBE_BROKEN=0
if command -v with-secrets >/dev/null 2>&1; then
  if token_present EDESKY_API_KEY; then TOKEN_VAR="EDESKY_API_KEY"; fi
else
  PROBE_BROKEN=1
  echo "== with-secrets is not on PATH — no authenticated call is possible." >&2
fi

if [ -z "$TOKEN_VAR" ]; then
  # Fails LOUDLY instead of storing the API's 401 text as a payload, and
  # leaves a manifest row so a blocked feed is visible to db.py health. The
  # two causes stay apart: "no key" is an owner action, "the probe could not
  # run" is an environment one.
  if [ "$PROBE_BROKEN" -eq 1 ]; then
    mf edesky error 000 0 0 0 "$STARTED" "" \
       "auth probe could not run: with-secrets never reached curl (sandboxed shell, locked vault or wrong --dir). Key presence UNKNOWN, not absent."
    echo "FAILED: could not probe the vault at all — key presence is UNKNOWN." >&2
  else
    mf edesky error 000 0 0 0 "$STARTED" "" \
       "no eDesky key in the vault: EDESKY_API_KEY fails curl variable expansion"
    echo "FAILED: EDESKY_API_KEY is not in the sops vault." >&2
    echo "        A human registers at https://edesky.cz/uzivatel/sign_up (e-mail, password," >&2
    echo "        VOP checkbox; the site is behind a bot-check gate), copies the key from" >&2
    echo "        https://edesky.cz/uzivatel/edit, then: sops-edit .env.enc" >&2
  fi
  exit 1
fi
echo "== auth: using \$$TOKEN_VAR via with-secrets (value never enters this shell)"

API="${EDESKY_API:-https://edesky.cz/api/v1/documents}"
KEYWORDS="${EDESKY_KEYWORDS:-záměr}"
SEARCH_WITH="${EDESKY_SEARCH_WITH:-sql}"
PAGES="${EDESKY_PAGES:-10}"
PAGE_SIZE=200          # apiary.apib: "každá stránka má 200 dokumentů"
DELAY="${EDESKY_DELAY:-2}"

OUT="$OUTDIR/edesky-zamery.jsonl"
# RAW (redacted) page bodies live under .fetch/ — NOT in the outdir root.
# normalize.py groups every file carrying the feed's filename token into ONE
# feed and parses them all with the same contract, so .xml beside the .jsonl
# would be a parse violation. `edesky` is the token to register; see the
# note at the bottom.
RAWD="$OUTDIR/.fetch/edesky"; mkdir -p "$RAWD"

TOT_BYTES=0; TOT_MS=0; LAST_CODE=000; ERRS=""
FETCHED=0; HITS=0; MODEA=0; DOCS=0; API_TOTAL=0; TOTAL_PAGES=1
TMPD="${TMPDIR:-/tmp}/edesky.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT
GOOD="$TMPD/good.list"; : > "$GOOD"

echo "== edesky: documents loaded since $SINCE whose name carries '$KEYWORDS' ($SEARCH_WITH), up to $PAGES page(s) of $PAGE_SIZE"

# ── THE WALK ─────────────────────────────────────────────────────────────────
p=1
while [ "$p" -le "$PAGES" ]; do
  tmp="$TMPD/page-$p.xml"; raw="$RAWD/edesky-documents-p$p.xml"
  [ "$p" -eq 1 ] || sleep "$DELAY"
  # -f stops a 4xx/5xx body being stored; the explicit 200 test below is not
  # redundant with it (a 302 passes -f untouched — the Hlídač receipt).
  # `--expand-url` carries the key; `-G` appends the parameters after it.
  parse_w "$(with-secrets --dir "$REPO" -- curl -fsSG -m 120 --retry 2 --retry-delay 5 \
                  -A "$UA" \
                  --variable "%$TOKEN_VAR" \
                  --expand-url "$API?api_key={{$TOKEN_VAR}}" \
                  --data-urlencode "keywords=$KEYWORDS" \
                  --data-urlencode "search_with=$SEARCH_WITH" \
                  --data-urlencode "created_from=$SINCE" \
                  --data-urlencode "include_texts=1" \
                  --data-urlencode "order=date" \
                  --data-urlencode "page=$p" \
                  -o "$tmp" --remove-on-error \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' 2>/dev/null || true)"
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS)); FETCHED=$((FETCHED + 1))

  if [ "$W_CODE" != "200" ]; then
    case "$W_CODE" in
      401) echo "FAILED p$p (HTTP 401) — the key was rejected: wrong value, or the account lapsed" ;;
      *)   echo "FAILED p$p (HTTP $W_CODE)" ;;
    esac
    ERRS="$ERRS p$p:HTTP-$W_CODE"; : > "$tmp"; break
  fi
  # ── REDACT, THEN MODE-A GUARD ── the guard writes the stored copy FIRST,
  # registrant and key blanked, whatever the body is; then it refuses an
  # Anubis page, the API's own error text, JSON, a foreign XML or a body
  # with no <documents>. The refused body stays under .fetch/ (redacted) as
  # evidence and is NEVER handed to the fold. Either way the un-redacted
  # download is truncated here and now.
  g="$(python3 "$EXTRACT" guard "$tmp" --redact-to "$raw" 2>&1)"; rc=$?
  : > "$tmp"
  if [ "$rc" -ne 0 ]; then
    echo "REFUSED p$p — MODE-A: $g"
    echo "        first 120 bytes (redacted copy): $(head -c 120 "$raw" | tr -d '\n')"
    MODEA=$((MODEA + 1)); ERRS="$ERRS p$p:mode-a"; break
  fi
  HITS=$((HITS + 1)); TOT_BYTES=$((TOT_BYTES + W_BYTES))
  printf '%s\n' "$raw" >> "$GOOD"
  # '<page>\t<total_pages>\t<count on disk>\t<api total>' — what LANDED and
  # what the API says exists, kept apart (the fetch_hlidac.sh lesson).
  IFS=$'\t' read -r g_page g_tp g_count g_total <<EOF
$g
EOF
  case "$g_count" in ''|*[!0-9]*) g_count=0 ;; esac
  case "$g_tp" in ''|*[!0-9]*) g_tp=1 ;; esac
  case "$g_total" in ''|*[!0-9]*) g_total=0 ;; esac
  DOCS=$((DOCS + g_count)); API_TOTAL="$g_total"; TOTAL_PAGES="$g_tp"
  echo "OK  p$p: +$g_count document(s) on disk (api total $g_total, page ${g_page:-?} of $g_tp)  ($W_BYTES bytes)"
  # Stop on a short page (the set ended) or once the last page is read —
  # both avoid spending a request on a page we already know is empty.
  if [ "$g_count" -lt "$PAGE_SIZE" ]; then break; fi
  if [ "$p" -ge "$g_tp" ]; then break; fi
  p=$((p + 1))
done

COVER=""
if [ "$TOTAL_PAGES" -gt "$PAGES" ] && [ "$API_TOTAL" -gt "$DOCS" ]; then
  COVER="coverage: $DOCS of $API_TOTAL available (page cap EDESKY_PAGES=$PAGES x $PAGE_SIZE)"
fi

# ── MECHANICAL EXTRACTION -> one JSONL payload ───────────────────────────────
# Only bodies that passed their guard are handed over, BY LIST FILE (a path
# with a space in it survives). The title rules, the text bar and the owner
# gate live in the extractor and are counted BY REASON — a bare total would
# say "most vanished" and not why; on this feed most DO vanish (§39
# disposals), and the reasons are the measurement.
N=0; DROPPED=0
if [ -s "$GOOD" ]; then
  if summary="$(python3 "$EXTRACT" fold --out "$TMPD/rows.jsonl" --paths-from "$GOOD" 2>&1)"; then
    jf() { printf '%s' "$summary" | jq -r "$1"; }
    N="$(jf .kept)"; DROPPED="$(jf .dropped)"
    echo "    extracted: $(jf .pages) guarded page(s), $(jf .documents) document(s) -> $N ask(s) from $(jf .owners) desk(s);" \
         "$DROPPED dropped, $(jf .duplicates) duplicate(s), $(jf .no_ico) without an IČO"
    jf '.kept_by_intent | to_entries[] | "      kept \(.value)× \(.key)"'
    jf '.dropped_by_reason | to_entries[] | "      dropped \(.value)× \(.key)"'
    jf '.dropped_detail[] | "        " + .'
  else
    echo "    extract failed: $summary"; ERRS="$ERRS extract:python-failed"
  fi
fi
case "$N" in ''|*[!0-9]*) N=0 ;; esac
if [ "$N" -gt 0 ]; then mv "$TMPD/rows.jsonl" "$OUT"; fi

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
echo "== edesky: $FETCHED page request(s) — $HITS accepted, $MODEA refused;" \
     "$DOCS document(s) on disk of $API_TOTAL available -> $N ask(s), $DROPPED dropped"
if [ "$N" -eq 0 ]; then
  # Bytes that arrived and yielded nothing is the yield=zero anomaly — an
  # error, so the feed cannot read LIVE while landing nothing. Zero matches
  # over 6,346 desks in a 14-day window is not an expected absence either:
  # it means the search changed under us.
  mf edesky error "$LAST_CODE" "$TOT_BYTES" 0 "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: zero asks from $DOCS document(s) on $HITS page(s)${ERRS:+ —$ERRS}${COVER:+ · $COVER}"
  exit 1
elif [ -n "$ERRS" ]; then
  mf edesky ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS${COVER:+ · $COVER}"
else
  # An `ok` row may still carry a coverage note: the run succeeded AND
  # under-fetched; both facts survive.
  mf edesky ok "$LAST_CODE" "$TOT_BYTES" "$N" "$TOT_MS" "$STARTED" "$OUTDIR" "$COVER"
fi
echo "    wrote $OUT"
exit 0

# ── FOR THE ORCHESTRATOR: THE FILENAME TOKEN, THE ENUM, THE VERDICT ──────────
# The payload is `edesky-zamery.jsonl`. normalize.py's FILE_FEED_TOKENS is
# FIRST-MATCH-WINS; checked 2026-09-05 (and proven in the feed's selftest):
# the name contains NONE of the existing tokens (hlidac, smlouvy, czechcrunch,
# cc-cz, vestbee, suggest, shoptet, upgates, veklep, tacr, hack, nenptk, nku,
# sukl, mpsv, ares, coi, hys, nen, ted, yc) nor a reddit marker, no other
# fetcher writes a filename containing `edesky`, and the raw bodies live
# under .fetch/ where the payload scan cannot see them — so ("edesky",
# "edesky") can be appended anywhere. Extractor: edesky_extract.extract_edesky
# under key "edesky". `source: edesky` is a NEW PUBLISHER and must be added to
# SignalSchema.source (web/lib/data.ts) in a commit BEFORE the first record
# lands (CONVENTIONS.md). And the data/feeds.json row's `access.verdict` is
# what this script gates on — see the header before setting it to `allowed`.
