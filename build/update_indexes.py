#!/usr/bin/env python3
"""
Update all index files after dictionary changes.

This script should be run after:
- Adding new entries to the dictionary
- Removing entries from the dictionary
- Any batch operations on entries

It will:
1. Update entries_index.json with current entry list
2. Remove from candidate_words.json any words that now exist as entries

Usage:
    python build/update_indexes.py
"""

import subprocess
import sys
from pathlib import Path


def main():
    # Get the project root (parent of build directory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Change to project root for consistent paths
    import os
    os.chdir(project_root)

    print("=" * 50)
    print("Updating Dictionary Indexes")
    print("=" * 50)

    # 1. Update entries index
    print("\n1. Updating entries_index.json...")
    result = subprocess.run(
        [sys.executable, 'build/update_entries_index.py'],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    # 2. Sync candidate words (remove any that now exist in dictionary)
    print("\n2. Syncing candidate_words.json...")
    candidates_file = Path('candidate_words.json')
    if candidates_file.exists():
        result = subprocess.run(
            [sys.executable, 'build/manage_candidates.py', 'sync'],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    else:
        print("   No candidate_words.json found, skipping sync.")

    print("\n" + "=" * 50)
    print("Index update complete!")
    print("=" * 50)


if __name__ == '__main__':
    main()
