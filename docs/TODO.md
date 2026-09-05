# Backlog

Open work, newest first. A line leaves this file when the work lands, not when
it is started. Receipts over plans: every entry names what is already true, so
whoever picks it up does not re-derive the case for it.

---

## Content pass owed after the 2026-09-03 runs

**Status:** open · surfaced by the weekly run, the who-pays audit and the harvest agents (2026-09-03)

Receipts already true, work not yet done — all of it record edits or attended
searches, none of it pipeline:

- **Five phone calls price the register's open fields** (docs/who-pays-audit-2026-09-03.md
  §3): a staffing agency's per-shift rate and mark-up (p-0033), a relocation
  agency's per-card fee (p-0009), a lender's outside-counsel cost per
  financial-arbiter case (p-0027), eCENTRE's or SMS ČR's pooled-purchase fee
  (p-0031), a care home's per-move-in (p-0032). Each lands as a `type: price`
  source; p-0001 and p-0003 show the shape (price the manual equivalent).
- **Wastewater sweep** (pipeline/SWEEP.md, topic "UWWTD transposition — ČOV
  energy assessment, stormwater charge, micropollutant EPR"): the cluster has
  its second signal (dotace-sfzp-2-2026-fn-cov + reg-vak-energeticke-posouzeni-cov
  + reg-vodni-zakon-epr-mikropolutanty + reg-vak-srazkove-vody-poplatek +
  veklep-KORNDXBH65S3) and fails only proof (no comp in corpus) and gap
  (unchecked). Buyer: VaK utilities and their municipal owners (~200 plants
  above 10,000 PE), pharma/cosmetics producers on the EPR; money: SFŽP
  1,355.2M CZK loans to 2027-03-31, RIA 8-15bn CZK. Collides with p-0026's
  buyer — Softlink CEM, VODÁRENSKÁ, SČVK, SUEZ hold the managed-service seat.
- **locals[] adjudications the match agents could not make** (no web access):
  BUILDSYS a.s. (IČO 27690253, since 2006), HGS a.s. (FLOWBOX) and Novatec EAS
  against p-0024 — recorded in its S6 note as adjacent, unledgered; Asseco
  Central Europe on national eHealth services against p-0022 (dismissed
  ted-601039-2026, gap already 0).
- **The graveyard inverse** as one checklist line in pipeline/MATCH.md §9 or
  SCANS.md: before a record reaches score ≥ 7, name the last comparable that
  FAILED at this, its recorded cause, and the dated Czech instrument that
  removes it — or say that nothing does. The audit's dry run found Directive
  (EU) 2024/2831 against p-0033 this way (now filed as S11).
- **MPSV figures already rendered**: the August health-care aggregate on
  p-0033 [S10] is cited on counts only because its EUR total was inflated ~21%
  by one mislabelled row; re-derived 2026-09-03 with the plausibility guards
  in scripts/mpsv_reduce.py it reads EUR 8.66M (was 11.03M). The July figure
  (EUR 10.8M, rendered in p-0011 and p-0033 prose) re-derives to EUR 10.84M —
  unchanged, no edit owed. Ledger lines are append-only; the corrected
  numbers enter with the next month's aggregate.
- **Two FX rates in one manifest** (dotace-scan 24.215, demand/reg-scan 24.5
  CZK/EUR on 2026-09-03): pick one and write it into SCANS.md.
- **`dotace-optak-technologie-mas-2`** carries `source: hlidac` on a dotace- id
  (pre-existing provenance mismatch, committed); the ledger cannot be edited —
  note it where the feed's provenance rule lives.

---

## Print ruling: the gist toggle on paper

**Status:** open · surfaced during the 33-record retrofit (landed 2026-09-02)

`@media print` prints a `<details>` closed, so a photocopy of a gist-carrying
record loses its `why` sentences. The site is meant to photocopy beautifully
(design-language, "the paper is the brand"). Needs a design ruling: force-open
the disclosure in the print block, or accept that the gist alone is what prints.

The retrofit itself landed 2026-09-02: all 33 records passed the plain-language
pass (gloss at first use · receipt-density tightening · a gist on every source ·
First moves in the house voice), `check-records.py` reports 34 records · 34
clean · 0 errors · 0 warnings, and no score, status or `note:` moved. The other
open ruling from that entry — allowlist noise on caps-styled names and Roman
numerals — was settled by practice, not by widening `GLOSS_ALLOWLIST`: every
flagged case read better glossed ("AZ LEGAL — three law firms —",
"OP TAK Technologie pro MAS II — the state's business-support programme"), so
the gate keeps flagging and authors keep glossing.
