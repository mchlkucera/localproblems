// / — the front page, grouped by opportunity. STATIC: it reads no
// `searchParams`; the category grouping is its own route, ./by-category/.
// Everything else lives in lib/site/front.tsx, which both routes share.
import "./styles/front.css";
import { FrontPage, frontMetadata } from "../../lib/site/front";
import type { Metadata } from "next";
import { siteOpenGraph } from "../../lib/og/share";

// the share preview (lib/og/share.ts): the title alone, this URL and the site
// card; og:description is filled from the lede
export const metadata: Metadata = { ...frontMetadata, openGraph: siteOpenGraph({ title: "Czech problems worth solving", path: "/" }) };

export default function LabFront() {
  return <FrontPage group="opportunity" />;
}
