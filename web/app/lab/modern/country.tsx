// /lab/modern — the country switcher in the top bar, and its flags.
//
// Owner, 2026-09-16: "make sure 'Czechia' in the header is a modern dropdown
// with nice flags. Fetch some countries around Czechia for now."
//
// TWO TRIGGERS, ONE MENU (owner, 2026-09-16): the top bar's text button
// ("Czechia", "CZ" on a phone — no flag: "hide the flag in the currently
// selected selector, show it only in the dropdown") and the word "Czech" in
// the page heading ("make 'Czech' also a selectable thing"). Both render
// <CountryMenu>, the same component and list; each gets its own instance
// because a popover is anchored to one button.
//
// NATIVE, NO SCRIPT: a <button popovertarget> opens a `popover="auto"` menu
// placed with CSS anchor positioning, so click/tap/Enter/Space open it,
// Escape and an outside click close it, and Tab moves from the button into
// the menu — all from the platform. Only Czechia has data: it is the one
// link, marked current; the neighbours are listed, muted and not focusable,
// as "Coming soon" (the live site's region line says the same).
//
// FLAGS ARE INLINE SVG, never emoji (Windows renders those as two letters) and
// never an image request. Every flag is drawn in one 20×14 box, clipped to a
// 2px radius by CSS, with a hairline inset border so a white stripe still
// reads on a white menu. Colours are the official ones; stripes are exact
// halves or thirds of the box; Czechia's wedge reaches half the length.
import type { CSSProperties, ReactNode } from "react";

type Code = "cz" | "de" | "pl" | "sk" | "at" | "hu";

const W = 20;
const H = 14;
const third = H / 3;

/** The hairline that keeps white stripes visible on white. */
const Edge = () => <rect x=".25" y=".25" width={W - 0.5} height={H - 0.5} rx="1.75" fill="none" stroke="#000" strokeOpacity=".16" strokeWidth=".5" />;

const stripes3 = (a: string, b: string, c: string) => (
  <>
    <rect width={W} height={third} fill={a} />
    <rect y={third} width={W} height={third} fill={b} />
    <rect y={third * 2} width={W} height={third} fill={c} />
  </>
);

const FLAG_ART: Record<Code, ReactNode> = {
  // white over red, a blue wedge from the hoist to half the length
  cz: (
    <>
      <rect width={W} height={H / 2} fill="#fff" />
      <rect y={H / 2} width={W} height={H / 2} fill="#D7141A" />
      <path d={`M0 0L${W / 2} ${H / 2}L0 ${H}Z`} fill="#11457E" />
    </>
  ),
  de: stripes3("#000", "#DD0000", "#FFCE00"),
  // white over red
  pl: (
    <>
      <rect width={W} height={H / 2} fill="#fff" />
      <rect y={H / 2} width={W} height={H / 2} fill="#DC143C" />
    </>
  ),
  // white, blue, red thirds; the arms toward the hoist, centred on the flag's
  // height: a white-edged red shield, the white double cross on three blue hills
  sk: (
    <>
      {stripes3("#fff", "#0B4EA2", "#EE1C25")}
      <path d="M3.9 3H10.1V7.6C10.1 9.9 8.7 11.1 7 11.9C5.3 11.1 3.9 9.9 3.9 7.6Z" fill="#fff" />
      <path d="M4.45 3.55H9.55V7.6C9.55 9.55 8.35 10.6 7 11.3C5.65 10.6 4.45 9.55 4.45 7.6Z" fill="#EE1C25" />
      <path d="M6.65 4.2H7.35V5.2H8.3V5.8H7.35V6.6H8.75V7.25H7.35V9.2H6.65V7.25H5.25V6.6H6.65V5.8H5.7V5.2H6.65Z" fill="#fff" />
      <path d="M4.75 9.35C5.25 8.7 5.95 8.65 6.4 9.15C6.75 8.5 7.25 8.5 7.6 9.15C8.05 8.65 8.75 8.7 9.25 9.35C8.85 10.2 8.1 10.8 7 11.3C5.9 10.8 5.15 10.2 4.75 9.35Z" fill="#0B4EA2" />
    </>
  ),
  at: stripes3("#C8102E", "#fff", "#C8102E"),
  hu: stripes3("#CD2A3E", "#fff", "#436F4D"),
};

export function Flag({ code }: { code: Code }) {
  return (
    <svg className="lf-flag" viewBox={`0 0 ${W} ${H}`} width={W} height={H} aria-hidden="true">
      {FLAG_ART[code]}
      <Edge />
    </svg>
  );
}

/** `short` is the bar's phone label; `adjective` is the heading's word
    ("Czech problems worth solving"). The menu always lists country names. */
const COUNTRIES: { code: Code; name: string; short: string; adjective: string; live: boolean }[] = [
  { code: "cz", name: "Czechia", short: "CZ", adjective: "Czech", live: true },
  { code: "sk", name: "Slovakia", short: "SK", adjective: "Slovak", live: false },
  { code: "pl", name: "Poland", short: "PL", adjective: "Polish", live: false },
  { code: "de", name: "Germany", short: "DE", adjective: "German", live: false },
  { code: "at", name: "Austria", short: "AT", adjective: "Austrian", live: false },
  { code: "hu", name: "Hungary", short: "HU", adjective: "Hungarian", live: false },
];
const current = COUNTRIES[0];

/** A solid caret and a solid tick, matching the page's filled glyphs. */
const Caret = () => (
  <svg className="lf-cc-caret" viewBox="0 0 10 10" width="10" height="10" fill="currentColor" aria-hidden="true">
    <path d="M2.2 3.6h5.6a.4.4 0 0 1 .3.66L5.3 7.1a.4.4 0 0 1-.6 0L1.9 4.26a.4.4 0 0 1 .3-.66Z" />
  </svg>
);
const Tick = () => (
  <svg className="lf-cc-tick" viewBox="0 0 16 16" width="14" height="14" fill="currentColor" aria-hidden="true">
    <path d="M2.9 8.3L6.3 11.7L13.1 4.9L11.95 3.75L6.3 9.4L4.05 7.15Z" />
  </svg>
);

/** The menu, anchored under whichever button owns `id`. */
function CountryMenu({ id, className }: { id: string; className?: string }) {
  return (
    <div
      id={id}
      popover="auto"
      className={className ? `lf-cc-menu ${className}` : "lf-cc-menu"}
      role="dialog"
      aria-label="Country"
      style={{ positionAnchor: `--${id}` } as CSSProperties}
    >
      <p className="lf-cc-head">Country</p>
      <ul className="lf-cc-list">
        {COUNTRIES.map((c) => (
          <li key={c.code}>
            {c.live ? (
              <a className="lf-cc-item" href="/lab/modern" aria-current="true">
                <Flag code={c.code} />
                <span className="lf-cc-item-name">{c.name}</span>
                <Tick />
              </a>
            ) : (
              <span className="lf-cc-item is-soon" aria-disabled="true">
                <Flag code={c.code} />
                <span className="lf-cc-item-name">{c.name}</span>
                <span className="lf-cc-soon">Coming soon</span>
              </span>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

/** The top bar's switcher: the country's name and a caret, no flag. */
export function CountrySwitcher() {
  const id = "lf-country";
  return (
    <span className="lf-crumb lf-cc">
      <button
        type="button"
        className="lf-cc-btn"
        popoverTarget={id}
        aria-label={`Country: ${current.name}`}
        style={{ anchorName: `--${id}` } as CSSProperties}
      >
        <span className="lf-cc-name">{current.name}</span>
        <span className="lf-cc-short" aria-hidden="true">{current.short}</span>
        <Caret />
      </button>
      <CountryMenu id={id} className="lf-cc-menu--bar" />
    </span>
  );
}

/** The heading's word: "Czech" set in the heading's own type, underlined
    dotted with a caret. Its text stays the heading's text ("Czech problems
    worth solving" to a screen reader); what it does is said in a description,
    which never joins the heading's name. Only the button goes inside the h1
    (phrasing content); its menu is <CountryWordMenu />, placed after the h1. */
const WORD_ID = "lf-country-h1";

export function CountryWord() {
  return (
    <button
      type="button"
      className="lf-cc-word"
      popoverTarget={WORD_ID}
      aria-describedby={`${WORD_ID}-d`}
      style={{ anchorName: `--${WORD_ID}` } as CSSProperties}
    >
      {current.adjective}<Caret />
    </button>
  );
}

export function CountryWordMenu() {
  return (
    <>
      <span id={`${WORD_ID}-d`} hidden>Choose a country</span>
      <CountryMenu id={WORD_ID} />
    </>
  );
}
