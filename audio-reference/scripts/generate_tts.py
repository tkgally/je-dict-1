"""Generate mp3 readings with the Gemini TTS models via OpenRouter.

    python generate_tts.py                 # full grid: 100 × 2 models × 3 strategies × 2 voices
    python generate_tts.py --limit 3       # first 3 sentences only (pilot)
    python generate_tts.py --controls      # error-injection control clips

OpenRouter returns raw 24 kHz mono 16-bit PCM for Gemini TTS; it is converted
to 64 kbps mp3 with ffmpeg.  Every call is recorded in data/tts_manifest.jsonl
(with its billed cost, looked up by generation id) and in data/cost_log.jsonl.
Existing clips are skipped, so the script can be re-run to resume."""
import argparse
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import (DATA, ROOT, TTS_MODELS, VOICES, generation_cost, log_cost,
                    post)
from prompts import STRATEGIES, STRATEGIES_2, build_prompt

SITE_AUDIO = ROOT / "site" / "audio"
MANIFEST = DATA / "tts_manifest.jsonl"


def clip_key(model, strategy, voice, s):
    return f"{model}/{strategy}/{voice}/{s['n']:03d}_{s['id']}"


def load_manifest():
    done = {}
    if MANIFEST.exists():
        for line in open(MANIFEST):
            r = json.loads(line)
            if not r.get("error"):
                done[r["key"]] = r
    return done


def synth(job, phase):
    out = SITE_AUDIO / f"{job['key']}.mp3"
    out.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    rec = {k: job[k] for k in ("key", "model", "strategy", "voice", "n", "id", "prompt",
                               "control_kind", "control_detail") if k in job}
    try:
        r = post("/audio/speech", {
            "model": TTS_MODELS[job["model"]], "input": job["prompt"],
            "voice": VOICES[job["voice"]], "response_format": "pcm"})
        rec["latency"] = round(time.time() - t0, 2)
        if not r.ok or not r.headers.get("content-type", "").startswith("audio"):
            rec["error"] = f"{r.status_code} {r.text[:300]}"
            return rec
        pcm = r.content
        rec["gen_id"] = r.headers.get("x-generation-id")
        rec["duration"] = round(len(pcm) / 48000, 2)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", "24000",
                        "-ac", "1", "-i", "pipe:0", "-codec:a", "libmp3lame",
                        "-b:a", "64k", str(out)], input=pcm, check=True)
        cost, gen = generation_cost(rec["gen_id"]) if rec["gen_id"] else (None, None)
        rec["cost"] = cost
        if gen:
            rec["tokens_prompt"] = gen.get("native_tokens_prompt")
            rec["tokens_completion"] = gen.get("native_tokens_completion")
        log_cost(phase, TTS_MODELS[job["model"]], cost, key=job["key"])
    except Exception as e:  # keep going; failures are listed in the manifest
        rec["error"] = repr(e)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--controls", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--strategies", nargs="+", help="default: A–D; 'round2' for E–H")
    args = ap.parse_args()

    sentences = json.load(open(DATA / "sentences.json"))[: args.limit]
    jobs = []
    if args.controls:
        from controls import control_jobs
        jobs, phase = control_jobs(sentences), "tts-controls"
    else:
        phase = "tts"
        strats = (STRATEGIES_2 if args.strategies == ["round2"] else args.strategies) or STRATEGIES
        if strats is STRATEGIES_2:
            phase = "tts-round2"
        for s in sentences:
            for model in TTS_MODELS:
                for strategy in strats:
                    for voice in VOICES:
                        jobs.append({"key": clip_key(model, strategy, voice, s),
                                     "model": model, "strategy": strategy,
                                     "voice": voice, "n": s["n"], "id": s["id"],
                                     "prompt": build_prompt(strategy, s)})
    done = load_manifest()
    todo = [j for j in jobs if j["key"] not in done
            or not (SITE_AUDIO / f"{j['key']}.mp3").exists()]
    print(f"{len(jobs)} clips, {len(todo)} to generate")
    errors = 0
    with ThreadPoolExecutor(args.workers) as pool, open(MANIFEST, "a") as mf:
        futs = [pool.submit(synth, j, phase) for j in todo]
        for i, f in enumerate(as_completed(futs), 1):
            rec = f.result()
            mf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            mf.flush()
            if rec.get("error"):
                errors += 1
                print("ERROR", rec["key"], rec["error"][:200])
            if i % 50 == 0:
                print(f"  {i}/{len(todo)}")
    print(f"done; {errors} errors")


if __name__ == "__main__":
    main()
