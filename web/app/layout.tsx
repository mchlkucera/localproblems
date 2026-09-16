import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { assertScoringVocabulary } from "../lib/scorecard";

// THE ROOT LAYOUT CARRIES NO DESIGN, only the font. Each route group brings its
// own stylesheet (docs/modern-migration.md step 3, audit B9): `(site)/layout.tsx`
// loads the modern tokens and `(gazette)/layout.tsx` loads web/shared.css for
// the private /sources page. A stylesheet imported here would reach every page,
// which is how the modern pages came to load the gazette sheet and both font
// stacks.
//
// INTER IS SELF-HOSTED (next/font): the files are downloaded at BUILD time and
// served from this site, so no reader's browser ever requests Google Fonts. It
// is declared here, as the `--font-inter` variable on <html>, because the root
// 404 renders outside the (site) layout and must get the same face; tokens.css
// reads the variable (`--l-font`). One family, the three weights the design
// uses (skills/design-language §2).
const inter = Inter({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500", "600"],
  display: "swap",
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "localproblems.org — a public register of local problems",
  description:
    "Real local problems, stated properly. Distilled weekly from tenders, regulations, funding rounds and documented complaints; every claim links to its source.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  assertScoringVocabulary(); // build gate: verdict words must match SCORING.md
  return (
    <html lang="en" className={inter.variable}>
      <body>{children}</body>
    </html>
  );
}
