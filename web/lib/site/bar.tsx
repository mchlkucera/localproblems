// The top bar: brand · country switcher · site links.
//
// Shared so every modern page marks its own link current. `current` names the
// page being shown; that link gets aria-current="page" (primary gray). Styles
// live in app/(site)/styles/front.css under `.lf`, so a page using this bar renders inside
// `.lab.lf` and imports that stylesheet.
//
// ALL THREE LINKS, ALWAYS (owner, 2026-09-17: "there should be always
// problems, signals, how it works visible on all devices … on mobile lets just
// hide it behind a burger menu"). Above 720px the three links sit in the bar.
// On a phone they move into a menu behind one button: a native popover
// (`popovertarget`), so it opens by tap or Enter and closes on Escape or an
// outside tap, with no script. Nothing is dropped any more to make room.
import { CountrySwitcher } from "./country";

export type BarPage = "problems" | "signals" | "how-it-works";

const LINKS: { page: BarPage; href: string; label: string }[] = [
  { page: "problems", href: "/", label: "Problems" },
  { page: "signals", href: "/signals/funded", label: "Signals" },
  // "How it works", not "About" (owner, 2026-09-16)
  { page: "how-it-works", href: "/how-it-works", label: "How it works" },
];

const MENU_ID = "lf-menu";

function Links({ current, className }: { current?: BarPage; className?: string }) {
  return (
    <>
      {LINKS.map((link) => (
        <a
          key={link.page}
          href={link.href}
          className={className}
          aria-current={link.page === current ? "page" : undefined}
        >
          {link.label}
        </a>
      ))}
    </>
  );
}

/** The burger: three solid bars, drawn for this site on the 16-unit grid. */
const Burger = () => (
  <svg viewBox="0 0 16 16" width="18" height="18" fill="currentColor" aria-hidden="true">
    <path d="M2 3.25h12v1.5H2Z M2 7.25h12v1.5H2Z M2 11.25h12v1.5H2Z" />
  </svg>
);

export function TopBar({ current }: { current?: BarPage }) {
  return (
    <header className="lf-bar">
      <div className="lf-bar-in">
        <a className="lf-brand" href="/">localproblems.org</a>
        <CountrySwitcher />
        <nav className="lf-nav" aria-label="Site">
          <Links current={current} />
        </nav>
        <button type="button" className="lf-burger" popoverTarget={MENU_ID} aria-label="Menu">
          <Burger />
        </button>
        <div id={MENU_ID} popover="auto" className="lf-menu" role="dialog" aria-label="Menu">
          <nav aria-label="Site menu">
            <Links current={current} className="lf-menu-item" />
          </nav>
        </div>
      </div>
    </header>
  );
}
