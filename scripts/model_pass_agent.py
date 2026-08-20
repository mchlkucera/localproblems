#!/usr/bin/env python3
"""
scripts/model_pass_agent.py — the SUBAGENT HALF of the model seam.

WHY THIS FILE EXISTS.

model_pass.sh spends the owner's Anthropic API CREDIT BALANCE. On 2026-08-20 that
balance ran out mid-run (HTTP 400, "Your credit balance is too low"), stranding 51
material survivors with their `_needs` intact. The owner's ruling:

    "instead of running Claude thru api credits, can you run the logic thru
     subagents?"

Subagents run on the session, not on that balance. So the MIDDLE of the seam gets a
second implementation. Nothing else changes:

    model_pass.py plan       (python)  staged.jsonl        -> .model/req/*.json
    ------------------------ pick ONE driver -------------------------------
    model_pass_agent.py      (python)  .model/req/*.json   -> .model/agent/*.prompt.md
      + a session's subagents           *.prompt.md        -> .model/agent/*.answer.json
      + model_pass_agent.py collect     *.answer.json      -> .model/resp/*.json
    model_pass.sh            (bash)    .model/req/*.json   -> .model/resp/*.json   [API]
    ------------------------------------------------------------------------
    model_pass.py apply      (python)  .model/resp/*.json  -> staged.jsonl

model_pass.py IS NOT MODIFIED BY THIS FILE'S EXISTENCE, and that is the whole point.
`plan`'s batch naming (a sha1 of the batch's own member ids) and `apply`'s validator
(closed vocabularies, atomic temp+os.replace write-back) are the proven halves. A
second driver that needed either of them loosened would be a second QA standard.
`collect` therefore adapts TRANSPORT ONLY: it wraps the agent's natural answer
    {"results": [...]}
in the /v1/messages envelope `apply` already parses
    {"content": [{"type": "text", "text": "<that JSON, as a string>"}], ...}
and never inspects, repairs or defaults a single field inside it. Every judgement in
the answer still faces `validate_a`/`validate_b` untouched.

WHY THE AGENT DOES NOT WRITE THE ENVELOPE ITSELF. It would have to hand-escape a
whole JSON document as a JSON string — em dashes, quotes, diacritics and all — which
is a transcription task with a real error rate and no upside. It writes one flat,
natural object; this file does the escaping with json.dumps, which cannot get it
wrong. "The shape apply expects" is preserved exactly; only who types it changed.

WHY A SCRIPT CANNOT SPAWN THE SUBAGENTS. It was measured, twice, on 2026-08-20:

    $ echo '...' | claude -p --model claude-opus-5
    Not logged in · Please run /login            # sandboxed: Keychain read denied
    Failed to authenticate. API Error: 401 OAuth access token has expired.
                                                 # unsandboxed: the token is stale

So a nested `claude -p` is NOT a driver on this box, and no shell script can become
one. The subagents are spawned by the SESSION running the pipeline — this is exactly
the ATTENDED mode pipeline/INGEST.md already describes, except the batching, the
schema and the validator now exist, so an agent never edits staged.jsonl by hand.
`worklist` is the handoff to that session and `collect` is the handoff back.

RESUMABLE, AND THE RULE IS UNCHANGED: a batch is DONE when its response file exists.
`worklist` skips those, so a crashed or abandoned agent costs only its own batch. An
answer that does not parse is REFUSED, not repaired — the batch simply stays pending
and the next `worklist` re-issues it. staged.jsonl is never touched here at all.
"""

import argparse
import json
import os
import re
import sys

MAX_ANSWER_BYTES = 4_000_000       # a batch answer is kilobytes; this is a tripwire

# --------------------------------------------------------------------------
# AGENT_BATCH — 50, and it was MEASURED, not guessed.
#
# The old batch sizes (50 for pass A, 25 for pass B) were tuned for an HTTP
# request, where the only real limits are max_tokens and the rate limiter. A
# subagent has a different failure curve: it re-reads a prompt, holds the whole
# batch in one context, and has to land the answer in ONE Write.
#
# THE EXPERIMENT (2026-08-20). 374 already-filled, already-material records were
# copied out of data/raw/2026-08-20/staged.jsonl into four throwaway corpora, had
# their title+summary stripped back into `_needs`, and were re-judged by pass B —
# the harder pass, two prose fields per record under hard length rules. Records
# were STRIDE-sampled across the id-sorted pool, so each corpus carries the real
# feed mix (yc-dominated, with ted/suggest/feed) rather than one alphabetical
# slice. Two independent subagents per size, eight in total, no retries:
#
#   size  records  validator   agents    tool calls   tokens    wall
#                  rejects     /100 rec  /batch       /record   /record
#     12       24         0        8.3         2.0     4.66k     6.71s
#     25       50         0        4.0         2.0     2.72k     5.36s
#     50      100         0        2.0         2.0     1.65k     3.21s
#    100      200         1        1.0         4.0     1.30k     3.77s
#
#   (rejects are `model_pass.py validate_b` verdicts; dup/alien/unanswered ids
#    were 0 everywhere, and every batch came back in input order at every size.)
#
# WHY 50 AND NOT 100. Cost per record falls 2.8x from 12 to 50 and then flattens:
# going on to 100 saves a further 21% of tokens and buys three problems for it.
#   1. It is where correctness first cracks. 1 record in 200 returned a
#      three-sentence summary; at <=50 it was 0 in 174. `apply` catches it and the
#      record keeps its `_needs`, so this is waste, not corruption — but it is
#      waste that grows with the corpus.
#   2. The tool-call count DOUBLES, from 2 to 4. At 100 items the answer no longer
#      fits one Write and the agent assembles it in pieces, which is both slower
#      per record (3.77s vs 3.21s) and strictly more ways to leave a half-written
#      answer file on disk.
#   3. Blast radius. A batch is the unit of loss when an agent is abandoned, so
#      100 doubles what a crash costs to redo.
# 50 keeps single-Write atomicity, zero measured rejects, the best wall time per
# record, and 2 agents per 100 records.
#
# WHAT THIS DOES NOT COVER, stated rather than implied: only pass B was measured.
# Pass A returns six short enum/int fields per record instead of two prose ones,
# so its output burden per record is far lower and it can very likely carry a
# larger batch — but that was not measured, so both passes ship at 50 and A is
# simply running below its ceiling.
AGENT_BATCH = 50


# --------------------------------------------------------------------------
# paths
# --------------------------------------------------------------------------

def model_dir(raw):
    return os.path.join(raw, ".model")


def agent_dir(raw):
    return os.path.join(model_dir(raw), "agent")


def read_plan(raw, pass_):
    path = os.path.join(model_dir(raw), f"plan-{pass_}.json")
    if not os.path.isfile(path):
        sys.stderr.write(f"model_pass_agent: no {path} — run 'model_pass.py plan' first\n")
        sys.exit(2)
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def resp_path(raw, name):
    return os.path.join(model_dir(raw), "resp", name + ".json")


def prompt_path(raw, name):
    return os.path.join(agent_dir(raw), name + ".prompt.md")


def answer_path(raw, name):
    return os.path.join(agent_dir(raw), name + ".answer.json")


# --------------------------------------------------------------------------
# worklist — turn pending request files into subagent prompts
# --------------------------------------------------------------------------

def describe_schema(schema):
    """Render the request's OWN json_schema as prose keys. Read from the request
    file, never restated here: a hand-copied field list is a second source of
    truth that drifts the first time `plan` changes."""
    props = (((schema or {}).get("properties") or {}).get("results") or {}) \
        .get("items", {}).get("properties", {})
    lines = []
    for key in sorted(props):
        spec = props[key]
        t = spec.get("type", "?")
        if spec.get("enum") is not None:
            enum = spec["enum"]
            if all(isinstance(x, int) for x in enum):
                lines.append(f'  "{key}": {t} — one of {enum}')
            else:
                lines.append(f'  "{key}": {t} — EXACTLY one of: {", ".join(map(str, enum))}')
        else:
            lines.append(f'  "{key}": {t}')
    return "\n".join(lines)


PROMPT = """\
# Batch `{name}` — {n} item(s), pass {pass_}

You are one worker in a batch job. Do the judgement below and write ONE file.
Do not read other files, do not search the web, do not run commands, do not edit
anything else. Everything you are allowed to use is in this prompt.

## The standard you apply

{system}

## Your output contract

Write a single JSON file to EXACTLY this path (use the Write tool):

    {answer}

Its content must be a JSON object of exactly this form, and nothing else — no
markdown fences, no commentary before or after:

    {{"results": [ {{...}}, {{...}}, ... ]}}

Every object in `results` must have EXACTLY these keys and no others:

{schema}

HARD REQUIREMENTS — these are checked mechanically and a failure costs the whole
batch a re-run:
- EXACTLY {n} objects in `results`, one per input item, in the input's order.
- Each `id` copied VERBATIM from its input item. Never invent, reorder-and-guess,
  merge or drop an id. If an item is hard to judge, still answer it: choose the
  most defensible value under the standard above.
- No extra keys, no `null`, no empty strings, no placeholders like "unknown".
- Judge ONLY from the item's own card. Never invent a fact, a number, a date or a
  name that is not on the card.

## The {n} items

```json
{items}
```

Write the file. Then reply with one line only: `{name}: <count> results written`.
"""


def cmd_worklist(args):
    raw = os.path.abspath(args.raw)
    plan = read_plan(raw, args.pass_)
    adir = agent_dir(raw)
    os.makedirs(adir, exist_ok=True)
    os.makedirs(os.path.join(model_dir(raw), "resp"), exist_ok=True)

    pending, done = [], 0
    for b in plan["batches"]:
        name = b["name"]
        # THE RESUMABILITY RULE, unchanged from model_pass.sh: a batch is done when
        # its response file exists. Not when an answer exists, not when an agent
        # said so — when the artifact `apply` will read is on disk.
        if os.path.isfile(resp_path(raw, name)) and os.path.getsize(resp_path(raw, name)) > 0:
            done += 1
            continue
        if args.limit and len(pending) >= args.limit:
            continue

        with open(b["req"], "r", encoding="utf-8") as fh:
            req = json.load(fh)
        items = json.loads(req["messages"][0]["content"])["items"]
        schema = (req.get("output_config") or {}).get("format", {}).get("schema")
        body = PROMPT.format(
            name=name, n=len(items), pass_=args.pass_,
            system=req["system"].strip(),
            answer=answer_path(raw, name),
            schema=describe_schema(schema),
            items=json.dumps(items, ensure_ascii=False, indent=1),
        )
        with open(prompt_path(raw, name), "w", encoding="utf-8") as fh:
            fh.write(body)
        pending.append({"name": name, "n": len(items),
                        "prompt": prompt_path(raw, name),
                        "answer": answer_path(raw, name)})

    wl = {"pass": args.pass_, "raw": raw, "done": done, "pending": pending}
    with open(os.path.join(adir, f"worklist-{args.pass_}.json"), "w", encoding="utf-8") as fh:
        json.dump(wl, fh, ensure_ascii=False, indent=1)

    print(f"worklist {args.pass_}: {len(pending)} batch(es) awaiting a subagent, "
          f"{done} already answered")
    for p in pending:
        print(f"  {p['name']}  {p['n']:3d} item(s)  {p['prompt']}")
    if not pending:
        print("  nothing to do — every batch already has a response file")
    return 0


# --------------------------------------------------------------------------
# collect — wrap agent answers into the envelope `apply` parses
# --------------------------------------------------------------------------

_FENCE = re.compile(r"^\s*```(?:json)?\s*\n(.*?)\n\s*```\s*$", re.S)


def load_answer(path):
    """Parse an agent's answer file. TRANSPORT ONLY — this never looks at a field's
    VALUE. A stray markdown fence is stripped because that is an encoding accident,
    not a judgement; anything else that does not parse is refused outright so the
    batch stays pending and gets re-issued."""
    size = os.path.getsize(path)
    if size > MAX_ANSWER_BYTES:
        raise ValueError(f"answer is {size} bytes — refusing to parse")
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    m = _FENCE.match(text)
    if m:
        text = m.group(1)
    data = json.loads(text)
    if not isinstance(data, dict) or not isinstance(data.get("results"), list):
        raise ValueError("no top-level `results` array")
    if not data["results"]:
        raise ValueError("`results` is empty")
    return data


def cmd_collect(args):
    raw = os.path.abspath(args.raw)
    plan = read_plan(raw, args.pass_)
    rdir = os.path.join(model_dir(raw), "resp")
    os.makedirs(rdir, exist_ok=True)

    wrapped = skipped = 0
    missing, broken, short = [], [], []
    for b in plan["batches"]:
        name = b["name"]
        rp = resp_path(raw, name)
        if os.path.isfile(rp) and os.path.getsize(rp) > 0:
            skipped += 1
            continue
        ap = answer_path(raw, name)
        if not os.path.isfile(ap):
            missing.append(name)
            continue
        try:
            data = load_answer(ap)
        except Exception as exc:                       # noqa: BLE001
            broken.append([name, str(exc)[:160]])
            continue
        if len(data["results"]) != len(b["ids"]):
            # NOT fatal and NOT repaired: `apply` reports every id the batch asked
            # for and did not get as `unanswered`, and those records keep their
            # `_needs`. Recorded here so a short answer is visible at the seam it
            # happened at rather than only in the apply report.
            short.append([name, len(data["results"]), len(b["ids"])])
        envelope = {
            "id": "subagent-" + name,
            "type": "message",
            "role": "assistant",
            "model": "subagent",
            "stop_reason": "end_turn",
            # Zero on purpose, and it is a TELL, not a placeholder: report-<PASS>.json
            # prints these totals, so `tokens: in=0 out=0` is proof the API driver
            # did not run and no credit was spent. The API path fills them for real.
            "usage": {"input_tokens": 0, "output_tokens": 0},
            "_via": "subagent",
            "content": [{"type": "text",
                         "text": json.dumps(data, ensure_ascii=False)}],
        }
        tmp = os.path.join(rdir, "." + name + ".part")
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(envelope, fh, ensure_ascii=False)
        os.replace(tmp, rp)                            # atomic: never a half response
        wrapped += 1

    print(f"collect {args.pass_} [SUBAGENT PATH — no API credit spent]: "
          f"wrapped {wrapped}, already present {skipped}, "
          f"{len(missing)} awaiting an agent, {len(broken)} unparseable")
    for n, e in broken:
        print(f"  UNPARSEABLE {n}: {e}")
    for n, got, want in short:
        print(f"  SHORT {n}: {got} result(s) for {want} id(s)")
    for n in missing[:10]:
        print(f"  PENDING {n}")
    return 0


# --------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(prog="model_pass_agent.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("worklist", cmd_worklist), ("collect", cmd_collect)):
        s = sub.add_parser(name)
        s.add_argument("--raw", required=True)
        s.add_argument("--pass", dest="pass_", choices=["A", "B"], required=True)
        s.set_defaults(fn=fn)
        if name == "worklist":
            s.add_argument("--limit", type=int, default=0,
                           help="emit at most N prompts this round (0 = all pending)")
    args = p.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
