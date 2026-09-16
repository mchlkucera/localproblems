// /category/[slug] — one category's problems, in the modern design.
// The port of the live `/category/[slug]`: all 12 categories pre-render (slug
// == category id), the rows are `categoryRows(slug)` (register order, rejected
// excluded), and a category with no problems still has its page, with a plain
// empty line.
//
// DESIGN: the front page itself, filtered. Its row card (`Entry`) and its
// opportunity grouping (`byOpportunity`) are imported from lib/site/front, never
// copied. The page names the category once, in the heading, and draws it once,
// beside the heading; so the rows drop the per-row category and drawing
// (`showCategory={false}`), as the front page's category grouping does.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "../../styles/front.css";
import "../../styles/category.css";
import { CATEGORIES, categoryCounts, categoryRows, extractDate } from "../../../../lib/data";
import { categoryLabel } from "../../../../lib/format";
import { CORRECTIONS_MAILTO } from "../../../../lib/chrome";
import { CategoryArt } from "../../../../lib/art/category-art";
import { TopBar } from "../../../../lib/site/bar";
import { Entry, byOpportunity, item } from "../../../../lib/site/front";
import { fmtDate } from "../../../../lib/site/sources";

export const dynamicParams = false;


type Category = (typeof CATEGORIES)[number];
type Params = { params: Promise<{ slug: Category }> };

export function generateStaticParams() {
  return CATEGORIES.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { slug } = await params;
  return { title: `${categoryLabel(slug)} problems — localproblems.org` };
}

/** Every category that has a problem, plus the current one even when it has
    none, so the reader can see where they are. Plain links; the current one
    underlined. "All problems" goes back to the front page. */
function CategoryTabs({ current }: { current: Category }) {
  const counts = categoryCounts();
  return (
    <nav className="lc-tabs" aria-label="Categories">
      <a href="/">All problems</a>
      {CATEGORIES.filter((c) => counts[c] > 0 || c === current).map((c) => (
        <a key={c} href={`/category/${c}`} aria-current={c === current ? "page" : undefined}>
          {categoryLabel(c)}
        </a>
      ))}
    </nav>
  );
}

export default async function ModernCategory({ params }: Params) {
  const { slug } = await params;
  if (!(CATEGORIES as readonly string[]).includes(slug)) notFound();

  const groups = byOpportunity(categoryRows(slug).map(item));
  const date = extractDate();

  return (
    <div className="lab lf lc">
      <TopBar current="problems" />

      <main className="lf-wrap">
        <header className="lc-head">
          {/* the name alone, no filler sentence: the tabs under it say where
              the reader is, and the rows say the rest */}
          <h1>{categoryLabel(slug)} problems</h1>
          <CategoryArt category={slug} className="lc-art" />
        </header>

        <CategoryTabs current={slug} />

        {groups.length === 0 ? (
          <p className="lc-empty">
            No problems in this category on the register as of{" "}
            <time dateTime={date}>{fmtDate(date)}</time>.
          </p>
        ) : (
          groups.map((g) => (
            <section key={g.id} className="lf-sec" aria-labelledby={`${g.id}-h`}>
              <header className="lf-sec-h">
                <h2 id={`${g.id}-h`}>{g.label}</h2>
                <p>{g.items.length} {g.items.length === 1 ? "problem" : "problems"}</p>
              </header>
              <ol className="lf-entries">
                {g.items.map((it) => <Entry key={it.p.id} it={it} showCategory={false} />)}
              </ol>
            </section>
          ))
        )}
      </main>

      <footer className="lf-foot">
        <div className="lf-wrap lf-foot-in">
          <span>localproblems.org · Czechia</span>
          <a href={CORRECTIONS_MAILTO}>Report a correction</a>
        </div>
      </footer>
    </div>
  );
}
