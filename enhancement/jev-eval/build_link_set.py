"""Kana-link homophone test set from reviews/link_decisions.jsonl (claude-adjudicated rows with context)
plus random current links as easy negatives."""
import json, sys, random
from pathlib import Path
sys.path.insert(0, "build")
import check_link_homophones as clh
import review_links as rl
S = Path(__file__).parent
random.seed(7)
info = rl.load_entry_info()
data = clh.load_data()
rows = [json.loads(l) for l in open("reviews/link_decisions.jsonl", encoding="utf-8") if l.strip()]
items = []
for r in rows:
    if not r.get("entry") or not r.get("context") or r.get("by") != "claude":
        continue
    tgt = r["target"]
    if tgt not in info: continue
    comps = (data["bases"].get(r["base"]) or {}).get("competitors") or []
    label = "entry" if r["decision"] == "keep" else "other"
    items.append({"src": "ledger", "entry": r["entry"], "field": r["field"], "surface": r["surface"],
                  "base": r["base"], "target": tgt, "context": r["context"], "english": None,
                  "competitors": comps, "label": label, "decision": r["decision"], "note": r.get("note")})
# dedupe on (entry, field, context)
seen = set(); led = []
for it in items:
    k = (it["entry"], it["field"], it["context"])
    if k in seen: continue
    seen.add(k); led.append(it)
print("ledger items", len(led), "other", sum(1 for i in led if i["label"]=="other"), file=sys.stderr)
# easy negatives: random current links in verify/unique tiers not in ledger
occ = clh.collect()
random.shuffle(occ)
idx = clh.decision_index(rows)
easy = []
for o in occ:
    if len(easy) >= 300: break
    if idx.get((clh.entry_num(o["entry"]), o["base"], o["target"])): continue
    if o["target"] not in info: continue
    comps = (data["bases"].get(o["base"]) or {}).get("competitors") or []
    easy.append({"src": "random", "entry": o["entry"], "field": o["field"], "surface": o["surface"],
                 "base": o["base"], "target": o["target"], "context": o["context"], "english": o.get("english"),
                 "competitors": comps, "label": "entry", "decision": "presumed-keep", "note": None})
# attach entry descriptions
for it in led + easy:
    e = info[it["target"]]
    it["target_info"] = {"headword": e["headword"], "reading": e["reading"], "pos": e["pos"],
                         "gloss": e["gloss"], "other_senses": [s for s in e["senses"] if s != e["gloss"]][:5]}
allitems = led + easy
random.shuffle(allitems)
for i, it in enumerate(allitems): it["n"] = i
json.dump(allitems, open(S / "link_set.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("total", len(allitems), file=sys.stderr)
