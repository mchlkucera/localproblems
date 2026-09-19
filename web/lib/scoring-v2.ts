// THE SCORING-V2 SWITCH (owner, 2026-09-19; SCORING.md, "THE SWITCH").
//
// The money and urgency ladders were rewritten before the records were
// rescored: Why now lost its freshness point and now reads how close and how
// real the deadline is; Willing to pay reads price receipts, and public money
// nearby only lifts it. A record listed here has been rescored to those
// ladders, so the page reads its `scores.urgency` and `scores.money` directly
// with the new words, ladders and About copy. A record not listed still
// carries its v1 values, and the page shows them exactly as before.
//
// This list is the mirror of SCORING_V2_ENFORCED in scripts/check-records.py,
// and the checker fails the build when the two differ. A rescored record joins
// BOTH in the same change as its rescore (docs/scoring-v2/rescore-2026-09-19.md).
// When every live record is here, delete this file and every v1 branch.
export const SCORING_V2: ReadonlySet<string> = new Set<string>([
]);

/** True when this record's money and urgency sit on the 2026-09-19 ladders. */
export const isScoringV2 = (id: string): boolean => SCORING_V2.has(id);
