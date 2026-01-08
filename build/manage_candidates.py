#!/usr/bin/env python3
"""
Manage the candidate words list (candidate_words.json).

This script provides utilities for managing candidate words that may be
added to the dictionary in the future.

Usage:
    # Add a single candidate
    python build/manage_candidates.py add "漢字" "かんじ" "Chinese characters - common word"

    # Remove candidates that now exist in dictionary
    python build/manage_candidates.py sync

    # Show statistics
    python build/manage_candidates.py stats
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone


CANDIDATES_FILE = Path('candidate_words.json')


def load_candidates() -> dict:
    """Load the candidates file, or create empty structure if not exists."""
    if CANDIDATES_FILE.exists():
        with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'metadata': {
            'description': 'Candidate words to potentially add to the dictionary',
            'last_updated': None,
            'total_candidates': 0,
            'next_id': 1
        },
        'candidates': []
    }


def save_candidates(data: dict):
    """Save the candidates file."""
    data['metadata']['last_updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    data['metadata']['total_candidates'] = len(data['candidates'])

    with open(CANDIDATES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_existing_entries() -> set:
    """Get set of (reading, headword) tuples from existing dictionary entries."""
    existing = set()
    entries_dir = Path('entries')

    for entry_file in entries_dir.rglob('*.json'):
        with open(entry_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            reading = data.get('reading', '')
            headword = data.get('headword', '')
            # Clean headword of furigana notation
            clean_headword = re.sub(r'\{([^|]+)\|[^}]+\}', r'\1', headword)
            existing.add((reading, clean_headword))

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
    data = load_candidates()

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: manage_candidates.py add <word> [reading] [notes]")
            return

        word = sys.argv[2]
        reading = sys.argv[3] if len(sys.argv) > 3 else None
        notes = sys.argv[4] if len(sys.argv) > 4 else None

        candidate = add_candidate(data, word, reading, notes)
        save_candidates(data)
        print(f"Added candidate: {candidate['id']} - {word}")

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
