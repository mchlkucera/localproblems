// The signal ledger view — one evidence type, one page of it.
//
// SIGNALS = the records; SOURCES = the feeds we ingest from (architecture-v3 §9).
// Shared by /signals/[type] (page 1) and /signals/[type]/[page] (pages 2…N) so
// there is exactly one ledger rendering; the route only decides which slice.
import {
  EVIDENCE_TYPES, extractDate, ledgerPages, ledgerRows,
  signalsByType, type EvidenceType, type Signal,
} from "./data";
import { categoryLabel, euro, pad2 } from "./format";
import { CORRECTIONS_MAILTO, FooterHouseLine, Masthead, Pager, SiteNav } from "./chrome";

// Both maps are Record<EvidenceType, string>, so registering a type in
// EVIDENCE_TYPES without writing its explainer is a TypeScript error. The
// checklist is self-policing by construction (architecture-v3 §13.2).
export const TITLES: Record<EvidenceType, string> = {
  funded: "Funded — companies founded and financed",
  regulation: "Regulation — triggers with dates",
  tenders: "Tenders — public money on record",
  demand: "Demand — documented complaints and unmet needs",
  hiring: "Hiring — salaries committed to the work",
};

// One serif paragraph per ledger: what this evidence is, and why it counts.
const DESCRIPTIONS: Record<EvidenceType, string> = {
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
};

const SOURCE_LABELS: Record<string, string> = {
  ted: "TED", hlidac: "CZ procurement", yc: "Y Combinator", round: "Rounds",
  "reg-scan": "Regulations", "arb-scan": "Market scan", feed: "Feed",
  "demand-scan": "Demand scan", suggest: "Google Suggest", reddit: "Reddit",
  mpsv: "MPSV vacancies",
};

/** The native `title` is the reveal — never a tooltip component — and it may
    carry a newline, exactly as the inline source markers do. Where ingest
    recorded a verbatim `quote` (§7.2) the row shows it beneath our paraphrase:
    the source's own words are the stronger receipt, and a field that reaches
    the JSONL but never reaches the page has not shipped (AC-Z3). */
function rowTitle(s: Signal): string {
  return s.quote ? `${s.summary}\n\n“${s.quote}”` : s.summary;
}

/** THE LEDGERS CARRY NO SORT SCRIPT, AND THAT IS THE POINT.
 *
 *  Sanctioned exception 3 re-sorts a register table client-side. It is honest
 *  on the register and the category pages because those tables ARE the whole
 *  record set: the script sees every row it claims to order. A paged ledger is
 *  a different animal — page 3 of 37 holds 100 of 3,612 rows, so a client sort
 *  could only ever reorder the slice while looking exactly like it had sorted
 *  the ledger. That is not a smaller feature, it is a false statement about the
 *  data, so the ledgers keep ONE order: date descending, fixed at build time,
 *  stated in the caption for assistive tech and in the crumb for everyone else.
 *
 *  If a ledger ever needs a second order, it is a second set of pre-rendered
 *  pages — never a script over one slice. */
export function Ledger({ type, page }: { type: EvidenceType; page: number }) {
  const all = signalsByType(type);
  const pages = ledgerPages(type);
  const rows = ledgerRows(type, page);
  const latest = all.map((s) => s.date).sort().at(-1);

  return (
    <>
      <Masthead />
      <SiteNav current={`/signals/${type}`} />

      <p className="crumb">
        {TITLES[type]} · {pad2(all.length)} signals on file
        {latest && <> · latest <time>{latest}</time></>}
        {/* once a ledger is more than one document, "page 03 of 37" and the
            order it is paged in are load-bearing facts about what you are
            looking at — not chrome. A single-page ledger states neither. */}
        {pages > 1 && <> · newest first · page {pad2(page)} of {pad2(pages)}</>}
      </p>

      <p>{DESCRIPTIONS[type]}</p>

      {rows.length === 0 ? (
        <p className="crumb">No signals on record in this ledger. As of <time>{extractDate()}</time>. Feed pending.</p>
      ) : (
        <table className="index">
          <colgroup>
            <col className="c-name" /><col className="c-src" /><col className="c-cat" />
            <col className="c-geo" /><col className="c-val" />
            <col className="c-date" />
          </colgroup>
          <caption>
            Sorted by date, descending · extract generated <time>{extractDate()}</time> ·
            hover a name for the recorded summary
            {pages > 1 && <> · page {pad2(page)} of {pad2(pages)}</>}
          </caption>
          <thead>
            <tr>
              <th>Name</th><th>Source</th><th>Sector</th><th>Origin</th>
              <th className="t-num">Value</th><th className="t-num">Date</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((s) => (
              <tr key={s.id} id={s.id}>
                <td className="t-title"><a href={s.url} title={rowTitle(s)}>{s.title}</a></td>
                <td className="t-cat">
                  {s.source === "arb-scan" ? s.geo_origin : SOURCE_LABELS[s.source] ?? s.source}
                  {/* §7.3: the extraction value IS the review flag — an
                      llm-fallback row is marked on the ledger for review, never
                      silently trusted. `structured` is the default and earns no
                      mark; a device that encodes nothing is slop. */}
                  {s.extraction && s.extraction !== "structured" &&
                    ` · ${s.extraction === "llm-fallback" ? "llm" : "manual"}`}
                </td>
                <td className="t-cat">{categoryLabel(s.sector)}</td>
                <td className="mono">{s.geo_origin}</td>
                <td className="t-num mono">{euro(s.money_eur)}</td>
                <td className="t-num t-date"><time>{s.date}</time></td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <Pager base={`/signals/${type}`} page={page} pages={pages} />

      <footer>
        <FooterHouseLine />
        <br />
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a> · <a href="/">problem register</a> ·{" "}
        <a href="/sources">feeds and health</a>
      </footer>
    </>
  );
}

/** Every ledger page there is, as `{ type, page }` params. Bottom-up: the
    `[page]` route has no layout above it that could generate `[type]`, so the
    child names both segments (next/docs generate-static-params). */
export function everyLedgerPage(): { type: EvidenceType; page: number }[] {
  return EVIDENCE_TYPES.flatMap((type) =>
    Array.from({ length: ledgerPages(type) }, (_, i) => ({ type, page: i + 1 })),
  );
}
