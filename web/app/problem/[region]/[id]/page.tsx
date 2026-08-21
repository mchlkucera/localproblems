// The record page — docket (dek, facts, quiet meta) · scorecard · evidence
// dialogs · fixed-role sections (problem → window → how big → who builds →
// where it works → first moves → revisions) · sources · provenance.
// Every section anchors down into receipts; absence is stated, never hidden.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, signalHref, sourceExpired, type Problem, type ProblemSource } from "../../../../lib/data";
import { annotateSourceRefs, renderBody, renderInline, repageLedgerLinks, type SourceRef } from "../../../../lib/md";
import { splitBody } from "../../../../lib/sections";
import { categoryLabel, countryName, euro, gapSurface, localityLong, pad2 } from "../../../../lib/format";
import { BANDS, DIMS, MAX, VERDICTS, bandWord, criterion, dimRefs, type Dim } from "../../../../lib/scorecard";
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

function sourceName(s: ProblemSource): { label: string; url: string | null } {
  const signal = s.signal ? getSignal(s.signal) : undefined;
  if (signal) return { label: signal.title, url: s.url };
  const host = s.url.startsWith("http") ? new URL(s.url).host.replace(/^www\./, "") : null;
  if (s.type === "gap-check") return { label: `Gap check — ${host ?? "market search (log in record source)"}`, url: s.url.startsWith("http") ? s.url : null };
  return { label: host ? `${s.type} — ${host}` : s.type, url: s.url.startsWith("http") ? s.url : null };
}

// ---- deadlines (the window) ----------------------------------------------

const DAY = 86_400_000;
const daysAfter = (iso: string, from: string) => Math.round((Date.parse(iso) - Date.parse(from)) / DAY);

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

// ---- gap-check coverage ---------------------------------------------------
// A gap-check is the receipt behind "no Czech company does this", and an
// absence claim is only worth what its coverage is worth. Three optional keys
// record that coverage — `checked` (the surfaces searched), `queries` (the
// strings actually typed) and `expires` (the check's own 90-day horizon) — and
// each renders only when it is on file: most gap-checks carry none of them,
// and a `gap: 0` record legitimately has no gap-check source at all. No key,
// no label, no dangling punctuation, nothing.

/** The staleness of a source's `expires`, as words. Display-only: `expired`
    paints the phrase stamp red via the existing `.urgent`, and that is the
    entire consequence — never a score, never a status (CONVENTIONS "THE LAW").
    Expiry is judged against extractDate(), never the wall clock. */
function Horizon({ s, ledger = false }: { s: ProblemSource; ledger?: boolean }) {
  if (!s.expires) return null;
  const gone = sourceExpired(s);
  const cls = gone ? "urgent" : undefined;
  const text = `${gone ? "expired" : "expires"} ${s.expires}`;
  // Ledger rows want a <time> (the row's own muted date voice); the rundown's
  // reference line wants a <span>, because `time` there would bulge one type
  // step out of the --fs-meta line.
  return ledger
    ? <time className={cls} dateTime={s.expires}>{text}</time>
    : <span className={cls}>{text}</span>;
}

/** What a gap-check searched and what it asked, under the exhibit's note.
    The surfaces are clerk metadata; the queries are the evidence itself, so
    they are set as the quoted strings a person typed and nothing more. */
function Coverage({ s }: { s: ProblemSource }) {
  const checked = s.checked ?? [];
  const queries = s.queries ?? [];
  if (checked.length === 0 && queries.length === 0) return null;
  return (
    <>
      {checked.length > 0 && (
        <p className="coverage">Searched {checked.map(gapSurface).join(" · ")}</p>
      )}
      {queries.length > 0 && (
        <ul className="queries">
          {queries.map((q) => <li key={q}><q>{q}</q></li>)}
        </ul>
      )}
    </>
  );
}

/** The gap-check coverage as one native-`title` reveal — the house device for
    "answer it without leaving the line" (design-language: the reveal is the
    native title, never a tooltip component). Lets the one-line sources ledger
    carry the coverage without growing the second line it is forbidden. */
function coverageTitle(s: ProblemSource): string | undefined {
  const parts = [
    ...(s.checked?.length ? [`Searched ${s.checked.map(gapSurface).join(" · ")}`] : []),
    ...(s.queries ?? []).map((q) => `“${q}”`),
  ];
  return parts.length ? parts.join("\n") : undefined;
}

/** One embedded evidence record inside a rundown dialog. External links only. */
function DialogSource({ p, n }: { p: Problem; n: number }) {
  const s = p.sources[n - 1];
  const sig = s.signal ? getSignal(s.signal) : undefined;
  const { label, url } = sourceName(s);
  const meta = [
    `S${n}`,
    sig ? sig.id : s.type,
    ...(sig ? [sig.source, sig.geo_origin] : []),
    s.date,
    ...(sig?.money_eur ? [euro(sig.money_eur)] : []),
  ].join(" · ");
  return (
    <div className="sig">
      {/* the reference line carries the exhibit's dates, so the check's own
          horizon is stated there — one date joins another, no new device */}
      <span className="meta">{meta}{s.expires && <> · <Horizon s={s} /></>}</span>
      {url ? <a className="name" href={url}>{label}</a> : <span className="name">{label}</span>}
      {/* `.note:has(+ .note)` distinguishes the source's voice from the
          register's by adjacency — coverage goes AFTER both, never between */}
      {sig && <p className="note">{sig.summary}</p>}
      <p className="note">{s.note}</p>
      <Coverage s={s} />
    </div>
  );
}

export default async function Record({ params }: Params) {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) notFound();

  const refs = dimRefs(p);
  const dimLabel = (d: Dim) => d.charAt(0).toUpperCase() + d.slice(1);
  const provenance = p.sources.filter((s) => s.signal).map((s) => s.signal!);
  const sections = splitBody(p.body);
  const extract = extractDate();
  const band = bandWord(p.score);
  const comps = p.comps ?? [];

  // Body prose renders through the ref post-pass: an explicit `[Sn]` marker —
  // or a link to a url already on the ledger — becomes the superscript
  // S-number, carrying the source's name and date for the hover reveal
  // (owner, 2026-08-19; explicit markers 2026-08-20).
  const sourceRefs: SourceRef[] = p.sources.map((s) => {
    const sig = s.signal ? getSignal(s.signal) : undefined;
    return {
      url: s.url,
      label: sourceName(s).label,
      date: s.date,
      note: s.note,
      // Seam: the ingest program is adding a verbatim `quote` to the signal
      // record. The day it lands in SignalSchema, the reveal quotes the source
      // — no change needed here or in md.ts.
      quote: (sig as { quote?: string } | undefined)?.quote,
    };
  });
  // repageLedgerLinks LAST: the body's hand-written ledger deep links
  // (`/sources/tenders#dotace-…`, and the `/signals/…` spelling) name a row,
  // and the paged ledgers moved most rows off page 1. Resolved at render time
  // against the same index that lays the pages out, so the corpus keeps its
  // stable human-written URL and no page number is ever baked into a markdown
  // file to rot the next time the ledger grows.
  const body = (md: string) =>
    repageLedgerLinks(annotateSourceRefs(renderBody(md), sourceRefs), signalHref);

  // Nearest future deadline among the urgency receipts feeds the docket Window fact.
  const windowFact = refs.urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0];

  return (
    <>
      <Masthead />
      <nav className="crumb">
        <a href="/">Problems</a> / <a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a>
      </nav>
      <SiteNav />

      <article>
        <header className="docket">
          <p className="idline">
            <span className="meta">
              {"updated "}<time className="rel" dateTime={p.updated}>{p.updated}</time>
              {" · created "}<time className="rel" dateTime={p.created}>{p.created}</time>
            </span>
          </p>
          <h1>{p.title}</h1>
          {/* The dek is the who-pays paragraph's opening sentence, lifted — so it
              renders through the same ref pass: a citation written once in the
              body still shows where the sentence is reused. */}
          {sections.dek && (
            <p className="dek" dangerouslySetInnerHTML={{ __html: repageLedgerLinks(annotateSourceRefs(renderInline(sections.dek), sourceRefs), signalHref) }} />
          )}
          <dl className="facts facts--rail">
            <div><dt>Category</dt><dd><a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a></dd></div>
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            {windowFact && <div><dt>Window</dt><dd>by <time dateTime={windowFact}>{windowFact}</time></dd></div>}
          </dl>
        </header>

        <section className="scorecard" aria-label="Scorecard — top-line dimensions, each opening its evidence">
          {DIMS.map((d) => (
            <button
              key={d}
              className={p.scores[d] === 0 ? "dim is-zero" : "dim"}
              popoverTarget={`d-${d}`}
            >
              <span className="label">{dimLabel(d)}</span>
              <span className="num">{p.scores[d]}/{MAX[d]}</span>
              <Tally s={p.scores[d]} max={MAX[d]} />
              <span className="verdict">{VERDICTS[d][p.scores[d]]}</span>
            </button>
          ))}
          <button
            className={p.score >= 10 ? "dim dim--total score-high" : "dim dim--total"}
            popoverTarget="d-total"
          >
            <span className="label">Total</span>
            <span className="num">{pad2(p.score)}/12</span>
            <Tally s={p.score} max={12} />
            <span className="verdict">{band}</span>
          </button>
        </section>

        <div aria-label="Score rundown dialogs — click a dimension above">
          {DIMS.map((d) => (
            <div key={d} className="rundown" id={`d-${d}`} popover="auto">
              <button className="x" popoverTarget={`d-${d}`} popoverTargetAction="hide" aria-label="Close">×</button>
              <header>
                <span className="label">{dimLabel(d)}</span>
                <span className="num">{p.scores[d]}/{MAX[d]}</span>
                <Tally s={p.scores[d]} max={MAX[d]} />
                <span className="verdict">{VERDICTS[d][p.scores[d]]}</span>
              </header>
              <p className="crit">{criterion(p, d)}.</p>
              {refs[d].map((n) => <DialogSource key={n} p={p} n={n} />)}
            </div>
          ))}
          <div className="rundown" id="d-total" popover="auto">
            <button className="x" popoverTarget="d-total" popoverTargetAction="hide" aria-label="Close">×</button>
            <header>
              <span className="label">Total</span>
              <span className="num">{pad2(p.score)}/12</span>
              <Tally s={p.score} max={12} />
              <span className="verdict">{band}</span>
            </header>
            <p className="crit">Five dimensions — proof, money, urgency, demand, gap — each point justified by a source on file.</p>
            <table className="bands" aria-label="Verdict bands">
              <tbody>
                {BANDS.map(([min, word], i) => (
                  <tr key={word} className={band === word ? "is-band" : undefined}>
                    <td>{band === word ? "→" : ""}</td>
                    <td>{word}</td>
                    <td>{min}–{i === 0 ? 12 : BANDS[i - 1][0] - 1}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <h2>The problem</h2>
        <div dangerouslySetInnerHTML={{ __html: body(sections.problem) }} />

        <h2>The window</h2>
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
                    /* plain mono date — the .deadline figure and T−n countdown
                       are retired (owner, 2026-08-19); .urgent inside T−14 */
                    <time dateTime={deadline} className={t < 14 ? "urgent" : undefined}>by {deadline}</time>
                  ) : (
                    <time>{s.date}</time>
                  )}
                </li>
              );
            })}
          </ul>
        )}

        <h2>How big</h2>
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

        {p.build && (
          <>
            <h2>Who builds this</h2>
            <ul className="buildfacts">
              <li>
                <span className="label">Capital</span>
                <span className="leader"></span>
                <span className="val">{p.build.capital.toUpperCase()} <span className="range">{CAPITAL_RANGE[p.build.capital]}</span></span>
              </li>
              <li>
                <span className="label">First revenue</span>
                <span className="leader"></span>
                <span className="val">{p.build.first_revenue.toUpperCase()}</span>
              </li>
              <li>
                <span className="label">Builder</span>
                <span className="leader"></span>
                <span className="val">{p.build.builder.replace("-", " ").toUpperCase()}</span>
              </li>
            </ul>
            <p className="buildnote">{p.build.note}</p>
          </>
        )}

        <h2>Where it works</h2>
        {sections.solved && <div dangerouslySetInnerHTML={{ __html: body(sections.solved) }} />}
        {comps.length > 0 ? (
          /* .works: ledger left, map right on wide viewports; narrow stacks
             map → ledger under the full-width prose (owner, 2026-08-19) */
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
                      <span className="leader"></span>
                      {c.signal && <a className="ref" href={signalHref(c.signal, sig?.type ?? "funded")}>{c.signal}</a>}
                    </span>
                    <p className="note">{c.traction}</p>
                  </li>
                );
              })}
            </ul>
          </div>
        ) : (
          <p className="absent">No verified foreign comparable on file. As of <time dateTime={p.updated}>{p.updated}</time>.</p>
        )}

        {sections.firstmoves && (
          <>
            <h2>First moves</h2>
            <div dangerouslySetInnerHTML={{ __html: body(sections.firstmoves) }} />
          </>
        )}

        {/* Revisions — the record's own audit trail, oldest first, one entry per
            date. It stays ON the record and in the reading order (never behind
            a disclosure: this page must photocopy whole), but it is set in the
            quiet register of a ledger rather than as the 4px-ruled interruption
            corrections used to be, because visible is not the same as dominant
            (owner, 2026-08-21). Each entry opens on the exhibit grammar the
            rundown already uses — full-measure row hairline, content indented,
            mono reference line — so nothing new was invented to hold it. */}
        {sections.revisions.length > 0 && (
          <>
            <h2>Revisions</h2>
            <ol className="revisions">
              {sections.revisions.map((r, i) => (
                <li key={i}>
                  {r.meta && <span className="meta">{r.meta}</span>}
                  <div dangerouslySetInnerHTML={{ __html: body(r.text) }} />
                </li>
              ))}
            </ol>
          </>
        )}

        <h2 id="sources">Sources</h2>
        <ol className="sources">
          {p.sources.map((s, i) => {
            const { label, url } = sourceName(s);
            // The ledger stays ONE line per source (design-language: no note or
            // url lines). A gap-check's coverage therefore rides the native
            // title reveal, and only its horizon — a date, which this row
            // already deals in — is spent on visible width.
            const title = coverageTitle(s);
            return (
              <li key={i} id={`s${i + 1}`}>
                {url ? <a href={url} title={title}>{label}</a> : <span title={title}>{label}</span>}
                <span className="leader"></span>
                <time dateTime={s.date}>{s.date}</time>
                {s.expires && <>·<Horizon s={s} ledger /></>}
              </li>
            );
          })}
        </ol>
      </article>

      <footer>
        Created <time>{p.created}</time> · updated <time>{p.updated}</time>
        {provenance.length > 0 && (
          <>
            {" "}· source signals:{" "}
            {provenance.map((sid, i) => {
              const sig = getSignal(sid)!;
              return <span key={sid}>{i > 0 && ", "}<a href={signalHref(sid, sig.type)}>{sid}</a></span>;
            })}
          </>
        )}{" "}
        · <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a>
        <br />
        <FooterHouseLine />
      </footer>

      <RelDatesScript />
    </>
  );
}
