// Evidence pages — one ledger per evidence type, the provenance target
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
};

const SOURCE_LABELS: Record<string, string> = {
  ted: "TED", hlidac: "Contract registry", yc: "Y Combinator", round: "Rounds",
  "reg-scan": "Regulations", "arb-scan": "Market scan", feed: "Feed",
};

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { type } = await params;
  return { title: `${TITLES[type]} — localproblems.org` };
}

export default async function SignalsPage({ params }: Params) {
  const { type } = await params;
  const rows = signalsByType(type);
  const latest = rows.map((s) => s.date).sort().at(-1) ?? extractDate();

  return (
    <>
      <Masthead />
      <SiteNav current={`/signals/${type}`} />

      <p className="crumb">
        {TITLES[type]} · {String(rows.length).padStart(2, "0")} signals · data/signals/{type}/ ·
        latest <time>{latest}</time>
      </p>

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

      <footer>
        <FooterHouseLine />
        <br />
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a> · <a href="/">register</a>
      </footer>
    </>
  );
}
