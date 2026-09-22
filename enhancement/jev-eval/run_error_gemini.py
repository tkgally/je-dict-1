"""Baseline on the recovered real errors: gemini-2.5-flash, paired wrong/fixed, translation and gloss only."""
import json, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, "build")
from review_runner import call_openrouter, extract_message_text, strip_code_fences, get_api_key
S = Path(__file__).parent
items = [it for it in json.load(open(S / "error_set.json", encoding="utf-8")) if it["dim"] in ("translation", "gloss")]
key = get_api_key(); MODEL = "google/gemini-2.5-flash"; COST = {"input": 0.30/1e6, "output": 2.50/1e6}
def p_tr(it, eng):
    return f"""You are checking an example sentence in a Japanese-English learner's dictionary.
Headword: {it['headword']} ({it['reading']}) — {it.get('gloss')}
Japanese: {it['japanese']}
English: {eng}
Is the English a faithful rendering of the meaning of the Japanese? Judge meaning only (wrong word meaning, wrong subject/object, polarity, tense, number, or content not in the Japanese), not style or naturalness.
Respond ONLY with JSON: {{"faithful": true/false, "confidence": 0.0-1.0, "reason": "<short>"}}"""
def p_gl(it, g):
    exs = "\n".join(f"- {x['japanese']} / {x['english']}" for x in it.get("examples") or [])
    return f"""You are checking a gloss in a Japanese-English learner's dictionary.
Headword: {it['headword']} ({it['reading']}), {it['pos']}
Gloss to check: {g}
Explanation: {it.get('explanation')}
Examples:
{exs}
Is the gloss an accurate English gloss of the headword? Judge meaning only: is every sense listed a real meaning of the word, and is the core meaning stated correctly? Completeness and style do not count.
Respond ONLY with JSON: {{"accurate": true/false, "confidence": 0.0-1.0, "reason": "<short>"}}"""
tot = {"in": 0, "out": 0}
def one(prompt):
    r = call_openrouter(key, MODEL, prompt, timeout=90, max_tokens=300)
    if not r: return None
    u = r.get("usage") or {}; tot["in"] += u.get("prompt_tokens", 0); tot["out"] += u.get("completion_tokens", 0)
    txt = strip_code_fences(extract_message_text(r) or ""); m = re.search(r"\{.*\}", txt, re.S)
    try: return json.loads(m.group()) if m else None
    except Exception: return None
def ask(it):
    out = {"entry": it["entry"], "dim": it["dim"], "note": it["note"]}
    for tag in ("wrong", "fixed"):
        if it["dim"] == "translation":
            j = one(p_tr(it, it[f"{tag}_english"])); k = "faithful"
        else:
            j = one(p_gl(it, it[f"{tag}_gloss"])); k = "accurate"
        out[f"{tag}_ok"] = None if not j else j.get(k); out[f"{tag}_conf"] = None if not j else j.get("confidence"); out[f"{tag}_reason"] = None if not j else j.get("reason")
    return out
res = [None] * len(items)
with ThreadPoolExecutor(max_workers=5) as ex:
    futs = {ex.submit(ask, it): i for i, it in enumerate(items)}
    for n, f in enumerate(as_completed(futs), 1):
        res[futs[f]] = f.result()
        if n % 100 == 0: print(n, file=sys.stderr)
cost = tot["in"] * COST["input"] + tot["out"] * COST["output"]
json.dump({"results": res, "tokens": tot, "est_cost": cost}, open(S / "error_gemini_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("gemini errors done; tokens", tot, "est cost", round(cost, 4))
