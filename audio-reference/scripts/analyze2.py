"""Second-round analysis: how close to zero errors can AI-only checking get?

Without human ratings the true error status of a clip is unknown, so it is
estimated in two ways:

1. Error controls (50 clips with deliberately injected errors): the share of
   known errors each checker misses.
2. A Dawid–Skene latent-class model over all clips: each clip is either
   correct or wrong; each checker has its own sensitivity (share of wrong
   clips it flags) and specificity (share of correct clips it passes); the
   error rate differs per TTS configuration.  Fitted by EM, with the control
   clips clamped to "wrong".  The model assumes checkers err independently
   given the truth; checkers from the same model family are therefore
   collapsed into one vote ("family") before fitting.

The output is, for each clip, the posterior probability that it contains an
error, and for each pipeline (a set of checkers that must all pass) the
expected number of errors among the clips it accepts.

    python analyze2.py                       # prints tables, writes data/summary2.json
"""
import json
import math
from collections import defaultdict

from common import DATA

# checker -> family: checkers in one family share a model lineage and are
# likely to make the same mistakes, so the latent-class model sees one vote
# per family (the family flags if any member does... see FAMILY_RULE).
FAMILY = {
    "kana:google/gemini-3.8-flash": "gemini",
    "kana:google/gemini-3.5-flash": "gemini",
    "kana:google/gemini-3.1-flash-lite": "gemini",
    "kana:~google/gemini-pro-latest": "gemini",
    "choice:google/gemini-3.8-flash": "gemini-choice",
    "compare:google/gemini-3.8-flash": "gemini-compare",
    "kana:openai/gpt-audio-mini": "openai",
    "kana:openai/gpt-audio": "openai",
    "choice:openai/gpt-audio-mini": "openai-choice",
    "compare:openai/gpt-audio-mini": "openai-compare",
    "openai/gpt-transcribe": "openai-stt",
    "qwen/qwen3-asr-flash-2026-02-10": "qwen-stt",
    "kana:qwen/qwen3.8-omni-flash": "qwen",
    "kana:xiaomi/mimo-v2.6-pro": "xiaomi",
    "kana:meta/muse-spark-1.3": "meta",
    "kana:thinkingmachines/inkling": "inkling",
    "kana:mistralai/voxtral-small-24b-2507": "mistral",
}
NORMAL_EXCLUDE = ("control", "furigana_unstructured")


def load():
    ev = json.load(open(DATA / "eval.json"))
    manifest = {}
    for line in open(DATA / "tts_manifest.jsonl"):
        r = json.loads(line)
        if not r.get("error"):
            manifest[r["key"]] = r
    return ev, manifest


def flag(ev, key, m):
    x = ev.get(key, {}).get(m)
    if not x or x["verdict"] == "n/a":
        return None
    return x["verdict"] == "mismatch"


def control_truth(ev, manifest):
    """Control clips whose injected error is really audible: text edits always;
    wrong readings when most kana transcribers heard the injected reading."""
    from controls import WRONG_READINGS
    from evaluate import loose, norm_kana
    wrong = {n: (loose(norm_kana(r)), loose(norm_kana(w))) for n, r, w in WRONG_READINGS}
    truth = {}
    for key, c in manifest.items():
        if c["strategy"] != "control":
            continue
        if c["control_kind"] != "wrong_reading":
            truth[key] = True
            continue
        right, bad = wrong[c["n"]]
        votes = [bad in loose(x["heard"]) and right not in loose(x["heard"])
                 for m, x in ev[key].items() if m.startswith("kana:") and x["verdict"] != "n/a"]
        truth[key] = sum(votes) > len(votes) / 2 if votes else None
    return truth


def control_recall(ev, manifest, truth, checkers):
    rows = {}
    for m in checkers:
        r = {}
        for kind in ("wrong_reading", "text_edit"):
            ks = [k for k, t in truth.items() if t and
                  (manifest[k]["control_kind"] == "wrong_reading") == (kind == "wrong_reading")]
            f = [flag(ev, k, m) for k in ks]
            f = [x for x in f if x is not None]
            r[kind] = [sum(f), len(f)]
        rows[m] = r
    return rows


def dawid_skene(items, labels, strata, n_iter=200):
    """items: {key: {checker: 0/1}}, labels: {key: 1} (clamped), strata: {key: s}.
    Returns posterior {key: P(error)}, sens {c}, spec {c}, prior {s}."""
    checkers = sorted({c for v in items.values() for c in v})
    post = {k: labels.get(k, 0.5 if sum(v.values()) >= 2 else 0.1) for k, v in items.items()}
    for _ in range(n_iter):
        sens, spec, prior = {}, {}, {}
        for c in checkers:
            a = b = d = e = 1.0  # Beta(1,1)-style smoothing
            for k, v in items.items():
                if c in v:
                    p = post[k]
                    a += p * v[c]; b += p * (1 - v[c])
                    d += (1 - p) * (1 - v[c]); e += (1 - p) * v[c]
            sens[c], spec[c] = a / (a + b), d / (d + e)
        by = defaultdict(lambda: [0.5, 1.0])
        for k, s in strata.items():
            if k not in labels:
                by[s][0] += post[k]; by[s][1] += 1
        prior = {s: v[0] / v[1] for s, v in by.items()}
        new = {}
        for k, v in items.items():
            if k in labels:
                new[k] = 1.0
                continue
            pi = prior[strata[k]]
            l1, l0 = math.log(pi), math.log(1 - pi)
            for c, y in v.items():
                l1 += math.log(sens[c] if y else 1 - sens[c])
                l0 += math.log(1 - spec[c] if y else spec[c])
            new[k] = 1 / (1 + math.exp(l0 - l1))
        post = new
    return post, sens, spec, prior


def family_votes(ev, key, checkers):
    """One vote per family: flagged if the majority of its members that ran flag
    (a single member's vote when only one ran)."""
    fam = defaultdict(list)
    for m in checkers:
        f = flag(ev, key, m)
        if f is not None:
            fam[FAMILY.get(m, m)].append(f)
    return {f: int(sum(v) * 2 > len(v)) if len(v) > 1 else int(v[0]) for f, v in fam.items()}


def main(checkers=None, pipelines=None):
    ev, manifest = load()
    all_checkers = sorted({m for e in ev.values() for m in e})
    checkers = checkers or all_checkers
    truth = control_truth(ev, manifest)
    rec = control_recall(ev, manifest, truth, all_checkers)
    print("Control recall (errors caught / known errors):")
    print(f"{'checker':46} {'wrong reading':>14} {'text edit':>10}")
    for m, r in sorted(rec.items(), key=lambda x: -x[1]["wrong_reading"][0]):
        print(f"{m:46} {r['wrong_reading'][0]:>6}/{r['wrong_reading'][1]:<7} {r['text_edit'][0]:>4}/{r['text_edit'][1]}")

    # latent-class model on clips where every chosen checker ran
    items, strata, labels = {}, {}, {}
    for k, c in manifest.items():
        if c["strategy"] == "furigana_unstructured":
            continue
        if c["strategy"] == "control" and not truth.get(k):
            continue
        v = family_votes(ev, k, checkers)
        if len(v) < 2:
            continue
        items[k] = v
        strata[k] = "control" if c["strategy"] == "control" else f"{c['model']}/{c['strategy']}"
        if c["strategy"] == "control":
            labels[k] = 1
    post, sens, spec, prior = dawid_skene(items, labels, strata)
    print(f"\nLatent-class model on {len(items)} clips ({len(labels)} clamped controls)")
    print(f"{'family vote':22} {'sensitivity':>11} {'specificity':>11}")
    for c in sorted(sens):
        print(f"{c:22} {sens[c]:11.3f} {spec[c]:11.3f}")
    print("\nEstimated error rate per TTS configuration:")
    for s, p in sorted(prior.items()):
        if s != "control":
            print(f"  {s:28} {p:6.1%}")
    out = {"control_truth": truth, "control_recall": rec, "sens": sens, "spec": spec,
           "prior": prior, "posterior": post}
    json.dump(out, open(DATA / "summary2.json", "w"), ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    import sys
    main(sys.argv[1:] or None)
