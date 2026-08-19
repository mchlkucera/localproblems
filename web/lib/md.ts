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
