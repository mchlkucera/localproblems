// Option H — who pays whom. Where the money comes from, who buys, and who is
// paid today; then the suggested solution's place in the same chain, dashed. A
// sentence the record states WITHOUT a citation is kept and marked, so the
// figure shows its own weak links instead of borrowing a source for them.
import type { ReactNode } from "react";
import type { Chain, Node } from "./hand";

type Cite = (nums: number[]) => ReactNode;

function Box({ n, cite }: { n: Node; cite: Cite }) {
  return (
    <span className={n.uncited ? "fgh-box is-uncited" : "fgh-box"}>
      {n.text}
      {n.cites.length > 0 && <> {cite(n.cites)}</>}
      {n.uncited && <span className="fgh-nosrc">no source on this sentence</span>}
    </span>
  );
}

export function ChainFig({ c, cite }: { c: Chain; cite: Cite }) {
  return (
    <div className="fgh">
      <div className="fgh-grid">
        <p className="fgh-ch">Money comes from</p>
        <span />
        <p className="fgh-ch">Buyer</p>
        <span />
        <p className="fgh-ch">Paid today</p>

        <div className="fgh-col">{c.funders.map((n, i) => <Box key={i} n={n} cite={cite} />)}</div>
        <span className="fgh-arrow" aria-hidden="true" />
        <div className="fgh-col fgh-col--mid"><span className="fgh-box fgh-box--buyer">{c.buyer.text}</span></div>
        <span className="fgh-arrow" aria-hidden="true" />
        <div className="fgh-col">{c.paidToday.map((n, i) => <Box key={i} n={n} cite={cite} />)}</div>
      </div>
      <div className="fgh-sol">
        <span className="fgh-sol-k">Suggested solution</span>
        <span className="fgh-sol-v">{c.solution.text}{c.solution.cites.length > 0 && <> {cite(c.solution.cites)}</>}</span>
      </div>
    </div>
  );
}
