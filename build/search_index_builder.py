"""
Search index generation for je-dict-1 dictionary.

Generates the search-index.js file (mapping Japanese, romaji, and English terms
to entry IDs) and loads the client-side search JavaScript files from templates.
"""

import json
import html
import sys
from pathlib import Path
from datetime import datetime, timezone

from path_utils import get_directory_range
from japanese_utils import (
    hiragana_to_romaji,
    strip_furigana
)
from entry_renderer import process_furigana


def generate_search_index(entries: list) -> str:
    """Generate the compact search index JavaScript file."""
    # Build index using sets for O(1) duplicate detection
    # Sets are converted to lists at the end for JSON serialization
    index_sets = {
        'japanese': {},
        'romaji': {},
        'english': {}
    }

    # Build entries lookup with minimal data
    entries_data = {}

    for entry in entries:
        entry_id = entry['id']
        headword = entry['headword']
        reading = entry['reading']
        gloss = entry.get('gloss', '')
        dir_range = get_directory_range(entry_id)

        # Get tags
        tags = entry.get('metadata', {}).get('tags', {})
        tier = entry.get('metadata', {}).get('vocabulary_tier', 'general')

        # Store minimal entry data for display
        # Note: headword is HTML-escaped by process_furigana(); gloss and reading
        # are escaped here to prevent XSS when rendered via innerHTML in search.js
        entries_data[entry_id] = {
            'id': entry_id,
            'headword': process_furigana(headword),
            'reading': html.escape(reading),
            'romaji': hiragana_to_romaji(reading),
            'gloss': html.escape(gloss),
            'dirRange': dir_range,
            'tier': tier,
            'tags': {
                'pos': tags.get('pos', []),
                'formality': tags.get('formality'),
                'politeness': tags.get('politeness'),
                'transitivity': tags.get('transitivity'),
                'semantic': tags.get('semantic', []),
                'style': tags.get('style', []),
                'domain': tags.get('domain', [])
            }
        }

        # Index headword (stripped)
        headword_clean = strip_furigana(headword)
        if headword_clean not in index_sets['japanese']:
            index_sets['japanese'][headword_clean] = set()
        index_sets['japanese'][headword_clean].add(entry_id)

        # Index reading
        if reading not in index_sets['japanese']:
            index_sets['japanese'][reading] = set()
        index_sets['japanese'][reading].add(entry_id)

        # Index romaji
        romaji = hiragana_to_romaji(reading)
        if romaji not in index_sets['romaji']:
            index_sets['romaji'][romaji] = set()
        index_sets['romaji'][romaji].add(entry_id)

        # Index English gloss words
        glosses = [gloss]
        for defn in entry.get('definitions', []):
            if 'gloss' in defn:
                glosses.append(defn['gloss'])

        for g in glosses:
            words = g.lower().replace(',', ' ').replace(';', ' ').split()
            for word in words:
                word = word.strip('()[].')
                if len(word) < 2:
                    continue
                if word not in index_sets['english']:
                    index_sets['english'][word] = set()
                index_sets['english'][word].add(entry_id)

    # Convert sets to lists for JSON serialization
    index = {
        'japanese': {k: list(v) for k, v in index_sets['japanese'].items()},
        'romaji': {k: list(v) for k, v in index_sets['romaji'].items()},
        'english': {k: list(v) for k, v in index_sets['english'].items()}
    }

    # Generate JavaScript
    js_content = f'''// Auto-generated search index - do not edit manually
// Generated: {datetime.now(timezone.utc).isoformat()}

window.SEARCH_INDEX = {json.dumps(index, ensure_ascii=False)};

window.SEARCH_ENTRIES = {json.dumps(entries_data, ensure_ascii=False)};
'''

    return js_content


def generate_search_js() -> str:
    """Generate the search.js JavaScript file."""
    js_path = Path(__file__).parent / 'templates' / 'search.js'
    try:
        return js_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: Template file not found: {js_path}")
        sys.exit(1)


def generate_tag_search_js() -> str:
    """Generate the tag-search.js JavaScript file for tag-based filtering."""
    js_path = Path(__file__).parent / 'templates' / 'tag-search.js'
    try:
        return js_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: Template file not found: {js_path}")
        sys.exit(1)
