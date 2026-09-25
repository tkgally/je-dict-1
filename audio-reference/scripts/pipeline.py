"""Generate → check → regenerate loop (the production pipeline being tested).

    python pipeline.py --strategy kanadict_noread --checkers kana:google/gemini-3.8-flash ... --tries 5

For every sentence × TTS model × voice, the existing clip for the strategy is
checked by every production checker.  If any checker flags it (or cannot give
a verdict), the clip is regenerated with the same prompt (Gemini TTS output
differs from call to call) and checked again, up to --tries attempts in all.
Sentences that never pass are left for a human.  Retries are stored as
strategy "<strategy>~r<attempt>" and are part of the normal manifest, so all
other scripts see them.  Result: data/pipeline_<strategy>_<models><tag>.json.

--rule any (first version): every checker must pass.
--rule p2 (after the user's ratings): the first checker (particle-aware
compare) must pass, and at most one of the others may object."""
import argparse
import json
from concurrent.futures import ThreadPoolExecutor

from common import DATA, TTS_MODELS, VOICES
from evaluate import check_record
from generate_tts import MANIFEST, load_manifest, synth
from prompts import build_prompt
from transcribe import STT_DIR, slug
import transcribe
import verify

SENTENCES = {s["n"]: s for s in json.load(open(DATA / "sentences.json"))}


def run_checker(checker, key, s):
    """Run one checker on one clip (cached in data/stt); return verdict."""
    mode, _, model = checker.partition(":")
    if mode in ("choice", "compare", "pcompare"):
        path = STT_DIR / f"{mode}_{slug(model)}.jsonl"
    else:
        path, model = STT_DIR / f"{slug(checker)}.jsonl", checker
    if path.exists():
        for line in open(path):
            r = json.loads(line)
            if r["key"] == key and "text" in r:
                return check_record(s, r["model"], r)["verdict"]
    for _ in range(3):
        if mode in ("choice", "compare", "pcompare"):
            rec = verify.run_one(mode, model, key, s, "pipeline")
        else:
            rec = transcribe.run_one(model, key, "ja", "pipeline")
        if not rec.get("error"):
            break
    if rec.get("error"):
        return "n/a"
    with open(path, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return check_record(s, rec["model"], rec)["verdict"]


def passes(rule, checkers, verdicts, s):
    """any: every checker must say "match" (a choice checker's "n/a" on a
    sentence without ambiguous words counts as a pass).
    p2: the first checker (particle-aware compare) must say "match", and fewer
    than two of the others may object ("n/a" counts as an objection)."""
    if rule == "p2":
        first, rest = checkers[0], checkers[1:]
        return verdicts[first] == "match" and sum(verdicts[c] != "match" for c in rest) < 2
    no_items = not verify.choice_items(s)
    return all(vd == "match" or (vd == "n/a" and c.startswith("choice:") and no_items)
               for c, vd in verdicts.items())


def one(args, m, v, n):
    """A clip passes when every checker says "match".  A choice checker has no
    verdict ("n/a") on sentences without ambiguous words, which counts as a
    pass; any other missing verdict counts as a failure."""
    s = SENTENCES[n]
    attempts = []
    for t in range(args.tries):
        st = args.strategy if t == 0 else f"{args.strategy}~r{t}"
        key = f"{m}/{st}/{v}/{n:03d}_{s['id']}"
        if key not in DONE:
            rec = synth({"key": key, "model": m, "strategy": st, "voice": v, "n": n,
                         "id": s["id"], "prompt": build_prompt(args.strategy, s)}, "pipeline-tts")
            with open(MANIFEST, "a") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if rec.get("error"):
                attempts.append({"key": key, "error": rec["error"]})
                continue
        verdicts = {c: run_checker(c, key, s) for c in args.checkers}
        ok = passes(args.rule, args.checkers, verdicts, s)
        attempts.append({"key": key, "verdicts": verdicts, "pass": ok})
        if ok:
            return {"model": m, "voice": v, "n": n, "accepted": key, "attempts": attempts}
    return {"model": m, "voice": v, "n": n, "accepted": None, "attempts": attempts}


def main():
    global DONE
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", required=True)
    ap.add_argument("--checkers", nargs="+", required=True)
    ap.add_argument("--tries", type=int, default=5)
    ap.add_argument("--rule", choices=["any", "p2"], default="any")
    ap.add_argument("--tag", default="", help="suffix for the result file name")
    ap.add_argument("--models", nargs="+", default=list(TTS_MODELS))
    ap.add_argument("--voices", nargs="+", default=list(VOICES))
    ap.add_argument("--workers", type=int, default=16)
    args = ap.parse_args()
    bad = [c for c in args.checkers if " " in c]
    if bad:
        ap.error(f"malformed checker names: {bad}")
    DONE = load_manifest()
    jobs = [(m, v, n) for m in args.models for v in args.voices for n in sorted(SENTENCES)]
    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(lambda j: one(args, *j), jobs))
    out = {"strategy": args.strategy, "checkers": args.checkers, "tries": args.tries,
           "rule": args.rule,
           "results": results}
    json.dump(out, open(DATA / f"pipeline_{args.strategy}_{'+'.join(args.models)}{args.tag}.json", "w"), ensure_ascii=False, indent=1)
    for m in args.models:
        rs = [r for r in results if r["model"] == m]
        first = sum(r["attempts"][0].get("pass", False) for r in rs)
        acc = sum(r["accepted"] is not None for r in rs)
        tries = sum(len(r["attempts"]) for r in rs)
        print(f"{m}: {first}/{len(rs)} passed first time, {acc}/{len(rs)} accepted within "
              f"{args.tries} tries, {tries} clips generated, {len(rs) - acc} left for a human")


DONE = {}
if __name__ == "__main__":
    main()
