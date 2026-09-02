#!/usr/bin/env python3
"""Regenerate planning/wiki/topics/quality-metrics.md from the metrics ledgers.

Replaces the hand-written "metrics trend" essay that the wiki mode used to
append to (39 refreshes, 35,000 words by 2026-08-27). This script derives the
same facts deterministically from pipeline/metrics-history.jsonl and
reviews/decisions.jsonl and writes a compact, dated page: a per-week table of
runs, entries changed, frontier, review queue, candidates, and spend; and a
per-dimension / per-family precision table for the reviewer flags. No model
involved; runs in well under a second.

Usage:
    python3 pipeline/metrics_report.py            # rewrite the wiki page
    python3 pipeline/metrics_report.py --stdout   # print instead of writing
    python3 pipeline/metrics_report.py --weeks 12 # how many weekly rows to show
"""
import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HISTORY = ROOT / "pipeline" / "metrics-history.jsonl"
DECISIONS = ROOT / "reviews" / "decisions.jsonl"
PAGE = ROOT / "planning" / "wiki" / "topics" / "quality-metrics.md"

MODES = ["polish", "accuracy-review", "systemic-fix", "new-entries", "candidates", "wiki"]


def read_jsonl(path):
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def parse_ts(s):
    try:
        return datetime.strptime(str(s)[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def week_key(dt):
    iso = dt.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def weekly_table(rows, weeks):
    by_week = defaultdict(list)
    for r in rows:
        dt = parse_ts(r.get("ts"))
        if dt:
            by_week[week_key(dt)].append(r)
    keys = sorted(by_week)[-weeks:]
    lines = ["| Week | Runs | Modes | Entries changed | Flags applied / rejected | Frontier | Review queue | Candidates | Entries | OpenRouter $ |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for k in keys:
        rs = by_week[k]
        modes = defaultdict(int)
        for r in rs:
            modes[r.get("mode")] += 1
        mode_s = " ".join(f"{m[:3]}{modes[m]}" for m in MODES if modes.get(m))
        last = rs[-1]
        spend = 0.0
        seen_days = {}
        for r in rs:  # ledger is per-day cumulative; take the max per day
            d = str(r.get("ts", ""))[:10]
            seen_days[d] = max(seen_days.get(d, 0.0), float(r.get("openrouter_spent_today_usd") or 0))
        spend = sum(seen_days.values())
        lines.append(
            f"| {k} | {len(rs)} | {mode_s} | {sum(int(r.get('entries_changed') or 0) for r in rs)} "
            f"| {sum(int(r.get('flags_applied') or 0) for r in rs)} / {sum(int(r.get('flags_rejected') or 0) for r in rs)} "
            f"| {last.get('comprehensive_next')} | {last.get('review_queue_len')} | {last.get('candidates')} "
            f"| {last.get('entries_total')} | {spend:.2f} |")
    return "\n".join(lines)


def precision_tables(decisions, since_days):
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    by_dim = defaultdict(lambda: defaultdict(int))
    by_family = defaultdict(lambda: defaultdict(int))
    for d in decisions:
        dt = parse_ts(d.get("ts"))
        if not dt or dt < cutoff:
            continue
        n = int(d.get("n", 1) or 1)
        dec = str(d.get("decision", "")).lower()
        if dec not in ("apply", "reject", "flag"):
            continue
        key = f"{d.get('src')}/{d.get('dim')}"
        by_dim[key][dec] += n
        fam = d.get("family") or "(unlabelled)"
        by_family[f"{d.get('dim')}:{fam}"][dec] += n

    def table(counter, title):
        lines = [f"| {title} | apply | reject | flag | precision |", "|---|---|---|---|---|"]
        for k in sorted(counter):
            c = counter[k]
            tot = c["apply"] + c["reject"] + c["flag"]
            prec = f"{c['apply'] / tot:.0%}" if tot else "-"
            lines.append(f"| {k} | {c['apply']} | {c['reject']} | {c['flag']} | {prec} |")
        return "\n".join(lines)

    return table(by_dim, "src/dim"), table(by_family, "dim:family")


def detector_line(rows):
    for r in reversed(rows):
        if r.get("detectors"):
            return f"Latest detector queue depths ({str(r.get('ts'))[:10]}): " + ", ".join(
                f"{k} {v}" for k, v in r["detectors"].items())
    return "No detector depths recorded yet."


def build_page(weeks):
    rows = read_jsonl(HISTORY)
    decisions = read_jsonl(DECISIONS)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    dim30, fam30 = precision_tables(decisions, 30)
    dim_all, _ = precision_tables(decisions, 36500)
    first = str(rows[0].get("ts"))[:10] if rows else "-"
    parts = [
        "# Quality Metrics",
        "",
        f"**Generated**: {now} by `pipeline/metrics_report.py` from "
        f"`pipeline/metrics-history.jsonl` ({len(rows)} runs since {first}) and "
        f"`reviews/decisions.jsonl` ({len(decisions)} adjudication lines). "
        "Do not edit by hand; rerun the script. The narrative history that used to live "
        "on this page is preserved in git (`git log -- planning/wiki/topics/quality-metrics.md`).",
        "",
        "## How to read this page",
        "",
        "- **Frontier** is the next entry ID of the sequential polish lane. **Review queue** is "
        "`reviews/queue.txt`: entries changed since their last external review (CI appends, the "
        "accuracy sweep drains). **Precision** is the share of reviewer flags that were applied; "
        "reject and flag (to curator) are the rest.",
        "- Per-family precision requires the `family` field that `build/review_accuracy.py` "
        "(prompt version 4, 2026-09-02) stamps on every issue; older decisions show as "
        "`(unlabelled)`.",
        "",
        f"## Weekly summary (last {weeks} weeks)",
        "",
        weekly_table(rows, weeks),
        "",
        detector_line(rows),
        "",
        "## Reviewer-flag precision, last 30 days",
        "",
        dim30,
        "",
        fam30,
        "",
        "## Reviewer-flag precision, all time",
        "",
        dim_all,
        "",
    ]
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Regenerate the quality-metrics wiki page.")
    ap.add_argument("--stdout", action="store_true", help="Print instead of writing.")
    ap.add_argument("--weeks", type=int, default=16)
    args = ap.parse_args()
    page = build_page(args.weeks)
    if args.stdout:
        sys.stdout.write(page)
    else:
        PAGE.parent.mkdir(parents=True, exist_ok=True)
        PAGE.write_text(page, encoding="utf-8")
        print(f"wrote {PAGE.relative_to(ROOT)} ({len(page.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
