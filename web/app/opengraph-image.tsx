// /opengraph-image — the site's share card, for every page without its own:
// the front page, How it works, the category and signals pages, the 404.
// STATIC: prerendered at build time (no request data), served as a PNG file.
// The record pages draw their own (problem/[region]/[id]/opengraph-image.tsx).
import { ImageResponse } from "next/og";
import { CARD, SiteCard, cardFonts } from "../lib/og/card";
import { SITE_IMAGE_ALT } from "../lib/og/share";

export const alt = SITE_IMAGE_ALT;
export const size = CARD;
export const contentType = "image/png";

/** The front page's title and lede, verbatim (lib/site/front.tsx). */
const TITLE = "Czech problems worth solving";
const LINE = "The register looks for problems where three things meet: what people want, what government wants, and what already works abroad.";

export default function Image() {
  return new ImageResponse(<SiteCard title={TITLE} line={LINE} />, { ...size, fonts: cardFonts() });
}
