// The problem register — distilled from the source ledgers.
import { registerRows } from "../lib/data";
import { categoryLabel, localityLabel, pad2 } from "../lib/format";
import { CategoryNav } from "../lib/category-nav";
import { CorrectionsLink, FooterHouseLine, Masthead, SiteNav, SortScript, Tally } from "../lib/chrome";

export default function Register() {
  const rows = registerRows();

  return (
    <>
      <Masthead index />
      <SiteNav current="/" />

      <nav className="filters" aria-label="Regions">
        {"Region: "}
        <a href="/" aria-current="page">Czechia</a>
        {[" Poland", " Slovakia", " Austria", " Germany"].map((r) => (
          <span key={r}>
            {" · "}
            <span className="soon" title="Coming soon">{r.trim()}</span>
          </span>
        ))}
      </nav>

      <p>
        A register of local problems, compiled weekly from public sources — tenders,
        regulations, funding rounds, documented complaints. Every claim links to its source.
      </p>

      <CategoryNav />

      <table className="index">
        {/* visually hidden — kept in the DOM so assistive tech gets the sort order */}
        <caption>Sorted by score, descending</caption>
        <thead>
          <tr>
            <th>Problem</th><th>Category</th><th>Locality</th>
            {/* the build order is score desc — stated for AT even with JS off */}
            <th className="t-num" aria-sort="descending">Score</th><th className="t-num">Updated</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((p) => {
            const href = `/problem/${p.region}/${p.id}`;
            return (
              <tr key={p.id} className={p.status === "stale" || p.status === "solved" ? "is-solved" : undefined}>
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
        {/* the stats self-narration ("N problems on record · Czechia, pilot
            country · distilled from …") is retired (owner, 2026-08-24) */}
        <FooterHouseLine />
        <br />
        <CorrectionsLink /> ·{" "}
        <a href="/signals/funded">signal ledgers</a>
      </footer>
      <SortScript />
    </>
  );
}
