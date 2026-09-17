// Record prose → React, with citations as components.
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
import { splitLead } from "../sections";
import { EXT, ExtArrow, citeParts, type CiteCtx } from "./cite";

type Tok =
  | { k: "text"; v: string }
  | { k: "strong"; kids: Tok[] }
  | { k: "link"; text: string; href: string; auto?: number }
  | { k: "cite"; nums: number[] };

// A link target is absolute (https?://), site-relative (/…) or an in-page
// `#anchor` (record-page redesign, 2026-09-16). An anchor link gets no EXT and
// no ↗: it stays on the page.
const INLINE =
  /\*\*([^*]+)\*\*|\[([^\]]+)\]\(((?:https?:\/\/|\/)[^\s)]+|#[a-z0-9-]+)\)|\[S(\d+)((?:\s*,\s*S?\d+)*)\](?!\()|(https?:\/\/[^\s<)]*[^\s<).,;:])/g;

const norm = (u: string) => u.replace(/\/+$/, "");

export type ProseOpts = {
  /** Resolve `/sources/<type>#<id>` ledger links to their paged ledger row. */
  resolveLedger: (id: string, type: string) => string;
  /** Keyed lists: return true for a key that should carry the `ls-soon` mark
      (e.g. a Why now date that is still ahead). Called once per key. */
  keyedSoon?: (key: string) => boolean;
};

/** A keyed bullet: `- **About €33M:** what the line says`. A bullet block
    renders as a keyed list only when EVERY line matches. */
const KEYED = /^- \*\*([^*]{1,40}?):\*\*\s+(.+)$/;

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
        <a key={k} className="ls-link" href={href} {...(ext ? EXT : {})}>
          {t.text}
          {ext && <ExtArrow />}
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
    each numbered step's are set as run-in leads (the production v1.19 rule);
    a first paragraph that is exactly ONE sentence is instead the section's
    answer line, `<p class="ls-answer">`. A bullet block whose every line is
    `- **Key:** value` renders as `<dl class="ls-keyed">` (rows `ls-keyed-row`,
    `dt.ls-keyed-k` [+ `ls-soon` via `opts.keyedSoon`], `dd.ls-keyed-v`). */
export function Prose(md: string, ctx: CiteCtx, opts: ProseOpts & { lead?: boolean }): ReactNode {
  const out: ReactNode[] = [];
  // bullets are held as raw lines + keys until flush, which decides between a
  // keyed list (every line keyed) and a plain one
  let ul: { l: string; k: string }[] | null = null;
  let ol: ReactNode[] | null = null;
  let led = !opts.lead;
  let b = 0;
  const flushUl = (items: { l: string; k: string }[]) => {
    const keyed = items.map(({ l }) => l.match(KEYED));
    if (keyed.every(Boolean)) {
      out.push(
        <dl key={`d${b++}`} className="ls-keyed">
          {items.map(({ k }, i) => {
            const m = keyed[i] as RegExpMatchArray;
            const soon = opts.keyedSoon?.(m[1]) ?? false;
            return (
              <div key={k} className="ls-keyed-row">
                <dt className={soon ? "ls-keyed-k ls-soon" : "ls-keyed-k"}>{m[1]}</dt>
                <dd className="ls-keyed-v">{inline(m[2], ctx, opts, k)}</dd>
              </div>
            );
          })}
        </dl>,
      );
    } else {
      out.push(
        <ul key={`u${b++}`} className="ls-ul">
          {items.map(({ l, k }) => <li key={k}>{inline(l.slice(2), ctx, opts, k)}</li>)}
        </ul>,
      );
    }
  };
  const flush = () => {
    if (ul) flushUl(ul);
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
    const bullet = (l: string, k: string) => ({ l, k });
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
      if (!led && splitLead(text).rest === "") {
        // the answer line: a first paragraph that is exactly one sentence
        out.push(<p key={k} className="ls-answer">{inline(text, ctx, opts, k)}</p>);
      } else {
        out.push(<p key={k} className="ls-p">{led ? inline(text, ctx, opts, k) : withLead(text, ctx, opts, k)}</p>);
      }
      led = true;
    }
    flush();
  });
  flush();
  return <>{out}</>;
}
