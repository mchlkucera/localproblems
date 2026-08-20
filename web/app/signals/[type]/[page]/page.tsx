// Signal ledger, pages 2…N. Page 1 is the parent route at `/signals/[type]`.
//
// `dynamicParams = false` plus a generateStaticParams that skips page 1 means
// `/signals/funded/1` is a 404 rather than a duplicate of `/signals/funded`,
// and `/signals/funded/99` is a 404 rather than an empty ledger claiming there
// are no signals. Both are the honest answer: the register never publishes a
// page it does not have.
import type { Metadata } from "next";
import { ledgerPages, type EvidenceType } from "../../../../lib/data";
import { Ledger, TITLES, everyLedgerPage } from "../../../../lib/ledger";
import { pad2 } from "../../../../lib/format";

export const dynamicParams = false;

export function generateStaticParams() {
  // Bottom-up: no layout sits above this segment, so the child names both
  // `[type]` and `[page]` (next/docs generate-static-params).
  return everyLedgerPage()
    .filter(({ page }) => page > 1)
    .map(({ type, page }) => ({ type, page: String(page) }));
}

type Params = { params: Promise<{ type: EvidenceType; page: string }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { type, page } = await params;
  return {
    title: `${TITLES[type]} · page ${pad2(Number(page))} of ${pad2(ledgerPages(type))} — localproblems.org`,
  };
}

export default async function SignalsPagePage({ params }: Params) {
  const { type, page } = await params;
  return <Ledger type={type} page={Number(page)} />;
}
