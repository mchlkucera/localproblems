// Minimal markdown → HTML for problem bodies. The corpus uses exactly:
// paragraphs, "- " bullet lists, "N. " numbered steps, **strong**,
// [text](url) links (absolute or site-relative), bare URLs, and
// ----separated CORRECTION paragraphs. No MDX, no plugins (SPEC.md §5).

const escapeHtml = (s: string) =>
  s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

function inline(s: string): string {
  let html = escapeHtml(s);
  // [text](url) — absolute https?:// or site-relative /… targets
  html = html.replace(/\[([^\]]+)\]\(((?:https?:\/\/|\/)[^\s)]+)\)/g, '<a href="$2">$1</a>');
  // bare URLs (not already inside an attribute — the corpus never nests them)
  html = html.replace(/(^|[\s(])((?:https?:\/\/)[^\s<)]+?)([).,;]?)(?=[\s<]|$)/g, '$1<a href="$2">$2</a>$3');
  // **strong**
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  return html;
}

/** One inline fragment, unwrapped by any block element — for derived views of
    body prose (the docket dek is the first sentence of the who-pays paragraph),
    so a citation written in the source paragraph still renders where the
    sentence is reused. */
export const renderInline = (s: string): string => inline(s);

const OL = /^\d+\.\s+/; // "N. " numbered step lines

export function renderBody(body: string): string {
  const out: string[] = [];
  let list: string[] | null = null;
  let olist: string[] | null = null;
  const flushList = () => {
    if (list) { out.push(`<ul class="prose">${list.join("")}</ul>`); list = null; }
    if (olist) { out.push(`<ol class="prose">${olist.join("")}</ol>`); olist = null; }
  };

  for (const block of body.split(/\n{2,}/)) {
    const lines = block.split("\n").map((l) => l.trim()).filter(Boolean);
    if (!lines.length) continue;
    if (lines.every((l) => l === "---")) { flushList(); continue; } // correction separator
    if (lines.every((l) => l.startsWith("- "))) {
      if (olist) flushList();
      list ??= [];
      for (const l of lines) list.push(`<li>${inline(l.slice(2))}</li>`);
      continue;
    }
    if (lines.every((l) => OL.test(l))) {
      if (list) flushList();
      olist ??= [];
      for (const l of lines) olist.push(`<li>${inline(l.replace(OL, ""))}</li>`);
      continue;
    }
    flushList();
    // a block may mix a paragraph with trailing list lines; split conservatively
    const para: string[] = [];
    for (const l of lines) {
      if (l === "---") continue;
      if (l.startsWith("- ")) { list ??= []; list.push(`<li>${inline(l.slice(2))}</li>`); }
      else if (OL.test(l)) { olist ??= []; olist.push(`<li>${inline(l.replace(OL, ""))}</li>`); }
      else para.push(l);
    }
    if (para.length) out.push(`<p>${inline(para.join(" "))}</p>`);
    flushList();
  }
  flushList();
  return out.join("\n");
}

/** Record bodies deep-link into the evidence ledgers by row:
 *  `[the OP TAK call](/sources/tenders#dotace-optak-technologie-mas-2)`.
 *  Nine such links are live in the corpus, all written in the retired
 *  `/sources/:type` spelling that next.config.ts 308s onto `/signals/:type`.
 *
 *  A FRAGMENT ONLY SCROLLS ON THE DOCUMENT THAT HOLDS THE ROW, so paging the
 *  ledgers would have quietly demoted every one of these to "lands on page 1,
 *  points at nothing" — a break no build gate can see, because the link still
 *  returns 200. This pass rewrites each href to the page the row actually sits
 *  on, resolved through `signalHref`, i.e. the same index that decided the
 *  page boundaries.
 *
 *  DELIBERATELY A RENDER-TIME RESOLUTION, NOT A DATA EDIT. Baking `/3` into a
 *  markdown file would be correct for exactly one build: the ledgers are
 *  date-descending and grow at the top, so a row's page number moves every
 *  time the pipeline appends. The corpus keeps the stable human-written URL;
 *  the build resolves it.
 *
 *  `resolve` is passed in rather than imported so this module stays a pure
 *  string transform, exactly as `annotateSourceRefs` takes its sources. The
 *  record page hands it `signalHref`, whose miss case returns the unpaged
 *  `/signals/<type>#<id>` — the old behaviour, never an invented page. */
export function repageLedgerLinks(
  html: string,
  resolve: (id: string, fallbackType: string) => string,
): string {
  return html.replace(
    /href="\/(?:signals|sources)\/([a-z]+)#([^"]+)"/g,
    (_raw, type: string, id: string) => `href="${resolve(id, type)}"`,
  );
}

/** One record source as the body's citations resolve it. Composed by the
    record page, which holds the signal lookup. */
export type SourceRef = {
  url: string;
  /** Display name — the same string the sources ledger row links. */
  label: string;
  /** ISO date as recorded on the source entry. */
  date: string;
  /** The record's own note on why this source is on file. */
  note?: string;
  /** SEAM (reserved): a verbatim snippet from the source. A parallel ingest
      program is adding `quote` to the signal schema; the day it lands, the
      page passes it through here and every ref reveal starts quoting the
      source instead of paraphrasing it. Nothing else has to change. */
  quote?: string;
};

const clip = (s: string, n = 220) => (s.length <= n ? s : `${s.slice(0, n - 1).trimEnd()}…`);

/** What a reader gets on hover / focus / long-press: which source this is.
    Plain text for a native `title` — no JS, no new visual device. */
function reveal(r: SourceRef, n: number): string {
  const head = `S${n} · ${r.label} · ${r.date}`;
  // A recorded verbatim quote outranks our own note — it is the source speaking.
  const body = r.quote ? `“${r.quote}”` : (r.note ?? "");
  return body ? `${head}\n${clip(body.replace(/\s+/g, " ").trim())}` : head;
}

function marker(r: SourceRef, n: number): string {
  const a = escapeHtml(`Source S${n} — ${r.label}`);
  return `<a class="ref" href="#s${n}" aria-label="${a}" title="${escapeHtml(reveal(r, n))}">S${n}</a>`;
}

/** Explicit citation markers written in the prose: `[S3]`, `[S3,S5]`,
    `[S3, S5]`. Uppercase S; a `]` followed by `(` is a markdown link, never a
    citation. An unresolvable number leaves the WHOLE marker as literal text —
    the defect stays visible on the page and the build lint names it. */
const MARKER = /\[S(\d+)((?:\s*,\s*S?\d+)*)\](?!\()/g;

/** Run a rewrite over text only, never inside a tag. `split` with a capture
    group keeps the delimiters, so the pass is total and order-preserving. */
const mapText = (html: string, f: (t: string) => string) =>
  html.split(/(<[^>]*>)/).map((seg) => (seg.startsWith("<") ? seg : f(seg))).join("");

/** Inline source references (owner, 2026-08-19; explicit markers 2026-08-20).
    Two triggers, one device — the small superscript S-number jumping to the
    ledger row (`id="sN"`):

    1. PRIMARY — an explicit `[Sn]` marker written in the body prose. It binds
       a claim to a source by number, so it survives rewording, needs no url in
       the sentence, and is checkable by `web/scripts/lint-citations.mjs`.
    2. Secondary — prose that links a url which is itself on the sources ledger
       gets its marker for free. Trailing slash ignored; a duplicated source url
       resolves to its first S-number. The external link stays untouched: where
       we source from outside, the record says so.

    Both markers carry the source's name and date in `title` (and its name in
    `aria-label`), so hovering, focusing or long-pressing one answers "which
    source is this?" without leaving the sentence. Post-pass over renderBody()
    output — body anchors there are exactly `<a href="…">…</a>`. */
export function annotateSourceRefs(html: string, sources: SourceRef[]): string {
  if (sources.length === 0) return html;

  // --- trigger 2: url match (renderBody escapes & to &amp;; source urls are raw)
  const norm = (u: string) => u.replace(/&amp;/g, "&").replace(/\/+$/, "");
  const byUrl = new Map<string, number>();
  sources.forEach((s, i) => {
    const k = norm(s.url);
    if (s.url.startsWith("http") && !byUrl.has(k)) byUrl.set(k, i + 1);
  });
  let out = byUrl.size
    ? html.replace(/<a href="([^"]+)">.*?<\/a>/g, (a, href: string) => {
        const n = byUrl.get(norm(href));
        return n ? `${a}${marker(sources[n - 1], n)}` : a;
      })
    : html;

  // --- trigger 1: explicit [Sn] markers
  out = mapText(out, (text) =>
    text.replace(MARKER, (raw, first: string, more: string) => {
      const nums = [first, ...more.split(",")]
        .map((x) => x.trim().replace(/^S/, ""))
        .filter(Boolean)
        .map(Number);
      if (nums.some((n) => !Number.isInteger(n) || n < 1 || n > sources.length)) return raw;
      return nums.map((n) => marker(sources[n - 1], n)).join("");
    }),
  );

  // A linked source that self-marks plus an explicit `[Sn]` for the same source
  // would print the marker twice — collapse the repeat, keep the first.
  return out.replace(
    /(<a class="ref" href="#s(\d+)"[^>]*>S\2<\/a>)(?:\s*<a class="ref" href="#s\2"[^>]*>S\2<\/a>)+/g,
    "$1",
  );
}
