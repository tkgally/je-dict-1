"""Realistic mode: one call per sentence, one Noul per {kanji|reading} pair in it (fan-out)."""
import json, sys, re
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
FURI = re.compile(r"\{([^|{}]+)\|([^}]+)\}")
items = json.load(open(S / "furigana_set.json", encoding="utf-8"))
MARK = ("Furigana markup is {kanji|reading}: the hiragana after the bar is the reading of ONLY the kanji "
        "inside the braces; okurigana follow the closing brace and are not part of the reading.")
def ask(it):
    pairs = list(dict.fromkeys(FURI.findall(it["sentence"])))
    state = {"dictionary_entry": {"headword": it["headword"], "reading": it["hw_reading"], "gloss": it["gloss"]},
             "example_sentence": it["sentence"], "english_translation": it["english"],
             "pairs": [{"id": f"p{i}", "kanji": k, "reading_given": r} for i, (k, r) in enumerate(pairs)]}
    qs = {f"p{i}": {"type": "noul",
                    "instructions": f"{MARK} In `example_sentence`, is `{r}` the correct reading of the kanji `{k}` (pair p{i})?",
                    "criteria": {"true": "the given hiragana is exactly the correct reading of those kanji in this context",
                                 "false": "the given hiragana is not how those kanji are read here: wrong reading, wrong voicing, missing or extra kana, or okurigana wrongly included"}}
          for i, (k, r) in enumerate(pairs)}
    r = J.decide(state, qs, test="furigana-fanout")
    out = {"n": it["n"], "label": it["label"], "kind": it["kind"], "kanji": it["kanji"], "reading": it["reading"], "npairs": len(pairs)}
    a = r.get("answers", {})
    out["all"] = {f"{k}|{rd}": a.get(f"p{i}", {}).get("noul") for i, (k, rd) in enumerate(pairs)}
    out["jev_noul"] = out["all"].get(f"{it['kanji']}|{it['reading']}")
    out["tokens"] = (r.get("usage") or {}).get("input_tokens")
    if "error" in r: out["error"] = r["error"]
    return out
res = J.run_batch(items, ask, workers=8, label="fanout")
json.dump(res, open(S / "furigana_fanout_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost", J.total_cost())
