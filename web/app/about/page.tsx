// About — the vision and the method, briefly. Serif prose, no chrome tricks.
import type { Metadata } from "next";
import { extractDate, stats } from "../../lib/data";
import { CORRECTIONS_MAILTO, FooterHouseLine, Masthead, SiteNav } from "../../lib/chrome";

export const metadata: Metadata = {
  title: "About — localproblems.org",
  description: "What this register is, where its signals come from, and the rules it holds itself to.",
};

export default function About() {
  const s = stats();
  return (
    <>
      {/* the masthead About link marks itself; the site nav has no About entry */}
      <Masthead current="/about" />
      <SiteNav />

      <h2>What this is</h2>
      <p>
        The age of AI makes solvers abundant and well-stated problems scarce. This register
        collects real local problems — stated properly, with their evidence attached — so that
        a builder can open it and find the one that fits their skills, network, and appetite.
        Czechia is the pilot region; the method is region-general.
      </p>

      <h2>Where the signals come from</h2>
      <p>
        Four streams of public evidence feed the register, collected weekly and kept
        region-blind: <a href="/sources/funded">funded</a> — companies founded and financed
        elsewhere, the proof a model works; <a href="/sources/regulation">regulation</a> —
        obligations with dates, the reason a market appears on schedule;{" "}
        <a href="/sources/tenders">tenders</a> — public money actually moving, from EU notices
        to below-threshold contracts and open subsidy calls; and{" "}
        <a href="/sources/demand">demand</a> — documented complaints and unmet needs, from
        audit findings and ombudsman inventories to petitions and live shortage data.
        Currently {s.signalCount.toLocaleString("en-US").replace(/,/g, " ")} signals on file.
      </p>
      <p>
        A region pass then does the judgment work the collection deliberately avoids: it clusters
        signals into problem records, scores each one against a fixed rubric — proof, money,
        urgency, demand, gap — and writes the statement a builder actually needs: why now, who
        pays, what exists already, where the model works abroad, and what the first moves are.
      </p>

      <h2>The rules it holds itself to</h2>
      <p>
        Every point in every score is justified by a source on file; every number in the prose
        links to where it was recorded. When a figure is not on file, the register says so — it
        never estimates. When a local player turns out to occupy a niche a record called empty,
        the record is corrected in print and de-ranked, with the incumbent named. Corrections
        stay visible. That is the difference between this register and asking a chatbot for
        business ideas: the claims here are checkable, they refresh weekly, and they are
        accountable to what actually happens.
      </p>

      <p className="crumb">
        Extract of <time>{extractDate()}</time> · {s.open} problems on record ·{" "}
        <a href={CORRECTIONS_MAILTO}>Source wrong? Corrections →</a>
      </p>

      <footer>
        <FooterHouseLine />
      </footer>
    </>
  );
}
