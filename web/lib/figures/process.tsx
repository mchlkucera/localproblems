// lib/figures — the process a record describes, told as one picture: THE HUB.
//
// ProcessSteps is the one process figure on the record page: it sits inside the
// Suggested solution box, carries no section heading, and returns null without
// `process` or with < 2 drawable steps.
//
// THE OWNER'S PICK (2026-09-18, "The hub is good"): "imagine this person has to
// interact here, this there, this there vs how they interact with one
// provider". Two blocks, stacked at every width:
//
//   Today        each person, wired to their OWN place: a small box naming it
//                in the step's own words ("free text", "phones · e-mail · old
//                dispatch software"). N wires, N boxes.
//   With the suggested solution
//                every person the solution touches, wired by one bracket into
//                ONE teal box ("One system", or "One provider"). What the
//                system itself now does is listed inside that box. A step the
//                solution leaves alone keeps its own wire and its own box, gray.
//
// When the solution replaces the sellers rather than giving people a tool (the
// after lines name a "provider"), the hub is the BUYER — the step whose actor
// is an organisation — and today's boxes are the sellers it deals with, one
// wire each; after, one wire to one provider.
//
// THE WIRES ARE ONE GRID (owner, 2026-09-18: "the ticks don't meet the
// bracket"). Three columns: people · a 32px wire column · places. Every tick
// starts at the wire column's left edge, the bracket runs inside that column
// from the first tick to the last, and the join to the one box leaves it at
// the box's own vertical centre. Rows in a bracketed block are EQUAL height
// (grid-auto-rows: 1fr), so each tick sits at its row's centre and the
// bracket's midpoint IS the centre of the rows it spans, where the box sits.
// It holds at any wrap and at 375px, with no script.
//
// HONEST ABSENCE: a step whose actor is unknown ("?") is never drawn as a
// person; its open question is one muted line under the figure. A step nobody
// does today is a dashed row, labelled plainly. The figure invents no system
// and no product: places are the record's own words (role-icons.tsx).
//
// The picture is aria-hidden; the visually hidden list under it carries every
// step's full text, in order.
import type { CSSProperties, ReactNode } from "react";
import type { ProblemSource } from "../data";
import type { CiteCtx } from "../site/cite";
import { uncited } from "./cites";
import { ObjIcon, OneIcon, RoleIcon, placeOf, roleOf, type Obj, type Role } from "./role-icons";
import type { ProcessField, ProcessStep } from "./types";

type Props = {
  /** The record's `process` field; absent → the component renders nothing. */
  process?: ProcessField | null;
  /** `p.sources` — kept for a uniform call site. */
  sources: readonly ProblemSource[];
  /** The record page's citation context — kept for a uniform call site. */
  ctx?: CiteCtx;
};

/** "A consultant who writes…" → "Consultant who writes…". */
function shortWho(who: string): string {
  const w = who.trim().replace(/^(a|an|the)\s+/i, "");
  return w.charAt(0).toUpperCase() + w.slice(1);
}
/** the name on a node: the role noun, without its "who …" clause (the node's
    own line says what they do) */
const nameOf = (who: string) => shortWho(who).replace(/\s+who\s+.*$/i, "");
/** A step's own words, markers stripped, with no full stop: these are phrases
    inside a figure, never sentences. */
const phrase = (t: string | null | undefined) => (t ? uncited(t).trim().replace(/[.;]+$/, "") : "");
const upFirst = (t: string) => t.charAt(0).toUpperCase() + t.slice(1);
const changed = (s: ProcessStep) => s.change === "changes" || s.change === "new";

/** The register's process voice is third person and present tense, so the verb
    is what tells a named subject from an implied one: the lexicon of verbs the
    pipeline's process lines actually use. */
const VERB = new Set([
  "answers", "are", "arranges", "become", "becomes", "captures", "carries", "checks", "confirms",
  "describe", "describes", "does", "do", "drafts", "fills", "files", "get", "gets", "go", "goes",
  "handles", "invoices", "is", "keep", "keeps", "makes", "make", "prepares", "produces", "proposes",
  "reads", "read", "registers", "runs", "sells", "sends", "shows", "signs", "stores", "takes",
  "writes", "write",
]);
const bare = (w: string) => w.replace(/[^A-Za-z-]/g, "").toLowerCase();

/** Who acts in a changed step's `after` line, in the record's own words:
    · a step the solution ADDS names its actor in `who`;
    · a line opening on a verb has the step's today actor as its subject;
    · otherwise the words before the first verb, when they name a role.
    A subject that is paperwork ("Those same two documents…") has no actor. */
function afterActor(s: ProcessStep): { role: Role | null; name: string; what: string } {
  const who = s.who.trim();
  const text = phrase(s.after);
  const words = text.split(/\s+/).filter(Boolean);
  const vi = words.findIndex((w) => VERB.has(bare(w)));
  if (s.change === "new" && who !== "?") return { role: roleOf(who), name: nameOf(who), what: upFirst(text) };
  if (vi === 0 && who !== "?" && roleOf(who) !== "nobody") return { role: roleOf(who), name: nameOf(who), what: upFirst(text) };
  if (vi > 0) {
    const subj = words.slice(0, vi).join(" ");
    const role = roleOf(subj);
    if (role !== "person") return { role, name: nameOf(subj), what: upFirst(words.slice(vi).join(" ")) };
  }
  return { role: null, name: "", what: upFirst(text) };
}

/** The one box's name, in the record's own words: the first qualified system
    ("the hospital system") or provider ("One fixed-price provider") an after
    line names, plus the templates it holds when a line names them. Otherwise
    "One piece of software" when a line names software, else "One system" /
    "One provider": never an invented product. */
function oneLabel(lines: string[], kind: "system" | "provider"): string {
  const text = lines.join(" · ");
  if (kind === "provider") {
    const m = /\b(?:one\s+)?(?:[a-z-]+\s+)?provider\b/i.exec(text);
    return m && !/^(the|same)\b/i.test(m[0]) ? upFirst(m[0]) : "One provider";
  }
  const m = /\b(?:the\s+)?([a-z-]+)\s+system\b/i.exec(text);
  const base = m && !/^(one|same|a|an)$/i.test(m[1]) ? `${upFirst(m[1])} system`
    : /\bsoftware\b/i.test(text) ? "One piece of software" : "One system";
  const t = /\b((?:[a-z-]+\s+)?template)s?\b/i.exec(text);
  return t ? `${base} with ${t[1]}s` : base;
}

/** An open question as one plain line: "Not known: …". A step whose actor is
    unknown but whose action is known reads "Not known: who …". */
function notKnown(s: ProcessStep): string {
  const t = phrase(s.today);
  if (!t) return "";
  const m = /^(.*?),?\s+(?:is|are)\s+not\s+known$/i.exec(t);
  const lower = (x: string) => (/^[A-Z][a-z]/.test(x) ? x.charAt(0).toLowerCase() + x.slice(1) : x);
  if (m) return `Not known: ${lower(m[1])}.`;
  if (s.who.trim() === "?") return `Not known: who ${lower(t)}.`;
  return `Not known: ${lower(t)}.`;
}

type Place = { objs: Obj[]; words: string } | null;
type Node = { role: Role; name: string; say: string; dash?: boolean };
type Row = { node: Node; place?: Place; spoke?: Node };

// ---- drawing ------------------------------------------------------------------

function Person({ n, teal }: { n: Node; teal?: boolean }) {
  return (
    <span className={`lk-hb-p${n.dash ? " is-dash" : ""}${teal ? " is-teal" : ""}`}>
      <span className="lk-hb-ic"><RoleIcon role={n.role} /></span>
      <span className="lk-hb-tx"><b>{n.name}</b>{n.say && <span>{n.say}</span>}</span>
    </span>
  );
}
function PlaceBox({ p }: { p: Place }) {
  if (!p) return <span className="lk-hb-place is-dash" />;
  return (
    <span className="lk-hb-place">
      <span className="lk-hb-objs">{p.objs.map((o, i) => <ObjIcon key={i} obj={o} />)}</span>
      <span className="lk-hb-pw">{p.words}</span>
    </span>
  );
}
function One({ kind, label, duties }: { kind: "system" | "provider"; label: string; duties: string[] }) {
  return (
    <span className="lk-hb-one">
      <span className="lk-hb-oh"><OneIcon kind={kind} /><b>{label}</b></span>
      {duties.map((d, i) => <span key={i} className="lk-hb-od">{d}</span>)}
    </span>
  );
}
const at = (r: number, r2?: number) => ({ gridRow: r2 ? `${r} / ${r2}` : r }) as CSSProperties;
const pos = (i: number, n: number) => (n === 1 ? " is-only" : i === 0 ? " is-first" : i === n - 1 ? " is-last" : "");

/** each person, wired straight to their own place */
function Pairs({ rows, quiet }: { rows: Row[]; quiet?: boolean }) {
  return (
    <div className={`lk-hb-grid${quiet ? " is-quiet" : ""}`}>
      {rows.map((r, i) => (
        <span key={i} className="lk-hb-row" style={at(i + 1)}>
          <Person n={r.node} />
          {r.place !== undefined && <span className={`lk-hb-c is-pair${r.place ? "" : " is-dash"}`} />}
          {r.place !== undefined && <span className="lk-hb-cell"><PlaceBox p={r.place} /></span>}
        </span>
      ))}
    </div>
  );
}

// ---- the figure ---------------------------------------------------------------

export function ProcessSteps({ process, sources, ctx }: Props): ReactNode {
  if (!process || process.steps.length < 2) return null;
  void sources; void ctx;
  const all = process.steps;
  // an unknown actor is never a person on the figure (owner, 2026-09-18:
  // "What does 'Not known' mean? why is it there?")
  const known = all.filter((s) => s.who.trim() !== "?");
  if (known.length < 2) return null;

  const isProvider = all.some((s) => changed(s) && /\bprovider\b/i.test(s.after ?? ""));
  const hubStep = isProvider ? known.find((s) => roleOf(s.who) === "org") : undefined;
  const kind: "system" | "provider" = hubStep ? "provider" : "system";
  const label = oneLabel(all.filter(changed).map((s) => phrase(s.after)), kind);
  const oneRole: Role = kind === "provider" ? "provider" : "software";

  /** a today node, dashed when nobody does the work or it is not done yet */
  const todayNode = (s: ProcessStep): Node => {
    const role = roleOf(s.who);
    const t = phrase(s.today);
    if (role === "nobody") {
      const clause = t.split(/;\s|,\s|\s—\s/)[0].replace(/^(nobody|no one)\s+/i, "");
      return { role, name: "Nobody does this today", say: clause ? upFirst(clause) : "", dash: true };
    }
    if (!t) return { role, name: nameOf(s.who), say: "Not done today", dash: true };
    return { role, name: nameOf(s.who), say: t };
  };
  const quietAfter = (s: ProcessStep) => (s.change === "goes" ? "No longer needed" : upFirst(phrase(s.after)) || "Unchanged");

  // the solution side: who still acts (and is wired into the one box), and
  // what the one box now does itself
  const people: Node[] = [];
  const duties: string[] = [];
  for (const s of all.filter(changed)) {
    if (hubStep && s === hubStep) continue;
    const a = afterActor(s);
    if (a.role && a.role !== oneRole && !(kind === "system" && a.role === "software") && a.role !== "nobody") {
      people.push({ role: a.role, name: a.name, say: a.what });
    } else if (a.what) duties.push(a.what);
  }

  let today: ReactNode;
  let after: ReactNode;
  if (hubStep) {
    // THE BUYER IS THE HUB: its sellers today, one provider after
    const hub: Node = { role: "org", name: nameOf(hubStep.who), say: "" };
    const others = known.filter((s) => s !== hubStep && s.today?.trim());
    const own = (say: string): Node => ({ role: "org", name: "Its own duty", say });
    const spokesToday: Node[] = [...others.map(todayNode), own(phrase(hubStep.today))];
    const fan = (spokes: ReactNode[], tealFirst: boolean, dashed: boolean[] = []) => (
      <div className="lk-hb-grid is-fan" style={{ "--k": spokes.length } as CSSProperties}>
        <span className="lk-hb-hub" style={at(1, spokes.length + 1)}><Person n={hub} /></span>
        {spokes.map((sp, i) => (
          <span key={`c${i}`} className={`lk-hb-c is-fan${pos(i, spokes.length)}${tealFirst && i === 0 ? " is-teal" : ""}${dashed[i] ? " is-dash" : ""}`} style={at(i + 1)} />
        ))}
        {spokes.map((sp, i) => <span key={`n${i}`} className="lk-hb-cell" style={at(i + 1)}>{sp}</span>)}
      </div>
    );
    const spokeBox = (n: Node, i: number) => (
      <span key={i} className={`lk-hb-spoke${n.dash ? " is-dash" : ""}`}><Person n={n} /></span>
    );
    today = fan(spokesToday.map(spokeBox), false, spokesToday.map((n) => !!n.dash));
    // after: ONE wire to one provider; the buyer's own duty, if the solution
    // leaves it alone, is a quiet line under it
    after = (
      <>
        {fan([<One key="one" kind={kind} label={label} duties={duties} />], true)}
        {!changed(hubStep) && <Pairs quiet rows={[{ node: own(quietAfter(hubStep)) }]} />}
      </>
    );
  } else {
    // EACH PERSON, THEIR OWN PLACE; then everyone into one system
    today = <Pairs rows={known.filter((s) => s.today?.trim()).map((s) => {
      const n = todayNode(s);
      return { node: n, place: n.dash ? null : placeOf(phrase(s.today)) ?? undefined };
    })} />;
    const rest = known.filter((s) => !changed(s));
    const k = people.length;
    after = (
      <>
        {k > 0 ? (
          <div className="lk-hb-grid is-tree">
            {people.map((n, i) => <span key={`p${i}`} className="lk-hb-cell is-p" style={at(i + 1)}><Person n={n} teal /></span>)}
            {people.map((n, i) => <span key={`c${i}`} className={`lk-hb-c is-tree${pos(i, k)}`} style={at(i + 1)} />)}
            <span className="lk-hb-cell is-one" style={at(1, k + 1)}><One kind={kind} label={label} duties={duties} /></span>
          </div>
        ) : <One kind={kind} label={label} duties={duties} />}
        {rest.length > 0 && (
          <Pairs quiet rows={rest.map((s) => ({ node: { ...todayNode(s), say: quietAfter(s) }, place: placeOf(phrase(s.today)) ?? undefined }))} />
        )}
      </>
    );
  }

  const questions = all.filter((s) => s.who.trim() === "?" || s.known === "unknown").map(notKnown).filter(Boolean);
  const heads = hubStep
    ? ["a different party for each part", "one provider for all of it"]
    : ["each person works separately, in their own place",
       known.some((s) => !changed(s)) ? "the steps it changes run through one system" : "everyone works in one system"];

  return (
    <figure className="lk lk-hb">
      <div className="lk-hb-pic" aria-hidden="true">
        <div className="lk-hb-block">
          <p className="lk-hb-h"><b>Today</b> · {heads[0]}</p>
          {today}
        </div>
        <div className="lk-hb-block is-after">
          <p className="lk-hb-h"><b>With the suggested solution</b> · {heads[1]}</p>
          {after}
        </div>
      </div>
      <ol className="lk-sr">
        {all.map((s, i) => (
          <li key={i}>
            {s.who.trim() === "?" ? "Who does this is not known" : s.who}.{" "}
            Today: {s.today?.trim() ? uncited(s.today) : "not done"}.{" "}
            With the suggested solution: {s.change === "goes" ? "no longer needed" : s.after ? uncited(s.after) : "same as today"}.
          </li>
        ))}
      </ol>
      {questions.length > 0 && (
        <div className="lk-hb-q">
          {questions.map((q, i) => <p key={i}>{q}</p>)}
        </div>
      )}
    </figure>
  );
}
