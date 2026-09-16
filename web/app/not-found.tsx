// The 404, in the modern design. The live 404's plain meaning, kept: the record
// is not here, check the address, go back to the problems.
//
// SCOPE (next/docs file-conventions/not-found): the ROOT not-found renders for
// every URL that matches no route AND for every `notFound()` below it (a
// rejected or unknown record, an unknown category, a ledger page past the end,
// the private /sources without LP_ADMIN).
//
// IT IS PART OF EVERY PAGE'S TREE. Whatever this file imports loads on every
// route, which is why it must never import the gazette stylesheet (audit B9:
// a gazette 404 put web/shared.css and the gazette fonts on the modern pages).
// Its own sheets are scoped under `.lab` / `.lf` / `.lnf` and touch nothing else.
import "./lab/tokens.css";
import "./lab/modern/front.css";
import "./not-found.css";
import { TopBar } from "./lab/modern/bar";

export default function NotFound() {
  return (
    <div className="lab lf lnf">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" />
      <TopBar />
      <main className="lf-wrap">
        <div className="lnf-body">
          <p className="lnf-code">404</p>
          <h1>Record not found</h1>
          <p className="lnf-lede">Check the address, or start again from the list of problems.</p>
          <p className="lnf-back"><a href="/">← Back to Problems</a></p>
        </div>
      </main>
    </div>
  );
}
