#!/usr/bin/env python3
"""
Check if a word already exists in the dictionary or candidates.

This script MUST be run before creating any new dictionary entry or candidate.
It provides a hard block against duplicate additions.

Usage:
    # Check a word before creating an entry (entries-only, for picking from candidates)
    python build/check_duplicate.py --skip-candidates "食べる" "たべる"

    # Check a word before adding to candidates (full check)
    python build/check_duplicate.py "食べる" "たべる"

    # Batch mode with --skip-candidates (for creating entries from candidates)
    python build/check_duplicate.py --batch --skip-candidates "食べる:たべる" "飲む:のむ"

    # Batch mode full check (for adding new candidates)
    python build/check_duplicate.py --batch "食べる:たべる" "飲む:のむ" "書く:かく"

Exit codes:
    0 = Word is safe to add (not found anywhere checked)
    1 = Word is a duplicate (found in entries or candidates)
    2 = Error (invalid arguments, missing files, etc.)
"""

import json
import sys
from pathlib import Path

# Calculate paths relative to script location
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from japanese_utils import strip_furigana

ENTRIES_INDEX_FILE = PROJECT_ROOT / 'entries_index.json'
CANDIDATES_FILE = PROJECT_ROOT / 'candidate_words.json'


def load_json_file(filepath: Path) -> dict:
    """Load a JSON file, returning empty dict on error."""
    if not filepath.exists():
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, PermissionError) as e:
        print(f"Warning: Could not load {filepath}: {e}", file=sys.stderr)
        return {}


def check_word(word: str, reading: str, entries_data: dict, candidates_data: dict,
                skip_candidates: bool = False) -> dict:
    """
    Check if a word exists in the dictionary or candidates.

    Args:
        word: The word to check (may include furigana markup)
        reading: The reading in hiragana
        entries_data: Data from entries_index.json
        candidates_data: Data from candidate_words.json
        skip_candidates: If True, skip checking against candidates (use when
                         creating entries from the candidate list)

    Returns dict with:
        - is_duplicate: bool
        - found_in: 'entries' | 'candidates' | None
        - match_type: 'exact' | 'reading_only' | 'word_only' | None
        - details: str
    """
    result = {
        'is_duplicate': False,
        'found_in': None,
        'match_type': None,
        'details': None
    }

    clean_word = strip_furigana(word)

    # Check entries_index.json
    for entry in entries_data.get('entries', []):
        entry_reading = entry.get('reading', '')
        entry_headword = strip_furigana(entry.get('headword', ''))

        if entry_reading == reading and entry_headword == clean_word:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'exact',
                'details': f"Exact match: {entry['id']} ({entry_headword} / {entry_reading})"
            }

        if entry_reading == reading:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'reading_only',
                'details': f"Reading match: {entry['id']} ({entry_headword} / {entry_reading})"
            }

        if entry_headword == clean_word:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'word_only',
                'details': f"Headword match: {entry['id']} ({entry_headword} / {entry_reading})"
            }

    # Check candidate_words.json (unless skipped)
    if not skip_candidates:
        for cand in candidates_data.get('candidates', []):
            cand_reading = cand.get('reading', '')
            cand_word = cand.get('word', '')

            if cand_reading == reading and cand_word == clean_word:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'exact',
                    'details': f"Exact match in candidates: {cand['id']} ({cand_word} / {cand_reading})"
                }

            if cand_reading == reading:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'reading_only',
                    'details': f"Reading match in candidates: {cand['id']} ({cand_word} / {cand_reading})"
                }

            if cand_word == clean_word:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'word_only',
                    'details': f"Word match in candidates: {cand['id']} ({cand_word} / {cand_reading})"
                }

    return result


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    # Parse flags
    args = sys.argv[1:]
    skip_candidates = False
    batch_mode = False

    # Extract flags
    while args and args[0].startswith('--'):
        flag = args.pop(0)
        if flag == '--skip-candidates':
            skip_candidates = True
        elif flag == '--batch':
            batch_mode = True
        else:
            print(f"Unknown flag: {flag}")
            sys.exit(2)

    # Load data files once
    entries_data = load_json_file(ENTRIES_INDEX_FILE)
    candidates_data = load_json_file(CANDIDATES_FILE)

    if not entries_data.get('entries'):
        print("Warning: entries_index.json is empty or missing", file=sys.stderr)

    # Handle batch mode
    if batch_mode:
        if len(args) < 1:
            print("Usage: check_duplicate.py --batch [--skip-candidates] 'word1:reading1' 'word2:reading2' ...")
            sys.exit(2)

        has_duplicates = False
        for arg in args:
            if ':' not in arg:
                print(f"Invalid format: {arg} (expected 'word:reading')")
                continue

            word, reading = arg.split(':', 1)
            result = check_word(word, reading, entries_data, candidates_data, skip_candidates)

            if result['is_duplicate']:
                print(f"DUPLICATE: {word} ({reading}) - {result['details']}")
                has_duplicates = True
            else:
                print(f"OK: {word} ({reading})")

        sys.exit(1 if has_duplicates else 0)

    # Single word check
    if len(args) < 2:
        print("Usage: check_duplicate.py [--skip-candidates] <word> <reading>")
        print("   or: check_duplicate.py --batch [--skip-candidates] 'word1:reading1' 'word2:reading2' ...")
        sys.exit(2)

    word = args[0]
    reading = args[1]

    result = check_word(word, reading, entries_data, candidates_data, skip_candidates)

    if result['is_duplicate']:
        print(f"DUPLICATE: {result['details']}")
        print(f"\nDO NOT create an entry for '{word}' ({reading}) - it already exists!")
        sys.exit(1)
    else:
        check_type = "entries only" if skip_candidates else "dictionary or candidates"
        print(f"OK: '{word}' ({reading}) is not in the {check_type}.")
        print("Safe to create entry.")
        sys.exit(0)


if __name__ == '__main__':
    main()
