"""Metadata classification: formality, politeness, POS family, and wrong-category semantic tag detection."""
import json, sys
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
items = json.load(open(S / "meta_set.json", encoding="utf-8"))
TAGDOC = {"formality": {"neutral": "ordinary vocabulary usable in most contexts", "formal": "formal, literary, written, official or technical register", "informal": "casual, colloquial, slang or familiar speech"},
          "politeness": {"plain": "no built-in politeness (dictionary form, ordinary words)", "polite": "a polite (teineigo) form such as です/ます or a polite word", "humble": "a humble (kenjougo) word that lowers the speaker", "honorific": "a respectful (sonkeigo) word that raises the listener or subject"},
          "posfam": {"noun": "noun (including suru-verb nouns and no-adjective nouns)", "verb": "verb (godan, ichidan, irregular, suru verb as verb)", "adjective": "i-adjective or na-adjective", "adverb": "adverb", "expression": "expression, phrase, idiom, proverb, interjection", "other": "particle, counter, prefix, suffix, conjunction, pronoun, auxiliary"}}
def posfam(pos):
    p = (pos or "").lower()
    if p.startswith("noun") or p == "suru verb" or "noun" in p.split(",")[0]: return "noun"
    if p.startswith("verb"): return "verb"
    if "adjective" in p.split(",")[0]: return "adjective"
    if p.startswith("adverb"): return "adverb"
    if p.startswith(("expression", "idiom", "proverb", "interjection", "phrase")): return "expression"
    return "other"
def ask(it):
    state = {"headword": it["headword"], "reading": it["reading"], "part_of_speech": it["pos"], "gloss": it["gloss"],
             "definitions": it["definitions"], "examples": it["examples"], "notes_excerpt": it["notes_head"]}
    qs = {"formality": {"type": "choice", "instructions": "What formality register does this dictionary headword have?", "criteria": TAGDOC["formality"]},
          "politeness": {"type": "choice", "instructions": "What politeness level is built into this headword itself (not its example sentences)?", "criteria": TAGDOC["politeness"]},
          "posfam": {"type": "choice", "instructions": "Which part-of-speech family does the headword belong to, judging from the headword, gloss and examples (ignore the `part_of_speech` field)?", "criteria": TAGDOC["posfam"]},
          "tag_wrong": {"type": "noul", "instructions": f"Is the semantic-domain tag `{it['wrong_tag']}` WRONG for this headword, i.e. names a domain the word does not belong to at all? (Breadth is never a reason: a tag that fits loosely is not wrong.)"}}
    if it["real_tag"]:
        qs["tag_real"] = {"type": "noul", "instructions": f"Is the semantic-domain tag `{it['real_tag']}` WRONG for this headword, i.e. names a domain the word does not belong to at all? (Breadth is never a reason: a tag that fits loosely is not wrong.)"}
    r = J.decide(state, qs, test="meta")
    a = r.get("answers", {})
    out = dict(it); out["posfam_true"] = posfam(it["pos"])
    for k in ("formality", "politeness", "posfam"):
        out[f"jev_{k}"] = a.get(k, {}).get("choice"); out[f"jev_{k}_conf"] = a.get(k, {}).get("confidence")
    out["jev_wrong_tag_noul"] = a.get("tag_wrong", {}).get("noul")
    out["jev_real_tag_noul"] = a.get("tag_real", {}).get("noul") if it["real_tag"] else None
    if "error" in r: out["error"] = r["error"]
    return out
res = J.run_batch(items, ask, workers=6, label="meta")
json.dump(res, open(S / "meta_jev_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost", J.total_cost())
