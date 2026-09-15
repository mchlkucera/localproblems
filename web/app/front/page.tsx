// The front page — the register read as a newspaper (owner, 2026-09-10: "so
// that I can read thru the whole first page and see the problem at a glance,
// likely solution"). A PROTOTYPE, LOCAL ONLY: it is gated exactly like the
// private /sources admin page — `npm run dev` sets LP_ADMIN=1, a production
// build without it 404s before any data is read, so nothing here ships until
// the owner decides it should.
//
// Every line on a story is derived, never written for this page: the headline
// is the record title, the lede is the problem section's run-in lead (the same
// `splitLead` the record page uses), the likely solution is the authored
// `solution:` field (required on every record, always labelled "Likely
// solution" — never stated as known), and the glance lines are the
// scorecard's own vetted reads (`scoreRead`), so the front page can never say
// something the record page contradicts.
//
// Its CSS lives in ./front.css, scoped under `.front`, because web/shared.css is
// checksum-locked to the design-language stylesheet. If this layout is adopted
// the rules move into skills/design-language/assets/style.css as a versioned
// round and this file goes away.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "./front.css";
import { extractDate, getSignal, registerRows, type Problem, type ProblemSource } from "../../lib/data";
import { ENTRY_LEVEL_LABELS, categoryLabel, countryName, entryGates, localityLabel, pad2 } from "../../lib/format";
import { compEstablished } from "./field";
import { dimRefs, scoreRead } from "../../lib/scorecard";
import { splitBody, splitLead } from "../../lib/sections";
import { CorrectionsLink, FooterHouseLine, Masthead, RegionNav, SiteNav, Tally } from "../../lib/chrome";

export const metadata: Metadata = { title: "Front page — localproblems.org" };

/** Read inside the component — see app/sources/page.tsx for why. */
const enabled = () => process.env.LP_ADMIN === "1";

/** Markdown and citation markers out: a story is a teaser whose one link is the
    record, so it carries no nested links and no S-numbers pointing at a ledger
    that is not on this page. */
const plain = (s: string) =>
  s
    .replace(/\s*\[S\d+(?:\s*,\s*S\d+)*\]/g, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\s+/g, " ")
    .trim();

const days = (from: string, to: string) => Math.round((Date.parse(to) - Date.parse(from)) / 86_400_000);

/** Distance to a future date against the register's own extract date — never the
    wall clock, so one commit renders the same on every day. */
function out(from: string, to: string): string {
  const d = days(from, to);
  const m = Math.round(d / 30.44);
  if (m < 1) { const w = Math.max(1, Math.round(d / 7)); return `${w} wk`; }
  if (m < 12) return `${m} mo`;
  return `${Math.round((m / 12) * 10) / 10} yr`;
}

function futureDate(s: ProblemSource, extract: string): string | null {
  if (s.date > extract) return s.date;
  const sig = s.signal ? getSignal(s.signal) : undefined;
  return sig && sig.date > extract ? sig.date : null;
}

type Story = {
  p: Problem;
  href: string;
  lede: string;
  /** The record page's dek — who pays, first sentence. Lead story only. */
  dek: string;
  solution: string;
  window: string | null;
};

function story(p: Problem, extract: string): Story {
  const s = splitBody(p.body);
  const lede = plain(splitLead(s.problem).lead);
  const window = dimRefs(p).urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0] ?? null;
  return { p, href: `/problem/${p.region}/${p.id}`, lede, dek: plain(s.dek), solution: plain(p.solution), window };
}

function Kicker({ p }: { p: Problem }) {
  return (
    <p className="kicker">
      <span>{categoryLabel(p.category)} · {localityLabel(p.geo)}</span>
      <span className="score"><Tally s={p.score} /><span className="num">{pad2(p.score)}/12</span></span>
    </p>
  );
}

/** One tick per company on file: ink = passes the established test, muted =
    early. Abroad that is good news; at home it means the space is taken — the
    row label carries the flip, exactly as SCORING.md states the test. */
function Ticks({ marks }: { marks: { name: string; est: boolean }[] }) {
  if (marks.length === 0) return null;
  return (
    <span className="ticks" aria-hidden="true">
      {marks.map((m, i) => <i key={i} className={m.est ? "est" : undefined} title={m.name} />)}
    </span>
  );
}

/** HQ countries in ledger order, spelt out — ISO2 would print Norway as "NO". */
function countries(p: Problem): string {
  const names = [...new Set((p.comps ?? []).map((c) => countryName(c.geo)))];
  return names.length <= 2 ? names.join(", ") : `${names.slice(0, 2).join(", ")} +${names.length - 2}`;
}

/** The glance ledger: the field strip (ticks) beside the scorecard's own reads. */
function Glance({ st, extract }: { st: Story; extract: string }) {
  const { p } = st;
  const e = p.entry;
  const year = Number(extract.slice(0, 4));
  const abroad = (p.comps ?? []).map((c) => ({ name: c.name, est: compEstablished(c.since, c.traction, year) }));
  const home = (p.locals ?? [])
    .filter((l) => l.competes === "direct")
    .map((l) => ({ name: l.name, est: l.maturity === "established" }));
  return (
    <dl className="glance">
      <div>
        <dt>Abroad</dt>
        <dd>{abroad.length ? <><Ticks marks={abroad} />{countries(p)}</> : "none on file"}</dd>
      </div>
      <div><dt>At home</dt><dd><Ticks marks={home} />{scoreRead(p, "gap")}</dd></div>
      {st.window && (
        <div><dt>Window</dt><dd><time dateTime={st.window}>by {st.window}</time> · {out(extract, st.window)} out</dd></div>
      )}
      {/* Difficulty to enter replaced the capital/revenue Build line
          (owner, 2026-09-15). */}
      <div><dt>Entry</dt><dd>{ENTRY_LEVEL_LABELS[e.level]} · {entryGates(e)}</dd></div>
    </dl>
  );
}

/** Always "Likely solution": the register says what would probably solve the
    problem, never that it knows (owner, 2026-09-10). */
function Solution({ st }: { st: Story }) {
  return (
    <p className="fix">
      <span className="k">Likely solution</span> {st.solution}
    </p>
  );
}

export default function Front() {
  if (!enabled()) notFound();
  const extract = extractDate();
  const stories = registerRows().map((p) => story(p, extract));
  const [lead, ...rest] = stories;
  // Top stories: the ≥ 7 scorers, cut to whole rows of three so the grid never
  // ends on a lone story — the remainder joins the briefs, order unchanged.
  const strong = rest.filter((s) => s.p.score >= 7);
  const top = strong.slice(0, strong.length - (strong.length % 3));
  const briefs = rest.slice(top.length);
  // The next eight — the column is the page's calendar, not the full ledger;
  // every window still prints on its own story below.
  const windows = stories
    .filter((s): s is Story & { window: string } => s.window !== null)
    .sort((a, b) => a.window.localeCompare(b.window))
    .slice(0, 8);

  return (
    <div className="front">
      <Masthead index />
      <SiteNav current="/">
        <RegionNav />
      </SiteNav>
      {/* the strip's legend, stated once for the whole page */}
      <p className="tickkey">
        <span>One tick per company on file</span>
        <span><span className="ticks"><i className="est" /></span>established</span>
        <span><span className="ticks"><i /></span>early</span>
      </p>

      <section className="above-fold">
        <article className="story story--lead">
          <Kicker p={lead.p} />
          <h2><a href={lead.href}>{lead.p.title}</a></h2>
          <p className="lede">{lead.lede}</p>
          {lead.dek && <p className="dek">{lead.dek}</p>}
          <Solution st={lead} />
          <Glance st={lead} extract={extract} />
        </article>

        <aside className="windows" aria-label="Next deadlines">
          <h3>Next deadlines</h3>
          {windows.length === 0 ? (
            <p className="absent">No dated deadline on file.</p>
          ) : (
            <ol>
              {windows.map((s) => (
                <li key={s.p.id}>
                  <time dateTime={s.window}>{s.window}</time>
                  <span className="out">{out(extract, s.window)}</span>
                  <a href={s.href}>{s.p.title}</a>
                </li>
              ))}
            </ol>
          )}
        </aside>
      </section>

      <section className="grid" aria-label="Top stories">
        {top.map((st) => (
          <article key={st.p.id} className="story">
            <Kicker p={st.p} />
            <h2><a href={st.href}>{st.p.title}</a></h2>
            <p className="lede">{st.lede}</p>
            <Solution st={st} />
            <Glance st={st} extract={extract} />
          </article>
        ))}
      </section>

      {briefs.length > 0 && (
        <section className="briefs" aria-labelledby="briefs-h">
          <h2 id="briefs-h">In brief</h2>
          <div className="cols">
            {briefs.map((st) => (
              <article key={st.p.id} className="brief">
                <Kicker p={st.p} />
                <h3><a href={st.href}>{st.p.title}</a></h3>
                <Solution st={st} />
              </article>
            ))}
          </div>
        </section>
      )}

      <footer>
        <FooterHouseLine />
        <br />
        <CorrectionsLink /> · <a href="/">the register as a table</a>
      </footer>
    </div>
  );
}
