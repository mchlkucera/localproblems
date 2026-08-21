#!/usr/bin/env python3
"""
nen_sukl_coi_stage_preview.py — run the REAL mechanical normalize over `nen` and
`sukl` payloads and show exactly what would be staged, WITHOUT touching any
shared file.

WHY THIS EXISTS RATHER THAN JUST RUNNING normalize.py
=====================================================
Three other workers are in this repo. `data/feeds.json` is shared, and a record
whose id prefix has no registry row FAILS the build. So this worker may not edit
`data/feeds.json` and may not edit `scripts/normalize.py`. But "the fetcher runs"
is a much weaker claim than "records reach the ledger" — and the gap between
those two is the named failure this project keeps rediscovering
(`SCRIPTED-SILENT`: five feeds whose scripts ran clean and whose output went
nowhere for weeks).

So this harness closes that gap without landing anything. It:

  1. builds an IN-MEMORY registry — the committed data/feeds.json with the two
     PROPOSED rows below merged over the current `nen` / `sukl` entries — and
     points normalize.FEEDS_JSON at a temp copy of it;
  2. registers `extract_nen` / `extract_sukl` into normalize.EXTRACTORS, which is
     the two-line hand-off diff scripts/normalize.py needs;
  3. runs normalize.run_mechanical() — the actual function, not a reimplementation
     — over a raw dir, into a SCRATCH copy so nothing under data/raw/ is written;
  4. prints items_fetched vs items_kept per feed, and sample staged records.

If step 2 is skipped (`--no-extractors`) it also demonstrates the failure mode:
normalize.py:962 does `if not extractor: break`, silently, so the run reports a
clean contract, a real items_fetched and items_kept = 0.

    python3 scripts/nen_sukl_coi_stage_preview.py --raw <dir>
    python3 scripts/nen_sukl_coi_stage_preview.py --raw <dir> --no-extractors
    python3 scripts/nen_sukl_coi_stage_preview.py --print-rows
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
from types import SimpleNamespace

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import normalize      # noqa: E402
import coi_extract    # noqa: E402
import nen_extract    # noqa: E402
import sukl_extract   # noqa: E402


# ==========================================================================
# THE PROPOSED data/feeds.json ROWS — the hand-off artefact.
# ==========================================================================
#
# These are merged over the committed `nen` and `sukl` entries by key. They are
# kept HERE, as the literal object this preview actually runs against, so that
# what gets merged into the shared registry is the same bytes that were proved
# to work — not a transcription of them.
#
# WHAT CHANGED FROM THE COMMITTED ROWS, AND WHY, FIELD BY FIELD:
#
#  nen.script          null -> scripts/fetch_nen.sh
#  nen.url             the HTML listing -> the open-data bulk file we actually
#                      read. `url` should name the thing the fetcher requests.
#  nen.contract.parse  html-table -> json. This is the CONSEQUENCE of choosing
#                      the open-data interface: there is no HTML to parse and
#                      therefore no LLM-fallback path to design around.
#  nen.required_fields ["datumPrvniUver"] -> the keys our payload really carries.
#                      `datumPrvniUver` was a URL MATRIX PARAMETER of the listing,
#                      not a field of any document — feeds-status.md §5 flags it:
#                      "a naive field check will fail on a healthy payload".
#  nen.expected_yield  UNMEASURED estimate -> measured on two real months.
#  nen.allow_missing   false -> true. The file for month M is published on the
#                      5th of M+1, so the newest month in any window legitimately
#                      404s. Without this the feed reads BROKEN for the first
#                      days of every month.
#  nen.access          unknown -> allowed, with the licence actually read.
#  nen.signal_source   stays `nen` (already correct) — see the source note below.
#
#  sukl.script         null -> scripts/fetch_sukl.sh
#  sukl.runner         cloud -> local. Nothing about this needs a cloud runner;
#                      it is a 1.6 MB unauthenticated GET.
#  sukl.contract.parse csv -> json. The raw member is CP1250 and ;-delimited;
#                      normalize.py's csv branch is UTF-8 and comma-delimited and
#                      would "succeed" into one garbage column per row. The
#                      fetcher decodes and AGGREGATES, and hands over JSON.
#  sukl.required_fields [] -> the aggregate keys, now measured rather than guessed.
#  sukl.expected_yield UNMEASURED -> measured: 15 aggregates on 2026-08-21.
#  sukl.signal_source  demand-scan -> sukl. See the source note below.
#
# THE `source` VALUE — the question the brief asks explicitly.
#
#   nen  -> "nen".  The 296 existing `nen-*` records carry `source: "hlidac"`,
#           which is a real attribution defect (feeds-status.md §6.2: `hlidac`
#           holds 463 records from THREE unrelated provenances, over-crediting
#           the one auth-blocked feed 4x). It is not retro-fixed here — the
#           ledgers are append-only — but new records must not extend it.
#   sukl -> "sukl". The 4 existing `sukl-*` records carry `source: "demand-scan"`,
#           which is honest for an agent harvest and wrong for a scripted feed:
#           `demand-scan` is explicitly "~12 different sites" of manual research,
#           and folding an automated feed into it means feed health can never see
#           this feed fail. Same defect as `hlidac`, one feed earlier.
#
#   BLOCKED ON A ONE-LINE SCHEMA EDIT, AND IT IS BUILD-ENFORCED:
#   web/lib/data.ts:95 declares `source` as a z.enum(["ted","hlidac","yc",
#   "round","reg-scan","arb-scan","feed","demand-scan","suggest","reddit","mpsv"])
#   — neither "nen" nor "sukl" is in it, so appending such a record RED-BUILDS
#   immediately. That is CONVENTIONS.md's step 6 working as designed. The enum
#   edit must land in the same change as the first append; until it does, nothing
#   from these feeds may be appended.
#
#   coi  -> "coi". There is NO `coi` registry row today: ČOI is catalog entry #5
#           with 3 `coi-*` records already sitting inside the `demand-scan`
#           harvest, where no feed-health check can see them (feeds-status.md
#           §6.1). This row creates the key, so step 2 of CONVENTIONS.md's
#           "adding an evidence type" checklist — every `source` in
#           data/signals/** must be claimed by a registry entry — is satisfied
#           BEFORE the first scripted append rather than after.
PROPOSED_ROWS = {
    "coi": {
        "key": "coi",
        "name": "ČOI — consumer-protection enforcement",
        "yields": ("Half-yearly aggregates of legally-final fines levied by the Czech Trade "
                   "Inspection Authority, split by the act breached: fine count, total value, "
                   "distinct businesses fined, top paragraphs, regional spread, and growth "
                   "against both the previous half-year and the year-ago half."),
        "role": "feed",
        "signal_source": "coi",
        "id_prefixes": ["coi"],
        "evidence_type": "demand",
        "cadence": "quarterly",
        "runner": "local",
        "url": "https://coi.gov.cz/userdata/files/dokumenty-ke-stazeni/open-data/sankce.csv",
        "script": "scripts/fetch_coi.sh",
        "status": "planned",
        "blocker": ("Fetcher exists (scripts/fetch_coi.sh, $1=SINCE ISO date, $2=outdir). Stays "
                    "`planned` until it lands a record, because status is INTENT and "
                    "PENDING/LIVE in feed_health.json is the observed half. THREE HAND-OFFS "
                    "REMAIN: (1) scripts/normalize.py FILE_FEED_TOKENS has no \"coi\" entry, so "
                    "coi-*.json is an UNMAPPED payload parsed by nobody; (2) EXTRACTORS has no "
                    "\"coi\" key and `if not extractor: break` is silent, so the feed would run "
                    "clean at items_kept 0 forever — map it to coi_extract.extract_coi; "
                    "(3) web/lib/data.ts SignalSchema `source` enum must gain \"coi\" or the "
                    "first append red-builds. Also needs an argv case in scripts/fetch_all.sh."),
        "last_known_good": None,
        "access": {
            "verdict": "allowed",
            "basis": ("ČOI has published these datasets under an explicit open licence since "
                      "27 October 2013 and links the licence from the dataset index. Plain "
                      "unauthenticated GET, 200 to a descriptive User-Agent, ETag and "
                      "Last-Modified served."),
            "checked": "2026-08-21",
        },
        "contract": {
            "parse": "json",
            "required_fields": ["zakon", "period", "fines", "czk_total"],
            "expected_yield": {
                "min": 5,
                "max": 40,
                "basis": ("MEASURED 2026-08-21: 176,945 sanction rows joined to 288,962 "
                          "inspection rows aggregate to 32 items over an 18-month window "
                          "(16 acts x 2 completed half-years). The grain is (act x half-year) "
                          "and NOT one row per fine, because the MEDIAN fine is 3,000 CZK "
                          "(~EUR 120) — money 0, urgency 0, scale 0 — so a per-fine feed would "
                          "carry 176,945 items and write approximately none of them while the "
                          "manifest read green (CONVENTIONS.md, the `hiring` trap). Bounded "
                          "above by ~16 acts with real volume x the number of completed "
                          "half-years in the window, so this range is structural. Counts "
                          "items_fetched."),
            },
            "allow_missing": False,
        },
    },
    "nen": {
        "key": "nen",
        "name": "NEN — below-threshold tenders (via ISVZ open data)",
        "yields": ("Czech public contracts under the TED threshold — small-scale (VZMR) and "
                   "below-threshold procedures from the National Electronic Tool, with buyer "
                   "IČO, CPV, NUTS, estimated value and, once awarded, the contract price and "
                   "the winning supplier."),
        "role": "feed",
        "signal_source": "nen",
        "id_prefixes": ["nen"],
        "evidence_type": "tenders",
        "cadence": "monthly",
        "runner": "local",
        "url": "https://isvz.nipez.cz/sites/default/files/content/opendata-rvz/VZ-MM-YYYY.zip",
        "script": "scripts/fetch_nen.sh",
        "status": "planned",
        "blocker": ("Fetcher exists (scripts/fetch_nen.sh, $1=SINCE ISO date, $2=outdir). Stays "
                    "`planned` until it lands a record, because status is INTENT and "
                    "PENDING/LIVE in feed_health.json is the observed half. TWO HAND-OFFS "
                    "REMAIN: (1) scripts/normalize.py maps \"nen\" to extract_hlidac, which "
                    "stamps hlidac- ids and source hlidac — it must map to "
                    "nen_extract.extract_nen; (2) web/lib/data.ts SignalSchema `source` enum "
                    "must gain \"nen\" or the first append red-builds. Also needs an argv case "
                    "in scripts/fetch_all.sh, which refuses unknown keys by design."),
        "last_known_good": None,
        "access": {
            "verdict": "allowed",
            "basis": ("Open data published by the Ministry for Regional Development (MMR) from "
                      "the Registr veřejných zakázek, with a named open-data curator and a "
                      "versioned public JSON schema (dokumentace 2.10.1). No auth, no rate "
                      "terms, no robots restriction — a bulk file offered for download."),
            "checked": "2026-08-21",
        },
        "contract": {
            "parse": "json",
            "required_fields": ["nen_kod", "nazev", "zadavatel", "datum_zahajeni"],
            "expected_yield": {
                "min": 100,
                "max": 8000,
                "basis": ("MEASURED 2026-08-21 on two real monthly files, not estimated. "
                          "VZ-07-2026: 33,855 contracts in file, 20,286 carrying a NEN "
                          "identifier, 3,868 below-threshold with a procedure started on or "
                          "after 2026-06-01. VZ-06-2026: 16,662 in file, 574 selected on the "
                          "same window. The spread is the changefeed's own shape — an older "
                          "month has had fewer of its recent procedures touched — so the range "
                          "is wide on purpose. Counts items_fetched. Replace with a rolling "
                          "median once six fetch_log runs exist."),
            },
            "allow_missing": True,
        },
    },
    "sukl": {
        "key": "sukl",
        "name": "SÚKL — medicine supply interruptions",
        "yields": ("Monthly aggregates over the state medicines agency's supply-notification "
                   "register: how many medicine presentations have interrupted supply right "
                   "now by ATC anatomical group, how many carry no promised restock date, the "
                   "manufacturers' stated reasons, and permanent market exits per month."),
        "role": "feed",
        "signal_source": "sukl",
        "id_prefixes": ["sukl"],
        "evidence_type": "demand",
        "cadence": "daily",
        "runner": "local",
        "url": "https://opendata.sukl.cz/soubory/MR/mr.zip",
        "script": "scripts/fetch_sukl.sh",
        "status": "planned",
        "blocker": ("Fetcher exists (scripts/fetch_sukl.sh, $1=outdir, no since-date — the "
                    "source is a full snapshot). Stays `planned` until it lands a record. TWO "
                    "HAND-OFFS REMAIN: (1) scripts/normalize.py has NO \"sukl\" key in "
                    "EXTRACTORS, and `if not extractor: break` is silent — the feed would run "
                    "clean at items_kept 0 forever; it must map to "
                    "sukl_extract.extract_sukl; (2) web/lib/data.ts SignalSchema `source` enum "
                    "must gain \"sukl\". Also needs an argv case in scripts/fetch_all.sh."),
        "last_known_good": None,
        "access": {
            "verdict": "allowed",
            "basis": ("Published open data of a state medicines agency; no auth, plain HTTP "
                      "GET of a bulk file, ETag and Last-Modified served so a conditional GET "
                      "is the polite default."),
            "checked": "2026-08-21",
        },
        "contract": {
            "parse": "json",
            "required_fields": ["kind", "period", "presentations", "validity"],
            "expected_yield": {
                "min": 5,
                "max": 30,
                "basis": ("MEASURED 2026-08-21: 82,837 notice rows aggregate to 15 items — 14 "
                          "ATC-1 interruption groups plus one monthly market-exit total. The "
                          "grain is (month x ATC group) and NOT one row per medicine, because "
                          "a single presentation scores money 0 / urgency 0 and would be "
                          "filtered out of existence by materiality while the manifest read "
                          "green (CONVENTIONS.md, the `hiring` trap). Bounded by the 14 WHO "
                          "anatomical groups, so this range is structural rather than "
                          "statistical. Counts items_fetched."),
            },
            "allow_missing": False,
        },
    },
}


def build_registry(tmpdir):
    with open(os.path.join(ROOT, "data", "feeds.json"), encoding="utf-8") as fh:
        reg = json.load(fh)
    merged, seen = [], set()
    for f in reg["feeds"]:
        if f.get("key") in PROPOSED_ROWS:
            merged.append(PROPOSED_ROWS[f["key"]])
            seen.add(f["key"])
        else:
            merged.append(f)
    for k, v in PROPOSED_ROWS.items():
        if k not in seen:
            merged.append(v)
    reg["feeds"] = merged
    path = os.path.join(tmpdir, "feeds.proposed.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(reg, fh, ensure_ascii=False, indent=2)
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--raw", help="a raw dir holding coi-*.json / nen-*.json / sukl-*.json payloads")
    ap.add_argument("--seen", default=os.path.join(ROOT, "data", "signals", "seen.txt"))
    ap.add_argument("--today", default=None)
    ap.add_argument("--no-extractors", action="store_true",
                    help="demonstrate the SCRIPTED-SILENT failure: skip the hand-off")
    ap.add_argument("--samples", type=int, default=2)
    ap.add_argument("--print-rows", action="store_true",
                    help="print the proposed data/feeds.json rows and exit")
    a = ap.parse_args()

    if a.print_rows:
        print(json.dumps(list(PROPOSED_ROWS.values()), ensure_ascii=False, indent=2))
        return 0
    if not a.raw:
        ap.error("--raw is required unless --print-rows is given")

    tmp = tempfile.mkdtemp(prefix="nen-sukl-preview-")
    # NOTHING UNDER data/raw/ IS WRITTEN. run_mechanical() drops staged.jsonl,
    # contract.json and a manifest section into the raw dir it is given, so it is
    # given a copy. Three other workers share this tree.
    scratch = os.path.join(tmp, os.path.basename(os.path.normpath(a.raw)))
    shutil.copytree(a.raw, scratch)

    normalize.FEEDS_JSON = build_registry(tmp)
    if not a.no_extractors:
        # THE HAND-OFF, APPLIED AT RUNTIME. This is the whole diff scripts/
        # normalize.py needs; it is done by assignment here because that file
        # belongs to another worker.
        normalize.EXTRACTORS["nen"] = nen_extract.extract_nen
        normalize.EXTRACTORS["sukl"] = sukl_extract.extract_sukl
        normalize.EXTRACTORS["coi"] = coi_extract.extract_coi
        # THE SECOND HALF OF THE coi HAND-OFF, AND IT IS EASY TO MISS BECAUSE IT
        # FAILS DIFFERENTLY. Without an EXTRACTORS entry a feed stages 0 records
        # silently; without a FILE_FEED_TOKENS entry the payload never reaches a
        # feed at all — feed_for_file() returns None and the file is listed as
        # "unmapped" at the bottom of the manifest, which reads like a stray file
        # rather than a broken feed. `coi` needs BOTH. Inserted before the
        # generic tokens, as that table is ordered specific-before-generic.
        if not any(t == "coi" for t, _ in normalize.FILE_FEED_TOKENS):
            normalize.FILE_FEED_TOKENS.insert(0, ("coi", "coi"))

    # `out_dir` is REQUIRED as of 2026-08-21: run_mechanical() now screens the
    # staged batch against the committed ledgers for a resource already held
    # under a different id, and out_dir is the ledger root it reads. Read-only
    # in this pass — nothing under data/signals/ is written.
    args = SimpleNamespace(raw=scratch, seen=a.seen, today=a.today,
                           out_dir=normalize.DEFAULT_SIGNALS_DIR)
    rc = normalize.run_mechanical(args)

    contract = json.load(open(os.path.join(scratch, "contract.json"), encoding="utf-8"))
    print("\n── items_fetched vs items_kept ─────────────────────────────────")
    for r in sorted(contract["results"], key=lambda x: x["feed_key"]):
        if r["feed_key"] not in ("coi", "nen", "sukl"):
            continue
        print(f"  {r['feed_key']:6s} http={r['http_status']} ok={r['ok']} "
              f"fetched={r['items_fetched']} kept={r['items_kept']} "
              f"yield={r['yield_anomaly']} parse={r['parse_method']} "
              f"err={r['error'] or '—'}")

    staged = [json.loads(l) for l in
              open(os.path.join(scratch, "staged.jsonl"), encoding="utf-8") if l.strip()]
    print(f"\n── staged records: {len(staged)} ───────────────────────────────")
    for key in ("coi", "nen", "sukl"):
        rows = [r for r in staged if r.get("_feed_key") == key]
        print(f"\n### {key}: {len(rows)} staged")
        for r in rows[:a.samples]:
            print(json.dumps(r, ensure_ascii=False, indent=1))
    print(f"\nscratch run dir (not under data/raw/): {scratch}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
