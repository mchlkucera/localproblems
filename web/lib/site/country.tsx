// The country switcher in the top bar, and its flags.
//
// Owner, 2026-09-16: "make sure 'Czechia' in the header is a modern dropdown
// with nice flags."
//
// THE FIVE "COMING SOON" (owner, 2026-09-17: "replace the mock … countries
// with countries that you guess have the most builders who are motivated to
// build stuff and problems to be addressed … keep it 5"). An educated guess,
// most likely first, not a roadmap:
//   India   — the world's largest and fastest-growing developer population, and
//             public services, health and SME tooling far behind its demand.
//   Brazil  — Latin America's biggest startup scene, notorious tax and
//             paperwork burden, and a lot of open procurement data.
//   Nigeria — Africa's most active builder and fintech scene, working around
//             missing payments, power and logistics infrastructure.
//   Ukraine — a deep engineering bench rebuilding a country, with EU accession
//             and reconstruction money pushing buyers to act.
//   Germany — Europe's largest pool of engineers beside one of its slowest
//             public and SME digitisation records; EU evidence like Czechia's.
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
// as "Coming soon".
//
// FLAGS ARE INLINE SVG, never emoji (Windows renders those as two letters) and
// never an image request. Every flag is drawn in one 20×14 box, clipped to a
// 2px radius by CSS, with a hairline inset border so a white stripe still
// reads on a white menu. Colours are the official ones; stripes are exact
// halves or thirds of the box; Czechia's wedge reaches half the length. At
// 20×14 India's 24-spoke chakra is a ring and hub, and Brazil keeps its
// rhombus, globe and white band but not the stars or motto.
import type { CSSProperties, ReactNode } from "react";

type Code = "cz" | "in" | "br" | "ng" | "ua" | "de";

const W = 20;
const H = 14;
const third = H / 3;

/** The hairline that keeps white stripes visible on white. */
const Edge = () => <rect x=".25" y=".25" width={W - 0.5} height={H - 0.5} rx="1.75" fill="none" stroke="#000" strokeOpacity=".16" strokeWidth=".5" />;

const vstripes3 = (a: string, b: string, c: string) => (
  <>
    <rect width={W / 3} height={H} fill={a} />
    <rect x={W / 3} width={W / 3} height={H} fill={b} />
    <rect x={(W / 3) * 2} width={W / 3} height={H} fill={c} />
  </>
);

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
  // saffron, white, green thirds; the navy chakra as a ring and hub
  in: (
    <>
      {stripes3("#FF671F", "#fff", "#046A38")}
      <circle cx={W / 2} cy={H / 2} r="1.95" fill="none" stroke="#06038D" strokeWidth=".45" />
      <circle cx={W / 2} cy={H / 2} r=".45" fill="#06038D" />
    </>
  ),
  // green field, yellow rhombus, blue globe crossed by a white band
  br: (
    <>
      <rect width={W} height={H} fill="#009C3B" />
      <path d={`M1.7 ${H / 2}L${W / 2} 1.2L18.3 ${H / 2}L${W / 2} 12.8Z`} fill="#FFDF00" />
      <circle cx={W / 2} cy={H / 2} r="3.5" fill="#002776" />
      <path d="M6.55 6.4Q10 5.3 13.45 7.55" fill="none" stroke="#fff" strokeWidth=".6" />
    </>
  ),
  // green, white, green, vertical thirds
  ng: vstripes3("#008751", "#fff", "#008751"),
  // blue over yellow
  ua: (
    <>
      <rect width={W} height={H / 2} fill="#0057B7" />
      <rect y={H / 2} width={W} height={H / 2} fill="#FFD700" />
    </>
  ),
  de: stripes3("#000", "#DD0000", "#FFCE00"),
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
  { code: "in", name: "India", short: "IN", adjective: "Indian", live: false },
  { code: "br", name: "Brazil", short: "BR", adjective: "Brazilian", live: false },
  { code: "ng", name: "Nigeria", short: "NG", adjective: "Nigerian", live: false },
  { code: "ua", name: "Ukraine", short: "UA", adjective: "Ukrainian", live: false },
  { code: "de", name: "Germany", short: "DE", adjective: "German", live: false },
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
              <a className="lf-cc-item" href="/" aria-current="true">
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
