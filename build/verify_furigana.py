#!/usr/bin/env python3
"""
Verify that entries have complete furigana coverage in their notes field.

This script checks specific entries (by ID or file path) and reports any
kanji that are missing furigana annotation.
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional

from japanese_utils import FURIGANA_PATTERN

# Kanji Unicode ranges
KANJI_PATTERN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf]')


def check_entry_furigana(entry_path: Path) -> tuple[bool, list[str], list[str]]:
    """
    Check if an entry's notes field has complete furigana coverage.

    Returns:
        Tuple of (is_complete, unannotated_kanji, context_snippets)
    """
    try:
        with open(entry_path, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return False, [], [f"Error loading file: {e}"]

    notes = entry.get('notes', '')
    if not notes:
        return True, [], []

    # Remove furigana-annotated text
    text_without_furigana = FURIGANA_PATTERN.sub('', notes)

    # Find remaining kanji
    unannotated = list(set(KANJI_PATTERN.findall(text_without_furigana)))

    if not unannotated:
        return True, [], []

    # Get context snippets for unannotated kanji
    contexts = []
    parts = FURIGANA_PATTERN.split(notes)
    for part in parts:
        if KANJI_PATTERN.search(part):
            snippet = part.strip()
            if len(snippet) > 80:
                snippet = snippet[:80] + "..."
            if snippet and snippet not in contexts:
                contexts.append(snippet)

    return False, unannotated, contexts[:5]


def find_entry_file(entry_id: str, entries_dir: Path) -> Optional[Path]:
    """Find an entry file by its ID."""
    # Search for file matching the ID pattern
    for json_file in entries_dir.rglob(f'{entry_id}.json'):
        return json_file
    # Also try without the numeric suffix pattern
    for json_file in entries_dir.rglob('*.json'):
        if json_file.stem == entry_id:
            return json_file
    return None


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Verify furigana coverage in dictionary entries'
    )
    parser.add_argument(
        'entries',
        nargs='*',
        help='Entry IDs or file paths to check (if none, reads from stdin)'
    )
    parser.add_argument(
        '--entries-dir',
        default='entries',
        help='Path to entries directory'
    )
    parser.add_argument(
        '--quiet',
        '-q',
        action='store_true',
        help='Only output entries with issues'
    )

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / args.entries_dir

    # Get entries to check
    entries_to_check = args.entries
    if not entries_to_check:
        # Read from stdin (one entry ID or path per line)
        entries_to_check = [line.strip() for line in sys.stdin if line.strip()]

    if not entries_to_check:
        print("No entries specified. Usage: verify_furigana.py <entry_id_or_path> [...]")
        sys.exit(1)

    issues_found = 0
    entries_checked = 0

    for entry_spec in entries_to_check:
        # Determine if it's a path or an ID
        if entry_spec.endswith('.json'):
            entry_path = entries_dir / entry_spec
            if not entry_path.exists():
                entry_path = Path(entry_spec)
        else:
            entry_path = find_entry_file(entry_spec, entries_dir)

        if not entry_path or not entry_path.exists():
            print(f"WARNING: Entry not found: {entry_spec}", file=sys.stderr)
            continue

        entries_checked += 1
        is_complete, unannotated, contexts = check_entry_furigana(entry_path)

        if is_complete:
            if not args.quiet:
                print(f"✓ {entry_spec}: OK")
        else:
            issues_found += 1
            print(f"✗ {entry_spec}: Missing furigana for: {', '.join(unannotated)}")
            for ctx in contexts:
                print(f"    Context: {ctx}")

    print(f"\n--- Summary ---")
    print(f"Entries checked: {entries_checked}")
    print(f"Entries with issues: {issues_found}")
    print(f"Entries OK: {entries_checked - issues_found}")

    sys.exit(0 if issues_found == 0 else 1)


if __name__ == '__main__':
    main()
