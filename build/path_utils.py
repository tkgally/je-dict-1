"""
Shared path utility functions for je-dict-1 build scripts.

This module consolidates duplicated path-related functions that were
previously defined in multiple scripts.

Directory Structure:
    entries/00000/  (entries 00001-00499)
    entries/00500/  (entries 00500-00999)
    entries/01000/  (entries 01000-01499)
    etc.

Entry ID Format:
    {5-digit-number}_{romaji}  (e.g., "00003_matsu")
"""

from pathlib import Path


def get_numeric_id(entry_id: str) -> int:
    """
    Extract the numeric portion from an entry ID.

    Args:
        entry_id: The entry ID (e.g., '00003_matsu')

    Returns:
        The numeric portion as an integer (e.g., 3)

    Examples:
        >>> get_numeric_id('00003_matsu')
        3
        >>> get_numeric_id('06512_inzei')
        6512
    """
    parts = entry_id.split('_')
    if len(parts) >= 1:
        try:
            return int(parts[0])
        except ValueError:
            pass
    return 0


def get_directory_range(entry_id: str) -> str:
    """
    Get the directory name for an entry based on its numeric ID.

    Entries are grouped in directories of 500:
    - 00001-00499 → 00000/
    - 00500-00999 → 00500/
    - 01000-01499 → 01000/
    - etc.

    Args:
        entry_id: The entry ID (e.g., '00003_matsu')

    Returns:
        The directory name (e.g., '00000')

    Examples:
        >>> get_directory_range('00003_matsu')
        '00000'
        >>> get_directory_range('00500_taberu')
        '00500'
        >>> get_directory_range('06512_inzei')
        '06500'
    """
    num_id = get_numeric_id(entry_id)
    # Calculate the range start (floor to nearest 500)
    range_start = (num_id // 500) * 500
    return f"{range_start:05d}"


def get_entry_path(entries_dir: Path, entry_id: str) -> Path:
    """
    Get the full path for an entry file.

    Args:
        entries_dir: Base entries directory
        entry_id: The entry ID (e.g., '00003_matsu')

    Returns:
        Path to the entry file

    Examples:
        >>> get_entry_path(Path('entries'), '00003_matsu')
        PosixPath('entries/00000/00003_matsu.json')
    """
    dir_range = get_directory_range(entry_id)
    return entries_dir / dir_range / f"{entry_id}.json"


# Legacy functions for backwards compatibility during migration

def get_entry_prefix(entry_id: str) -> str:
    """
    DEPRECATED: Legacy function for old 2-character prefix system.

    Now returns the directory range for the new system.

    Args:
        entry_id: The entry ID

    Returns:
        The directory range (e.g., '00000')
    """
    return get_directory_range(entry_id)
