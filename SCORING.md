score = proof + money + urgency + demand + gap                      (0-12)

Five top-line dimensions — rendered as the scorecard band on every record
page, comparable across the whole register. Every point must be justified by
a sources[] entry — no source, no point. Subjective vibes-scores are
forbidden.

THE ESTABLISHED TEST (owner, 2026-08-25) — the axis PROOF and GAP both turn
on, with the sign flipped. It replaces the v1 "does a company exist?" test,
which could not discriminate: half the signal corpus is "a funded foreign
company exists" (yc + round + arb-scan), so 81% of records were born passing
it. Existence is not information. Maturity is.

  A player is ESTABLISHED when it has been selling for >= 3 years AND shows
  at least one of: named customers or a public customer count · >= 2 distinct
  public buyers in data/lookup/cz-contract-parties.jsonl · funding at Series A
  or later · a state certification, attest or framework listing.
  Otherwise it is EARLY — funded-but-prototype, solo-operator, pre-customer.

  Every field the test reads is on the record already: comps[].since,
  comps[].traction, locals[].since, locals[].ico, locals[].evidence. It is
  therefore CHECKED BY SCRIPT, not judged — which is the whole point. A
  dimension a machine cannot audit is a dimension that silently rots.

  ABROAD an established player is GOOD NEWS: the model is proven and someone
  has already paid the tuition. An early one is weaker validation but not
  nothing — two founders with a prototype means the market is being proven
  right now, and it is a good moment to join.

  LOCALLY the sign flips. An established, well-maintained local product means
  the space is taken. An early local player does NOT close the space and must
  not de-rank a record on its own.

PROOF (0-3)     is an established solution running elsewhere?
                0: no foreign solution on file · 1: EARLY foreign players only
                (prototype, pre-customer, seed) — model unproven, but a good
                moment to join · 2: one ESTABLISHED foreign player · 3:
                ESTABLISHED in 2+ markets, at least one CEE-adjacent
                (DE/AT/PL/Nordics/Baltics/SI/SK/HU)
                verdicts   0 NONE · 1 EARLY · 2 ESTABLISHED · 3 VALIDATED

                NO GAP CONDITION MAY APPEAR ON THIS LADDER. The v1 rung 2
                read "funded analog in DE/AT/PL/Nordics + no CZ player found",
                which put a LOCAL fact inside a FOREIGN dimension: finding a
                Czech vendor knocked out rung 2 while rung 3 carried no such
                rider and still passed, so 13 of 26 live records ended up
                scoring proof <= 1 above their own funded comparables. One
                fact, counted twice, in the wrong column.

MONEY (0-2)     is budget attached?
                0: none · 1: relevant tender/grant exists · 2: OPEN tender or
                grant >= ~5M CZK, or recurring annual spend
                verdicts   0 UNFUNDED · 1 NEARBY · 2 ATTACHED

URGENCY (0-3)   why now?                     [deadline 0-2 + freshness 0-1]
                deadline sub-score — 0: no regulatory trigger · 1: compliance
                date >18mo out · 2: compliance date <18mo (forcing function
                live)
                freshness sub-score — +1: newest source < 90 days
                verdicts   0 NONE · 1 MILD · 2 BUILDING · 3 FORCING

DEMAND (0-2)    is the pain documented?
                0: assumed · 1: scattered complaints · 2: recurring documented
                complaints, petition, or industry pressure
                verdicts   0 ASSUMED · 1 SCATTERED · 2 DOCUMENTED

GAP (0-2)       is the local field still open?
                0: an ESTABLISHED local player already sells this (named in
                locals[]) — the space is taken · 1: local players exist but
                all EARLY, or only weak/legacy incumbents — contested, still
                enterable · 2: checked against Czech-language surfaces and no
                local player found
                verdicts   0 TAKEN · 1 CONTESTED · 2 OPEN

                "NOT CHECKED" IS NOT A SCORE ON THIS LADDER. In v1, rung 0
                read "CZ incumbent check not done" — so a de-ranked record and
                an unchecked one landed on the same number and rendered the
                same verdict, UNCHECKED, above a printed list of competitors.
                An absent check is a MISSING RECEIPT, caught by
                scripts/check-records.py and blocked at the build gate. It is
                never expressed as a score.

                GAP AUTHORITY REMAINS ASYMMETRIC. Evidence of a named
                established local player lowers this score. Failure to find
                one NEVER raises it — only a check with recorded queries[],
                checked[] and a passing positive control can do that.

Verdict bands (total score → word):

                10-12   PRIME
                 8-9    STRONG
                 5-7    FAIR
                 0-4    FAINT

                Score >= 8 (STRONG and up) = newsletter-lead material.

Rules: every point must be justified by a sources[] entry - no source, no
point. Tie-break by (urgency.deadline, money). Tier-3 sources can never lift
proof or demand above 1 on their own. Verdict words render exactly as written
— one word, mono, uppercase, no emoji — on the scorecard and nowhere else.
