// The record page — docket · scorecard · evidence dialogs · prose · sources · provenance.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getProblems, getSignal, type Problem, type ProblemSource } from "../../../../lib/data";
import { renderBody } from "../../../../lib/md";
import { categoryLabel, euro, localityLong, pad2 } from "../../../../lib/format";
import { DIMS, MAX, VERDICTS, bandWord, criterion, dimRefs, type Dim } from "../../../../lib/scorecard";
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

  return (
    <>
      <Masthead />
      <nav className="crumb">
        <a href="/">Problems</a> / {categoryLabel(p.category)} / {idUp}
      </nav>
      <SiteNav />

      <article>
        <header className="docket">
          <span className="id">{idUp}</span>
          <h1>{p.title}</h1>
          <dl className="facts">
            <div><dt>Category</dt><dd>{categoryLabel(p.category)}</dd></div>
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            <div><dt>Updated</dt><dd><time className="rel" dateTime={p.updated}>{p.updated}</time></dd></div>
            <div><dt>Created</dt><dd><time className="rel" dateTime={p.created}>{p.created}</time></dd></div>
            <div><dt>Sources</dt><dd>{pad2(p.sources.length)}</dd></div>
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
            <span className="verdict">{bandWord(p.score)}</span>
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
              <span className="verdict">{bandWord(p.score)}</span>
            </header>
            <p className="crit">
              score = proof + money + urgency + demand + gap · every point is justified by a
              source on file · bands: PRIME 10–12 · STRONG 8–9 · FAIR 5–7 · FAINT 0–4
            </p>
          </div>
        </div>

        <h2>The problem</h2>
        <div dangerouslySetInnerHTML={{ __html: renderBody(p.body) }} />

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
