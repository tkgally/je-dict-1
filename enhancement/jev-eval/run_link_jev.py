"""Ask Jev whether each marked kana word is the linked entry's word (link_set.json)."""
import json, sys
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
items = json.load(open(S / "link_set.json", encoding="utf-8"))

def ask(it):
    ti = it["target_info"]
    state = {"text_with_one_word_marked": it["context"],
             "marked_word": it["surface"],
             "english_translation": it.get("english"),
             "linked_dictionary_entry": {"headword": ti["headword"], "reading": ti["reading"], "part_of_speech": ti["pos"],
                                         "gloss": ti["gloss"], "other_senses": ti["other_senses"]},
             "known_same_kana_competitors": it["competitors"]}
    qs = {
        "is_entry_word": {"type": "choice",
            "instructions": ("In `text_with_one_word_marked`, one word is marked 【like this】. An automatic linker linked it to "
                             "`linked_dictionary_entry`. Is the marked word, in this context, that entry's word? Inflection, politeness and "
                             "kanji-versus-kana spelling do not matter; any of the entry's senses counts."),
            "criteria": {"entry": "the marked word is the linked entry's word (any sense, any inflection)",
                         "other": "the marked word is a different word or construction here: a homophone with different kanji, an inflected form of another word, or a sequence of smaller words"}},
        "is_other_noul": {"type": "noul",
            "instructions": "Is the marked word 【…】 in `text_with_one_word_marked` a DIFFERENT word from `linked_dictionary_entry` (a homophone, another word's inflected form, or a sequence of smaller words)?"},
    }
    r = J.decide(state, qs, test="links")
    out = dict(it)
    a = r.get("answers", {})
    out["jev_choice"] = a.get("is_entry_word", {}).get("choice")
    out["jev_p_other"] = (a.get("is_entry_word", {}).get("probabilities") or {}).get("other")
    out["jev_conf"] = a.get("is_entry_word", {}).get("confidence")
    out["jev_noul_other"] = a.get("is_other_noul", {}).get("noul")
    if "error" in r: out["error"] = r["error"]
    return out
res = J.run_batch(items, ask, workers=8, label="links")
json.dump(res, open(S / "link_jev_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost so far", J.total_cost())
