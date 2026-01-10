#!/usr/bin/env python3
"""
Cross-Reference Extraction for je-dict-1

This script parses notes fields in dictionary entries and extracts
potential cross-references based on common patterns.

Usage:
    python3 extract_references.py              # Dry run - show proposed changes
    python3 extract_references.py --apply      # Apply changes to entry files
    python3 extract_references.py --id <id>    # Process single entry
"""

import json
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple


# Pattern to extract furigana notation: {kanji|reading}
FURIGANA_PATTERN = re.compile(r'\{([^|]+)\|([^}]+)\}')


def extract_furigana_words(text: str) -> List[Tuple[str, str]]:
    """
    Extract all words with furigana notation from text.
    Returns list of (headword, reading) tuples.
    """
    return [(match.group(0), match.group(2)) for match in FURIGANA_PATTERN.finditer(text)]


def extract_word_after_keyword(notes: str, keywords: List[str]) -> Optional[Tuple[str, str, str]]:
    """
    Extract a Japanese word following specified keywords.
    Returns (headword, reading, label) tuple or None.

    Handles compound words like:
    - {閉|し}まる (furigana + hiragana)
    - {召|め}し{上|あ}がる (multiple furigana groups)
    - いただく (plain hiragana)
    """
    for keyword in keywords:
        # Build pattern: keyword followed by optional colon/space, then the word
        # Word can be: furigana groups optionally followed by hiragana, or plain hiragana
        pattern = (
            keyword +
            r'[:\s]*' +
            r'((?:\{[^}]+\})+[ぁ-んァ-ヴー]*|[ぁ-んァ-ヴー]+)' +
            r'(?:\s*\(([^)]+)\))?'
        )

        match = re.search(pattern, notes, re.IGNORECASE)
        if match:
            headword = match.group(1)
            label = match.group(2) if match.lastindex >= 2 and match.group(2) else None

            # Extract reading by combining furigana readings and plain hiragana
            reading = ''
            i = 0
            while i < len(headword):
                if headword[i] == '{':
                    # Find the reading part
                    pipe = headword.find('|', i)
                    close = headword.find('}', i)
                    if pipe != -1 and close != -1:
                        reading += headword[pipe+1:close]
                        i = close + 1
                    else:
                        i += 1
                else:
                    reading += headword[i]
                    i += 1

            return (headword, reading, label)

    return None


def extract_pair_verb(notes: str) -> Optional[Dict[str, Any]]:
    """
    Extract transitivity pair verb from notes.

    Patterns:
    - "Pair: {閉|し}まる" or "PAIR: {閉|し}まる"
    - "Pair verb: {閉|し}まる (intransitive)"
    - "PAIR VERB: ..." (any case)
    """
    keywords = [
        r'[Pp]air\s+verb',
        r'PAIR\s+VERB',
        r'[Pp]air',
        r'PAIR',
    ]

    result = extract_word_after_keyword(notes, keywords)
    if result:
        headword, reading, label = result

        # Determine label from context if not explicit
        if not label:
            if 'intransitive' in notes.lower():
                label = 'intransitive'
            elif 'transitive' in notes.lower():
                label = 'transitive'

        return {
            'type': 'pair',
            'reading': reading,
            'headword': headword,
            'label': label
        }

    return None


def extract_antonym(notes: str) -> Optional[Dict[str, Any]]:
    """
    Extract antonym from notes.

    Patterns:
    - "Opposite: {開|あ}ける"
    - "Antonym: ..."
    """
    keywords = [
        r'[Oo]pposite',
        r'[Aa]ntonym',
    ]

    result = extract_word_after_keyword(notes, keywords)
    if result:
        headword, reading, label = result
        return {
            'type': 'antonym',
            'reading': reading,
            'headword': headword,
            'label': label
        }

    return None


def extract_keigo(notes: str) -> List[Dict[str, Any]]:
    """
    Extract keigo (honorific/humble) forms from notes.

    Patterns:
    - "honorific: {召|め}し{上|あ}がる" or similar
    - "{召|め}し{上|あ}がる (honorific)"
    """
    refs = []

    # Look for honorific patterns
    honorific_patterns = [
        r'[Hh]onorific[:\s]+(\{[^|]+\|[^}]+\}(?:\{[^|]+\|[^}]+\})*)',
        r'(\{[^|]+\|[^}]+\}(?:\{[^|]+\|[^}]+\})*)\s*\([Hh]onorific\)',
    ]

    for pattern in honorific_patterns:
        match = re.search(pattern, notes)
        if match:
            headword = match.group(1)
            # Extract reading by combining all readings
            readings = FURIGANA_PATTERN.findall(headword)
            if readings:
                reading = ''.join(r[1] for r in readings)
                refs.append({
                    'type': 'keigo',
                    'reading': reading,
                    'headword': headword,
                    'label': 'honorific'
                })
                break

    # Look for humble patterns
    humble_patterns = [
        r'[Hh]umble[:\s]+(\{[^|]+\|[^}]+\}(?:\{[^|]+\|[^}]+\})*)',
        r'(\{[^|]+\|[^}]+\}(?:\{[^|]+\|[^}]+\})*)\s*\([Hh]umble\)',
    ]

    for pattern in humble_patterns:
        match = re.search(pattern, notes)
        if match:
            headword = match.group(1)
            readings = FURIGANA_PATTERN.findall(headword)
            if readings:
                reading = ''.join(r[1] for r in readings)
                refs.append({
                    'type': 'keigo',
                    'reading': reading,
                    'headword': headword,
                    'label': 'humble'
                })
                break

    return refs


def extract_see_also(notes: str) -> List[Dict[str, Any]]:
    """
    Extract "See also" references from notes.

    Patterns:
    - "See also: {X|y}, {Z|w}"
    - "See: ..."
    """
    refs = []

    pattern = r'[Ss]ee(?:\s+also)?[:\s]+(.+?)(?:\.|$|\n)'
    match = re.search(pattern, notes)
    if match:
        content = match.group(1)
        # Extract all furigana words from the "See also" section
        words = extract_furigana_words(content)
        for headword, reading in words:
            refs.append({
                'type': 'see_also',
                'reading': reading,
                'headword': headword,
                'label': None
            })

    return refs


def extract_references_from_entry(entry: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract all potential cross-references from an entry's notes field.
    """
    notes = entry.get('notes', '')
    if not notes:
        return []

    refs = []
    entry_reading = entry.get('reading', '')

    # Extract pair verb
    pair = extract_pair_verb(notes)
    if pair and pair['reading'] != entry_reading:
        refs.append(pair)

    # Extract antonym
    antonym = extract_antonym(notes)
    if antonym and antonym['reading'] != entry_reading:
        refs.append(antonym)

    # Extract keigo forms
    keigo_refs = extract_keigo(notes)
    for ref in keigo_refs:
        if ref['reading'] != entry_reading:
            refs.append(ref)

    # Extract see also
    see_also_refs = extract_see_also(notes)
    for ref in see_also_refs:
        if ref['reading'] != entry_reading:
            refs.append(ref)

    # Remove duplicates (same reading)
    seen_readings = set()
    unique_refs = []
    for ref in refs:
        if ref['reading'] not in seen_readings:
            seen_readings.add(ref['reading'])
            unique_refs.append(ref)

    return unique_refs


def merge_references(existing: List, new: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Merge new references with existing ones.
    Preserves existing structured refs, converts legacy string refs,
    and adds new refs that don't duplicate existing ones.
    """
    result = []
    existing_readings = set()

    # Process existing references
    for ref in existing:
        if isinstance(ref, str):
            # Legacy format - keep as is for now (will be resolved at build time)
            result.append(ref)
        elif isinstance(ref, dict):
            result.append(ref)
            reading = ref.get('reading', '')
            if reading:
                existing_readings.add(reading)

    # Add new references that don't duplicate
    for ref in new:
        if ref['reading'] not in existing_readings:
            result.append(ref)
            existing_readings.add(ref['reading'])

    return result


def process_entry(entry_path: Path, dry_run: bool = True) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Process a single entry file and extract/add cross-references.

    Returns:
        Tuple of (was_modified, list of added references)
    """
    with open(entry_path, 'r', encoding='utf-8') as f:
        entry = json.load(f)

    # Extract references from notes
    extracted_refs = extract_references_from_entry(entry)

    if not extracted_refs:
        return False, []

    # Get existing cross-references
    existing_refs = entry.get('cross_references', [])

    # Merge
    merged_refs = merge_references(existing_refs, extracted_refs)

    # Check if anything changed
    if len(merged_refs) == len(existing_refs):
        return False, []

    # Calculate what was added
    added_refs = merged_refs[len(existing_refs):]

    if not dry_run:
        # Update entry
        entry['cross_references'] = merged_refs
        entry['metadata']['modified'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

        # Write back
        with open(entry_path, 'w', encoding='utf-8') as f:
            json.dump(entry, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return True, added_refs


def process_all_entries(project_root: Path, dry_run: bool = True) -> Dict[str, Any]:
    """
    Process all entry files and extract cross-references.

    Returns a report dictionary.
    """
    entries_dir = project_root / 'entries'

    report = {
        'total_entries': 0,
        'entries_with_new_refs': 0,
        'total_new_refs': 0,
        'changes': []
    }

    for entry_path in sorted(entries_dir.rglob('*.json')):
        report['total_entries'] += 1

        try:
            was_modified, added_refs = process_entry(entry_path, dry_run)

            if was_modified:
                report['entries_with_new_refs'] += 1
                report['total_new_refs'] += len(added_refs)
                report['changes'].append({
                    'file': str(entry_path.relative_to(project_root)),
                    'added': added_refs
                })
        except Exception as e:
            print(f"Error processing {entry_path}: {e}", file=sys.stderr)

    return report


def print_report(report: Dict[str, Any], dry_run: bool = True):
    """Print a formatted report of the extraction results."""
    print("=" * 60)
    print("Cross-Reference Extraction Report")
    print("=" * 60)
    print(f"Mode: {'DRY RUN (no changes made)' if dry_run else 'APPLIED'}")
    print(f"Total entries scanned: {report['total_entries']}")
    print(f"Entries with new references: {report['entries_with_new_refs']}")
    print(f"Total new references found: {report['total_new_refs']}")
    print()

    if report['changes']:
        print("Changes:")
        print("-" * 60)
        for change in report['changes']:
            print(f"\n{change['file']}:")
            for ref in change['added']:
                ref_type = ref.get('type', 'unknown')
                reading = ref.get('reading', '')
                headword = ref.get('headword', reading)
                label = ref.get('label', '')
                label_str = f" ({label})" if label else ""
                print(f"  + {ref_type}: {headword}{label_str}")

    if dry_run and report['entries_with_new_refs'] > 0:
        print()
        print("To apply these changes, run:")
        print("  python3 build/extract_references.py --apply")


def main():
    parser = argparse.ArgumentParser(
        description='Extract cross-references from dictionary entry notes'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply changes to entry files (default is dry run)'
    )
    parser.add_argument(
        '--id',
        type=str,
        help='Process only the entry with this ID'
    )
    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if args.id:
        # Process single entry
        entry_path = None
        for path in entries_dir.rglob(f'{args.id}.json'):
            entry_path = path
            break

        if not entry_path:
            print(f"Entry not found: {args.id}", file=sys.stderr)
            return 1

        was_modified, added_refs = process_entry(entry_path, dry_run=not args.apply)

        if was_modified:
            print(f"{'Would add' if not args.apply else 'Added'} {len(added_refs)} reference(s):")
            for ref in added_refs:
                print(f"  + {ref['type']}: {ref.get('headword', ref['reading'])}")
        else:
            print("No new references found.")

        return 0

    # Process all entries
    report = process_all_entries(project_root, dry_run=not args.apply)
    print_report(report, dry_run=not args.apply)

    return 0


if __name__ == '__main__':
    sys.exit(main())
