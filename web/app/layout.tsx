import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { assertScoringVocabulary } from "../lib/scorecard";
import { OG_BASE, SITE_URL } from "../lib/og/share";

// THE ROOT LAYOUT CARRIES NO DESIGN, only the font. `(site)/layout.tsx` loads
// the modern tokens and each page imports its own sheet (audit B9). A
// stylesheet imported here would reach every page, which is how the modern
// pages once came to load the gazette sheet and both font stacks. The gazette
// route group is gone since 2026-09-17: /sources is a modern page.
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

// SHARE PREVIEWS (lib/og/share.ts): the site-wide half lives here. Every URL in
// metadata resolves against the public origin; the Open Graph carries no title
// or description, so a page that sets none gets its own <title> and
// description, never another page's; the share image is ./opengraph-image.tsx
// (records: their own). X and the rest read the large-image card.
export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: "localproblems.org — a public register of local problems",
  description:
    "Real local problems, stated properly. Distilled weekly from tenders, regulations, funding rounds and documented complaints; every claim links to its source.",
  openGraph: { ...OG_BASE },
  twitter: { card: "summary_large_image" },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  assertScoringVocabulary(); // build gate: verdict words must match SCORING.md
  return (
    <html lang="en" className={inter.variable}>
      <body>{children}</body>
    </html>
  );
}
