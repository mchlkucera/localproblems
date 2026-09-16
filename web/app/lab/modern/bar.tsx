// /lab/modern — the top bar: brand · country switcher · site links.
//
// Shared so every modern page marks its own link current. `current` names the
// page being shown; that link gets aria-current="page" (primary gray, and on a
// phone it is the one hidden to make room — see front.css). Styles live in
// ./front.css under `.lf`, so a page using this bar renders inside `.lab.lf`
// and imports that stylesheet.
import { CountrySwitcher } from "./country";

export type BarPage = "problems" | "how-it-works";

const LINKS: { page: BarPage | "signals"; href: string; label: string }[] = [
  { page: "problems", href: "/lab/modern", label: "Problems" },
  { page: "signals", href: "/signals/funded", label: "Signals" },
  // "How it works", not "About" (owner, 2026-09-16), pointing at the modern
  // page another session is building in ./how-it-works/
  { page: "how-it-works", href: "/lab/modern/how-it-works", label: "How it works" },
];

export function TopBar({ current }: { current?: BarPage }) {
  return (
    <header className="lf-bar">
      <div className="lf-bar-in">
        <a className="lf-brand" href="/">localproblems.org</a>
        <CountrySwitcher />
        <nav className="lf-nav" aria-label="Site">
          {LINKS.map((link) => (
            <a key={link.page} href={link.href} aria-current={link.page === current ? "page" : undefined}>
              {link.label}
            </a>
          ))}
        </nav>
      </div>
    </header>
  );
}
