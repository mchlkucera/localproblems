// Source ledgers — one page per evidence type, the provenance target
// for every record footer (SPEC.md §5).
import type { Metadata } from "next";
import { EVIDENCE_TYPES, extractDate, signalsByType, type EvidenceType } from "../../../lib/data";
import { categoryLabel, euro } from "../../../lib/format";
import { CORRECTIONS_MAILTO, FooterHouseLine, Masthead, SiteNav } from "../../../lib/chrome";

export const dynamicParams = false;

export function generateStaticParams() {
  return EVIDENCE_TYPES.map((type) => ({ type }));
}

type Params = { params: Promise<{ type: EvidenceType }> };

const TITLES: Record<EvidenceType, string> = {
  funded: "Funded — companies founded and financed",
  regulation: "Regulation — triggers with dates",
  tenders: "Tenders — public money on record",
  demand: "Demand — documented complaints and unmet needs",
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
};

const SOURCE_LABELS: Record<string, string> = {
  ted: "TED", hlidac: "CZ procurement", yc: "Y Combinator", round: "Rounds",
  "reg-scan": "Regulations", "arb-scan": "Market scan", feed: "Feed",
  "demand-scan": "Demand scan", suggest: "Google Suggest", reddit: "Reddit",
};

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { type } = await params;
  return { title: `${TITLES[type]} — localproblems.org` };
}

export default async function SourcesPage({ params }: Params) {
  const { type } = await params;
  const rows = signalsByType(type);
  const latest = rows.map((s) => s.date).sort().at(-1);

  return (
    <>
      <Masthead />
      <SiteNav current={`/sources/${type}`} />

      <p className="crumb">
        {TITLES[type]} · {String(rows.length).padStart(2, "0")} signals on file
        {latest && <> · latest <time>{latest}</time></>}
      </p>

      <p>{DESCRIPTIONS[type]}</p>

      {rows.length === 0 ? (
        <p className="crumb">No signals on record in this ledger. As of <time>{extractDate()}</time>. Feed pending.</p>
      ) : (
        <table className="index">
          <colgroup>
            <col className="c-name" /><col className="c-src" /><col className="c-cat" />
            <col className="c-geo" /><col className="c-val" /><col className="c-rec" />
            <col className="c-date" />
          </colgroup>
          <caption>
            Sorted by date, descending · extract generated <time>{extractDate()}</time> ·
            hover a name for the recorded summary
          </caption>
          <thead>
            <tr>
              <th>Name</th><th>Source</th><th>Sector</th><th>Origin</th>
              <th className="t-num">Value</th><th>Record</th><th className="t-num">Date</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((s) => (
              <tr key={s.id} id={s.id}>
                <td className="t-title"><a href={s.url} title={s.summary}>{s.title}</a></td>
                <td className="t-cat">{s.source === "arb-scan" ? s.geo_origin : SOURCE_LABELS[s.source] ?? s.source}</td>
                <td className="t-cat">{categoryLabel(s.sector)}</td>
                <td className="mono">{s.geo_origin}</td>
                <td className="t-num mono">{euro(s.money_eur)}</td>
                <td className="t-id">{s.id}</td>
                <td className="t-num t-date"><time>{s.date}</time></td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <footer>
        <FooterHouseLine />
        <br />
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a> · <a href="/">problem register</a>
      </footer>
    </>
  );
}
