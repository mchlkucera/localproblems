// Category pages — the register table filtered per category, one page per
// category id, pre-generated (SPEC.md §5). Slug == category id (CONVENTIONS.md).
import type { Metadata } from "next";
import { CATEGORIES, categoryRows, extractDate } from "../../../lib/data";
import { categoryLabel, localityLabel, pad2 } from "../../../lib/format";
import { CategoryNav } from "../../../lib/category-nav";
import { CORRECTIONS_MAILTO, FooterHouseLine, Masthead, SiteNav, SortScript, Tally } from "../../../lib/chrome";

export const dynamicParams = false;

export function generateStaticParams() {
  return CATEGORIES.map((slug) => ({ slug }));
}

type Category = (typeof CATEGORIES)[number];
type Params = { params: Promise<{ slug: Category }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { slug } = await params;
  return { title: `${categoryLabel(slug)} — localproblems.org` };
}

export default async function CategoryPage({ params }: Params) {
  const { slug } = await params;
  const rows = categoryRows(slug);
  const date = extractDate();

  return (
    <>
      <Masthead />
      <nav className="crumb">
        <a href="/">Problems</a> / {categoryLabel(slug)}
      </nav>
      <SiteNav current="/" />
      <CategoryNav current={slug} />

      {rows.length === 0 ? (
        <p className="crumb">
          No open problems on record in this category. As of <time>{date}</time>.
        </p>
      ) : (
        <table className="index">
          <caption>
            Sorted by score, descending · extract generated <time>{date}</time>
          </caption>
          <thead>
            <tr>
              <th>ID</th><th>Problem</th><th>Category</th><th>Locality</th>
              {/* the build order is score desc — stated for AT even with JS off */}
              <th className="t-num" aria-sort="descending">Score</th><th className="t-num">Updated</th>
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
      )}

      <footer>
        <FooterHouseLine />
        <br />
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a> ·{" "}
        <a href="/signals/funded">signal ledgers</a> · <a href="/sources">feeds and health</a>
      </footer>
      {/* an empty category renders no table — ship no script for it */}
      {rows.length > 0 && <SortScript />}
    </>
  );
}
