#!/usr/bin/env python3
"""
scripts/model_pass.py — the PYTHON HALF of the model seam (INGEST.md 3b / 3d).

WHY THIS FILE EXISTS AT ALL, i.e. why the model call is not inside normalize.py.

`with-secrets` is the only working path to the vault (`direnv exec .` fires the
sops hook, exits clean and exports nothing but DIRENV_* bookkeeping), and it
refuses bash, node, python, jq, awk and sed BY ALLOWLIST — an interpreter can
encode a secret past its output scrubber. normalize.py is a python interpreter,
so it can never be the process holding ANTHROPIC_API_KEY. Only `curl` can, and
only by importing the value itself (`--variable '%ANTHROPIC_API_KEY'`) and
expanding it straight into a header (`--expand-header`), so no process we
control ever holds the secret.

THE SEAM IS THEREFORE THREE PARTS, and the split is the design, not a workaround:

    model_pass.py plan   (python)  reads staged.jsonl -> writes .model/req/*.json
    model_pass.sh        (bash)    `with-secrets curl` per request file, ALONE
    model_pass.py apply  (python)  validates .model/resp/*.json -> staged.jsonl

The secret only ever exists inside one curl process. The request and response
files carry no credential, so the python halves are ordinary file I/O.

CRASH SAFETY. `plan` and the driver never touch staged.jsonl. `apply` reads it
whole, merges validated fields, writes `<raw>/.staged.jsonl.tmp` and os.replace()s
it — atomic on POSIX, so a crash leaves either the old file or the new one and
never a half-written ledger. Nothing is ever deleted (`rm` is blocked in this
environment; stale files are superseded by name, never removed).

RESUMABLE. A batch is "done" when its response file exists. Re-running the
driver skips those; re-running `plan` re-derives pending work from staged.jsonl
itself, which is the only source of truth. A crash costs at most one batch.

VALIDATION IS THE POINT. Every returned field is checked against the closed
vocabularies in data/CONVENTIONS.md before it is written: sector against
SECTORS, geo_origin against ^([A-Z]{2}|EU)$, every score an integer 0-3,
summary at most two sentences. A field that fails is REFUSED — the record keeps
its `_needs` entry and stays staged, because --complete refusing a record is
recoverable and writing vibes into an append-only ledger is not.

ORDER IS LOAD-BEARING (INGEST.md 3a-3d). Pass A (scoring: scale, recurrence,
grade-3 urgency, sector, geo_origin, and the suggest/reddit pain bar) runs over
everything; the MATERIALITY FILTER then decides who survives; only then does
pass B (EN title + summary) run, over SURVIVORS ONLY — so we never pay to write
a summary for a record we are about to discard. `plan --pass B` enforces that by
selecting on is_material() itself, from the same normalize.py function the
filter uses.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from normalize import SECTORS, collapse, is_material, sha1_8  # noqa: E402

MODEL = "claude-opus-5"
GEO_RE = re.compile(r"^([A-Z]{2}|EU)$")

# The fields each pass may write, in a fixed order so a batch signature is
# stable across runs. NOTHING outside these lists is ever written back onto a
# staged record by this file — in particular never `quote` (verbatim, captured
# and verified at ingest, and a model must never be able to invent one) and
# never `money_eur` (pure arithmetic).
PASS_A_FIELDS = ["sector", "geo_origin", "scores.scale", "scores.recurrence",
                 "scores.urgency", "pain", "stated_need"]
PASS_B_FIELDS = ["title", "summary"]

# Payload keys worth putting in front of the model. yc-oss ships HQ location and
# an industry taxonomy in the payload; passing them is the difference between a
# judged geo_origin and a guessed one. Read from the raw payload, never invented.
ENRICH_KEYS = ("all_locations", "industry", "subindustry", "long_description",
               "tags", "batch", "stage", "team_size")

RUBRIC = """\
You are the SCORING pass of an evidence pipeline. You apply a fixed rubric to
signals that have already been fetched and mechanically parsed. You judge ONLY
from the card you are given. You never invent facts, never translate a quote,
and never add or drop an item.

Return EXACTLY ONE result object per input item, with the item's own `id`.

scale (integer 0-3) — how many entities the UNDERLYING NEED touches:
  0 = one organisation only
  1 = a niche segment (a specialised trade, a handful of operators)
  2 = a whole sector (most operators in that sector share the need)
  3 = economy-wide or cross-sector
recurrence (integer 0-3) — how the underlying need repeats:
  0 = a one-off event
  1 = probably repeatable
  2 = a recurring need (annual or continuous)
  3 = structural (mandated or built into how the market works, indefinitely)
urgency (integer 0-3) — ONLY when the item asks for it:
  0 = no dated trigger
  1 = a dated event more than 18 months out
  2 = a dated event less than 18 months out
  3 = less than 6 months out, OR already in force with active enforcement
  An item carrying `event_date_in_past` is the ONLY urgency case you are asked
  to rule on, and the question is narrow: is the obligation or deadline STILL
  BITING today (in force, actively enforced, work still to be delivered) -> 3;
  or has the date simply passed with nothing ongoing -> 0. Never grade an
  expired one-off event above 0 just because it was once imminent.
sector — EXACTLY ONE of: fintech, health, housing, energy, mobility, govtech,
  retail-services, b2b, legal-compliance, education, environment, other.
  Public buyers procuring IT or administration are govtech; generic business
  services are b2b; construction and real estate are housing. Use `other` only
  when no listed sector fits.
geo_origin — where the signal comes FROM, never where it might be useful:
  an ISO-3166-1 alpha-2 code in CAPITALS (GB not UK), or EU for an EU-level
  signal. Resolve a city or region to its country. A tender's geo is its
  buyer's country; a company's geo is its headquarters country. Do not infer a
  country from the language of the text alone.
pain (boolean) — ONLY when the item asks for it. true when the text is a
  COMPLAINT, a FAILURE or a WORKAROUND (something is broken, missing, refused
  or unusable). false for neutral curiosity, how-to questions, marketing and
  anything justified only by engagement.
stated_need (boolean) — ONLY when the item asks for it. The item is an ASK: a
  named institution (a hospital, a city, a ministry) publicly inviting
  solutions. true when the owner names a CONCRETE need it cannot meet today —
  a specific task done by hand, a slow, costly or unreliable process, a
  capacity or a tool it lacks, a decision it cannot make well — even when
  the text is phrased as a request rather than a complaint. false for a
  theme or an area ("environment", "safety"), an open call for ideas, a bare
  topic line, a wish with no stated task, or a vendor's product pitch dressed
  as a challenge. The test is: could a builder start on Monday knowing what
  the owner needs? If the text names the need, true.

RULES
- Score the NEED behind the signal, not the size or fame of the company naming it.
- One organisation buying something for itself is scale 0, however expensive.
- FOR AN ASK (an item carrying `stated_need_bar`), the owner is ONE INSTANCE OF
  ITS KIND, and scale counts how many institutions of that kind share the
  stated need: a hospital asking for structured reports, coded discharge
  summaries or an internal knowledge assistant names a need most hospitals
  have (2); a need shared by a specialised subset of them (1); a need that is
  about THIS institution alone — its own building, its own brand, its own
  staffing roster — (0). "Buying for itself" is scale 0 only in that last
  sense. Do not read "one hospital posted it" as "one organisation only".
- Do not inflate. "A whole sector" means most operators in that sector share it.
- When two grades are defensible, choose the LOWER one.
"""

WRITER = """\
You write the ENGLISH display line for signals that have already been fetched,
parsed and scored. You judge ONLY from the card you are given: never invent a
number, a date, a customer or a name that is not on the card, and never translate
or reproduce the verbatim quote.

Return EXACTLY ONE result object per input item, with the item's own `id`.

title — English, the exact form "Thing — what it is": the subject, then a spaced
  em dash (—), then a short plain-English description. No trailing period, at
  most 95 characters. Example: "Děčín aquapark study — CZ city tender for a
  capacity-expansion feasibility study".
summary — English, AT MOST TWO SENTENCES, factual, no marketing language, no
  speculation about opportunity. Say what the signal is and what it evidences.
"""


# --------------------------------------------------------------------------
# staged.jsonl I/O — the only writer, and it writes atomically
# --------------------------------------------------------------------------

def staged_path(raw):
    return os.path.join(raw, "staged.jsonl")


def model_dir(raw):
    return os.path.join(raw, ".model")


def read_staged(raw):
    recs = []
    with open(staged_path(raw), "r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                recs.append(json.loads(line))
    return recs


def write_staged(raw, recs):
    """Temp + os.replace. NEVER an in-place rewrite: a crash halfway through a
    4,807-line file would leave a truncated staging ledger and no way back."""
    tmp = os.path.join(raw, ".staged.jsonl.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, staged_path(raw))


def load_enrichment(raw):
    """url -> extra payload context, for feeds whose payload carries more than
    the mechanical extractor keeps. Read off the raw payload still on disk; this
    is evidence, not invention."""
    out = {}
    for name in sorted(os.listdir(raw)):
        if not name.endswith(".json") or name in ("contract.json", "staged.jsonl"):
            continue
        try:
            with open(os.path.join(raw, name), "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            continue
        if not isinstance(data, list):
            continue
        for it in data:
            if not isinstance(it, dict):
                continue
            url = it.get("url")
            if not isinstance(url, str) or not url:
                continue
            ctx = {}
            for k in ENRICH_KEYS:
                v = it.get(k)
                if v in (None, "", [], {}):
                    continue
                if isinstance(v, str):
                    v = collapse(v)[:320]
                elif isinstance(v, list):
                    v = [str(x) for x in v][:6]
                ctx[k] = v
            if ctx:
                out[url] = ctx
    return out


# --------------------------------------------------------------------------
# what each record still owes THIS pass
# --------------------------------------------------------------------------

def pending(rec, pass_):
    fields = PASS_A_FIELDS if pass_ == "A" else PASS_B_FIELDS
    needs = rec.get("_needs") or []
    return [f for f in fields if f in needs]


def eligible(recs, pass_):
    """Pass A: everything still owing a pass-A field, minus records already
    refused by the pain bar or exhausted on retries.

    Pass B: SURVIVORS ONLY. The materiality filter sits between the two passes
    (INGEST.md 3c) precisely so no summary is ever written for a record that is
    about to be dropped, so this asks is_material() — the same function
    normalize.py --complete drops on — rather than re-deriving the rule."""
    out = []
    for r in recs:
        if r.get("_model_refused"):
            continue
        if pass_ == "B":
            sc = r.get("scores") or {}
            if not all(isinstance(sc.get(k), int)
                       for k in ("scale", "money", "urgency", "recurrence")):
                continue          # pass A never completed for it
            if not is_material(sc, r.get("evidence_type")):
                continue          # dropped by materiality; pass B never runs
        if pending(r, pass_):
            out.append(r)
    return out


# --------------------------------------------------------------------------
# plan — build the request files
# --------------------------------------------------------------------------

def card_for(rec, pass_, enrich):
    c = {"id": rec["id"], "source": rec.get("source"), "date": rec.get("date")}
    nt = rec.get("title_native") or rec.get("title")
    if nt:
        c["native_title"] = collapse(nt)[:220]
    if rec.get("entity_native"):
        c["entity"] = collapse(rec["entity_native"])[:120]
    ex = collapse(rec.get("excerpt") or "")[:400]
    if ex and ex != c.get("native_title"):
        c["excerpt"] = ex
    if rec.get("money_eur") is not None:
        c["money_eur"] = rec["money_eur"]
    ctx = enrich.get(rec.get("url"))
    if ctx:
        c["payload_context"] = ctx
    if pass_ == "B":
        # The writer sees what the scorer decided, so the English line agrees
        # with the record it belongs to.
        c["sector"] = rec.get("sector")
        c["geo_origin"] = rec.get("geo_origin")
        c["scores"] = rec.get("scores")
    if "scores.urgency" in pending(rec, pass_):
        # urgency is only ever a model field when the arithmetic hit its one
        # unobservable branch: score_urgency() returns None for a date already
        # in the PAST, because "already in force with active enforcement" is a
        # judgement a date subtraction cannot make. Say so on the card rather
        # than handing over a bare date and hoping.
        if rec.get("urgency_date"):
            c["event_date"] = rec["urgency_date"]
        c["event_date_in_past"] = True
    if "pain" in pending(rec, pass_):
        c["pain_bar"] = "this item needs a pain verdict"
    if "stated_need" in pending(rec, pass_):
        c["stated_need_bar"] = "this item needs a stated-need verdict (an ask: does the owner name a concrete need?)"
    return c


def schema_for(pass_, fields):
    props = {"id": {"type": "string"}}
    if pass_ == "A":
        if "sector" in fields:
            props["sector"] = {"type": "string", "enum": sorted(SECTORS)}
        if "geo_origin" in fields:
            props["geo_origin"] = {"type": "string"}
        if "scores.scale" in fields:
            props["scale"] = {"type": "integer", "enum": [0, 1, 2, 3]}
        if "scores.recurrence" in fields:
            props["recurrence"] = {"type": "integer", "enum": [0, 1, 2, 3]}
        if "scores.urgency" in fields:
            props["urgency"] = {"type": "integer", "enum": [0, 1, 2, 3]}
        if "pain" in fields:
            props["pain"] = {"type": "boolean"}
        if "stated_need" in fields:
            props["stated_need"] = {"type": "boolean"}
    else:
        props["title"] = {"type": "string"}
        props["summary"] = {"type": "string"}
    return {
        "type": "object",
        "properties": {
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": props,
                    "required": sorted(props),
                    "additionalProperties": False,
                },
            }
        },
        "required": ["results"],
        "additionalProperties": False,
    }


def build_request(pass_, fields, cards, effort, max_tokens=None):
    system = RUBRIC if pass_ == "A" else WRITER
    return {
        "model": MODEL,
        "max_tokens": max_tokens or min(32000, 2000 + 260 * len(cards)),
        "output_config": {"effort": effort,
                          "format": {"type": "json_schema",
                                     "schema": schema_for(pass_, fields)}},
        "system": system,
        "messages": [{"role": "user",
                      "content": json.dumps({"items": cards}, ensure_ascii=False)}],
    }


def cmd_plan(args):
    raw = os.path.abspath(args.raw)
    mdir = model_dir(raw)
    os.makedirs(os.path.join(mdir, "req"), exist_ok=True)
    os.makedirs(os.path.join(mdir, "resp"), exist_ok=True)
    recs = read_staged(raw)
    enrich = load_enrichment(raw)
    todo = eligible(recs, args.pass_)

    # Group by the exact set of fields the record still owes, so every batch
    # carries ONE schema that requires exactly those keys — no wasted output,
    # and a returned key that was never asked for is a validation error rather
    # than something to silently ignore.
    groups = {}
    for r in todo:
        groups.setdefault(tuple(pending(r, args.pass_)), []).append(r)

    batches, lines = [], []
    for sig in sorted(groups, key=lambda s: (-len(groups[s]), s)):
        members = sorted(groups[sig], key=lambda r: r["id"])
        if args.proof:
            # STRIDE, not head. The groups are sorted by id and ids are prefixed
            # by feed, so members[:10] of the 4,397-record group is ten
            # czechcrunch records and zero yc — a "proof" that never touches 91%
            # of the corpus it is supposed to prove.
            step = max(1, len(members) // args.batch)
            members = members[::step][:args.batch]
        for i in range(0, len(members), args.batch):
            chunk = members[i:i + args.batch]
            # THE BATCH NAME CARRIES A DIGEST OF ITS OWN MEMBERSHIP, and that is
            # what makes a re-plan safe. A positional name (A-...-007) would be
            # reused by the next plan for a DIFFERENT set of records, and the
            # driver — which treats "a response file exists" as "this batch is
            # done" — would hand `apply` an answer about seven other records.
            # With the digest in the name, an identical batch reuses its
            # response (resumability) and a changed one cannot.
            digest = sha1_8("\n".join(r["id"] for r in chunk))
            name = "%s-%s-%03d-%s" % (args.pass_, "_".join(
                f.replace("scores.", "").replace("geo_origin", "geo")[:4]
                for f in sig) or "none", len(batches), digest)
            req = os.path.join(mdir, "req", name + ".json")
            body = build_request(args.pass_, list(sig),
                                 [card_for(r, args.pass_, enrich) for r in chunk],
                                 args.effort)
            with open(req, "w", encoding="utf-8") as fh:
                json.dump(body, fh, ensure_ascii=False)
            batches.append({"name": name, "req": req, "fields": list(sig),
                            "ids": [r["id"] for r in chunk]})
            lines.append(req)

    plan = {"pass": args.pass_, "effort": args.effort, "batch": args.batch,
            "proof": bool(args.proof), "batches": batches}
    with open(os.path.join(mdir, f"plan-{args.pass_}.json"), "w", encoding="utf-8") as fh:
        json.dump(plan, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(mdir, f"plan-{args.pass_}.list"), "w", encoding="utf-8") as fh:
        for ln in lines:
            fh.write(ln + "\n")

    print(f"plan {args.pass_}: {len(todo)} record(s) pending, "
          f"{len(batches)} batch(es) of <= {args.batch}, effort={args.effort}")
    for sig in sorted(groups, key=lambda s: -len(groups[s])):
        print(f"  {len(groups[sig]):5d}  {', '.join(sig) or '(none)'}")
    return 0


# --------------------------------------------------------------------------
# apply — validate every field, then write back
# --------------------------------------------------------------------------

_SENT = re.compile(r"(?<=[.!?])\s+(?=[\"'“„(]?[A-Z0-9ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ])")


def sentences(s):
    return [p for p in _SENT.split(collapse(s)) if p]


def validate_a(item, fields):
    """-> (writes, errors). A field that does not validate is never written."""
    w, e = {}, []
    for f in fields:
        if f == "sector":
            v = item.get("sector")
            if v in SECTORS:
                w["sector"] = v
            else:
                e.append(f"sector={v!r} not in the closed list")
        elif f == "geo_origin":
            v = item.get("geo_origin")
            if isinstance(v, str) and GEO_RE.match(v):
                w["geo_origin"] = v
            else:
                e.append(f"geo_origin={v!r} not ISO2/EU")
        elif f in ("pain", "stated_need"):
            v = item.get(f)
            if isinstance(v, bool):
                w[f] = v
            else:
                e.append(f"{f}={v!r} not a boolean")
        else:
            key = f.split(".", 1)[1]
            v = item.get(key)
            if isinstance(v, bool) or not isinstance(v, int):
                e.append(f"{f}={v!r} not an integer")
            elif not 0 <= v <= 3:
                e.append(f"{f}={v} out of range 0-3")
            else:
                w[f] = v
    return w, e


def validate_b(item, _fields):
    w, e = {}, []
    t = collapse(item.get("title") or "")
    if not t:
        e.append("title empty")
    else:
        if " — " not in t:
            t = re.sub(r"\s+[-–]\s+", " — ", t, count=1)
        if " — " not in t:
            e.append(f"title has no ' — ' separator: {t[:60]!r}")
        elif len(t) > 140:
            e.append(f"title {len(t)} chars > 140")
        else:
            w["title"] = t.rstrip(" .")
    s = collapse(item.get("summary") or "")
    if not s:
        e.append("summary empty")
    elif len(sentences(s)) > 2:
        e.append(f"summary is {len(sentences(s))} sentences, max 2")
    elif len(s) > 600:
        e.append(f"summary {len(s)} chars > 600")
    else:
        w["summary"] = s
    return w, e


def response_items(path):
    """The response `content` array LEADS WITH A THINKING BLOCK on this model —
    content[0]["text"] raises KeyError. Select the block whose type is text."""
    with open(path, "r", encoding="utf-8") as fh:
        body = json.load(fh)
    if body.get("type") == "error" or "content" not in body:
        raise ValueError(f"API error: {json.dumps(body)[:300]}")
    if body.get("stop_reason") == "max_tokens":
        raise ValueError("truncated: stop_reason=max_tokens")
    if body.get("stop_reason") == "refusal":
        raise ValueError(f"refusal: {json.dumps(body.get('stop_details'))[:200]}")
    texts = [b.get("text", "") for b in body["content"] if b.get("type") == "text"]
    if not texts:
        raise ValueError(f"no text block; types={[b.get('type') for b in body['content']]}")
    data = json.loads("".join(texts))
    if not isinstance(data.get("results"), list):
        raise ValueError("no results array")
    return data["results"], body.get("usage") or {}


def cmd_apply(args):
    raw = os.path.abspath(args.raw)
    mdir = model_dir(raw)
    with open(os.path.join(mdir, f"plan-{args.pass_}.json"), "r", encoding="utf-8") as fh:
        plan = json.load(fh)
    recs = read_staged(raw)
    by_id = {r["id"]: r for r in recs}

    report = {"pass": args.pass_, "batches": [], "filled": 0, "pain_refused": [],
              "rejected": [], "missing_response": [], "unanswered": [],
              "usage": {"input_tokens": 0, "output_tokens": 0, "thinking_tokens": 0}}
    validate = validate_a if args.pass_ == "A" else validate_b

    for b in plan["batches"]:
        resp = os.path.join(mdir, "resp", b["name"] + ".json")
        if not os.path.isfile(resp):
            report["missing_response"].append(b["name"])
            continue
        try:
            items, usage = response_items(resp)
        except Exception as exc:                       # noqa: BLE001
            report["batches"].append({"name": b["name"], "error": str(exc)})
            report["missing_response"].append(b["name"])
            continue
        report["usage"]["input_tokens"] += usage.get("input_tokens", 0)
        report["usage"]["output_tokens"] += usage.get("output_tokens", 0)
        report["usage"]["thinking_tokens"] += (
            usage.get("output_tokens_details") or {}).get("thinking_tokens", 0)

        wanted = set(b["ids"])
        answered, filled = set(), 0
        for item in items:
            sid = item.get("id")
            if sid not in wanted:
                report["rejected"].append([b["name"], sid, "id not in this batch"])
                continue
            if sid in answered:
                report["rejected"].append([b["name"], sid, "duplicate answer"])
                continue
            answered.add(sid)
            rec = by_id[sid]
            fields = pending(rec, args.pass_)
            writes, errs = validate(item, fields)
            if errs:
                report["rejected"].append([b["name"], sid, "; ".join(errs)])
                rec["_model_attempts"] = rec.get("_model_attempts", 0) + 1
                if rec["_model_attempts"] >= 2:
                    # Retried once, still malformed. INGEST.md 3b: retry a
                    # malformed batch ONCE, then skip it and record the error.
                    rec["_model_refused"] = "validation failed twice"
                continue
            # THE PAIN BAR IS AN ADMISSION BAR, NOT A FIELD (CONVENTIONS: it is
            # never persisted). A false verdict means the record is not admitted
            # at all, so NOTHING is written to it: it keeps its `_needs`, stays
            # staged, and --complete lists it as incomplete. Filling its other
            # fields and dropping `pain` from `_needs` would have let it through,
            # because `pain` is not in REQUIRED_OUT.
            if writes.pop("pain", None) is False:
                rec["_model_refused"] = "pain bar: no complaint/failure/workaround"
                report["pain_refused"].append(sid)
                continue
            # THE STATED-NEED BAR is the asks feeds' admission bar — a sibling
            # of `pain`, not a reuse of it. Measured 2026-09-03: graded under the
            # pain sentence ("a COMPLAINT, a FAILURE or a WORKAROUND"), 29 of 39
            # owner-set asks were refused, inconsistently — an ask is by nature
            # "something is missing", and a hospital asking for a tool is not a
            # complaint. One word carrying two admission tests is the defect
            # CLAUDE.md rule 1 names, so the bar got its own name and sentence.
            if writes.pop("stated_need", None) is False:
                rec["_model_refused"] = "stated-need bar: a theme, an invitation or a pitch, not a stated need"
                report["pain_refused"].append(sid)
                continue
            for k, v in writes.items():
                if k.startswith("scores."):
                    rec.setdefault("scores", {})[k.split(".", 1)[1]] = v
                else:
                    rec[k] = v
            # A model produced this record's judgement fields, so the ledger says
            # so: `structured` is reserved for a record a PARSER produced end to
            # end. See the note in the run report — no feed contract was
            # violated here; this value is the review flag, not a fault claim.
            rec["extraction"] = "llm-fallback"
            rec["_needs"] = [f for f in (rec.get("_needs") or [])
                             if f not in writes and f not in ("pain", "stated_need")]
            filled += 1
        for sid in sorted(wanted - answered):
            report["unanswered"].append([b["name"], sid])
        report["filled"] += filled
        report["batches"].append({"name": b["name"], "asked": len(b["ids"]),
                                  "filled": filled})

    if not args.dry_run:
        write_staged(raw, recs)
    with open(os.path.join(mdir, f"report-{args.pass_}.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)

    u = report["usage"]
    print(f"apply {args.pass_}: filled {report['filled']} record(s); "
          f"{len(report['rejected'])} field-set(s) rejected; "
          f"{len(report['pain_refused'])} refused by the pain bar; "
          f"{len(report['unanswered'])} unanswered; "
          f"{len(report['missing_response'])} batch(es) without a usable response")
    print(f"  tokens: in={u['input_tokens']} out={u['output_tokens']} "
          f"(thinking {u['thinking_tokens']})")
    for r in report["rejected"][:8]:
        print(f"  REJECTED {r[1]}: {r[2]}")
    return 0


def cmd_status(args):
    raw = os.path.abspath(args.raw)
    recs = read_staged(raw)
    import collections
    need = collections.Counter()
    refused = collections.Counter()
    material = complete = 0
    for r in recs:
        for f in r.get("_needs") or []:
            need[f] += 1
        if r.get("_model_refused"):
            refused[r["_model_refused"][:40]] += 1
        if not (r.get("_needs") or []):
            complete += 1
        sc = r.get("scores") or {}
        if all(isinstance(sc.get(k), int) for k in ("scale", "money", "urgency", "recurrence")) \
                and is_material(sc, r.get("evidence_type")):
            material += 1
    print(f"staged: {len(recs)}   fully filled: {complete}   material survivors: {material}")
    for f, n in need.most_common():
        print(f"  still needs {f}: {n}")
    for k, n in refused.most_common():
        print(f"  refused ({k}): {n}")
    return 0


def main():
    p = argparse.ArgumentParser(prog="model_pass.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("plan", cmd_plan), ("apply", cmd_apply), ("status", cmd_status)):
        s = sub.add_parser(name)
        s.add_argument("--raw", required=True)
        s.set_defaults(fn=fn)
        if name != "status":
            s.add_argument("--pass", dest="pass_", choices=["A", "B"], required=True)
        if name == "plan":
            s.add_argument("--batch", type=int, default=40)
            s.add_argument("--effort", default="medium",
                           choices=["low", "medium", "high", "xhigh", "max"])
            s.add_argument("--proof", action="store_true",
                           help="one batch per field-signature — the small run you inspect first")
        if name == "apply":
            s.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
