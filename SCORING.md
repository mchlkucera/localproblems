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

MONEY (0-2)     is someone paying for this job now?       [shown as "Willing to pay"]
                "This job" is the product in `solution:` sold to the buyer in
                `entry.buyer`, or its manual equivalent bought in.
                0: no price receipt for this job on file. PUBLIC MONEY NEARBY
                ALONE SCORES HERE, however large · 1: an ASKING receipt, what
                the job costs: a vendor's or consultant's published price, a
                buyer's stated figure, or the sourced cost of doing it by hand
                · 2: a PAID receipt dated within 24 months of `updated`: a
                signed contract for this job, an awarded tender line for it, or
                a consultant paid to do it by hand; or rung 1 plus the
                public-money lift below
                verdicts   0 NONE · 1 INDICATED · 2 EVIDENCED

                THE RECEIPT IS A `type: price` SOURCE TAGGED `dims: [money]`,
                and nothing else is. It names payer · amount_czk · unit · basis
                · date (data/CONVENTIONS.md), so every point on this ladder
                says who pays and how much. ASKING is basis list-price,
                buyer-interview or manual-equivalent; PAID is basis
                signed-contract or tender-line. A paid receipt older than 24
                months shows what the job once cost, not that anyone pays now,
                and counts as ASKING. A `contract` or `tender` that buys THIS
                job is restated as a price receipt (signed-contract or
                tender-line); left as `type: contract`, `tender` or `subsidy`,
                it is PUBLIC MONEY NEARBY. One source type, one meaning.

                PUBLIC MONEY NEARBY NEVER EARNS A POINT ON ITS OWN. It lifts
                the score by at most one rung, 1 -> 2, and only when ALL hold:
                the base is already 1 from a price receipt; the programme names
                this record's buyer type as eligible; it names this job or its
                cost category as eligible spend; it is open on `updated`, or
                was awarded to buyers of this type within 12 months; and the
                buyer still co-pays (it funds under 100%). A fully funded
                purchase shows the state's willingness, not the buyer's.

                KNOWN CAVEAT, STATED AND NOT CORRECTED. Only public buyers
                publish what they pay (registr smluv, TED, NEN), so a record
                sold to private firms reaches rung 2 only through a signed
                private contract on file or the lift, and will tend to score
                lower than a public-buyer record. The section's About panel
                says so. Nothing re-weights for it: a receipt the register
                cannot see is not a receipt.

                WHY IT CHANGED (owner, 2026-09-19). Until then this ladder
                measured PROXIMITY TO A PUBLIC BUDGET (0 none · 1 a relevant
                tender or grant · 2 an open tender or grant >= ~5M CZK, or
                recurring spend) and never asked whose pocket the money left or
                whether it bought this. docs/who-pays-audit-2026-09-03.md found
                six of eight rung-1 records calling their own money "adjacent"
                and two rung-2 records scored on spend by a party who was not
                their buyer, under a section already named "Willing to pay".
                One name, two questions. The name won: the price receipt, added
                on 2026-09-03 as its own field for exactly this question, is
                now the evidence the score is read from.

URGENCY (0-3)   how close and how real is the deadline?   [shown as "Why now"]
                A trigger is a dated instrument on file as a `type: regulation`
                source: a law, a decree, an EU regulation, a regulator's
                decision, a mandated switch-off. Three tests, read off it:
                  REAL   enacted (the Sbírka zákonů or the EU Official Journal,
                         binding as published: an EU regulation, or a directive
                         once its Czech law has passed; never a bill, a draft
                         decree or a directive awaiting transposition, so a
                         record carrying `draft_law:` fails it by definition)
                         AND it binds THIS buyer (`entry.buyer`), not an
                         authority that must accept something, not the vendor
                  CLOSE  the compliance date is at most 18 months after
                         `updated`, or passed at most 12 months before it and
                         the duty now applies. An older duty is the status
                         quo: only a newer dated change to it (an amendment,
                         an enforcement campaign) can be the trigger
                  TEETH  the instrument names a sanction on the buyer for
                         missing it: a fine, a ban on trading or operating, a
                         licence withdrawn. For a date already passed, an
                         enforcement receipt dated within 12 months of
                         `updated` (fines levied, an inspection campaign,
                         proceedings opened)
                0: no dated duty falls on this buyer or forces it · 1: a dated
                duty that fails REAL or CLOSE: a draft, an untransposed
                directive, a duty on someone else that reaches the buyer
                indirectly, or a date more than 18 months out · 2: REAL and
                CLOSE, with no sanction on file · 3: REAL, CLOSE and TEETH
                verdicts   0 NONE · 1 MILD · 2 BUILDING · 3 FORCING

                NOT A DEADLINE ON THIS LADDER, so rung 0: a rule that only
                permits something or changes what the state pays (it binds no
                one to act); a government plan with no bill; a grant's closing
                date (its consequence is a lost subsidy, which is money, and
                MONEY's lift reads it); "the technology matured"; a market
                event or a court ruling with no dated duty on the buyer.

                FRESHNESS IS GONE, AND IT MAY NOT COME BACK AS A POINT (owner,
                2026-09-19). v1 read deadline 0-2 + freshness 0-1, the +1 for a
                newest source under 90 days old. It held on 29 of 29 live
                records, so it separated nothing, and on 13 it was the only Why
                now point: "we looked recently" was scoring as "buyers must
                act". When a record was last checked is a fact about the
                register, not about the deadline. It is shown as the page's
                Verified date (`updated`) and never as a score (one field, one
                meaning). The max stays 3: the rung the freshness point used to
                fill is now the deadline with teeth, so the total stays 12 and
                the bands below stand.

THE SWITCH (2026-09-19). The MONEY and URGENCY ladders above were rewritten
before the records were rescored, so the rescore is tracked per record, exactly
as the body rewrite was. A record joins `SCORING_V2_ENFORCED` in
scripts/check-records.py, and its mirror `SCORING_V2` in web/lib/scoring-v2.ts
(the checker fails the build when the two differ), IN THE SAME CHANGE as its
rescore; docs/scoring-v2/rescore-2026-09-19.md is the worklist. From then on
the checker's v2 invariants are ERRORs for it and its page reads both scores on
these ladders. Until then it still carries its v1 values (urgency = deadline +
freshness; money = public budget nearby) and its page shows them with the v1
words and ladders. When every live record is in the set, delete the set, the
mirror and every v1 branch, including the freshness code in web/lib/data.ts
`urgencySplit`, web/lib/scorecard.ts `dimRefs` and scripts/db.py.

DEMAND (0-2)    is the pain documented?
                0: assumed · 1: scattered complaints · 2: recurring documented
                complaints, petition, or industry pressure
                verdicts   0 ASSUMED · 1 SCATTERED · 2 DOCUMENTED

GAP (0-2)       is the local field still open?             [shown as "Market gap"]
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

DIFFICULTY TO ENTER IS NOT A SCORE (owner, 2026-09-15). The `entry` block on
every record — level, buyer, permission, incumbents, integration, money, why —
is FEASIBILITY, not opportunity: it never enters the 12 points, never moves a
band, and is rendered apart from the scorecard. It replaced the `build`
scorecard (capital ladder, team band, time to first revenue); the definitions
live in data/CONVENTIONS.md.

  `level` is DERIVED, not judged: buyer small-firms 0 / large-firms 1 /
  public 2 · permission none 0 / registration 1 / licence 2 · integration
  software 0 / national-system 1 / certified 2 · money bootstrap 0 /
  outside-money 2. Max weight 0 -> easy · max 1 -> moderate · exactly one gate
  at 2 -> hard · two or more at 2 -> very-hard.

  `entry.incumbents` CARRIES NO WEIGHT, and that is this file's business:
  GAP already prices established local competition, so weighing it again in
  the level priced ONE FACT TWICE — the same one-field-two-meanings defect
  this rubric has fixed at PROOF rung 2 and GAP rung 0. The gate stays on the
  record (derived from locals[], asserted by the checker, rendered as the
  ALREADY HERE row); it just does not set the level. Measured before the
  amendment: 20 of 37 records came out hard or very-hard and the owner's own
  canonical easy example, an app for trucking firms, came out hard.

  `entry.incumbents` and `scores.gap` read the same ledger and must not
  disagree about it — both turn on competes: direct + maturity: established.

Verdict bands (total score → word):

                10-12   PRIME
                 8-9    STRONG
                 5-7    FAIR
                 0-4    FAINT

                Score >= 8 (STRONG and up) = newsletter-lead material.

                The max is 12 and these bands are unchanged by the 2026-09-19
                amendment: URGENCY keeps its max of 3 and EXECUTION DIFFICULTY
                stays out of the sum.

Rules: every point must be justified by a sources[] entry - no source, no
point. Tie-break by (urgency, money); on a record not yet rescored, by its
deadline part. Tier-3 sources can never lift proof or demand above 1 on their
own. Verdict words are rubric vocabulary: they are asserted by the build
(web/lib/scorecard.ts) and never rendered on a public page.

PRESENTATION (owner, 2026-09-17 and 2026-09-19). The public page shows each
dimension as a section with its points as n/max (never "out of 10"), one
reasonable judgement word per rung, and a reason line read from the data
(web/lib/site/score-proto.ts). There is no business-fit row.

  field     section              words, rung 0 -> max
  demand    The opportunity      Unclear pain · Some pain · Clear, recurring pain
  urgency   Why now              No deadline · Soft deadline · Firm deadline ·
                                 Deadline with penalties
  money     Willing to pay       No sign yet · Some signs · Clear signs
  proof     Validated abroad     Not yet · Early abroad · Proven once ·
                                 Proven in 2+ markets
  gap       Market gap           Crowded · Early rivals only · Open
  entry     Execution difficulty Very hard · Hard · Moderate · Easy
                                 (easier = more points, /3; shown beside the
                                 total, never summed into it)

  MARKET GAP, NOT "COMPETITION" (owner, 2026-09-19). Every summed row reads
  more = better, so a full bar always means good. Printed as "Competition 2/2",
  a full bar meant "nobody sells this" and read as "heavy competition". The
  field stays `gap` and its rungs did not move; only the name the reader sees
  changed. Anchors keep `#competition`.

  WILLING TO PAY'S WORDS ARE EVIDENCE WORDS, not "paying": rung 2 is reached
  either by a paid receipt or by an asking price plus the public-money lift,
  and "Already paying" would overclaim the second route. The reason line
  names which.

  EXECUTION DIFFICULTY STAYS OUT OF THE TOTAL (owner, 2026-09-19). It is the
  effort side of the decision, and it depends on who is reading. The total is
  the rubric sum above, /12, on the record page and the front page alike.
