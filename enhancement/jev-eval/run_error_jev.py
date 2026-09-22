"""Paired test on real recovered errors: the pre-fix (wrong) and post-fix (fixed) text get the same questions."""
import json, sys
from pathlib import Path
S = Path(__file__).parent
sys.path.insert(0, str(S))
import jevclient as J
items = json.load(open(S / "error_set.json", encoding="utf-8"))
TRIAGE = {"type": "score", "instructions": "How likely is it that this dictionary material contains a factual error (wrong meaning, wrong translation, or a false claim about Japanese)?",
          "criteria": ["almost certainly correct", "probably correct", "unsure", "probably contains an error", "almost certainly contains an error"]}
def q_translation(it, english):
    state = {"headword": it["headword"], "reading": it["reading"], "gloss": it.get("gloss"),
             "example": {"japanese": it["japanese"], "english": english}}
    qs = {"faithful": {"type": "noul", "instructions": "Is `example.english` a faithful rendering of the meaning of `example.japanese`? Judge meaning only, not style or naturalness.",
                       "criteria": {"true": "the English conveys what the Japanese sentence means", "false": "the English mistranslates the Japanese: wrong word meaning, wrong subject or object, wrong polarity, tense or number, or a clause that is not in the Japanese"}},
          "kind": {"type": "choice", "instructions": "How does `example.english` relate to `example.japanese`?",
                   "criteria": {"faithful": "conveys the same meaning", "nuance": "same meaning but a shade off in nuance, register or naturalness", "wrong": "a different meaning"}},
          "triage": TRIAGE}
    return state, qs
def q_gloss(it, gloss):
    state = {"headword": it["headword"], "reading": it["reading"], "part_of_speech": it["pos"], "gloss_to_check": gloss,
             "explanation": it.get("explanation"), "examples": it.get("examples")}
    qs = {"accurate": {"type": "noul", "instructions": "Is `gloss_to_check` an accurate English gloss of the Japanese headword? Judge meaning, not completeness or style.",
                       "criteria": {"true": "every sense listed in the gloss is a real meaning of the word", "false": "the gloss contains a meaning the word does not have, or misstates its core meaning"}},
          "triage": TRIAGE}
    return state, qs
def q_notes(it, notes, lines):
    state = {"headword": it["headword"], "reading": it["reading"], "gloss": it.get("gloss"), "usage_notes": notes}
    qs = {"has_error": {"type": "noul", "instructions": "Does `usage_notes` contain a claim about Japanese meaning, grammar, usage, or facts that is false?",
                        "criteria": {"true": "at least one factual, grammatical, or usage claim in the notes is wrong", "false": "every claim in the notes is correct (style, breadth and omissions do not count)"}},
          "triage": TRIAGE}
    state2 = {"headword": it["headword"], "reading": it["reading"], "gloss": it.get("gloss"), "claim": "\n".join(lines)}
    qs2 = {"claim_false": {"type": "noul", "instructions": "Is the statement in `claim` (from a learner's dictionary note about the headword) false or misleading about Japanese?"}}
    return state, qs, state2, qs2
def ask(it):
    out = dict(it)
    try:
        if it["dim"] == "translation":
            for tag, eng in (("wrong", it["wrong_english"]), ("fixed", it["fixed_english"])):
                s, q = q_translation(it, eng); r = J.decide(s, q, test="err-translation"); a = r.get("answers", {})
                out[f"{tag}_faithful"] = a.get("faithful", {}).get("noul"); out[f"{tag}_kind"] = a.get("kind", {}).get("choice")
                out[f"{tag}_p_wrong"] = (a.get("kind", {}).get("probabilities") or {}).get("wrong"); out[f"{tag}_triage"] = a.get("triage", {}).get("score")
        elif it["dim"] == "gloss":
            for tag, g in (("wrong", it["wrong_gloss"]), ("fixed", it["fixed_gloss"])):
                s, q = q_gloss(it, g); r = J.decide(s, q, test="err-gloss"); a = r.get("answers", {})
                out[f"{tag}_accurate"] = a.get("accurate", {}).get("noul"); out[f"{tag}_triage"] = a.get("triage", {}).get("score")
        else:
            for tag, n, lines in (("wrong", it["wrong_notes"], it["wrong_lines"]), ("fixed", it["fixed_notes"], it["fixed_lines"])):
                s, q, s2, q2 = q_notes(it, n, lines)
                r = J.decide(s, q, test="err-notes"); a = r.get("answers", {})
                out[f"{tag}_has_error"] = a.get("has_error", {}).get("noul"); out[f"{tag}_triage"] = a.get("triage", {}).get("score")
                r2 = J.decide(s2, q2, test="err-notes-line"); out[f"{tag}_claim_false"] = r2.get("answers", {}).get("claim_false", {}).get("noul")
    except Exception as e:
        out["error"] = repr(e)
    return out
res = J.run_batch(items, ask, workers=6, label="errors")
json.dump(res, open(S / "error_jev_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("done; total cost", J.total_cost())
