# Design language v2 — spec (planned, NOT yet implemented)

Owner-approved direction, recorded 2026-08-13. Nothing here is binding for v1.x
builds; the weekly pipeline keeps following SKILL.md until v2 ships. When v2 is
implemented, fold these into SKILL.md + assets/style.css and delete this file.

## 1. Proof dialogs carry the full signal record

Opening a scorecard dimension must show the evidence itself, not a pointer to it.

- The dialog embeds, for every referenced source (S1…Sn), **all recorded data
  from the signal's normalized record** (`data/normalized/<id>.md` frontmatter +
  body): id, source, url, date, category, tier, geo, the 2-sentence summary, and
  any quote. Not just the `→ S4` anchor link.
- Inlined at build time (static site — no fetch, no JS data loading). The weekly
  pipeline copies the record fields into the dialog markup when it renders the page.
- Layout (top to bottom): dimension label · score figure **with the wide-tick
  tally squares** · verdict word — then a hairline rule — then the justification
  sentence — then the embedded signal record(s).
- A **close cross** sits top-right: text glyph `×`, mono, muted-until-hover,
  implemented declaratively (`popovertarget` + `popovertargetaction="hide"`) —
  still zero JS.
- General polish: the dialog is an official notice — 2px ink border, paper
  ground, ink scrim backdrop, spacing on the --sp scale, fixed width ~30rem.

## 2. Sources section shows the record, not just the row

Below the "Sources" header, each entry expands beyond the one-line ledger row:

- The one-line row (S-number · linked name … date) stays as the scannable spine.
- Beneath it, the full signal record detail from the normalized file: summary,
  tier, geo, category, quote — same fields as in the proof dialogs, same
  build-time inlining. The register shows its evidence without leaving the page.
- Presentation to be designed: either always-visible detail lines or a
  disclosure per row — but never a second rule line per row (one row, one line).

## 3. Market math becomes prose

Retire the dot-leader ledger lines for market math. A serif, human-voice
paragraph states the assumptions and arithmetic inline — figures and sums stay
mono inline per the two-voice rule (e.g. wrapped in `<code>`/`.mono`). The
reasoning is an argument a human makes, not a clerk's ledger — so it is serif.

## 4. Status treatment replaces "OPEN — UNCLAIMED"

The current floating statline chip reads like a SaaS badge and does not match
the design language. v2 replaces it with a native device:

- Status moves into the docket **facts grid** as the first fact (label STATUS,
  value = status dot + word), or is expressed via the razítko stamp grammar for
  lifecycle events (CLAIMED / SOLVED / CLOSED already have stamps).
- The default open state should be quiet: the hollow green dot IS the signal;
  no floating chip, no uppercase shouting in the docket's air space.
- Exact treatment to be decided at implementation; the constraint is that it
  must come from the existing component grammar (dot, facts grid, stamp) —
  nothing new invented.
