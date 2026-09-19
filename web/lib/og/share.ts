// SHARE PREVIEWS: what LinkedIn, X, Facebook, Slack, WhatsApp and iMessage
// show when a link to the site is pasted. The root layout carries the
// site-wide part (metadataBase, site name, type, locale, the large-image
// Twitter card); each page names its own title, description and URL here.
//
// NEXT MERGES METADATA SHALLOWLY: a page that sets `openGraph` replaces the
// root's whole object, the file-based share image included. So every page's
// Open Graph is built by one of the two functions below, never by hand:
//   · `pageOpenGraph` for a record page, which has its own image file
//     (problem/[region]/[id]/opengraph-image.tsx). It sets no `images` key, so
//     Next keeps that file's image.
//   · `siteOpenGraph` for every other page: the same, plus the site card that
//     app/opengraph-image.tsx draws.
// A page that sets no `openGraph` at all (the front page before this module,
// the 404) inherits the root's, and Next fills og:title and og:description
// from its <title> and description.
import type { Metadata } from "next";

/** The one public origin. Relative URLs in metadata resolve against it. */
export const SITE_URL = "https://www.localproblems.org";
export const SITE_NAME = "localproblems.org";

type OpenGraph = NonNullable<Metadata["openGraph"]>;

/** The fields every page shares. `type` stays "website" on every page, the
    records included: one value, one meaning. */
export const OG_BASE = { siteName: SITE_NAME, type: "website", locale: "en_US" } as const satisfies OpenGraph;

/** The site card: app/opengraph-image.tsx, served at /opengraph-image. Named
    here because a page that sets its own `openGraph` loses the file-based one. */
export const SITE_IMAGE_ALT = "Czech problems worth solving: localproblems.org, a public register of local problems";
export const SITE_IMAGE = {
  url: "/opengraph-image",
  width: 1200,
  height: 630,
  type: "image/png",
  alt: SITE_IMAGE_ALT,
} as const;

/** A page's own Open Graph without an image key: the record pages, whose
    opengraph-image file supplies the image. `url` doubles as the canonical. */
export function pageOpenGraph({ title, description, path }: { title: string; description?: string; path: string }): OpenGraph {
  return { ...OG_BASE, title, ...(description ? { description } : {}), url: path };
}

/** Every page without an image of its own: its title, description and URL,
    and the site card. With no description, Next fills it from the page's. */
export function siteOpenGraph(page: { title: string; description?: string; path: string }): OpenGraph {
  return { ...pageOpenGraph(page), images: [SITE_IMAGE] };
}

/** Markdown to one plain line, for <meta> and the share card: no [Sn]
    citation markers, links reduced to their words, no emphasis or code. */
export const plainText = (s: string) =>
  s
    .replace(/\s*\[S\d+(?:\s*,\s*S?\d+)*\](?!\()/g, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/(^|[^*\w])[*_]([^*_\n]+)[*_](?![*\w])/g, "$1$2")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
