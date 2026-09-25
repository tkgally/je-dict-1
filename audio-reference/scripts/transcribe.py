"""Transcribe generated clips with STT models (proof-listening).

    python transcribe.py --models google/chirp-3 qwen/qwen3-asr-flash-2026-02-10 --set all
    python transcribe.py --models ... --set pilot      # STT model selection sample

Two kinds of transcriber:
  * dedicated STT models via /audio/transcriptions (output: normal kanji text)
  * audio-input LLMs via /chat/completions, prompted to write what is heard
    in hiragana ("kana:" prefix in --models, e.g. kana:google/gemini-3.8-flash),
    which makes the reading of heteronyms such as 今日 checkable.
Results go to data/stt/<model>.jsonl; costs to data/cost_log.jsonl."""
import argparse
import base64
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import DATA, ROOT, log_cost, post

STT_DIR = DATA / "stt"
AUDIO = ROOT / "site" / "audio"

KANA_PROMPT = (
    "Transcribe the Japanese speech in this audio exactly as it is pronounced, "
    "writing everything in hiragana (katakana only for loanwords). Do not use "
    "kanji, do not correct or normalize anything, and write any non-Japanese "
    "speech verbatim. Output only the transcription.")


def clips(which):
    recs = {}
    for line in open(DATA / "tts_manifest.jsonl"):
        r = json.loads(line)
        if not r.get("error"):
            recs[r["key"]] = r
    keys = sorted(recs)
    if which == "pilot":  # controls + unstructured pilot + one full normal configuration
        keys = [k for k in keys if recs[k]["strategy"] in ("control", "furigana_unstructured")
                or k.startswith("flash/plain/female/")]
    elif which == "round2":  # prompts E–H
        from prompts import STRATEGIES_2
        keys = [k for k in keys if recs[k]["strategy"] in STRATEGIES_2]
    return keys


# providers that only accept WAV input
WAV_ONLY = ("assemblyai/", "meta/")


def audio_b64(key, model):
    path = AUDIO / f"{key}.mp3"
    if model.startswith(WAV_ONLY):
        wav = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ar", "16000",
                              "-ac", "1", "-f", "wav", "pipe:1"],
                             capture_output=True, check=True).stdout
        return base64.b64encode(wav).decode(), "wav"
    return base64.b64encode(path.read_bytes()).decode(), "mp3"


def slug(model):
    return model.replace("/", "__").replace(":", "_")


def run_one(model, key, language, phase):
    b, fmt = audio_b64(key, model)
    rec = {"key": key, "model": model}
    try:
        if model.startswith("kana:"):
            m = model[5:]
            r = post("/chat/completions", {
                "model": m, "temperature": 0,
                "reasoning": {"effort": "low"},
                "messages": [{"role": "user", "content": [
                    {"type": "text", "text": KANA_PROMPT},
                    {"type": "input_audio", "input_audio": {"data": b, "format": "mp3"}}]}]})
            d = r.json()
            if "choices" not in d:
                rec["error"] = str(d)[:300]
                return rec
            rec["text"] = (d["choices"][0]["message"].get("content") or "").strip()
            rec["cost"] = d.get("usage", {}).get("cost")
            log_cost(phase, m, rec["cost"], key=key, mode="kana")
        else:
            payload = {"model": model, "input_audio": {"data": b, "format": fmt}}
            if language:
                payload["language"] = language
            r = post("/audio/transcriptions", payload)
            d = r.json()
            if "text" not in d:
                rec["error"] = str(d)[:300]
                return rec
            rec["text"] = d["text"]
            rec["cost"] = d.get("usage", {}).get("cost")
            log_cost(phase, model, rec["cost"], key=key)
    except Exception as e:
        rec["error"] = repr(e)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--set", default="all", choices=["all", "pilot", "round2"])
    ap.add_argument("--keys", help="file with one clip key per line (overrides --set)")
    ap.add_argument("--language", default="ja")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--phase", default="stt-pilot", help="label for the cost log")
    args = ap.parse_args()
    STT_DIR.mkdir(exist_ok=True)
    keys = [l.strip() for l in open(args.keys)] if args.keys else clips(args.set)
    for model in args.models:
        path = STT_DIR / f"{slug(model)}.jsonl"
        done = set()
        if path.exists():
            done = {json.loads(l)["key"] for l in open(path) if "text" in json.loads(l)}
        todo = [k for k in keys if k not in done]
        print(f"{model}: {len(todo)} of {len(keys)} clips to transcribe")
        errs = 0
        with ThreadPoolExecutor(args.workers) as pool, open(path, "a") as f:
            futs = [pool.submit(run_one, model, k, args.language, args.phase) for k in todo]
            for fut in as_completed(futs):
                rec = fut.result()
                if rec.get("error"):
                    errs += 1
                    if errs <= 3:
                        print("  ERROR", rec["key"], rec["error"][:200])
                    continue
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f.flush()
        print(f"  done, {errs} errors")


if __name__ == "__main__":
    main()
