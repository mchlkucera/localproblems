// MOCKUP C (2026-09-18) — keyboard-first. STATIC, like A and B.
//
// The page below the bar is the register, untouched. "Search problems…" sits in
// the top bar and opens a native popover on click, or on `/`; the overlay lists
// every problem as a compact row (title, category, score dot) and the script
// narrows it as you type, Enter opens the first hit, Escape closes. With no
// script the popover still opens — its rows are server-rendered — so the
// overlay degrades into a complete one-line index of the register.
import type { Metadata } from "next";
import "../styles/front.css";
import "../styles/filter-mock.css";
import { PalettePage } from "../../../lib/site/filter-mock";

export const metadata: Metadata = { title: "Mockup C · keyboard search — localproblems.org" };

export default function FilterC() {
  return <PalettePage />;
}
