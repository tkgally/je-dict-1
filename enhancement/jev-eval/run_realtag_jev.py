"""Realistic wrong-category test: tags the accuracy reviewer flagged; label = curator applied (wrong) or rejected (fine)."""
import json, sys
from pathlib import Path
S = Path(__file__).parent; sys.path.insert(0, str(S))
import jevclient as J
items = json.load(open(S / "realtag_set.json", encoding="utf-8"))
def ask(it):
    state = {"headword": it["headword"], "reading": it["reading"], "part_of_speech": it["pos"], "gloss": it["gloss"],
             "definitions": it["definitions"], "examples": it["examples"], "semantic_tags": it["all_tags"]}
    qs = {"tag_wrong": {"type": "noul", "instructions": f"Is the semantic-domain tag `{it['tag']}` WRONG for this headword, i.e. names a domain the word does not belong to at all? (Breadth is never a reason: a tag that fits loosely is not wrong.)"},
          "tag_fit": {"type": "score", "instructions": f"How well does the semantic-domain tag `{it['tag']}` fit this headword?",
                      "criteria": ["names a domain the word does not belong to at all", "a stretch: only a weak or indirect connection", "fits loosely but acceptably", "fits well"]}}
    r = J.decide(state, qs, test="realtag"); a = r.get("answers", {})
    out = dict(it); out["jev_wrong"] = a.get("tag_wrong", {}).get("noul"); out["jev_fit"] = a.get("tag_fit", {}).get("score"); out["jev_fit_probs"] = a.get("tag_fit", {}).get("probabilities")
    if "error" in r: out["error"] = r["error"]
    return out
res = J.run_batch(items, ask, workers=6, label="realtag")
json.dump(res, open(S / "realtag_jev_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
from analyze import auc, pr_at
ok = [r for r in res if not r.get("error")]
w = [r["jev_wrong"] for r in ok if r["decision"] == "apply"]; f = [r["jev_wrong"] for r in ok if r["decision"] == "reject"]
print(f"real wrong-category: n apply={len(w)} reject={len(f)}; AUC={auc(w, f):.3f}; mean P(wrong) apply={sum(w)/len(w):.2f} reject={sum(f)/len(f):.2f}")
sl = [(r["jev_wrong"], r["decision"]) for r in ok]
for thr in (0.3, 0.5, 0.7, 0.9):
    tp, fp, fn, p, rc = pr_at(sl, thr, "apply"); print(f"  thr {thr}: TP {tp} FP {fp} FN {fn} precision {p:.3f} recall {rc:.3f}")
print("-- rejects Jev calls wrong (P>=0.7) --")
for r in sorted([r for r in ok if r["decision"] == "reject" and r["jev_wrong"] >= 0.7], key=lambda r: -r["jev_wrong"])[:10]:
    print(f"  {r['jev_wrong']:.2f} {r['headword']} ({(r['gloss'] or '')[:35]}) tag={r['tag']}")
print("-- applies Jev misses (P<0.3) --")
for r in sorted([r for r in ok if r["decision"] == "apply" and r["jev_wrong"] < 0.3], key=lambda r: r["jev_wrong"])[:10]:
    print(f"  {r['jev_wrong']:.2f} {r['headword']} ({(r['gloss'] or '')[:35]}) tag={r['tag']} :: {(r['concern'] or '')[:80]}")
