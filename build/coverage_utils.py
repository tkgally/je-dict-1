#!/usr/bin/env python3
"""Shared lookup utilities for vocabulary coverage auditing.

Used by audit_semantic_field.py and analyze_scenarios.py.
"""

import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
INDEX_FILE = PROJECT_DIR / "entries_index.json"
CANDIDATES_FILE = PROJECT_DIR / "candidate_words.json"


def load_entry_index(index_file=INDEX_FILE):
    """Load entries_index.json and build a lookup set of (word, reading) pairs.

    Returns:
        tuple: (lookup set of (headword, reading), set of readings only)
    """
    with open(index_file) as f:
        data = json.load(f)

    lookup = set()
    reading_only = set()

    for entry in data["entries"]:
        headword = entry["headword"]
        reading = entry["reading"]
        lookup.add((headword, reading))
        reading_only.add(reading)

    return lookup, reading_only


def load_candidates(candidates_file=CANDIDATES_FILE):
    """Load candidate_words.json and build a lookup set of (word, reading) pairs."""
    if not candidates_file.exists():
        return set()

    with open(candidates_file) as f:
        data = json.load(f)

    lookup = set()
    for candidate in data.get("candidates", []):
        word = candidate.get("word", "")
        reading = candidate.get("reading", "")
        if word and reading:
            lookup.add((word, reading))
    return lookup


def is_all_kana(word):
    """Check if a word contains only kana (hiragana + katakana)."""
    for ch in word:
        cp = ord(ch)
        # Hiragana: U+3040-U+309F, Katakana: U+30A0-U+30FF
        if not (0x3040 <= cp <= 0x309F or 0x30A0 <= cp <= 0x30FF or ch in "ー"):
            return False
    return True


def word_in_dictionary(word, reading, entry_lookup, reading_only):
    """Check if a word is in the dictionary.

    Checks exact (headword, reading) match first, then for kana-only words
    also matches by reading alone.

    Returns:
        bool: True if word is found in the dictionary
    """
    if (word, reading) in entry_lookup:
        return True
    if is_all_kana(word) and reading in reading_only:
        return True
    return False
