"""Baseline: gemini-2.5-flash on the same furigana set, one pair per call, JSON verdict."""
import json, sys, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, "build")
from review_runner import call_openrouter, extract_message_text, strip_code_fences, get_api_key
S = Path(__file__).parent
items = json.load(open(S / "furigana_set.json", encoding="utf-8"))
key = get_api_key()
MODEL = "google/gemini-2.5-flash"
COST = {"input": 0.30/1e6, "output": 2.50/1e6}
def prompt(it):
    return f"""Check ONE furigana reading in a Japanese dictionary example sentence.
Format: {{kanji|reading}}okurigana — the reading covers ONLY the kanji inside the braces; okurigana follow the closing brace.
Rendaku, counter sound changes and compound readings are correct when that is how the word is actually pronounced.

Entry: {it['headword']} ({it['hw_reading']}) — {it['gloss']}
Sentence: {it['sentence']}
English: {it['english']}

Pair to check: {{{it['kanji']}|{it['reading']}}}
Is "{it['reading']}" the correct reading of 「{it['kanji']}」 in this sentence?
Respond ONLY with JSON: {{"correct": true/false, "confidence": 0.0-1.0, "reason": "<short>"}}"""
tot = {"in": 0, "out": 0}
def ask(it):
    r = call_openrouter(key, MODEL, prompt(it), timeout=90, max_tokens=300)
    out = dict(it)
    if not r:
        out["gem_error"] = "no response"; return out
    u = r.get("usage") or {}
    tot["in"] += u.get("prompt_tokens", 0); tot["out"] += u.get("completion_tokens", 0)
    txt = strip_code_fences(extract_message_text(r) or "")
    m = re.search(r"\{.*\}", txt, re.S)
    try:
        j = json.loads(m.group()) if m else None
    except Exception:
        j = None
    if j is None:
        out["gem_error"] = txt[:200]; return out
    out["gem_correct"] = j.get("correct"); out["gem_conf"] = j.get("confidence"); out["gem_reason"] = j.get("reason")
    return out
res = [None] * len(items)
with ThreadPoolExecutor(max_workers=6) as ex:
    futs = {ex.submit(ask, it): i for i, it in enumerate(items)}
    for n, f in enumerate(as_completed(futs), 1):
        res[futs[f]] = f.result()
        if n % 100 == 0: print(n, file=sys.stderr)
cost = tot["in"] * COST["input"] + tot["out"] * COST["output"]
json.dump({"results": res, "tokens": tot, "est_cost": cost}, open(S / "furigana_gemini_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("gemini furigana done; tokens", tot, "est cost", round(cost, 4))
