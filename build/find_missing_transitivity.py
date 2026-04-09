#!/usr/bin/env python3
"""
Find verb entries missing transitivity data (tag, notes, pair link).

Scans all entry JSON files and reports on verbs that are missing:
- transitivity tag in metadata.tags
- TRANSITIVITY section or 自動詞/他動詞 mention in notes
- pair link via prominent_see_also or cross_references with type "pair"

Usage:
    python3 build/find_missing_transitivity.py                # Full report
    python3 build/find_missing_transitivity.py --tier basic   # Filter to one tier
    python3 build/find_missing_transitivity.py --limit 20     # Limit missing list
    python3 build/find_missing_transitivity.py --json         # Machine-readable JSON
    python3 build/find_missing_transitivity.py --missing-only # Only list missing verbs
"""

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
ENTRIES_DIR = PROJECT_ROOT / 'entries'

sys.path.insert(0, str(SCRIPT_DIR))

from japanese_utils import strip_furigana

VERB_POS_TAGS = {'verb-godan', 'verb-ichidan', 'verb-suru', 'verb-kuru', 'verb-irregular'}

TIER_ORDER = {'basic': 0, 'core': 1, 'general': 2}


def is_verb(entry: dict) -> bool:
    """Check if an entry is a verb based on POS tags."""
    pos_tags = entry.get('metadata', {}).get('tags', {}).get('pos', [])
    return any(tag in VERB_POS_TAGS for tag in pos_tags)


def has_transitivity_tag(entry: dict) -> bool:
    """Check if the entry has a non-null transitivity tag."""
    tags = entry.get('metadata', {}).get('tags', {})
    val = tags.get('transitivity')
    return val is not None and val != ''


def has_transitivity_in_notes(entry: dict) -> bool:
    """Check if notes mention transitivity (自動詞, 他動詞, or TRANSITIVITY: header)."""
    notes = entry.get('notes', '') or ''
    stripped = strip_furigana(notes)
    return ('自動詞' in stripped or '他動詞' in stripped or 'TRANSITIVITY:' in notes)


def has_pair_link(entry: dict) -> bool:
    """Check if the entry has a pair verb linked via prominent_see_also or cross_references."""
    # Check prominent_see_also
    psa = entry.get('prominent_see_also', [])
    if psa:
        for ref in psa:
            note = (ref.get('note', '') or '').lower()
            if 'transitive' in note or 'intransitive' in note or 'pair' in note:
                return True
        # If prominent_see_also exists at all, it likely links the pair
        # (many entries use it primarily for transitivity pairs)
        return True

    # Check cross_references with type "pair"
    xrefs = entry.get('cross_references', [])
    for ref in xrefs:
        if ref.get('type') == 'pair':
            return True

    return False


def get_tier(entry: dict) -> str:
    """Get the vocabulary tier of an entry."""
    return entry.get('metadata', {}).get('vocabulary_tier', 'general')


def get_numeric_id(entry_id: str) -> int:
    """Extract the numeric portion of an entry ID."""
    return int(entry_id.split('_')[0])


def classify_verb(entry: dict) -> str:
    """Classify a verb as 'complete', 'partial', or 'missing'."""
    tag = has_transitivity_tag(entry)
    notes = has_transitivity_in_notes(entry)
    pair = has_pair_link(entry)

    count = sum([tag, notes, pair])
    if count == 0:
        return 'missing'
    elif count == 3:
        return 'complete'
    else:
        return 'partial'


def missing_parts(entry: dict) -> list[str]:
    """Return which parts of transitivity data are missing."""
    parts = []
    if not has_transitivity_tag(entry):
        parts.append('tag')
    if not has_transitivity_in_notes(entry):
        parts.append('notes')
    if not has_pair_link(entry):
        parts.append('pair')
    return parts


def scan_entries() -> list[dict]:
    """Scan all entry files and return verb entry data."""
    print("Scanning entries...", file=sys.stderr)
    verbs = []

    for json_file in sorted(ENTRIES_DIR.rglob('*.json')):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                entry = json.load(f)

            if not is_verb(entry):
                continue

            entry_id = entry.get('id', '')
            headword = strip_furigana(entry.get('headword', ''))
            reading = entry.get('reading', '')
            tier = get_tier(entry)

            verbs.append({
                'id': entry_id,
                'headword': headword,
                'reading': reading,
                'tier': tier,
                'has_tag': has_transitivity_tag(entry),
                'has_notes': has_transitivity_in_notes(entry),
                'has_pair': has_pair_link(entry),
                'classification': classify_verb(entry),
                'missing': missing_parts(entry),
            })
        except json.JSONDecodeError as e:
            print(f"Error parsing {json_file}: {e}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing {json_file}: {e}", file=sys.stderr)

    # Sort by tier priority, then numeric ID
    verbs.sort(key=lambda v: (TIER_ORDER.get(v['tier'], 99), get_numeric_id(v['id'])))
    return verbs


def build_summary(verbs: list[dict]) -> dict:
    """Build summary statistics from verb data."""
    total = len(verbs)
    with_tag = sum(1 for v in verbs if v['has_tag'])
    with_notes = sum(1 for v in verbs if v['has_notes'])
    with_pair = sum(1 for v in verbs if v['has_pair'])
    complete = sum(1 for v in verbs if v['classification'] == 'complete')
    missing = sum(1 for v in verbs if v['classification'] == 'missing')

    by_tier = {}
    for tier in ['basic', 'core', 'general']:
        tier_verbs = [v for v in verbs if v['tier'] == tier]
        tier_total = len(tier_verbs)
        tier_missing = sum(1 for v in tier_verbs if v['classification'] == 'missing')
        by_tier[tier] = {'total': tier_total, 'missing': tier_missing}

    return {
        'total': total,
        'with_tag': with_tag,
        'with_notes': with_notes,
        'with_pair': with_pair,
        'complete': complete,
        'missing': missing,
        'by_tier': by_tier,
    }


def pct(n: int, total: int) -> str:
    """Format a percentage string."""
    if total == 0:
        return '0.0'
    return f'{n / total * 100:.1f}'


def print_text_report(verbs: list[dict], summary: dict, limit: int | None, missing_only: bool):
    """Print a human-readable text report to stdout."""
    incomplete = [v for v in verbs if v['classification'] != 'complete']
    total = summary['total']

    if not missing_only:
        print("=== Verb Transitivity Report ===")
        print()
        print(f"Total verbs: {total}")
        print(f"With transitivity tag: {summary['with_tag']} ({pct(summary['with_tag'], total)}%)")
        print(f"With transitivity in notes: {summary['with_notes']} ({pct(summary['with_notes'], total)}%)")
        print(f"With pair link: {summary['with_pair']} ({pct(summary['with_pair'], total)}%)")
        print(f"Fully complete: {summary['complete']} ({pct(summary['complete'], total)}%)")
        print(f"Missing (no transitivity data at all): {summary['missing']} ({pct(summary['missing'], total)}%)")
        print()
        print("--- By Tier ---")
        for tier in ['basic', 'core', 'general']:
            t = summary['by_tier'].get(tier, {'total': 0, 'missing': 0})
            tier_label = f"{tier}:".ljust(10)
            print(f"{tier_label}{t['total']} verbs, {t['missing']} missing ({pct(t['missing'], t['total'])}%)")
        print()
        print("--- Verbs Missing Transitivity (sorted by tier priority) ---")

    display = incomplete[:limit] if limit else incomplete
    for v in display:
        missing_str = ', '.join(v['missing']) if v['missing'] else 'partial'
        print(f"{v['id']}  {v['headword']}  {v['reading']}  {v['tier']}  [{missing_str}]")

    if limit and len(incomplete) > limit:
        print(f"... and {len(incomplete) - limit} more")


def print_json_report(verbs: list[dict], summary: dict, limit: int | None):
    """Print machine-readable JSON report to stdout."""
    incomplete = [v for v in verbs if v['classification'] != 'complete']
    display = incomplete[:limit] if limit else incomplete

    output = {
        'summary': summary,
        'entries': display,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description='Find verb entries missing transitivity data'
    )
    parser.add_argument(
        '--tier',
        choices=['basic', 'core', 'general'],
        help='Filter output to only one tier'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=None,
        help='Limit the number of entries in the missing list (default: show all)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output machine-readable JSON instead of text report'
    )
    parser.add_argument(
        '--missing-only',
        action='store_true',
        help='Only print the list of verbs missing transitivity (skip summary stats)'
    )
    args = parser.parse_args()

    if not ENTRIES_DIR.exists():
        print(f"Error: entries directory not found at {ENTRIES_DIR}", file=sys.stderr)
        sys.exit(1)

    verbs = scan_entries()

    # Filter by tier if requested
    if args.tier:
        verbs = [v for v in verbs if v['tier'] == args.tier]

    summary = build_summary(verbs)

    print(f"Found {summary['total']} verb entries", file=sys.stderr)

    if args.json:
        print_json_report(verbs, summary, args.limit)
    else:
        print_text_report(verbs, summary, args.limit, args.missing_only)


if __name__ == '__main__':
    main()
