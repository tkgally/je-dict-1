"""Run decision models (Decisions API) and LLM baselines over the test sets.

python3 run.py dec <model> <task> [--workers 8]
python3 run.py llm <model> <task> [--batch 20]
Results cached in results/<model-slug>/<task>.jsonl (one line per item; reruns skip done ids).
"""
import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

HERE = Path(__file__).parent
KEY = os.environ["OPENROUTER_API_KEY"]
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
     "HTTP-Referer": "https://github.com/tkgally/je-dict-1", "X-Title": "je-dict-1 decision-model eval"}

READING_Q = {"type": "noul",
             "instructions": "Is proposed_reading (hiragana) exactly the correct reading of the word marked 【】 as it is used in this Japanese sentence?",
             "criteria": {"true": "The proposed reading is exactly how a native speaker reads the marked word in this sentence.",
                          "false": "The proposed reading is wrong here: a different word's reading, a mispronunciation, or a wrong sound change (voicing, long vowel, small っ/ゃ/ゅ/ょ)."}}
QUESTIONS = {
    "reading": READING_Q,
    "furigana": READING_Q,
    "translation": {"type": "noul",
                    "instructions": "Does the English accurately convey the meaning of the Japanese sentence? Natural, free translation is fine, but who does what, tense, negation, quantities and the main content must match.",
                    "criteria": {"true": "The English is an accurate translation of the Japanese.",
                                 "false": "The English says something different from the Japanese (wrong content, negation, tense, person, quantity, or a different sentence)."}},
    "control": {"type": "noul", "instructions": "Does this English sentence describe an event that happened in the past?",
                "criteria": {"true": "It reports something that already happened.",
                             "false": "It is a request, a habit, a general fact, or about the future."}},
    "links": {"type": "noul",
              "instructions": "In a Japanese learner's dictionary, the word marked 【】 in the text is linked to linked_entry. Is the marked word really an occurrence of that entry's word (the same lexeme and function), so the link is correct?",
              "criteria": {"true": "The marked word is the linked entry's word, used in one of its senses; the link is correct.",
                           "false": "The marked word is a different word that only looks the same in kana (a homophone, a different particle/function, part of a larger word or set phrase, a different verb's form); the link is wrong."}},
    "flags": {"type": "noul",
              "instructions": "A reviewer model raised this flag on an entry of a Japanese-English learner's dictionary. An editor decides whether to apply it. Is this a real error that should be fixed, rather than a stylistic nitpick, a house-style matter, or a mistaken concern?",
              "criteria": {"true": "Apply: the concern identifies a real inaccuracy or a clear improvement a careful editor would make.",
                           "false": "Reject: the current entry is acceptable; the flag is a nitpick, a matter of style, or factually mistaken."}},
    "conjugation": {"type": "noul",
                    "instructions": "Is proposed_form exactly the correct standard Japanese form of the verb for the named conjugation?",
                    "criteria": {"true": "It is the correct form.",
                                 "false": "It is not a correct form of this verb (wrong verb class, wrong sound change, or wrong form)."}},
    "transitivity": {"type": "choice",
                     "instructions": "Is this Japanese verb (or suru-verb) transitive, intransitive, or both?",
                     "criteria": {"transitive": "Takes a direct object marked with を (acting on something).",
                                  "intransitive": "Takes no を direct object (something happens, or を marks only a place passed through/left).",
                                  "both": "Commonly used both with a を object and without one, in the same sense or closely related senses."}},
}


def question_for(item):
    t = item.get("task_kind") or item["task"]
    if t in ("sense", "meaning"):
        ins = ("Which sense of the headword is used in this sentence?" if t == "sense"
               else "Which English gloss gives the meaning of this Japanese word?")
        return {"type": "choice", "instructions": ins, "criteria": item["senses"]}
    return QUESTIONS[t]


def slug(m):
    return m.replace("/", "__").replace(":", "_").replace("~", "")


def load(task):
    return [json.loads(l) for l in open(HERE / "sets" / f"{task}.jsonl")]


def done_ids(path):
    if not path.exists():
        return set()
    return {json.loads(l)["id"] for l in open(path) if '"error"' not in l}


lock = threading.Lock()


def post(url, body, timeout=120):
    for attempt in range(5):
        t0 = time.time()
        try:
            r = requests.post(url, headers=H, json=body, timeout=timeout)
        except requests.RequestException as ex:
            err = str(ex)
            time.sleep(2 ** attempt)
            continue
        dt = time.time() - t0
        if r.status_code in (429, 500, 502, 503, 504):
            err = f"HTTP {r.status_code} {r.text[:200]}"
            time.sleep(2 ** (attempt + 1))
            continue
        try:
            return r.status_code, r.json(), dt
        except ValueError:
            return r.status_code, {"raw": r.text[:500]}, dt
    return -1, {"error": err}, None


def run_dec(model, task, workers):
    items = load(task)
    out = HERE / "results" / slug(model) / f"{task}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    have = done_ids(out)
    todo = [it for it in items if it["id"] not in have]
    # drop old error lines for retried ids
    if out.exists():
        keep = [l for l in open(out) if '"error"' not in l]
        out.write_text("".join(keep))

    def one(it):
        q = question_for(it)
        state = it["state"]
        if model.startswith("respan/"):  # Respan accepts only a string (or a chat span) as state
            state = json.dumps(state, ensure_ascii=False)
        body = {"model": model, "state": state, "questions": {"q": q}}
        code, js, dt = post("https://openrouter.ai/api/alpha/decisions", body)
        rec = {"id": it["id"], "label": it["label"], "sub": it.get("sub"), "kind": it.get("task_kind"),
               "latency": dt, "code": code}
        ans = (js.get("answers") or {}).get("q") if isinstance(js, dict) else None
        if ans:
            rec["answer"] = ans
            rec["usage"] = js.get("usage")
            rec["served"] = js.get("model")
        else:
            rec["error"] = json.dumps(js, ensure_ascii=False)[:400]
        with lock:
            with open(out, "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return rec

    with ThreadPoolExecutor(workers) as ex:
        res = list(ex.map(one, todo))
    errs = [r for r in res if "error" in r]
    print(f"{model} {task}: {len(res)} run, {len(errs)} errors" + (f" e.g. {errs[0]['error'][:200]}" if errs else ""))


LLM_HEAD = """You are checking data for a Japanese-English learner's dictionary. Answer every numbered item below.

Question for every item: {ins}
{crit}
Return ONLY a JSON array, one object per item, in order: {fmt}
"""


def llm_prompt(batch):
    q = question_for(batch[0])
    if q["type"] == "noul":
        crit = f'Answer "yes" if: {q["criteria"]["true"]}\nAnswer "no" if: {q["criteria"]["false"]}'
        fmt = '{"n": <item number>, "answer": "yes" or "no", "p_yes": <your probability 0-1 that the answer is yes>}'
    else:
        if batch[0]["task"] in ("sense",) or batch[0].get("task_kind") == "meaning":
            crit = "Each item lists its own options; answer with the option key."
        else:
            crit = "Options:\n" + "\n".join(f"- {k}: {v}" for k, v in q["criteria"].items())
        fmt = '{"n": <item number>, "answer": "<option key>", "p": <your probability 0-1 that this answer is right>}'
    lines = [LLM_HEAD.format(ins=q["instructions"], crit=crit, fmt=fmt)]
    for n, it in enumerate(batch, 1):
        st = dict(it["state"])
        if q["type"] == "choice" and "senses" in it:
            st["options"] = it["senses"]
        lines.append(f"{n}. " + json.dumps(st, ensure_ascii=False))
    return "\n".join(lines)


def parse_arr(text):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    i, j = text.find("["), text.rfind("]")
    return json.loads(text[i:j + 1])


def run_llm(model, task, bs, workers, effort=None):
    items = load(task)
    out = HERE / "results" / slug(model) / f"{task}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    have = done_ids(out)
    todo = [it for it in items if it["id"] not in have]
    if out.exists():
        out.write_text("".join(l for l in open(out) if '"error"' not in l))
    groups = {}
    for it in todo:
        groups.setdefault(it.get("task_kind"), []).append(it)
    batches = [g[i:i + bs] for g in groups.values() for i in range(0, len(g), bs)]

    def one(batch):
        body = {"model": model, "messages": [{"role": "user", "content": llm_prompt(batch)}],
                "temperature": 0, "max_tokens": 8000, "usage": {"include": True}}
        if effort:
            body["reasoning"] = {"effort": effort}
        code, js, dt = post("https://openrouter.ai/api/v1/chat/completions", body, timeout=300)
        recs = []
        try:
            txt = js["choices"][0]["message"]["content"]
            arr = {int(a["n"]): a for a in parse_arr(txt)}
            err = None
        except Exception as ex:  # noqa
            arr, err = {}, f"{ex}: {json.dumps(js, ensure_ascii=False)[:300]}"
        usage = js.get("usage", {}) if isinstance(js, dict) else {}
        share = (usage.get("cost") or 0) / len(batch)
        for n, it in enumerate(batch, 1):
            rec = {"id": it["id"], "label": it["label"], "sub": it.get("sub"), "kind": it.get("task_kind"),
                   "latency": dt, "batch_latency": dt, "batch_size": len(batch), "code": code}
            a = arr.get(n)
            if a:
                rec["answer"] = a
                rec["usage"] = {"cost": share, "input_tokens": (usage.get("prompt_tokens") or 0) / len(batch),
                                "output_tokens": (usage.get("completion_tokens") or 0) / len(batch)}
            else:
                rec["error"] = err or "missing item"
            recs.append(rec)
        with lock:
            with open(out, "a") as f:
                for rec in recs:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return recs

    with ThreadPoolExecutor(workers) as ex:
        res = [r for rs in ex.map(one, batches) for r in rs]
    errs = [r for r in res if "error" in r]
    print(f"{model} {task}: {len(res)} run, {len(errs)} errors" + (f" e.g. {errs[0]['error'][:200]}" if errs else ""))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode")
    ap.add_argument("model")
    ap.add_argument("tasks")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--batch", type=int, default=20)
    ap.add_argument("--effort")
    a = ap.parse_args()
    for t in a.tasks.split(","):
        if a.mode == "dec":
            run_dec(a.model, t, a.workers)
        else:
            run_llm(a.model, t, a.batch, a.workers, a.effort)
