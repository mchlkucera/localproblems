// Category pages — the register table filtered per category, one page per
// category id, pre-generated (SPEC.md §5). Slug == category id (CONVENTIONS.md).
import type { Metadata } from "next";
import { CATEGORIES, categoryRows, extractDate } from "../../../../lib/data";
import { ENTRY_LEVEL_LABELS, categoryLabel, countryName, entryRank, pad2 } from "../../../../lib/format";
import { CategoryNav } from "../../../../lib/category-nav";
import { CorrectionsLink, FooterHouseLine, Masthead, RegionNav, SiteNav, SortScript, Tally } from "../../../../lib/chrome";

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
      {/* Problems / Country / Category (owner, 2026-09-04) — the same hierarchy
          the record page states; the country is plain text until it has a
          route of its own. The region line rides in the nav wrapper as on the
          register: a category page is a filtered register and carries the
          same country selection. */}
      <nav className="crumb">
        <a href="/">Problems</a> / {countryName("CZ")} / {categoryLabel(slug)}
      </nav>
      <SiteNav current="/">
        <RegionNav />
      </SiteNav>
      <CategoryNav current={slug} />

      {rows.length === 0 ? (
        <p className="crumb">
          No open problems in this category as of <time>{date}</time>.
        </p>
      ) : (
        <table className="index">
          {/* visually hidden — kept in the DOM so assistive tech gets the sort order */}
          <caption>Sorted by score, descending</caption>
          <thead>
            <tr>
              <th>Problem</th><th>Category</th>
              {/* Difficulty to enter, in the index view (owner, 2026-09-15). The
                  cell sorts on its `data-sort` rank, not its text: Easy, Hard,
                  Moderate, Very hard is alphabetical nonsense. */}
              <th>Entry</th>
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
                  <td className="t-entry" data-sort={String(entryRank(p.entry.level))}>{ENTRY_LEVEL_LABELS[p.entry.level]}</td>
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
        <CorrectionsLink /> ·{" "}
        <a href="/signals/funded">signal ledgers</a>
      </footer>
      {/* an empty category renders no table — ship no script for it */}
      {rows.length > 0 && <SortScript />}
    </>
  );
}
