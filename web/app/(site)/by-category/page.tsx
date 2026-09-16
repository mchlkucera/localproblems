// /by-category — the front page, grouped by category. STATIC, like
// ../page.tsx; it replaces the old `?group=category` query (audit B1).
import "../styles/front.css";
import { FrontPage, frontMetadata } from "../../../lib/site/front";

export const metadata = frontMetadata;

export default function LabFrontByCategory() {
  return <FrontPage group="category" />;
}
