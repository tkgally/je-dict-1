"""
Shared utilities for duplicate entry detection.

This module provides common duplicate-checking logic used by both
check_duplicate.py and manage_candidates.py.
"""

from typing import Dict, Any, List

from japanese_utils import strip_furigana


def check_for_duplicate(
    word: str,
    reading: str,
    entries_data: Dict[str, Any],
    candidates_data: Dict[str, Any] = None,
    skip_candidates: bool = False
) -> Dict[str, Any]:
    """
    Check if a word already exists in entries or candidates.

    Args:
        word: The word to check (may include furigana markup)
        reading: The reading in hiragana
        entries_data: Data from entries_index.json (with 'entries' key)
        candidates_data: Data from candidate_words.json (with 'candidates' key)
        skip_candidates: If True, skip checking against candidates

    Returns:
        Dict with:
            - is_duplicate: bool
            - found_in: 'entries' | 'candidates' | None
            - match_type: 'exact' | 'reading_only' | 'word_only' | None
            - details: str with match information
    """
    result = {
        'is_duplicate': False,
        'found_in': None,
        'match_type': None,
        'details': None
    }

    # Normalize the word (strip furigana if present)
    clean_word = strip_furigana(word)

    # Check entries_index.json
    for entry in entries_data.get('entries', []):
        entry_reading = entry.get('reading', '')
        entry_headword = strip_furigana(entry.get('headword', ''))

        # Check for exact match (both reading and headword)
        if entry_reading == reading and entry_headword == clean_word:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'exact',
                'details': f"Exact match: {entry['id']} ({entry_headword} / {entry_reading})"
            }

        # Check for reading-only match
        if entry_reading == reading:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'reading_only',
                'details': f"Reading match: {entry['id']} ({entry_headword} / {entry_reading})"
            }

        # Check for headword-only match
        if entry_headword == clean_word:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'word_only',
                'details': f"Headword match: {entry['id']} ({entry_headword} / {entry_reading})"
            }

    # Check candidate_words.json (unless skipped)
    if not skip_candidates and candidates_data:
        for cand in candidates_data.get('candidates', []):
            cand_reading = cand.get('reading', '')
            cand_word = cand.get('word', '')

            # Check for exact match
            if cand_reading == reading and cand_word == clean_word:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'exact',
                    'details': f"Exact match in candidates: {cand['id']} ({cand_word} / {cand_reading})"
                }

            # Check for reading-only match
            if cand_reading == reading:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'reading_only',
                    'details': f"Reading match in candidates: {cand['id']} ({cand_word} / {cand_reading})"
                }

            # Check for word-only match
            if cand_word == clean_word:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'word_only',
                    'details': f"Word match in candidates: {cand['id']} ({cand_word} / {cand_reading})"
                }

    return result
