#!/usr/bin/env python3
"""Detect noun entries whose example sentences never contain the headword.

Read-only review-queue generator for the Routine's systemic-fix mode
(Cleanup Backlog P19). Never modifies entries.

Motivating case (2026-06-10, curator-flagged): 00472 仕様 carried the example
こんなに壊れたら直しようがない — but 直しようがない is 直し + よう(様) + がない;
the string しよう only appears across a morpheme boundary. Such examples teach
the wrong word. A scan found two failure tiers among single-POS noun entries:

  reading-only     The kanji headword is absent but its kana reading appears
                   as a substring. Either a cross-boundary misparse (仕様 in
                   直しようがない) or legitimate kana orthography (ごちそう for
                   ご馳走) — per-entry judgment required.
  headword-absent  Neither the kanji form nor the reading appears. The example
                   may illustrate a related compound (東経 in a 経度 entry), a
                   verb form (仕組まれた in a 仕組み entry), or simply the
                   wrong word (目玉焼き in a 卵 entry).

Scope: entries whose POS is exactly ["noun"] and whose headword contains
kanji. Verbs/adjectives are excluded (inflection makes substring tests
meaningless); multi-POS entries are excluded to keep the queue high-precision.

Usage:
    python3 build/check_example_headword.py             # human summary + samples
    python3 build/check_example_headword.py --summary   # counts only
    python3 build/check_example_headword.py --json      # full review queue
    python3 build/check_example_headword.py --tier reading-only
    python3 build/check_example_headword.py --range 1 5000 --limit 50
"""
import argparse
import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

FURIGANA_RE = re.compile(r"\{([^|]+)\|[^}]+\}")
LINK_RE = re.compile(r"⟦([^⟧→]*)→[^⟧]*⟧")
KANJI_RE = re.compile(r"[一-鿿]")

VERIFY = ("Open the entry and judge each flagged example: kana orthography of "
          "the headword (e.g. ごちそう for ご馳走) is legitimate — skip it; an "
          "example that illustrates a different word or a cross-boundary string "
          "match should be replaced with a genuine example of the headword "
          "(with full inline links) or, if the entry has examples to spare, "
          "removed. Update the modified timestamp.")


def plain_jp(text):
    """Strip inline-link syntax and furigana wrappers to plain Japanese."""
    if not text:
        return ""
    text = LINK_RE.sub(lambda m: m.group(1), text)
    return FURIGANA_RE.sub(r"\1", text)


def numeric_id(stem):
    m = re.match(r"(\d+)", stem)
    return int(m.group(1)) if m else None


def classify_entry(entry):
    """Yield (tier, example_id, plain_text) for each suspect example."""
    tags = (entry.get("metadata") or {}).get("tags", {}) or {}
    if tags.get("pos") != ["noun"]:
        return
    headword = plain_jp(entry.get("headword", ""))
    if not headword or not KANJI_RE.search(headword):
        return
    reading = entry.get("reading", "") or ""
    for ex in entry.get("examples") or []:
        jp = plain_jp(ex.get("japanese", ""))
        if headword in jp:
            continue
        tier = "reading-only" if (reading and reading in jp) else "headword-absent"
        yield tier, ex.get("id"), jp.strip()


def scan(id_range=None):
    records = []
    for path in sorted(ENTRIES_DIR.glob("*/*.json")):
        nid = numeric_id(path.stem)
        if nid is None:
            continue
        if id_range and not (id_range[0] <= nid <= id_range[1]):
            continue
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for tier, ex_id, jp in classify_entry(entry):
            records.append({
                "entry_id": entry.get("id", path.stem),
                "file": str(path.relative_to(PROJECT_ROOT)),
                "headword": plain_jp(entry.get("headword", "")),
                "reading": entry.get("reading"),
                "example_id": ex_id,
                "example": jp[:80],
                "check": tier,
                "severity": "warn",
                "verify": VERIFY,
            })
    return records


def main():
    ap = argparse.ArgumentParser(
        description="Find noun entries whose examples never contain the headword (read-only).")
    ap.add_argument("--summary", action="store_true", help="Counts only.")
    ap.add_argument("--json", action="store_true", help="Full JSON review queue.")
    ap.add_argument("--tier", choices=["reading-only", "headword-absent"],
                    help="Filter to one tier.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--limit", type=int, default=25, help="Sample size (default 25).")
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None)
    if args.tier:
        records = [r for r in records if r["check"] == args.tier]

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    entries = {r["entry_id"] for r in records}
    by_tier = {}
    for r in records:
        by_tier[r["check"]] = by_tier.get(r["check"], 0) + 1
    print(f"Suspect examples: {len(records)} in {len(entries)} noun entries")
    for tier, n in sorted(by_tier.items()):
        print(f"  {tier:17} {n}")
    if not args.summary:
        print()
        for r in records[:args.limit]:
            print(f"  [{r['check']}] {r['entry_id']} {r['headword']} ({r['reading']}): {r['example']}")
        if len(records) > args.limit:
            print(f"  ... and {len(records) - args.limit} more (use --json for all)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
