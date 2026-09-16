// The top bar: brand · country switcher · site links.
//
// Shared so every modern page marks its own link current. `current` names the
// page being shown; that link gets aria-current="page" (primary gray). Styles
// live in app/(site)/styles/front.css under `.lf`, so a page using this bar renders inside
// `.lab.lf` and imports that stylesheet.
//
// ON A PHONE ONE LINK GOES, AND THE BAR PICKS IT: three links cannot share
// 375px with the brand and the country switcher, so the link to the page
// being shown is hidden (`lf-nav-spare`), and on a page with no current link
// (the 404) "Problems" goes, because those pages link back to it in their
// body. No page needs its own hide-a-link CSS.
import { CountrySwitcher } from "./country";

export type BarPage = "problems" | "signals" | "how-it-works";

const LINKS: { page: BarPage; href: string; label: string }[] = [
  { page: "problems", href: "/", label: "Problems" },
  { page: "signals", href: "/signals/funded", label: "Signals" },
  // "How it works", not "About" (owner, 2026-09-16)
  { page: "how-it-works", href: "/how-it-works", label: "How it works" },
];

export function TopBar({ current }: { current?: BarPage }) {
  const spare: BarPage = current ?? "problems";
  return (
    <header className="lf-bar">
      <div className="lf-bar-in">
        <a className="lf-brand" href="/">localproblems.org</a>
        <CountrySwitcher />
        <nav className="lf-nav" aria-label="Site">
          {LINKS.map((link) => (
            <a
              key={link.page}
              href={link.href}
              className={link.page === spare ? "lf-nav-spare" : undefined}
              aria-current={link.page === current ? "page" : undefined}
            >
              {link.label}
            </a>
          ))}
        </nav>
      </div>
    </header>
  );
}
