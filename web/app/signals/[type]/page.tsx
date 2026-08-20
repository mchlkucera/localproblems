// Signal ledger, page 1 — the canonical entry for an evidence type and the
// provenance target for every record footer (SPEC.md §5).
//
// PAGE 1 KEEPS THE BARE URL. `/signals/funded` is what the nav links, what the
// retired `/sources/:type` 308 lands on (next.config.ts), and what every
// pre-paging bookmark holds. Pages 2…N live at `/signals/[type]/[page]`; there
// is deliberately no `/signals/funded/1`, so no document has two addresses.
import type { Metadata } from "next";
import { EVIDENCE_TYPES, type EvidenceType } from "../../../lib/data";
import { Ledger, TITLES } from "../../../lib/ledger";

export const dynamicParams = false;

export function generateStaticParams() {
  return EVIDENCE_TYPES.map((type) => ({ type }));
}

type Params = { params: Promise<{ type: EvidenceType }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { type } = await params;
  return { title: `${TITLES[type]} — localproblems.org` };
}

export default async function SignalsPage({ params }: Params) {
  const { type } = await params;
  return <Ledger type={type} page={1} />;
}
