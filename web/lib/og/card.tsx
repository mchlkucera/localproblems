// THE SHARE CARDS: the 1200×630 PNGs a link preview shows, drawn by next/og
// (Satori: flexbox and a subset of CSS; every box with children is a flex box).
// Both are rendered at BUILD time by the opengraph-image files, never per
// request: they read `data/` like every page does.
//
// DESIGN (skills/design-language): the site's modern look at thumbnail scale.
// White ground, Inter only, hierarchy from size, weight and gray shade. The only
// hues are the ones that already mean something: the score scale on the score
// dots and the entry level's dot, each with its word beside it. No citation
// pills, no badges, no chrome. It must still read at 400px wide, so the type is
// large and there are few things on it.
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { isValidElement, type ReactNode } from "react";
import { CategoryArt } from "../art/category-art";
import { ENTRY_LEVEL_LABELS } from "../format";
import type { EntryLevel } from "../data";

export const CARD = { width: 1200, height: 630 } as const;

// ---- fonts --------------------------------------------------------------------
// INTER, THE SITE'S OWN FILES. next/font self-hosts Inter 4.001 (Google Fonts'
// variable build) as woff2, which Satori can't read. lib/og/fonts holds static
// TTF instances cut from those same files: the latin and latin-ext subsets,
// instanced at wght 400 and 600 and merged, with fontTools:
//   instantiateVariableFont(TTFont(woff2), {"wght": w}) → fontTools.merge.Merger
// No request to Google at build time. OFL-1.1, see fonts/OFL.txt.
let fonts: { name: string; data: Buffer; weight: 400 | 600; style: "normal" }[] | undefined;
export function cardFonts() {
  fonts ??= ([400, 600] as const).map((weight) => ({
    name: "Inter",
    data: readFileSync(join(process.cwd(), "lib/og/fonts", `Inter-${weight}.ttf`)),
    weight,
    style: "normal" as const,
  }));
  return fonts;
}

// ---- the palette: tokens.css and problem.css, never new values ---------------
const C = {
  bg: "#ffffff",
  text1: "#1b1c1f",
  text2: "#5f6168",
  text3: "#6e7077", // the AA-passing meta gray (.lab.ls, .lab.lf)
  ring: "#8a8c93", // the Venn rings (--lf-ring)
  art: "#9fa1a8", // the category drawing (.ls-art)
  empty: "#e3e4e8", // an unearned meter segment (--l-bg-4)
  score: { good: "#3f8f7f", mid: "#b58a2e", bad: "#c4564f" },
  level: {
    easy: ["#4f9c8c", "#2e7466"],
    moderate: ["#b58a2e", "#8a6414"],
    hard: ["#d0763f", "#a3542a"],
    "very-hard": ["#c4564f", "#a8413c"],
  } satisfies Record<EntryLevel, [string, string]>,
} as const;

const PAD_X = 72;

// ---- the category drawing, as an image -----------------------------------------
// CategoryArt is inline SVG built from fragments, which Satori's own SVG path
// doesn't walk. Serialise it to a string (currentColor → the page's gray) and
// hand it over as a data URI.
const kebab = (k: string) => (k === "viewBox" ? k : k.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`));
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
function svgString(node: ReactNode): string {
  if (node == null || typeof node === "boolean") return "";
  if (Array.isArray(node)) return node.map(svgString).join("");
  if (typeof node === "string" || typeof node === "number") return esc(String(node));
  if (!isValidElement(node)) return "";
  const { children, className: _c, ...attrs } = node.props as Record<string, unknown>;
  if (typeof node.type !== "string") return svgString(children as ReactNode); // a fragment
  const a = Object.entries(attrs)
    .filter(([, v]) => v != null && v !== false)
    .map(([k, v]) => ` ${kebab(k)}="${esc(String(v))}"`)
    .join("");
  return `<${node.type}${a}>${svgString(children as ReactNode)}</${node.type}>`;
}
function artUri(category: string, width: number, height: number) {
  const svg = svgString(CategoryArt({ category }))
    .replace("<svg ", `<svg xmlns="http://www.w3.org/2000/svg" `)
    .replace(/ width="\d+" height="\d+"/, ` width="${width}" height="${height}"`)
    .replaceAll("currentColor", C.art);
  return `data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}`;
}

// ---- pieces ---------------------------------------------------------------------

function Footer() {
  return (
    <div style={{ display: "flex", fontSize: 24, lineHeight: 1, color: C.text3 }}>
      <span style={{ color: C.text1, fontWeight: 600 }}>localproblems.org</span>
      <span style={{ margin: "0 12px" }}>·</span>
      <span>Czechia</span>
    </div>
  );
}

const Dot = ({ color, size }: { color: string; size: number }) => (
  <div style={{ width: size, height: size, borderRadius: size, background: color, flexShrink: 0 }} />
);

/** A label on its own line over its value, as the page's facts and labels. */
function Stat({ label, children }: { label: string; children: ReactNode }) {
  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <div style={{ fontSize: 22, lineHeight: 1, color: C.text3, marginBottom: 14 }}>{label}</div>
      <div style={{ display: "flex", alignItems: "center", height: 48 }}>{children}</div>
    </div>
  );
}

/** Long titles step down so every record fits in four lines at most; `balance`
    keeps the lines even, so none ends on a lone word. No line clamp on the
    title: Satori's `balance` narrows a clamped block until it truncates. */
function titleSize(t: string) {
  const n = t.length;
  return n <= 48 ? 72 : n <= 76 ? 64 : n <= 100 ? 58 : 52;
}

/** The line under the title, cut at a word to about `lines` lines at 28px, so
    the clamp never has to cut a word in half, and never left on "the…". Its
    last two words are joined by a no-break space, so it never ends on a lone
    word (a clamped block can't take `balance`: see titleSize). */
const WEAK_END = /\s+(?:a|an|the|of|to|in|on|at|by|for|with|from|and|or|but|that|than|its|their|is|are|was|were)$/i;
function cardLine(text: string, lines: number) {
  const max = lines * 56;
  const t = text.trim();
  let out = t;
  if (t.length > max) {
    let cut = t.slice(0, max + 1).replace(/\s+\S*$/, "");
    while (WEAK_END.test(cut)) cut = cut.replace(WEAK_END, "");
    out = `${cut.replace(/[\s,;:–—-]+$/, "")}…`;
  }
  return out.replace(/\s+(\S+)$/, "\u00a0$1");
}

// ---- the record card ---------------------------------------------------------------

export type RecordCardData = {
  title: string;
  /** the brief as plain text (cut here to fit), else the category name */
  line: string;
  category: string;
  /** the five summed sections, in page order */
  scores: { n: number; max: number }[];
  total: { n: number; max: number };
  level: EntryLevel;
};

export function RecordCard({ title, line, category, scores, total, level }: RecordCardData) {
  const size = titleSize(title);
  // a short title (two lines) leaves room for a third line of brief
  const lines = size >= 72 ? 3 : 2;
  const [lvl, lvlInk] = C.level[level];
  const art = { w: 252, h: 168 };
  return (
    <div
      style={{
        width: "100%", height: "100%", display: "flex", flexDirection: "column",
        background: C.bg, padding: `64px ${PAD_X}px 56px`, fontFamily: "Inter", position: "relative",
      }}
    >
      <div
        style={{
          fontSize: size, lineHeight: 1.1, fontWeight: 600, letterSpacing: "-0.028em",
          color: C.text1, textWrap: "balance", maxWidth: CARD.width - 2 * PAD_X,
        }}
      >
        {title}
      </div>
      <div
        style={{
          marginTop: 24, fontSize: 28, lineHeight: 1.4, color: C.text2, maxWidth: 840,
          display: "block", lineClamp: lines,
        }}
      >
        {cardLine(line, lines)}
      </div>
      <div style={{ flexGrow: 1 }} />
      <div style={{ display: "flex", gap: 72 }}>
        <Stat label="Opportunity">
          <span style={{ fontSize: 48, lineHeight: 1, fontWeight: 600, color: C.text1, letterSpacing: "-0.02em" }}>{total.n}</span>
          <span style={{ fontSize: 48, lineHeight: 1, fontWeight: 400, color: C.text3, letterSpacing: "-0.02em" }}>/{total.max}</span>
          {/* the front page's meter at card scale: one segment per point, teal
              up to the score, gray after it (owner: "the last dot should be grey") */}
          <div style={{ display: "flex", gap: 6, marginLeft: 24 }}>
            {Array.from({ length: total.max }, (_, i) => (
              <div key={i} style={{ width: 12, height: 28, borderRadius: 3, background: i < total.n ? C.score.good : C.empty }} />
            ))}
          </div>
        </Stat>
        <Stat label="Entry">
          <Dot color={lvl} size={18} />
          <span style={{ marginLeft: 14, fontSize: 40, lineHeight: 1, fontWeight: 600, color: lvlInk, letterSpacing: "-0.015em" }}>
            {ENTRY_LEVEL_LABELS[level]}
          </span>
        </Stat>
      </div>
      <div style={{ marginTop: 40, display: "flex" }}>
        <Footer />
      </div>
      <img
        src={artUri(category, art.w, art.h)}
        width={art.w}
        height={art.h}
        alt=""
        style={{ position: "absolute", right: PAD_X - 16, bottom: 44 }}
      />
    </div>
  );
}

// ---- the site card ---------------------------------------------------------------------

/** The front page's header at card scale: the title and its one sentence, beside
    the Venn (lib/site/front.tsx): three monoline rings, the shared core faintly
    filled, the labels in the page's words. */
export function SiteCard({ title, line }: { title: string; line: string }) {
  const label = { position: "absolute", fontSize: 22, lineHeight: 1.1, fontWeight: 400, color: C.text2 } as const;
  return (
    <div
      style={{
        width: "100%", height: "100%", display: "flex", flexDirection: "column",
        background: C.bg, padding: `64px ${PAD_X}px 56px`, fontFamily: "Inter",
      }}
    >
      <div style={{ display: "flex", flexGrow: 1, alignItems: "center", justifyContent: "space-between" }}>
        <div style={{ display: "flex", flexDirection: "column", width: 540, flexShrink: 0 }}>
          <div style={{ fontSize: 70, lineHeight: 1.06, fontWeight: 600, letterSpacing: "-0.03em", color: C.text1, textWrap: "balance" }}>
            {title}
          </div>
          <div style={{ marginTop: 28, fontSize: 28, lineHeight: 1.4, color: C.text2, textWrap: "pretty" }}>{line}</div>
        </div>
        {/* THE VENN, redrawn for the card (owner, 2026-09-19: "messy"): three
            equal rings on an equilateral triangle, each label centred in the
            widest part of its own ring's outer lobe, the overlaps shaded by stacking the same faint
            fill, and one teal dot where all three meet: the register's aim */}
        <div style={{ display: "flex", position: "relative", width: 450, height: 430, flexShrink: 0 }}>
          <svg width="450" height="430" viewBox="0 0 450 430" fill="none">
            <circle cx="150" cy="150" r="120" fill={C.text1} fillOpacity="0.035" stroke={C.ring} strokeWidth="2" />
            <circle cx="300" cy="150" r="120" fill={C.text1} fillOpacity="0.035" stroke={C.ring} strokeWidth="2" />
            <circle cx="225" cy="280" r="120" fill={C.text1} fillOpacity="0.035" stroke={C.ring} strokeWidth="2" />
            <circle cx="225" cy="193" r="11" fill={C.score.good} />
          </svg>
          <div style={{ ...label, left: 105 - 80, width: 160, top: 124, display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center" }}>
            <span>People</span><span style={{ marginTop: 4 }}>want</span>
          </div>
          <div style={{ ...label, left: 345 - 80, width: 160, top: 124, display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center" }}>
            <span>Government</span><span style={{ marginTop: 4 }}>wants</span>
          </div>
          <div style={{ ...label, left: 225 - 80, width: 160, top: 318, display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center" }}>
            <span>Works</span><span style={{ marginTop: 4 }}>abroad</span>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}
