"""Ask Jev about every pair in furigana_set.json: with sentence context and without."""
import json, sys
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
items = json.load(open(S / "furigana_set.json", encoding="utf-8"))
MARK = ("Furigana markup is {kanji|reading}: the hiragana after the bar is the reading of ONLY the kanji "
        "inside the braces; okurigana follow the closing brace and are not part of the reading.")

def ask(it):
    state = {"dictionary_entry": {"headword": it["headword"], "reading": it["hw_reading"], "gloss": it["gloss"]},
             "example_sentence": it["sentence"], "english_translation": it["english"],
             "pair_to_check": {"kanji": it["kanji"], "reading_given": it["reading"]}}
    qs = {
        "reading_correct": {"type": "noul",
            "instructions": f"{MARK} In `example_sentence`, is `pair_to_check.reading_given` the correct reading of the kanji `pair_to_check.kanji` as used in that sentence?",
            "criteria": {"true": "the given hiragana is exactly the correct reading of those kanji in this context (rendaku, counters and compound readings count as correct when they are how the word is actually pronounced)",
                         "false": "the given hiragana is not how those kanji are read here: a wrong reading, a wrong voicing, a missing or extra kana, or okurigana wrongly included in the reading"}},
        "verdict": {"type": "choice",
            "instructions": f"{MARK} Judge `pair_to_check`: is `reading_given` the right reading of `kanji` in `example_sentence`?",
            "criteria": {"correct": "the reading is right", "wrong": "the reading is wrong in any way (wrong kana, voicing, length, or okurigana bleed)"}},
    }
    r1 = J.decide(state, qs, test="furigana-ctx")
    # no-context variant
    state2 = {"pair_to_check": {"kanji": it["kanji"], "reading_given": it["reading"]}}
    q2 = {"reading_correct": {"type": "noul",
            "instructions": "Is `pair_to_check.reading_given` a correct Japanese reading (hiragana) of the kanji string `pair_to_check.kanji`, as the word is normally pronounced?"}}
    r2 = J.decide(state2, q2, test="furigana-noctx")
    out = dict(it)
    a = r1.get("answers", {})
    out["jev_noul"] = a.get("reading_correct", {}).get("noul")
    out["jev_choice"] = a.get("verdict", {}).get("choice")
    out["jev_choice_p_wrong"] = (a.get("verdict", {}).get("probabilities") or {}).get("wrong")
    out["jev_choice_conf"] = a.get("verdict", {}).get("confidence")
    out["jev_noul_noctx"] = r2.get("answers", {}).get("reading_correct", {}).get("noul")
    out["tokens"] = (r1.get("usage") or {}).get("input_tokens")
    if "error" in r1: out["error"] = r1["error"]
    return out
res = J.run_batch(items, ask, workers=8, label="furigana")
json.dump(res, open(S / "furigana_jev_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost so far", J.total_cost())
