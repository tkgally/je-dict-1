"""Run one accuracy reviewer over sets/accuracy.jsonl with review_accuracy.py's own prompt (v4)
and post-filters, so only the model (and the transport) differs.

python3 run_accuracy.py openrouter openai/gpt-6.1-sol [--workers 4]
python3 run_accuracy.py claude sonnet [--effort low] [--workers 6] [--batch 10]
Results: results/accuracy/<label>.jsonl, one line per entry (reruns skip done entries)."""
import argparse
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "build"))
sys.path.insert(0, str(HERE))
import review_accuracy as ra  # noqa: E402
from review_runner import call_openrouter, parse_model_response, get_api_key, strip_code_fences  # noqa: E402
from claude_backend import call_claude  # noqa: E402

DIMS = ra.DIMENSIONS
lock = threading.Lock()
TUNED = False

# --tuned: the error classes the Routine's adjudication has accepted from gpt-6.1-sol since 2026-10-23,
# stated outright (Claude reads v4's "do NOT report claims that are merely simplified" as covering them).
TUNED_TEXT = """What counts as WRONG (report these; they are not simplifications):
- an absolute or restriction the language does not have: "only", "exclusively", "always", "never",
  "almost exclusively", "cannot", "is not used in X" when the word is in fact used more widely;
- a claim about ANOTHER word (a synonym, contrast or confusable word named in the notes) that is false,
  including a wrong reading, a wrong meaning or a wrong register for that word;
- a gloss that reverses who does what (give vs take, lend vs borrow, administer vs take) or names a
  different, neighbouring concept (conflict of interest vs. stake in something);
- an English translation that adds, drops or shifts meaning (time, agent, negation, desire, degree);
- a wrong etymology, origin language, kanji explanation or cultural fact.
Do not report style, missing information or emphasis.

"""


def build(entry):
    p = ra.build_prompt(entry, DIMS)
    if TUNED:
        p = p.replace("Project conventions", TUNED_TEXT + "Project conventions", 1)
    return p


def batch_prompt(entries):
    """review_accuracy's prompt with N entries in place of one, answered as {id: [issues]}."""
    one = build(entries[0])
    head = one.split("Entry (JSON):\n")[0]
    head = head.replace("reviewing one \\\nentry", "reviewing entries").replace(
        "reviewing one entry", "reviewing several entries")
    body = "\n\n".join(f"Entry {e['id']} (JSON):\n" + json.dumps(
        ra.entry_payload(e, include_notes=True), ensure_ascii=False, indent=2) for e in entries)
    tail = ("\n\nReview each entry independently. Respond with ONLY a JSON object (no prose, no "
            "code fences) whose keys are the entry ids and whose values are that entry's array of "
            "issue objects. Each object:\n"
            '{"dimension": "gloss|translation|tags|notes", "location": "<gloss | definitions[n].gloss '
            '| examples[i] | tags.semantic | tags.formality | tags.politeness | notes>", "severity": '
            '"error|warn", "concern": "<what is wrong, briefly>", "suggestion": "<concrete fix>", '
            '"quote": "<verbatim sentence from the entry, required for tags.formality, '
            'tags.politeness, and notes>"}\n'
            "An entry that is accurate on the checked dimensions gets []. Include every entry id.")
    return head + "Entries:\n\n" + body + tail


def finish(entry, raw):
    issues, dropped = ra.postfilter_issues(entry, ra.filter_issues(raw, DIMS), DIMS)
    return ra.offvocab_issues(entry) + issues, dropped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("backend", choices=["openrouter", "claude"])
    ap.add_argument("model")
    ap.add_argument("--effort")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--label")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--ids", help="comma-separated subset")
    ap.add_argument("--tuned", action="store_true")
    a = ap.parse_args()
    global TUNED
    TUNED = a.tuned
    label = a.label or (a.model.split("/")[-1] + (f"-{a.effort}" if a.effort else "")
                        + (f"-b{a.batch}" if a.batch > 1 else "") + ("-tuned" if a.tuned else ""))
    items = [json.loads(l) for l in open(HERE / "sets/accuracy.jsonl")]
    if a.ids:
        keep = set(a.ids.split(","))
        items = [it for it in items if it["id"] in keep]
    if a.limit:
        items = items[:a.limit]
    out = HERE / "results/accuracy" / f"{label}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out.exists():
        done = {json.loads(l)["id"] for l in open(out) if '"error"' not in l}
        out.write_text("".join(l for l in open(out) if '"error"' not in l))
    todo = [it for it in items if it["id"] not in done]
    key = get_api_key() if a.backend == "openrouter" else None

    def call(prompt):
        t0 = time.time()
        if a.backend == "openrouter":
            resp = call_openrouter(key, a.model, prompt, timeout=180)
            meta = {"wall_s": time.time() - t0,
                    "usage": (resp or {}).get("usage"),
                    "est_usd": ra.estimate_cost(a.model, ra.rough_token_count(prompt), 400)}
        else:
            resp = call_claude(prompt, model=a.model, effort=a.effort)
            meta = {"wall_s": (resp or {}).get("wall_s", time.time() - t0),
                    "usage": (resp or {}).get("usage"), "error": (resp or {}).get("error")}
        return resp, meta

    def write(recs):
        with lock:
            with open(out, "a") as f:
                for r in recs:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")

    def one(group):
        entries = [it["entry"] for it in group]
        if len(group) == 1:
            resp, meta = call(build(entries[0]))
            raws = [parse_model_response(resp) if resp and "choices" in resp else None]
        else:
            resp, meta = call(batch_prompt(entries))
            raws = [None] * len(group)
            try:
                txt = strip_code_fences(resp["choices"][0]["message"]["content"].strip())
                obj = json.loads(txt[txt.find("{"): txt.rfind("}") + 1])
                raws = [obj.get(e["id"]) if isinstance(obj.get(e["id"]), list) else None
                        for e in entries]
            except Exception as ex:  # noqa: BLE001
                meta["error"] = meta.get("error") or f"parse: {ex}"
        recs = []
        for it, raw in zip(group, raws):
            rec = {"id": it["id"], "label": label, "backend": a.backend, "model": a.model,
                   "batch": len(group), **{k: v for k, v in meta.items()}}
            if raw is None:
                rec["error"] = rec.get("error") or "no parse"
            else:
                rec["raw"] = raw
                rec["issues"], rec["dropped"] = finish(it["entry"], raw)
            recs.append(rec)
        write(recs)
        return recs

    groups = [todo[i:i + a.batch] for i in range(0, len(todo), a.batch)]
    t0 = time.time()
    with ThreadPoolExecutor(a.workers) as ex:
        res = [r for rs in ex.map(one, groups) for r in rs]
    errs = [r for r in res if r.get("error") or "issues" not in r]
    print(f"{label}: {len(res)} entries in {time.time() - t0:.0f}s, {len(errs)} errors, "
          f"{sum(1 for r in res if r.get('issues'))} flagged, "
          f"{sum(len(r.get('issues') or []) for r in res)} issues")


if __name__ == "__main__":
    main()
