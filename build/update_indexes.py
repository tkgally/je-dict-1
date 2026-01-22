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

    # Use absolute paths throughout instead of os.chdir()
    print("=" * 50)
    print("Updating Dictionary Indexes")
    print("=" * 50)

    has_errors = False

    # 1. Update entries index
    print("\n1. Updating entries_index.json...")
    entries_index_script = project_root / 'build' / 'update_entries_index.py'
    if not entries_index_script.exists():
        print(f"   ERROR: Script not found: {entries_index_script}")
        has_errors = True
    else:
        result = subprocess.run(
            [sys.executable, str(entries_index_script)],
            capture_output=True,
            text=True,
            cwd=str(project_root)
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        if result.returncode != 0:
            print(f"   ERROR: update_entries_index.py failed with exit code {result.returncode}")
            has_errors = True

    # 2. Sync candidate words (remove any that now exist in dictionary)
    print("\n2. Syncing candidate_words.json...")
    candidates_file = project_root / 'candidate_words.json'
    manage_candidates_script = project_root / 'build' / 'manage_candidates.py'
    if not candidates_file.exists():
        print("   No candidate_words.json found, skipping sync.")
    elif not manage_candidates_script.exists():
        print(f"   ERROR: Script not found: {manage_candidates_script}")
        has_errors = True
    else:
        result = subprocess.run(
            [sys.executable, str(manage_candidates_script), 'sync'],
            capture_output=True,
            text=True,
            cwd=str(project_root)
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        if result.returncode != 0:
            print(f"   ERROR: manage_candidates.py sync failed with exit code {result.returncode}")
            has_errors = True

    # 3. Check for new kanji
    print("\n3. Checking for new kanji...")
    update_kanji_script = project_root / 'build' / 'update_kanji_index.py'
    if not update_kanji_script.exists():
        print(f"   WARNING: Script not found: {update_kanji_script}")
    else:
        result = subprocess.run(
            [sys.executable, str(update_kanji_script), '--check-new'],
            capture_output=True,
            text=True,
            cwd=str(project_root)
        )
        if 'new kanji' in result.stdout.lower() and 'found' in result.stdout.lower():
            print(result.stdout)
        else:
            print("   No new kanji found.")

    print("\n" + "=" * 50)
    if has_errors:
        print("Index update completed with ERRORS!")
        print("=" * 50)
        sys.exit(1)
    else:
        print("Index update complete!")
        print("=" * 50)


if __name__ == '__main__':
    main()
