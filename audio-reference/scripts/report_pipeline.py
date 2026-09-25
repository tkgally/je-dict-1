"""How reliable is an AI-only generate → check → regenerate pipeline?

    python report_pipeline.py      # prints report; writes data/report_pipeline.json
                                   # and data/review.json (clips for a human to hear)

The production pipeline (pipeline.py) accepts a clip only when all four
checkers pass it: compare-Gemini, and hiragana transcription by Gemini,
GPT-audio-mini and Inkling (Google, OpenAI, Thinking Machines).

Its reliability is judged by *audit* checkers from other companies (Alibaba
Qwen-Omni, Meta Muse Spark, Mistral Voxtral), plus two related Gemini models
(Pro, 3.5 Flash).  Single audit flags are mostly noise (these models often
"correct" the sentence, write kanji, or drop text), so a clip counts as a
*consensus error* only when two checkers from different families heard the
same deviation: their two transcripts are closer to each other than either is
to the dictionary reading.

1. Natural errors: prompt-A clips with a consensus error among the
   independent audit checkers.  Miss rate = those every pipeline checker passed.
2. Error-injection controls: known errors every pipeline checker passed.
3. Audit of accepted clips: accepted clips with a consensus error
   (independent pair, or independent + related Gemini pair).
4. Review list: for each pipeline, the items left for a human (best attempt)
   plus the audit suspects, plus the natural errors the pipeline missed.
"""
import glob
import itertools
import json

from analyze2 import control_truth, flag, load
from common import DATA, KANJI
from evaluate import distance, loose, norm_kana

PIPE = ["compare:google/gemini-3.8-flash", "kana:google/gemini-3.8-flash",
        "kana:openai/gpt-audio-mini", "kana:thinkingmachines/inkling"]
IND = ["kana:qwen/qwen3.8-omni-flash", "kana:meta/muse-spark-1.3",
       "kana:mistralai/voxtral-small-24b-2507"]
REL = ["kana:~google/gemini-pro-latest", "kana:google/gemini-3.5-flash"]
SENTENCES = {s["n"]: s for s in json.load(open(DATA / "sentences.json"))}


def upper95(k, n):
    """One-sided 95% Clopper–Pearson upper limit for k events in n trials."""
    from math import comb
    if n == 0:
        return 1.0
    cdf = lambda p: sum(comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k + 1))
    lo, hi = k / n, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if cdf(mid) > 0.05 else (lo, mid)
    return hi


def heard_kana(ev, key, m):
    x = ev.get(key, {}).get(m)
    if not x or x["verdict"] != "mismatch" or KANJI.search(x["text"]) or not x["heard"]:
        return None
    return loose(x["heard"])


def agreeing(ev, manifest, key, group, other=None):
    """Pairs of checkers that heard the same deviation.  With `other`, only
    pairs with one checker from each group."""
    s = SENTENCES[manifest[key]["n"]]
    exp = [loose(norm_kana(t)) for t in [s["kana"], *s["alt_kana"]]]
    ms = group + (other or [])
    pairs = []
    for a, b in itertools.combinations(ms, 2):
        if other is not None and (a in group) == (b in group):
            continue
        ta, tb = heard_kana(ev, key, a), heard_kana(ev, key, b)
        if ta is None or tb is None:
            continue
        if distance(ta, tb) < min(min(distance(ta, e), distance(tb, e)) for e in exp):
            pairs.append([a, b])
    return pairs


def natural_miss(ev, manifest):
    plain = [k for k, c in manifest.items() if c["strategy"] == "plain"]
    wrong = [k for k in plain if agreeing(ev, manifest, k, IND)]
    per = {m: sum(flag(ev, k, m) is False for k in wrong) for m in PIPE}
    missed = [k for k in wrong if not any(flag(ev, k, m) for m in PIPE)]
    return {"wrong": len(wrong), "per_checker_missed": per, "missed": missed}


def control_miss(ev, manifest):
    truth = control_truth(ev, manifest)
    known = [k for k, t in truth.items() if t]
    return {"known_errors": len(known),
            "missed": [k for k in known if not any(flag(ev, k, m) for m in PIPE)]}


def summary_diffs(ev, key, ms):
    return {m: ev[key][m]["diff"][:3] for m in ms if flag(ev, key, m)}


PIPE_V2 = ["pcompare:google/gemini-3.8-flash"] + PIPE[1:]


def rejects_v2(ev, key):
    """The v2 rule: particle-aware compare objects, or 2+ of the 3 kana transcribers do."""
    p = flag(ev, key, PIPE_V2[0])
    return p is not False or sum(flag(ev, key, m) is not False for m in PIPE_V2[1:]) >= 2


def control_miss_v2(ev, manifest):
    truth = control_truth(ev, manifest)
    known = [k for k, t in truth.items() if t and k in ev and PIPE_V2[0] in ev[k]]
    return {"known_errors": len(known), "missed": [k for k in known if not rejects_v2(ev, k)]}


def audit_pipeline(ev, manifest, path):
    p = json.load(open(path))
    rs = p["results"]
    acc = [r["accepted"] for r in rs if r["accepted"]]
    suspects = []
    # the independent audit was wrong every time the user checked it
    # (ratings of 2026-09-25), so it is not applied to the v2 pipelines
    for k in (acc if p.get("rule", "any") == "any" else []):
        pairs = agreeing(ev, manifest, k, IND) + agreeing(ev, manifest, k, IND, REL)
        if pairs:
            suspects.append({"key": k, "pairs": pairs, "heard": summary_diffs(ev, k, IND + REL)})
    escalated = []
    for r in rs:
        if r["accepted"]:
            continue
        tried = [a for a in r["attempts"] if "verdicts" in a]
        # best attempt: fewest pipeline flags
        best = min(tried, key=lambda a: sum(v != "match" for v in a["verdicts"].values()))
        escalated.append({"key": best["key"], "attempts": len(r["attempts"]),
                          "heard": summary_diffs(ev, best["key"], list(best["verdicts"]))})
    return {
        "file": path.split("/")[-1], "strategy": p["strategy"], "rule": p.get("rule", "any"),
        "model": rs[0]["model"], "items": len(rs),
        "passed_first": sum(r["attempts"][0].get("pass", False) for r in rs),
        "accepted": len(acc), "clips_generated": sum(len(r["attempts"]) for r in rs),
        "escalated": escalated, "suspects": suspects,
    }


def main():
    ev, manifest = load()
    nat, ctl = natural_miss(ev, manifest), control_miss(ev, manifest)
    k, n = len(nat["missed"]), nat["wrong"]
    print(f"Natural errors (prompt A; 2+ independent checkers heard the same deviation): {n}")
    for m, x in nat["per_checker_missed"].items():
        print(f"  {m:40} missed {x}/{n}")
    print(f"  PIPELINE missed {k}/{n} (95% upper bound {upper95(k, n):.1%})")
    for key in nat["missed"]:
        print("     ", key, summary_diffs(ev, key, IND))
    kc = len(ctl["missed"])
    print(f"Controls: pipeline missed {kc}/{ctl['known_errors']} known injected errors "
          f"(95% upper bound {upper95(kc, ctl['known_errors']):.1%})")
    c2 = control_miss_v2(ev, manifest)
    print(f"Controls, v2 rule: missed {len(c2['missed'])}/{c2['known_errors']} "
          f"(95% upper bound {upper95(len(c2['missed']), c2['known_errors']):.1%}) {c2['missed']}")
    reports, review = [], []
    for path in sorted(glob.glob(str(DATA / "pipeline_*.json"))):
        a = audit_pipeline(ev, manifest, path)
        reports.append(a)
        print(f"\n{a['file']}: {a['items']} items; passed first time {a['passed_first']}; "
              f"accepted {a['accepted']} after {a['clips_generated']} clips; "
              f"left for a human {len(a['escalated'])}; audit suspects {len(a['suspects'])}")
        for s in a["suspects"]:
            print("     suspect", s["key"], s["heard"])
        name = a["file"][len("pipeline_"):-len(".json")]
        for e in a["escalated"]:
            review.append({"pipeline": name, "key": e["key"], "reason": "escalated",
                           "note": f"failed the checks in all {e['attempts']} attempts; best attempt shown",
                           "heard": e["heard"]})
        if a["rule"] == "p2":  # optional spot-check: accepted although one transcriber objected
            for k in [r["accepted"] for r in json.load(open(path))["results"] if r["accepted"]]:
                objecting = [m for m in PIPE_V2[1:] if flag(ev, k, m)]
                if len(objecting) == 1:
                    review.append({"pipeline": name + "_spot", "key": k, "reason": "spotcheck",
                                   "note": "accepted (the particle-aware compare passed it), but one transcriber objected",
                                   "heard": summary_diffs(ev, k, objecting)})
        for s in a["suspects"]:
            review.append({"pipeline": name, "key": s["key"], "reason": "audit",
                           "note": "accepted by the pipeline, but two audit checkers heard the same deviation",
                           "heard": s["heard"]})
    for key in nat["missed"]:
        review.append({"pipeline": "calibration", "key": key, "reason": "calibration",
                       "note": "prompt A clip: the pipeline checkers and the independent checkers disagree",
                       "heard": {**summary_diffs(ev, key, IND), **summary_diffs(ev, key, PIPE)}})
    order = {"kanadict_flash_v2": 0, "kanadict_flash_v2_spot": 1, "kanadict_lite_v2_spot": 2}
    review.sort(key=lambda r: order.get(r["pipeline"], 9))
    json.dump({"natural": nat, "controls": ctl, "controls_v2": c2, "pipelines": reports},
              open(DATA / "report_pipeline.json", "w"), ensure_ascii=False, indent=1)
    json.dump(review, open(DATA / "review.json", "w"), ensure_ascii=False, indent=1)
    print(f"\n{len(review)} clips in data/review.json")


if __name__ == "__main__":
    main()
