// /how-it-works — "How it works", in the owner's own words.
//
// SOURCE: mike-oxhard/projects/Localproblems/The vision.md (owner, 2026-09-16).
// Its three sections, in its order, with its words. Only obvious typos and
// punctuation are fixed ("adress" → "address", "company exist" → "companies
// exist", the "and ... what is already solved elsewhere" tail made the list's
// third item, a lead-in colon and a closing comma after "(mikeoxhard.com)",
// typographic quotes). The "?" is dropped from "How it works?" and "Why?".
// Nothing is added or rewritten; the three bare domains became links out.
//
// DESIGN: the front page's chrome and type (styles/front.css, lib/site/bar.tsx),
// one reading column on the page's left content edge, a 64ch measure. The
// three-circle Venn from the front page's header sits under "How it works",
// the idea it draws. `/about` redirects here permanently (next.config.ts).
import type { Metadata } from "next";
import type { ReactNode } from "react";
import "../styles/front.css";
import "../styles/how-it-works.css";
import { TopBar } from "../../../lib/site/bar";
import { CORRECTIONS_MAILTO } from "../../../lib/chrome";
import { siteOpenGraph } from "../../../lib/og/share";
import { Venn } from "./venn";

// the description is the page's own first line, verbatim (audit B14)
export const metadata: Metadata = {
  title: "How it works — localproblems.org",
  description: "A register of meaningful problems to solve.",
  // no description here: Next fills og:description from the page's own
  openGraph: siteOpenGraph({ title: "How it works", path: "/how-it-works" }),
};

/** A link to another site: "↗" after it, and words for screen readers. */
function Out({ href, children }: { href: string; children: ReactNode }) {
  return (
    <a className="lh-out" href={href} target="_blank" rel="noopener noreferrer">
      {children}
      <span className="lh-ext" aria-hidden="true">{"\u202F↗"}</span>
      <span className="lf-sr"> (another site)</span>
    </a>
  );
}

export default function HowItWorks() {

  return (
    <div className="lab lf lh">
      <TopBar current="how-it-works" />

      <main className="lf-wrap">
        <article className="lh-doc">
          <header className="lh-head">
            <h1>How it works</h1>
          </header>

          <section className="lh-sec" aria-labelledby="what">
            <h2 id="what">What is this</h2>
            <p>A register of meaningful problems to solve.</p>
          </section>

          <section className="lh-sec" aria-labelledby="how">
            <h2 id="how">How it works</h2>
            <p>
              This thing is built on the hypothesis that meaningful projects live in the intersection of:
            </p>
            <ul className="lh-list">
              <li>
                What people want and are complaining about (in places like forums, petitions, ombudsman
                inventories)
              </li>
              <li>
                What governments and institutions want (and are issuing regulations, tenders or statements to
                take care of it)
              </li>
              <li>
                What is already solved elsewhere (companies exist and got recently funded or are growing solving
                this problem somewhere abroad)
              </li>
            </ul>
            <Venn className="lh-venn" />
          </section>

          <section className="lh-sec" aria-labelledby="why">
            <h2 id="why">Why</h2>
            <ul className="lh-list lh-list--paras">
              <li>
                Because I, the creator <span className="lh-nw">(<Out href="https://mikeoxhard.com">mikeoxhard.com</Out>),</span> don’t want to
                create another app for pet owner networking. I want to solve something that will Make the world a
                better place™. And because places for global software-shaped problems already exist (
                <Out href="https://ideabrowser.com">ideabrowser.com</Out>,{" "}
                <span className="lh-nw"><Out href="https://bigideasdb.com">bigideasdb.com</Out>)</span> I figured I might start with problems of
                my country.
              </li>
              <li>
                Because I think as the means to build are getting cheaper, the question “what to build” is getting
                more valuable. This place is attempting to address this question.
              </li>
            </ul>
          </section>
        </article>
      </main>

      <footer className="lf-foot">
        <div className="lf-wrap lf-foot-in">
          <span>localproblems.org · Czechia</span>
          <a href={CORRECTIONS_MAILTO}>Report a correction</a>
        </div>
      </footer>
    </div>
  );
}
