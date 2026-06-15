#!/usr/bin/env python3
"""Detect U+FFFD (replacement-character) mojibake corruption — READ-ONLY.

Companion detector to check_furigana_format.py / check_artifacts.py. It flags
entries that contain one or more U+FFFD (`�`) replacement characters embedded in
their text (headwords, readings, glosses, examples, notes, cross-references,
conjugation tables, …). These are the silent remains of a batch-creation episode
where UTF-8 multi-byte sequences were corrupted at write time — a kanji, a kana
of the standard reading, or an inline-link delimiter (⟦ ⟧ → ：) got replaced by
one or more `�`. They never render correctly on the live site.

This is the detector for Tooling Backlog item 16. It NEVER modifies entries; it
only produces a review queue so a human/agent can reconstruct each character from
its surrounding context. The furigana screener has false negatives on these, so a
direct scan (this script, or `grep -rlP '\\xEF\\xBF\\xBD' entries/`) is the
reliable way to surface them.

build/validate.py carries a hard guard that fails CI on any newly introduced
U+FFFD, so once this detector reports zero the corruption cannot recur.

Usage:
    python3 build/check_mojibake.py                 # human summary + sample
    python3 build/check_mojibake.py --summary       # counts only
    python3 build/check_mojibake.py --json          # full JSON queue (for systemic-fix)
    python3 build/check_mojibake.py --range 20000 21000
"""
import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

REPLACEMENT_CHAR = "�"
# A run of one-or-more U+FFFD with up to 18 non-space chars of context on each side.
RUN_RE = re.compile(r"\S{0,18}�+\S{0,18}")


def numeric_id(entry_id):
    m = re.match(r"(\d+)", str(entry_id))
    return int(m.group(1)) if m else None


def iter_entries(id_range=None):
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            continue
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = None
        nid = numeric_id((data or {}).get("id", path.stem))
        if id_range and nid is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        yield data, path, raw


def walk_strings(obj, prefix=""):
    """Yield (field_path, string) for every string value in a nested structure."""
    if isinstance(obj, str):
        yield prefix or "(root)", obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            child = f"{prefix}.{k}" if prefix else k
            yield from walk_strings(v, child)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            child = f"{prefix}[{i}]"
            yield from walk_strings(v, child)


def scan(id_range=None):
    """Return a list of per-entry records for every entry containing U+FFFD."""
    records = []
    for data, path, raw in iter_entries(id_range):
        if REPLACEMENT_CHAR not in raw:
            continue
        eid = (data or {}).get("id", path.stem)
        rel = str(path.relative_to(PROJECT_ROOT))
        fields = []
        if data is not None:
            for field_path, text in walk_strings(data):
                if REPLACEMENT_CHAR not in text:
                    continue
                runs = [m.group(0) for m in RUN_RE.finditer(text)]
                fields.append({
                    "field": field_path,
                    "count": text.count(REPLACEMENT_CHAR),
                    "contexts": runs,
                })
        records.append({
            "entry_id": eid,
            "file": rel,
            "count": raw.count(REPLACEMENT_CHAR),
            "fields": fields,
        })
    return records


def main():
    ap = argparse.ArgumentParser(description="Detect U+FFFD mojibake corruption (read-only).")
    ap.add_argument("--json", action="store_true", help="Emit the full JSON review queue.")
    ap.add_argument("--summary", action="store_true", help="Print counts only.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"), help="Limit to an ID range.")
    ap.add_argument("--limit", type=int, default=25, help="Sample size for the default view.")
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None)
    total_chars = sum(r["count"] for r in records)

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 1 if records else 0

    print(f"U+FFFD mojibake: {total_chars} replacement chars across {len(records)} entries")
    if not args.summary and records:
        print(f"\nSample (first {args.limit}, most-corrupted first):")
        for r in sorted(records, key=lambda r: -r["count"])[:args.limit]:
            print(f"  {r['entry_id']} ({r['count']} chars) — {r['file']}")
            for fl in r["fields"]:
                for ctx in fl["contexts"]:
                    print(f"      {fl['field']}: …{ctx}…")
    return 1 if records else 0


if __name__ == "__main__":
    sys.exit(main())
