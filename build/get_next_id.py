#!/usr/bin/env python3
"""
Get the next available entry ID by scanning the filesystem.

This script scans all entry files in the entries/ directory to find the
highest numeric ID currently in use, then prints the next available ID.

IMPORTANT: This script reads the actual filesystem, not entries_index.json.
This ensures accuracy even when entries have been created in the current
session without running update_indexes.py.

Usage:
    python3 build/get_next_id.py
    # Output: Next available ID: 11494

    python3 build/get_next_id.py --number-only
    # Output: 11494
"""

import argparse
import re
import sys
from pathlib import Path


def get_max_entry_id(entries_dir: Path) -> int:
    """
    Scan the entries directory to find the highest numeric entry ID.

    Args:
        entries_dir: Path to the entries/ directory

    Returns:
        The highest numeric ID found, or 0 if no entries exist
    """
    max_id = 0
    # Match filenames like 00001_taberu.json, 10678_shokubai.json
    id_pattern = re.compile(r'^(\d{5})_.*\.json$')

    for json_file in entries_dir.rglob('*.json'):
        match = id_pattern.match(json_file.name)
        if match:
            numeric_id = int(match.group(1))
            if numeric_id > max_id:
                max_id = numeric_id

    return max_id


def main():
    parser = argparse.ArgumentParser(
        description='Get the next available entry ID by scanning the filesystem.'
    )
    parser.add_argument(
        '--number-only', action='store_true',
        help='Print only the numeric ID (for use in scripts)'
    )
    args = parser.parse_args()

    # Resolve paths relative to this script's location
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    entries_dir = project_root / 'entries'

    if not entries_dir.exists():
        print("Error: entries directory not found", file=sys.stderr)
        sys.exit(1)

    max_id = get_max_entry_id(entries_dir)
    next_id = max_id + 1

    if args.number_only:
        print(f"{next_id:05d}")
    else:
        print(f"Highest existing ID: {max_id:05d}")
        print(f"Next available ID: {next_id:05d}")


if __name__ == '__main__':
    main()
