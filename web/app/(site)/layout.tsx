// The public site: every page in the modern design (skills/design-language).
// The tokens load here; each page imports its own sheet from ./styles. Every
// page wraps its content in <div className="lab …">, which the tokens are
// scoped to. Inter is self-hosted by the root layout (next/font). A route
// group adds nothing to the URL.
import "./styles/tokens.css";

export default function SiteLayout({ children }: { children: React.ReactNode }) {
  return children;
}
