#!/usr/bin/env python3
"""
Compute the correct file path for a dictionary entry.

This helper script determines the correct directory structure for placing
dictionary entries, based on the two-level hierarchy:
1. Kana row directory: Determined by the FIRST KANA of the READING
2. Prefix subdirectory: First 2 characters of the ENTRY ID

Usage:
    python3 build/get_entry_path.py <reading> <entry_id>

Examples:
    python3 build/get_entry_path.py ふみきる fumikiru_06311
    # Output: entries/ha/fu/fumikiru_06311.json

    python3 build/get_entry_path.py こうりつてき kouritsuteki_00001
    # Output: entries/ka/ko/kouritsuteki_00001.json

    python3 build/get_entry_path.py たべる taberu_00001
    # Output: entries/ta/ta/taberu_00001.json

IMPORTANT NOTES:
- The kana directory is determined by the READING (e.g., ふ → ha)
- The prefix is determined by the ENTRY ID (e.g., fumikiru → fu)
- These are often different! ふ romanizes to 'fu', so:
  - kana folder = 'ha' (は行, because ふ is in は行)
  - prefix folder = 'fu' (first 2 chars of ID)
  - Result: entries/ha/fu/
"""

import sys
from pathlib import Path

# Add build directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from japanese_utils import get_kana_folder
from path_utils import get_entry_prefix


def get_full_entry_path(reading: str, entry_id: str) -> str:
    """
    Compute the correct path for an entry file.

    Args:
        reading: Hiragana reading (e.g., 'ふみきる')
        entry_id: Entry ID (e.g., 'fumikiru_06311')

    Returns:
        The correct path (e.g., 'entries/ha/fu/fumikiru_06311.json')
    """
    # Kana folder is determined by the READING's first kana
    kana_folder = get_kana_folder(reading)

    # Prefix is determined by the ENTRY ID's first 2 characters
    prefix = get_entry_prefix(entry_id)

    return f"entries/{kana_folder}/{prefix}/{entry_id}.json"


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 build/get_entry_path.py <reading> <entry_id>")
        print()
        print("Examples:")
        print("  python3 build/get_entry_path.py ふみきる fumikiru_06311")
        print("  python3 build/get_entry_path.py こうりつてき kouritsuteki_00001")
        print("  python3 build/get_entry_path.py たべる taberu_00001")
        print()
        print("This script determines the correct file path for a dictionary entry.")
        print("The path follows a two-level hierarchy:")
        print("  1. Kana row folder - based on the first kana of the READING")
        print("  2. Prefix subfolder - first 2 characters of the ENTRY ID")
        sys.exit(1)

    reading = sys.argv[1]
    entry_id = sys.argv[2]

    # Validate reading is hiragana
    if not reading or not all('\u3041' <= c <= '\u3096' or c == 'ー' for c in reading):
        print(f"Error: Reading must be hiragana (got: '{reading}')")
        sys.exit(1)

    # Compute path
    path = get_full_entry_path(reading, entry_id)

    # Also show the breakdown for clarity
    kana_folder = get_kana_folder(reading)
    prefix = get_entry_prefix(entry_id)

    print(f"Reading: {reading}")
    print(f"Entry ID: {entry_id}")
    print(f"Kana folder: {kana_folder} (from reading '{reading[0]}' = {reading[0]}行)")
    print(f"Prefix: {prefix} (from entry ID)")
    print(f"Full path: {path}")


if __name__ == '__main__':
    main()
