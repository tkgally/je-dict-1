#!/usr/bin/env python3
"""
Manage the candidate words list (candidate_words.json).

This script provides utilities for managing candidate words that may be
added to the dictionary in the future.

Usage:
    # Add a single candidate (automatically checks for duplicates)
    python build/manage_candidates.py add "漢字" "かんじ" "Chinese characters - common word"

    # Add with --force to bypass duplicate check (use with caution!)
    python build/manage_candidates.py add --force "漢字" "かんじ" "note"

    # Check if a word is a duplicate (exits 0 if safe to add, 1 if duplicate)
    python build/manage_candidates.py check "漢字" "かんじ"

    # Remove candidates that now exist in dictionary
    python build/manage_candidates.py sync

    # Show statistics
    python build/manage_candidates.py stats
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

from japanese_utils import strip_furigana
from duplicate_utils import check_for_duplicate


# Calculate paths relative to script location
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CANDIDATES_FILE = PROJECT_ROOT / 'candidate_words.json'
ENTRIES_INDEX_FILE = PROJECT_ROOT / 'entries_index.json'
ENTRIES_DIR = PROJECT_ROOT / 'entries'


def load_candidates() -> dict:
    """Load the candidates file, or create empty structure if not exists."""
    if CANDIDATES_FILE.exists():
        try:
            with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {CANDIDATES_FILE}: {e}")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied reading {CANDIDATES_FILE}")
            sys.exit(1)
    return {
        'metadata': {
            'description': 'Candidate words to potentially add to the dictionary',
            'last_updated': None,
            'total_candidates': 0,
            'next_id': 1
        },
        'candidates': []
    }


def load_entries_index() -> dict:
    """Load the entries index file."""
    if ENTRIES_INDEX_FILE.exists():
        try:
            with open(ENTRIES_INDEX_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {ENTRIES_INDEX_FILE}: {e}")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied reading {ENTRIES_INDEX_FILE}")
            sys.exit(1)
    return {'metadata': {}, 'entries': []}


def check_duplicate(word: str, reading: str, candidates_data: dict = None) -> dict:
    """
    Check if a word already exists in entries or candidates.

    This is a wrapper around the shared check_for_duplicate function
    that handles loading the entries index.

    Returns a dict with:
        - is_duplicate: bool
        - found_in: 'entries' | 'candidates' | None
        - match_type: 'exact' | 'reading_only' | 'word_only' | None
        - details: str with match information
    """
    entries_data = load_entries_index()
    if candidates_data is None:
        candidates_data = load_candidates()

    return check_for_duplicate(word, reading, entries_data, candidates_data)


def save_candidates(data: dict):
    """Save the candidates file."""
    data['metadata']['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    data['metadata']['total_candidates'] = len(data['candidates'])

    try:
        with open(CANDIDATES_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except PermissionError:
        print(f"Error: Permission denied writing to {CANDIDATES_FILE}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: Could not write to {CANDIDATES_FILE}: {e}")
        sys.exit(1)


def get_existing_entries() -> set:
    """Get set of (reading, headword) tuples from existing dictionary entries."""
    existing = set()

    if not ENTRIES_DIR.exists():
        print(f"Warning: Entries directory not found: {ENTRIES_DIR}")
        return existing

    for entry_file in ENTRIES_DIR.rglob('*.json'):
        try:
            with open(entry_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                reading = data.get('reading', '')
                headword = data.get('headword', '')
                # Clean headword of furigana notation
                clean_headword = strip_furigana(headword)
                existing.add((reading, clean_headword))
        except json.JSONDecodeError as e:
            print(f"Warning: Invalid JSON in {entry_file}: {e}")
        except PermissionError:
            print(f"Warning: Permission denied reading {entry_file}")

    return existing


def generate_candidate_id(data: dict) -> str:
    """Generate next candidate ID."""
    next_id = data['metadata']['next_id']
    data['metadata']['next_id'] = next_id + 1
    return f"C{next_id:05d}"


def add_candidate(data: dict, word: str, reading: str = None, notes: str = None) -> dict:
    """Add a single candidate to the list."""
    candidate = {
        'id': generate_candidate_id(data),
        'word': word,
        'reading': reading,
        'notes': notes,
        'added': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    data['candidates'].append(candidate)
    return candidate


def sync_with_dictionary(data: dict) -> int:
    """Remove candidates that now exist in the dictionary."""
    existing = get_existing_entries()

    original_count = len(data['candidates'])
    data['candidates'] = [
        c for c in data['candidates']
        if (c.get('reading'), c.get('word')) not in existing
    ]

    removed_count = original_count - len(data['candidates'])
    return removed_count


def show_stats(data: dict):
    """Show statistics about the candidates list."""
    print(f"Total candidates: {len(data['candidates'])}")
    print(f"Next ID: C{data['metadata']['next_id']:05d}")
    if data['metadata'].get('last_updated'):
        print(f"Last updated: {data['metadata']['last_updated']}")

    # Count by first character
    by_char = {}
    for c in data['candidates']:
        word = c.get('word', '')
        if word:
            first_char = word[0]
            by_char[first_char] = by_char.get(first_char, 0) + 1

    print(f"\nTop 10 starting characters:")
    for char, count in sorted(by_char.items(), key=lambda x: -x[1])[:10]:
        print(f"  {char}: {count}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]

    # Handle --force flag for add command
    force = False
    args = sys.argv[2:]
    if '--force' in args:
        force = True
        args = [a for a in args if a != '--force']

    data = load_candidates()

    if command == 'add':
        if len(args) < 1:
            print("Usage: manage_candidates.py add [--force] <word> [reading] [notes]")
            print("\nOptions:")
            print("  --force    Skip duplicate check (use with caution!)")
            return

        word = args[0]
        reading = args[1] if len(args) > 1 else None
        notes = args[2] if len(args) > 2 else None

        # Check for duplicates BEFORE adding (unless --force)
        if not force and reading:
            dup_check = check_duplicate(word, reading, data)
            if dup_check['is_duplicate']:
                print(f"ERROR: Duplicate detected!")
                print(f"  {dup_check['details']}")
                print(f"\nThis word already exists. NOT adding to candidates.")
                print(f"Use --force to bypass this check (not recommended).")
                sys.exit(1)

        candidate = add_candidate(data, word, reading, notes)
        save_candidates(data)
        print(f"Added candidate: {candidate['id']} - {word}")

    elif command == 'check':
        # Check command: verify if a word is a duplicate
        if len(args) < 2:
            print("Usage: manage_candidates.py check <word> <reading>")
            print("\nChecks if a word exists in entries_index.json or candidate_words.json.")
            print("Exit code 0 = safe to add, exit code 1 = duplicate found")
            return

        word = args[0]
        reading = args[1]

        dup_check = check_duplicate(word, reading, data)
        if dup_check['is_duplicate']:
            print(f"DUPLICATE: {dup_check['details']}")
            sys.exit(1)
        else:
            print(f"OK: '{word}' ({reading}) is not in the dictionary or candidates.")
            sys.exit(0)

    elif command == 'sync':
        removed = sync_with_dictionary(data)
        save_candidates(data)
        print(f"Removed {removed} candidates that now exist in dictionary")
        print(f"Remaining candidates: {len(data['candidates'])}")

    elif command == 'stats':
        show_stats(data)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == '__main__':
    main()
