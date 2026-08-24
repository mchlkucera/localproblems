import { Masthead, SiteNav } from "../lib/chrome";

export default function NotFound() {
  return (
    <>
      <Masthead />
      <SiteNav />
      <h2>404</h2>
      <p>Record not found. Check the address, or start from the register.</p>
      <p className="crumb"><a href="/">← Back to the register</a></p>
    </>
  );
}
