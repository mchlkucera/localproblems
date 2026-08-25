// The record page — a board brief, not a dossier (owner rebuild, 2026-08-24).
// docket (id, dek, the one-line proposed fix, facts, quiet meta) · a plain
// "Opportunity /12" scorecard (plain
// labels, plain reads, no verdict words, no rundown dialogs) · a builder funnel
// of plain sections: the problem → proven abroad → local competition → how big
// → why now → what you need → first moves → sources. Each scorecard cell links
// to the section carrying its evidence (v1.13, owner: "easier to scan, with
// links to read more"). Sources render as a named link + one plain
// line; the internal receipt (`note`) and the audit trail (revisions) stay in
// the markdown/git, not shouted on the page.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, signalHref, type Problem, type ProblemSource } from "../../../../lib/data";
import { annotateSourceRefs, renderBody, renderInline, repageLedgerLinks, type SourceRef } from "../../../../lib/md";
import { splitBody } from "../../../../lib/sections";
import { categoryLabel, countryName, euro, localityLong } from "../../../../lib/format";
import { type Dim, MAX, SCORE_ROWS, dimRefs, scoreRead } from "../../../../lib/scorecard";
import {
  CORRECTIONS_MAILTO, FooterHouseLine, Masthead, RelDatesScript, SiteNav, Tally,
} from "../../../../lib/chrome";
import { EuropeMap } from "../../../../lib/geomap";

export const dynamicParams = false;

export function generateStaticParams() {
  return getProblems().map((p) => ({ region: p.region, id: p.id }));
}

type Params = { params: Promise<{ region: string; id: string }> };

function find(region: string, id: string): Problem | undefined {
  return getProblems().find((p) => p.region === region && p.id === id);
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { region, id } = await params;
  const p = find(region, id);
  return { title: p ? `${p.title} — localproblems.org` : "Record not found" };
}

// ---- source display -------------------------------------------------------
// The reader sees a plain NAME and one plain WHY. The internal `note` is the
// receipt and no longer renders. `name`/`why` override when authored; otherwise
// the source falls back to its signal's title/summary, then to its type — never
// to the raw "gap-check — host" the owner struck out.

function sourceName(s: ProblemSource): { label: string; url: string | null } {
  const url = s.url.startsWith("http") ? s.url : null;
  if (s.name) return { label: s.name, url };
  const signal = s.signal ? getSignal(s.signal) : undefined;
  if (signal) return { label: signal.title, url };
  const host = url ? new URL(url).host.replace(/^www\./, "") : null;
  if (s.type === "gap-check") return { label: host ? `Market check — ${host}` : "Market check", url };
  return { label: host ? `${s.type} — ${host}` : s.type, url };
}

/** The one plain line under a source name — what it is / why it's cited. */
function sourceWhy(s: ProblemSource): string | null {
  if (s.why) return s.why;
  const sig = s.signal ? getSignal(s.signal) : undefined;
  return sig?.summary ?? null;
}

// ---- deadlines / relative time (deterministic against extractDate) --------

const DAY = 86_400_000;
const daysAfter = (iso: string, from: string) => Math.round((Date.parse(iso) - Date.parse(from)) / DAY);

/** Plain relative distance to a future date, computed at build from the
    register's own newest `updated` (extractDate) — never the wall clock, so the
    same commit renders the same on any day (build reproducibility). */
function relativeOut(from: string, to: string): string {
  const days = daysAfter(to, from);
  if (days <= 0) return "now";
  const months = Math.round(days / 30.44);
  if (months < 1) { const w = Math.max(1, Math.round(days / 7)); return `~${w} ${w === 1 ? "week" : "weeks"} out`; }
  if (months < 12) return `~${months} months out`;
  const years = Math.round((months / 12) * 10) / 10;
  return `~${years % 1 === 0 ? years.toFixed(0) : years} years out`;
}

/** A source's forward-looking date: its own, or its signal's, when after the
    extract date — the compliance deadline a regulation source records. */
function futureDate(s: ProblemSource, extract: string): string | null {
  if (s.date > extract) return s.date;
  const sig = s.signal ? getSignal(s.signal) : undefined;
  return sig && sig.date > extract ? sig.date : null;
}

// ---- buildability vocabulary (CONVENTIONS.md capital ladder) -------------

const CAPITAL_RANGE: Record<string, string> = {
  kiosk: "<€10k", garage: "€10–100k", funded: "€100k–1M", industrial: ">€1M",
};
const FIRST_REVENUE: Record<string, string> = {
  weeks: "weeks", months: "months", "year-plus": "a year or more",
};
function builderLabel(b: string): string {
  const s = b.replace("-", " ");
  return s.charAt(0).toUpperCase() + s.slice(1);
}
/** The builder ladder as plain headcount (CONVENTIONS.md: small-team = 2–5). */
const TEAM_BAND: Record<string, string> = {
  solo: "1 person", "small-team": "2–5 people", "funded-team": "a funded team",
};

export default async function Record({ params }: Params) {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) notFound();

  const refs = dimRefs(p);
  const sections = splitBody(p.body);
  const extract = extractDate();
  const comps = p.comps ?? [];
  const locals = p.locals ?? [];

  // Body prose renders through the ref post-pass: an explicit `[Sn]` marker —
  // or a link to a url already on the ledger — becomes the superscript
  // S-number, carrying the source's name and date for the hover reveal.
  const sourceRefs: SourceRef[] = p.sources.map((s) => {
    const sig = s.signal ? getSignal(s.signal) : undefined;
    return {
      url: s.url,
      label: sourceName(s).label,
      date: s.date,
      note: s.why ?? s.note,
      quote: (sig as { quote?: string } | undefined)?.quote,
    };
  });
  const body = (md: string) =>
    repageLedgerLinks(annotateSourceRefs(renderBody(md), sourceRefs), signalHref);

  // Nearest future deadline among the urgency receipts feeds the docket Window
  // fact and the "why now" relative line.
  const windowFact = refs.urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0];

  // "Last verified" — the quiet currency marker that replaces the old wall of
  // revision prose (owner: thin and professional; the full trail stays in git).
  const lastVerified = p.updated;

  const build = p.build;

  // Scorecard "read more" targets (owner, 2026-08-24): each cell links to the
  // section of the page carrying its evidence. Gap falls back to the sources
  // ledger only when a record has NEITHER a locals[] ledger nor a
  // local-competition paragraph; demand lands on its first backing source row,
  // or on the problem when none is on file.
  const anchors: Record<Dim, string> = {
    proof: "#proven-abroad",
    gap: locals.length > 0 || sections.competition ? "#local-competition" : "#sources",
    demand: refs.demand.length ? `#s${refs.demand[0]}` : "#problem",
    money: "#how-big",
    urgency: "#why-now",
  };

  // "What you need" — team intelligence from the comps: where a comp's
  // traction string records its own headcount, that comp is the evidence and
  // gets stated and linked; where none does, the build note alone carries it.
  const teamComp = comps
    .map((c) => ({ c, m: c.traction.match(/(\d+)[-\s]person team/i) }))
    .find((x) => x.m !== null);

  return (
    <>
      <Masthead />
      <nav className="crumb">
        <a href="/">Problems</a> / <a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a>
      </nav>
      <SiteNav />

      <article>
        <header className="docket">
          {/* The record id is back on the DETAIL page (owner correction,
              2026-08-25). The 2026-08-21 removal read "no ids in the frontend"
              and stripped them everywhere; the owner meant the TABLE VIEW only.
              The id is how a record is referred to out loud — "p-0033" — and
              without it here the only place to read one was the URL bar. It
              returns as reference furniture, NOT as a headline: quiet, in the
              housekeeping meta line, never above or inside the <h1> and never
              in the crumb, which is the placement that was objected to.
              Uppercased so it reads as a reference code rather than a slug
              fragment, and set in the dormant `.docket .id` grammar the
              stylesheet has carried all along — mono 600 at --fs-meta with the
              0.08em registry tracking. NO CSS WAS ADDED: web/shared.css is
              byte-locked to skills/design-language/assets/style.css by
              web/scripts/check-css.mjs, and the rules already existed. That is
              also why the id sits BESIDE `.meta` rather than inside it: the
              stylesheet's `.docket .idline` is a space-between flex and
              `.docket .idline .meta` carries `margin-left:auto` — the pair was
              authored to put the filing number at the left margin and the
              housekeeping at the right, which is the line this restores. The
              register and category tables stay id-free — that half of the
              2026-08-21 change was right — and the ledger rows keep their
              `id` anchors. */}
          <p className="idline">
            <span className="id">{p.id.toUpperCase()}</span>
            <span className="meta">
              {"updated "}<time className="rel" dateTime={p.updated}>{p.updated}</time>
              {" · created "}<time className="rel" dateTime={p.created}>{p.created}</time>
            </span>
          </p>
          <h1>{p.title}</h1>
          {sections.dek && (
            <p className="dek" dangerouslySetInnerHTML={{ __html: repageLedgerLinks(annotateSourceRefs(renderInline(sections.dek), sourceRefs), signalHref) }} />
          )}
          {/* The proposed fix — one plain sentence naming the product, directly
              under the dek (owner, 2026-08-25). Unlike the dek, which is
              compressed out of the who-pays paragraph at build time, this is an
              AUTHORED frontmatter field: `fix:` on the record, a real column in
              the projection, a typed optional in ProblemSchema. Optional by
              design — a record with no clear product answer omits it and this
              renders nothing, which is honest; a vague fix would read worse
              than none. It goes through the same inline pipeline as the dek so
              an `[Sn]` marker or a ledger url inside it resolves rather than
              printing as literal text. */}
          {p.fix && (
            <p className="fixline">
              <span className="k">What to build</span>
              <span dangerouslySetInnerHTML={{ __html: repageLedgerLinks(annotateSourceRefs(renderInline(p.fix), sourceRefs), signalHref) }} />
            </p>
          )}
          <dl className="facts facts--rail">
            <div><dt>Category</dt><dd><a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a></dd></div>
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            {windowFact && <div><dt>Window</dt><dd><time dateTime={windowFact} title={`by ${windowFact}`}>{relativeOut(extract, windowFact)}</time></dd></div>}
          </dl>
        </header>

        {/* The scorecard: "how good is this opportunity, objectively?" in one
            plain card, before a line of prose. Plain labels, plain reads, tally
            pips (more is better on every row), zero rows muted. No verdict
            words, no rundown dialogs — the receipts live in Sources. The Build
            line sits apart: it is feasibility, not opportunity. */}
        <section className="scorecard" aria-label="Opportunity scorecard">
          <div className="hd">
            <span className="t">Opportunity</span>
            <span className="n"><b>{p.score}</b>/12</span>
          </div>
          <div className="dims">
            {/* Each row is a plain anchor to the section carrying its
                evidence (owner: "easier to scan, with links to read more").
                Rows scan straight down — label, pip meter with its figure,
                read — and the read line wears the hairline underline + a
                mono "→" so the affordance is visible at rest. No JS. */}
            {SCORE_ROWS.map(({ dim, label }) => (
              <a key={dim} className={p.scores[dim] === 0 ? "dim is-zero" : "dim"} href={anchors[dim]}>
                <span className="label">{label}</span>
                <span className="meter">
                  <Tally s={p.scores[dim]} max={MAX[dim]} />
                  <span className="num">{p.scores[dim]}/{MAX[dim]}</span>
                </span>
                <span className="read">{scoreRead(p, dim)}</span>
              </a>
            ))}
            <a className="dim dim--build" href="#what-you-need">
              <span className="label">Build</span>
              <span className="meter"><span className="pill">{builderLabel(build.builder)}</span></span>
              <span className="read">{CAPITAL_RANGE[build.capital]} · first revenue in {FIRST_REVENUE[build.first_revenue]}</span>
            </a>
          </div>
        </section>

        <h2 id="problem">The problem</h2>
        <div dangerouslySetInnerHTML={{ __html: body(sections.problem) }} />

        <h2 id="proven-abroad">Proven abroad</h2>
        {sections.solved && <div dangerouslySetInnerHTML={{ __html: body(sections.solved) }} />}
        {comps.length > 0 ? (
          <div className="works">
            <EuropeMap comps={comps.map((c) => ({ geo: c.geo, markets: c.markets }))} home={p.region} />
            <ul className="comps">
              {comps.map((c) => {
                const sig = c.signal ? getSignal(c.signal) : undefined;
                return (
                  <li key={c.name} className="entry">
                    <span className="line">
                      <a className="name" href={c.url}>{c.name}</a>
                      <span>· {countryName(c.geo)} · since {c.since}</span>
                      {/* the raw signal slug (yc-hemut) is an internal id no
                          reader wants; the company name already links out.
                          Keep the evidence cross-link, label it plainly. */}
                      <span className="leader"></span>
                      {c.signal && <a className="ref" href={signalHref(c.signal, sig?.type ?? "funded")}>evidence&nbsp;→</a>}
                    </span>
                    <p className="note">{c.traction}</p>
                  </li>
                );
              })}
            </ul>
          </div>
        ) : (
          <p className="absent">No verified foreign comparable on file as of <time dateTime={p.updated}>{p.updated}</time>.</p>
        )}

        {/* LOCAL COMPETITION — the mirror of "Proven abroad", and structured for
            the same reason: `locals[].status` is what the GAP score turns on
            (SCORING.md, the established test), so it has to be a rendered fact a
            reader can check, not a clause buried in a paragraph. The ledger uses
            the comps `.entry` grammar verbatim — serif linked name, since year,
            evidence as the muted note line — with the established/early band as
            the quiet bordered `.pill` the Build row already spends on a closed
            enum. The prose paragraph keeps rendering UNDERNEATH when a record
            states one: the ledger says who, the prose says what that means. */}
        {(locals.length > 0 || sections.competition) && (
          <>
            <h2 id="local-competition">Local competition</h2>
            {locals.length > 0 && (
              <ul className="comps">
                {locals.map((l) => {
                  // ONLY THE FACTS THAT ARE ON FILE. `ico` is optional and
                  // `since` is optional on an EARLY player — small Czech vendors
                  // routinely publish no founding year — so the line is composed
                  // from what exists rather than templated over what should. A
                  // fixed template renders "· since undefined", which is the
                  // register asserting a fact it does not hold.
                  const meta = [l.ico && `IČO ${l.ico}`, l.since && `since ${l.since}`]
                    .filter(Boolean)
                    .map((s) => `· ${s}`)
                    .join(" ");
                  return (
                    <li key={l.name} className="entry">
                      <span className="line">
                        <a className="name" href={l.url}>{l.name}</a>
                        {meta && <span>{meta}</span>}
                        <span className="leader"></span>
                        <span className="pill">{l.status}</span>
                      </span>
                      <p className="note">{l.evidence}</p>
                    </li>
                  );
                })}
              </ul>
            )}
            {sections.competition && (
              <div dangerouslySetInnerHTML={{ __html: body(sections.competition) }} />
            )}
          </>
        )}

        <h2 id="how-big">How big</h2>
        {sections.howbig && <div dangerouslySetInnerHTML={{ __html: body(sections.howbig) }} />}
        {refs.money.length > 0 ? (
          <ul className="comps">
            {refs.money.map((n) => {
              const s = p.sources[n - 1];
              const sig = s.signal ? getSignal(s.signal) : undefined;
              const { label, url } = sourceName(s);
              return (
                <li key={n}>
                  {url ? <a href={url}>{label}</a> : <span>{label}</span>}
                  <span className="leader"></span>
                  <span>{sig?.money_eur ? `${euro(sig.money_eur)} · ` : ""}<time>{s.date}</time></span>
                </li>
              );
            })}
          </ul>
        ) : (
          <p className="absent">No sized figure on file.</p>
        )}

        <h2 id="why-now">Why now</h2>
        {sections.window && <div dangerouslySetInnerHTML={{ __html: body(sections.window) }} />}
        {p.scores.urgency > 0 && refs.urgency.length > 0 && (
          <ul className="comps">
            {refs.urgency.map((n) => {
              const s = p.sources[n - 1];
              const { label, url } = sourceName(s);
              const deadline = futureDate(s, extract);
              const t = deadline ? daysAfter(deadline, extract) : 0;
              return (
                <li key={n}>
                  {url ? <a href={url}>{label}</a> : <span>{label}</span>}
                  <span className="leader"></span>
                  {deadline ? (
                    <time dateTime={deadline} className={t < 14 ? "urgent" : undefined}>by {deadline}</time>
                  ) : (
                    <time>{s.date}</time>
                  )}
                </li>
              );
            })}
          </ul>
        )}
        {windowFact && (
          <p className="whenline">{relativeOut(extract, windowFact)}, as of <time dateTime={extract}>{extract}</time>.</p>
        )}

        {/* What you need — the buy-in requirements, stated plainly (owner,
            2026-08-24): the capital band as money, the team the comps prove
            sufficient abroad (linked where a comp records its headcount),
            time to first revenue, and the build note carrying what the
            product actually demands. The scorecard Build cell lands here. */}
        <h2 id="what-you-need">What you need</h2>
        <ul className="buildfacts">
          <li>CAPITAL<span className="leader"></span><span className="val">{CAPITAL_RANGE[build.capital]}</span></li>
          <li>TEAM<span className="leader"></span>
            <span className="val">{TEAM_BAND[build.builder]}{teamComp && (
              <span className="range"> — <a href={teamComp.c.url}>{teamComp.c.name}</a> runs this with a {teamComp.m![1]}-person team</span>
            )}</span>
          </li>
          <li>FIRST REVENUE<span className="leader"></span><span className="val">in {FIRST_REVENUE[build.first_revenue]}</span></li>
        </ul>
        <p className="buildnote">{build.note}</p>
        {comps.length > 0 && (
          <p className="buildnote"><a href="#proven-abroad">See the teams doing it abroad →</a></p>
        )}

        {sections.firstmoves && (
          <>
            <h2 id="first-moves">First moves</h2>
            <div dangerouslySetInnerHTML={{ __html: body(sections.firstmoves) }} />
          </>
        )}

        <h2 id="sources">Sources</h2>
        {/* Named link + one plain line. The S-number is the row's anchor
            (id="sN") so in-body [Sn] markers still jump here, but it is no
            longer printed — a reader wants the source, not its filing number
            (owner, 2026-08-21). The receipt in `note` does not render. */}
        <ol className="sources">
          {p.sources.map((s, i) => {
            const { label, url } = sourceName(s);
            const why = sourceWhy(s);
            return (
              <li key={i} id={`s${i + 1}`}>
                <span className="line">
                  {url ? <a href={url}>{label}</a> : <span>{label}</span>}
                  <span className="leader"></span>
                  <time dateTime={s.date}>{s.date}</time>
                </span>
                {why && <p className="why">{why}</p>}
              </li>
            );
          })}
        </ol>
        <p className="verified">Last verified <time dateTime={lastVerified}>{lastVerified}</time>.</p>
      </article>

      <footer>
        Created <time>{p.created}</time> · updated <time>{p.updated}</time>
        {" "}· <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a>
        <br />
        <FooterHouseLine />
      </footer>

      <RelDatesScript />
    </>
  );
}
