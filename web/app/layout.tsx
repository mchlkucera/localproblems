import "../shared.css";
import type { Metadata } from "next";
import { assertScoringVocabulary } from "../lib/scorecard";

export const metadata: Metadata = {
  title: "localproblems.org — a public register of local problems",
  description:
    "Real local problems, stated properly. Distilled weekly from tenders, regulations, funding rounds and documented complaints; every claim links to its source.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  assertScoringVocabulary(); // build gate: verdict words must match SCORING.md
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
