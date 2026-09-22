"""False-positive rate on a large sample of presumed-correct sentences, fan-out mode (one call per sentence)."""
import json, sys, re, glob, random
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
random.seed(99)
FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}"); LINK = re.compile(r"⟦([^⟧]*?)→[^⟧]*⟧")
def plain(t): return LINK.sub(r"\1", t or "")
paths = sorted(glob.glob("entries/*/*.json")); random.shuffle(paths)
items = []
for p in paths[:1500]:
    e = json.load(open(p, encoding="utf-8"))
    exs = [x for x in e.get("examples") or [] if x.get("japanese") and FURI.search(plain(x["japanese"]))]
    if not exs: continue
    ex = random.choice(exs)
    items.append({"entry": e["id"], "headword": plain(e.get("headword")), "hw_reading": e.get("reading"), "gloss": e.get("gloss"),
                  "sentence": plain(ex["japanese"]), "english": ex.get("english")})
MARK = ("Furigana markup is {kanji|reading}: the hiragana after the bar is the reading of ONLY the kanji "
        "inside the braces; okurigana follow the closing brace and are not part of the reading.")
def ask(it):
    pairs = list(dict.fromkeys(FURI.findall(it["sentence"])))
    state = {"dictionary_entry": {"headword": it["headword"], "reading": it["hw_reading"], "gloss": it["gloss"]},
             "example_sentence": it["sentence"], "english_translation": it["english"],
             "pairs": [{"id": f"p{i}", "kanji": k, "reading_given": r} for i, (k, r) in enumerate(pairs)]}
    qs = {f"p{i}": {"type": "noul", "instructions": f"{MARK} In `example_sentence`, is `{r}` the correct reading of the kanji `{k}` (pair p{i})?",
                    "criteria": {"true": "the given hiragana is exactly the correct reading of those kanji in this context",
                                 "false": "the given hiragana is not how those kanji are read here: wrong reading, wrong voicing, missing or extra kana, or okurigana wrongly included"}}
          for i, (k, r) in enumerate(pairs)}
    r = J.decide(state, qs, test="fp-rate")
    a = r.get("answers", {})
    return {"entry": it["entry"], "sentence": it["sentence"], "pairs": [(k, rd, a.get(f"p{i}", {}).get("noul")) for i, (k, rd) in enumerate(pairs)],
            "tokens": (r.get("usage") or {}).get("input_tokens"), "error": r.get("error")}
res = J.run_batch(items, ask, workers=8, label="fp-rate")
json.dump(res, open(S / "fp_rate_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost", J.total_cost())
