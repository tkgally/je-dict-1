#!/usr/bin/env python3
"""Audit dictionary coverage of semantic fields."""

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
FIELDS_FILE = SCRIPT_DIR / "data" / "semantic_fields.json"
INDEX_FILE = PROJECT_DIR / "entries_index.json"
CANDIDATES_FILE = PROJECT_DIR / "candidate_words.json"


def load_fields(fields_file=FIELDS_FILE):
    """Load semantic field definitions."""
    with open(fields_file) as f:
        return json.load(f)


def load_entry_index(index_file=INDEX_FILE):
    """Load entries_index.json and build a lookup set of (word, reading) pairs."""
    with open(index_file) as f:
        data = json.load(f)

    lookup = set()
    reading_only = set()  # for kana-only matching

    for entry in data["entries"]:
        headword = entry["headword"]
        reading = entry["reading"]
        lookup.add((headword, reading))
        reading_only.add(reading)

    return lookup, reading_only


def load_candidates(candidates_file=CANDIDATES_FILE):
    """Load candidate_words.json and build a lookup set of (word, reading) pairs."""
    if not candidates_file.exists():
        return set()

    with open(candidates_file) as f:
        data = json.load(f)

    lookup = set()
    for candidate in data.get("candidates", []):
        word = candidate.get("word", "")
        reading = candidate.get("reading", "")
        if word and reading:
            lookup.add((word, reading))
    return lookup


def is_all_kana(word):
    """Check if a word contains only kana (hiragana + katakana)."""
    for ch in word:
        cp = ord(ch)
        # Hiragana: U+3040-U+309F, Katakana: U+30A0-U+30FF
        if not (0x3040 <= cp <= 0x309F or 0x30A0 <= cp <= 0x30FF or ch in "ー"):
            return False
    return True


def audit_field(field, entry_lookup, reading_only, priority_filter=None):
    """Check coverage for a single semantic field. Returns dict with results."""
    expected = field["expected_words"]
    if priority_filter:
        expected = [w for w in expected if w["priority"] == priority_filter]

    found = []
    missing = []

    for word_entry in expected:
        word = word_entry["word"]
        reading = word_entry["reading"]

        # Check exact (headword, reading) match
        if (word, reading) in entry_lookup:
            found.append(word_entry)
        # For kana-only words, also match by reading alone
        elif is_all_kana(word) and reading in reading_only:
            found.append(word_entry)
        else:
            missing.append(word_entry)

    total = len(expected)
    found_count = len(found)
    coverage = (found_count / total * 100) if total > 0 else 100.0

    return {
        "id": field["id"],
        "name": field["name"],
        "category": field.get("category", ""),
        "total": total,
        "found": found_count,
        "coverage_percent": round(coverage, 1),
        "missing": missing
    }


def print_field_report(result, show_missing=True):
    """Print human-readable report for one field."""
    print(f"\n--- {result['id']} ({result['name']}) ---")
    print(f"Coverage: {result['found']}/{result['total']} ({result['coverage_percent']}%)")

    if show_missing and result["missing"]:
        by_priority = {"high": [], "medium": [], "low": []}
        for w in result["missing"]:
            by_priority[w["priority"]].append(w)

        for priority in ("high", "medium", "low"):
            words = by_priority[priority]
            print(f"Missing ({priority} priority):")
            if not words:
                print("  (none)")
            else:
                for w in words:
                    print(f"  {w['word']} ({w['reading']}) - {w['gloss']}")


def print_summary(results):
    """Print overall summary statistics."""
    total_expected = sum(r["total"] for r in results)
    total_found = sum(r["found"] for r in results)
    total_missing = total_expected - total_found
    overall_pct = (total_found / total_expected * 100) if total_expected > 0 else 100.0

    # Count missing by priority
    high_missing = 0
    medium_missing = 0
    low_missing = 0
    for r in results:
        for w in r["missing"]:
            if w["priority"] == "high":
                high_missing += 1
            elif w["priority"] == "medium":
                medium_missing += 1
            else:
                low_missing += 1

    print(f"\n=== Summary ===")
    print(f"Total fields: {len(results)}")
    print(f"Total expected words: {total_expected:,}")
    print(f"Found in dictionary: {total_found:,} ({overall_pct:.1f}%)")
    print(f"Missing: {total_missing:,} ({100 - overall_pct:.1f}%)")
    print(f"  High priority missing: {high_missing}")
    print(f"  Medium priority missing: {medium_missing}")
    print(f"  Low priority missing: {low_missing}")

    # Fields below 50%
    below_50 = [r for r in results if r["coverage_percent"] < 50.0]
    if below_50:
        print(f"\nFields below 50% coverage:")
        for r in sorted(below_50, key=lambda x: x["coverage_percent"]):
            print(f"  {r['id']} ({r['name']}): {r['found']}/{r['total']} ({r['coverage_percent']}%)")


def main():
    parser = argparse.ArgumentParser(description="Audit dictionary coverage of semantic fields.")
    parser.add_argument("--field", help="Audit a single field by ID")
    parser.add_argument("--category", help="Audit all fields in a category")
    parser.add_argument("--below", type=float, metavar="N", help="Show only fields with coverage below N%%")
    parser.add_argument("--priority", choices=["high", "medium", "low"], help="Filter by priority level")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Output in JSON format")
    parser.add_argument("--candidates", action="store_true", help="Output missing words in candidate format")
    parser.add_argument("--add-candidates", action="store_true", help="Directly add missing words as candidates")
    parser.add_argument("--summary", action="store_true", help="Show only summary, not individual missing words")
    args = parser.parse_args()

    # Load data
    if not FIELDS_FILE.exists():
        print(f"Error: {FIELDS_FILE} not found. Run build/assemble_semantic_fields.py first.",
              file=sys.stderr)
        sys.exit(1)

    field_data = load_fields()
    entry_lookup, reading_only = load_entry_index()

    # Filter fields
    fields = field_data["fields"]
    if args.field:
        fields = [f for f in fields if f["id"] == args.field]
        if not fields:
            print(f"Error: field '{args.field}' not found", file=sys.stderr)
            sys.exit(1)
    elif args.category:
        fields = [f for f in fields if f.get("category") == args.category]
        if not fields:
            print(f"Error: category '{args.category}' not found", file=sys.stderr)
            sys.exit(1)

    # Audit each field
    results = []
    for field in fields:
        result = audit_field(field, entry_lookup, reading_only, priority_filter=args.priority)
        results.append(result)

    # Filter by coverage threshold
    if args.below is not None:
        results = [r for r in results if r["coverage_percent"] < args.below]

    # Output
    if args.json_output:
        total_expected = sum(r["total"] for r in results)
        total_found = sum(r["found"] for r in results)
        overall_pct = (total_found / total_expected * 100) if total_expected > 0 else 100.0
        output = {
            "audit_date": str(date.today()),
            "total_fields": len(results),
            "total_expected": total_expected,
            "total_found": total_found,
            "coverage_percent": round(overall_pct, 1),
            "fields": results
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))

    elif args.candidates:
        for r in results:
            for w in r["missing"]:
                print(f"\"{w['word']}\" \"{w['reading']}\" \"{w['gloss']}\"")

    elif args.add_candidates:
        # Determine which priorities to include
        if args.priority:
            include_priorities = {args.priority}
        else:
            include_priorities = {"high", "medium"}

        candidate_lookup = load_candidates()
        added = 0
        already_existed = 0
        errors = 0

        for r in results:
            for w in r["missing"]:
                if w["priority"] not in include_priorities:
                    continue

                # Check if already a candidate
                if (w["word"], w["reading"]) in candidate_lookup:
                    print(f"  Already candidate: {w['word']} ({w['reading']})")
                    already_existed += 1
                    continue

                # Add via manage_candidates.py
                cmd = [
                    sys.executable,
                    str(SCRIPT_DIR / "manage_candidates.py"),
                    "add",
                    w["word"],
                    w["reading"],
                    w["gloss"]
                ]
                try:
                    result_proc = subprocess.run(cmd, capture_output=True, text=True)
                    if result_proc.returncode == 0:
                        if "already exists" in result_proc.stdout.lower():
                            print(f"  Already exists: {w['word']} ({w['reading']})")
                            already_existed += 1
                        else:
                            print(f"  Added: {w['word']} ({w['reading']}) - {w['gloss']}")
                            added += 1
                    else:
                        print(f"  Error adding {w['word']}: {result_proc.stderr.strip()}")
                        errors += 1
                except Exception as e:
                    print(f"  Error adding {w['word']}: {e}")
                    errors += 1

        print(f"\nSummary: Added {added} new candidates, {already_existed} already existed, {errors} errors")

    else:
        print("=== Semantic Field Coverage Report ===")
        for r in results:
            print_field_report(r, show_missing=not args.summary)
        print_summary(results)


if __name__ == "__main__":
    main()
