#!/usr/bin/env python3
"""
Compute the correct file path for a dictionary entry.

This helper script determines the correct directory structure for placing
dictionary entries, based on the numeric ID range system:
    entries/00000/ (entries 00001-00499)
    entries/00500/ (entries 00500-00999)
    entries/01000/ (entries 01000-01499)
    etc.

Usage:
    python3 build/get_entry_path.py <entry_id>
    python3 build/get_entry_path.py <number> <romaji>

Examples:
    python3 build/get_entry_path.py 00003_matsu
    # Output: entries/00000/00003_matsu.json

    python3 build/get_entry_path.py 06512 inzei
    # Output: entries/06500/06512_inzei.json

    python3 build/get_entry_path.py 00001 taberu
    # Output: entries/00000/00001_taberu.json

IMPORTANT NOTES:
- Entry IDs use the format: {5-digit-number}_{romaji}
- The directory is determined by the numeric portion of the ID
- Entries are grouped in directories of 500
"""

import sys
from pathlib import Path

# Add build directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from path_utils import get_directory_range


def get_full_entry_path(entry_id: str) -> str:
    """
    Compute the correct path for an entry file.

    Args:
        entry_id: Entry ID (e.g., '00003_matsu')

    Returns:
        The correct path (e.g., 'entries/00000/00003_matsu.json')
    """
    dir_range = get_directory_range(entry_id)
    return f"entries/{dir_range}/{entry_id}.json"


def main():
    if len(sys.argv) == 2:
        # Single argument: full entry ID
        entry_id = sys.argv[1]
    elif len(sys.argv) == 3:
        # Two arguments: number and romaji
        try:
            number = int(sys.argv[1])
            romaji = sys.argv[2].lower()
            entry_id = f"{number:05d}_{romaji}"
        except ValueError:
            print(f"Error: First argument must be a number (got: '{sys.argv[1]}')")
            sys.exit(1)
    else:
        print("Usage: python3 build/get_entry_path.py <entry_id>")
        print("       python3 build/get_entry_path.py <number> <romaji>")
        print()
        print("Examples:")
        print("  python3 build/get_entry_path.py 00003_matsu")
        print("  python3 build/get_entry_path.py 6512 inzei")
        print("  python3 build/get_entry_path.py 00001 taberu")
        print()
        print("This script determines the correct file path for a dictionary entry.")
        print("Entries are organized by numeric ID range:")
        print("  00001-00499 → entries/00000/")
        print("  00500-00999 → entries/00500/")
        print("  01000-01499 → entries/01000/")
        print("  etc.")
        sys.exit(1)

    # Validate entry_id format
    parts = entry_id.split('_')
    if len(parts) < 2:
        print(f"Error: Invalid entry ID format: '{entry_id}'")
        print("Expected format: 00000_romaji or 00000_romaji_suffix")
        sys.exit(1)

    try:
        num = int(parts[0])
    except ValueError:
        print(f"Error: Entry ID must start with 5 digits: '{entry_id}'")
        sys.exit(1)

    # Compute path
    path = get_full_entry_path(entry_id)
    dir_range = get_directory_range(entry_id)

    print(f"Entry ID: {entry_id}")
    print(f"Numeric ID: {num}")
    print(f"Directory range: {dir_range}/ (entries {int(dir_range):05d}-{int(dir_range)+499:05d})")
    print(f"Full path: {path}")


if __name__ == '__main__':
    main()
