// The problem register — distilled from the source ledgers.
import { extractDate, registerRows, stats, EVIDENCE_TYPES } from "../lib/data";
import { categoryLabel, localityLabel, pad2 } from "../lib/format";
import { CategoryNav } from "../lib/category-nav";
import { FooterHouseLine, Masthead, SiteNav, Tally, CORRECTIONS_MAILTO } from "../lib/chrome";

export default function Register() {
  const rows = registerRows();
  const s = stats();
  const date = extractDate();

  return (
    <>
      <Masthead index />
      <SiteNav current="/" />

      <p>
        Real local problems, stated properly. Distilled weekly from public sources — tenders,
        regulations, funding rounds, documented complaints. Every claim links to its source.
      </p>

      <p className="crumb">
        {s.open} problems on record · Czechia, pilot country · distilled from{" "}
        {s.signalCount} source signals:{" "}
        {EVIDENCE_TYPES.map((t, i) => (
          <span key={t}>
            {i > 0 && " · "}
            <a href={`/sources/${t}`}>{s.byType[t]} {t}</a>
          </span>
        ))}
        {s.nextDeadline && (
          <>
            {" "}· next regulatory deadline{" "}
            <a href={`/sources/regulation#${s.nextDeadline.id}`}><time>{s.nextDeadline.date}</time></a>
          </>
        )}
      </p>

      <CategoryNav />

      <table className="index">
        <caption>
          Sorted by score, descending · extract generated <time>{date}</time>
        </caption>
        <thead>
          <tr>
            <th>ID</th><th>Problem</th><th>Category</th><th>Locality</th>
            <th className="t-num">Score</th><th className="t-num">Updated</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((p) => {
            const href = `/problem/${p.region}/${p.id}`;
            return (
              <tr key={p.id} className={p.status === "stale" || p.status === "solved" ? "is-solved" : undefined}>
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
        <a href="/sources/funded">source ledgers</a>
      </footer>
    </>
  );
}
