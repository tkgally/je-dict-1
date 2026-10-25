"""Blind adjudication of every accuracy flag raised on the test set.

For each entry that any reviewer flagged, the judge sees the entry and the pooled flags,
shuffled and relabelled F1..Fn (no reviewer names), and returns for each flag a verdict
(valid = a real error a careful editor would fix; invalid) and an issue key shared by flags
that describe the same underlying problem. Code-side off-vocabulary flags are identical for
every reviewer and are left out.

python3 judge.py claude opus            # headless Claude judge (subscription)
python3 judge.py openrouter google/gemini-4-argon
Results: results/judge/<label>.jsonl."""
import argparse
import hashlib
import json
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "build"))
sys.path.insert(0, str(HERE))
import review_accuracy as ra  # noqa: E402
from review_runner import call_openrouter, get_api_key, extract_message_text, strip_code_fences  # noqa: E402
from claude_backend import call_claude  # noqa: E402

lock = threading.Lock()


def pooled_flags():
    """{entry_id: [(reviewer, flag)]} over every reviewer result on disk plus sol's historical flags."""
    items = {json.loads(l)["id"]: json.loads(l) for l in open(HERE / "sets/accuracy.jsonl")}
    pool = {eid: [] for eid in items}
    for eid, it in items.items():
        for f in it["sol_flags"]:
            if f.get("family") != "offvocab":
                pool[eid].append(("sol-hist", f))
    for p in sorted((HERE / "results/accuracy").glob("*.jsonl")):
        for l in open(p):
            r = json.loads(l)
            if r.get("raw") is None:
                continue
            # keep_warn=True: warn-severity flags are judged too (production drops them)
            kept, _ = ra.postfilter_issues(items[r["id"]]["entry"], ra.filter_issues(r["raw"], ra.DIMENSIONS),
                                           ra.DIMENSIONS, keep_warn=True)
            for f in kept:
                pool[r["id"]].append((r["label"], f))
    return items, pool


def flag_key(f):
    s = json.dumps({k: f.get(k) for k in ("dimension", "location", "concern", "suggestion", "quote")},
                   ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def judge_prompt(entry, flags):
    payload = ra.entry_payload(entry, include_notes=True)
    lines = []
    for n, f in enumerate(flags, 1):
        d = {k: f.get(k) for k in ("dimension", "location", "concern", "suggestion", "quote") if f.get(k)}
        lines.append(f"F{n}: " + json.dumps(d, ensure_ascii=False))
    return f"""You are the senior editor of a Japanese-English dictionary for intermediate learners.
Several independent reviewers checked the entry below and raised the flags listed after it.
Decide each flag on its merits.

valid   = the flag points to a REAL error that would mislead a learner and that a careful editor
          would fix: a wrong or misleading gloss, an English translation that misrepresents the
          Japanese, a semantic tag naming a domain the word does not belong to, a false factual,
          grammatical or usage claim in the notes. A restriction or absolute the language does not
          have ("only", "exclusively", "never", "always", "cannot") is a false claim, not a
          simplification; so is a false statement about another word the notes mention. A flag is
          valid if its core concern is right, even when its suggested fix is imperfect.
invalid = the entry is acceptable as it stands: a stylistic preference, a matter of emphasis or
          completeness, a claim that is simplified but not false, a house-style choice, or a
          concern that is itself mistaken.

House style (not errors): concise 3-8 word glosses; natural rather than literal translations;
politeness "plain" and formality "neutral" as defaults; kinship terms tagged "humble"; the semantic
tag "action" on suru-verbs and action nouns; notes that are selective rather than exhaustive.

Also group the flags: give flags that describe the same underlying problem in the entry the same
issue letter (A, B, C ...), and different problems different letters.

Entry (JSON):
{json.dumps(payload, ensure_ascii=False, indent=2)}

Flags:
{chr(10).join(lines)}

Respond with ONLY a JSON object, no prose and no code fences:
{{"flags": [{{"f": "F1", "verdict": "valid|invalid", "issue": "A", "why": "<ten words or fewer>"}}, ...],
 "issues": {{"A": "<the problem, ten words or fewer>", ...}}}}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("backend", choices=["openrouter", "claude"])
    ap.add_argument("model")
    ap.add_argument("--effort")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--label")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    label = a.label or a.model.split("/")[-1] + (f"-{a.effort}" if a.effort else "")
    items, pool = pooled_flags()
    out = HERE / "results/judge" / f"{label}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out.exists():
        done = {json.loads(l)["id"] for l in open(out) if '"error"' not in l}
        out.write_text("".join(l for l in open(out) if '"error"' not in l))
    jobs = []
    for eid, fl in pool.items():
        if not fl or eid in done:
            continue
        uniq = {}
        for rev, f in fl:
            uniq.setdefault(flag_key(f), (f, []))[1].append(rev)
        keys = sorted(uniq)
        random.Random(eid).shuffle(keys)
        jobs.append((eid, keys, uniq))
    print(f"{len(jobs)} entries to judge, {sum(len(j[1]) for j in jobs)} distinct flags")
    if a.dry_run:
        eid, keys, uniq = jobs[0]
        print(judge_prompt(items[eid]["entry"], [uniq[k][0] for k in keys]))
        return
    key = get_api_key() if a.backend == "openrouter" else None

    def one(job):
        eid, keys, uniq = job
        prompt = judge_prompt(items[eid]["entry"], [uniq[k][0] for k in keys])
        if a.backend == "openrouter":
            resp = call_openrouter(key, a.model, prompt, timeout=300, max_tokens=16000)
            txt = extract_message_text(resp)
            usage = (resp or {}).get("usage")
        else:
            resp = call_claude(prompt, model=a.model, effort=a.effort)
            txt = (resp or {}).get("choices", [{}])[0].get("message", {}).get("content") if resp and "choices" in resp else None
            usage = (resp or {}).get("usage")
        rec = {"id": eid, "judge": label, "usage": usage}
        try:
            t = strip_code_fences(txt.strip())
            obj = json.loads(t[t.find("{"): t.rfind("}") + 1])
            verdicts = {d["f"]: d for d in obj["flags"]}
            rec["flags"] = []
            for n, k in enumerate(keys, 1):
                v = verdicts.get(f"F{n}") or {}
                rec["flags"].append({"key": k, "reviewers": uniq[k][1], "flag": uniq[k][0],
                                     "verdict": v.get("verdict"), "issue": v.get("issue"), "why": v.get("why")})
            rec["issues"] = obj.get("issues")
        except Exception as ex:  # noqa: BLE001
            rec["error"] = f"{ex}: {str(txt)[:300]}"
        with lock:
            with open(out, "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return rec

    with ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(one, jobs))
    print(f"{label}: {len(res)} judged, {sum(1 for r in res if 'error' in r)} errors")


if __name__ == "__main__":
    main()
