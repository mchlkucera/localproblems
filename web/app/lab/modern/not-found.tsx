// /lab/modern — the 404, in the modern design. The live 404's plain meaning,
// kept: the record is not here, check the address, go back to the problems.
//
// SCOPE (next/docs file-conventions/not-found): a segment `not-found.tsx`
// renders when a page BELOW it calls `notFound()` — a rejected or unknown
// record, an unknown category, a ledger page past the end. A URL that matches
// no route at all (`/lab/modern/no/such/path`) is answered by the ROOT
// `app/not-found.tsx`, which is still the gazette page until the migration moves
// this file there. It also renders only with LP_ADMIN=1: without it the /lab
// layout's own `notFound()` falls through to the root 404.
import "./front.css";
import "./not-found.css";
import { TopBar } from "./bar";

export default function ModernNotFound() {
  return (
    <div className="lab lf lnf">
      <TopBar />
      <main className="lf-wrap">
        <div className="lnf-body">
          <p className="lnf-code">404</p>
          <h1>Record not found</h1>
          <p className="lnf-lede">Check the address, or start again from the list of problems.</p>
          <p className="lnf-back"><a href="/lab/modern">← Back to Problems</a></p>
        </div>
      </main>
    </div>
  );
}
