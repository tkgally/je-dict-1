"""
Shared path utility functions for je-dict-1 build scripts.

This module consolidates duplicated path-related functions that were
previously defined in multiple scripts.
"""

from pathlib import Path


def get_entry_prefix(entry_id: str) -> str:
    """
    Get the 2-character prefix for entry file organization.

    This creates a subdirectory structure to avoid GitHub's 1,000 file limit.

    Args:
        entry_id: The entry ID (e.g., 'taberu_00001')

    Returns:
        The first 2 characters lowercase (e.g., 'ta')

    Examples:
        >>> get_entry_prefix('taberu_00001')
        'ta'
    """
    return entry_id[:2].lower()


def get_entry_path(entries_dir: Path, kana_folder: str, entry_id: str) -> Path:
    """
    Get the full path for an entry file.

    Args:
        entries_dir: Base entries directory
        kana_folder: The kana row folder (e.g., 'ta', 'ka')
        entry_id: The entry ID (e.g., 'taberu_00001')

    Returns:
        Path to the entry file
    """
    prefix = get_entry_prefix(entry_id)
    return entries_dir / kana_folder / prefix / f"{entry_id}.json"
