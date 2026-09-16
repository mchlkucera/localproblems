// /signals/[type]/[page] — ledger pages 2…N. Page 1 is the parent
// route. As on the live ledger, `dynamicParams = false` plus params that skip
// page 1 make `/…/funded/1` a 404 (not a second address for page 1) and
// `/…/funded/99` a 404 (not an empty page claiming there are no signals).
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "../../../styles/front.css";
import "../../../styles/signals.css";
import { EVIDENCE_TYPES, ledgerPages, type EvidenceType } from "../../../../../lib/data";
import { everyLedgerPage } from "../../../../../lib/ledger";
import { LedgerPage, ledgerMetadata } from "../../../../../lib/site/ledger";

export const dynamicParams = false;

export function generateStaticParams() {
  // bottom-up: no layout above names `[type]`, so the child names both segments
  return everyLedgerPage()
    .filter(({ page }) => page > 1)
    .map(({ type, page }) => ({ type, page: String(page) }));
}

type Params = { params: Promise<{ type: EvidenceType; page: string }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { type, page } = await params;
  return ledgerMetadata(type, Number(page));
}

export default async function ModernSignalsPage({ params }: Params) {
  const { type, page } = await params;
  const n = Number(page);
  if (!(EVIDENCE_TYPES as readonly string[]).includes(type) || !Number.isInteger(n) || n < 2 || n > ledgerPages(type) || String(n) !== page) notFound();
  return <LedgerPage type={type} page={n} />;
}
