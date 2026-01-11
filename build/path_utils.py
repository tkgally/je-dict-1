"""
Shared path utility functions for je-dict-1 build scripts.

This module consolidates duplicated path-related functions that were
previously defined in multiple scripts.
"""

from pathlib import Path


def get_entry_prefix(entry_id: str) -> str:
    """
    Get the 2-character prefix for entry/audio file organization.

    This creates a subdirectory structure to avoid GitHub's 1,000 file limit.

    Args:
        entry_id: The entry ID (e.g., 'taberu_00001') or filename

    Returns:
        The first 2 characters lowercase (e.g., 'ta')

    Examples:
        >>> get_entry_prefix('taberu_00001')
        'ta'
        >>> get_entry_prefix('ittai_00493-ex1.mp3')
        'it'
    """
    return entry_id[:2].lower()


# Alias for backwards compatibility - audio and entry prefixes use the same logic
get_audio_prefix = get_entry_prefix


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


def get_audio_path(audio_dir: Path, kana_folder: str, entry_id: str, example_num: int) -> Path:
    """
    Get the full path for an audio file.

    Args:
        audio_dir: Base audio directory
        kana_folder: The kana row folder (e.g., 'ta', 'ka')
        entry_id: The entry ID (e.g., 'taberu_00001')
        example_num: Example number (1-based)

    Returns:
        Path to the audio file
    """
    prefix = get_entry_prefix(entry_id)
    return audio_dir / kana_folder / prefix / f"{entry_id}-ex{example_num}.mp3"
