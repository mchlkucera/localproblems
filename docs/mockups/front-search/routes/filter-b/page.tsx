// MOCKUP B (2026-09-18) — A, plus a search box that filters as you type across
// title, story, suggested solution and category. STATIC, like A.
//
// The box is optional: the list is the whole register without it, and with
// scripts off the box is not rendered at all (a text field that filters
// nothing is a lie), leaving the category links and the true total.
import type { Metadata } from "next";
import "../styles/front.css";
import "../styles/filter-mock.css";
import { ChipPage } from "../../../lib/site/filter-mock";

export const metadata: Metadata = { title: "Mockup B · search and chips — localproblems.org" };

export default function FilterB() {
  return <ChipPage current="b" note="search box plus the same chips" search />;
}
