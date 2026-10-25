"""Pool every model's NEW brainstorm proposals (after the tool's filter), hide who proposed them,
and ask a judge to apply the find-candidates gates: add (a real, established word in lemma form,
worth an entry for an intermediate learner) or reject. Then count accepted words per model.

python3 judge_brainstorm.py claude opus | openrouter google/gemini-4-argon ; python3 judge_brainstorm.py --score"""
import argparse
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "build"))
sys.path.insert(0, str(HERE))
from claude_backend import call_claude  # noqa: E402
from review_runner import call_openrouter, get_api_key, extract_message_text, strip_code_fences  # noqa: E402

B = HERE / "results/brainstorm"


def pool():
    words = {}
    for p in sorted(B.glob("*.new.json")):
        label, lens = p.name[:-len(".new.json")].rsplit("-", 1)
        for it in json.load(open(p)):
            k = (lens, it["word"], it["reading"])
            w = words.setdefault(k, {"lens": lens, "word": it["word"], "reading": it["reading"],
                                     "gloss": it.get("gloss"), "variant": it.get("possible_variant"), "by": set()})
            w["by"].add(label)
    return list(words.values())


def prompt(ws):
    lines = [f'{n}. {w["word"]} ({w["reading"]}): {w["gloss"]}' for n, w in enumerate(ws, 1)]
    return ("You are the editor of a Japanese-English learner's dictionary of about 32,000 entries for "
            "intermediate learners who read kana. None of the words below is in it yet. For each, decide:\n"
            "add    = a real, established Japanese word or set phrase, in dictionary form, with the reading "
            "and meaning given, that an intermediate learner would meet in everyday life, school, news, work "
            "or culture, and that deserves its own entry;\n"
            "reject = not an established word, a wrong reading or gloss, a free phrase (noun+の+noun, "
            "adjective+noun), an inflected form, a mere spelling variant of a common word, or too rare, "
            "technical, archaic, dialectal or slangy to be worth an entry.\n\n"
            + "\n".join(lines)
            + '\n\nRespond with ONLY a JSON array, one object per item, in order: '
              '{"n": <number>, "verdict": "add|reject", "why": "<six words or fewer>"}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("backend", nargs="?")
    ap.add_argument("model", nargs="?")
    ap.add_argument("--score", action="store_true")
    a = ap.parse_args()
    ws = pool()
    ws.sort(key=lambda w: (w["lens"], w["word"]))
    random.Random(5).shuffle(ws)
    if a.score:
        score(ws)
        return
    label = a.model.split("/")[-1]
    p = prompt(ws)
    if a.backend == "claude":
        txt = call_claude(p, model=a.model)["choices"][0]["message"]["content"]
    else:
        txt = extract_message_text(call_openrouter(get_api_key(), a.model, p, timeout=300, max_tokens=16000))
    t = strip_code_fences(txt.strip())
    arr = json.loads(t[t.find("["): t.rfind("]") + 1])
    out = [{"word": w["word"], "reading": w["reading"], "lens": w["lens"], "by": sorted(w["by"]),
            "verdict": next((x["verdict"] for x in arr if int(x["n"]) == n), None),
            "why": next((x.get("why") for x in arr if int(x["n"]) == n), None)} for n, w in enumerate(ws, 1)]
    (B / f"judge-{label}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"{len(out)} words judged by {label}: {sum(1 for o in out if o['verdict'] == 'add')} add")


def score(ws):
    judges = {p.stem[6:]: {(o["lens"], o["word"], o["reading"]): o["verdict"] for o in json.load(open(p))}
              for p in B.glob("judge-*.json")}
    models = sorted({m for w in ws for m in w["by"]})
    print(f"{len(ws)} distinct new proposals; judges: {', '.join(judges)}")
    res = {}
    for m in models:
        row = {}
        for lens in ("seeds", "field"):
            mine = [w for w in ws if m in w["by"] and w["lens"] == lens]
            row[lens] = {"new": len(mine)}
            for j, v in judges.items():
                row[lens][j] = sum(1 for w in mine if v.get((w["lens"], w["word"], w["reading"])) == "add")
            row[lens]["both"] = sum(1 for w in mine if all(v.get((w["lens"], w["word"], w["reading"])) == "add"
                                                           for v in judges.values()))
            row[lens]["unique_both"] = sum(1 for w in mine if len(w["by"]) == 1 and all(
                v.get((w["lens"], w["word"], w["reading"])) == "add" for v in judges.values()))
        res[m] = row
        print(f"{m:18s} " + "  ".join(f"{lens}: new {r['new']:2d}, accepted(both) {r['both']:2d}, only-this-model {r['unique_both']:2d}"
                                      for lens, r in row.items()))
    json.dump(res, open(HERE / "brainstorm_summary.json", "w"), indent=1)


if __name__ == "__main__":
    main()
