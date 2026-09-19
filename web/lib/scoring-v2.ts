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
  "p-0001", "p-0002", "p-0003", "p-0004", "p-0005", "p-0006", "p-0007", "p-0008", "p-0009", "p-0010", "p-0011", "p-0017", "p-0018", "p-0022", "p-0023", "p-0024", "p-0025", "p-0026", "p-0027", "p-0028", "p-0029", "p-0030", "p-0031", "p-0032", "p-0033", "p-0034", "p-0035", "p-0036", "p-0037", "p-0038", "p-0040", "p-0041", "p-0042", "p-0044", "p-0045",
]);

/** True when this record's money and urgency sit on the 2026-09-19 ladders. */
export const isScoringV2 = (id: string): boolean => SCORING_V2.has(id);
