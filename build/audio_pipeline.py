#!/usr/bin/env python3
"""Example-audio pipeline: plan → run → publish (AUDIO_WORKFLOW.md; prompts/audio.md).

    python3 build/audio_pipeline.py status                   # coverage, stale, needs-human, store use
    python3 build/audio_pipeline.py plan --budget 2.30       # choose examples (priority order) → audio_work/plan.json
    python3 build/audio_pipeline.py run --budget 2.30        # generate → check → regenerate; stage accepted MP3s
    python3 build/audio_pipeline.py publish                  # push MP3s to the audio repository, then write the manifest
    python3 build/audio_pipeline.py testset --voice Aoede    # voice pilot on the 100-sentence test set
    python3 build/audio_pipeline.py undetermined             # examples skipped because their reading is not determined

Nothing binary is ever written inside je-dict-1's tracked tree: MP3s are staged
in audio_work/ (gitignored) and pushed to the audio repository named in
audio/config.json. je-dict-1 keeps only text: the manifest
(audio/manifest/<range>.jsonl), audio/needs_human.jsonl and audio/runs.jsonl.

A manifest line is valid while its "h" equals audio_text.text_hash() of the
example's current `japanese` field (first 16 hex digits); the site build shows
the recording only then, and `plan` queues the example again otherwise.
"""
import argparse
import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audio_text import (build_reading_index, build_tts_prompt, majority_readings,  # noqa: E402
                        parse_example, text_hash, undetermined_reason)

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "audio"
CONFIG = AUDIO / "config.json"
MANIFEST_DIR = AUDIO / "manifest"
NEEDS_HUMAN = AUDIO / "needs_human.jsonl"
RUNS = AUDIO / "runs.jsonl"
TESTSET = AUDIO / "testset" / "sentences.json"
WORK = ROOT / "audio_work"
PLAN = WORK / "plan.json"
RESULTS = WORK / "results.jsonl"
STAGED = WORK / "staged"
HASH_LEN = 16
TIER_ORDER = {"basic": 0, "core": 1, "general": 2}


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_config(path=None):
    """audio/config.json, or a trial copy (re-evaluation of a new model or prompt)."""
    return json.loads(Path(path or CONFIG).read_text(encoding="utf-8"))


def short_hash(raw):
    return text_hash(raw)[:HASH_LEN]


def entry_range(entry_id):
    return f"{int(str(entry_id)[:5]) // 500 * 500:05d}"


# --------------------------------------------------------------------------- dictionary
def iter_entries():
    for f in sorted(glob.glob(str(ROOT / "entries" / "*" / "*.json"))):
        try:
            yield json.loads(Path(f).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue


def load_examples():
    """All examples, in entry-ID order: dicts with ex, entry, num, idx, tier, raw."""
    out = []
    for d in iter_entries():
        tier = (d.get("metadata") or {}).get("vocabulary_tier", "general")
        num = int(str(d["id"])[:5])
        for i, e in enumerate(d.get("examples") or []):
            if e.get("id") and e.get("japanese"):
                out.append({"ex": e["id"], "entry": d["id"], "num": num, "idx": i,
                            "tier": tier, "raw": e["japanese"]})
    return out


def majority_from_examples(examples):
    return majority_readings(build_reading_index(x["raw"] for x in examples))


# --------------------------------------------------------------------------- manifest
def load_manifest():
    """example id → manifest record (all shards)."""
    out = {}
    for f in sorted(MANIFEST_DIR.glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                out[r["ex"]] = r
    return out


def write_manifest_records(records):
    """Insert or replace records (by example id) in their range shards."""
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    by_shard = defaultdict(list)
    for r in records:
        by_shard[entry_range(r["ex"])].append(r)
    for shard, recs in by_shard.items():
        path = MANIFEST_DIR / f"{shard}.jsonl"
        cur = {}
        if path.exists():
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    x = json.loads(line)
                    cur[x["ex"]] = x
        for r in recs:
            cur[r["ex"]] = r
        path.write_text("".join(json.dumps(cur[k], ensure_ascii=False, separators=(",", ":")) + "\n"
                                for k in sorted(cur)), encoding="utf-8")


def load_jsonl_by_ex(path):
    out = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                out[r["ex"]] = r
    return out


def write_jsonl_by_ex(path, records):
    path.write_text("".join(json.dumps(records[k], ensure_ascii=False, separators=(",", ":")) + "\n"
                            for k in sorted(records)), encoding="utf-8")


# --------------------------------------------------------------------------- spend ledger
def record_ledger(usd, phase, n):
    """Add this spend to pipeline/openrouter-ledger.json (the Routine's daily cap)."""
    p = ROOT / "pipeline" / "openrouter-ledger.json"
    try:
        led = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        led = {}
    today = datetime.now(timezone.utc).date().isoformat()
    if led.get("date") != today:
        led.update({"date": today, "spent_usd": 0.0, "calls": []})
    led["spent_usd"] = round(float(led.get("spent_usd", 0)) + usd, 4)
    led.setdefault("calls", []).append({"ts": now_iso(), "mode": "audio", "phase": phase,
                                        "entries": n, "est_usd": round(usd, 4)})
    p.write_text(json.dumps(led, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- voices
def assign_voice(example, voices, previous=None):
    """Deterministic rotation: within an entry, cycle through the production
    voices in example order starting at (entry number mod N). A re-recording
    keeps its previous voice while that voice is still in production."""
    if previous and previous in voices:
        return previous
    return voices[(example["num"] + example["idx"]) % len(voices)]


# --------------------------------------------------------------------------- priorities
def polish_cursor():
    p = ROOT / "polishing" / "tasks" / "comprehensive" / "progress.txt"
    try:
        import re
        m = re.search(r"next:\s*(\d+)", p.read_text(encoding="utf-8"))
        return int(m.group(1)) if m else 0
    except OSError:
        return 0


def priority_key(x, cursor):
    """Lower sorts first: stale re-recordings, then basic, core, general
    (general: entries the polish frontier has passed, then the rest), each in
    entry-ID and example order."""
    stale = 0 if x.get("stale") else 1
    tier = TIER_ORDER.get(x["tier"], 2)
    ahead = 1 if tier == 2 and x["num"] >= cursor else 0
    return (stale, tier, ahead, x["num"], x["idx"])


def classify(examples, manifest, needs_human, wf):
    """Split examples into recorded (valid), candidates (to record, with stale
    flag), undetermined (reason), and held (left for a human with this text
    and this workflow version)."""
    recorded, todo, undetermined, held = [], [], [], []
    for x in examples:
        h = short_hash(x["raw"])
        x["h"] = h
        m = manifest.get(x["ex"])
        if m and m.get("h") == h:
            recorded.append(x)
            continue
        reason = undetermined_reason(parse_example(x["raw"]))
        if reason:
            x["reason"] = reason
            undetermined.append(x)
            continue
        nh = needs_human.get(x["ex"])
        if nh and nh.get("h") == h and nh.get("wf") == wf:
            held.append(x)
            continue
        x["stale"] = bool(m)
        x["previous_voice"] = m.get("v") if m else None
        todo.append(x)
    return recorded, todo, undetermined, held


# --------------------------------------------------------------------------- status
def cmd_status(args):
    cfg = load_config()
    examples = load_examples()
    manifest = load_manifest()
    needs_human = load_jsonl_by_ex(NEEDS_HUMAN)
    recorded, todo, undetermined, held = classify(examples, manifest, needs_human,
                                                  cfg["workflow_version"])
    by_tier = defaultdict(Counter)
    for x in examples:
        by_tier[x["tier"]]["examples"] += 1
    for x in recorded:
        by_tier[x["tier"]]["recorded"] += 1
    for x in todo:
        by_tier[x["tier"]]["stale" if x.get("stale") else "to_record"] += 1
    for x in undetermined:
        by_tier[x["tier"]]["undetermined"] += 1
    for x in held:
        by_tier[x["tier"]]["needs_human"] += 1
    reasons = Counter(x["reason"] for x in undetermined)
    store_bytes = Counter()
    for r in manifest.values():
        store_bytes[r.get("s")] += int(r.get("b", 0))
    out = {"tiers": {t: dict(c) for t, c in sorted(by_tier.items(), key=lambda kv: TIER_ORDER.get(kv[0], 9))},
           "undetermined_reasons": dict(reasons),
           "manifest_records": len(manifest),
           "stores": [{"id": s["id"], "repo": s["repo"], "status": s["status"],
                       "used_mb": round(store_bytes.get(s["id"], 0) / 1e6, 1),
                       "limit_mb": s["limit_mb"]} for s in cfg["stores"]],
           "voices": cfg["voices"], "workflow_version": cfg["workflow_version"]}
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_undetermined(args):
    examples = load_examples()
    for x in examples:
        reason = undetermined_reason(parse_example(x["raw"]))
        if reason and (not args.reason or reason in args.reason):
            print(f"{x['ex']}\t{reason}\t{parse_example(x['raw'])['plain']}")


# --------------------------------------------------------------------------- plan
def cmd_plan(args):
    cfg = load_config()
    if not cfg.get("production", {}).get("enabled") and not args.force:
        sys.exit("audio production is disabled in audio/config.json (production.enabled): "
                 + cfg.get("production", {}).get("reason", ""))
    from audio_maintenance import production_blocked
    blocked = production_blocked(cfg)
    if blocked and not args.force:
        sys.exit("production is blocked until these are done: "
                 + "; ".join(f"{t}: {r}" for t, _, r in blocked))
    examples = load_examples()
    manifest = load_manifest()
    needs_human = load_jsonl_by_ex(NEEDS_HUMAN)
    _recorded, todo, undetermined, held = classify(examples, manifest, needs_human,
                                                   cfg["workflow_version"])
    if args.ids:
        want = {i.strip()[:5] for i in args.ids.split(",") if i.strip()}
        todo = [x for x in todo if f"{x['num']:05d}" in want]
    if args.tiers:
        tiers = set(args.tiers.split(","))
        todo = [x for x in todo if x["tier"] in tiers]
    cursor = polish_cursor()
    todo.sort(key=lambda x: priority_key(x, cursor))
    per_example = float(cfg.get("est_cost_per_example_usd", 0.0025))
    n = int(args.budget / per_example) if args.budget else len(todo)
    if args.max:
        n = min(n, args.max)
    # finish whole entries: do not split an entry's examples across runs
    chosen, last_entry = [], None
    for x in todo:
        if len(chosen) >= n and x["entry"] != last_entry:
            break
        chosen.append(x)
        last_entry = x["entry"]
    for x in chosen:
        x["voice"] = assign_voice(x, cfg["voices"], x.get("previous_voice"))
    WORK.mkdir(exist_ok=True)
    plan = {"created": now_iso(), "workflow_version": cfg["workflow_version"],
            "budget_usd": args.budget, "items": [
                {k: x[k] for k in ("ex", "entry", "num", "idx", "tier", "raw", "h", "voice", "stale")}
                for x in chosen]}
    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tiers = Counter(x["tier"] for x in chosen)
    print(json.dumps({"planned": len(chosen), "entries": len({x['entry'] for x in chosen}),
                      "stale_rerecordings": sum(1 for x in chosen if x.get("stale")),
                      "by_tier": dict(tiers), "voices": dict(Counter(x["voice"] for x in chosen)),
                      "remaining_after_plan": len(todo) - len(chosen),
                      "skipped_undetermined": len(undetermined), "held_for_human": len(held),
                      "first": chosen[0]["ex"] if chosen else None,
                      "last": chosen[-1]["ex"] if chosen else None}, ensure_ascii=False, indent=2))


# --------------------------------------------------------------------------- run (generate → check → regenerate)
def process_item(item, sentence, prompt, cfg, api, cost_pool, cost_futs):
    """Up to max_attempts generations; returns a result dict (with mp3 bytes
    under "_mp3" when accepted). Each attempt records its TTS generation id
    (billed cost looked up later) and the checkers' cost."""
    from audio_api import encode_mp3, pcm_duration
    from audio_checks import accept, run_checkers
    attempts = []
    for t in range(cfg["max_attempts"]):
        try:
            pcm, gen_id = api.tts(cfg["tts_model"], prompt, item["voice"])
        except Exception as e:  # noqa: BLE001
            attempts.append({"error": repr(e)[:200]})
            continue
        if gen_id:
            cost_futs[gen_id] = cost_pool.submit(api.generation_cost, gen_id)
        mp3 = encode_mp3(pcm, cfg["mp3_kbps"])
        checks = run_checkers(mp3, sentence, cfg["checkers"], api)
        ok = accept(cfg["rule"], [c["verdict"] for c in checks])
        attempts.append({"verdicts": {c["name"]: c["verdict"] for c in checks},
                         "texts": {c["name"]: c["text"][:200] for c in checks},
                         "diffs": {c["name"]: c["diff"] for c in checks if c["diff"]},
                         "duration": pcm_duration(pcm), "accepted": ok, "gen_id": gen_id,
                         "check_cost": round(sum(c["cost"] for c in checks), 6)})
        if ok:
            return {"accepted": True, "attempts": attempts, "_mp3": mp3,
                    "duration": pcm_duration(pcm)}
    return {"accepted": False, "attempts": attempts}


def run_items(items, make_sentence, cfg, budget, workers, out_path, stage_dir, majority,
              reserve_per_item=0.008, deadline=None):
    """Shared by `run` and `testset`. Resumable: items already in out_path are
    skipped. Stops starting new items when the budget would be exceeded."""
    from audio_api import OpenRouter
    api = OpenRouter()
    done = set()
    if out_path.exists():
        for line in out_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["key"])
    todo = [x for x in items if x["key"] not in done]
    lock = threading.Lock()
    cost_pool = ThreadPoolExecutor(4)
    cost_futs = {}
    stats = Counter()
    t0 = time.time()

    def one(x):
        with lock:
            if budget is not None and api.spent + reserve_per_item > budget:
                stats["deferred_budget"] += 1
                return
            if deadline and time.time() > deadline:
                stats["deferred_time"] += 1
                return
        s = make_sentence(x)
        prompt = build_tts_prompt(s, majority)
        res = process_item(x, s, prompt, cfg, api, cost_pool, cost_futs)
        rec = {"key": x["key"], "ex": x.get("ex"), "h": x.get("h"), "voice": x["voice"],
               "accepted": res["accepted"], "attempts": res["attempts"],
               "n_attempts": len(res["attempts"]), "at": now_iso()}
        if res["accepted"]:
            mp3 = res.pop("_mp3")
            digest = hashlib.sha256(mp3).hexdigest()[:8]
            rel = f"{x['stage_prefix']}.{digest}.mp3"
            path = stage_dir / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(mp3)
            rec.update({"file": rel, "bytes": len(mp3), "duration": res["duration"]})
        with lock:
            with open(out_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            stats["accepted" if res["accepted"] else "failed"] += 1
            stats["first_pass"] += bool(res["attempts"] and res["attempts"][0].get("accepted"))
            n = stats["accepted"] + stats["failed"]
            if n % 50 == 0:
                print(f"  {n}/{len(todo)} done, ${api.spent:.3f} spent, "
                      f"{time.time() - t0:.0f}s", flush=True)

    with ThreadPoolExecutor(workers) as pool:
        list(pool.map(one, todo))
    tts_cost = {}
    for gen_id, f in cost_futs.items():  # billed TTS costs (the estimate until known)
        try:
            tts_cost[gen_id] = f.result(timeout=180)
        except Exception:  # noqa: BLE001
            tts_cost[gen_id] = None
    cost_pool.shutdown(wait=True)
    add_costs(out_path, tts_cost, api.tts_estimate)
    return stats, api.spent


def add_costs(path, tts_cost, estimate):
    """Give every result row without one a "cost": its checkers' cost plus the
    billed (or, if unknown, estimated) cost of each TTS call."""
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    for r in rows:
        if "cost" in r:
            continue
        c = 0.0
        for a in r["attempts"]:
            if "gen_id" in a:
                billed = tts_cost.get(a["gen_id"])
                c += billed if billed is not None else estimate
                c += a.get("check_cost", 0.0)
        r["cost"] = round(c, 6)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
                    encoding="utf-8")


def results_rows(path=RESULTS):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def cmd_run(args):
    """Resumable: call again until it prints "remaining": 0. --max-minutes keeps
    each call under the tool timeout; the budget counts earlier calls' cost."""
    cfg = load_config()
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    if plan["workflow_version"] != cfg["workflow_version"]:
        sys.exit("plan was made for another workflow version; run plan again")
    examples = load_examples()
    majority = majority_from_examples(examples)
    items = []
    for x in plan["items"]:
        x = dict(x)
        x["key"] = x["ex"]
        x["stage_prefix"] = f"{entry_range(x['entry'])}/{x['ex']}"
        items.append(x)
    budget = args.budget if args.budget is not None else plan.get("budget_usd")
    keys = {x["key"] for x in items}
    prior = sum(r.get("cost", 0.0) for r in results_rows()
                if r["key"] in keys and not r.get("published"))
    left = None if budget is None else max(0.0, budget - prior)
    deadline = time.time() + 60 * args.max_minutes if args.max_minutes else None
    stats, spent = run_items(items, lambda x: parse_example(x["raw"]), cfg, left,
                             args.workers, RESULTS, STAGED, majority, deadline=deadline)
    rows = results_rows()
    done = {r["key"] for r in rows} & keys
    remaining = [x for x in items if x["key"] not in done]
    budget_out = left is not None and stats.get("deferred_budget", 0) > 0
    print(json.dumps({"this_call": dict(stats), "this_call_usd": round(spent, 4),
                      "done": len(done), "accepted": sum(1 for r in rows if r["accepted"]),
                      "remaining": 0 if budget_out else len(remaining),
                      "stopped_for_budget": budget_out,
                      "spent_on_plan_usd": round(sum(r.get("cost", 0.0) for r in rows
                                                     if r["key"] in keys and not r.get("published")), 4)},
                     indent=2))


# --------------------------------------------------------------------------- testset (voice pilot)
def cmd_testset(args):
    cfg = load_config(args.config)
    sentences = json.loads(TESTSET.read_text(encoding="utf-8"))
    if args.limit:
        sentences = sentences[: args.limit]
    majority = majority_from_examples(load_examples())
    out_dir = Path(args.out or (WORK / f"pilot_{args.voice}"))
    out_dir.mkdir(parents=True, exist_ok=True)
    items = [{"key": f"{s['n']:03d}_{s['id']}", "ex": s["id"], "voice": args.voice,
              "n": s["n"], "stage_prefix": f"{s['n']:03d}_{s['id']}"} for s in sentences]
    by_n = {s["n"]: s for s in sentences}
    stats, spent = run_items(items, lambda x: by_n[x["n"]], cfg, args.budget, args.workers,
                             out_dir / "results.jsonl", out_dir / "clips", majority)
    summ = pilot_summary(out_dir / "results.jsonl", cfg)
    record_ledger(spent, f"pilot {args.voice}", summ["items"])
    print(json.dumps(summ, indent=2))
    if not args.limit and not args.config and summ["items"] == len(sentences):
        record_pilot(cfg, args.voice, summ)


def record_pilot(cfg, voice, summ):
    """Append the pilot to audio/pilots.jsonl. A voice is acceptable for
    production when its first-pass and final acceptance are close to the
    baseline (config "baseline") and Tom has approved its sound (the voice is
    then listed in config "voices"); see AUDIO_WORKFLOW.md §5."""
    from audio_maintenance import checks_fingerprint, generation_fingerprint, pilot_acceptable
    n = summ["items"]
    fp, acc = summ["first_pass"] / n, summ["accepted"] / n
    ok = pilot_acceptable({"first_pass_rate": fp, "accepted_rate": acc}, cfg)
    line = {"at": now_iso(), "voice": voice, "tts": cfg["tts_model"],
            "generation_fingerprint": generation_fingerprint(cfg),
            "checks_fingerprint": checks_fingerprint(cfg), "items": n,
            "first_pass_rate": round(fp, 3), "accepted_rate": round(acc, 3),
            "left_for_human": summ["left_for_human"], "attempts": summ["attempts"],
            "objection_rate_per_attempt": summ["objection_rate_per_attempt"],
            "cost_usd": summ["cost_usd"], "acceptable": ok}
    with open(AUDIO / "pilots.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")
    print(f"pilot recorded in audio/pilots.jsonl (acceptable: {ok})")


def pilot_summary(path, cfg):
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    obj = Counter()
    first_attempts = 0
    for r in rows:
        for a in r["attempts"]:
            if "verdicts" not in a:
                continue
            for name, v in a["verdicts"].items():
                obj[name] += v != "match"
        first_attempts += 1 if r["attempts"] and "verdicts" in r["attempts"][0] else 0
    n_att = sum(len([a for a in r["attempts"] if "verdicts" in a]) for r in rows)
    return {"items": len(rows),
            "first_pass": sum(1 for r in rows if r["attempts"] and r["attempts"][0].get("accepted")),
            "accepted": sum(1 for r in rows if r["accepted"]),
            "left_for_human": [r["key"] for r in rows if not r["accepted"]],
            "attempts": n_att,
            "objection_rate_per_attempt": {k: round(v / max(1, n_att), 3) for k, v in obj.items()},
            "cost_usd": round(sum(r.get("cost", 0) for r in rows), 4),
            "cost_per_item_usd": round(sum(r.get("cost", 0) for r in rows) / max(1, len(rows)), 5)}


# --------------------------------------------------------------------------- publish
def git(repo, *args, input=None, check=True):
    return subprocess.run(["git", "-C", str(repo), *args], input=input, capture_output=True,
                          text=True, check=check)


def active_store(cfg):
    for s in cfg["stores"]:
        if s["status"] == "active":
            return s
    sys.exit("no active audio store in audio/config.json")


def ensure_clone(store, repo_dir):
    """A thin clone of the audio repository: one commit deep, no file contents."""
    if (repo_dir / ".git").exists():
        git(repo_dir, "fetch", "--depth", "1", "--filter=blob:none", "origin", "main")
        git(repo_dir, "reset", "-q", "--soft", "origin/main")
        git(repo_dir, "read-tree", "origin/main")
        return
    repo_dir.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--no-checkout",
                    f"https://github.com/{store['repo']}", str(repo_dir)], check=True)
    git(repo_dir, "read-tree", "HEAD")


def store_dir(store, repo_dir=None):
    """Where to work on the store: --repo-dir, else a clone the session already
    has next to je-dict-1 (a Routine with the audio repository among its
    repositories), else a thin clone in audio_work/."""
    if repo_dir:
        return Path(repo_dir)
    sibling = ROOT.parent / store["repo"].split("/")[-1]
    if (sibling / ".git").exists():
        return sibling
    return WORK / "repo" / store["id"]


def cmd_check_access(args):
    """Can this session push to the active store? Costs nothing: a thin clone
    (or fetch) and a dry-run push. Exit 1 with the git error if not."""
    store = active_store(load_config())
    repo_dir = store_dir(store, args.repo_dir)
    try:
        ensure_clone(store, repo_dir)
    except subprocess.CalledProcessError as e:
        print(json.dumps({"store": store["repo"], "push": False,
                          "error": f"clone/fetch failed: {(e.stderr or '')[:300]}"}, indent=2))
        return 1
    p = git(repo_dir, "push", "--dry-run", "origin", "HEAD:refs/heads/access-check", check=False)
    ok = p.returncode == 0
    print(json.dumps({"store": store["repo"], "repo_dir": str(repo_dir), "push": ok,
                      **({} if ok else {"error": (p.stderr or p.stdout).strip()[:300]})}, indent=2))
    return 0 if ok else 1


def stage_file(repo_dir, path_in_repo, src):
    sha = git(repo_dir, "hash-object", "-w", str(src)).stdout.strip()
    git(repo_dir, "update-index", "--add", "--cacheinfo", f"100644,{sha},{path_in_repo}")


def cmd_publish(args):
    cfg = load_config()
    store = active_store(cfg)
    pages = sorted((WORK / "review").glob("*.html")) if (WORK / "review").exists() else []
    if not RESULTS.exists() and not pages:
        sys.exit("nothing to publish: no audio_work/results.jsonl and no review page")
    rows = [r for r in results_rows() if not r.get("published")]
    plan = ({x["ex"]: x for x in json.loads(PLAN.read_text(encoding="utf-8"))["items"]}
            if PLAN.exists() else {})
    manifest = load_manifest()
    accepted = [r for r in rows if r["accepted"]]
    failed = [r for r in rows if not r["accepted"]]

    # capacity
    used = sum(int(m.get("b", 0)) for m in manifest.values() if m.get("s") == store["id"])
    replaced = sum(int(manifest[r["ex"]].get("b", 0)) for r in accepted
                   if r["ex"] in manifest and manifest[r["ex"]].get("s") == store["id"])
    new = sum(r["bytes"] for r in accepted)
    after_mb = (used - replaced + new) / 1e6
    if after_mb > store["limit_mb"]:
        sys.exit(f"store {store['id']} would hold {after_mb:.0f} MB > limit {store['limit_mb']} MB: "
                 "a new audio repository is needed (see AUDIO_WORKFLOW.md §7)")

    repo_dir = store_dir(store, args.repo_dir)
    if accepted or pages:
        ensure_clone(store, repo_dir)
        for page in pages:  # spot-check pages (audio_maintenance.py spotcheck)
            stage_file(repo_dir, f"review/{page.name}", page)
        if git(repo_dir, "cat-file", "-e", "HEAD:.nojekyll", check=False).returncode != 0:
            empty = WORK / ".nojekyll"
            empty.write_text("", encoding="utf-8")
            stage_file(repo_dir, ".nojekyll", empty)
        for r in accepted:
            stage_file(repo_dir, r["file"], STAGED / r["file"])
            old = manifest.get(r["ex"])
            if old and old.get("s") == store["id"] and old.get("f") != r["file"]:
                git(repo_dir, "update-index", "--force-remove", old["f"], check=False)
        # detailed log (text) in the audio repository, not in je-dict-1
        if rows:
            log_name = f"logs/{datetime.now(timezone.utc):%Y-%m-%d_%H%M%S}.jsonl"
            log_src = WORK / "log_upload.jsonl"
            log_src.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
                               encoding="utf-8")
            stage_file(repo_dir, log_name, log_src)
        msg = (f"Add {len(accepted)} example recordings ({cfg['workflow_version']})" if accepted
               else f"Add review page {', '.join(p.name for p in pages)}")
        c = git(repo_dir, "commit", "-q", "-m", msg, check=False)
        if c.returncode != 0:
            sys.exit(f"commit failed: {c.stderr or c.stdout}")
        for i in range(4):
            p = git(repo_dir, "push", "-q", "origin", "HEAD:main", check=False)
            if p.returncode == 0:
                break
            time.sleep(2 ** (i + 1))
        else:
            sys.exit(f"push to {store['repo']} failed: {p.stderr.strip()[:500]}\n"
                     "Attach the repository first (add_repo, access push) and retry.")

    for page in pages:  # published: move out of the queue, tell Tom
        done = WORK / "review_published"
        done.mkdir(exist_ok=True)
        shutil.move(str(page), done / page.name)
        with open(ROOT / "reviews" / "needs_curator.txt", "a", encoding="utf-8") as f:
            f.write(f"{now_iso()} audio-spotcheck — please listen and rate: "
                    f"{store['base_url']}review/{page.name} (then upload the downloaded ratings "
                    "file to audio/spotchecks/ in je-dict-1)\n")
    if not rows:
        print(json.dumps({"published_pages": [p.name for p in pages]}, indent=2))
        return

    # manifest and needs-human records (only after a successful push)
    today = datetime.now(timezone.utc).date().isoformat()
    published_at = now_iso()  # the Recent page dates audio additions by this
    recs = []
    for r in accepted:
        last = r["attempts"][-1]
        recs.append({"ex": r["ex"], "h": r["h"], "v": r["voice"], "s": store["id"], "f": r["file"],
                     "d": r["duration"], "b": r["bytes"], "at": published_at,
                     "wf": cfg["workflow_version"], "tts": cfg["tts_model"],
                     "n": r["n_attempts"],
                     "obj": sorted(k for k, v in last["verdicts"].items() if v != "match")})
    write_manifest_records(recs)
    # has_audio in the entries follows the manifest (build/sync_audio_flags.py)
    if recs:
        sync = subprocess.run([sys.executable, str(ROOT / "build" / "sync_audio_flags.py"), "--ids",
                               ",".join(sorted({r["ex"][:5] for r in recs}))],
                              capture_output=True, text=True)
        print(sync.stdout.strip() or sync.stderr.strip(), file=sys.stderr)
    nh = load_jsonl_by_ex(NEEDS_HUMAN)
    for r in accepted:
        nh.pop(r["ex"], None)
    for r in failed:
        nh[r["ex"]] = {"ex": r["ex"], "h": r["h"], "wf": cfg["workflow_version"], "at": today,
                       "voice": r["voice"], "raw": plan.get(r["ex"], {}).get("raw"),
                       "attempts": [{"verdicts": a.get("verdicts"), "diffs": a.get("diffs"),
                                     "error": a.get("error")} for a in r["attempts"]]}
    write_jsonl_by_ex(NEEDS_HUMAN, nh)

    # run summary
    obj = Counter()
    n_att = 0
    for r in rows:
        for a in r["attempts"]:
            if "verdicts" in a:
                n_att += 1
                for k, v in a["verdicts"].items():
                    obj[k] += v != "match"
    cost = round(sum(r.get("cost", 0) for r in rows), 4)
    summary = {"at": now_iso(), "wf": cfg["workflow_version"], "tts": cfg["tts_model"],
               "store": store["id"], "examples": len(rows), "accepted": len(accepted),
               "first_pass": sum(1 for r in rows if r["attempts"] and r["attempts"][0].get("accepted")),
               "needs_human": len(failed), "attempts": n_att,
               "objections": dict(obj), "cost_usd": cost,
               "cost_per_accepted_usd": round(cost / max(1, len(accepted)), 5),
               "bytes": new, "store_used_mb": round(after_mb, 1),
               "voices": dict(Counter(r["voice"] for r in accepted)),
               "first_example": min((r["ex"] for r in rows), default=None),
               "last_example": max((r["ex"] for r in rows), default=None)}
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(summary, ensure_ascii=False) + "\n")
    record_ledger(cost, "production", len(rows))
    # mark published so a rerun does not publish twice
    all_rows = results_rows()
    for r in all_rows:
        r["published"] = True
    RESULTS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in all_rows),
                       encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if accepted:
        print(f"check: {store['base_url']}{accepted[0]['file']} (GitHub Pages deploys in a few minutes)")


# --------------------------------------------------------------------------- verify
def cmd_verify(args):
    """Wait until the newest published recordings are served (GitHub Pages
    deploys a few minutes after the push). Exit 1 if they are not after --wait."""
    import requests
    cfg = load_config()
    stores = {s["id"]: s["base_url"] for s in cfg["stores"]}
    rows = [r for r in results_rows() if r.get("accepted") and r.get("file")]
    if not rows:
        sys.exit("no published recordings in audio_work/results.jsonl")
    store = active_store(cfg)
    newest = max(r.get("at", "") for r in rows)[:13]  # the latest batch (same hour)
    batch = [r for r in rows if r.get("at", "")[:13] == newest] or rows
    urls = [store["base_url"] + r["file"] for r in (batch[0], batch[-1])]
    deadline = time.time() + args.wait
    while True:
        codes = []
        for u in urls:
            try:
                codes.append(requests.head(u, timeout=30, allow_redirects=True).status_code)
            except requests.RequestException:
                codes.append(None)
        if all(c == 200 for c in codes):
            print(json.dumps({"served": urls}, indent=2))
            return
        if time.time() > deadline:
            print(json.dumps({"not_served_yet": dict(zip(urls, codes))}, indent=2))
            sys.exit(1)
        time.sleep(20)


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    p = sub.add_parser("undetermined")
    p.add_argument("--reason", nargs="*", help="malformed bare-kanji digits latin")
    p = sub.add_parser("plan")
    p.add_argument("--budget", type=float, default=2.0, help="USD; sizes the plan")
    p.add_argument("--max", type=int, help="at most this many examples")
    p.add_argument("--ids", help="comma-separated entry IDs only")
    p.add_argument("--tiers", help="e.g. basic,core")
    p.add_argument("--force", action="store_true", help="plan even if production is disabled or blocked")
    p = sub.add_parser("run")
    p.add_argument("--budget", type=float, help="USD cap for the whole plan (default: the plan's)")
    p.add_argument("--workers", type=int, default=12)
    p.add_argument("--max-minutes", type=float, default=8,
                   help="stop starting new items after this long (0 = no limit); call again to resume")
    p = sub.add_parser("publish")
    p.add_argument("--repo-dir", help="existing clone of the audio repository")
    p = sub.add_parser("check-access")
    p.add_argument("--repo-dir")
    p = sub.add_parser("verify")
    p.add_argument("--wait", type=int, default=540, help="seconds to wait for GitHub Pages")
    p = sub.add_parser("testset")
    p.add_argument("--voice", required=True)
    p.add_argument("--config", help="trial config (not recorded in audio/pilots.jsonl)")
    p.add_argument("--out")
    p.add_argument("--limit", type=int)
    p.add_argument("--budget", type=float, default=1.5)
    p.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    rc = {"status": cmd_status, "undetermined": cmd_undetermined, "plan": cmd_plan, "run": cmd_run,
     "publish": cmd_publish, "testset": cmd_testset, "verify": cmd_verify,
     "check-access": cmd_check_access}[args.cmd](args)
    sys.exit(rc or 0)


if __name__ == "__main__":
    main()
