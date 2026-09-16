import type { Metadata } from "next";
import { assertScoringVocabulary } from "../lib/scorecard";

// THE ROOT LAYOUT CARRIES NO DESIGN. Each route group brings its own stylesheet
// and fonts (docs/modern-migration.md step 3, audit B9): `(gazette)/layout.tsx`
// loads web/shared.css and the gazette fonts for the routes that are still
// gazette pages, and the modern pages load their own. A stylesheet imported here
// would reach every page, which is how the modern pages came to load the
// gazette sheet and both font stacks.
export const metadata: Metadata = {
  title: "localproblems.org — a public register of local problems",
  description:
    "Real local problems, stated properly. Distilled weekly from tenders, regulations, funding rounds and documented complaints; every claim links to its source.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  assertScoringVocabulary(); // build gate: verdict words must match SCORING.md
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
