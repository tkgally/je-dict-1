"""Run headless Claude over the 10 October labeled sets (enhancement/decision-models-2026-10-10/sets),
with that study's own batched LLM prompt (20 items a call), and score it the same way, so the
numbers sit beside the OpenRouter LLM baselines in that study's summary.json.

python3 run_sets.py <haiku|sonnet|opus> furigana,links,flags,conjugation,translation,transitivity,sense [--workers 3] [--effort low]
python3 run_sets.py --score
Results: results/sets/<label>/<task>.jsonl."""
import argparse
import json
import statistics
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
DM = HERE.parent / "decision-models-2026-10-10"
sys.path.insert(0, str(DM))
sys.path.insert(0, str(HERE))
import os  # noqa: E402
os.environ.setdefault("OPENROUTER_API_KEY", "unused")
import run as dm_run  # noqa: E402
import score as dm_score  # noqa: E402
from claude_backend import call_claude  # noqa: E402

TASKS = ["furigana", "links", "flags", "conjugation", "translation", "transitivity", "sense"]
lock = threading.Lock()


def run(model, task, bs, workers, effort, label):
    items = dm_run.load(task)
    out = HERE / "results/sets" / label / f"{task}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    have = dm_run.done_ids(out)
    if out.exists():
        out.write_text("".join(l for l in open(out) if '"error"' not in l))
    todo = [it for it in items if it["id"] not in have]
    groups = {}
    for it in todo:
        groups.setdefault(it.get("task_kind"), []).append(it)
    batches = [g[i:i + bs] for g in groups.values() for i in range(0, len(g), bs)]

    def one(batch):
        resp = call_claude(dm_run.llm_prompt(batch), model=model, effort=effort)
        err, arr = None, {}
        try:
            arr = {int(a["n"]): a for a in dm_run.parse_arr(resp["choices"][0]["message"]["content"])}
        except Exception as ex:  # noqa: BLE001
            err = f"{ex}: {str(resp)[:300]}"
        u = (resp or {}).get("usage") or {}
        tin = (u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
               + u.get("cache_read_input_tokens", 0))
        recs = []
        for n, it in enumerate(batch, 1):
            rec = {"id": it["id"], "label": it["label"], "sub": it.get("sub"), "kind": it.get("task_kind"),
                   "latency": (resp or {}).get("wall_s"), "batch_latency": (resp or {}).get("wall_s"),
                   "batch_size": len(batch)}
            if arr.get(n):
                rec["answer"] = arr[n]
                rec["usage"] = {"cost": (u.get("list_cost_usd") or 0) / len(batch),
                                "input_tokens": tin / len(batch),
                                "output_tokens": u.get("output_tokens", 0) / len(batch)}
            else:
                rec["error"] = err or "missing item"
            recs.append(rec)
        with lock:
            with open(out, "a") as f:
                for r in recs:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
        return recs

    t0 = time.time()
    with ThreadPoolExecutor(workers) as ex:
        res = [r for rs in ex.map(one, batches) for r in rs]
    errs = [r for r in res if "error" in r]
    print(f"{label} {task}: {len(res)} items in {time.time() - t0:.0f}s, {len(errs)} errors")


def load(label, task):
    p = HERE / "results/sets" / label / f"{task}.jsonl"
    drop = set(dm_score.DROP.get(task, []))
    d = {}
    if p.exists():
        for l in open(p):
            r = json.loads(l)
            if r["id"] not in drop:
                d[r["id"]] = r
    return list(d.values())


def score():
    base = json.load(open(DM / "summary.json"))
    labels = sorted(p.name for p in (HERE / "results/sets").iterdir())
    out = {}
    for t in TASKS:
        print(f"\n{t}")
        for m in base["models"]["llm"]:
            s = base["tasks"][t].get(m)
            if s:
                print(f"  {'OR ' + m:34s} acc={s['acc']:.3f} by_sub={ {k: round(v, 2) for k, v in s['by_sub'].items()} } "
                      f"$/1k={s['cost_per_1k']:.3f}")
        for lab in labels:
            rs = load(lab, t)
            if not rs:
                continue
            s = dm_score.summary(rs)
            by = {}
            for r in rs:
                by.setdefault(r["sub"].split(":")[0] if r.get("sub") else "-", []).append(r)
            s["by_sub"] = {k: dm_score.summary(v)["acc"] for k, v in by.items()}
            toks = [((r.get("usage") or {}).get("input_tokens", 0) + (r.get("usage") or {}).get("output_tokens", 0))
                    for r in rs]
            s["tokens_per_item"] = statistics.mean(toks) if toks else None
            s["list_cost_per_1k"] = s["cost"] / len(rs) * 1000 if rs else None
            bl = [r["batch_latency"] for r in rs if r.get("batch_latency")]
            s["batch_lat_med"] = statistics.median(bl) if bl else None
            out.setdefault(t, {})[lab] = s
            print(f"  {'CC ' + lab:34s} acc={s['acc']:.3f} by_sub={ {k: round(v, 2) for k, v in s['by_sub'].items()} } "
                  f"list$/1k={s['list_cost_per_1k']:.3f} tok/item={s['tokens_per_item']:.0f} "
                  f"batch_s={s['batch_lat_med']:.0f}")
    json.dump(out, open(HERE / "sets_summary.json", "w"), indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("model", nargs="?")
    ap.add_argument("tasks", nargs="?", default=",".join(TASKS))
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--batch", type=int, default=20)
    ap.add_argument("--effort")
    ap.add_argument("--label")
    ap.add_argument("--score", action="store_true")
    a = ap.parse_args()
    if a.score:
        score()
        sys.exit(0)
    label = a.label or (a.model + (f"-{a.effort}" if a.effort else ""))
    for t in a.tasks.split(","):
        run(a.model, t, a.batch, a.workers, a.effort, label)
