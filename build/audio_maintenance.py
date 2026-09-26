#!/usr/bin/env python3
"""Keeping the example-audio workflow correct over time (AUDIO_WORKFLOW.md §10).

    python3 build/audio_maintenance.py due                # what is due; exit 2 if production is blocked
    python3 build/audio_maintenance.py check-models       # configured model IDs alive? newer candidates?
    python3 build/audio_maintenance.py drift              # first-pass rate and cost of recent runs vs baseline
    python3 build/audio_maintenance.py spotcheck --n 30   # build a listening page for Tom (risky clips first)
    python3 build/audio_maintenance.py import-ratings F   # Tom's exported ratings → regression suite, re-records
    python3 build/audio_maintenance.py reaudit --sample 100 --budget 0.50   # re-check existing recordings

Blocking (production must not run until done):
  - the checkers or rule changed since the last passing regression run
    (audio/regression/history.jsonl) → run build/audio_regression.py;
  - the TTS model, prompt or bit rate changed since the last test-set pilot of
    a production voice (audio/pilots.jsonl) → run audio_pipeline.py testset.
Due, not blocking: regression older than 90 days, model check older than 30,
spot check (30 days and 200 new recordings), re-audit (90 days and 500
recordings), re-evaluation of models and prompts (120 days).
State: audio/maintenance.json (dates of the last check of each kind).
"""
import argparse
import hashlib
import json
import random
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio_pipeline as P  # noqa: E402
from audio_text import parse_example  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "audio"
STATE = AUDIO / "maintenance.json"
PILOTS = AUDIO / "pilots.jsonl"
REG_HISTORY = AUDIO / "regression" / "history.jsonl"
REG_INDEX = AUDIO / "regression" / "index.json"
REAUDITS = AUDIO / "reaudits.jsonl"
CURATOR = ROOT / "reviews" / "needs_curator.txt"

INTERVALS = {"regression": 90, "models": 30, "spotcheck": 30, "reaudit": 90, "reevaluate": 120}
MIN_NEW = {"spotcheck": 200, "reaudit": 500}


def today():
    return datetime.now(timezone.utc).date()


def load_state():
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_state(st):
    st["_doc"] = ("Dates of the last maintenance task of each kind (build/audio_maintenance.py). "
                  "Updated by the tool; edit only to record a task done by hand.")
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def days_since(iso):
    if not iso:
        return 10 ** 6
    return (today() - date.fromisoformat(iso[:10])).days


def checks_fingerprint(cfg):
    return hashlib.sha256(json.dumps({k: cfg[k] for k in ("checkers", "rule")},
                                     sort_keys=True).encode()).hexdigest()[:12]


def generation_fingerprint(cfg):
    return hashlib.sha256(json.dumps({k: cfg[k] for k in ("tts_model", "prompt_strategy", "mp3_kbps")},
                                     sort_keys=True).encode()).hexdigest()[:12]


def jsonl(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def last_passing_regression(cfg):
    fp = checks_fingerprint(cfg)
    runs = [r for r in jsonl(REG_HISTORY) if r.get("checkers_rule_hash") == fp and r.get("passed")
            and not r.get("kbps") and r.get("clips", 0) >= 150]
    return runs[-1] if runs else None


def pilot_acceptable(p, cfg):
    """A pilot passes when its first-take rate is within 8 points of the
    config baseline and at least 97 of 100 sentences were accepted. Judged
    against the current baseline, so a corrected baseline applies to old pilots."""
    base = cfg.get("baseline", {}).get("first_pass_rate", 0.9)
    return p.get("first_pass_rate", 0) >= base - 0.08 and p.get("accepted_rate", 0) >= 0.97


def pilots_for(cfg):
    fp = generation_fingerprint(cfg)
    return [p for p in jsonl(PILOTS) if p.get("generation_fingerprint") == fp
            and p.get("checks_fingerprint") == checks_fingerprint(cfg)]


def due_tasks(cfg=None, st=None):
    """[(task, blocking, reason)]"""
    cfg = cfg or P.load_config()
    st = st if st is not None else load_state()
    out = []
    reg = last_passing_regression(cfg)
    if not reg:
        out.append(("regression", True, "no passing regression run for the current checkers and rule"))
    elif days_since(reg["at"]) >= INTERVALS["regression"]:
        out.append(("regression", False, f"last passing regression run {days_since(reg['at'])} days ago"))
    piloted = {p["voice"] for p in pilots_for(cfg) if pilot_acceptable(p, cfg)}
    missing = [v for v in cfg["voices"] if v not in piloted]
    if missing:
        out.append(("pilot", True, "no acceptable test-set pilot for the current TTS model, prompt, "
                    f"bit rate and checkers with voice(s) {', '.join(missing)}"))
    if days_since(st.get("models")) >= INTERVALS["models"]:
        out.append(("models", False, "configured model IDs not checked for 30 days"))
    recorded = len(P.load_manifest())
    for task in ("spotcheck", "reaudit"):
        since = recorded - int(st.get(f"{task}_records", 0))
        if days_since(st.get(task)) >= INTERVALS[task] and since >= MIN_NEW[task]:
            out.append((task, False, f"{since} recordings since the last {task}"))
    if days_since(st.get("reevaluate")) >= INTERVALS["reevaluate"]:
        out.append(("reevaluate", False, "models and prompts not re-evaluated for 120 days"))
    return out


def production_blocked(cfg=None):
    return [t for t in due_tasks(cfg) if t[1]]


def cmd_due(args):
    tasks = due_tasks()
    print(json.dumps([{"task": t, "blocking": b, "reason": r} for t, b, r in tasks],
                     ensure_ascii=False, indent=2))
    return 2 if any(b for _, b, _ in tasks) else 0


# --------------------------------------------------------------------------- models
def cmd_check_models(args):
    import requests
    cfg = P.load_config()
    api = "https://openrouter.ai/api/v1"
    wanted = [cfg["tts_model"]] + [c["model"] for c in cfg["checkers"]]
    alive, dead = [], []
    for m in dict.fromkeys(wanted):
        r = requests.get(f"{api}/models/{m}/endpoints", timeout=30)
        ok = r.ok and (r.json().get("data") or {}).get("endpoints")
        (alive if ok else dead).append(m)
    listing = requests.get(f"{api}/models", timeout=60).json().get("data", [])
    audio_in = sorted(m["id"] for m in listing
                      if "audio" in (m.get("architecture") or {}).get("input_modalities", [])
                      and m["id"] not in wanted and not m["id"].endswith(":free"))
    speech = requests.get(f"{api}/models", params={"output_modalities": "speech"}, timeout=60)
    tts_like = sorted({m["id"] for m in speech.json().get("data", [])} - set(wanted)) if speech.ok else []
    st = load_state()
    known = set(st.get("known_models", []))
    new = [m for m in audio_in + tts_like if m not in known] if known else []
    st["known_models"] = sorted(known | set(audio_in) | set(tts_like))
    st["models"] = today().isoformat()
    save_state(st)
    out = {"alive": alive, "dead": dead,
           "new_since_last_check": new,
           "other_audio_input_models": audio_in, "other_tts_models": tts_like}
    print(json.dumps(out, indent=2))
    if dead:
        print("A configured model is gone: production must stop until the workflow is updated "
              "(regression suite + pilot) — flag it for Tom.")
        return 1
    return 0


# --------------------------------------------------------------------------- drift
def cmd_drift(args):
    runs = jsonl(P.RUNS)
    if not runs:
        print("no production runs yet")
        return 0
    recent = runs[-args.last:]
    ex = sum(r["examples"] for r in recent)
    fp = sum(r["first_pass"] for r in recent) / max(1, ex)
    nh = sum(r["needs_human"] for r in recent) / max(1, ex)
    cost = sum(r["cost_usd"] for r in recent) / max(1, sum(r["accepted"] for r in recent))
    base = P.load_config().get("baseline", {})
    warn = []
    if fp < base.get("first_pass_rate", 0.9) - 0.08:
        warn.append(f"first-pass rate {fp:.1%} is well below the baseline {base.get('first_pass_rate'):.0%}")
    if nh > max(0.02, 2 * base.get("needs_human_rate", 0.01)):
        warn.append(f"left-for-human rate {nh:.1%} is high")
    if cost > 1.5 * base.get("cost_per_accepted_usd", 0.003):
        warn.append(f"cost per accepted clip ${cost:.4f} is 1.5× the baseline")
    print(json.dumps({"runs": len(recent), "examples": ex, "first_pass_rate": round(fp, 3),
                      "needs_human_rate": round(nh, 3), "cost_per_accepted_usd": round(cost, 5),
                      "warnings": warn}, indent=2))
    return 1 if warn else 0


# --------------------------------------------------------------------------- spot check
def risk_score(rec):
    return (2 * len(rec.get("obj", [])) + (rec.get("n", 1) - 1))


def cmd_spotcheck(args):
    """Choose clips accepted since the last spot check, riskiest first, and
    write a listening page (to be published in the audio repository)."""
    from audio_review_page import make_page
    cfg = P.load_config()
    st = load_state()
    since = st.get("spotcheck", "0000-00-00")
    manifest = P.load_manifest()
    stores = {s["id"]: s["base_url"] for s in cfg["stores"]}
    examples = {x["ex"]: x for x in P.load_examples()}
    recent = [r for r in manifest.values() if r.get("at", "")[:10] > since and r["ex"] in examples
              and P.short_hash(examples[r["ex"]]["raw"]) == r["h"]]
    rng = random.Random(args.seed or today().isoformat())
    risky = sorted([r for r in recent if risk_score(r) > 0], key=lambda r: -risk_score(r))
    plain = [r for r in recent if risk_score(r) == 0]
    rng.shuffle(plain)
    n_risky = min(len(risky), args.n * 2 // 3)
    chosen = risky[:n_risky] + plain[:args.n - n_risky]
    clips = []
    for r in chosen:
        p = parse_example(examples[r["ex"]]["raw"])
        reason = (f"a checker objected ({', '.join(r['obj'])})" if r.get("obj") else "") + \
                 (f"; accepted on attempt {r['n']}" if r.get("n", 1) > 1 else "")
        clips.append({"key": r["ex"], "text": p["plain"], "reading": p["kana"],
                      "src": stores[r["s"]] + r["f"],
                      "meta": f"{r['ex']} · {r['v']} · {r['at']}" + (f" · {reason.strip('; ')}" if reason else "")})
    page_id = f"spotcheck-{today().isoformat()}"
    intro = ("<p>Recordings the dictionary accepted since the last spot check, the riskiest first "
             "(a checker objected, or it took more than one attempt), then a random sample.</p>"
             "<p>Listen to each and mark ✓ correct, ✗ wrong (any misread, missing, added or repeated "
             "word) or ? unsure; a comment helps with ✗. Then press <b>Download ratings</b> and "
             "upload the file to je-dict-1 at <code>audio/spotchecks/</code> (GitHub: Add file → "
             "Upload files). The next audio run adds your verdicts to the regression suite and "
             "re-records anything you marked wrong.</p>")
    out = P.WORK / "review" / f"{page_id}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(make_page(page_id, f"Audio spot check {today().isoformat()}", intro, [(None, clips)]),
                   encoding="utf-8")
    st["spotcheck"] = today().isoformat()
    st["spotcheck_records"] = len(manifest)
    save_state(st)
    print(json.dumps({"page": str(out.relative_to(ROOT)), "clips": len(clips), "risky": n_risky,
                      "publish_as": f"review/{page_id}.html"}, indent=2))


# --------------------------------------------------------------------------- ratings
def cmd_import_ratings(args):
    """Tom's ratings of production clips → regression suite (by URL); a clip
    marked wrong loses its manifest line, so the next run records it again."""
    cfg = P.load_config()
    stores = {s["id"]: s["base_url"] for s in cfg["stores"]}
    manifest = P.load_manifest()
    index = json.loads(REG_INDEX.read_text(encoding="utf-8"))
    known = {c["key"] for c in index}
    tests = {s["id"]: s for s in json.loads(P.TESTSET.read_text(encoding="utf-8"))}
    examples = {x["ex"]: x for x in P.load_examples()}
    added, wrong, skipped = 0, [], 0
    for path in args.files:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        for key, v in (data.get("ratings") or {}).items():
            r = (v or {}).get("r")
            rec = manifest.get(key)
            if not r or not rec or key not in examples:
                skipped += 1
                continue
            clip_key = f"production/{rec['f']}"
            if clip_key not in known:
                p = parse_example(examples[key]["raw"])
                index.append({"key": clip_key, "url": stores[rec["s"]] + rec["f"], "voice": rec["v"],
                              "example_id": key, "raw": examples[key]["raw"],
                              "truth": f"human: {r}" + (f" - {v['c']}" if v.get("c") else ""),
                              "source": data.get("page")})
                known.add(clip_key)
                added += 1
            if r == "err":
                wrong.append(key)
    REG_INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if wrong:
        drop_manifest(wrong)
    for path in args.files:  # file the imported ratings
        src = Path(path)
        dest = AUDIO / "spotchecks" / "imported" / src.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.resolve() != dest.resolve():
            src.rename(dest)
    print(json.dumps({"added_to_regression": added, "marked_wrong_rerecord": wrong,
                      "skipped": skipped}, ensure_ascii=False, indent=2))
    if wrong:
        print("Tom heard an error the checks passed: log it in the AUDIO_WORKFLOW.md changelog and "
              "rerun build/audio_regression.py (the new clips must be caught).")


def drop_manifest(ex_ids):
    ids = set(ex_ids)
    for f in sorted(P.MANIFEST_DIR.glob("*.jsonl")):
        lines = f.read_text(encoding="utf-8").splitlines()
        keep = [l for l in lines if l.strip() and json.loads(l)["ex"] not in ids]
        if len(keep) != len([l for l in lines if l.strip()]):
            f.write_text("".join(l + "\n" for l in keep), encoding="utf-8")


# --------------------------------------------------------------------------- re-audit
def cmd_reaudit(args):
    """Re-check a random sample of valid recordings with the current checkers.
    A rejected clip loses its manifest line (re-recorded by the next run)."""
    import requests
    from concurrent.futures import ThreadPoolExecutor
    from audio_api import OpenRouter
    from audio_checks import accept, run_checkers
    cfg = P.load_config()
    stores = {s["id"]: s["base_url"] for s in cfg["stores"]}
    manifest = P.load_manifest()
    examples = {x["ex"]: x for x in P.load_examples()}
    valid = [r for r in manifest.values() if r["ex"] in examples
             and P.short_hash(examples[r["ex"]]["raw"]) == r["h"]]
    rng = random.Random(args.seed or today().isoformat())
    sample = rng.sample(valid, min(args.sample, len(valid)))
    api = OpenRouter()

    def one(r):
        if api.spent > args.budget:
            return None
        mp3 = requests.get(stores[r["s"]] + r["f"], timeout=60).content
        checks = run_checkers(mp3, parse_example(examples[r["ex"]]["raw"]), cfg["checkers"], api)
        return {"ex": r["ex"], "f": r["f"], "accepted": accept(cfg["rule"], [c["verdict"] for c in checks]),
                "verdicts": {c["name"]: c["verdict"] for c in checks},
                "diffs": {c["name"]: c["diff"] for c in checks if c["diff"]}}

    with ThreadPoolExecutor(8) as pool:
        res = [x for x in pool.map(one, sample) if x]
    rejected = [x for x in res if not x["accepted"]]
    if rejected and not args.dry_run:
        drop_manifest([x["ex"] for x in rejected])
    line = {"at": P.now_iso(), "checked": len(res), "rejected": [x["ex"] for x in rejected],
            "checks_fingerprint": checks_fingerprint(cfg), "cost_usd": round(api.spent, 4)}
    P.record_ledger(api.spent, "reaudit", len(res))
    with open(REAUDITS, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")
    st = load_state()
    st["reaudit"] = today().isoformat()
    st["reaudit_records"] = len(manifest)
    save_state(st)
    print(json.dumps({**line, "details": rejected}, ensure_ascii=False, indent=2))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("due")
    sub.add_parser("check-models")
    p = sub.add_parser("drift")
    p.add_argument("--last", type=int, default=6)
    p = sub.add_parser("spotcheck")
    p.add_argument("--n", type=int, default=30)
    p.add_argument("--seed")
    p = sub.add_parser("import-ratings")
    p.add_argument("files", nargs="+")
    p = sub.add_parser("reaudit")
    p.add_argument("--sample", type=int, default=100)
    p.add_argument("--budget", type=float, default=0.5)
    p.add_argument("--seed")
    p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    fn = {"due": cmd_due, "check-models": cmd_check_models, "drift": cmd_drift,
          "spotcheck": cmd_spotcheck, "import-ratings": cmd_import_ratings,
          "reaudit": cmd_reaudit}[args.cmd]
    return fn(args) or 0


if __name__ == "__main__":
    sys.exit(main())
