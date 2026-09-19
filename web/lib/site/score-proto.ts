// The record page's scores as sections (2026-09-17), on the ladders the owner
// approved on 2026-09-19 (SCORING.md). Every value is derived deterministically
// from the record's own fields; nothing here is stored or checked. The front
// page's card reads this module too, so the two never disagree.
//
//   The opportunity      = scores.demand                  /2
//   Why now              = scores.urgency                 /3  how close and how real the
//                          deadline is: no deadline · soft · firm · with penalties
//   Willing to pay       = scores.money                   /2  is someone paying for this
//                          job now? read from price receipts; public money only lifts it
//   Validated abroad     = scores.proof                   /3
//   Market gap           = scores.gap                     /2  more points = a more open
//                          field (the field and its rungs are unchanged; it was
//                          "Competition", whose full bar read as "heavy competition")
//   Execution difficulty = entry.level Easy 3 … Very hard 0 /3 (more points = easier),
//                          shown beside the total, never summed into it
//   Total                = the five rubric checks = scores total /12, so the record page
//                          and the front page never disagree
//
// THE V1 BRANCH. A record not yet rescored (lib/scoring-v2.ts) still carries
// urgency = deadline + a freshness point, and money = public budget nearby. For
// it, Why now and Willing to pay render exactly as they did before 2026-09-19,
// words and reasons included, because the new words would misdescribe its old
// numbers. Delete the branch with the switch.
import { priceReceipts, urgencySplit, type EntryLevel, type Problem } from "../data";
import { dimRefs } from "../scorecard";
import { entryGates } from "../format";
import { isScoringV2 } from "../scoring-v2";

/** Section keys double as the page's anchors, so the Market gap section keeps
    the key (and the `#competition` anchor) it had as Competition. */
export type ProtoKey = "opportunity" | "why-now" | "willing-to-pay" | "validated-abroad" | "competition" | "execution-difficulty";

export type ProtoScore = {
  key: ProtoKey;
  /** the section's name, as the TOC and the heading say it */
  label: string;
  /** a level word appended to the label in the TOC; unused since Market gap */
  labelSuffix?: string;
  n: number;
  max: number;
  /** the judgement word for this rung */
  word: string;
  /** one line from the data: counts, never company names */
  reason: string;
  /** false for a score shown beside the total but not summed into it */
  inTotal: boolean;
};

/** One judgement word per rung, rung 0 first — SCORING.md "PRESENTATION". */
const WORDS: Record<ProtoKey, string[]> = {
  opportunity: ["Unclear pain", "Some pain", "Clear, recurring pain"],
  "why-now": ["No deadline", "Soft deadline", "Firm deadline", "Deadline with penalties"],
  "willing-to-pay": ["No sign yet", "Some signs", "Clear signs"],
  "validated-abroad": ["Not yet", "Early abroad", "Proven once", "Proven in 2+ markets"],
  competition: ["Crowded", "Early rivals only", "Open"],
  "execution-difficulty": ["Very hard", "Hard", "Moderate", "Easy"],
};

/** The pre-2026-09-19 words, for a record not yet rescored. Why now's are
    indexed by the deadline part of its urgency, as they always were. */
const WORDS_V1: Pick<Record<ProtoKey, string[]>, "why-now" | "willing-to-pay"> = {
  "why-now": ["No deadline", "Deadline later", "Deadline soon"],
  "willing-to-pay": ["No sign yet", "Some buyers", "Already paying"],
};

const LEVEL_POINTS: Record<EntryLevel, number> = { easy: 3, moderate: 2, hard: 1, "very-hard": 0 };

/** A PAID receipt (SCORING.md MONEY): signed or awarded, dated within 24
    months of the record's `updated`. Anything else priced is an asking price. */
const PAID_BASES: ReadonlySet<string> = new Set(["signed-contract", "tender-line"]);
const PAID_WINDOW_DAYS = 730;
const daysBefore = (date: string, ref: string) => Math.round((Date.parse(ref) - Date.parse(date)) / 86_400_000);

const count = (k: number, one: string, many: string) => `${k} ${k === 1 ? one : many}`;
const clamp = (n: number, max: number) => Math.max(0, Math.min(max, n));

export function protoScores(p: Problem): ProtoScore[] {
  const v2 = isScoringV2(p.id);
  const refs = dimRefs(p);
  const comps = p.comps ?? [];
  const locals = p.locals ?? [];

  const demand = clamp(p.scores.demand, 2);
  const deadline = clamp(urgencySplit(p).deadline, 2);
  const urgency = clamp(p.scores.urgency, 3);
  const money = clamp(p.scores.money, 2);
  const proof = clamp(p.scores.proof, 3);
  const gap = clamp(p.scores.gap, 2);
  const ease = LEVEL_POINTS[p.entry.level] ?? 0;

  const nDemand = refs.demand.length;
  const nUrgency = refs.urgency.length;
  const prices = priceReceipts(p);
  const publicMoney = refs.money.filter((n) => p.sources[n - 1]?.type !== "price").length;
  const countries = new Set(comps.map((c) => c.geo)).size;
  const direct = locals.filter((l) => l.competes === "direct");
  const directEst = direct.filter((l) => l.maturity === "established").length;
  const adjacent = locals.length - direct.length;

  // v2: only a price receipt tagged `dims: [money]` is evidence of paying;
  // it is PAID when signed or awarded inside the window, else an asking price.
  const moneyReceipts = prices.filter(({ n }) => refs.money.includes(n));
  const paid = moneyReceipts.filter(({ s }) =>
    PAID_BASES.has(s.basis) && daysBefore(s.date, p.updated) >= 0 && daysBefore(s.date, p.updated) <= PAID_WINDOW_DAYS).length;
  const asked = moneyReceipts.length - paid;

  const whyNowV2 = [
    "No dated rule forces buyers to act",
    p.draft_law
      ? "The rule it rests on is not law yet"
      : "A dated rule, but far off or binding someone else",
    "An enacted rule binds these buyers within 18 months",
    "An enacted rule binds these buyers within 18 months, with penalties",
  ][urgency];

  const reasons: Record<ProtoKey, string> = {
    opportunity: nDemand
      ? `${count(nDemand, "source documents", "sources document")} the pain`
      : "No complaint or request on file yet",
    "why-now": v2
      ? urgency === 0 ? whyNowV2 : `${whyNowV2} · ${count(nUrgency, "source", "sources")}`
      : deadline === 2
        ? `A compliance date within 18 months · ${count(nUrgency, "source", "sources")}`
        : deadline === 1
          ? `A compliance date more than 18 months away · ${count(nUrgency, "source", "sources")}`
          : "No dated rule forces buyers to act",
    // (v1 only: the +1 for evidence under 90 days old is appended below)
    "willing-to-pay": v2
      ? [
          paid ? count(paid, "payment for this on file", "payments for this on file") : "",
          asked ? count(asked, "price asked", "prices asked") : "",
          publicMoney ? count(publicMoney, "sign of public money nearby", "signs of public money nearby") : "",
        ].filter(Boolean).join(" · ") || "No price or payment on file"
      : [
          prices.length ? count(prices.length, "price paid on file", "prices paid on file") : "No price paid on file",
          publicMoney ? count(publicMoney, "public contract or grant nearby", "public contracts or grants nearby") : "",
        ].filter(Boolean).join(" · "),
    "validated-abroad": comps.length
      ? `${count(comps.length, "company", "companies")} abroad, in ${count(countries, "country", "countries")}`
      : "No company abroad on file",
    competition: direct.length
      ? `${count(direct.length, "Czech seller", "Czech sellers")}, ${directEst ? `${directEst} established` : "all early"}${adjacent ? ` · ${adjacent} nearby` : ""}`
      : `No Czech seller on file${adjacent ? ` · ${adjacent} nearby sell something else` : ""}`,
    "execution-difficulty": `Set by ${entryGates(p.entry).toLowerCase()}`,
  };

  if (!v2 && urgencySplit(p).freshness) reasons["why-now"] += " · +1 for evidence under 90 days old";

  const row = (key: ProtoKey, label: string, n: number, max: number, word: string, inTotal = true): ProtoScore =>
    ({ key, label, n, max, word, reason: reasons[key], inTotal });

  return [
    row("opportunity", "The opportunity", demand, 2, WORDS.opportunity[demand]),
    row("why-now", "Why now", urgency, 3, v2 ? WORDS["why-now"][urgency] : WORDS_V1["why-now"][deadline]),
    row("willing-to-pay", "Willing to pay", money, 2, (v2 ? WORDS : WORDS_V1)["willing-to-pay"][money]),
    row("validated-abroad", "Validated abroad", proof, 3, WORDS["validated-abroad"][proof]),
    row("competition", "Market gap", gap, 2, WORDS.competition[gap]),
    row("execution-difficulty", "Execution difficulty", ease, 3, WORDS["execution-difficulty"][ease], false),
  ];
}

export const protoTotal = (rows: ProtoScore[]) => {
  const summed = rows.filter((r) => r.inTotal);
  return { n: summed.reduce((s, r) => s + r.n, 0), max: summed.reduce((s, r) => s + r.max, 0) };
};
