#!/usr/bin/env bash
# fetch_ec_hys.sh — EC "Have Your Say": initiatives currently OPEN for feedback.
#
# WHY THIS FEED. A Commission initiative open for feedback is the earliest
# public moment of a regulatory wave: the problem statement is published, the
# act type is declared, and the closing date is a hard deadline. That is a
# top-down demand signal with a date attached.
#
# ── THE URL IN THE REGISTRY IS WRONG, AND IT IS WRONG IN THE MODE-A WAY ──────
# data/feeds.json currently points ec-hys at
#     https://ec.europa.eu/info/law/better-regulation/api/groupInitiatives
# MEASURED 2026-08-21 from the real network path:
#     HTTP 200 · 3,956 bytes · content-type text/html;charset=UTF-8
#     body = `<!doctype html>` … `<title>Have your say</title>`
# That is the SPA shell, not an API. A fetcher that trusted the status code
# would have stored a 4 KB HTML page as a JSON feed payload every day and
# reported success — the §7.1 Mode-A failure, the same shape as the Vestbee
# 404-saved-as-a-feed bug. The `api/` path segment is not an API.
#
# The real declared interface is `brpapi/` (the portal's own backend):
#     https://ec.europa.eu/info/law/better-regulation/brpapi/searchInitiatives
#     -> 200 · application/json · {"initiativeResultDtoPage":{"content":[…]}}
# It is a versioned, declared JSON interface with server-side paging, which is
# why it is preferred over scraping the rendered portal (the tradeoff the owner
# asked for: the JSON is stable and self-describing; the HTML is neither).
#
# ── TRANSPORT NOTE: THIS HOST NEEDS THE REAL NETWORK PATH ────────────────────
# Under the sandbox proxy ec.europa.eu fails at TLS, not at HTTP:
#     curl: (60) SSL certificate problem: unable to get local issuer certificate
# That is a LOCAL interception fact, NOT a remote refusal — the same request
# unsandboxed returns 200. The script distinguishes the two explicitly below,
# because recording a sandbox artefact as a site blocking us would retire a
# working source. Registry `runner` stays `cloud` for this reason.
#
# Usage: scripts/fetch_ec_hys.sh [outdir]           <-- outdir is $1 (see §5.3)
set -uo pipefail
export LC_NUMERIC=C   # curl's %{time_total} must use '.' whatever the locale

TODAY="$(date +%Y-%m-%d)"
OUTDIR="${1:-data/raw/$TODAY}"
mkdir -p "$OUTDIR"
UA="localproblems-register/1.0 (public register of local problems; contact: corrections@localproblems.org)"

API="${EC_HYS_API:-https://ec.europa.eu/info/law/better-regulation/brpapi}"
# ── ASK THE SERVER FOR THE FILTER, DON'T FILTER 4,097 ROWS CLIENT-SIDE ───────
# MEASURED which query params this endpoint actually honours, because guessing
# is how a filter silently becomes a no-op:
#     feedbackStatus=OPEN            -> totalElements 45   HONOURED
#     receivingFeedbackStatus=OPEN   -> totalElements 4097 IGNORED
#     initiativeStatus=ACTIVE        -> totalElements 4097 IGNORED
#     topic=CLIMA                    -> totalElements 210  honoured
#     sort=startDate,DESC            -> HTTP 406
# A param the server ignores returns a full, healthy-looking 200 — so the
# client-side OPEN check below is KEPT as a cross-check even though the server
# filter works. If the two ever disagree, the run says so instead of quietly
# widening. (They agreed exactly on 2026-08-21: 45 and 45.)
FILTER="${EC_HYS_FILTER:-&feedbackStatus=OPEN}"
# MEASURED: `size` is capped server-side at 100 regardless of what is asked
# (size=100/200/300 all return exactly 100). So paging is the only way to go
# deeper, and PAGES is the knob — not size. With the OPEN filter the whole set
# is 45, so one page suffices; a second page is cheap insurance against growth.
PAGES="${EC_HYS_PAGES:-2}"
# Enrich each open initiative with its `dossierSummary` (the actual problem
# statement) from brpapi/groupInitiatives/<id>. Best-effort by design: a failed
# detail call costs that record its summary, never the run.
DETAIL="${EC_HYS_DETAIL:-1}"

# ── run manifest ── docs/architecture-v3.md §7.2 / §7.5 ──────────────────────
# One appended row per REGISTRY FEED KEY per run. Columns map 1:1 onto the
# `fetch_log` DDL (§2.3); `db.py fetchlog <dir>` reads this table and
# normalize.py fills items_kept / yield_anomaly / parse_method afterwards.
#   result=ok      -> fetch_log.ok = 1
#   result=skipped -> fetch_log.ok = 1, parse_method='none' (expected absence)
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

  # ── the MACHINE seam ── <raw>/.fetch/receipts.jsonl ─────────────────────────
  # normalize.py cannot reconstruct a status code after the fact; the true
  # status, byte count and transfer time exist ONLY here, at fetch time. Field
  # names are exactly db.py's FETCHLOG_FIELDS so no translation is needed.
  # Lives in a SUBDIRECTORY so normalize.py's payload scan (isfile only) can
  # never mistake it for a feed payload.
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

# Parse curl's -w receipt into W_CODE / W_BYTES / W_SECS / W_MS / W_CT / W_EXIT.
parse_w() { # "<http_code> <size_download> <time_total> <content_type>" <exit>
  set -- ${1:-}
  W_CODE="${1:-000}"; W_BYTES="${2:-0}"; W_SECS="${3:-0}"; W_CT="${4:-}"
  W_MS="$(awk -v s="$W_SECS" 'BEGIN{printf "%d", s*1000}')"
}

command -v jq >/dev/null 2>&1 || { echo "fetch_ec_hys: jq is required" >&2; exit 2; }

STARTED="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
OUT="$OUTDIR/ec-hys-initiatives.jsonl"
TMPD="${TMPDIR:-/tmp}/echys.$$"; mkdir -p "$TMPD"
cleanup() { [ -d "$TMPD" ] && find "$TMPD" -type f -delete 2>/dev/null; rmdir "$TMPD" 2>/dev/null; }
trap cleanup EXIT

TOT_BYTES=0; TOT_MS=0; FETCHED=0; LAST_CODE=000; ERRS=""; PAGES_OK=0
: > "$TMPD/all.json"

p=0
while [ "$p" -lt "$PAGES" ]; do
  body="$TMPD/page-$p.json"
  url="$API/searchInitiatives?page=$p&size=100&language=EN$FILTER"
  # -f keeps a >=400 BODY off disk; --remove-on-error clears partials. The
  # explicit `code = 200` test below is NOT redundant with -f: --fail only
  # trips at >= 400, so a 3xx that lands bytes still needs catching.
  W_EXIT=0
  parse_w "$(curl -fsS -m 60 --retry 2 --retry-delay 5 --remove-on-error \
                  -A "$UA" -H 'Accept: application/json' -o "$body" \
                  -w '%{http_code} %{size_download} %{time_total} %{content_type}' \
                  "$url" 2>"$TMPD/err-$p.txt")" || W_EXIT=$?
  LAST_CODE="$W_CODE"; TOT_MS=$((TOT_MS + W_MS))

  # ── TLS INTERCEPTION vs REMOTE REFUSAL — these are different facts ─────────
  # curl exit 60 is a certificate-chain failure in OUR path, so the request
  # never reached the Commission. Saying "ec.europa.eu blocked us" here would
  # be a fabricated remote fact.
  if [ "$W_EXIT" = "60" ]; then
    echo "FAILED page $p — curl exit 60: TLS interception on the LOCAL path (sandbox proxy)."
    echo "       This is NOT a refusal by ec.europa.eu. Re-run from the real network path."
    ERRS="$ERRS page$p:tls-intercept-local-exit60"
    break
  fi
  if [ "$W_CODE" != "200" ]; then
    echo "FAILED page $p (HTTP $W_CODE, curl exit $W_EXIT)"
    ERRS="$ERRS page$p:HTTP-$W_CODE"
    break
  fi

  # ── MODE-A GUARD ── a good transfer carrying the wrong body ───────────────
  # This is the whole reason this fetcher exists: the registry's own URL
  # answers 200 with an HTML SPA shell. Two independent assertions, because
  # either alone is defeatable — a JSON content-type on an error document, or
  # a valid JSON body that is not this resource.
  case "$W_CT" in
    *json*) : ;;
    *) echo "FAILED page $p — MODE-A: HTTP 200 but content-type '$W_CT', expected JSON."
       echo "       first 120 bytes: $(head -c 120 "$body" | tr -d '\n')"
       ERRS="$ERRS page$p:mode-a-content-type-$W_CT"
       break ;;
  esac
  if ! jq -e 'has("initiativeResultDtoPage")
              and (.initiativeResultDtoPage.content | type == "array")' \
        "$body" >/dev/null 2>&1; then
    echo "FAILED page $p — MODE-A: 200 + JSON, but no .initiativeResultDtoPage.content[] array."
    echo "       first 200 bytes: $(head -c 200 "$body" | tr -d '\n')"
    ERRS="$ERRS page$p:mode-a-shape"
    break
  fi

  n=$(jq '.initiativeResultDtoPage.content | length' "$body")
  TOT_BYTES=$((TOT_BYTES + W_BYTES)); FETCHED=$((FETCHED + n)); PAGES_OK=$((PAGES_OK + 1))
  jq -c '.initiativeResultDtoPage.content[]' "$body" >> "$TMPD/all.json"
  echo "OK  page $p: $n initiatives ($W_BYTES bytes)"
  [ "$n" -lt 100 ] && { p=$((p + 1)); break; }
  p=$((p + 1))
  sleep 1
done

# ── SELECTION ── open-for-feedback only, flattened to one line per initiative.
# `currentStatuses` is an ARRAY: an initiative can carry several stages, so the
# OPEN one is selected explicitly rather than assuming index 0.
# The Czech SHORT_TITLE is carried when the API ships one — this is a Czech
# register, and the EU publishes the translation itself, so taking it is free
# and strictly better than translating downstream.
jq -c '
  . as $i
  | ($i.currentStatuses // [] | map(select(.receivingFeedbackStatus == "OPEN")) | first) as $st
  | select($st != null)
  | ($i.initiativeTranslations // []
     | map(select(.field == "SHORT_TITLE" and .language == "CS")) | first | .value) as $cs
  | {
      initiative_id: ($i.id | floor | tostring),
      reference:     ($i.reference // ""),
      title:         ($i.shortTitle // ""),
      title_cs:      ($cs // ""),
      link:          ("https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/"
                      + ($i.id | floor | tostring)),
      act_type:      ($i.foreseenActType // ""),
      status:        ($i.initiativeStatus // ""),
      stage:         ($st.frontEndStage // ""),
      feedback_start:($st.feedbackStartDate // ""),
      feedback_end:  ($st.feedbackEndDate // ""),
      topics:        ([$i.topics // [] | .[] | .label] | join("; ")),
      topic_codes:   ([$i.topics // [] | .[] | .code] | join(";")),
      summary:       ""
    }
' "$TMPD/all.json" 2>/dev/null | jq -sc 'unique_by(.initiative_id) | .[]' > "$TMPD/open.jsonl" 2>/dev/null
KEPT=$(wc -l < "$TMPD/open.jsonl" 2>/dev/null | tr -d ' '); [ -n "$KEPT" ] || KEPT=0

# ── best-effort enrichment: the problem statement itself ─────────────────────
# `dossierSummary` is what makes this a problem signal rather than a title. A
# detail failure degrades ONE record's summary and is never allowed to fail the
# run, so these calls are deliberately outside the transport assertions above.
DET_OK=0; DET_FAIL=0
if [ "$DETAIL" = "1" ] && [ "$KEPT" -gt 0 ]; then
  : > "$TMPD/enriched.jsonl"
  while IFS= read -r line; do
    [ -n "$line" ] || continue
    iid=$(printf '%s' "$line" | jq -r '.initiative_id')
    dcode=$(curl -fsS -m 30 -A "$UA" -H 'Accept: application/json' \
                 -o "$TMPD/det.json" --remove-on-error \
                 -w '%{http_code}' "$API/groupInitiatives/$iid" 2>/dev/null || true)
    if [ "$dcode" = "200" ] && jq -e 'type=="object"' "$TMPD/det.json" >/dev/null 2>&1; then
      s=$(jq -r '(.dossierSummary // "") | gsub("<[^>]*>"; " ") | gsub("\\s+"; " ")' "$TMPD/det.json" 2>/dev/null)
      printf '%s' "$line" | jq -c --arg s "${s:0:1200}" '.summary = $s' >> "$TMPD/enriched.jsonl"
      DET_OK=$((DET_OK + 1))
    else
      printf '%s\n' "$line" >> "$TMPD/enriched.jsonl"
      DET_FAIL=$((DET_FAIL + 1))
    fi
    sleep 0.2
  done < "$TMPD/open.jsonl"
  mv "$TMPD/enriched.jsonl" "$TMPD/open.jsonl"
  echo "    detail: $DET_OK enriched, $DET_FAIL without summary (best-effort)"
fi

if [ "$KEPT" -gt 0 ]; then
  mv "$TMPD/open.jsonl" "$OUT"
fi

# ── SERVER FILTER vs CLIENT CHECK — disagreement is a finding, not noise ─────
# If the server filter silently stops working, FETCHED balloons to the whole
# corpus while KEPT stays honest. Saying so is the only way that drift is ever
# noticed; a filter that quietly becomes a no-op still returns a clean 200.
if [ "$FETCHED" -gt 0 ] && [ "$KEPT" -ne "$FETCHED" ]; then
  echo "    NOTE: server returned $FETCHED with feedbackStatus=OPEN but only $KEPT are"
  echo "          actually OPEN client-side — the server filter may have drifted."
  ERRS="$ERRS filter-drift:$FETCHED-vs-$KEPT"
fi

# ── ITEMS FETCHED vs ITEMS KEPT — a zero-yield run must be LOUD ──────────────
echo "== ec-hys: fetched $FETCHED initiatives over $PAGES_OK page(s) -> kept $KEPT open for feedback"
if [ -n "$ERRS" ] && [ "$KEPT" -eq 0 ]; then
  mf ec-hys error "$LAST_CODE" "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" "no records:$ERRS"
  exit 1
elif [ "$FETCHED" -gt 0 ] && [ "$KEPT" -eq 0 ]; then
  # A 200 that parsed cleanly and still selected nothing is the yield=zero
  # anomaly, not a success. It is reported as an error so the feed cannot read
  # LIVE while landing nothing.
  mf ec-hys error "$LAST_CODE" "$TOT_BYTES" "$FETCHED" "$TOT_MS" "$STARTED" "$OUTDIR" \
     "yield: $FETCHED initiatives fetched, 0 open for feedback"
  exit 1
elif [ -n "$ERRS" ]; then
  mf ec-hys ok "$LAST_CODE" "$TOT_BYTES" "$KEPT" "$TOT_MS" "$STARTED" "$OUTDIR" "partial:$ERRS"
else
  mf ec-hys ok "$LAST_CODE" "$TOT_BYTES" "$KEPT" "$TOT_MS" "$STARTED" "$OUTDIR" ""
fi
echo "    wrote $OUT"
