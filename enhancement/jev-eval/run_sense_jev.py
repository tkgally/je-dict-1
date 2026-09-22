"""Sense assignment: for multi-sense entries, which sense does an example illustrate? Ground truth = the entry's sense_numbers."""
import json, sys, re, glob, random, collections
from pathlib import Path
S = Path(__file__).parent; sys.path.insert(0, str(S))
import jevclient as J
from analyze import auc
random.seed(21)
LINK = re.compile(r"⟦([^⟧]*?)→[^⟧]*⟧"); FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}")
def plain(t): return FURI.sub(r"\1", LINK.sub(r"\1", t or ""))
paths = sorted(glob.glob("entries/*/*.json")); random.shuffle(paths)
items = []
for p in paths:
    if len(items) >= 400: break
    e = json.load(open(p, encoding="utf-8"))
    defs = e.get("definitions") or []
    if len(defs) < 2 or len(defs) > 5: continue
    exs = [x for x in e.get("examples") or [] if x.get("sense_numbers") and len(x["sense_numbers"]) == 1 and x.get("japanese")]
    if not exs: continue
    # prefer examples that are not all sense 1
    ex = random.choice(exs)
    items.append({"entry": e["id"], "headword": plain(e.get("headword")), "reading": e.get("reading"), "pos": e.get("part_of_speech"),
                  "senses": {str(d.get("sense_number", i + 1)): f"{d.get('gloss')} — {d.get('explanation') or ''}"[:300] for i, d in enumerate(defs)},
                  "japanese": plain(ex["japanese"]), "english": ex.get("english"), "true": str(ex["sense_numbers"][0])})
print("items", len(items), collections.Counter(i["true"] for i in items), file=sys.stderr)
def ask(it):
    state = {"headword": it["headword"], "reading": it["reading"], "part_of_speech": it["pos"], "senses": it["senses"],
             "example": {"japanese": it["japanese"], "english": it["english"]}}
    qs = {"sense": {"type": "choice", "instructions": "Which numbered sense in `senses` does `example` illustrate?", "criteria": {k: v for k, v in it["senses"].items()}}}
    r = J.decide(state, qs, test="sense"); a = r.get("answers", {}).get("sense", {})
    out = dict(it); out["jev"] = a.get("choice"); out["conf"] = a.get("confidence"); out["probs"] = a.get("probabilities")
    if "error" in r: out["error"] = r["error"]
    return out
res = J.run_batch(items, ask, workers=8, label="sense")
json.dump(res, open(S / "sense_jev_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
ok = [r for r in res if not r.get("error")]
print(f"sense agreement: {sum(1 for r in ok if r['jev']==r['true'])}/{len(ok)} = {sum(1 for r in ok if r['jev']==r['true'])/len(ok):.3f}; majority (sense 1) baseline {sum(1 for r in ok if r['true']=='1')/len(ok):.3f}")
for lo, hi in ((0.9, 1.01), (0.7, 0.9), (0.5, 0.7), (0, 0.5)):
    g = [r for r in ok if lo <= (r["conf"] or 0) < hi]
    if g: print(f"  confidence [{lo},{hi}): n={len(g)} agreement={sum(1 for r in g if r['jev']==r['true'])/len(g):.3f}")
print("-- disagreements at confidence>=0.9 (either the entry's sense number or Jev is wrong) --")
for r in [r for r in ok if r["jev"] != r["true"] and (r["conf"] or 0) >= 0.9][:12]:
    print(f"  {r['entry']} {r['headword']}: entry says {r['true']}, Jev {r['jev']} ({r['conf']}) | {r['japanese'][:40]} / {(r['english'] or '')[:50]}")
    for k, v in r["senses"].items(): print(f"      {k}: {v[:70]}")
