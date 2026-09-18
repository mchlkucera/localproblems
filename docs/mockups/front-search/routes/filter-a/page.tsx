// MOCKUP A (2026-09-18) — filter chips only, no typing. STATIC: no
// `searchParams`, so the route pre-renders like every other page.
//
// The register, plus one quiet bar of toggles above it: category (a real link
// to /category/<slug>, so it works with no script), opportunity band, deadline
// within a year, nobody sells it here yet. Chips combine; the count line says
// what is showing. With scripts off only the category links are rendered, and
// the count line reads the plain total.
import type { Metadata } from "next";
import "../styles/front.css";
import "../styles/filter-mock.css";
import { ChipPage } from "../../../lib/site/filter-mock";

export const metadata: Metadata = { title: "Mockup A · filter chips — localproblems.org" };

export default function FilterA() {
  return <ChipPage current="a" note="filter chips only, no typing" search={false} />;
}
