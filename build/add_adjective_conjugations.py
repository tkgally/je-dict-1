#!/usr/bin/env python3
"""
Add full conjugation tables to i-adjective entries.

Generates all conjugated forms for each i-adjective and writes them
directly into the entry JSON files. Handles the irregular いい/良い
pattern (いい compounds conjugate with よ- stem).

Usage:
    python3 build/add_adjective_conjugations.py                  # Process all
    python3 build/add_adjective_conjugations.py --start 0 --end 500
    python3 build/add_adjective_conjugations.py --dry-run        # Preview
    python3 build/add_adjective_conjugations.py --stats          # Statistics only

The conjugation field structure written to each entry:

    "conjugation": {
      "type": "i-adjective",       // or "ii" for いい compounds
      "forms": [
        {"label": "Present", "affirmative": "{高|たか}い", "negative": "{高|たか}くない"},
        {"label": "Past", "affirmative": "{高|たか}かった", "negative": "{高|たか}くなかった"},
        ...
      ]
    }
"""

import json
import sys
import os
import re
import glob
import argparse
from pathlib import Path

# Ensure build/ is on path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from japanese_utils import strip_furigana

# Furigana pattern: {漢字|かんじ}
FURIGANA_RE = re.compile(r'\{([^|{}]+)\|([^|{}]+)\}')

# Regular i-adjectives whose reading ends in いい but are NOT いい compounds.
# These conjugate regularly (e.g., かわいい → かわいくない, NOT かわよくない).
_REGULAR_II_ENDINGS = {'かわいい'}


def _generate_i_adjective_forms(stem: str) -> list:
    """Generate conjugation forms for a regular i-adjective.

    stem is the headword minus final い (e.g., {高|たか} for {高|たか}い).
    """
    s = stem
    return [
        {'label': 'Present', 'affirmative': f'{s}い', 'negative': f'{s}くない'},
        {'label': 'Past', 'affirmative': f'{s}かった', 'negative': f'{s}くなかった'},
        {'label': 'て form', 'affirmative': f'{s}くて', 'negative': f'{s}くなくて'},
        {'label': 'Adverbial', 'affirmative': f'{s}く', 'negative': None},
        {'label': 'Conditional ば', 'affirmative': f'{s}ければ', 'negative': f'{s}くなければ'},
        {'label': 'Conditional たら', 'affirmative': f'{s}かったら', 'negative': f'{s}くなかったら'},
    ]


def _generate_ii_forms(prefix: str) -> list:
    """Generate conjugation forms for いい or an いい compound.

    prefix is everything before いい (empty string for いい itself).
    All non-present forms use the よ- stem.
    """
    p = prefix
    return [
        {'label': 'Present', 'affirmative': f'{p}いい', 'negative': f'{p}よくない'},
        {'label': 'Past', 'affirmative': f'{p}よかった', 'negative': f'{p}よくなかった'},
        {'label': 'て form', 'affirmative': f'{p}よくて', 'negative': f'{p}よくなくて'},
        {'label': 'Adverbial', 'affirmative': f'{p}よく', 'negative': None},
        {'label': 'Conditional ば', 'affirmative': f'{p}よければ', 'negative': f'{p}よくなければ'},
        {'label': 'Conditional たら', 'affirmative': f'{p}よかったら', 'negative': f'{p}よくなかったら'},
    ]


def _strip_suffix_from_headword(headword: str, suffix: str) -> str:
    """Remove a plain-text suffix from headword, handling furigana notation."""
    if headword.endswith(suffix):
        return headword[:-len(suffix)]
    # Try stripping by plain text comparison
    plain = strip_furigana(headword)
    plain_suffix = strip_furigana(suffix)
    if plain.endswith(plain_suffix):
        target_len = len(plain) - len(plain_suffix)
        current_plain_len = 0
        i = 0
        while i < len(headword) and current_plain_len < target_len:
            if headword[i] == '{':
                end = headword.index('}', i)
                pipe = headword.index('|', i)
                kanji_len = pipe - i - 1
                current_plain_len += kanji_len
                i = end + 1
            else:
                current_plain_len += 1
                i += 1
        return headword[:i]
    return headword


def _detect_adjective_type(entry: dict) -> tuple:
    """
    Detect i-adjective type and extract stem/prefix.

    Returns: (adj_type, details_dict) or (None, None) if not an i-adjective.
    adj_type is 'i-adjective' or 'ii'.
    details_dict contains 'stem' (for regular) or 'prefix' (for ii).
    """
    tags = entry.get('metadata', {}).get('tags', {})
    pos_tags = tags.get('pos', [])

    if 'adjective-i' not in pos_tags:
        return None, None

    headword = entry.get('headword', '')
    reading = entry.get('reading', '')

    if not reading.endswith('い'):
        return None, None

    # Check for いい compounds: reading ends in いい and is not a known regular exception
    if reading.endswith('いい') and reading not in _REGULAR_II_ENDINGS:
        # This is an いい compound (or いい itself)
        prefix = _strip_suffix_from_headword(headword, 'いい')
        if prefix == headword:
            # Fallback: headword didn't end in いい literally; empty prefix
            prefix = ''
        return 'ii', {'prefix': prefix}

    # Regular i-adjective: stem = headword minus final い
    stem = _strip_suffix_from_headword(headword, 'い')
    if stem == headword:
        return None, None

    return 'i-adjective', {'stem': stem}


def generate_adjective_conjugation(entry: dict) -> dict:
    """
    Generate full conjugation data for an i-adjective entry.

    Returns a dict with 'type' and 'forms' keys, or None if not applicable.
    """
    adj_type, details = _detect_adjective_type(entry)
    if adj_type is None:
        return None

    if adj_type == 'ii':
        forms = _generate_ii_forms(details['prefix'])
    else:
        forms = _generate_i_adjective_forms(details['stem'])

    if not forms:
        return None

    return {
        'type': adj_type,
        'forms': forms,
    }


def process_entry_file(filepath: str, dry_run: bool = False) -> dict:
    """
    Process a single entry file, adding conjugation data if it's an i-adjective.

    Returns a status dict: {'status': 'added'|'skipped'|'error', 'type': ...}
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        return {'status': 'error', 'error': str(e)}

    conjugation = generate_adjective_conjugation(entry)
    if conjugation is None:
        return {'status': 'skipped', 'reason': 'not an i-adjective or undetectable'}

    entry['conjugation'] = conjugation

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(entry, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return {'status': 'added', 'type': conjugation['type'],
            'headword': entry.get('headword', ''),
            'id': entry.get('id', '')}


def main():
    parser = argparse.ArgumentParser(
        description='Add conjugation data to i-adjective entries')
    parser.add_argument('--start', type=int, default=0, help='Start ID (inclusive)')
    parser.add_argument('--end', type=int, default=99999, help='End ID (inclusive)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--stats', action='store_true', help='Print statistics only')
    parser.add_argument('--force', action='store_true',
                        help='Overwrite existing conjugation data')
    args = parser.parse_args()

    entries_dir = Path(__file__).parent.parent / 'entries'
    files = sorted(glob.glob(str(entries_dir / '**' / '*.json'), recursive=True))

    counts = {'added': 0, 'skipped': 0, 'error': 0, 'already': 0}
    type_counts = {}

    for filepath in files:
        basename = os.path.basename(filepath)
        match = re.match(r'^(\d{5})_', basename)
        if not match:
            continue
        entry_id = int(match.group(1))
        if entry_id < args.start or entry_id > args.end:
            continue

        # Check if already has conjugation data
        if not args.force:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if 'conjugation' in data and data['conjugation'].get('forms'):
                    counts['already'] += 1
                    continue
            except (json.JSONDecodeError, OSError):
                pass

        result = process_entry_file(filepath, dry_run=args.dry_run or args.stats)

        if result['status'] == 'added':
            counts['added'] += 1
            atype = result.get('type', 'unknown')
            type_counts[atype] = type_counts.get(atype, 0) + 1
            if args.dry_run:
                print(f"  {result.get('id', '?'):20s} {result.get('headword', '?'):20s} → {atype}")
        elif result['status'] == 'skipped':
            counts['skipped'] += 1
        elif result['status'] == 'error':
            counts['error'] += 1
            print(f"  ERROR {filepath}: {result.get('error', '?')}", file=sys.stderr)

    action = 'Would add' if (args.dry_run or args.stats) else 'Added'
    print(f"\n{action} conjugation to {counts['added']} entries")
    if counts['already']:
        print(f"Already had conjugation: {counts['already']}")
    print(f"Skipped (not i-adjective): {counts['skipped']}")
    if counts['error']:
        print(f"Errors: {counts['error']}")

    if type_counts:
        print("\nBy type:")
        for atype in sorted(type_counts):
            print(f"  {atype}: {type_counts[atype]}")


if __name__ == '__main__':
    main()
