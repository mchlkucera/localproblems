# Backlog

Open work, newest first. A line leaves this file when the work lands, not when
it is started. Receipts over plans: every entry names what is already true, so
whoever picks it up does not re-derive the case for it.

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
