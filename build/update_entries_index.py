#!/usr/bin/env python3
"""
Update the entries index file (entries_index.json).

This script scans all dictionary entries and creates/updates an index file
containing key identifying information for each entry. This index should be
updated whenever entries are added or removed.

Usage:
    python build/update_entries_index.py
"""

import json
from pathlib import Path
from datetime import datetime, timezone

from japanese_utils import strip_furigana


def extract_entry_info(entry_path: Path, project_root: Path) -> dict:
    """Extract key identifying information from an entry file."""
    with open(entry_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get headword and clean it (remove furigana notation for display)
    headword = data.get('headword', '')
    headword_clean = strip_furigana(headword)

    # Get reading (kana)
    reading = data.get('reading', '')

    # Get first gloss
    gloss = data.get('gloss', '')

    # Get entry ID
    entry_id = data.get('id', '')

    # Get filename and path relative to project root
    filename = entry_path.name
    relative_path = str(entry_path.relative_to(project_root))

    return {
        'id': entry_id,
        'headword': headword_clean,
        'reading': reading,
        'gloss': gloss,
        'filename': filename,
        'path': relative_path
    }


def update_entries_index():
    """Scan all entries and update the index file."""
    # Use script-relative paths for robustness
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'
    index_file = project_root / 'entries_index.json'

    if not entries_dir.exists():
        print(f"Error: entries directory not found at {entries_dir}")
        return False

    # Collect all entries
    entries = []
    entry_files = sorted(entries_dir.rglob('*.json'))

    for entry_path in entry_files:
        try:
            entry_info = extract_entry_info(entry_path, project_root)
            entries.append(entry_info)
        except Exception as e:
            print(f"Warning: Failed to process {entry_path}: {e}")

    # Sort by reading (kana) for consistent ordering
    entries.sort(key=lambda x: (x['reading'], x['headword']))

    # Create index structure
    index_data = {
        'metadata': {
            'description': 'Index of all dictionary entries',
            'generated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'total_entries': len(entries)
        },
        'entries': entries
    }

    # Write index file
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print(f"Updated {index_file} with {len(entries)} entries")
    return True


if __name__ == '__main__':
    update_entries_index()
