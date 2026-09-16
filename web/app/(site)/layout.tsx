// The public site: every page in the modern design (skills/design-language).
// The tokens load here; each page imports its own sheet from ./styles. Every
// page wraps its content in <div className="lab …">, which the tokens are
// scoped to. A route group adds nothing to the URL.
import "./styles/tokens.css";

export default function SiteLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" />
      {children}
    </>
  );
}
