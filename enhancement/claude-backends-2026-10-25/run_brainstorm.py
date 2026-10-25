"""Ask each model the brainstorm question (build/brainstorm_candidates.py's own prompt) for the
same two batches (one seeds batch, one field batch), then run the tool's own filter on each
model's proposals. Spend is not recorded in the Routine's ledger (trial).

python3 run_brainstorm.py openrouter openai/gpt-6.1-sol
python3 run_brainstorm.py claude sonnet"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "build"))
sys.path.insert(0, str(HERE))
import brainstorm_candidates as bc  # noqa: E402
from claude_backend import call_claude  # noqa: E402
from review_runner import get_api_key  # noqa: E402

OUT = HERE / "results/brainstorm"


def parse(text):
    import re
    m = re.search(r"\[.*\]", text or "", re.DOTALL)
    try:
        return json.loads(m.group()) if m else None
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("backend", choices=["openrouter", "claude"])
    ap.add_argument("model")
    ap.add_argument("--effort")
    a = ap.parse_args()
    label = a.model.split("/")[-1] + (f"-{a.effort}" if a.effort else "")
    for lens in ("seeds", "field"):
        batch = json.load(open(OUT / f"batch-{lens}.json"))
        prompt = bc.prompt_for(batch, 6)
        t0 = time.time()
        if a.backend == "openrouter":
            items, cost = bc.call_model(get_api_key(), a.model, prompt)
            meta = {"usd": cost}
        else:
            resp = call_claude(prompt, model=a.model, effort=a.effort)
            items = parse(resp["choices"][0]["message"]["content"]) if resp and "choices" in resp else None
            meta = {"usage": (resp or {}).get("usage")}
        items = [dict(it, by=label) for it in items or [] if isinstance(it, dict) and it.get("word")]
        raw = OUT / f"{label}-{lens}.json"
        raw.write_text(json.dumps(items, ensure_ascii=False, indent=1))
        new = OUT / f"{label}-{lens}.new.json"
        f = subprocess.run([sys.executable, str(ROOT / "build/brainstorm_candidates.py"), "filter", str(raw),
                            "--out", str(new)], capture_output=True, text=True)
        meta.update({"label": label, "lens": lens, "wall_s": round(time.time() - t0, 1),
                     "proposals": len(items), "filter": f.stdout.strip() + f.stderr.strip()})
        with open(OUT / "runs.jsonl", "a") as fh:
            fh.write(json.dumps(meta, ensure_ascii=False) + "\n")
        print(meta)


if __name__ == "__main__":
    main()
