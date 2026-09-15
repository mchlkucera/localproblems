// One monoline illustration per register category — the lab record page's
// header art (owner, 2026-09-15: "maybe add SVG illustration based on the
// category"). CONTRACT (both lab designers build against it):
//   <CategoryArt category={p.category} className="…" />
//   · inline SVG, viewBox "0 0 240 160", decorative (aria-hidden)
//   · strokes only, `currentColor`, so the page sets the gray via `color`
//   · unknown category → the `other` drawing, never nothing
// PLACEHOLDER until the illustration pass lands: a quiet framed rectangle.
export function CategoryArt({ category, className }: { category: string; className?: string }) {
  return (
    <svg
      className={className}
      viewBox="0 0 240 160"
      width="240"
      height="160"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.25"
      aria-hidden="true"
      data-category={category}
    >
      <rect x="40" y="30" width="160" height="100" rx="4" />
    </svg>
  );
}
