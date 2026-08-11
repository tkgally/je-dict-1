#!/usr/bin/env python3
"""Append one quality-metrics line per Routine run to pipeline/metrics-history.jsonl.

Replaces the inline fallback snippet in prompts/routine2.md §5. One JSON line
per run gives the curator (and the wiki mode's metrics-trend activity) a real
time series for "is the dictionary getting better?".

Cheap collectors run every time (file counts, cursors, ledger). Detector queue
depths (the three read-only check_* scripts, each a full corpus scan) are
collected only when the last row that has them is older than 7 days, or with
--full.

Flag tallies (--applied/--rejected/--flagged) default to "today's
reviews/decisions.jsonl lines not yet attributed to an earlier metrics row
today", so a Routine run that logged its adjudications per §C can omit them.

Usage:
    python3 pipeline/metrics_snapshot.py --mode polish --changed 16
    python3 pipeline/metrics_snapshot.py --mode wiki --changed 0 --dry-run
    python3 pipeline/metrics_snapshot.py --mode polish --changed 16 \
        --applied 3 --rejected 27 --flagged 0     # explicit override
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VALID_MODES = ["polish", "systemic-fix", "accuracy-review", "new-entries",
               "candidates", "wiki"]
DETECTORS = {
    "furigana_format": "build/check_furigana_format.py",
    "artifacts": "build/check_artifacts.py",
    "tag_drift": "build/check_tag_drift.py",
}
DETECTOR_MAX_AGE_DAYS = 7


def now_utc():
    return datetime.now(timezone.utc)


def today_str():
    return now_utc().date().isoformat()


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default


def count_lines(path):
    p = Path(path)
    if not p.exists():
        return 0
    return sum(1 for _ in p.open(encoding="utf-8"))


def read_jsonl(path):
    p = Path(path)
    if not p.exists():
        return
    for line in p.open(encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def decisions_today(root):
    """Tally today's APPLY/REJECT/FLAG decisions (aggregated lines count as n)."""
    tally = {"apply": 0, "reject": 0, "flag": 0}
    for d in read_jsonl(root / "reviews" / "decisions.jsonl"):
        if str(d.get("ts", ""))[:10] != today_str():
            continue
        dec = d.get("decision")
        if dec in tally:
            tally[dec] += int(d.get("n", 1))
    return tally


def metrics_today(history_rows):
    """Sum the flag fields already recorded in today's metrics rows."""
    sums = {"flags_applied": 0, "flags_rejected": 0, "flags_to_curator": 0}
    for row in history_rows:
        if str(row.get("ts", ""))[:10] != today_str():
            continue
        for k in sums:
            sums[k] += int(row.get(k) or 0)
    return sums


def detectors_stale(history_rows):
    cutoff = now_utc().timestamp() - DETECTOR_MAX_AGE_DAYS * 86400
    for row in reversed(history_rows):
        if "detectors" not in row:
            continue
        try:
            ts = datetime.strptime(row["ts"], "%Y-%m-%dT%H:%M:%SZ")
            return ts.replace(tzinfo=timezone.utc).timestamp() < cutoff
        except (ValueError, KeyError):
            continue
    return True


def collect_detectors(root):
    """Queue depth per read-only detector (full corpus scans — weekly only)."""
    depths = {}
    for name, script in DETECTORS.items():
        path = root / script
        if not path.exists():
            continue
        try:
            out = subprocess.run(
                [sys.executable, str(path), "--json"],
                capture_output=True, text=True, timeout=600, cwd=root,
            )
            items = json.loads(out.stdout) if out.returncode == 0 else None
            depths[name] = len(items) if isinstance(items, list) else None
        except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
            depths[name] = None
    return depths


def comprehensive_next(root):
    try:
        text = (root / "polishing/tasks/comprehensive/progress.txt").read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return None
    m = re.search(r"next:\s*(\d+)", text)
    return int(m.group(1)) if m else None


def ledger_spent_today(root):
    led = read_json(root / "pipeline/openrouter-ledger.json", {})
    if led.get("date") == today_str():
        return led.get("spent_usd")
    return 0.0


def build_row(args, root):
    history = list(read_jsonl(root / "pipeline/metrics-history.jsonl"))

    applied, rejected, flagged = args.applied, args.rejected, args.flagged
    if applied is None and rejected is None and flagged is None:
        decided = decisions_today(root)
        recorded = metrics_today(history)
        applied = max(0, decided["apply"] - recorded["flags_applied"])
        rejected = max(0, decided["reject"] - recorded["flags_rejected"])
        flagged = max(0, decided["flag"] - recorded["flags_to_curator"])

    cand = read_json(root / "candidate_words.json", {}) or {}
    idx = read_json(root / "entries_index.json", {}) or {}
    row = {
        "ts": now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mode": args.mode,
        "entries_changed": args.changed,
        "flags_applied": applied or 0,
        "flags_rejected": rejected or 0,
        "flags_to_curator": flagged or 0,
        "entries_total": len(idx.get("entries", [])) or None,
        "candidates": len(cand.get("candidates", [])) or None,
        "review_queue_len": count_lines(root / "reviews/queue.txt"),
        "observations_lines": count_lines(root / "polishing/observations.md"),
        "comprehensive_next": comprehensive_next(root),
        "openrouter_spent_today_usd": ledger_spent_today(root),
    }
    if args.full or detectors_stale(history):
        row["detectors"] = collect_detectors(root)
    return row


def main():
    ap = argparse.ArgumentParser(description="Append a Routine quality-metrics snapshot.")
    ap.add_argument("--mode", required=True, choices=VALID_MODES)
    ap.add_argument("--changed", type=int, default=0,
                    help="Entry files created or modified this run.")
    ap.add_argument("--applied", type=int, default=None,
                    help="Flags applied this run (default: derived from today's decisions.jsonl).")
    ap.add_argument("--rejected", type=int, default=None)
    ap.add_argument("--flagged", type=int, default=None,
                    help="Flags escalated to the curator this run.")
    ap.add_argument("--full", action="store_true",
                    help="Force the weekly detector-depth collectors.")
    ap.add_argument("--dry-run", action="store_true", help="Print the row; write nothing.")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent),
                    help="Project root (for tests).")
    args = ap.parse_args()

    root = Path(args.root)
    row = build_row(args, root)
    if not args.dry_run:
        with (root / "pipeline/metrics-history.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(("dry-run " if args.dry_run else "") + "metrics: "
          + json.dumps(row, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
