# Backlog

Open work, newest first. A line leaves this file when the work lands, not when
it is started. Receipts over plans: every entry names what is already true, so
whoever picks it up does not re-derive the case for it.

---

## Retrofit the remaining 33 records to the p-0010 standard

**Status:** open · **Owner mandate 2026-08-25** ("continue doing this with the
rest") · **Proven on:** p-0010 ([live](https://www.localproblems.org/problem/cz/p-0010), commit `130a857`)

p-0010 was rewritten to what the record page is for: a builder orients,
understands and can act. The remaining 33 records have not had that pass. Do it
per record — the four parts travel together, because a glossed record that is
still 540 words has only fixed half the problem:

1. **Gloss the jargon at first use.** A plain-language appositive inside the
   sentence — em-dash or parenthesis — then the bare term after. The law is in
   `data/CONVENTIONS.md`; `scripts/check-records.py` enforces it warning-level.
   **The worklist is the gate's own output:** 146 unglossed terms across 25
   records at the time of writing. Run it and work the list:
   ```bash
   python3 scripts/check-records.py 2>&1 | grep -B2 gloss
   ```
   Top offenders on the first run: TED, KYC, DORA, ERP, ARES, ČNB, NZÚ, SME, ČR.
2. **Tighten for receipt density.** Test every sentence: does it carry a receipt
   (number, name, date, source) or a decision a builder needs? If not, cut it.
   `check-records.py` warns above 450 argument words. Density means receipts per
   word goes UP — never that receipts are dropped. p-0010 went 542 → ~430 with
   all 32 citation markers, every figure and every named company kept.
3. **Add a `gist` to every source.** 2–6 words, clerk voice, no verb needed. The
   row then renders `NAME · gist · date` with the `why` sentence folded behind
   the native `more` toggle. Never touch `note:` — internal receipt, law.
4. **First moves in the plain house voice.** Verbs first, short sentences, no
   consultant nouns. Read p-0010, p-0032 or p-0001 for the target.

Log each record's pass in its `## Revisions` entry for the date, house style,
one entry per date. Scores, status and `note:` fields are never touched by a
language pass.

### Two rulings this retrofit will need

- **Allowlist noise.** The gloss gate currently flags Roman numerals inside
  names ("NZÚ II") and caps-styled company names (SAKO, ARROWS). Decide whether
  to widen `GLOSS_ALLOWLIST` in `scripts/check-records.py` or to exclude those
  token classes by rule. Do it while working the list, not before — the list is
  the evidence for which way to rule.
- **The toggle on paper.** `@media print` prints a closed `<details>` closed, so
  a photocopy of a gist-carrying record loses its `why` sentences. The site is
  meant to photocopy beautifully (design-language, "the paper is the brand").
  Needs a design ruling: force-open the disclosure in the print block, or accept
  that the gist alone is what prints.
