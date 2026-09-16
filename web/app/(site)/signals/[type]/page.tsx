// /signals/[type] — a signal ledger, page 1, in the modern design.
// Page 1 keeps the bare URL, as the live `/signals/[type]` does; pages 2…N live
// at ./[page]. STATIC: six params at build time, nothing at request time.
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import "../../styles/front.css";
import "../../styles/signals.css";
import { EVIDENCE_TYPES, type EvidenceType } from "../../../../lib/data";
import { LedgerPage, ledgerMetadata } from "../../../../lib/site/ledger";

export const dynamicParams = false;

export function generateStaticParams() {
  return EVIDENCE_TYPES.map((type) => ({ type }));
}

type Params = { params: Promise<{ type: EvidenceType }> };

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { type } = await params;
  return ledgerMetadata(type, 1);
}

export default async function ModernSignals({ params }: Params) {
  const { type } = await params;
  if (!(EVIDENCE_TYPES as readonly string[]).includes(type)) notFound();
  return <LedgerPage type={type} page={1} />;
}
