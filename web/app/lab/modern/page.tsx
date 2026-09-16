// /lab/modern — the register as something you read through (owner, 2026-09-15:
// "The mainpage is messy … everything after [the header] is messy and hard to
// read. Figure out a new way to present. Instead of showing preview, just
// underline the thing."). LOCAL ONLY — the /lab layout 404s every route
// without LP_ADMIN=1, and this page checks again before any data is read.
//
// THE READING CONTRACT: a reader who reads only the title and the "Suggested
// solution" of every entry has read the whole register. Where a record carries
// the headline copy (owner, 2026-09-16: `brief` and `good_for`), the entry
// reads title → the story → Suggested → Good for. The quiet line under them
// (the opportunity meter, the category) is there to be skipped.
//
// The layout is a label rail and a ruled column: the group label (opportunity
// band or category — one quiet line of links above the list
// picks which) sits in the left rail, sticky while its entries scroll past; the
// problems run down one reading column. No table columns, no preview — the
// title is the one link, stretched over its entry, so hovering or focusing
// anywhere on an entry washes it and underlines the title.
//
// Every word is derived, never written for this page: title = the record
// title, the solution = `p.solution`, the brief and "Good for" = the record's
// own optional `brief` / `good_for`, the meter and its card = `p.scores` read
// through lib/scorecard (the record page's own words), the bands = the
// SCORING.md thresholds as numbers.
import type { Metadata } from "next";
import type { ReactNode } from "react";
import { notFound } from "next/navigation";
import "./front.css";
import { registerRows, type Problem } from "../../../lib/data";
import { categoryLabel } from "../../../lib/format";
import { capitalize } from "../../../lib/sections";
import { BANDS, MAX, SCORE_ROWS, scoreRead } from "../../../lib/scorecard";
import { CORRECTIONS_MAILTO } from "../../../lib/chrome";
import { CategoryArt } from "../parts/art/category-art";
import { TopBar } from "./bar";
import { CountryWord, CountryWordMenu } from "./country";

export const metadata: Metadata = { title: "Front (lab) — localproblems.org" };

const enabled = () => process.env.LP_ADMIN === "1";

// ---- derivations (as app/front/page.tsx; only the design differs) ------------

/** Citation markers and links out: an entry's one link is the record. */
const unmark = (s: string) =>
  s
    .replace(/\s*\[S\d+(?:\s*,\s*S\d+)*\]/g, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1");

/** … and emphasis out too, for the one-paragraph solution. */
const plain = (s: string) =>
  unmark(s)
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\s+/g, " ")
    .trim();

type Item = { p: Problem; href: string; solution: string; brief: string | null; goodFor: string | null };

function item(p: Problem): Item {
  // NEW OPTIONAL FIELDS (headline copy, 2026-09-16), read through a local
  // structural type until the schema in lib/data.ts carries them. `brief` is
  // ONE sentence (owner: "3 bullets at most" — brief, Suggested, Good for).
  const h = p as { brief?: string; good_for?: string };
  return {
    p,
    href: `/lab/modern/${p.region}/${p.id}`,
    solution: plain(p.solution),
    brief: typeof h.brief === "string" && h.brief.trim() ? h.brief.trim() : null,
    goodFor: h.good_for?.trim() || null,
  };
}

// ---- grouping (owner, 2026-09-15: "bring back the grouping selector") -------
// Plain server-rendered links (`?group=`), no JS. Every grouping yields the same
// shape — a rail label, a count, entries in register order — so the sticky rail
// works identically for both. Deadline grouping was removed (owner, 2026-09-16:
// "Remove deadline sort"); `?group=deadline` and any unknown value fall back to
// Opportunity.

const GROUPINGS = [
  { key: "opportunity", label: "By opportunity" },
  { key: "category", label: "By category" },
] as const;
type GroupKey = (typeof GROUPINGS)[number]["key"];
type Group = { id: string; label: string; items: Item[]; category?: string };

/** Opportunity bands at the SCORING.md thresholds, stated as numbers — the
    band words themselves are rubric vocabulary the public pages retired. */
function byOpportunity(items: Item[]): Group[] {
  const mins = BANDS.map(([min]) => min); // [10, 8, 5, 0]
  return mins.map((min, i) => {
    const max = i === 0 ? 12 : mins[i - 1] - 1;
    return {
      id: `score-${min}`,
      label: `Opportunity ${min}–${max}`,
      items: items.filter((it) => it.p.score >= min && it.p.score <= max),
    };
  }).filter((g) => g.items.length > 0);
}

/** Categories in the order their strongest problem appears in the register. */
function byCategory(items: Item[]): Group[] {
  const order: string[] = [];
  for (const it of items) if (!order.includes(it.p.category)) order.push(it.p.category);
  return order.map((c) => ({ id: `cat-${c}`, label: categoryLabel(c), category: c, items: items.filter((it) => it.p.category === c) }));
}

// ---- pieces --------------------------------------------------------------------

/** What the register looks for, drawn: three monoline circles, the shared core
    faintly filled. r = 40, centres 58 apart; the core's corners are the three
    inner pairwise intersections. Every label sits inside the 344×160 box so the
    figure can scale down on a phone without clipping.

    Owner, 2026-09-16: "make sure we can hover over the SVG diagram showing a
    message … explaining what does it mean and why it's relevant, non-technical
    simple language". Each circle (with its label) and the core is a focusable
    part; hovering, focusing or tapping one shows its line in a card under the
    figure, and hovering the figure anywhere else shows what the whole drawing
    means. CSS only (`:has`), no client JS. The card is as wide as the figure and
    hangs from it, so it never leaves the screen. The words describe what the
    register LOOKS FOR, never a promise that every problem meets all three. */
const VENN_TIPS = [
  {
    k: "all",
    h: "What this diagram means",
    t: "Each circle is one kind of public evidence. A problem is most worth building for where all three overlap: people feel it, something is pushing buyers to act, and a similar product already sells abroad, so you aren’t guessing.",
  },
  { k: "people", h: "People want", t: "People are visibly asking for this, or complaining that it’s missing." },
  { k: "gov", h: "Government wants", t: "A new rule, a deadline or public money is pushing buyers to act." },
  { k: "abroad", h: "Works abroad", t: "A company in another country already sells this, so there is proof that buyers pay for it." },
  {
    k: "core",
    h: "Where all three meet",
    t: "The register looks for problems in this middle area. Not every problem on the list sits here; its opportunity score shows how strong the evidence is.",
  },
] as const;

function VennPart({ k, label, children }: { k: string; label: string; children: ReactNode }) {
  return (
    <g className="lf-venn-part" data-k={k} tabIndex={0} role="img" aria-label={label} aria-describedby={`lf-venn-${k}`}>
      {children}
    </g>
  );
}

function Venn() {
  return (
    <div className="lf-venn-fig">
      <svg className="lf-venn" viewBox="0 0 344 160" width="344" height="160" role="group" aria-label="What the register looks for">
        <VennPart k="people" label="People want">
          <rect className="lf-venn-hit" x="0" y="30" width="82" height="26" />
          <circle cx="124" cy="44" r="40" />
          <text x="74" y="48" textAnchor="end">People want</text>
        </VennPart>
        <VennPart k="gov" label="Government wants">
          <rect className="lf-venn-hit" x="224" y="30" width="120" height="26" />
          <circle cx="182" cy="44" r="40" />
          <text x="232" y="48">Government wants</text>
        </VennPart>
        <VennPart k="abroad" label="Works abroad">
          <rect className="lf-venn-hit" x="108" y="138" width="90" height="22" />
          <circle cx="153" cy="94.23" r="40" />
          <text x="153" y="154" textAnchor="middle">Works abroad</text>
        </VennPart>
        <VennPart k="core" label="Where all three meet">
          <path d="M143.64 55.34A40 40 0 0 1 162.36 55.34A40 40 0 0 1 153 71.55A40 40 0 0 1 143.64 55.34Z" />
        </VennPart>
      </svg>
      <div className="lf-venn-tips">
        {VENN_TIPS.map((tip) => (
          <p key={tip.k} id={`lf-venn-${tip.k}`} className="lf-venn-tip" data-k={tip.k} role="tooltip">
            <strong>{tip.h}</strong> {tip.t}
          </p>
        ))}
      </div>
    </div>
  );
}

/** The quiet selector: one line of text links, the current one in the primary
    gray and underlined. It sits just above the first rule — it belongs to the
    list, not to the header. No "Group by" label (owner, 2026-09-16: "just have
    'By opportunity' and 'By category'"): the links name themselves, and they
    start on the page's leftmost column, the rail edge ("line up 'By
    opportunity' to the leftmost column"). */
function GroupBy({ current }: { current: GroupKey }) {
  return (
    <nav className="lf-by" aria-label="Group problems by">
      <span className="lf-by-opts">
        {GROUPINGS.map((g) => (
          <a
            key={g.key}
            href={g.key === "opportunity" ? "/lab/modern" : `/lab/modern?group=${g.key}`}
            aria-current={g.key === current ? "true" : undefined}
          >
            {g.label}
          </a>
        ))}
      </span>
    </nav>
  );
}

// ---- icons ---------------------------------------------------------------------
// The icon language of /lab/paper (owner, 2026-09-16: "use icons as they're used
// in /lab/paper"): the per-category isometric drawing from ../parts/art — paper
// sets one beside each card, or in the rail when the rail already names the
// category — in one 1.25 stroke, round caps and joins, `currentColor`, a quiet
// gray. The meta line's category glyphs are drawn here in that same stroke on a
// 16-unit grid and set at 14px, on Inter's 12px x-height band.
//
// ONE GLYPH PER CATEGORY (owner, 2026-09-16: "add relevant icons instead of just
// boxes for the categories"), SOLID (owner: "choose solid icons instead of
// outlined ones"): each is a filled silhouette on the 16-unit grid, set at
// 14px in `currentColor`, with its one telling detail cut out as negative space
// (even-odd fill) so it survives being filled — the card's stripe and number
// line, the house's door, the crate's hand slot, the shield's tick, the book's
// spine, the leaf's vein, the truck's gap above its wheels. A card, a medical
// cross, a house, a bolt, a truck, a columned civic building, a shopping bag, a
// lidded crate, a shield with a tick, an open book, a leaf, and a plain dot for
// "other". Ink is kept to roughly the same density across all twelve (measured
// on the icon sheet). `lib/data.ts` CATEGORIES is the list; an unknown category
// draws the dot rather than nothing.

function Glyph({ children }: { children: ReactNode }) {
  return (
    <svg className="lf-glyph" viewBox="0 0 16 16" width="14" height="14" fill="currentColor"
      fillRule="evenodd" clipRule="evenodd" aria-hidden="true">
      {children}
    </svg>
  );
}

const CATEGORY_GLYPHS: Record<string, ReactNode> = {
  // a payment card: the stripe is a gap between its two parts, the number line a hole
  fintech: <path d="M3.5 3h9a2 2 0 0 1 2 2v.75h-13V5a2 2 0 0 1 2-2Z M1.5 7.5h13V11a2 2 0 0 1-2 2h-9a2 2 0 0 1-2-2Z M3.75 9.5v1.5h4V9.5Z" />,
  // the medical cross
  health: <path d="M6.5 1.75h3a.75.75 0 0 1 .75.75v3.25h3.25a.75.75 0 0 1 .75.75v3a.75.75 0 0 1-.75.75h-3.25v3.25a.75.75 0 0 1-.75.75h-3a.75.75 0 0 1-.75-.75v-3.25H2.5a.75.75 0 0 1-.75-.75v-3a.75.75 0 0 1 .75-.75h3.25V2.5a.75.75 0 0 1 .75-.75Z" />,
  // a house, its door cut out of the base
  housing: <path d="M7.5 1.7a.75.75 0 0 1 1 0l5.75 5.1a.75.75 0 0 1 .25.56V13.5a.75.75 0 0 1-.75.75H10V9.75H6v4.5H2.25a.75.75 0 0 1-.75-.75V7.36a.75.75 0 0 1 .25-.56Z" />,
  // a lightning bolt
  energy: <path d="M10.1 0.75L2.3 9.5h5L5.9 15.25l7.8-8.9H8.75Z" />,
  // a truck: cargo box, cab, and two wheels clear of the body
  mobility: <><path d="M1.75 3h7.5a.75.75 0 0 1 .75.75V10H1V3.75A.75.75 0 0 1 1.75 3Z M10.75 5.5h2.2a.75.75 0 0 1 .6.3l1.3 1.75a.75.75 0 0 1 .15.45V10h-4.25Z" /><circle cx="4.25" cy="12.6" r="1.65" /><circle cx="11.75" cy="12.6" r="1.65" /></>,
  // a civic building: pediment, three columns, the step
  govtech: <path d="M8 1.1L14.75 5.1H1.25Z M2.5 6.4h2.25v5.35H2.5Z M6.875 6.4h2.25v5.35h-2.25Z M11.25 6.4h2.25v5.35H11.25Z M1.25 12.75h13.5v2H1.25Z" />,
  // a shopping bag with its handle
  "retail-services": <path d="M2.35 5.5h11.3l-.72 8.3a.75.75 0 0 1-.75.7H3.82a.75.75 0 0 1-.75-.7Z M5 5.5V4.6a3 3 0 0 1 6 0v.9H9.5v-.9a1.5 1.5 0 0 0-3 0v.9Z" />,
  // a lidded crate, its hand slot cut out
  b2b: <path d="M1.75 2.25h12.5a.75.75 0 0 1 .75.75v1.75a.75.75 0 0 1-.75.75H1.75A.75.75 0 0 1 1 4.75V3a.75.75 0 0 1 .75-.75Z M2.25 6.75h11.5v6.5a.75.75 0 0 1-.75.75H3a.75.75 0 0 1-.75-.75Z M5.5 8.75v1.75h5V8.75Z" />,
  // a shield, the tick cut out
  "legal-compliance": <path d="M8 1L13.75 3.2V7.5c0 3.4-2.3 5.95-5.75 7.3C4.55 13.45 2.25 10.9 2.25 7.5V3.2Z M4.75 8.15L7.05 10.45L11.35 6.1L10.2 4.95L7.05 8.15L5.9 7Z" />,
  // an open book: two pages, the spine a gap between them
  education: <path d="M7.25 4C5.95 3.1 4.2 2.7 1.5 2.85v9.4c2.7-.15 4.45.25 5.75 1.15Z M8.75 4c1.3-.9 3.05-1.3 5.75-1.15v9.4c-2.7-.15-4.45.25-5.75 1.15Z" />,
  // a leaf, its vein cut out
  environment: <path d="M1.75 14.25C1.75 6.3 5.9 1.75 14.25 1.75C14.25 10.1 9.7 14.25 1.75 14.25Z M3.65 13.35L10.4 6.6L9.4 5.6L2.65 12.35Z" />,
  // a plain dot: no area, no false picture
  other: <circle cx="8" cy="8" r="5.25" />,
};
const CategoryGlyph = ({ category }: { category: string }) => (
  <Glyph>{CATEGORY_GLYPHS[category] ?? CATEGORY_GLYPHS.other}</Glyph>
);

// ---- an entry --------------------------------------------------------------------

/** The meter item: the bars, the score, and this record's card on hover or
    tap. It sits above the entry's stretched link, so it takes its own pointer;
    it is focusable by pointer or tap (tabIndex -1) but kept out of the tab
    order, so a keyboard reader tabs title to title. The category beside it
    has no card (owner, 2026-09-16: "remove the category hover, doesn't add
    value") — its glyph and word are plain text. */
function Meta({ id, lead, tip, children }: { id: string; lead: ReactNode; tip: ReactNode; children: ReactNode }) {
  return (
    <span className="lf-m" tabIndex={-1} aria-describedby={id}>
      {lead}
      <span>{children}</span>
      <span className="lf-m-tip lf-m-tip--wide" id={id} role="tooltip">{tip}</span>
    </span>
  );
}

/** A row of segments in the record page's favour teal: `n` of `max` filled. */
function Pips({ n, max, className }: { n: number; max: number; className: string }) {
  return (
    <span className={className} aria-hidden="true">
      {Array.from({ length: max }, (_, i) => <span key={i} className={i < n ? "on" : undefined} />)}
    </span>
  );
}

/** THIS record's five checks (owner, 2026-09-16: "on hover show specific
    information, not generic"): each check's plain label, its own bars, its
    score and the one-line read the record page prints for it — ordered as the
    record page orders them, most filled bars first, then the longer bar. */
function OpportunityCard({ p }: { p: Problem }) {
  const rows = SCORE_ROWS.map((r, i) => ({ ...r, i }))
    .sort((a, b) => p.scores[b.dim] - p.scores[a.dim] || MAX[b.dim] - MAX[a.dim] || a.i - b.i);
  return (
    <>
      <strong>Opportunity {p.score} of 12</strong>
      <span className="lf-opp">
        {rows.map(({ dim, label }) => {
          const n = p.scores[dim];
          return (
            <span key={dim} className={n === 0 ? "lf-opp-row is-zero" : "lf-opp-row"}>
              <span className="lf-opp-l">{label}</span>
              <Pips n={n} max={MAX[dim]} className="lf-pips" />
              <span className="lf-opp-n">{n}/{MAX[dim]}</span>
              <span className="lf-opp-read">{capitalize(scoreRead(p, dim))}</span>
            </span>
          );
        })}
      </span>
    </>
  );
}

/** `showCategory` is false only when the rail already names (and draws) the
    category. The whole entry is the hit area: the title is its one real link,
    stretched over the entry in CSS (owner, 2026-09-16: "make the whole page
    hoverable").

    HEADLINE COPY (owner, 2026-09-16: "put it to site", then "the visual with
    the bullets is very messy", then "too many text styles"): the title, the
    brief as a plain paragraph, then "Suggested" and "Good for", each a quiet
    label on its own line over its words — no bullets, no emphasis, three
    text styles in all. A record with neither new field is the same card with one
    property, "Suggested", so it reads as the same design, not a leftover. */
function Entry({ it, showCategory }: { it: Item; showCategory: boolean }) {
  const { p } = it;
  return (
    <li className={showCategory ? "lf-entry lf-entry--art" : "lf-entry"}>
      {/* first in source so a phone can float it beside the title */}
      {showCategory && <CategoryArt category={p.category} className="lf-art" />}
      <div className="lf-entry-body">
        <h3 className="lf-title"><a href={it.href}>{p.title}</a></h3>
        <div className="lf-copy">
          {it.brief && <p className="lf-story">{plain(it.brief)}</p>}
          <p className="lf-item"><span className="lf-item-k">Suggested</span> <span className="lf-item-v">{it.solution}</span></p>
          {it.goodFor && <p className="lf-item"><span className="lf-item-k">Good for</span> <span className="lf-item-v">{plain(it.goodFor)}</span></p>}
        </div>
        <p className="lf-meta">
          <Meta id={`${p.id}-opp`} lead={<Pips n={p.score} max={12} className="lf-meter" />} tip={<OpportunityCard p={p} />}>
            <span className="lf-sr">Opportunity </span>{p.score}/12
          </Meta>
          {showCategory && (
            <span className="lf-cat"><CategoryGlyph category={p.category} />{categoryLabel(p.category)}</span>
          )}
        </p>
      </div>
    </li>
  );
}

// ---- page ----------------------------------------------------------------------

export default async function LabFront({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  if (!enabled()) notFound();
  const q = (await searchParams).group;
  const group: GroupKey = GROUPINGS.some((g) => g.key === q) ? (q as GroupKey) : "opportunity";

  const items = registerRows().map(item);
  const groups = group === "category" ? byCategory(items) : byOpportunity(items);

  return (
    <div className="lab lf">
      <TopBar current="problems" />

      <main className="lf-wrap">
        <section className="lf-intro">
          {/* "Czech" is the country selector (owner, 2026-09-16) — a button in
              the h1, so the heading still reads "Czech problems worth solving" */}
          <h1><CountryWord /> problems worth solving</h1>
          <CountryWordMenu />
          <p className="lf-lede">
            The register looks for problems where three things meet: what people want, what government
            wants, and what already works abroad.
          </p>
          <Venn />
        </section>

        <GroupBy current={group} />

        {groups.map((g) => (
          <section key={g.id} className="lf-sec" aria-labelledby={`${g.id}-h`}>
            <header className="lf-sec-h">
              <h2 id={`${g.id}-h`}>{g.label}</h2>
              <p>{g.items.length} {g.items.length === 1 ? "problem" : "problems"}</p>
              {g.category && <CategoryArt category={g.category} className="lf-rail-art" />}
            </header>
            <ol className="lf-entries">
              {g.items.map((it) => <Entry key={it.p.id} it={it} showCategory={group !== "category"} />)}
            </ol>
          </section>
        ))}
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
