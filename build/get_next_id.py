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

    python3 build/get_next_id.py --count 20
    # Also warns when a batch of 20 starting at the next ID crosses a
    # 500-entry directory boundary (IDs round DOWN: 30495 -> entries/30000/).
"""

import argparse
import json
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

    # A retired entry's number is a live redirect URL and is never reused
    retired = entries_dir.parent / 'build' / 'data' / 'retired_entries.json'
    if retired.exists():
        for old in json.loads(retired.read_text(encoding='utf-8')):
            if old[:5].isdigit():
                max_id = max(max_id, int(old[:5]))

    return max_id


def entry_directory(numeric_id: int) -> str:
    """Directory an ID belongs in: the ID rounded down to the nearest 500."""
    return f"entries/{numeric_id // 500 * 500:05d}/"


def boundary_lines(next_id: int, count: int = 1) -> list:
    """Lines telling where the next ID (and a batch of `count`) must be written.

    Entries 30495-30499 were once written into entries/30500/ because 304xx
    looks like 30500; printing the directory removes that trap.
    """
    lines = [f"Directory: {entry_directory(next_id)}"]
    if next_id % 500 == 0:
        lines.append(f"NOTE: {next_id:05d} is the first ID of a new directory.")
    last = next_id + max(count, 1) - 1
    boundary = (next_id // 500 + 1) * 500
    if last >= boundary:
        lines.append(
            f"WARNING: a batch of {count} ({next_id:05d}-{last:05d}) crosses a directory "
            f"boundary: {next_id:05d}-{boundary - 1:05d} go in {entry_directory(next_id)}, "
            f"{boundary:05d} onward in {entry_directory(boundary)}."
        )
    return lines


def main():
    parser = argparse.ArgumentParser(
        description='Get the next available entry ID by scanning the filesystem.'
    )
    parser.add_argument(
        '--number-only', action='store_true',
        help='Print only the numeric ID (for use in scripts)'
    )
    parser.add_argument(
        '--count', type=int, default=1,
        help='Batch size: warn if this many IDs from the next one cross a 500 boundary'
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
        for line in boundary_lines(next_id, args.count):
            print(line)


if __name__ == '__main__':
    main()
