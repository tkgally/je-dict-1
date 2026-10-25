"""Score every accuracy reviewer against the blind judges' verdicts.

valid issue = an (entry, issue-group) that the judge called valid for at least one flag.
precision   = valid flags / flags;  recall = valid issues the reviewer found / all valid issues
              found by any reviewer on the same entries (pooled recall).
"prod" counts error-severity flags only (what review_accuracy.py keeps); "+warn" adds warn flags.
Writes accuracy_summary.json and prints tables."""
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "build"))
sys.path.insert(0, str(HERE))
import review_accuracy as ra  # noqa: E402
from judge import flag_key  # noqa: E402

items = {json.loads(l)["id"]: json.loads(l) for l in open(HERE / "sets/accuracy.jsonl")}
JUDGES = [p.stem for p in sorted((HERE / "results/judge").glob("*.jsonl"))]


def load_judge(j):
    verdict, issue = {}, {}
    for l in open(HERE / f"results/judge/{j}.jsonl"):
        r = json.loads(l)
        for f in r.get("flags") or []:
            verdict[(r["id"], f["key"])] = f["verdict"] == "valid"
            issue[(r["id"], f["key"])] = (r["id"], f["issue"])
    return verdict, issue


def reviewer_flags():
    """{label: {"ids": set, "prod": [(id,key)], "warn": [(id,key)], "meta": [...]}}"""
    out = {}
    out["sol-hist"] = {"ids": set(items), "prod": [], "warn": [], "meta": []}
    for eid, it in items.items():
        for f in it["sol_flags"]:
            if f.get("family") != "offvocab":
                out["sol-hist"]["prod"].append((eid, flag_key(f)))
    for p in sorted((HERE / "results/accuracy").glob("*.jsonl")):
        d = {"ids": set(), "prod": [], "warn": [], "meta": []}
        for l in open(p):
            r = json.loads(l)
            d["ids"].add(r["id"])
            d["meta"].append(r)
            if r.get("raw") is None:
                continue
            kept, _ = ra.postfilter_issues(items[r["id"]]["entry"], ra.filter_issues(r["raw"], ra.DIMENSIONS),
                                           ra.DIMENSIONS, keep_warn=True)
            for f in kept:
                sev = str(f.get("severity") or "error").lower()
                d["prod" if sev != "warn" else "warn"].append((r["id"], flag_key(f)))
        out[p.stem] = d
    return out


def cost_meta(d):
    m = d["meta"]
    if not m:
        return {}
    w = [r["wall_s"] for r in m if r.get("wall_s")]
    tok_in = tok_out = usd = 0.0
    for r in m:
        u = r.get("usage") or {}
        share = 1 / (r.get("batch") or 1)
        if "subagent_tokens" in u:
            tok_in += u["subagent_tokens"]
            continue
        if "prompt_tokens" in u:  # OpenRouter
            tok_in += u.get("prompt_tokens", 0)
            tok_out += u.get("completion_tokens", 0)
            usd += u.get("cost") or 0
        else:
            tok_in += share * (u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
                               + u.get("cache_read_input_tokens", 0))
            tok_out += share * u.get("output_tokens", 0)
            usd += share * (u.get("list_cost_usd") or 0)
    n = len(m)
    return {"n": n, "tok_in_per_entry": tok_in / n, "tok_out_per_entry": tok_out / n,
            "usd_per_1k": usd / n * 1000, "call_s_median": statistics.median(w) if w else None}


def main():
    revs = reviewer_flags()
    summary = {"judges": JUDGES, "reviewers": {}}
    jd = {j: load_judge(j) for j in JUDGES}
    # judge agreement
    if len(JUDGES) == 2:
        a, b = jd[JUDGES[0]][0], jd[JUDGES[1]][0]
        common = [k for k in a if k in b and a[k] is not None and b[k] is not None]
        agree = sum(1 for k in common if a[k] == b[k])
        summary["judge_agreement"] = {"n": len(common), "agree": agree,
                                      f"{JUDGES[0]}_valid": sum(a[k] for k in common),
                                      f"{JUDGES[1]}_valid": sum(b[k] for k in common)}
        print(f"judge agreement {agree}/{len(common)}; valid: {JUDGES[0]} {sum(a[k] for k in common)}, "
              f"{JUDGES[1]} {sum(b[k] for k in common)}")
    for j in JUDGES + ["both"]:
        if j == "both":
            if len(JUDGES) < 2:
                continue
            v1, i1 = jd[JUDGES[0]]
            v2, _ = jd[JUDGES[1]]
            verdict = {k: bool(v1.get(k)) and bool(v2.get(k)) for k in v1}
            issue = i1
        else:
            verdict, issue = jd[j]
        universe = {issue[k] for k, v in verdict.items() if v}
        print(f"\n== judge: {j} — {len(universe)} distinct valid issues in the pool")
        print(f"{'reviewer':18s} {'entries':>7s} | {'flags':>5s} {'valid':>5s} {'prec':>5s} {'recall':>6s} | "
              f"{'+warn flags':>11s} {'valid':>5s} {'prec':>5s} {'recall':>6s}")
        for lab, d in revs.items():
            uni = {u for u in universe if u[0] in d["ids"]}
            row = {"entries": len(d["ids"]), "pool_issues": len(uni)}
            for mode, fl in (("prod", d["prod"]), ("warn", d["prod"] + d["warn"])):
                fl = [k for k in fl if k in verdict]
                valid = [k for k in fl if verdict[k]]
                found = {issue[k] for k in valid}
                row[mode] = {"flags": len(fl), "valid": len(valid),
                             "precision": len(valid) / len(fl) if fl else None,
                             "issues": len(found), "recall": len(found) / len(uni) if uni else None,
                             "found": sorted(f"{a}:{b}" for a, b in found)}
            summary["reviewers"].setdefault(lab, {"cost": cost_meta(d)})[j] = row
            p, w = row["prod"], row["warn"]
            fmt = lambda x: f"{x:.2f}" if x is not None else "  -  "
            print(f"{lab:18s} {row['entries']:7d} | {p['flags']:5d} {p['valid']:5d} {fmt(p['precision']):>5s} "
                  f"{fmt(p['recall']):>6s} | {w['flags']:11d} {w['valid']:5d} {fmt(w['precision']):>5s} "
                  f"{fmt(w['recall']):>6s}")
    print("\ncost / tokens / time per entry")
    for lab, d in revs.items():
        c = summary["reviewers"][lab]["cost"]
        if c:
            print(f"{lab:18s} tok_in={c['tok_in_per_entry']:7.0f} tok_out={c['tok_out_per_entry']:6.0f} "
                  f"$/1k(list)={c['usd_per_1k']:6.2f} call_s={c['call_s_median'] or 0:5.1f}")
    json.dump(summary, open(HERE / "accuracy_summary.json", "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
