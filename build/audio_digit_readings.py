#!/usr/bin/env python3
"""Readings for examples with digits or Latin letters (AUDIO_WORKFLOW.md §3.1).

Furigana do not say how 3時, 20%, NHK or Wi-Fi are read, so about 2,600
examples have no recording. This tool has a strong text model write the
reading of each such sentence (with every other acceptable reading), has a
second model confirm it, and stores the result in audio/digit_readings.json.
The audio pipeline then records the example against that reading, exactly as
the hand-written readings of the test set (build/audio_pipeline.py
spoken_example). Production uses confirmed readings only after Tom has
listened to a sample and approved the method (`method_approved`).

    python3 build/audio_digit_readings.py status
    python3 build/audio_digit_readings.py generate --n 200 --budget 1.00 [--sample]
    python3 build/audio_digit_readings.py confirm --budget 0.50
    python3 build/audio_digit_readings.py sample --n 30 --budget 0.30     # clips + listening page in audio_work/digit_sample/
    python3 build/audio_digit_readings.py approve --note "Tom approved the sample 2026-10-24"

A model reading must keep every part of the sentence the furigana already
fix: outside the digits and letters it has to match the known reading kana for
kana, or it is not stored. `generate` and `confirm` record their billed cost
in pipeline/openrouter-ledger.json (mode audio).
"""
import argparse
import json
import os
import re
import sys
import threading
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audio_pipeline as P  # noqa: E402
from audio_text import kata2hira, undetermined_reason  # noqa: E402

GEN_MODEL = "openai/gpt-6.1-sol"
CONFIRM_MODEL = "google/gemini-3.8-flash"
PRICES = {"openai/gpt-6.1-sol": (2.0, 10.0), "google/gemini-3.8-flash": (0.83, 4.12)}
BATCH = 20
SPEND_LEDGER = P.ROOT / "pipeline" / "openrouter-ledger.json"
DOC = ("Model-written readings for examples with digits or Latin letters (AUDIO_WORKFLOW.md §3.1; "
       "build/audio_digit_readings.py). state: generated (one model), confirmed (a second model "
       "agreed), disputed (it did not). h is the short text hash of the example the reading was "
       "written for. Production records an example against its reading only when the state is "
       "confirmed and method_approved is true (Tom, after listening to a sample).")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load():
    try:
        data = json.loads(P.DIGIT_READINGS.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    data.setdefault("_doc", DOC)
    data.setdefault("method_approved", False)
    data.setdefault("readings", {})
    return data


def save(data):
    data["readings"] = dict(sorted(data["readings"].items()))
    P.DIGIT_READINGS.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def record_spend(usd, phase, n):
    try:
        led = json.loads(SPEND_LEDGER.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        led = {}
    today = datetime.now(timezone.utc).date().isoformat()
    if led.get("date") != today:
        led.update({"date": today, "spent_usd": 0.0, "calls": []})
    led["spent_usd"] = round(float(led.get("spent_usd", 0)) + usd, 4)
    led.setdefault("calls", []).append({"ts": now(), "mode": "audio", "phase": phase,
                                        "entries": n, "est_usd": round(usd, 4)})
    SPEND_LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- reading check
def norm(s):
    """Hiragana and the long-vowel mark only (katakana folded to hiragana)."""
    return "".join(c for c in kata2hira(unicodedata.normalize("NFKC", s))
                   if "ぁ" <= c <= "ゖ" or c == "ー")


def pattern(known):
    """Regex for full readings consistent with the known reading: its kana
    stay as they are, each run of digits, letters or symbols becomes a gap."""
    out, gap = [], False
    for c in kata2hira(unicodedata.normalize("NFKC", known)):
        if "ぁ" <= c <= "ゖ" or c == "ー":
            out.append(re.escape(c))
            gap = False
        elif unicodedata.category(c)[0] in "LNS" or c in "%.,:/-+~'&":
            if not gap:
                out.append("(.+?)")
            gap = True
        # punctuation and spaces are not spoken
    return re.compile("".join(out))


def consistent(known, reading):
    return bool(pattern(known).fullmatch(norm(reading)))


# --------------------------------------------------------------------------- model calls
def call(model, prompt):
    from review_runner import call_openrouter, extract_message_text, strip_code_fences
    resp = call_openrouter(os.environ["OPENROUTER_API_KEY"], model, prompt, timeout=240,
                           max_tokens=24000)
    if not resp:
        return None, 0.0
    usage = resp.get("usage") or {}
    cost = usage.get("cost")
    if cost is None:
        pin, pout = PRICES.get(model, (2.0, 10.0))
        cost = (usage.get("prompt_tokens", 0) * pin + usage.get("completion_tokens", 0) * pout) / 1e6
    text = strip_code_fences(extract_message_text(resp) or "")
    m = re.search(r"\[.*\]", text, re.DOTALL)
    try:
        return (json.loads(m.group()) if m else None), float(cost)
    except ValueError:
        return None, float(cost)


GEN_PROMPT = """Below are Japanese example sentences from a learner's dictionary. Each contains Arabic digits, Latin letters or symbols whose reading the text does not show. For each sentence write how a native speaker would read the WHOLE sentence aloud, in hiragana (loanwords and letter names may be in katakana).

- KNOWN gives the reading of every other part (from the furigana). Keep it exactly: change only the digits, letters and symbols, and a word still in kanji right after a number (its counter: 3日 みっか, 20分 にじゅっぷん, 3階 さんがい). Write the particles は, へ, を as written, not as pronounced.
- Use the reading a careful native speaker would use in this sentence: counters with their sound changes (3本 さんぼん, 1泊 いっぱく, 8分 はっぷん), dates (1日 ついたち, 20日 はつか), years, times, prices, telephone and room numbers as they are said, abbreviations as they are said (NHK エヌエイチケー, JR ジェイアール, Wi-Fi ワイファイ, cm センチ).
- In "alt" list every other reading a careful native speaker would also accept for the same sentence (じゅっぷん and じっぷん, エヌエイチケー and エヌエッチケー); leave it empty if there is none.
- If you are not sure how a sentence is read, set "unsure": true.

Reply with a JSON array only: [{"ex": "…", "kana": "…", "alt": ["…"], "unsure": false}]

"""

CONFIRM_PROMPT = """Below are Japanese example sentences with a proposed reading of the whole sentence in kana (and any accepted alternatives). Check how the digits, Latin letters and symbols are read: counter sound changes, dates, times, prices, abbreviations. For each, answer "ok": true if the main reading is a correct, natural reading of the sentence aloud; otherwise "ok": false and give the right reading in "kana". Add to "alt" any other reading a careful native speaker would accept that is missing.

Reply with a JSON array only: [{"ex": "…", "ok": true, "kana": "…", "alt": ["…"]}]

"""


# --------------------------------------------------------------------------- selection
DIGIT_OR_LATIN = re.compile(r"[0-9A-Za-z０-９Ａ-Ｚａ-ｚ][%.,:/\-]*$")


def known_reading(p):
    """The reading the furigana fix, as kana, with the gaps the model fills left
    as they are written. A word with furigana right after a digit or a letter
    (3{日|にち}, 20{分|ふん}) stays in kanji too: its reading depends on the number
    (みっか, にじゅっぷん) and the furigana sometimes give the bare counter."""
    out, prev = [], ""
    for base, reading in p["tokens"]:
        if reading and DIGIT_OR_LATIN.search(prev):
            out.append(base)
        else:
            out.append(reading or base)
        prev = base
    return "".join(out)


def undetermined_examples():
    """Examples whose only reading problem is digits or Latin letters."""
    out = []
    for x in P.load_examples():
        p = P.parse_example(x["raw"])
        if undetermined_reason(p) in ("digits", "latin"):
            x["plain"], x["known"] = p["plain"], known_reading(p)
            out.append(x)
    return out


def spread(items, n):
    """n items spread evenly over the list (a sample across the dictionary)."""
    if len(items) <= n:
        return items
    step = len(items) / n
    return [items[int(i * step)] for i in range(n)]


# --------------------------------------------------------------------------- commands
def cmd_status(args):
    data = load()
    pending = undetermined_examples()
    states = {}
    current = {x["ex"]: P.short_hash(x["raw"]) for x in pending}
    for ex, r in data["readings"].items():
        k = r.get("state") if current.get(ex) == r.get("h") else "outdated"
        states[k] = states.get(k, 0) + 1
    print(json.dumps({"method_approved": data["method_approved"], "undetermined_digits_latin": len(pending),
                      "readings": states,
                      "without_reading": sum(1 for x in pending
                                             if data["readings"].get(x["ex"], {}).get("h") != current[x["ex"]])},
                     indent=2))
    return 0


def run_parallel(batches, ask, apply, budget, workers, data, label):
    """Send the batches to the model `workers` at a time; apply each answer under a
    lock and save as it arrives, so an interrupted run keeps what it has. Stops
    starting batches once `budget` is spent; the spend goes to the ledger at the end."""
    lock = threading.Lock()
    state = {"spent": 0.0, "done": 0}
    total = sum(len(b) for b in batches)

    def one(batch):
        with lock:
            if state["spent"] >= budget:
                return
        items, cost = ask(batch)
        with lock:
            state["spent"] += cost
            apply(batch, items or [])
            state["done"] += len(batch)
            save(data)
            print(f"  {state['done']}/{total}  ${state['spent']:.3f}", flush=True)

    try:
        with ThreadPoolExecutor(workers) as pool:
            list(pool.map(one, batches))
    finally:
        if state["spent"]:
            record_spend(state["spent"], label, state["done"])
    print(f"EST_COST={state['spent']:.4f}")
    return state["spent"]


def cmd_generate(args):
    data = load()
    todo = [x for x in undetermined_examples()
            if data["readings"].get(x["ex"], {}).get("h") != P.short_hash(x["raw"])]
    todo = spread(todo, args.n) if args.sample else todo[:args.n]
    counts = {"stored": 0, "rejected": 0}

    def ask(batch):
        lines = "\n".join(f'{x["ex"]}\tTEXT: {x["plain"]}\tKNOWN: {x["known"]}' for x in batch)
        return call(args.model, GEN_PROMPT + lines)

    def apply(batch, items):
        by_ex = {x["ex"]: x for x in batch}
        for it in items:
            x = by_ex.get(str(it.get("ex")))
            if not x or not it.get("kana") or it.get("unsure") or not consistent(x["known"], it["kana"]):
                counts["rejected"] += 1
                continue
            alts = [a for a in (it.get("alt") or []) if a and consistent(x["known"], a)]
            data["readings"][x["ex"]] = {"h": P.short_hash(x["raw"]), "kana": norm(it["kana"]),
                                         "alt_kana": sorted({norm(a) for a in alts} - {norm(it["kana"])}),
                                         "state": "generated", "by": args.model, "added": now()}
            counts["stored"] += 1

    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    run_parallel(batches, ask, apply, args.budget, args.workers, data, "digit-readings generate")
    print(json.dumps(counts))
    return 0


def cmd_confirm(args):
    data = load()
    examples = {x["ex"]: x for x in undetermined_examples()}
    todo = [(ex, r) for ex, r in data["readings"].items()
            if r.get("state") == "generated" and ex in examples
            and r.get("h") == P.short_hash(examples[ex]["raw"])]
    counts = {"confirmed": 0, "disputed": 0}

    def ask(batch):
        lines = "\n".join(f'{ex}\tTEXT: {examples[ex]["plain"]}\tREADING: {r["kana"]}'
                          + (f'\tALSO: {" / ".join(r["alt_kana"])}' if r.get("alt_kana") else "")
                          for ex, r in batch)
        return call(args.model, CONFIRM_PROMPT + lines)

    def apply(batch, items):
        by_ex = dict(batch)
        for it in items:
            r = by_ex.get(str(it.get("ex")))
            if not r:
                continue
            known = examples[str(it["ex"])]["known"]
            extra = {norm(a) for a in (it.get("alt") or []) if a and consistent(known, a)}
            if it.get("ok"):
                r["alt_kana"] = sorted((set(r.get("alt_kana", [])) | extra) - {r["kana"]})
                r["state"], r["confirmed_by"] = "confirmed", args.model
                counts["confirmed"] += 1
            else:
                r["state"] = "disputed"
                r["disputed_by"] = {"model": args.model, "kana": norm(it.get("kana", "")),
                                    "alt": sorted(extra)}
                counts["disputed"] += 1

    batches = [todo[i:i + BATCH] for i in range(0, len(todo), BATCH)]
    run_parallel(batches, ask, apply, args.budget, args.workers, data, "digit-readings confirm")
    print(json.dumps(counts))
    return 0


def cmd_sample(args):
    """Record a spread sample of confirmed readings (TTS and the four checks, as in
    production) and write a listening page for Tom next to the clips."""
    from audio_review_page import make_page
    cfg = P.load_config()
    readings = load_digit_readings_all()
    examples = {x["ex"]: x for x in P.load_examples()}
    pool = [examples[ex] for ex in sorted(readings) if ex in examples
            and readings[ex]["h"] == P.short_hash(examples[ex]["raw"])]
    chosen = spread(pool, args.n)
    out = Path(args.out)
    (out / "clips").mkdir(parents=True, exist_ok=True)
    items = [{"key": x["ex"], "ex": x["ex"], "h": P.short_hash(x["raw"]),
              "voice": P.assign_voice(x, cfg["voices"]), "stage_prefix": x["ex"]} for x in chosen]
    majority = P.majority_from_examples(P.load_examples())
    overrides = P.load_overrides()
    stats, spent = P.run_items(items, lambda it: P.spoken_example(examples[it["ex"]], overrides, readings),
                               cfg, args.budget, 4, out / "results.jsonl", out / "clips", majority)
    record_spend(spent, "digit-readings sample", len(items))
    rows = [json.loads(l) for l in (out / "results.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    clips = []
    for r in rows:
        if not r.get("accepted"):
            continue
        p = P.spoken_example(examples[r["ex"]], overrides, readings)
        alts = readings[r["ex"]].get("alt_kana") or []
        clips.append({"key": r["ex"], "text": p["plain"], "reading": p["kana"]
                      + (f"  (also accepted: {' / '.join(alts)})" if alts else ""),
                      "src": f"clips/{r['file']}", "meta": f"{r['ex']} · {r['voice']}"})
    page_id = f"digit-readings-{datetime.now(timezone.utc).date().isoformat()}"
    intro = ("<p>Example sentences with digits or Latin letters (3時, 20%, NHK), which had no "
             "recording because the furigana do not say how they are read. A text model wrote each "
             "reading, a second model confirmed it, and the recording passed the usual four checks "
             "against that reading.</p><p>Listen for the numbers and letters above all: ✓ correct, "
             "✗ wrong (a misread number, counter or abbreviation, or anything else), ? unsure; a "
             "comment helps with ✗. Then press <b>Download ratings</b> and send the file back.</p>")
    (out / "index.html").write_text(make_page(page_id, "Readings of digits and letters", intro,
                                              [(None, clips)]), encoding="utf-8")
    failed = [r["ex"] for r in rows if not r.get("accepted")]
    print(json.dumps({"page": str(out / "index.html"), "clips": len(clips), "not_accepted": failed,
                      "cost_usd": round(spent, 4), **{k: v for k, v in stats.items() if isinstance(v, int)}},
                     indent=2))
    return 0


def load_digit_readings_all():
    return P.load_digit_readings(approved_only=False)


def cmd_counter_furigana(args):
    """Examples whose confirmed reading contradicts the furigana of the word after a
    number (3{日|にち} said みっか, 3{階|かい} said さんがい): the displayed furigana are
    wrong. Read-only queue for the systemic-fix item digit-counter-furigana."""
    data = load()
    out = []
    for x in undetermined_examples():
        r = data["readings"].get(x["ex"])
        if not r or r.get("state") != "confirmed" or r.get("h") != P.short_hash(x["raw"]):
            continue
        strict = P.parse_example(x["raw"])["kana"]
        if not any(consistent(strict, k) for k in [r["kana"], *r.get("alt_kana", [])]):
            out.append({"ex": x["ex"], "entry": x["entry"], "text": x["raw"], "said": r["kana"]})
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"{len(out)} examples", file=sys.stderr)
    return 0


BACKLOG = P.ROOT / "planning" / "wiki" / "ideas" / "backlog-queue.json"
BACKLOG_ITEM = "audio-digit-readings"


def cmd_approve(args):
    """Tom's go-ahead after the sample: production uses confirmed readings, and the
    systemic-fix item that writes the rest of them is opened."""
    data = load()
    data["method_approved"] = True
    data["approved"] = {"at": now(), "note": args.note}
    save(data)
    try:
        q = json.loads(BACKLOG.read_text(encoding="utf-8"))
        for it in q.get("items", []):
            if it.get("id") == BACKLOG_ITEM:
                it["status"], it["batch_ready"] = "open", True
        BACKLOG.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError):
        pass
    print(f"method approved: confirmed readings are now used by production; {BACKLOG_ITEM} opened")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    p = sub.add_parser("generate")
    p.add_argument("--n", type=int, default=200)
    p.add_argument("--budget", type=float, default=1.0)
    p.add_argument("--sample", action="store_true", help="spread the n examples over the dictionary")
    p.add_argument("--model", default=GEN_MODEL)
    p.add_argument("--workers", type=int, default=6)
    p.set_defaults(fn=cmd_generate)
    p = sub.add_parser("confirm")
    p.add_argument("--budget", type=float, default=0.5)
    p.add_argument("--model", default=CONFIRM_MODEL)
    p.add_argument("--workers", type=int, default=6)
    p.set_defaults(fn=cmd_confirm)
    p = sub.add_parser("sample")
    p.add_argument("--n", type=int, default=30)
    p.add_argument("--budget", type=float, default=0.3)
    p.add_argument("--out", default=str(P.WORK / "digit_sample"))
    p.set_defaults(fn=cmd_sample)
    sub.add_parser("counter-furigana", help="examples whose counter furigana contradict the reading").set_defaults(
        fn=cmd_counter_furigana)
    p = sub.add_parser("approve")
    p.add_argument("--note", required=True)
    p.set_defaults(fn=cmd_approve)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
