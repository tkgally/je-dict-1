#!/usr/bin/env python3
"""
Dictionary health dashboard for je-dict-1.

Provides a quick summary of the dictionary's current state including
entry counts, type breakdowns, cross-reference stats, example coverage,
inline link usage, furigana coverage, and recent activity.

Usage:
    python3 build/report.py
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from constants import LINK_OPEN
from japanese_utils import FURIGANA_PATTERN, is_kanji, strip_furigana


def load_all_entries(entries_dir: Path) -> list[dict]:
    """Load all entry JSON files from the entries directory."""
    entries = []
    for file_path in sorted(entries_dir.glob('**/*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                entries.append(json.load(f))
        except (json.JSONDecodeError, IOError):
            pass
    return entries


def text_has_uncovered_kanji(text: str) -> bool:
    """Check if text contains kanji not wrapped in furigana markup."""
    stripped = FURIGANA_PATTERN.sub('', text)
    return any(is_kanji(ch) for ch in stripped)


def report_tier_breakdown(entries: list[dict]) -> None:
    """Print entry counts by vocabulary tier."""
    tier_counts = Counter()
    for entry in entries:
        tier = entry.get('metadata', {}).get('vocabulary_tier') or 'unset'
        tier_counts[tier] += 1

    print("VOCABULARY TIERS")
    print("-" * 40)
    for tier in ['basic', 'core', 'general', 'unset']:
        count = tier_counts.get(tier, 0)
        if count > 0:
            print(f"  {tier:<12} {count:>6}")
    print(f"  {'TOTAL':<12} {len(entries):>6}")
    print()


def report_pos_breakdown(entries: list[dict]) -> None:
    """Print entry counts by part-of-speech tag."""
    pos_counts = Counter()
    no_pos_count = 0
    for entry in entries:
        tags = entry.get('metadata', {}).get('tags', {})
        pos_list = tags.get('pos', [])
        if not pos_list:
            no_pos_count += 1
        for pos in pos_list:
            pos_counts[pos] += 1

    print("PART OF SPEECH (tags.pos)")
    print("-" * 40)
    for pos, count in pos_counts.most_common():
        print(f"  {pos:<24} {count:>6}")
    if no_pos_count:
        print(f"  {'(no pos tags)':<24} {no_pos_count:>6}")
    print()


def report_cross_references(entries: list[dict]) -> None:
    """Print cross-reference statistics."""
    total_refs = 0
    with_target_id = 0
    without_target_id = 0
    legacy_string = 0
    type_counts = Counter()
    entries_with_refs = 0

    all_ids = {e['id'] for e in entries}

    for entry in entries:
        refs = entry.get('cross_references', [])
        if refs:
            entries_with_refs += 1
        for ref in refs:
            total_refs += 1
            if isinstance(ref, str):
                legacy_string += 1
            elif isinstance(ref, dict):
                ref_type = ref.get('type', 'unknown')
                type_counts[ref_type] += 1
                if ref.get('target_id'):
                    target = ref['target_id']
                    if target in all_ids:
                        with_target_id += 1
                    else:
                        with_target_id += 1  # count as hardened even if stale
                else:
                    without_target_id += 1

    print("CROSS-REFERENCES")
    print("-" * 40)
    print(f"  Total references:      {total_refs:>6}")
    print(f"  Entries with refs:     {entries_with_refs:>6}")
    print(f"  Hardened (target_id):  {with_target_id:>6}")
    print(f"  Unhardened (lookup):   {without_target_id:>6}")
    if legacy_string:
        print(f"  Legacy string format:  {legacy_string:>6}")
    print()
    if type_counts:
        print("  By type:")
        for ref_type, count in type_counts.most_common():
            print(f"    {ref_type:<20} {count:>6}")
        print()


def report_examples(entries: list[dict]) -> None:
    """Print example sentence statistics."""
    total_examples = 0
    entries_with_zero = 0
    example_counts = []

    for entry in entries:
        examples = entry.get('examples', [])
        count = len(examples)
        total_examples += count
        example_counts.append(count)
        if count == 0:
            entries_with_zero += 1

    avg = total_examples / len(entries) if entries else 0

    print("EXAMPLE SENTENCES")
    print("-" * 40)
    print(f"  Total examples:        {total_examples:>6}")
    print(f"  Average per entry:     {avg:>9.1f}")
    print(f"  Entries with 0:        {entries_with_zero:>6}")

    # Distribution
    dist = Counter()
    for c in example_counts:
        if c == 0:
            dist['0'] += 1
        elif c <= 2:
            dist['1-2'] += 1
        elif c <= 4:
            dist['3-4'] += 1
        elif c <= 6:
            dist['5-6'] += 1
        elif c <= 9:
            dist['7-9'] += 1
        else:
            dist['10+'] += 1

    print("  Distribution:")
    for bucket in ['0', '1-2', '3-4', '5-6', '7-9', '10+']:
        count = dist.get(bucket, 0)
        print(f"    {bucket + ' examples':<20} {count:>6}")
    print()


def report_inline_links(entries: list[dict]) -> None:
    """Print inline word link coverage statistics."""
    entries_with_links = 0
    total_links = 0

    for entry in entries:
        entry_has_links = False
        for example in entry.get('examples', []):
            jp = example.get('japanese', '')
            link_count = jp.count(LINK_OPEN)
            if link_count > 0:
                entry_has_links = True
                total_links += link_count
        # Also check notes
        notes = entry.get('notes', '') or ''
        notes_links = notes.count(LINK_OPEN)
        if notes_links > 0:
            entry_has_links = True
            total_links += notes_links

        if entry_has_links:
            entries_with_links += 1

    pct = (entries_with_links / len(entries) * 100) if entries else 0

    print("INLINE WORD LINKS")
    print("-" * 40)
    print(f"  Entries with links:    {entries_with_links:>6} ({pct:.1f}%)")
    print(f"  Total link instances:  {total_links:>6}")
    print()


def report_furigana(entries: list[dict]) -> None:
    """Print furigana coverage statistics."""
    entries_checked = 0
    entries_with_gaps = 0
    gap_locations = Counter()  # which fields have gaps

    for entry in entries:
        entries_checked += 1
        has_gap = False

        # Check headword
        headword = entry.get('headword', '')
        if text_has_uncovered_kanji(headword):
            has_gap = True
            gap_locations['headword'] += 1

        # Check examples
        for example in entry.get('examples', []):
            jp = example.get('japanese', '')
            if text_has_uncovered_kanji(jp):
                has_gap = True
                gap_locations['examples'] += 1
                break  # count once per entry

        # Check notes
        notes = entry.get('notes', '') or ''
        if notes and text_has_uncovered_kanji(notes):
            has_gap = True
            gap_locations['notes'] += 1

        if has_gap:
            entries_with_gaps += 1

    covered = entries_checked - entries_with_gaps
    pct = (covered / entries_checked * 100) if entries_checked else 0

    print("FURIGANA COVERAGE")
    print("-" * 40)
    print(f"  Fully covered:         {covered:>6} ({pct:.1f}%)")
    print(f"  Entries with gaps:     {entries_with_gaps:>6}")
    if gap_locations:
        print("  Gap locations:")
        for loc, count in gap_locations.most_common():
            print(f"    {loc:<20} {count:>6}")
    print()


def report_recent_activity(entries: list[dict], days: int = 7) -> None:
    """Print entries modified in the last N days."""
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    recent = []

    for entry in entries:
        modified_str = entry.get('metadata', {}).get('modified', '')
        if not modified_str:
            continue
        try:
            dt = datetime.fromisoformat(modified_str.replace('Z', '+00:00'))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            if dt >= cutoff:
                recent.append((dt, entry['id'], entry.get('headword', '')))
        except (ValueError, AttributeError):
            pass

    recent.sort(key=lambda x: x[0], reverse=True)

    print(f"RECENT ACTIVITY (last {days} days)")
    print("-" * 40)
    print(f"  Entries modified:      {len(recent):>6}")
    if recent:
        shown = recent[:15]
        for dt, entry_id, headword in shown:
            date_str = dt.strftime('%Y-%m-%d')
            print(f"    {date_str}  {entry_id:<24} {headword}")
        if len(recent) > 15:
            print(f"    ... and {len(recent) - 15} more")
    print()


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if not entries_dir.exists():
        print(f"Error: entries directory not found: {entries_dir}")
        return 1

    print("Loading entries...")
    entries = load_all_entries(entries_dir)

    if not entries:
        print("No entries found.")
        return 1

    print(f"Loaded {len(entries)} entries.\n")
    print("=" * 40)
    print("  DICTIONARY HEALTH REPORT")
    print("=" * 40)
    print()

    report_tier_breakdown(entries)
    report_pos_breakdown(entries)
    report_cross_references(entries)
    report_examples(entries)
    report_inline_links(entries)
    report_furigana(entries)
    report_recent_activity(entries)

    return 0


if __name__ == '__main__':
    sys.exit(main())
