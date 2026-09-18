// lib/figures — small role and object glyphs, drawn for this site, and the
// keyword tables that pick them from a record's own words.
//
// HOUSE STYLE (skills/design-language §10 rule 9): the same hand as the
// category icons in lib/site/front.tsx — a 16-unit grid, solid `currentColor`
// fill, even-odd, 0.75 corner radii, and the telling detail cut out as negative
// space of at least 1px. No stroke, no stock set, no emoji.
//
// A ROLE IS ONE BUST PLUS ONE DETAIL: a hole in the chest (the cross, the
// barcode), a band round the head (the headset), or a small badge cut free of
// the bust by a ground-coloured stroke (the record card, the truck, the screen,
// the speech bubble, the tag). Organisations are buildings, not people.
//
// TO ADD A ROLE: draw its one detail on the 16-unit grid, add it to ROLE_GLYPH,
// and add one row to ROLE_TABLE. Anything the table does not match draws the
// plain bust, so a new `who` never breaks the figure; it only looks generic.
// The same goes for objects: OBJ_GLYPH plus a row in PLACE_TABLE.
import type { ReactNode } from "react";

export type Role =
  | "person" | "doctor" | "coder" | "documentarian" | "dispatcher" | "driver" | "office"
  | "consultant" | "seller" | "org" | "provider" | "software" | "nobody";
export type Obj = "document" | "phone" | "email" | "software" | "registry" | "invoice" | "form" | "spreadsheet";

/** who → role. First match wins; anything else is a person. */
const ROLE_TABLE: readonly [RegExp, Role][] = [
  [/^(nobody|no one)\b/i, "nobody"],
  [/\b(doctor|physician|radiologist|nurse)\b/i, "doctor"],
  [/\bcoder\b/i, "coder"],
  [/\b(documentarian|registrar)\b/i, "documentarian"],
  [/\bdispatcher\b/i, "dispatcher"],
  [/\bdriver\b/i, "driver"],
  [/\b(consultant|adviser|advisor|lawyer)\b/i, "consultant"],
  [/\b(seller|supplier|vendor)\b/i, "seller"],
  [/\bprovider\b/i, "provider"],
  [/\b(software|system|app|platform)\b/i, "software"],
  [/\b(town|municipality|care home|hospital|school|organisation|ministry|agency)\b/i, "org"],
  [/\b(office|clerk|accountant|bookkeeper)\b/i, "office"],
];
export const roleOf = (who: string): Role => ROLE_TABLE.find(([re]) => re.test(who.trim()))?.[1] ?? "person";

/** Where a step happens, in the step's OWN words: the matched text is the
    label, so the figure never names a product the record does not. */
const PLACE_TABLE: readonly [RegExp, Obj][] = [
  [/\bfree text\b/i, "document"],
  [/\b(?:the )?(?:cancer )?registry\b/i, "registry"],
  [/\bthe report\b/i, "document"],
  [/\bphones?\b/i, "phone"],
  [/\be-?mail\b/i, "email"],
  [/\b(?:old )?(?:dispatch )?software\b/i, "software"],
  [/\bspreadsheets?\b|\bexcel\b/i, "spreadsheet"],
  [/\b(?:EU )?grant application\b/i, "form"],
  [/\b(?:the )?required documents\b/i, "document"],
];
export function placeOf(text: string): { objs: Obj[]; words: string } | null {
  const hits: { obj: Obj; w: string; at: number }[] = [];
  for (const [re, obj] of PLACE_TABLE) {
    const m = re.exec(text);
    if (m && !hits.some((h) => h.w.toLowerCase() === m[0].toLowerCase())) {
      hits.push({ obj, w: m[0].replace(/^the /i, ""), at: m.index });
    }
  }
  if (!hits.length) return null;
  hits.sort((a, b) => a.at - b.at);
  return { objs: hits.map((h) => h.obj), words: hits.map((h) => h.w).join(" · ") };
}

// ---- the glyphs --------------------------------------------------------------

type Part = { d: string; badge?: boolean; tf?: string };
const HEAD = "M8 2a2.6 2.6 0 1 1 0 5.2A2.6 2.6 0 1 1 8 2Z";
const BODY = "M2.75 14.25V13.1A4.35 4.35 0 0 1 7.1 8.75h1.8a4.35 4.35 0 0 1 4.35 4.35v1.15a.75.75 0 0 1-.75.75H3.5a.75.75 0 0 1-.75-.75Z";
const bust = (hole = "", dx = 0): Part[] => {
  const tf = dx ? `translate(${dx} 0)` : undefined;
  return [{ d: HEAD, tf }, { d: BODY + hole, tf }];
};
// the category glyphs' civic building and truck, reused so the sets agree
const CIVIC = "M8 1.1L14.75 5.1H1.25Z M2.5 6.4h2.25v5.35H2.5Z M6.875 6.4h2.25v5.35h-2.25Z M11.25 6.4h2.25v5.35H11.25Z M1.25 12.75h13.5v2H1.25Z";
const TRUCK = "M1.75 3h7.5a.75.75 0 0 1 .75.75V10H1V3.75A.75.75 0 0 1 1.75 3Z M10.75 5.5h2.2a.75.75 0 0 1 .6.3l1.3 1.75a.75.75 0 0 1 .15.45V10h-4.25Z M4.25 10.95a1.65 1.65 0 1 1 0 3.3a1.65 1.65 0 1 1 0-3.3Z M11.75 10.95a1.65 1.65 0 1 1 0 3.3a1.65 1.65 0 1 1 0-3.3Z";
// a window with two lines of content: software, and the ONE system
const WINDOW = "M2.25 2h11.5a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75H2.25a.75.75 0 0 1-.75-.75V2.75A.75.75 0 0 1 2.25 2Z M2.75 5.25v7.5h10.5v-7.5Z M4.25 6.75h7.5v1.25h-7.5Z M4.25 9.25h5v1.25h-5Z";
// an office block, its windows cut out: a firm, the ONE provider
const FIRM = "M2.75 1.75h7a.75.75 0 0 1 .75.75v3.25h2.75a.75.75 0 0 1 .75.75v7.5a.75.75 0 0 1-.75.75H2.75a.75.75 0 0 1-.75-.75V2.5a.75.75 0 0 1 .75-.75Z M4 3.75h1.5v1.5H4Z M7 3.75h1.5v1.5H7Z M4 6.75h1.5v1.5H4Z M7 6.75h1.5v1.5H7Z M4 9.75h1.5v1.5H4Z M7 9.75h1.5v1.5H7Z M11.25 8h1.25v1.5h-1.25Z M11.25 10.75h1.25v1.5h-1.25Z M6.5 12.5v2h-1v-2Z";

const ROLE_GLYPH: Record<Role, Part[]> = {
  person: bust(),
  // the medical cross, cut out of the chest
  doctor: bust(" M7.35 10.1h1.3v1.15H9.8v1.3H8.65v1.15h-1.3v-1.15H6.2v-1.3h1.15Z"),
  // a barcode, cut out of the chest
  coder: bust(" M5.4 10.4h1v3.2h-1Z M7.1 10.4h.65v3.2H7.1Z M8.45 10.4h1.1v3.2h-1.1Z M10.25 10.4h.65v3.2h-.65Z"),
  // a record card with two lines
  documentarian: [...bust("", -1.5), { d: "M10.4 8.4h3.1l1.9 1.9v4.2a.75.75 0 0 1-.75.75h-4.25a.75.75 0 0 1-.75-.75v-5.35a.75.75 0 0 1 .75-.75Z M11.2 11.3h3.2v.8h-3.2Z M11.2 12.9h3.2v.8h-3.2Z", badge: true }],
  // a headset: band and two cups round a smaller head
  dispatcher: [
    { d: "M8 2.9a2.2 2.2 0 1 1 0 4.4A2.2 2.2 0 1 1 8 2.9Z" }, { d: BODY },
    { d: "M4.1 5.2a3.9 3.9 0 0 1 7.8 0h-.8a3.1 3.1 0 0 0-6.2 0Z" },
    { d: "M3.4 5h1.7v2.7a.5.5 0 0 1-.5.5h-.7a.5.5 0 0 1-.5-.5Z M10.9 5h1.7v2.7a.5.5 0 0 1-.5.5h-.7a.5.5 0 0 1-.5-.5Z" },
  ],
  // the register's own truck (the mobility glyph), small
  driver: [...bust("", -1.5), { d: TRUCK, tf: "translate(8.6 8.2) scale(.46)", badge: true }],
  // a screen on a stand
  office: [...bust("", -1.5), { d: "M9.9 8.6h5a.6.6 0 0 1 .6.6v3.6a.6.6 0 0 1-.6.6h-5a.6.6 0 0 1-.6-.6V9.2a.6.6 0 0 1 .6-.6Z M11.9 13.4h1v1h1.1v.9h-3.2v-.9h1.1Z", badge: true }],
  // a speech bubble: someone who advises
  consultant: [...bust("", -1.5), { d: "M10.6 1h4a.9.9 0 0 1 .9.9v2.7a.9.9 0 0 1-.9.9h-2.1l-1.5 1.3V5.5h-.4a.9.9 0 0 1-.9-.9V1.9a.9.9 0 0 1 .9-.9Z", badge: true }],
  // a price tag
  seller: [...bust("", -1.5), { d: "M10.1 9.1h3.1l2.3 2.35-2.3 2.35h-3.1a.6.6 0 0 1-.6-.6V9.7a.6.6 0 0 1 .6-.6Z M11.3 10.9a.55.55 0 1 0 0 1.1a.55.55 0 1 0 0-1.1Z", badge: true }],
  org: [{ d: CIVIC }],
  provider: [{ d: FIRM }],
  software: [{ d: WINDOW }],
  // nobody: the plain bust, drawn as a dashed outline (see Glyph)
  nobody: bust(),
};

const OBJ_GLYPH: Record<Obj, string> = {
  // a page, its corner cut, three lines
  document: "M3.5 1.25h5.75l3.5 3.5v9.25a.75.75 0 0 1-.75.75H3.5a.75.75 0 0 1-.75-.75V2a.75.75 0 0 1 .75-.75Z M4.75 7.25h6.5v1.1h-6.5Z M4.75 9.75h6.5v1.1h-6.5Z M4.75 12.25h4v1.1h-4Z",
  // a mobile phone, its screen cut out
  phone: "M5 1h6a1.25 1.25 0 0 1 1.25 1.25v11.5A1.25 1.25 0 0 1 11 15H5a1.25 1.25 0 0 1-1.25-1.25V2.25A1.25 1.25 0 0 1 5 1Z M5.25 2.75v9.25h5.5V2.75Z",
  // an envelope, its flap a gap
  email: "M2.25 3h11.5a.75.75 0 0 1 .75.75v8.5a.75.75 0 0 1-.75.75H2.25a.75.75 0 0 1-.75-.75v-8.5A.75.75 0 0 1 2.25 3Z M2.9 4.4L8 8.35l5.1-3.95v1.45L8 9.8 2.9 5.85Z",
  software: WINDOW,
  // three stacked discs
  registry: "M2.5 3.75C2.5 2.5 5 1.5 8 1.5s5.5 1 5.5 2.25S11 6 8 6 2.5 5 2.5 3.75Z M2.5 5.9C3.4 6.9 5.6 7.5 8 7.5s4.6-.6 5.5-1.6v2.35C13.5 9.5 11 10.5 8 10.5S2.5 9.5 2.5 8.25Z M2.5 10.4c.9 1 3.1 1.6 5.5 1.6s4.6-.6 5.5-1.6v2.35c0 1.25-2.5 2.25-5.5 2.25s-5.5-1-5.5-2.25Z",
  // a receipt with a torn foot
  invoice: "M3 1.5h10v13l-1.67-1-1.66 1-1.67-1-1.67 1-1.66-1L3 14.5Z M5 4.5h6v1.1H5Z M5 7h6v1.1H5Z M5 9.5h3.5v1.1H5Z",
  // a clipboard
  form: "M3.25 2.5h2V2a.5.5 0 0 1 .5-.5h4.5a.5.5 0 0 1 .5.5v.5h2a.75.75 0 0 1 .75.75v11a.75.75 0 0 1-.75.75h-9.5a.75.75 0 0 1-.75-.75v-11a.75.75 0 0 1 .75-.75Z M6.25 2.5v1.25h3.5V2.5Z M5 6.5h6v1.1H5Z M5 9h6v1.1H5Z M5 11.5h3.5v1.1H5Z",
  // a sheet with a header row and four cells
  spreadsheet: "M2.25 2.5h11.5a.75.75 0 0 1 .75.75v9.5a.75.75 0 0 1-.75.75H2.25a.75.75 0 0 1-.75-.75v-9.5a.75.75 0 0 1 .75-.75Z M3 5h3.25v2.5H3Z M7 5h6v2.5H7Z M3 8.5h3.25v2.75H3Z M7 8.5h6v2.75H7Z",
};

function Glyph({ parts, size, ghost = false }: { parts: Part[]; size: number; ghost?: boolean }) {
  return (
    <svg className="lk-glyph" viewBox="0 0 16 16" width={size} height={size} aria-hidden="true"
      fill={ghost ? "none" : "currentColor"} fillRule="evenodd" clipRule="evenodd">
      {parts.map((p, i) => (
        <path key={i} d={p.d} transform={p.tf}
          {...(ghost ? { stroke: "currentColor", strokeWidth: 0.9, strokeDasharray: "1.6 1.3" } : {})}
          {...(p.badge && !ghost ? { stroke: "var(--lk-ground, #fff)", strokeWidth: 1.5, paintOrder: "stroke" } : {})} />
      ))}
    </svg>
  );
}

export const RoleIcon = ({ role, size = 22 }: { role: Role; size?: number }): ReactNode =>
  <Glyph parts={ROLE_GLYPH[role]} size={size} ghost={role === "nobody"} />;
export const ObjIcon = ({ obj, size = 16 }: { obj: Obj; size?: number }): ReactNode =>
  <Glyph parts={[{ d: OBJ_GLYPH[obj] }]} size={size} />;
/** the ONE thing the solution brings: a system (a window) or a provider (a firm) */
export const OneIcon = ({ kind, size = 24 }: { kind: "system" | "provider"; size?: number }): ReactNode =>
  <Glyph parts={[{ d: kind === "provider" ? FIRM : WINDOW }]} size={size} />;
