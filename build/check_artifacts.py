#!/usr/bin/env python3
"""Detect batch-creation artifacts and structural lint — READ-ONLY review queue.

Surfaces several recurring, wiki-documented defect classes so the Routine's
systemic-fix mode can verify and fix each instance. It never modifies entries.

Issues detected:
  register-trailer   `[Register: ...]` legacy trailer in notes (Cleanup P16, ~188)  [warn]
  teiru-brace        `{ている}` furigana-brace artifact (Cleanup P15, ~49)           [warn]
  surusuru           `するする` in notes — often a `する` typo in TRANSITIVITY/Pattern
                     lines (Cleanup P10), BUT can be the legitimate mimetic
                     adverb ("smoothly") — VERIFY each.                            [warn]
  dup-conjugation    duplicate top-level `"conjugation":` keys (Cleanup P4)        [warn]
  missing-target-id  a cross_references / prominent_see_also item without a
                     non-empty `target_id` (Cleanup P2)                            [warn]

Usage:
    python3 build/check_artifacts.py                 # human summary + sample
    python3 build/check_artifacts.py --summary
    python3 build/check_artifacts.py --json          # full JSON queue (for systemic-fix)
    python3 build/check_artifacts.py --issue teiru-brace
    python3 build/check_artifacts.py --range 5000 5500
"""
import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

CONJ_KEY_RE = re.compile(r'"conjugation"\s*:')
ISSUES = ["register-trailer", "teiru-brace", "surusuru", "dup-conjugation", "missing-target-id"]


def numeric_id(entry_id):
    m = re.match(r"(\d+)", str(entry_id))
    return int(m.group(1)) if m else None


def iter_entries(id_range=None):
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        try:
            raw = path.read_text(encoding="utf-8")
            data = json.loads(raw)
        except (json.JSONDecodeError, OSError):
            continue
        nid = numeric_id(data.get("id", path.stem))
        if id_range and nid is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        yield data, raw, path


def context(text, needle, width=36):
    i = text.find(needle)
    if i < 0:
        return None
    start = max(0, i - width // 2)
    return text[start:i + len(needle) + width // 2].replace("\n", "\\n")


def scan(id_range=None, only=None):
    records = []

    def add(eid, rel, issue, field, ctx, severity="warn", verify=None):
        records.append({
            "entry_id": eid, "file": rel, "issue": issue, "field": field,
            "context": ctx, "severity": severity, "verify": verify,
        })

    for data, raw, path in iter_entries(id_range):
        eid = data.get("id", path.stem)
        rel = str(path.relative_to(PROJECT_ROOT))
        notes = data.get("notes") or ""

        if only in (None, "register-trailer") and "[Register:" in notes:
            add(eid, rel, "register-trailer", "notes", context(notes, "[Register:"),
                verify="Confirm the formality field already carries this; then remove the trailer.")

        if only in (None, "teiru-brace"):
            for field, text in [("notes", notes)] + \
                    [(f"examples[{i}].japanese", ex.get("japanese") or "")
                     for i, ex in enumerate(data.get("examples", []) or [])]:
                if "{ている}" in text:
                    add(eid, rel, "teiru-brace", field, context(text, "{ている}"),
                        verify="Replace {ている} with plain ている (brace syntax is for kanji only).")

        if only in (None, "surusuru") and "するする" in notes:
            add(eid, rel, "surusuru", "notes", context(notes, "するする"),
                verify="MAY be legitimate mimetic 'smoothly'. Only fix if it is a "
                       "doubled する in a TRANSITIVITY/Pattern line.")

        if only in (None, "dup-conjugation") and len(CONJ_KEY_RE.findall(raw)) > 1:
            add(eid, rel, "dup-conjugation", "conjugation",
                f'{len(CONJ_KEY_RE.findall(raw))} "conjugation": keys',
                verify="Keep the full forms-array block; remove the legacy stub.")

        if only in (None, "missing-target-id"):
            for fld in ("cross_references", "prominent_see_also"):
                for j, ref in enumerate(data.get(fld, []) or []):
                    if isinstance(ref, dict) and not ref.get("target_id"):
                        label = ref.get("headword") or ref.get("reading") or "?"
                        add(eid, rel, "missing-target-id", f"{fld}[{j}]", label,
                            verify="Resolve the intended entry id, or drop the dangling reference.")

    return records


def main():
    ap = argparse.ArgumentParser(description="Detect batch-creation artifacts (read-only).")
    ap.add_argument("--json", action="store_true", help="Emit the full JSON review queue.")
    ap.add_argument("--summary", action="store_true", help="Print counts only.")
    ap.add_argument("--issue", choices=ISSUES, help="Filter to one issue type.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None, only=args.issue)

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    by_issue, entries = {}, set()
    for r in records:
        by_issue[r["issue"]] = by_issue.get(r["issue"], 0) + 1
        entries.add(r["entry_id"])
    print(f"Batch-creation artifacts: {len(records)} instances across {len(entries)} entries")
    for issue in ISSUES:
        if issue in by_issue:
            print(f"  {issue:18} {by_issue[issue]}")
    if not args.summary and records:
        print(f"\nSample (first {args.limit}):")
        for r in records[:args.limit]:
            print(f"  {r['entry_id']} [{r['issue']}] {r['field']}: {r['context']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
