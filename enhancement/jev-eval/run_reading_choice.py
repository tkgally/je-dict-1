"""Choose-the-reading test: for kanji strings with several readings in the dictionary, can Jev pick the right one in context?"""
import json, sys, re, glob, random
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
random.seed(3)
FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}"); LINK = re.compile(r"⟦([^⟧]*?)→[^⟧]*⟧")
def plain(t): return LINK.sub(r"\1", t or "")
inv = json.load(open(S / "pair_inventory.json", encoding="utf-8"))
multi = {k: v for k, v in inv.items() if len([r for r, n in v.items() if n >= 2]) >= 2}
paths = sorted(glob.glob("entries/*/*.json")); random.shuffle(paths)
items = []
for p in paths:
    if len(items) >= 400: break
    e = json.load(open(p, encoding="utf-8"))
    for ex in e.get("examples") or []:
        sent = plain(ex.get("japanese"))
        ms = [m for m in FURI.finditer(sent) if m.group(1) in multi and inv[m.group(1)][m.group(2)] >= 2]
        if not ms: continue
        m = random.choice(ms); k, r = m.group(1), m.group(2)
        opts = [x for x, n in inv[k].items() if n >= 2]
        random.shuffle(opts)
        masked = sent[:m.start()] + "{" + k + "|？}" + sent[m.end():]
        items.append({"entry": e["id"], "headword": plain(e.get("headword")), "gloss": e.get("gloss"), "sentence": masked,
                      "english": ex.get("english"), "kanji": k, "true": r, "options": opts,
                      "majority": max(inv[k].items(), key=lambda x: x[1])[0], "counts": {x: inv[k][x] for x in opts}})
        break
print("items", len(items), file=sys.stderr)
def ask(it):
    state = {"dictionary_entry": {"headword": it["headword"], "gloss": it["gloss"]},
             "example_sentence_with_one_reading_masked": it["sentence"], "english_translation": it["english"],
             "kanji_to_read": it["kanji"]}
    qs = {"reading": {"type": "choice", "instructions": "Which hiragana reading does `kanji_to_read` have at the position marked {kanji|？} in `example_sentence_with_one_reading_masked`? The reading covers only the kanji, not the okurigana that follow the closing brace.",
                      "criteria": {o: None for o in it["options"]}}}
    r = J.decide(state, qs, test="reading-choice")
    out = dict(it); a = r.get("answers", {}).get("reading", {})
    out["jev"] = a.get("choice"); out["conf"] = a.get("confidence"); out["probs"] = a.get("probabilities")
    if "error" in r: out["error"] = r["error"]
    return out
res = J.run_batch(items, ask, workers=8, label="reading-choice")
json.dump(res, open(S / "reading_choice_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost", J.total_cost())
