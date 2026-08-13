import { Masthead, SiteNav } from "../lib/chrome";

export default function NotFound() {
  return (
    <>
      <Masthead />
      <SiteNav />
      <h2>404</h2>
      <p>Record not found. Either it never existed, or it was solved so thoroughly it disappeared.</p>
      <p className="crumb"><a href="/">← Back to the register</a></p>
    </>
  );
}
