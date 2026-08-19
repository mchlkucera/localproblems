// The category filter nav — build-time counts, plain links (SPEC.md §5).
// Shared by the register and the category pages; v1 grammar: `All (31) · B2B (07) · …`.
import { CATEGORIES, categoryCounts, registerRows } from "./data";
import { categoryLabel, pad2 } from "./format";

/** `current` is a category id on a category page, undefined on the register ("All").
    Only categories with at least one record appear, in CATEGORIES order. */
export function CategoryNav({ current }: { current?: string }) {
  const counts = categoryCounts();
  return (
    <nav className="filters" aria-label="Categories">
      <a href="/" aria-current={current === undefined ? "page" : undefined}>
        All ({registerRows().length})
      </a>
      {CATEGORIES.filter((c) => counts[c] >= 1).map((c) => (
        <span key={c}>
          {" · "}
          <a href={`/category/${c}`} aria-current={current === c ? "page" : undefined}>
            {categoryLabel(c)} ({pad2(counts[c])})
          </a>
        </span>
      ))}
    </nav>
  );
}
