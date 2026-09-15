// /lab/problem — record prose → React, with citations as components.
//
// The corpus grammar is the one web/lib/md.ts documents: paragraphs, "- "
// bullets, "N. " steps, **strong**, [text](url) links, bare URLs, and explicit
// `[S3]` / `[S3,S5]` markers. The production page turns markers into HTML
// strings; here each marker becomes a real <button> + popover pair, so this is
// a small tokenizer rather than a string post-pass.
//
// TYPOGRAPHY RULE: a pill never starts a line on its own. The word before it
// and any punctuation after it ("services [S1]." → `services⎵[pill].`) are
// wrapped with it in one no-break span.
import type { ReactNode } from "react";
import { splitLead } from "../../../lib/sections";
import { citeParts, type CiteCtx } from "./cite";

type Tok =
  | { k: "text"; v: string }
  | { k: "strong"; kids: Tok[] }
  | { k: "link"; text: string; href: string; auto?: number }
  | { k: "cite"; nums: number[] };

const INLINE =
  /\*\*([^*]+)\*\*|\[([^\]]+)\]\(((?:https?:\/\/|\/)[^\s)]+)\)|\[S(\d+)((?:\s*,\s*S?\d+)*)\](?!\()|(https?:\/\/[^\s<)]*[^\s<).,;:])/g;

const norm = (u: string) => u.replace(/\/+$/, "");

export type ProseOpts = {
  /** Resolve `/sources/<type>#<id>` ledger links to their paged ledger row. */
  resolveLedger: (id: string, type: string) => string;
};

function tokenize(s: string, ctx: CiteCtx): Tok[] {
  const byUrl = new Map<string, number>();
  ctx.sources.forEach((src) => {
    if (src.url && !byUrl.has(norm(src.url))) byUrl.set(norm(src.url), src.n);
  });
  const out: Tok[] = [];
  let last = 0;
  for (const m of s.matchAll(INLINE)) {
    const at = m.index ?? 0;
    if (at > last) out.push({ k: "text", v: s.slice(last, at) });
    if (m[1] !== undefined) {
      out.push({ k: "strong", kids: tokenize(m[1], ctx) });
    } else if (m[2] !== undefined) {
      out.push({ k: "link", text: m[2], href: m[3], auto: byUrl.get(norm(m[3])) });
    } else if (m[4] !== undefined) {
      const nums = [m[4], ...(m[5] ?? "").split(",")]
        .map((x) => x.trim().replace(/^S/, ""))
        .filter(Boolean)
        .map(Number);
      const ok = nums.every((n) => Number.isInteger(n) && n >= 1 && n <= ctx.sources.length);
      // an unresolvable marker stays literal — the defect stays visible
      out.push(ok ? { k: "cite", nums: [...new Set(nums)] } : { k: "text", v: m[0] });
    } else if (m[6] !== undefined) {
      out.push({ k: "link", text: m[6], href: m[6], auto: byUrl.get(norm(m[6])) });
    }
    last = at + m[0].length;
  }
  if (last < s.length) out.push({ k: "text", v: s.slice(last) });

  // A link whose url is itself on the ledger cites that source for free —
  // unless the author already wrote the marker right after it.
  const res: Tok[] = [];
  out.forEach((t, i) => {
    res.push(t);
    if (t.k !== "link" || !t.auto) return;
    let j = i + 1;
    while (j < out.length && out[j].k === "text" && !(out[j] as { v: string }).v.trim()) j++;
    const next = out[j];
    if (next && next.k === "cite" && next.nums.includes(t.auto)) return;
    res.push({ k: "cite", nums: [t.auto] });
  });
  return res;
}

function renderToks(toks: Tok[], ctx: CiteCtx, opts: ProseOpts, key: string): ReactNode[] {
  const nodes: ReactNode[] = [];
  const ts = toks.map((t) => ({ ...t })) as Tok[];
  ts.forEach((t, i) => {
    const k = `${key}.${i}`;
    if (t.k === "text") {
      if (t.v) nodes.push(t.v);
    } else if (t.k === "strong") {
      nodes.push(<strong key={k}>{renderToks(t.kids, ctx, opts, k)}</strong>);
    } else if (t.k === "link") {
      const ledger = t.href.match(/^\/(?:signals|sources)\/([a-z]+)#(.+)$/);
      const href = ledger ? opts.resolveLedger(ledger[2], ledger[1]) : t.href;
      const ext = href.startsWith("http");
      nodes.push(
        <a key={k} className="ls-link" href={href} {...(ext ? { target: "_blank", rel: "noopener noreferrer" } : {})}>
          {t.text}
        </a>,
      );
    } else {
      // glue: the trailing word of the text before, and punctuation after
      let word = "";
      const prev = nodes[nodes.length - 1];
      if (typeof prev === "string") {
        const m = prev.match(/(\S+)\s*$/);
        if (m) {
          word = m[1];
          nodes[nodes.length - 1] = prev.slice(0, m.index);
        } else {
          nodes[nodes.length - 1] = prev.replace(/\s+$/, "");
        }
      }
      let punct = "";
      const next = ts[i + 1];
      if (next && next.k === "text") {
        const m = next.v.match(/^[.,;:!?)\]]+/);
        if (m) {
          punct = m[0];
          next.v = next.v.slice(punct.length);
        }
      }
      const { pill, peek } = citeParts(t.nums, ctx);
      // A sentence-final stop moves BEFORE the pill ("services. [pill]"), the
      // way ChatGPT and Perplexity attach a citation to the sentence it backs;
      // a comma, semicolon or colon stays after it, inside the clause.
      const stop = /^[.!?]+$/.test(punct);
      nodes.push(
        <span key={k} className="ls-nb">
          {word}
          {stop && punct}
          {pill}
          {!stop && punct}
        </span>,
        <span key={`${k}p`} className="ls-peek-slot">{peek}</span>,
      );
    }
  });
  return nodes;
}

export function inline(s: string, ctx: CiteCtx, opts: ProseOpts, key = "i"): ReactNode[] {
  return renderToks(tokenize(s, ctx), ctx, opts, key);
}

/** A unit with its first sentence set as the run-in lead — the scan line. */
function withLead(s: string, ctx: CiteCtx, opts: ProseOpts, key: string): ReactNode[] {
  const { lead, rest } = splitLead(s);
  // a "lead" longer than ~3 lines is not a scan line, it is a heavy paragraph
  const leadLen = lead.replace(/\s*\[S[\d,\sS]+\]/g, "").length;
  if (!rest || leadLen > 240) return inline(s, ctx, opts, key);
  return [
    <span key={`${key}L`} className="ls-lead">{inline(lead, ctx, opts, `${key}l`)}</span>,
    " ",
    ...inline(rest, ctx, opts, `${key}r`),
  ];
}

const OL = /^\d+\.\s+/;

/** Body markdown → blocks. `lead`: the first paragraph's opening sentence and
    each numbered step's are set as run-in leads (the production v1.19 rule). */
export function Prose(md: string, ctx: CiteCtx, opts: ProseOpts & { lead?: boolean }): ReactNode {
  const out: ReactNode[] = [];
  let ul: ReactNode[] | null = null;
  let ol: ReactNode[] | null = null;
  let led = !opts.lead;
  let b = 0;
  const flush = () => {
    if (ul) out.push(<ul key={`u${b++}`} className="ls-ul">{ul}</ul>);
    if (ol) out.push(<ol key={`o${b++}`} className="ls-steps">{ol}</ol>);
    ul = ol = null;
  };
  const step = (l: string, k: string) => {
    const text = l.replace(OL, "");
    return (
      <li key={k}>
        <span className="ls-step-body">{opts.lead ? withLead(text, ctx, opts, k) : inline(text, ctx, opts, k)}</span>
      </li>
    );
  };

  md.split(/\n{2,}/).forEach((block, bi) => {
    const lines = block.split("\n").map((l) => l.trim()).filter(Boolean);
    if (!lines.length || lines.every((l) => l === "---")) return flush();
    const bullet = (l: string, k: string) => <li key={k}>{inline(l.slice(2), ctx, opts, k)}</li>;
    // a block of only bullets / only steps continues the open list
    if (lines.every((l) => l.startsWith("- "))) {
      if (ol) flush();
      lines.forEach((l, li) => (ul ??= []).push(bullet(l, `${bi}.${li}`)));
      return;
    }
    if (lines.every((l) => OL.test(l))) {
      if (ul) flush();
      lines.forEach((l, li) => (ol ??= []).push(step(l, `${bi}.${li}`)));
      return;
    }
    // a paragraph with trailing list lines: paragraph first, then its list
    flush();
    const para: string[] = [];
    lines.forEach((l, li) => {
      const k = `${bi}.${li}`;
      if (l === "---") return;
      if (l.startsWith("- ")) (ul ??= []).push(bullet(l, k));
      else if (OL.test(l)) (ol ??= []).push(step(l, k));
      else para.push(l);
    });
    if (para.length) {
      const text = para.join(" ");
      const k = `p${bi}`;
      out.push(<p key={k} className="ls-p">{led ? inline(text, ctx, opts, k) : withLead(text, ctx, opts, k)}</p>);
      led = true;
    }
    flush();
  });
  flush();
  return <>{out}</>;
}
