// /by-category — the front page, grouped by category. STATIC, like
// ../page.tsx; it replaces the old `?group=category` query (audit B1).
import "../styles/front.css";
import { FrontPage, frontMetadata } from "../../../lib/site/front";
import type { Metadata } from "next";
import { siteOpenGraph } from "../../../lib/og/share";

// the share preview (lib/og/share.ts): the title alone, this URL and the site
// card; og:description is filled from the lede
export const metadata: Metadata = { ...frontMetadata, openGraph: siteOpenGraph({ title: "Czech problems worth solving", path: "/by-category" }) };

export default function LabFrontByCategory() {
  return <FrontPage group="category" />;
}
