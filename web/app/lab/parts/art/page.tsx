// /lab/parts/art — review sheet for the category header illustrations
// (category-art.tsx). Every drawing at the size and gray the record header
// uses (240×160, --l-text-3), plus the unknown-slug fallback. LOCAL ONLY:
// the /lab layout 404s without LP_ADMIN=1, and this page checks again.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { CategoryArt } from "./category-art";
import "./art.css";

export const metadata: Metadata = { title: "Category art (lab) — localproblems.org" };

const SLUGS = [
  "fintech", "health", "housing", "energy",
  "mobility", "govtech", "retail-services", "b2b",
  "legal-compliance", "education", "environment", "other",
];

export default function LabArtPage() {
  if (process.env.LP_ADMIN !== "1") notFound();
  return (
    <div className="lab">
      <main className="art-sheet">
        <header className="art-head">
          <h1>Category art</h1>
          <p>Record-page header illustrations, one per category, at 240×160 in --l-text-3.</p>
        </header>
        <ul className="art-grid">
          {SLUGS.map((slug) => (
            <li key={slug}>
              <CategoryArt category={slug} className="art-svg" />
              <span>{slug}</span>
            </li>
          ))}
          <li>
            <CategoryArt category="not-a-category" className="art-svg" />
            <span>unknown slug → other</span>
          </li>
        </ul>
      </main>
    </div>
  );
}
