"""Turn the subagents' JSON answers into results/accuracy/sub-<model>.jsonl, through the same post-filters."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.argv = sys.argv[:1]
from run_accuracy import finish  # noqa: E402

items = {json.loads(l)["id"]: json.loads(l) for l in open(HERE / "sets/accuracy.jsonl")}
stats = json.load(open(HERE / "subagent/stats.json"))
for model in ("sonnet", "haiku"):
    out = open(HERE / f"results/accuracy/sub-{model}.jsonl", "w")
    for k in (1, 2):
        ids = (HERE / f"subagent/batch{k}.ids").read_text().split(",")
        ans = json.load(open(HERE / f"subagent/out-{model}-{k}.json"))
        st = stats[f"{model}-{k}"]
        for eid in ids:
            rec = {"id": eid, "label": f"sub-{model}", "backend": "subagent", "model": model, "batch": len(ids),
                   "wall_s": st["seconds"] / len(ids), "usage": {"subagent_tokens": st["tokens"] / len(ids)}}
            raw = next((v for kk, v in ans.items() if kk[:5] == eid), None)
            if not isinstance(raw, list):
                rec["error"] = "missing"
            else:
                rec["raw"] = raw
                rec["issues"], rec["dropped"] = finish(items[eid]["entry"], raw)
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    out.close()
    rs = [json.loads(l) for l in open(HERE / f"results/accuracy/sub-{model}.jsonl")]
    print(model, len(rs), sum(1 for r in rs if 'error' in r), sum(len(r.get('raw') or []) for r in rs), sum(len(r.get('issues') or []) for r in rs))
