# `asks` — a sixth evidence type: direct asks from problem owners

Owner decision, 2026-09-03: "owner-set is what we're looking for … make it SIMPLE."

## What it is

An **ask** is a named institution publicly stating a problem it wants solved and
inviting solutions — before any procurement money is attached. Today the register
has no home for that: the five ledgers answer "where did this come from" and an
owner-stated need lands in `demand` beside Reddit complaints, losing the one fact
that makes it strong evidence: **who asked**.

`asks` is the ledger for that fact. Two sources land it in this change; a third
(NEN market consultations) is documented as a follow-up, not built.

| source key  | prefix  | publisher                                     | what one record is                                          |
|-------------|---------|-----------------------------------------------|-------------------------------------------------------------|
| `tacr`      | `tacr-` | Technology Agency ČR, programmes BETA2/BETA3  | one ministry research need (TT…-coded) with its consultation |
| `hackathon` | `hack-` | six Czech organizers whose challenges are set by a hospital, a city or a ministry | one challenge statement with its owner |

Sites (all measured 2026-09-03, plain HTML, HTTP 200 with a browser User-Agent):
hackjakbrno.cz (FN Brno, FNUSA, MOÚ, JINAG — 15 challenge boxes) ·
rakathon.cz (FN Motol, MOÚ, FN Ostrava — 4 named challenges) ·
hackathon.upol.cz (Olomoucký kraj + město Olomouc — "letošní témata", 3.6 MB page) ·
idea13.cz (MČ Praha 13 — 4 "Výzva č. N") · aimtechackathon.cz/hackathon (City of
Plzeň, Ottobock, NGOs — 5 challenges) · nakopniprahu.cz (MHMP + OICT — 3 areas
with sub-topics).

## Where it sits in the doctrine

- **Evidence type, not voice.** SPEC §1 gains a fifth stream, *Direct asks*. The
  ledger answers "what is this evidence", the record's `notes: owner: …`
  receipt (and its title) answers "who asked". One field, one meaning
  (MATCH.md §0). Found while landing: `entity_native` is a STAGING field the
  append allowlist drops, so the owner rides on `notes`, the one allowlisted
  free-text receipt, exactly as ted carries its counterparties.
- **Scoring.** On a problem record an `ask` source cites the DEMAND dimension
  (`TYPE_TO_DIM` in `web/lib/scorecard.ts` and `scripts/db.py`, both). It never
  moves MONEY: a 50k CZK hackathon prize is not a budget for the problem, and a
  TAČR need's budget is in the later tender, which arrives through NEN/TED.
- **Engagement is not pain.** Team counts, prizes and winners are never scored.
  The record is the challenge statement and its owner.
- **Materiality.** A single challenge scores money 0. It survives normalize's
  materiality drop through `urgency_date` = the event/consultation date, on the
  same reasoning `ec-hys` already uses ("a consultation deadline is a real date
  the world imposes on us"). Where no date parses, the model's `scale` decides,
  exactly as for every other feed. No aggregation, no default scores.
- **Personal data.** Challenge pages name garants and contacts. The fetchers stage
  only the challenge title and the problem text; contact/garant lines are cut at
  the fetcher, and the existing allowlist + email/phone gate runs unchanged.
- **Append-only ledger law.** `SignalSchema.source` is widened to `tacr` and
  `hackathon` in a commit BEFORE the first record lands (CONVENTIONS.md).

## The two commits

**Commit A — registration, zero records.** `EVIDENCE_TYPES` + source enum
(`web/lib/data.ts`), ledger title/description + source labels
(`web/lib/ledger.tsx`), about-page prose, `TYPE_TO_DIM` ×2, `data/feeds.json`
rows (status `planned`), CONVENTIONS/SPEC/design-skill/MATCH/RECORD-TEMPLATE text,
sources-catalog wave 4, `normalize.py` tokens + extractor wiring, `fetch_all.sh`
argv cases, `db.py health` → two PENDING rows. Build gate green with an empty
`/signals/asks`.

**Commit B — fetchers + first records.** `scripts/fetch_tacr.sh` +
`scripts/tacr_extract.py`; `scripts/fetch_hackathons.sh` + `scripts/hack_extract.py`;
`scripts/asks_contract_selftest.py` with checked-in fixtures; feeds flipped to
`active`; one attended ingest run (mechanical → model pass A/B via session
subagents → `--complete` → `db.py upsert` → `health`). Then `vercel build --prod`
and `vercel deploy --prebuilt --prod`.

**Commit C (small, judgment) — attach.** Where an ask is a direct fit for an
existing problem record, add it as a `type: ask` source citing DEMAND, per
MATCH.md. Only clear fits; never to move a score.

## Contracts (read by both the fetcher and the extractor)

`tacr` payload `tacr-needs.jsonl`, one line per research need:
`need_id` (TT…, uppercase as published) · `title` · `link` · `date` (ISO) ·
`ministry` (native, as named in the post) · `consultation_date` (ISO or "") ·
`body` (collapsed text ≤ 2000 chars). Required: need_id, title, link.
Posts without a TT-coded need (budget notices, outages) are dropped by the
fetcher and counted.

`hackathon` payload `hack-challenges.jsonl`, one line per challenge:
`site` (host) · `owner` (the institution that set the challenge, or the organizer
when the page names none) · `page_url` · `title` · `text` (≤ 1500 chars, no
contact lines) · `event_date` (ISO or "") · `edition` (year). Required: site,
owner, page_url, title, text.

Extractor outputs follow the `extract_nku`/`extract_ec_hys` shape:
`id`, `source`, `evidence_type: "asks"`, `url`, `date`, `title_native`,
`entity_native` (= ministry / owner), `sector: None`, `money_eur: None`,
`money_note: ""`, `urgency_date`, `quote_parts`, `excerpt`. Ids:
`tacr-<need_id lowercased>` and `hack-<sha1_8(site + "|" + title)>`.

## Out of scope, stated

NEN market consultations (predběžné tržní konzultace): the bulk ISVZ files the
NEN fetcher reads may or may not carry the procedure kind; unverified, so not
built. Petitions, aggregator pointer feeds, student-picked hackathon topics
(#hackujstát): researched, rejected for this ledger.
