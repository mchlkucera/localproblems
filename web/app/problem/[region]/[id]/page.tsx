// The record page — docket (dek, facts, quiet meta) · scorecard · evidence
// dialogs · fixed-role sections (problem → window → how big → who builds →
// where it works → first moves → record updates) · sources · provenance.
// Every section anchors down into receipts; absence is stated, never hidden.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, type Problem, type ProblemSource } from "../../../../lib/data";
import { renderBody } from "../../../../lib/md";
import { splitBody } from "../../../../lib/sections";
import { categoryLabel, euro, localityLong, pad2 } from "../../../../lib/format";
import { BANDS, DIMS, MAX, VERDICTS, bandWord, criterion, dimRefs, type Dim } from "../../../../lib/scorecard";
import {
  CORRECTIONS_MAILTO, FooterHouseLine, Masthead, RelDatesScript, SiteNav, Tally,
} from "../../../../lib/chrome";

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
  return { title: p ? `${p.id.toUpperCase()} · ${p.title} — localproblems.org` : "Record not found" };
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
      <span className="meta">{meta}</span>
      {url ? <a className="name" href={url}>{label}</a> : <span className="name">{label}</span>}
      {sig && <p className="note">{sig.summary}</p>}
      <p className="note">{s.note}</p>
    </div>
  );
}

export default async function Record({ params }: Params) {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) notFound();

  const refs = dimRefs(p);
  const idUp = p.id.toUpperCase();
  const dimLabel = (d: Dim) => d.charAt(0).toUpperCase() + d.slice(1);
  const provenance = p.sources.filter((s) => s.signal).map((s) => s.signal!);
  const sections = splitBody(p.body);
  const extract = extractDate();
  const band = bandWord(p.score);
  const comps = p.comps ?? [];

  // Nearest future deadline among the urgency receipts feeds the docket Window fact.
  const windowFact = refs.urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0];

  return (
    <>
      <Masthead />
      <nav className="crumb">
        <a href="/">Problems</a> / <a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a> / {idUp}
      </nav>
      <SiteNav />

      <article>
        <header className="docket">
          <span className="id">{idUp}</span>
          <h1>{p.title}</h1>
          {sections.dek && <p className="dek">{sections.dek}</p>}
          <dl className="facts">
            <div><dt>Category</dt><dd><a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a></dd></div>
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            {windowFact && <div><dt>Window</dt><dd>by <time dateTime={windowFact}>{windowFact}</time></dd></div>}
          </dl>
          <p className="meta">
            {p.sources.length > 1 ? `S01–S${pad2(p.sources.length)}` : "S01"} on file
            {" · updated "}<time className="rel" dateTime={p.updated}>{p.updated}</time>
            {" · created "}<time className="rel" dateTime={p.created}>{p.created}</time>
          </p>
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
        <div dangerouslySetInnerHTML={{ __html: renderBody(sections.problem) }} />

        <h2>The window</h2>
        {sections.window && <div dangerouslySetInnerHTML={{ __html: renderBody(sections.window) }} />}
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
                    <span className={t < 14 ? "deadline urgent" : "deadline"}>by {deadline} · T−{pad2(t)}</span>
                  ) : (
                    <time>{s.date}</time>
                  )}
                </li>
              );
            })}
          </ul>
        )}

        <h2>How big</h2>
        {sections.howbig && <div dangerouslySetInnerHTML={{ __html: renderBody(sections.howbig) }} />}
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
            <dl className="facts">
              <div>
                <dt>Capital</dt>
                <dd>{p.build.capital.toUpperCase()} <span className="range">{CAPITAL_RANGE[p.build.capital]}</span></dd>
              </div>
              <div><dt>First revenue</dt><dd>{p.build.first_revenue.toUpperCase()}</dd></div>
              <div><dt>Builder</dt><dd>{p.build.builder.replace("-", " ").toUpperCase()}</dd></div>
            </dl>
            <p className="buildnote">{p.build.note}</p>
          </>
        )}

        <h2>Where it works</h2>
        {sections.solved && <div dangerouslySetInnerHTML={{ __html: renderBody(sections.solved) }} />}
        {comps.length > 0 ? (
          <ul className="comps">
            {comps.map((c) => {
              const sig = c.signal ? getSignal(c.signal) : undefined;
              return (
                <li key={c.name} className="entry">
                  <span className="line">
                    <a className="name" href={c.url}>{c.name}</a>
                    <span>· {c.geo} · since {c.since}</span>
                    <span className="leader"></span>
                    {c.signal && <a className="ref" href={`/sources/${sig?.type ?? "funded"}#${c.signal}`}>{c.signal}</a>}
                  </span>
                  <p className="note">{c.traction}</p>
                </li>
              );
            })}
          </ul>
        ) : (
          <p className="absent">No verified foreign comparable on file. As of <time dateTime={p.updated}>{p.updated}</time>.</p>
        )}

        {sections.firstmoves && (
          <>
            <h2>First moves</h2>
            <div dangerouslySetInnerHTML={{ __html: renderBody(sections.firstmoves) }} />
          </>
        )}

        {sections.updates.length > 0 && (
          <>
            <h2>Record updates</h2>
            {sections.updates.map((u, i) =>
              u.startsWith("**CORRECTION") ? (
                <div key={i} className="correction" dangerouslySetInnerHTML={{ __html: renderBody(u) }} />
              ) : (
                <div key={i} dangerouslySetInnerHTML={{ __html: renderBody(u) }} />
              ),
            )}
          </>
        )}

        <h2 id="sources">Sources</h2>
        <ol className="sources">
          {p.sources.map((s, i) => {
            const { label, url } = sourceName(s);
            return (
              <li key={i} id={`s${i + 1}`}>
                {url ? <a href={url}>{label}</a> : <span>{label}</span>}
                <span className="leader"></span>
                <time>{s.date}</time>
              </li>
            );
          })}
        </ol>
      </article>

      <footer>
        Record {idUp} · created <time>{p.created}</time> · updated <time>{p.updated}</time>
        {provenance.length > 0 && (
          <>
            {" "}· source signals:{" "}
            {provenance.map((sid, i) => {
              const sig = getSignal(sid)!;
              return <span key={sid}>{i > 0 && ", "}<a href={`/sources/${sig.type}#${sid}`}>{sid}</a></span>;
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
