"""Baseline: gemini-2.5-flash on link_set.json using review_links.py's own prompt, in batches of 15."""
import json, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, "build")
from review_runner import call_openrouter, extract_message_text, strip_code_fences, get_api_key
import review_links as rl
import check_link_homophones as clh
S = Path(__file__).parent
items = json.load(open(S / "link_set.json", encoding="utf-8"))
key = get_api_key()
MODEL = "google/gemini-2.5-flash"
COST = {"input": 0.30/1e6, "output": 2.50/1e6}
info = rl.load_entry_info()
data = clh.load_data()
B = 15
batches = [items[i:i+B] for i in range(0, len(items), B)]
tot = {"in": 0, "out": 0}
def ask(batch):
    occ = [clh.Occurrence(entry=it["entry"], field=it["field"], surface=it["surface"], base=it["base"],
                          target=it["target"], context=it["context"], english=it.get("english")) for it in batch]
    p = rl.review_prompt(occ, info, data)
    r = call_openrouter(key, MODEL, p, timeout=180, max_tokens=4000)
    out = [dict(it) for it in batch]
    if not r:
        for o in out: o["gem_error"] = "no response"
        return out
    u = r.get("usage") or {}
    tot["in"] += u.get("prompt_tokens", 0); tot["out"] += u.get("completion_tokens", 0)
    txt = strip_code_fences(extract_message_text(r) or "")
    m = re.search(r"\[.*\]", txt, re.S)
    try:
        arr = json.loads(m.group()) if m else []
    except Exception:
        arr = []
    byn = {a.get("n"): a for a in arr if isinstance(a, dict)}
    for i, o in enumerate(out, 1):
        a = byn.get(i)
        if a: o["gem_verdict"] = a.get("verdict"); o["gem_word"] = a.get("word"); o["gem_note"] = a.get("note")
        else: o["gem_error"] = "missing"
    return out
res = [None] * len(batches)
with ThreadPoolExecutor(max_workers=5) as ex:
    futs = {ex.submit(ask, b): i for i, b in enumerate(batches)}
    for n, f in enumerate(as_completed(futs), 1):
        res[futs[f]] = f.result()
        if n % 20 == 0: print(n, file=sys.stderr)
flat = [o for b in res for o in b]
cost = tot["in"] * COST["input"] + tot["out"] * COST["output"]
json.dump({"results": flat, "tokens": tot, "est_cost": cost}, open(S / "link_gemini_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("gemini links done; tokens", tot, "est cost", round(cost, 4))
