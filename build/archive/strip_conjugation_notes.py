#!/usr/bin/env python3
"""
Strip free-text CONJUGATION: blocks from entry notes fields.

Targets verb and i-adjective entries that now have structured conjugation data
in the conjugation JSON field, making the notes-embedded CONJUGATION: block
redundant.

Usage:
    python3 build/strip_conjugation_notes.py --dry-run   # Preview changes
    python3 build/strip_conjugation_notes.py              # Apply changes
"""

import json
import glob
import re
import argparse
from pathlib import Path


def strip_conjugation_block(notes: str) -> str:
    """Remove a CONJUGATION: block (header + bullet lines) from notes text.

    The block pattern is:
        CONJUGATION:
        - line 1
        - line 2
        ...

    Also removes surrounding blank lines left by the removal.
    """
    if 'CONJUGATION:' not in notes:
        return notes

    # Match: optional leading newline, CONJUGATION: header, bullet lines, trailing blank lines
    # The block is: CONJUGATION:\n followed by lines starting with "- "
    pattern = r'\n*CONJUGATION:\n(?:- [^\n]*\n?)*\n*'
    result = re.sub(pattern, '\n\n', notes)

    # Clean up: collapse triple+ newlines to double
    result = re.sub(r'\n{3,}', '\n\n', result)

    # Strip leading/trailing whitespace
    result = result.strip()

    return result


def has_structured_conjugation(entry: dict) -> bool:
    """Check if entry has a structured conjugation field with forms."""
    conj = entry.get('conjugation', {})
    return bool(conj and conj.get('forms'))


def main():
    parser = argparse.ArgumentParser(
        description='Strip CONJUGATION: blocks from notes in verb and i-adjective entries')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    args = parser.parse_args()

    entries_dir = Path(__file__).parent.parent / 'entries'
    files = sorted(glob.glob(str(entries_dir / '**' / '*.json'), recursive=True))

    changed = 0
    skipped_no_block = 0
    skipped_no_conj = 0

    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                entry = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        notes = entry.get('notes', '') or ''
        if 'CONJUGATION:' not in notes:
            skipped_no_block += 1
            continue

        # Only strip if entry has structured conjugation data
        if not has_structured_conjugation(entry):
            skipped_no_conj += 1
            continue

        new_notes = strip_conjugation_block(notes)

        if new_notes == notes:
            skipped_no_block += 1
            continue

        if args.dry_run:
            entry_id = entry.get('id', filepath)
            print(f"=== {entry_id} ===")
            print(f"BEFORE ({len(notes)} chars):")
            print(notes)
            print(f"\nAFTER ({len(new_notes)} chars):")
            print(new_notes)
            print("\n" + "=" * 60 + "\n")
        else:
            entry['notes'] = new_notes
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(entry, f, ensure_ascii=False, indent=2)
                f.write('\n')

        changed += 1

    action = 'Would strip' if args.dry_run else 'Stripped'
    print(f"\n{action} CONJUGATION: from {changed} entries")
    print(f"Skipped (no CONJUGATION: block): {skipped_no_block}")
    print(f"Skipped (no structured conjugation data): {skipped_no_conj}")


if __name__ == '__main__':
    main()
