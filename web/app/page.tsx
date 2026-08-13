// The register — index.html of the gazette.
import { extractDate, registerRows, stats } from "../lib/data";
import { categoryLabel, localityLabel, pad2 } from "../lib/format";
import { FooterHouseLine, Masthead, SiteNav, StatusDot, Tally, CORRECTIONS_MAILTO } from "../lib/chrome";

export default function Register() {
  const rows = registerRows();
  const s = stats();
  const date = extractDate();

  return (
    <>
      <Masthead index />
      <SiteNav current="/" />

      <p>
        Real local problems, stated properly — with receipts. Extracted weekly from tenders,
        regulations, complaint data and foreign markets; every claim links to a source. Pick one
        that fits you, and claim it.
      </p>

      <p className="crumb">
        {s.open} open problems · Czechia, pilot country · {s.sourcesOnFile} sources on file ·{" "}
        {s.deadlinesTracked} regulatory triggers tracked
        {s.nextDeadline && (
          <>
            , next <a href={`/signals/regulation#${s.nextDeadline.id}`}><time>{s.nextDeadline.date}</time></a>
          </>
        )}{" "}
        · {s.signalCount} signals on file:{" "}
        <a href="/signals/funded">{s.byType.funded} funded</a> ·{" "}
        <a href="/signals/regulation">{s.byType.regulation} regulation</a> ·{" "}
        <a href="/signals/tenders">{s.byType.tenders} tenders</a>
      </p>

      <table className="index">
        <caption>
          Sorted by score, descending · extract generated <time>{date}</time>
        </caption>
        <thead>
          <tr>
            <th></th><th>ID</th><th>Problem</th><th>Category</th><th>Locality</th>
            <th className="t-num">Score</th><th className="t-num">Updated</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((p) => {
            const href = `/problem/${p.region}/${p.id}`;
            return (
              <tr key={p.id} className={p.status === "stale" || p.status === "solved" ? "is-solved" : undefined}>
                <td><StatusDot status={p.status} /></td>
                <td className="t-id"><a href={href}>{p.id.toUpperCase()}</a></td>
                <td className="t-title"><a href={href}>{p.title}</a></td>
                <td className="t-cat">{categoryLabel(p.category)}</td>
                <td>{localityLabel(p.geo)}</td>
                <td className="t-num">
                  <span className="score">
                    <Tally s={p.score} />
                    <span className="num">{pad2(p.score)}/12</span>
                  </span>
                </td>
                <td className="t-num t-date"><time>{p.updated}</time></td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <footer>
        <FooterHouseLine />
        <br />
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a> ·{" "}
        <a href="/signals/funded">source data</a>
      </footer>
    </>
  );
}
