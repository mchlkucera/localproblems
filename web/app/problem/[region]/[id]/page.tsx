// The record page — a board brief, not a dossier (owner rebuild, 2026-08-24).
// docket (id, dek, the one-line likely solution, facts, quiet meta) · a plain
// "Opportunity /12" scorecard (plain
// labels, plain reads, no verdict words, no rundown dialogs) · a builder funnel
// of plain sections: the problem → proven abroad → local competition → how big
// → why now → difficulty to enter → first moves → sources. Each scorecard cell links
// to the section carrying its evidence (v1.13, owner: "easier to scan, with
// links to read more"). Sources render as a named link + one plain
// line; the internal receipt (`note`) and the audit trail (revisions) stay in
// the markdown/git, not shouted on the page.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { extractDate, getProblems, getSignal, localHref, priceReceipts, signalHref, type Problem, type ProblemSource } from "../../../../lib/data";
import { annotateSourceRefs, renderBody, renderInline, repageLedgerLinks, type SourceRef } from "../../../../lib/md";
import { capitalize, splitBody, splitLead } from "../../../../lib/sections";
import {
  ENTRY_BUYER_LABELS, ENTRY_INCUMBENT_LABELS, ENTRY_INTEGRATION_LABELS,
  ENTRY_LEVEL_LABELS, ENTRY_MONEY_LABELS, ENTRY_PERMISSION_LABELS,
  PRICE_BASIS_LABELS, PRICE_UNIT_LABELS, categoryLabel, countryName, czk,
  euro, localityLong,
} from "../../../../lib/format";
import { type Dim, MAX, SCORE_ROWS, dimRefs, scoreRead } from "../../../../lib/scorecard";
import {
  CorrectionsLink, FooterHouseLine, Masthead, RelDatesScript, Tally,
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

/** A ledger note as scan, then dive (v1.19, owner: "each section should be
    very easy to scan and then to dive deeper"): its first clause (`clause` — a
    comp's `;`-joined traction) or first sentence (`sentence` — a local player's
    evidence) is the <summary> of a native fold, and the rest unfolds beneath
    it, capitalised as the continuation it now is. A note one unit long renders
    open, as before — there is nothing to fold. Same device as the sources gist:
    the short form IS the control; no "more" word anywhere. HTML, not script. */
function Note({ text, mode }: { text: string; mode: "sentence" | "clause" }) {
  const { lead, rest } = splitLead(text, mode);
  if (!rest) return <p className="note">{text}</p>;
  return (
    <details className="more">
      <summary>{lead}</summary>
      <p className="note">{capitalize(rest)}</p>
    </details>
  );
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

// The buildability vocabulary — CAPITAL_RANGE, FIRST_REVENUE, TEAM_BAND and
// the team-size lookup into comps[].traction — is RETIRED (owner, 2026-09-15:
// "get rid of the team predictions"; "CAPITAL €10–100k / TEAM 2–5 people is
// pretty arbitrary"). What replaced it is `entry`, whose every label lives in
// lib/format.ts with the rest of the house vocabulary.

// ---- local competition: two groups, in this order -------------------------
// DIRECT FIRST, because it is the group the score above the section is about —
// a reader who stops after one line has read the answer to "is this taken?".
// ADJACENT SECOND, and never omitted: it is who else is already in the room and
// who the buyer already pays, which is the intelligence a builder cannot get
// from a score. The headings are plain counts, in the muted mono `.crumb` voice
// the site already uses for a quiet label — so the two groups read as "3 sell
// this / 4 nearby" at a glance, with no new visual device invented for it.
const LOCAL_GROUPS: { competes: "direct" | "adjacent"; heading: (n: number) => string }[] = [
  {
    competes: "direct",
    heading: (n) => `${n} sell${n === 1 ? "s" : ""} this`,
  },
  {
    competes: "adjacent",
    heading: (n) => `${n} nearby, selling something else`,
  },
];

export default async function Record({ params }: Params) {
  const { region, id } = await params;
  const p = find(region, id);
  if (!p) notFound();

  const refs = dimRefs(p);
  const prices = priceReceipts(p);
  // A price source tagged `dims: [money]` is in refs.money too; its price row
  // below already states it, in full, so it is not printed twice in one ledger.
  const moneyRows = refs.money.filter((n) => p.sources[n - 1].type !== "price");
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
  // `lead: true` — every section's first sentence, and every first-moves
  // step's, sets as the run-in lead (v1.19): skim the headings and the leads
  // and you have read the findings; the rest of each paragraph is the evidence.
  const body = (md: string) =>
    repageLedgerLinks(annotateSourceRefs(renderBody(md, { lead: true }), sourceRefs), signalHref);

  // Nearest future deadline among the urgency receipts feeds the docket Window
  // fact and the "why now" relative line.
  const windowFact = refs.urgency
    .map((n) => futureDate(p.sources[n - 1], extract))
    .filter((d): d is string => d !== null)
    .sort()[0];

  const entry = p.entry;

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

  return (
    <>
      <Masthead />
      {/* Problems / Country / Category (owner, 2026-09-04): the register's
          hierarchy stated in full. The country has no page of its own yet —
          the register IS the Czechia register — so it is plain text until a
          per-country route exists. The site nav is gone from the record page
          (owner, same day): the crumb is the way back, and the nav's other
          half — the signal ledgers — is reached through the sources it cites. */}
      <nav className="crumb">
        <a href="/">Problems</a> / {countryName(p.region.toUpperCase())} /{" "}
        <a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a>
      </nav>

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
          {/* ONE DATE, ONCE, ON THE WHOLE PAGE (owner, 2026-08-25: "there are
              still artifacts like `Created … · updated … · Source wrong?
              Corrections →`"). Three separate passes each added a currency
              marker and none removed the one before it, so p-0032 shipped the
              same date FIVE times: here, the `.verified` line under the sources,
              twice in the footer, and once more in the site footer line. The
              reader needs exactly one answer to "how current is this?", and it
              belongs at the top, where the trust judgment is actually formed —
              so the standalone `.verified` paragraph and both footer dates are
              gone and this is the survivor.

              "VERIFIED", NOT "UPDATED": `updated` reads as a file timestamp —
              somebody touched the file — where what the date actually certifies
              is that the evidence was re-checked on that day.

              `created` IS GONE ENTIRELY. When a record was first minted is
              pipeline bookkeeping; a builder deciding what to build this quarter
              has no use for it, and git holds it. Same class of furniture as the
              record ids the owner had removed from the tables. */}
          <p className="idline">
            <span className="id">{p.id.toUpperCase()}</span>
            <span className="meta">
              {"verified "}<time className="rel" dateTime={p.updated}>{p.updated}</time>
            </span>
          </p>
          <h1>{p.title}</h1>
          {sections.dek && (
            <p className="dek" dangerouslySetInnerHTML={{ __html: repageLedgerLinks(annotateSourceRefs(renderInline(sections.dek), sourceRefs), signalHref) }} />
          )}
          {/* The likely solution — one plain sentence, directly under the dek.
              An AUTHORED frontmatter field (`solution:`, required since
              2026-09-10; it was the optional `fix:` from 2026-08-25), a NOT NULL
              column in the projection. The label is fixed and ALWAYS "Likely
              solution" (owner, 2026-09-10: "don't try to make it like we know
              everything") — the register states what would probably solve the
              problem, never that it knows. It goes through the same inline
              pipeline as the dek so an `[Sn]` marker or a ledger url inside it
              resolves rather than printing as literal text. The `.fixline`
              class keeps its name: the stylesheet is checksum-locked. */}
          <p className="fixline">
            <span className="k">Likely solution</span>
            <span dangerouslySetInnerHTML={{ __html: repageLedgerLinks(annotateSourceRefs(renderInline(p.solution), sourceRefs), signalHref) }} />
          </p>
          <dl className="facts facts--rail">
            <div><dt>Category</dt><dd><a href={`/category/${p.category}`}>{categoryLabel(p.category)}</a></dd></div>
            <div><dt>Locality</dt><dd>{localityLong(p.geo)}</dd></div>
            {windowFact && <div><dt>Window</dt><dd><time dateTime={windowFact} title={`by ${windowFact}`}>{relativeOut(extract, windowFact)}</time></dd></div>}
          </dl>
        </header>

        {/* The scorecard: "how good is this opportunity, objectively?" in one
            plain card, before a line of prose. Plain labels, plain reads, tally
            pips (more is better on every row), zero rows muted. No verdict
            words, no rundown dialogs — the receipts live in Sources.

            FIVE ROWS, AND ONLY FIVE (owner, 2026-09-15). The sixth row — the
            old Build line, latterly the difficulty-to-enter Entry line — is
            GONE: the level is not part of the /12, so inside the card it read
            as a sixth dimension of a five-dimension score. Difficulty to enter
            keeps its own section (`#difficulty-to-enter`) and its own index
            column; it just no longer poses as a score. */}
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
                    <Note text={c.traction} mode="clause" />
                  </li>
                );
              })}
            </ul>
          </div>
        ) : (
          // the "as of {p.updated}" that closed this sentence was another copy
          // of the docket's currency line; the absence is the statement, and
          // when it was last checked is answered once, at the top.
          <p className="absent">No verified foreign comparable on file.</p>
        )}

        {/* LOCAL COMPETITION — the mirror of "Proven abroad", and structured for
            the same reason: `locals[]` is what the GAP score turns on
            (SCORING.md, the established test), so it has to be a rendered fact a
            reader can check, not a clause buried in a paragraph. The ledger uses
            the comps `.entry` grammar verbatim — serif linked name, since year,
            evidence as the muted note line — with the established/early band as
            the quiet bordered `.pill` the Build row already spends on a closed
            enum. The prose paragraph renders FIRST and the ledger under it
            (owner, 2026-09-03: "Local competition should first show text and
            then the list") — every evidence section reads prose then ledger,
            the prose the scan and the ledger the dive, and this one was the
            inversion. The prose says what it means; the ledger says who.

            IT RENDERS IN TWO GROUPS, BECAUSE THE LEDGER HOLDS TWO KINDS OF ROW.
            `competes: direct` is a player selling THIS to THIS buyer;
            `competes: adjacent` is a real firm in the neighbourhood selling
            something else. Both are recorded — "never exclude, the goal is to
            inform the builder properly" (owner, 2026-08-25) — and a builder
            needs the second group as much as the first: it is who else is in
            the room, who the buyer already pays, who could turn and compete
            next quarter. But an adjacent firm printed in one undifferentiated
            list reads as a competitor the record failed to score against, which
            is how the pre-split ledger pushed one agent into mislabelling them
            `early` and the other into leaving them out. So they are LABELLED,
            not merged: direct first (it answers the score above it), each group
            opened by a plain mono count line, and the `.pill` now carries
            maturity alone — one field, one meaning, on the page as in the
            schema. */}
        {(locals.length > 0 || sections.competition) && (
          <>
            <h2 id="local-competition">Local competition</h2>
            {sections.competition && (
              <div dangerouslySetInnerHTML={{ __html: body(sections.competition) }} />
            )}
            {LOCAL_GROUPS.map(({ competes, heading }) => {
              const group = locals.filter((l) => l.competes === competes);
              if (group.length === 0) return null;
              return (
                <div key={competes} className="locals">
                  <p className="crumb">{heading(group.length)}</p>
                  <ul className="comps">
                    {group.map((l) => {
                      // ONLY THE FACTS THAT ARE ON FILE. `ico` is optional and
                      // `since` is optional on an EARLY player — small Czech
                      // vendors routinely publish no founding year — so the line
                      // is composed from what exists rather than templated over
                      // what should. A fixed template renders "· since
                      // undefined", which is the register asserting a fact it
                      // does not hold.
                      const meta = [l.ico && `IČO ${l.ico}`, l.since && `since ${l.since}`]
                        .filter(Boolean)
                        .map((s) => `· ${s}`)
                        .join(" ");
                      return (
                        <li key={l.name} className="entry">
                          <span className="line">
                            {/* localHref: the product site, or the company's
                                ARES record where no product page exists. The
                                fallback is what lets a real player with nothing
                                to link to be RECORDED rather than dropped —
                                inventing a URL is never the third option. */}
                            <a className="name" href={localHref(l)}>{l.name}</a>
                            {meta && <span>{meta}</span>}
                            <span className="leader"></span>
                            <span className="pill">{l.maturity}</span>
                          </span>
                          <Note text={l.evidence} mode="sentence" />
                        </li>
                      );
                    })}
                  </ul>
                </div>
              );
            })}
          </>
        )}

        <h2 id="how-big">How big</h2>
        {sections.howbig && <div dangerouslySetInnerHTML={{ __html: body(sections.howbig) }} />}
        {/* One ledger under the prose, two kinds of row (owner ruling,
            2026-09-03). The money receipts are PUBLIC MONEY MOVING NEAR THIS
            PROBLEM — the tenders, grants and contracts the MONEY score reads,
            with their recorded euro values. They were never an answer to "who
            pays and how much": the who-pays audit found six of the eight
            rung-1 records writing "adjacent" in their own notes. That answer
            is the PRICE RECEIPT row — one mono line per `type: price` source,
            after the money rows, in the same ruled grammar: who pays, the
            exact crown figure, per what, on what basis, dated, linked to the
            source. A price receipt IS a sized figure, so the "no sized
            figure" line renders only when the ledger has no row of either
            kind. */}
        {moneyRows.length > 0 || prices.length > 0 ? (
          <ul className="comps">
            {moneyRows.map((n) => {
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
            {prices.map(({ n, s }) => {
              const { url } = sourceName(s);
              const line = `${s.payer} pays ${czk(s.amount_czk)} ${PRICE_UNIT_LABELS[s.unit]}`;
              return (
                <li key={`price-${n}`}>
                  {url ? <a href={url}>{line}</a> : <span>{line}</span>}
                  <span className="leader"></span>
                  <span>{PRICE_BASIS_LABELS[s.basis]} · <time>{s.date}</time></span>
                </li>
              );
            })}
          </ul>
        ) : (
          <p className="absent">No sized figure on file.</p>
        )}
        {prices.length === 0 && p.score >= 7 && (
          /* The house absence line, in the ledger position, for a record worth
             a builder's quarter (score >= 7, the First-moves threshold) that no
             Czech buyer has yet priced. Stated, never estimated: the audit's
             finding was that the register's open fields are exactly its
             unpriced ones. */
          <p className="absent">
            No Czech buyer has priced this yet.
            {/* the owner's estimate of WHERE to look — never of how much */}
            {p.price_search && ` Where to look: ${p.price_search}`}
          </p>
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
        {/* "~4 months out." — the relative distance, and no longer ", as of
            2026-08-25": that trailing clause was the register re-stating its own
            extract date beside a deadline the row above already prints in full.
            The anchor for the relative reading is the one currency line in the
            docket, and it is stated once. The DEADLINE itself keeps its date —
            that is a fact about the world, not about our filing, and the two
            must not be confused when cutting furniture. */}
        {windowFact && (
          <p className="whenline">{relativeOut(extract, windowFact)}.</p>
        )}

        {/* Difficulty to enter — REPLACES "What you need" (owner, 2026-09-15:
            "include a clear difficulty to enter — e.g. app for truck people is
            easy, entering government healthcare is tough"). The capital band
            and the team band are gone: a euro range and a headcount were a
            prediction about a team nobody has met, where these five are facts
            about the market the record already carries evidence for.

            IT IS SET AS PROSE, NOT AS A LEDGER (owner, 2026-09-15, on the
            leader-dot version shipped the same morning: "should be level —
            hard — and the rest is explanatory, under it, bullet points, like
            First moves, just a simple list"; the `.buildfacts` table "looks
            different from the rest of the page"). So the section reads the way
            every other section of the funnel reads: the derived LEVEL as the
            run-in `strong.lead` of one paragraph — the same grammar the problem
            section's opener and each First-moves step already wear — with
            `entry.why` following it in the same sentence flow, then the five
            gates as a plain `ul.prose` list, each opened by its own run-in
            label. A dot-leader ledger earns its keep where a reader compares a
            column of recorded values down the page (sources, comps, the docket
            facts); five closed-enum phrases read once are not that, and the
            device was encoding nothing here. */}
        <h2 id="difficulty-to-enter">Difficulty to enter</h2>
        <p><strong className="lead">{ENTRY_LEVEL_LABELS[entry.level]}.</strong> {entry.why}</p>
        <ul className="prose">
          <li><strong className="lead">Permission</strong> — {ENTRY_PERMISSION_LABELS[entry.permission]}.</li>
          <li><strong className="lead">Who buys</strong> — {ENTRY_BUYER_LABELS[entry.buyer]}.</li>
          <li><strong className="lead">Plug into</strong> — {ENTRY_INTEGRATION_LABELS[entry.integration]}.</li>
          <li><strong className="lead">Money</strong> — {ENTRY_MONEY_LABELS[entry.money]}.</li>
          <li><strong className="lead">Already here</strong> — {ENTRY_INCUMBENT_LABELS[entry.incumbents]}.</li>
        </ul>
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
                {/* the gist — the clerk's few-word label (owner, 2026-08-25:
                    "a few word explanation and see more on a toggle") — IS the
                    fold's control (v1.19, owner: "the 'more' under Sources is
                    very repetitive and ugly"): it is the <summary> of the
                    native <details> holding the full why sentence, on its own
                    line under the name, so no word repeats down the ledger and
                    the short form opens in place into the long one. HTML, not
                    script (NEVER 13). A why with no gist renders open, no fold;
                    a gist with no why is a plain gist line. */}
                {s.gist && why ? (
                  <details className="more">
                    <summary>{s.gist}</summary>
                    <p className="why">{why}</p>
                  </details>
                ) : s.gist ? (
                  <p className="gist">{s.gist}</p>
                ) : why ? (
                  <p className="why">{why}</p>
                ) : null}
              </li>
            );
          })}
        </ol>
        {/* the "Last verified {date}" paragraph that stood here is GONE — it was
            the second of five renderings of the same date, and it rendered with
            an orphaned full stop floating after the <time>. The one currency
            marker is in the docket at the top of the page. */}
      </article>

      {/* The footer carried "Created … · updated …" — dates three and four, and
          on a record created and updated on the same day it printed one date
          twice in a single sentence. Both gone; the footer is now what a footer
          is for, which is where to write to us. */}
      <footer>
        <CorrectionsLink />
        <br />
        <FooterHouseLine />
      </footer>

      <RelDatesScript />
    </>
  );
}
