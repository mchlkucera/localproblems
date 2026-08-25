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

MATURITY IS ONLY HALF THE LOCAL ANSWER (owner, 2026-08-25, one day later).
The first cut of locals[] carried a single field, status: established | early,
and it lasted one commit. Both content agents hit the same wall independently:
a MATURE Czech firm that sells something ADJACENT — the other side of the
counter, a different segment, a service firm rather than a product vendor — is
not "early", but writing "established" forced gap to 0 and stood a record down
over a company that does not sell this. One agent wrote those firms down as
early (a false maturity claim); the other left them out of the ledger entirely
(a false absence). The same one-field-two-meanings defect this document has
already fixed twice — the gap condition inside PROOF, "not checked" inside GAP.

  So the field is SPLIT, and the two halves answer different questions:

    competes: direct    sells THIS record's product to THIS record's buyer
    competes: adjacent  a real player in the neighbourhood that does NOT sell
                        this — different segment, different side of the
                        counter, legacy/partial, or a service firm rather than
                        a product vendor. Its evidence line must say plainly
                        WHAT IT DOES SELL and why that is not this.

    maturity:           the ESTABLISHED test above, unchanged and machine-
                        checked. It sets the RUNG, once competes has decided
                        the entry counts at all.

  AN ADJACENT PLAYER NEVER MOVES GAP, at any maturity. That is the entire
  point of the split.

  RECORD EVERY LOCAL PLAYER — never exclude one to protect a score. "The goal
  is to inform the builder properly": a builder needs to see who else is in
  the room, who the buyer already pays, and who could turn and compete next
  quarter. The adjacent half of the ledger is intelligence, not noise, and it
  renders as its own labelled group so it can never be mistaken for a
  competitor the record failed to score against.

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
                0: at least one locals[] entry with competes: direct AND
                maturity: established — someone mature already sells THIS, the
                space is taken · 1: locals sell this (competes: direct) but all
                are EARLY — contested, still enterable · 2: checked, and NO
                local sells this. Adjacent players may be recorded and do NOT
                affect the score
                verdicts   0 TAKEN · 1 CONTESTED · 2 OPEN

                EVERY RUNG READS BOTH FIELDS, competes FIRST. `competes`
                decides whether an entry counts at all; `maturity` decides
                which rung it lands on. An entry at competes: adjacent moves
                NOTHING, however old and however proven — a mature firm selling
                the other side of the counter has not taken this space, and
                before the split the only ways to say so were to mislabel it
                `early` or to leave it out of the ledger. Both shipped, in
                different halves of the register, which is how the defect was
                found.

                RUNG 2 STILL COSTS A CHECK. "No local sells this" is a claim,
                and it needs a type: gap-check source with recorded queries[]
                and a passing positive control — exactly as before. What
                changed is only that a populated locals[] no longer
                contradicts it: four adjacent firms on file and nobody selling
                this IS rung 2, and the page says so in those words.

                "NOT CHECKED" IS NOT A SCORE ON THIS LADDER. In v1, rung 0
                read "CZ incumbent check not done" — so a de-ranked record and
                an unchecked one landed on the same number and rendered the
                same verdict, UNCHECKED, above a printed list of competitors.
                An absent check is a MISSING RECEIPT, caught by
                scripts/check-records.py and blocked at the build gate. It is
                never expressed as a score.

                GAP AUTHORITY REMAINS ASYMMETRIC. Evidence of a named
                established local player THAT SELLS THIS lowers this score.
                Failure to find one NEVER raises it — only a check with
                recorded queries[], checked[] and a passing positive control
                can do that.

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
