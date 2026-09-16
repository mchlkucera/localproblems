// Option B — the suggested solution, split into its parts, against who already
// sells each part abroad and here. The right-hand verdict is the only coloured
// cell: green marks a part the Czech market check found nobody selling, i.e.
// where the suggested solution has room. An "open" verdict must cite a gap-check
// (the kind of source that runs a positive control) — the absence is the
// check's claim, never the figure's.
import type { ReactNode } from "react";
import type { Part, Seller } from "./hand";
import { shortName } from "./kit/text";

type Cite = (nums: number[]) => ReactNode;

const VERDICT: Record<Part["verdict"], string> = {
  sold: "Sold here",
  early: "Early only",
  open: "Nobody here",
};

function SellerLine({ s, cite }: { s: Seller; cite: Cite }) {
  return (
    <li className="fgp-seller">
      <span className="fgp-name">{shortName(s.name)}</span>
      {s.maturity && <span className={`fgp-mat fgp-mat--${s.maturity}`}>{s.maturity}</span>}
      {s.ledger === "adjacent" && <span className="fgp-mat">sells something else</span>}
      {s.ledger === "off-ledger" && <span className="fgp-mat fgp-mat--off">not on the ledger</span>}
      <span className="fgp-note">{s.note} {s.cites.length > 0 && cite(s.cites)}</span>
    </li>
  );
}

export function PartsFig({ parts, cite }: { parts: Part[]; cite: Cite }) {
  return (
    <div className="fgp" role="table" aria-label="Parts of the suggested solution and who sells each">
      <div className="fgp-row fgp-row--hd" role="row">
        <span role="columnheader">Part of the suggested solution</span>
        <span role="columnheader">Abroad</span>
        <span role="columnheader">In Czechia</span>
        <span role="columnheader" />
      </div>
      {parts.map((p, i) => (
        <div key={i} className={`fgp-row is-${p.verdict}`} role="row">
          <span className="fgp-part" role="cell"><span className="fgp-n">{i + 1}</span>{p.part}</span>
          <span role="cell">
            {p.abroad.length ? (
              <ul className="fgp-list">{p.abroad.map((s) => <SellerLine key={s.name} s={s} cite={cite} />)}</ul>
            ) : (
              <span className="fgp-none">None on the comps ledger</span>
            )}
          </span>
          <span role="cell">
            {p.here.length ? (
              <ul className="fgp-list">{p.here.map((s) => <SellerLine key={s.name} s={s} cite={cite} />)}</ul>
            ) : (
              <span className="fgp-none">None on the local ledger</span>
            )}
          </span>
          <span className={`fgp-verdict fgp-verdict--${p.verdict}`} role="cell">
            <span className="fgp-vpill">{VERDICT[p.verdict]}</span>
            {p.verdictNote && <span className="fgp-vnote">{p.verdictNote}</span>}
            <span className="fgp-vcite">{cite(p.verdictCites)}</span>
          </span>
        </div>
      ))}
    </div>
  );
}
