#!/usr/bin/env python3
"""
One-time script to fix round timestamps in dictionary entries.
Adds random minutes and seconds to timestamps that end in :00:00Z.
"""

import json
import os
import random
import re
from pathlib import Path

def fix_round_timestamp(timestamp: str) -> str:
    """Add random minutes and seconds to a round timestamp."""
    # Check if it's a round timestamp (ends with :00:00Z)
    if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:00:00Z$', timestamp):
        return timestamp

    # Add random minutes (1-59) and seconds (1-59)
    minutes = random.randint(1, 59)
    seconds = random.randint(1, 59)

    # Replace :00:00Z with the new time
    new_timestamp = timestamp.replace(':00:00Z', f':{minutes:02d}:{seconds:02d}Z')
    return new_timestamp

def process_entry(entry_path: Path) -> bool:
    """Process a single entry file. Returns True if modified."""
    with open(entry_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    modified = False

    # Check and fix created timestamp
    if 'metadata' in data:
        if 'created' in data['metadata']:
            old_created = data['metadata']['created']
            new_created = fix_round_timestamp(old_created)
            if old_created != new_created:
                data['metadata']['created'] = new_created
                modified = True

        if 'modified' in data['metadata']:
            old_modified = data['metadata']['modified']
            new_modified = fix_round_timestamp(old_modified)
            if old_modified != new_modified:
                data['metadata']['modified'] = new_modified
                modified = True

    if modified:
        with open(entry_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return modified

def main():
    entries_dir = Path(__file__).parent.parent / 'entries'

    total_files = 0
    modified_files = 0

    # Process all JSON files in entries directory
    for json_file in entries_dir.rglob('*.json'):
        total_files += 1
        if process_entry(json_file):
            modified_files += 1
            print(f"  Fixed: {json_file.relative_to(entries_dir)}")

    print(f"\nProcessed {total_files} files, modified {modified_files} files")

if __name__ == '__main__':
    main()
