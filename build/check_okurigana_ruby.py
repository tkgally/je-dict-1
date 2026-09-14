#!/usr/bin/env python3
"""Detect okurigana swallowed into a single-kanji furigana ruby — a READ-ONLY
review-queue generator.

Every existing furigana check (`check_furigana_format.py`, `verify_furigana.py`)
asks "does this kanji have a reading?" and stops there. That misses a shape
where the wrapper's surface side is a single bare kanji but the reading side
has absorbed okurigana that belongs outside the braces, e.g. `{痛|いたみ}`
(should be `{痛|いた}み`) or `{切|きり}` (should be `{切|き}り`). The site
renders the whole reading as the kanji's ruby, so the learner reads a wrong
(too-long) reading for the kanji. Addresses Cleanup Backlog P64 / Tooling 130.

Detection rule: for a single-kanji base K with reading R (R occurring at most
`--max-count` times for K across the dictionary), flag R if some proper
prefix of R is itself an attested reading of K occurring at least
`--min-prefix-count` times. Not mechanical: a flagged pair can be a genuine
longer reading (`{止|とど}` = とどまる) or a deliberate whole-word wrapper,
so every flag needs per-entry verification before a fix.

Usage:
    python3 build/check_okurigana_ruby.py                  # human summary + sample
    python3 build/check_okurigana_ruby.py --json            # full JSON queue
    python3 build/check_okurigana_ruby.py --range 5000 5500
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

WRAPPER_RE = re.compile(r"\{([^|{}]*)\|([^}{]*)\}")
HIRAGANA_RE = re.compile(r"^[ぁ-ゟー]+$")
LINK_TAIL_RE = re.compile(r"→[^⟧]*⟧")


def numeric_id(entry_id):
    m = re.match(r"(\d+)", str(entry_id))
    return int(m.group(1)) if m else None


def iter_entries(id_range=None):
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        nid = numeric_id(data.get("id", path.stem))
        if id_range and nid is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        yield data, path


def fields_of(data):
    if data.get("headword"):
        yield "headword", data["headword"]
    for i, ex in enumerate(data.get("examples", []) or []):
        if ex.get("japanese"):
            yield f"examples[{i}].japanese", ex["japanese"]
    if data.get("notes"):
        yield "notes", data["notes"]


def single_kanji_wrappers(id_range=None):
    """Yield (entry_id, file, field, left, right, match_text) for every
    wrapper whose surface side is exactly one kanji with a pure-hiragana
    reading (the shape this class needs)."""
    for data, path in iter_entries(id_range):
        eid = data.get("id", path.stem)
        rel = str(path.relative_to(PROJECT_ROOT))
        for label, raw in fields_of(data):
            text = LINK_TAIL_RE.sub("", raw)
            for m in WRAPPER_RE.finditer(text):
                left, right = m.group(1), m.group(2)
                if len(left) == 1 and HIRAGANA_RE.match(right or ""):
                    yield eid, rel, label, left, right, m.group(0)


def build_reading_counts(id_range=None):
    """Count occurrences of each (kanji, reading) pair dictionary-wide."""
    counts = Counter()
    for eid, rel, label, left, right, _ in single_kanji_wrappers(id_range):
        counts[(left, right)] += 1
    return counts


def scan(id_range=None, max_count=3, min_prefix_count=10):
    """Detect readings over id_range whose prefix is attested dictionary-wide
    (counts always measured over the full dictionary, regardless of range,
    so a --range scan still sees the true population)."""
    full_counts = build_reading_counts(None)
    by_kanji = defaultdict(dict)
    for (k, r), n in full_counts.items():
        by_kanji[k][r] = n

    records = []
    for eid, rel, label, left, right, orig in single_kanji_wrappers(id_range):
        n_right = full_counts[(left, right)]
        if n_right > max_count:
            continue
        best_prefix, best_count = None, 0
        for prefix, n_prefix in by_kanji[left].items():
            if prefix != right and len(prefix) < len(right) and right.startswith(prefix):
                if n_prefix >= min_prefix_count and n_prefix > best_count:
                    best_prefix, best_count = prefix, n_prefix
        if best_prefix is None:
            continue
        okurigana = right[len(best_prefix):]
        records.append({
            "entry_id": eid, "file": rel, "field": label,
            "kanji": left, "reading": right, "reading_count": n_right,
            "suggested_reading": best_prefix, "suggested_reading_count": best_count,
            "okurigana": okurigana,
            "original": orig,
            "suggestion": f"{{{left}|{best_prefix}}}{okurigana}",
        })
    return records


def main():
    ap = argparse.ArgumentParser(description="Detect okurigana swallowed into a single-kanji ruby (read-only).")
    ap.add_argument("--json", action="store_true", help="Emit the full JSON review queue.")
    ap.add_argument("--summary", action="store_true", help="Print counts only.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"), help="Limit to an ID range.")
    ap.add_argument("--max-count", type=int, default=3, help="Max dictionary-wide count for the flagged reading.")
    ap.add_argument("--min-prefix-count", type=int, default=10, help="Min dictionary-wide count for the prefix reading.")
    ap.add_argument("--limit", type=int, default=25, help="Sample size for the default view.")
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None, args.max_count, args.min_prefix_count)
    records.sort(key=lambda r: (-r["suggested_reading_count"], r["kanji"], r["entry_id"]))

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    pairs = {(r["kanji"], r["reading"]) for r in records}
    entries = {r["entry_id"] for r in records}
    print(f"Okurigana-swallowed rubies: {len(records)} instances / {len(pairs)} distinct pairs "
          f"across {len(entries)} entries")
    if not args.summary and records:
        print(f"\nSample (first {args.limit}, strongest signal first):")
        for r in records[:args.limit]:
            print(f"  {r['entry_id']} {r['field']}: {r['original']}  ->  {r['suggestion']}"
                  f"   ({{{r['kanji']}|{r['reading']}}}x{r['reading_count']} vs "
                  f"{{{r['kanji']}|{r['suggested_reading']}}}x{r['suggested_reading_count']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
