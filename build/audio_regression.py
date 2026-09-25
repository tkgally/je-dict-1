#!/usr/bin/env python3
"""Rerun the audio checks on the 163 regression clips with known answers.

    python3 build/audio_regression.py                 # current audio/config.json checkers + rule
    python3 build/audio_regression.py --kbps 32       # re-encode each clip first (bit-rate test)
    python3 build/audio_regression.py --tag "new pcompare model"

The clips (audio/regression/*.mp3, listed in index.json) are:
  - 50 with deliberately injected errors (wrong reading forced through kana;
    omitted, substituted, inserted, repeated words). 6 are inaudible: the TTS
    "corrected" them (index field "audible": false).
  - 113 rated by Tom by ear: 3 errors ("err"), 2 unsure, the rest correct.

Pass criteria for any workflow change (AUDIO_WORKFLOW.md §10): every audible
injected error and every one of Tom's errors is rejected, and the false-alarm
rate on the clips Tom rated correct does not rise much (v2 baseline in the
workflow's "What was validated").

Writes audio/regression/last_run.json (every verdict and transcript) and
appends one summary line to audio/regression/history.jsonl. Cost: about $0.30.
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audio_checks import accept, checker_name, run_checkers  # noqa: E402
from audio_text import loose, norm_kana  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "audio" / "regression"
TESTSET = ROOT / "audio" / "testset" / "sentences.json"
CONFIG = ROOT / "audio" / "config.json"


def truth_of(clip):
    """('injected', kind, detail) or ('human', rating, comment)."""
    t = clip["truth"]
    head, _, rest = t.partition(":")
    rest = rest.strip()
    if head == "injected error":
        kind, _, detail = rest.partition(" ")
        return "injected", kind, detail
    rating, _, comment = rest.partition(" - ")
    return "human", rating.strip(), comment


def reencode(mp3, kbps):
    import miniaudio
    from audio_api import encode_mp3
    d = miniaudio.decode(mp3, output_format=miniaudio.SampleFormat.SIGNED16,
                         nchannels=1, sample_rate=24000)
    return encode_mp3(d.samples.tobytes(), kbps)


def heard_injected(clip, results):
    """For a wrong-reading control: did most kana transcribers hear the injected
    reading (and not the right one)? Used to decide audibility when the index
    does not record it."""
    detail = truth_of(clip)[2]
    right, _, wrong = detail.partition(" → ")
    right, wrong = loose(norm_kana(right)), loose(norm_kana(wrong))
    votes = []
    for r in results:
        if r["name"].startswith("kana:") and r["verdict"] != "n/a":
            h = loose(norm_kana(r["text"]))
            votes.append(wrong in h and right not in h)
    return sum(votes) > len(votes) / 2 if votes else None


def summarize(rows, cfg):
    out = {"injected_audible": [0, 0], "injected_inaudible_rejected": [0, 0],
           "human_err": [0, 0], "human_ok_false_alarms": [0, 0], "human_unsure_rejected": [0, 0],
           "misses": [], "false_alarms": []}
    objections = Counter()
    for row in rows:
        rejected = not row["accepted"]
        for r in row["checks"]:
            if r["verdict"] != "match":
                objections[r["name"]] += 1
        cat, label, _ = row["truth_parsed"]
        if cat == "injected":
            if row.get("audible") is False:
                key = "injected_inaudible_rejected"
            else:
                key = "injected_audible"
                if not rejected:
                    out["misses"].append(row["key"])
            out[key][0] += rejected
            out[key][1] += 1
        elif label == "err":
            out["human_err"][0] += rejected
            out["human_err"][1] += 1
            if not rejected:
                out["misses"].append(row["key"])
        elif label == "ok":
            out["human_ok_false_alarms"][0] += rejected
            out["human_ok_false_alarms"][1] += 1
            if rejected:
                out["false_alarms"].append(row["key"])
        else:
            out["human_unsure_rejected"][0] += rejected
            out["human_unsure_rejected"][1] += 1
    out["objections_per_checker"] = dict(objections)
    out["passed"] = (out["injected_audible"][0] == out["injected_audible"][1]
                     and out["human_err"][0] == out["human_err"][1])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--kbps", type=int, help="re-encode each clip at this bit rate first")
    ap.add_argument("--limit", type=int, help="first N clips only (smoke test)")
    ap.add_argument("--tag", default="", help="note stored with the summary")
    ap.add_argument("--no-write", action="store_true", help="print only")
    ap.add_argument("--freeze-audibility", action="store_true",
                    help="write the audibility decided by this run into index.json "
                         "for injected clips that lack it")
    args = ap.parse_args()

    from audio_api import OpenRouter
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    sentences = {s["n"]: s for s in json.loads(TESTSET.read_text(encoding="utf-8"))}
    index = json.loads((REG / "index.json").read_text(encoding="utf-8"))
    clips = index[: args.limit] if args.limit else index
    api = OpenRouter()

    def one(clip):
        mp3 = (REG / clip["file"]).read_bytes()
        if args.kbps:
            mp3 = reencode(mp3, args.kbps)
        s = sentences[clip["n"]]
        checks = run_checkers(mp3, s, cfg["checkers"], api)
        row = {"key": clip["key"], "truth": clip["truth"], "truth_parsed": truth_of(clip),
               "checks": checks, "accepted": accept(cfg["rule"], [c["verdict"] for c in checks])}
        if row["truth_parsed"][0] == "injected":
            row["audible"] = clip.get("audible")
            if row["audible"] is None and row["truth_parsed"][1] == "wrong_reading":
                row["audible"] = heard_injected(clip, checks)
                row["audible_decided_now"] = True
            elif row["audible"] is None:
                row["audible"] = True  # text edits are always audible
        return row

    with ThreadPoolExecutor(args.workers) as pool:
        rows = list(pool.map(one, clips))

    summ = summarize(rows, cfg)
    ia, he, fa = summ["injected_audible"], summ["human_err"], summ["human_ok_false_alarms"]
    print(f"Checkers: {', '.join(checker_name(c) for c in cfg['checkers'])}; rule {cfg['rule']}"
          + (f"; clips re-encoded at {args.kbps} kbps" if args.kbps else ""))
    print(f"Audible injected errors caught : {ia[0]}/{ia[1]}")
    print(f"Inaudible injected, rejected   : {summ['injected_inaudible_rejected'][0]}/"
          f"{summ['injected_inaudible_rejected'][1]} (no requirement)")
    print(f"Tom's errors caught            : {he[0]}/{he[1]}")
    print(f"False alarms on Tom's correct  : {fa[0]}/{fa[1]}")
    print(f"Unsure clips rejected          : {summ['human_unsure_rejected'][0]}/"
          f"{summ['human_unsure_rejected'][1]}")
    print(f"Objections per checker         : {summ['objections_per_checker']}")
    for k in summ["misses"]:
        print("  MISSED     ", k)
    for k in summ["false_alarms"]:
        print("  false alarm", k)
    print(f"Cost: ${api.spent:.3f}")
    print("PASS" if summ["passed"] else "FAIL: the workflow change must not go into production")

    if args.freeze_audibility:
        by_key = {r["key"]: r for r in rows}
        for clip in index:
            r = by_key.get(clip["key"])
            if r and r.get("audible_decided_now"):
                clip["audible"] = bool(r["audible"])
        (REG / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n",
                                        encoding="utf-8")
        print("audibility written to index.json")

    if not args.no_write:
        stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        cfg_hash = hashlib.sha256(json.dumps(
            {k: cfg[k] for k in ("checkers", "rule")}, sort_keys=True).encode()).hexdigest()[:12]
        (REG / "last_run.json").write_text(json.dumps(
            {"at": stamp, "config": {k: cfg[k] for k in ("checkers", "rule")},
             "kbps": args.kbps, "rows": rows}, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
        line = {"at": stamp, "tag": args.tag, "checkers_rule_hash": cfg_hash,
                "kbps": args.kbps, "clips": len(rows), "passed": summ["passed"],
                "injected_audible_caught": ia, "human_err_caught": he,
                "human_ok_false_alarms": fa, "misses": summ["misses"],
                "false_alarms": summ["false_alarms"],
                "objections_per_checker": summ["objections_per_checker"],
                "cost_usd": round(api.spent, 4)}
        with open(REG / "history.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    return 0 if summ["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
