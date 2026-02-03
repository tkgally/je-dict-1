"""
Shared utilities for duplicate entry detection.

This module provides common duplicate-checking logic used by both
check_duplicate.py and manage_candidates.py.

DUPLICATE DEFINITION:
A word is considered a duplicate ONLY if both the headword (kanji/kana)
AND reading match an existing entry exactly.

Homophones (same reading, different headword) are NOT duplicates.
Examples: 橋/箸/端 (all はし), 線香/先行 (both せんこう)

Homographs (same headword, different reading) are NOT duplicates.
Examples: 行く (いく/ゆく), 明日 (あした/あす)
"""

from typing import Dict, Any, List, Optional

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

    A word is considered a duplicate ONLY if both headword AND reading match.
    Homophones (same reading, different headword) are NOT duplicates.
    Homographs (same headword, different reading) are NOT duplicates.

    Args:
        word: The word to check (may include furigana markup)
        reading: The reading in hiragana
        entries_data: Data from entries_index.json (with 'entries' key)
        candidates_data: Data from candidate_words.json (with 'candidates' key)
        skip_candidates: If True, skip checking against candidates

    Returns:
        Dict with:
            - is_duplicate: bool (True only for exact matches)
            - found_in: 'entries' | 'candidates' | None
            - match_type: 'exact' | None
            - details: str with match information
            - homophones: list of entries with same reading (informational)
            - homographs: list of entries with same headword (informational)
    """
    result = {
        'is_duplicate': False,
        'found_in': None,
        'match_type': None,
        'details': None,
        'homophones': [],
        'homographs': []
    }

    # Normalize the word (strip furigana if present)
    clean_word = strip_furigana(word)

    # Check entries_index.json
    for entry in entries_data.get('entries', []):
        entry_reading = entry.get('reading', '')
        entry_headword = strip_furigana(entry.get('headword', ''))

        # Check for exact match (both reading AND headword match)
        if entry_reading == reading and entry_headword == clean_word:
            return {
                'is_duplicate': True,
                'found_in': 'entries',
                'match_type': 'exact',
                'details': f"Exact match: {entry['id']} ({entry_headword} / {entry_reading})",
                'homophones': [],
                'homographs': []
            }

        # Track homophones (same reading, different headword) - informational only
        if entry_reading == reading and entry_headword != clean_word:
            result['homophones'].append({
                'id': entry['id'],
                'headword': entry_headword,
                'reading': entry_reading
            })

        # Track homographs (same headword, different reading) - informational only
        if entry_headword == clean_word and entry_reading != reading:
            result['homographs'].append({
                'id': entry['id'],
                'headword': entry_headword,
                'reading': entry_reading
            })

    # Check candidate_words.json (unless skipped)
    if not skip_candidates and candidates_data:
        for cand in candidates_data.get('candidates', []):
            cand_reading = cand.get('reading', '')
            cand_word = cand.get('word', '')

            # Check for exact match (both reading AND word match)
            if cand_reading == reading and cand_word == clean_word:
                return {
                    'is_duplicate': True,
                    'found_in': 'candidates',
                    'match_type': 'exact',
                    'details': f"Exact match in candidates: {cand['id']} ({cand_word} / {cand_reading})",
                    'homophones': result['homophones'],
                    'homographs': result['homographs']
                }

            # Track homophones in candidates - informational only
            if cand_reading == reading and cand_word != clean_word:
                result['homophones'].append({
                    'id': cand['id'],
                    'headword': cand_word,
                    'reading': cand_reading,
                    'source': 'candidates'
                })

            # Track homographs in candidates - informational only
            if cand_word == clean_word and cand_reading != reading:
                result['homographs'].append({
                    'id': cand['id'],
                    'headword': cand_word,
                    'reading': cand_reading,
                    'source': 'candidates'
                })

    return result


def format_related_entries(result: Dict[str, Any]) -> str:
    """
    Format informational messages about homophones and homographs.

    Args:
        result: The result dict from check_for_duplicate

    Returns:
        Formatted string with information about related entries, or empty string.
    """
    messages = []

    if result.get('homophones'):
        homophones = result['homophones'][:3]  # Limit to first 3
        homophone_strs = [f"{h['headword']} ({h['id']})" for h in homophones]
        if len(result['homophones']) > 3:
            homophone_strs.append(f"...and {len(result['homophones']) - 3} more")
        messages.append(f"Homophones exist: {', '.join(homophone_strs)}")

    if result.get('homographs'):
        homographs = result['homographs'][:3]  # Limit to first 3
        homograph_strs = [f"{h['reading']} ({h['id']})" for h in homographs]
        if len(result['homographs']) > 3:
            homograph_strs.append(f"...and {len(result['homographs']) - 3} more")
        messages.append(f"Same kanji with different readings: {', '.join(homograph_strs)}")

    return '\n'.join(messages)
