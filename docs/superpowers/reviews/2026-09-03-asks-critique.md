# Critique — asks ledger (39aa121, 8fec4d4, dc88747)

Gates: tacr selftest "SELFTEST PASSED — 41 checks"; hack selftest "SELFTEST PASSED — 69 cases"; check-records "records: 35 · clean: 26 · errors: 0 · warnings: 9". Live: /signals/asks 200 (32 rows), /about 200, /sources 404 (by design, 3c73a7f).

## Findings, ranked

**1. should-fix (blocks the "sixth evidence type" claim) — "who asked" ships nowhere.**
`web/lib/ledger.tsx` never reads `notes`; the live /signals/asks HTML contains `owner:` zero times. Value is "—" on all 32 rows. No problem record cites a `type: ask` source (grep data/problems = 0), so `TYPE_TO_DIM["ask"]` is dead code and the design's Commit C never happened. §0 violation too: `notes` is "optional free text" (CONVENTIONS.md:167) and now also carries a structured key the spec admits is a workaround. Fix: an allowlisted, schema'd `owner` receipt (SignalSchema, same change), rendered in the Source cell for asks rows, gated by "every asks line has owner". Then attach the eight hospital asks to records.

**2. should-fix — materiality is decided by the hackathon calendar, not the problem.**
`normalize.py:371-400`: any event <6 months = urgency 3; `is_material` drops only at urgency 0 AND scale ≤1. All 22 dated challenges survived regardless of scale (7 at scale 1: Sarkom, X-Face, Rekurze, RadMan, three UPOL); the 3 undated aimtec rows died at the same scale 1. The design says so. `urgency` now means both "a deadline the world imposes on this problem" and "the hackathon is in November". Fix: asks rows stage `urgency_date: None`, keep the event date as a receipt materiality ignores, let scale decide — what the tacr half already does.

**3. should-fix — 10–12 of 32 rows are asks a builder could act on.**
Actionable: the 8 hackjakbrno hospital rows, tacr MŠMT, Plzeň mobility, arguably Rekurze/RadMan. The rest: 5 UPOL rows are bare titles (quote is `title — title`); 4 IDEA13 rows are citizen idea-contest themes ("poses a hackathon theme"); 6 Nakopni Prahu rows are thematic questions; 4 Rakathon rows and hack-20c85264 carry the organizer as owner via the fallback at `hack_extract.py:346-352` — "the organizer when the page names none" is the definition of not owner-set. hack-45597a87 claims the ask is cut off — false, the staged text ends "Cílem je vytvořit pilotní verzi nástroje…"; pass B read the quote, not the text; the owner names AstraZeneca. tacr-tieru0015 is a 2021 need whose calculator ERÚ shipped years ago. Fix: extractor refuses organizer-fallback owners and text == title; pass B reads `text`.

**4. should-fix — the TA ČR feed is hollow; the grading rule lives in a manifest note.**
feeds.json: 15 needs is "the whole public history", 10 from 2020–22, BETA3 budget cut June 2026, steady state 0–2/run — ~950 lines at cadence daily for two records, one from 2021. "Two graders, lower wins" is conservative (13 still dropped), not score-shopping — but the card was rebuilt after the first grade disappointed, and the rule exists only in `data/raw/2026-09-03/manifest.md`; `pipeline/INGEST.md` mentions neither feed nor graders. Fix: weekly cadence; write the rule into INGEST.md or drop it; refuse needs older than the tender that followed.

**5. should-fix — "an ask never cites money" is prose.**
Problem-source `type` is `z.string().min(1)` (`data.ts:205`); `check-records.py` has no TYPE_TO_DIM and no ask rule; TYPE_TO_DIM only routes display. A record citing an ask under money builds green. Nothing validates an asks line has `money_eur: null` or an owner — selftests test the extractor, not the ledger. Fix: check-records invariant + db-gate invariant, same commit as MATCH.md §11.

**6. should-fix — the fetchlog fix trades a false BROKEN for a hidden failure.**
`db.py:2054-2080` skips "no receipt and no payload". In a full unattended run a fetcher dying before its first `mf` (`fetch_tacr.sh` exits 2 on missing jq before any receipt; a kill) leaves that exact signature, and `run_feed` (`fetch_all.sh:182-191`) writes no fallback receipt. Before: BROKEN at once. Now: no row, LIVE until 3× cadence → STALE, never BROKEN. One signature, two meanings. Fix: `fetch_all.sh` writes a `skipped` receipt for every undispatched feed (it knows WANT) and an `error` receipt on nonzero rc without one; delete the db.py branch.

**7. nit — receipts and copy.** Every hack URL is a homepage that changes each edition; raw lives in `/tmp/claude-501/asks-run`; quotes cut mid-word. All 32 rows read "· llm" while feed_health says parse_method structured. About says "Six streams", SPEC §1 says five. The `s.byType.hiring === 0` clause is dead (34 hiring signals) — delete. Titles: "Nabídka × poptávka tool", "…keto apps". dc88747 silently rewrote yield_7d for 12 unrelated feeds.

## Cut / next
Cut: tacr daily cadence and its HTML backfill; the organizer-owner fallback; the urgency-from-event-date trick; UPOL until it publishes text. Single most valuable step: a schema'd, gated `owner` receipt rendered in the Source cell, then Commit C for the eight hospital asks.

## Verdict
The plumbing is good — guards, selftests, enum-before-record, honest doctrine notes — but what shipped is a demand ledger with a new intro paragraph, because the one fact the type exists for renders nowhere, scores nothing, and rides in a free-text field no validator reads. About a third of the 32 rows are asks a builder could act on; the rest are topic lines and organizer prompts that passed materiality on the event's date, not the problem's. Keep the hospital rows, make the owner a real field, drop the calendar trick, and stop calling the TA ČR feed live.
