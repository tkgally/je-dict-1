#!/usr/bin/env python3
"""Triage queue for examples the audio workflow left for a human.

`audio/needs_human.jsonl` holds the examples no recording attempt passed. When
the four checkers keep hearing one reading that differs from the furigana, the
furigana is usually what is wrong ({十四|じゅうよん}{日|にち} for じゅうよっか,
{一|いち}{回|かい} for いっかい, {二|に}つ for ふたつ), so the queue is worked by
the systemic-fix mode (backlog item `audio-needs-human-triage`), not by ear.

Lists the held examples whose text and workflow version still match their
needs-human record and that have no triage verdict for that text, most
consistent disagreement first. Fixing the entry changes the example's text, so
it leaves the queue by itself and the audio mode records it again. When the
entry is right and the recording failed for another reason (the TTS said あさって
for {明後日|みょうごにち}, or added a particle), record a verdict so the example
is not listed again until its text changes:

    python3 build/audio_needs_human_triage.py                 # JSON queue (read-only)
    python3 build/audio_needs_human_triage.py --summary       # counts only
    python3 build/audio_needs_human_triage.py --entry 00955   # one entry's held examples
    python3 build/audio_needs_human_triage.py --record 00301_myougonichi_ex1 \\
        --verdict tts-error --note "TTS reads 明後日 as あさって"

Verdicts (audio/needs_human_triage.jsonl): `tts-error` (entry right, the
recording is the problem), `ambiguous` (both readings acceptable; left for Tom).
"""
import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audio_pipeline import (NEEDS_HUMAN, ROOT, load_config, load_examples,  # noqa: E402
                            load_jsonl_by_ex, short_hash)

LEDGER = ROOT / "audio" / "needs_human_triage.jsonl"
VERDICTS = ("tts-error", "ambiguous")


def load_ledger():
    out = {}
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                out[(r["ex"], r["h"])] = r
    return out


def votes(record):
    """(expected, heard) pairs counted over every attempt and checker."""
    c = Counter()
    for a in record.get("attempts") or []:
        for diffs in (a.get("diffs") or {}).values():
            for d in diffs:
                if len(d) == 3:
                    c[(d[1], d[2])] += 1
    return c


def queue(entry=None):
    wf = load_config()["workflow_version"]
    held = load_jsonl_by_ex(NEEDS_HUMAN)
    decided = load_ledger()
    examples = {x["ex"]: x for x in load_examples()}
    out = []
    for ex, r in held.items():
        x = examples.get(ex)
        if not x or r.get("wf") != wf:
            continue
        h = short_hash(x["raw"])
        if r.get("h") != h or (ex, h) in decided:
            continue
        if entry and not x["entry"].startswith(entry):
            continue
        c = votes(r)
        top = c.most_common(1)[0] if c else (("", ""), 0)
        out.append({"ex": ex, "entry": x["entry"], "text": x["raw"],
                    "expected": top[0][0], "heard": top[0][1], "votes": top[1],
                    "attempts": len(r.get("attempts") or []),
                    "other_diffs": [f"{a}→{b} ×{n}" for (a, b), n in c.most_common(4)[1:]]})
    out.sort(key=lambda q: (-q["votes"], q["ex"]))
    return out


def record(ex, verdict, note):
    examples = {x["ex"]: x for x in load_examples()}
    if ex not in examples:
        sys.exit(f"no example {ex}")
    line = {"ex": ex, "h": short_hash(examples[ex]["raw"]), "verdict": verdict, "note": note,
            "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")
    print(json.dumps(line, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--summary", action="store_true", help="counts only")
    ap.add_argument("--entry", help="only this entry ID (or ID prefix)")
    ap.add_argument("--limit", type=int, default=0, help="first N of the queue")
    ap.add_argument("--record", metavar="EXAMPLE_ID", help="record a verdict for one example")
    ap.add_argument("--verdict", choices=VERDICTS)
    ap.add_argument("--note", default="")
    args = ap.parse_args()
    if args.record:
        if not args.verdict:
            sys.exit("--record needs --verdict")
        record(args.record, args.verdict, args.note)
        return 0
    q = queue(args.entry)
    if args.summary:
        print(json.dumps({"open": len(q),
                          "consistent (>= 6 votes)": sum(1 for x in q if x["votes"] >= 6),
                          "entries": len({x["entry"] for x in q})}, indent=2))
        return 0
    print(json.dumps(q[:args.limit] if args.limit else q, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
