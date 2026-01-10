#!/usr/bin/env python3
"""
Cross-Reference Link Resolution for je-dict-1

This module resolves cross-references at build time, determining which
target entries exist and enriching the data with resolution status.

Usage:
    from resolve_links import resolve_cross_references
    resolved_entries = resolve_cross_references(entries, entries_index)
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


def build_reading_index(entries: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Build a lookup index from reading to entry data.

    Args:
        entries: List of entry dictionaries

    Returns:
        Dictionary mapping reading (hiragana) to entry info
    """
    index = {}
    for entry in entries:
        reading = entry.get('reading', '')
        if reading:
            # Store entry info for lookup
            index[reading] = {
                'id': entry.get('id', ''),
                'headword': entry.get('headword', ''),
                'reading': reading,
                'gloss': entry.get('gloss', '')
            }
    return index


def normalize_legacy_reference(ref: str, reading_index: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Convert legacy string reference (entry ID) to new structured format.

    Args:
        ref: Legacy reference string (entry ID like "nomu_00001")
        reading_index: Reading lookup index

    Returns:
        Structured cross-reference dictionary
    """
    # Try to find entry by ID in the index
    for reading, info in reading_index.items():
        if info['id'] == ref:
            return {
                'type': 'see_also',
                'reading': reading,
                'headword': info['headword'],
                'label': None
            }

    # If not found, try to extract reading from ID
    # ID format: romaji_00000
    parts = ref.split('_')
    if len(parts) >= 1:
        romaji = parts[0]
        # Convert basic romaji to hiragana (simplified)
        reading = romaji_to_hiragana(romaji)
        return {
            'type': 'see_also',
            'reading': reading,
            'headword': None,
            'label': None
        }

    return {
        'type': 'see_also',
        'reading': ref,
        'headword': None,
        'label': None
    }


def romaji_to_hiragana(romaji: str) -> str:
    """
    Convert romaji to hiragana (simplified conversion).

    This handles common patterns but is not comprehensive.
    """
    # Mapping table for common romaji to hiragana
    conversions = [
        # Long vowels and special cases first
        ('shi', 'し'), ('chi', 'ち'), ('tsu', 'つ'),
        ('sha', 'しゃ'), ('shu', 'しゅ'), ('sho', 'しょ'),
        ('cha', 'ちゃ'), ('chu', 'ちゅ'), ('cho', 'ちょ'),
        ('ja', 'じゃ'), ('ju', 'じゅ'), ('jo', 'じょ'),
        ('nya', 'にゃ'), ('nyu', 'にゅ'), ('nyo', 'にょ'),
        ('hya', 'ひゃ'), ('hyu', 'ひゅ'), ('hyo', 'ひょ'),
        ('mya', 'みゃ'), ('myu', 'みゅ'), ('myo', 'みょ'),
        ('rya', 'りゃ'), ('ryu', 'りゅ'), ('ryo', 'りょ'),
        ('gya', 'ぎゃ'), ('gyu', 'ぎゅ'), ('gyo', 'ぎょ'),
        ('bya', 'びゃ'), ('byu', 'びゅ'), ('byo', 'びょ'),
        ('pya', 'ぴゃ'), ('pyu', 'ぴゅ'), ('pyo', 'ぴょ'),
        # Double consonants
        ('kk', 'っk'), ('ss', 'っs'), ('tt', 'っt'),
        ('pp', 'っp'), ('mm', 'っm'), ('nn', 'ん'),
        # Basic syllables
        ('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ'),
        ('sa', 'さ'), ('su', 'す'), ('se', 'せ'), ('so', 'そ'),
        ('ta', 'た'), ('te', 'て'), ('to', 'と'),
        ('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の'),
        ('ha', 'は'), ('hi', 'ひ'), ('fu', 'ふ'), ('he', 'へ'), ('ho', 'ほ'),
        ('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も'),
        ('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ'),
        ('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ'),
        ('wa', 'わ'), ('wo', 'を'),
        ('ga', 'が'), ('gi', 'ぎ'), ('gu', 'ぐ'), ('ge', 'げ'), ('go', 'ご'),
        ('za', 'ざ'), ('ji', 'じ'), ('zu', 'ず'), ('ze', 'ぜ'), ('zo', 'ぞ'),
        ('da', 'だ'), ('de', 'で'), ('do', 'ど'),
        ('ba', 'ば'), ('bi', 'び'), ('bu', 'ぶ'), ('be', 'べ'), ('bo', 'ぼ'),
        ('pa', 'ぱ'), ('pi', 'ぴ'), ('pu', 'ぷ'), ('pe', 'ぺ'), ('po', 'ぽ'),
        # Single vowels
        ('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e', 'え'), ('o', 'お'),
        ('n', 'ん'),
    ]

    result = romaji.lower()
    for rom, hira in conversions:
        result = result.replace(rom, hira)

    return result


def resolve_reference(ref: Dict[str, Any], reading_index: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Resolve a single cross-reference, adding resolution status.

    Args:
        ref: Cross-reference dictionary with type, reading, etc.
        reading_index: Reading lookup index

    Returns:
        Enriched cross-reference with resolved status and target_id
    """
    resolved_ref = dict(ref)
    reading = ref.get('reading', '')

    if reading and reading in reading_index:
        target = reading_index[reading]
        resolved_ref['resolved'] = True
        resolved_ref['target_id'] = target['id']
        # Fill in headword if not provided
        if not resolved_ref.get('headword'):
            resolved_ref['headword'] = target['headword']
    else:
        resolved_ref['resolved'] = False
        resolved_ref['target_id'] = None

    return resolved_ref


def resolve_cross_references(entries: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, List[str]]]:
    """
    Resolve all cross-references in entries.

    Args:
        entries: List of entry dictionaries

    Returns:
        Tuple of:
        - List of entries with resolved cross-references
        - Dictionary of pending links (reading -> list of entry IDs wanting that link)
    """
    # Build reading index
    reading_index = build_reading_index(entries)

    # Track pending links
    pending_links: Dict[str, List[str]] = {}

    # Process each entry
    resolved_entries = []
    for entry in entries:
        resolved_entry = dict(entry)
        refs = entry.get('cross_references', [])

        if refs:
            resolved_refs = []
            for ref in refs:
                # Handle legacy string format
                if isinstance(ref, str):
                    ref = normalize_legacy_reference(ref, reading_index)

                # Resolve the reference
                resolved_ref = resolve_reference(ref, reading_index)
                resolved_refs.append(resolved_ref)

                # Track pending links
                if not resolved_ref['resolved']:
                    reading = resolved_ref.get('reading', '')
                    if reading:
                        if reading not in pending_links:
                            pending_links[reading] = []
                        pending_links[reading].append(entry.get('id', ''))

            resolved_entry['cross_references'] = resolved_refs

        resolved_entries.append(resolved_entry)

    return resolved_entries, pending_links


def generate_link_report(entries: List[Dict[str, Any]], pending_links: Dict[str, List[str]]) -> str:
    """
    Generate a report on cross-reference status.

    Args:
        entries: List of resolved entries
        pending_links: Dictionary of pending links

    Returns:
        Formatted report string
    """
    total_refs = 0
    resolved_refs = 0
    pending_refs = 0

    for entry in entries:
        for ref in entry.get('cross_references', []):
            total_refs += 1
            if ref.get('resolved'):
                resolved_refs += 1
            else:
                pending_refs += 1

    report = []
    report.append("Cross-Reference Report")
    report.append("=" * 50)
    report.append(f"Total references: {total_refs}")
    if total_refs > 0:
        report.append(f"Resolved: {resolved_refs} ({resolved_refs * 100 // total_refs}%)")
        report.append(f"Pending: {pending_refs} ({pending_refs * 100 // total_refs}%)")
    report.append("")

    if pending_links:
        report.append("Top pending targets (entries wanted):")
        # Sort by number of entries wanting each link
        sorted_pending = sorted(pending_links.items(), key=lambda x: len(x[1]), reverse=True)
        for reading, entry_ids in sorted_pending[:10]:
            report.append(f"  {reading} - referenced by {len(entry_ids)} entries")

    return "\n".join(report)


if __name__ == '__main__':
    # Test with actual entries
    import sys

    entries_dir = Path(__file__).parent.parent / 'entries'
    entries = []

    for json_file in entries_dir.rglob('*.json'):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                entry = json.load(f)
                entries.append(entry)
        except Exception as e:
            print(f"Error loading {json_file}: {e}", file=sys.stderr)

    print(f"Loaded {len(entries)} entries")

    resolved_entries, pending_links = resolve_cross_references(entries)
    print(generate_link_report(resolved_entries, pending_links))
