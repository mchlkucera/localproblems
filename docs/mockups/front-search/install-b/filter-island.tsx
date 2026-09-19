"use client";
// THE FRONT PAGE'S SEARCH ISLAND (owner, 2026-09-18: "B, plus C's `/`
// shortcut"). Makes ./front-filter.tsx's bar live on / and /by-category.
//
// PROGRESSIVE ONLY. It renders nothing and never adds a word to the page: it
// sets `hidden` on rows that are already in the HTML and rewrites the counts it
// is allowed to rewrite (the count line, each group's "N problems"). Without it
// the page is the whole register with true counts, and the controls that need
// it are hidden by `@media (scripting: enabled)`. What it adds:
//   · the box filters rows as you type: every word must appear in the title,
//     story, suggested solution or category (accents ignored: "hlidac" finds
//     "Hlídač"). Escape clears it; Escape again leaves it.
//   · chips toggle filters: any of the picked categories, any of the picked
//     bands, and each "Also" flag narrows further. A category chip is a link
//     without the island; with it, a click filters in place.
//   · `/` anywhere outside a text field focuses the box (option C's shortcut).
//   · /by-category: a fold with no match hides, a fold with one opens; clearing
//     puts every fold back as the reader left it.
// It first touches the DOM in an effect, after hydration, so the server HTML
// and the hydrated tree never disagree (the mockup's first cut set aria state
// on load and hit exactly that mismatch). One set of listeners, no state
// outside the DOM, no dependency.
import { useEffect } from "react";

type Facet = { c: string; n: string; b: string; d: 0 | 1; l: 0 | 1 };

const fold = (s: string) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
const problems = (n: number) => `${n} ${n === 1 ? "problem" : "problems"}`;

export function FilterIsland() {
  useEffect(() => {
    const bar = document.querySelector<HTMLElement>("[data-find]");
    const box = bar?.querySelector<HTMLInputElement>("[data-q]");
    const idxEl = document.getElementById("lf-find-idx");
    if (!bar || !box || !idxEl) return;
    const idx = JSON.parse(idxEl.textContent || "{}") as Record<string, Facet>;
    const $ = (s: string) => bar.querySelector<HTMLElement>(s);
    const count = $("[data-count]"), none = $("[data-none]"), clear = $("[data-clear]"), live = $("[data-live]");
    const chips = [...bar.querySelectorAll<HTMLElement>("[data-k]")];

    const rows = [...document.querySelectorAll<HTMLElement>(".lf-entry")].flatMap((li) => {
      const f = idx[li.querySelector(".lf-title a")?.getAttribute("href") ?? ""];
      if (!f) return [];
      const words = [...li.querySelectorAll(".lf-title, .lf-story, .lf-item-v")].map((e) => e.textContent);
      return [{ li, f, t: fold(`${words.join(" ")} ${f.n} ${f.c}`) }];
    });
    const groups = [...document.querySelectorAll<HTMLElement>(".lf-sec, .lf-fold")].map((g) => {
      const n = g.querySelector<HTMLElement>(".lf-sec-h p, .lf-fold-meta");
      return { g, n, text: n?.textContent ?? "", all: g.querySelectorAll(".lf-entry").length, was: false };
    });
    const on: Record<string, Set<string>> = { cat: new Set(), band: new Set(), flag: new Set() };
    let wasLive = false;

    const apply = () => {
      const q = fold(box.value).split(/\s+/).filter(Boolean);
      const picked = on.cat.size + on.band.size + on.flag.size;
      const isLive = picked > 0 || q.length > 0;
      let n = 0;
      for (const { li, f, t } of rows) {
        const ok = (!on.cat.size || on.cat.has(f.c)) && (!on.band.size || on.band.has(f.b))
          && (!on.flag.has("d") || !!f.d) && (!on.flag.has("l") || !!f.l) && q.every((w) => t.includes(w));
        li.hidden = !ok;
        if (ok) n++;
      }
      for (const G of groups) {
        const vis = G.g.querySelectorAll(".lf-entry:not([hidden])").length;
        G.g.hidden = !vis;
        if (G.n) G.n.textContent = isLive ? `${vis} of ${problems(G.all)}` : G.text;
        if (G.g instanceof HTMLDetailsElement) {
          if (isLive && !wasLive) G.was = G.g.open;
          if (isLive) G.g.open = vis > 0;
          else if (wasLive) G.g.open = G.was;
        }
      }
      wasLive = isLive;
      if (count) count.textContent = isLive ? `${n} of ${problems(rows.length)}` : problems(rows.length);
      if (none) none.hidden = n > 0;
      if (clear) clear.hidden = !isLive;
      if (live) { live.hidden = !picked; live.textContent = String(picked); }
    };

    const reset = () => {
      for (const s of Object.values(on)) s.clear();
      for (const c of chips) c.setAttribute(c.tagName === "A" ? "aria-current" : "aria-pressed", "false");
      box.value = "";
    };
    const onClick = (e: MouseEvent) => {
      const t = e.target as Element;
      const c = t.closest<HTMLElement>("[data-k]");
      if (c) {
        e.preventDefault();
        const s = on[c.dataset.k ?? ""], v = c.dataset.v ?? "";
        if (!s) return;
        if (!s.delete(v)) s.add(v);
        c.setAttribute(c.tagName === "A" ? "aria-current" : "aria-pressed", String(s.has(v)));
      } else if (t.closest("[data-clear]")) {
        reset();
        box.focus();
      } else return;
      apply();
    };
    const onBoxKey = (e: KeyboardEvent) => {
      if (e.key !== "Escape") return;
      e.preventDefault();
      if (box.value) { box.value = ""; apply(); } else box.blur();
    };
    const onKey = (e: KeyboardEvent) => {
      if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey || e.defaultPrevented) return;
      const a = document.activeElement as HTMLElement | null;
      if (a && (a.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName))) return;
      e.preventDefault();
      box.focus();
      box.select();
    };

    bar.addEventListener("click", onClick);
    box.addEventListener("input", apply);
    box.addEventListener("keydown", onBoxKey);
    document.addEventListener("keydown", onKey);
    if (box.value) apply(); // a value the browser restored on back/forward
    return () => {
      bar.removeEventListener("click", onClick);
      box.removeEventListener("input", apply);
      box.removeEventListener("keydown", onBoxKey);
      document.removeEventListener("keydown", onKey);
    };
  }, []);
  return null;
}
