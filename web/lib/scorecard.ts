// Scorecard vocabulary. Verdict words and bands are constants asserted at build
// time against ../SCORING.md — drift breaks the build, not the page (SPEC.md §5).
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { extractDate, type Problem, type ProblemSource, urgencySplit } from "./data";

export const DIMS = ["proof", "money", "urgency", "demand", "gap"] as const;
export type Dim = (typeof DIMS)[number];

export const MAX: Record<Dim, number> = { proof: 3, money: 2, urgency: 3, demand: 2, gap: 2 };

// PROOF and GAP were re-worded on 2026-08-25 with the ladders themselves
// (SCORING.md, THE ESTABLISHED TEST). Both now turn on the same axis — is the
// player ESTABLISHED or EARLY — with the sign flipped, so the words say which
// side of that axis a score is on: EARLY/ESTABLISHED abroad, TAKEN/CONTESTED/
// OPEN at home. `UNCHECKED` is gone and cannot come back: an absent gap check
// is a missing receipt caught by scripts/check-records.py at the build gate, so
// it is never a score, and therefore never a word on this card.
export const VERDICTS: Record<Dim, string[]> = {
  proof: ["NONE", "EARLY", "ESTABLISHED", "VALIDATED"],
  money: ["UNFUNDED", "NEARBY", "ATTACHED"],
  urgency: ["NONE", "MILD", "BUILDING", "FORCING"],
  demand: ["ASSUMED", "SCATTERED", "DOCUMENTED"],
  gap: ["TAKEN", "CONTESTED", "OPEN"],
};

export const BANDS: [number, string][] = [
  [10, "PRIME"], [8, "STRONG"], [5, "FAIR"], [0, "FAINT"],
];
export const bandWord = (score: number) => BANDS.find(([min]) => score >= min)![1];

// ---- the PUBLIC scorecard: plain labels + plain reads (owner, 2026-08-24) ---
// The record page no longer shows the SCORING.md verdict words (UNPROVEN, FAINT,
// LIKELY …) — "who are you impressing with the jargon". Each dimension is stated
// with a plain, builder-facing label and one plain line, and the whole card is
// headed "Opportunity {sum}/12". Polarity is consistent: on EVERY row more is
// better (gap high = the field is open, not "more competition"). The Build line
// is separate — it is feasibility, not opportunity. VERDICTS/criterion above
// stay in the module: they remain the vocabulary the build asserts against
// SCORING.md (lib layout.tsx `assertScoringVocabulary`), just not rendered.

/** Dimension order and plain label on the public card — proof first, urgency
    ("why now") last, exactly as the owner's exemplar reads. */
export const SCORE_ROWS: { dim: Dim; label: string }[] = [
  { dim: "proof", label: "Validated abroad" },
  { dim: "gap", label: "Local opportunity" },
  { dim: "demand", label: "Demand signal" },
  { dim: "money", label: "Money available" },
  { dim: "urgency", label: "Why now" },
];

/** One plain line per dimension level. Indexed by the raw sub-score; higher is
    always the better reading. No verdict words, no rubric jargon. */
const READS: Record<Dim, string[]> = {
  proof: [
    "no solution found abroad",
    "only early players abroad — the model is not proven yet",
    "an established company already sells this abroad",
    "established across several markets, one close to home",
  ],
  gap: [
    "an established local player already sells this",
    "local players exist, but all still early",
    "no local player found — the field is open",
  ],
  demand: [
    "demand assumed, not yet shown",
    "documented, not yet loud",
    "recurring, documented demand",
  ],
  money: [
    "no funding receipt on file",
    "an adjacent grant or tender nearby",
    "funding attached to this",
  ],
  urgency: [
    "no dated trigger",
    "a trigger, but over a year out",
    "a dated trigger, closing in",
    "a dated deadline is forcing the change",
  ],
};

/** The one-line read under each score.
 *
 *  IT IS DERIVED FROM THE DATA, NOT ONLY FROM THE NUMBER, and that is the whole
 *  point: a read that contradicts what the reader can see two inches below it
 *  destroys more trust than a missing read ever would. The bug this shape was
 *  built to kill (cc2dcda) was `gap: 0` meaning TWO OPPOSITE THINGS — v1
 *  SCORING.md defined rung 0 as "CZ incumbent check not done" while the SPEC §4
 *  de-rank rule ALSO set it to 0 when a local player WAS found, so twelve live
 *  records printed "local competitors not yet checked" directly above the
 *  competitors that had been found.
 *
 *  THAT AMBIGUITY IS NOW CLOSED AT THE LADDER, NOT HERE. `gap: 0` means TAKEN
 *  and nothing else; an absent check is a missing receipt that fails the build
 *  in scripts/check-records.py. So this function no longer asks "was it
 *  checked?" — it asks WHO, reading the established player straight out of
 *  `locals[]` and naming them. **No branch of this function may ever say a
 *  score was not checked**: an unchecked dimension is not a score.
 *
 *  Where a rung's meaning is a fact about a LEDGER — how many comparables, how
 *  many local players, which one — the read states that fact and lets the
 *  section below it speak. Where the score contradicts its own ledger
 *  (`proof: 0` above two funded comps, as p-0008 shipped) the read reports the
 *  ledger, never the score: whether the score itself is right is a MATCH
 *  judgment this function must not pre-empt, and the checker's business. */
export function scoreRead(p: Problem, dim: Dim): string {
  const n = p.comps?.length ?? 0;
  const plural = (k: number) => (k === 1 ? "" : "s");
  const companies = (k: number) => `${k} compan${k === 1 ? "y" : "ies"}`;

  if (dim === "proof" && n > 0) {
    if (p.scores.proof >= 3) return `${companies(n)} abroad, established across several markets`;
    if (p.scores.proof === 2)
      return n === 1
        ? "one established company abroad — the model is proven"
        : `${n} companies abroad, at least one established`;
    if (p.scores.proof === 1) return `${companies(n)} abroad, all still early`;
    // proof 0 with comps under it: the ledger wins, and check-records.py has
    // already made this an ERROR on the new ladder.
    return `${n} comparable${plural(n)} on file — see Proven abroad`;
  }

  if (dim === "gap") {
    const locals = p.locals ?? [];
    const established = locals.filter((l) => l.status === "established");
    if (p.scores.gap === 0 && established.length > 0) {
      // Oldest first — the longest-selling incumbent is the one that closed the
      // space, and its start year is the reader's fastest check on the claim.
      // LocalSchema's refinement guarantees `since` on an established player, so
      // the undefined arm is unreachable; it is written anyway because a read is
      // rendered on every record and "since undefined" is exactly the class of
      // sentence this function exists to prevent.
      const year = (l: { since?: number }) => l.since ?? Number.POSITIVE_INFINITY;
      const oldest = established.reduce((a, b) => (year(b) < year(a) ? b : a));
      const since = oldest.since === undefined ? "" : ` since ${oldest.since}`;
      const rest = established.length - 1;
      // No parenthetical: a third of the corpus names its incumbent with one
      // already ("STORMWARE (POHODA)"), and nested parens read as a typo.
      return rest === 0
        ? `${oldest.name} has sold this${since} — see Local competition`
        : `${oldest.name} has sold this${since}, and ${rest} more sell it locally`;
    }
    if (p.scores.gap === 1 && locals.length > 0)
      return `${locals.length} local player${plural(locals.length)} on file, all still early`;
    // gap 2 says "no local player found". A locals[] ledger under it is the
    // contradiction this whole round exists to kill, and check-records.py fails
    // the build on it — but for as long as one can exist, the read reports the
    // ledger rather than denying it two inches above its own contents.
    if (p.scores.gap === 2 && locals.length > 0)
      return `${locals.length} local player${plural(locals.length)} on file — see Local competition`;
  }

  return READS[dim][p.scores[dim]];
}

// Rubric criteria, quoted from SCORING.md — the rundown drawers state the
// criterion for the achieved level, never invented prose.
const CRITERIA: Record<Dim, string[]> = {
  proof: [
    "no foreign solution on file",
    "EARLY foreign players only (prototype, pre-customer, seed)",
    "one ESTABLISHED foreign player",
    "ESTABLISHED in 2+ markets, at least one CEE-adjacent",
  ],
  money: [
    "no budget attached",
    "relevant tender/grant exists",
    "OPEN tender or grant ≥ ~5M CZK, or recurring annual spend",
  ],
  urgency: [], // composed from the deadline + freshness sub-scores below
  demand: [
    "pain assumed, not documented",
    "scattered complaints",
    "recurring documented complaints, petition, or industry pressure",
  ],
  gap: [
    "an ESTABLISHED local player already sells this (named in locals[])",
    "local players exist but all EARLY, or only weak/legacy incumbents",
    "checked against Czech-language surfaces and no local player found",
  ],
};

const DEADLINE_CRITERIA = [
  "no regulatory trigger",
  "compliance date >18mo out",
  "compliance date <18mo (forcing function live)",
];
const FRESHNESS_CRITERION = "newest source < 90 days";

export function criterion(p: Problem, dim: Dim): string {
  if (dim !== "urgency") return CRITERIA[dim][p.scores[dim]];
  const { deadline, freshness } = urgencySplit(p);
  const parts = [`${DEADLINE_CRITERIA[deadline]} (${deadline}/2)`];
  if (freshness) parts.push(`${FRESHNESS_CRITERION} (1/1)`);
  return parts.join("; ");
}

// ---- source refs per dimension (docs/archive/05 §4 rules) ----------------

const TYPE_TO_DIM: Record<string, Dim> = {
  arbitrage: "proof",
  tender: "money", contract: "money", subsidy: "money",
  regulation: "urgency",
  complaint: "demand", news: "demand",
  "gap-check": "gap",
};

/** 1-based S-numbers backing each dimension. Priority: explicit dims: tag,
    then type→dimension mapping (+ the "Demand point" gap-check convention),
    then freshness always refs the newest sub-90-day source. */
export function dimRefs(p: Problem): Record<Dim, number[]> {
  const refs: Record<Dim, number[]> = { proof: [], money: [], urgency: [], demand: [], gap: [] };
  const add = (dim: Dim, n: number) => { if (!refs[dim].includes(n)) refs[dim].push(n); };

  p.sources.forEach((s: ProblemSource, i) => {
    const n = i + 1;
    if (s.dims) {
      for (const d of s.dims) add(d, n);
      return;
    }
    const dim = TYPE_TO_DIM[s.type];
    if (dim) add(dim, n);
    if (s.type === "gap-check" && s.note.includes("Demand point")) add("demand", n);
  });

  const { freshness } = urgencySplit(p);
  if (freshness) {
    const newest = [...p.sources.entries()].sort((a, b) => a[1].date.localeCompare(b[1].date)).at(-1)!;
    add("urgency", newest[0] + 1);
  }
  for (const dim of DIMS) refs[dim].sort((a, b) => a - b);
  return refs;
}

// ---- build-time assertion ------------------------------------------------

let _asserted = false;
export function assertScoringVocabulary(): void {
  if (_asserted) return;
  const scoring = readFileSync(join(resolve(process.cwd(), ".."), "SCORING.md"), "utf8");
  const words = [...Object.values(VERDICTS).flat(), ...BANDS.map(([, w]) => w)];
  const missing = words.filter((w) => !scoring.includes(w));
  if (missing.length)
    throw new Error(`verdict words not found verbatim in SCORING.md: ${missing.join(", ")} — fix the constants, never the page`);
  _asserted = true;
}
