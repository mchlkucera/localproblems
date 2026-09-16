// The signal ledgers: what each evidence type is called, what it is, and how
// its pages are laid out. SIGNALS = the records; SOURCES = the feeds we ingest
// from (architecture-v3 §9). The ledger view itself is lib/site/ledger.tsx,
// shared by /signals/[type] (page 1) and /signals/[type]/[page] (pages 2…N).
import { EVIDENCE_TYPES, ledgerPages, type EvidenceType } from "./data";

// Both maps are Record<EvidenceType, string>, so registering a type in
// EVIDENCE_TYPES without writing its explainer is a TypeScript error. The
// checklist is self-policing by construction (architecture-v3 §13.2).
export const TITLES: Record<EvidenceType, string> = {
  funded: "Funded — companies founded and financed",
  regulation: "Regulation — triggers with dates",
  tenders: "Tenders — public money on record",
  demand: "Demand — documented complaints and unmet needs",
  hiring: "Hiring — salaries committed to the work",
  asks: "Asks — problems stated by their owners",
};

// One serif paragraph per ledger: what this evidence is, and why it counts.
export const DESCRIPTIONS: Record<EvidenceType, string> = {
  funded:
    "Companies founded and financed elsewhere. A funded business that works is the strongest evidence a problem is real and someone pays to solve it. Where no local equivalent exists, that absence is the arbitrage this register hunts.",
  regulation:
    "Obligations written into law, each with a date. Regulation is the only signal that says when a market opens: demand arrives on schedule, and enforcement makes it non-optional.",
  tenders:
    "Public money in motion — tenders, signed contracts, open subsidy calls. Each row proves somebody pays: for what, at what scale, with the buyer's name on record.",
  demand:
    "Documented complaints and unmet needs — audit findings, ombudsman inventories, petitions with counts, live shortage data. They prove the pain is real before any market exists. Bottom-up evidence is noisy, so the ledger admits pain language only, never engagement metrics.",
  hiring:
    "Vacancies aggregated by theme and employer — the salary bill a market is already paying to do the work by hand. A posting is direct evidence that a task is real, recurring and unautomated: somebody costed it and hired for it. Postings are aggregated because a single vacancy is immaterial and reposting is endemic; one is recorded alone only when the posting itself is the evidence.",
  asks:
    "Problems stated outright by the institutions that own them. A ministry, a hospital or a city publicly names a problem it wants solved and invites solutions — before any procurement money is attached, which is why an ask is evidence and not yet a tender. The record is the statement and who made it; prizes, team counts and winners are engagement, not pain, and are never scored.",
};

export const SOURCE_LABELS: Record<string, string> = {
  ted: "TED", hlidac: "CZ procurement", yc: "Y Combinator", round: "Rounds",
  "reg-scan": "Regulations", "arb-scan": "Market scan", feed: "Feed",
  "demand-scan": "Demand scan", suggest: "Google Suggest", reddit: "Reddit",
  mpsv: "MPSV vacancies", tacr: "TA ČR needs", hackathon: "Hackathon challenge",
};

/** Every ledger page there is, as `{ type, page }` params. Bottom-up: the
    `[page]` route has no layout above it that could generate `[type]`, so the
    child names both segments (next/docs generate-static-params). */
export function everyLedgerPage(): { type: EvidenceType; page: number }[] {
  return EVIDENCE_TYPES.flatMap((type) =>
    Array.from({ length: ledgerPages(type) }, (_, i) => ({ type, page: i + 1 })),
  );
}
