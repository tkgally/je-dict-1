"""Build the accuracy-review test set: 200 entries from the two latest gpt-6.1-sol sweeps
(PRs #4031: 21514-21873 and #4037: 21874-22473), each at the version the reviewer saw
(the parent of the sweep's squash commit), with sol's surviving flags and the Routine's decisions.

All flagged entries plus a seeded random sample of unflagged ones. Writes sets/accuracy.jsonl."""
import json
import random
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
SWEEPS = [("aeab44c2", 21514, 21873, "2026-10-24T12", "2026-10-24T15"),
          ("10e78f21", 21874, 22473, "2026-10-25T00", "2026-10-25T02")]
N_TOTAL = 200


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, check=True).stdout


flags = [json.loads(l) for l in open(ROOT / "reviews/accuracy_flags.jsonl")]
decisions = [json.loads(l) for l in open(ROOT / "reviews/decisions.jsonl") if l.strip()]
items = []
for commit, lo, hi, t0, t1 in SWEEPS:
    base = f"{commit}^"
    paths = [p for p in git("ls-tree", "-r", "--name-only", base, "entries/").split()
             if p.endswith(".json") and lo <= int(Path(p).stem[:5]) <= hi]
    for p in paths:
        eid = Path(p).stem[:5]
        fl = [f for f in flags if f["entry_id"][:5] == eid and t0 <= f["reviewed_at"] <= t1]
        dec = [d for d in decisions if d.get("entry") == eid and d.get("src") == "accuracy"
               and t0 <= d["ts"] <= "2026-10-25T03"]
        items.append({"id": eid, "path": p, "commit": base, "sweep": commit,
                      "sol_flags": [i for f in fl for i in f["issues"]], "decisions": dec})

flagged = [it for it in items if it["sol_flags"]]
clean = [it for it in items if not it["sol_flags"]]
random.seed(20261025)
chosen = flagged + random.sample(clean, N_TOTAL - len(flagged))
chosen.sort(key=lambda it: it["id"])
out = HERE / "sets"
out.mkdir(exist_ok=True)
with open(out / "accuracy.jsonl", "w") as f:
    for it in chosen:
        it["entry"] = json.loads(git("show", f"{it['commit']}:{it['path']}"))
        f.write(json.dumps(it, ensure_ascii=False) + "\n")
print(f"{len(items)} entries in the sweeps, {len(flagged)} flagged by sol; wrote {len(chosen)}")
