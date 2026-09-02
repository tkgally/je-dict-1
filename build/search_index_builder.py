"""
Search index generation for je-dict-1 dictionary.

Generates two JavaScript data files and loads the client-side search scripts
from templates.

search-index.js  (loaded by index.html, advanced.html, curator.html)
    window.SEARCH_INDEX = {
        japanese: {"食べる": 396, "たべる": [396, ...], ...},   # headwords + readings
        romaji:   {"taberu": 396, ...},                          # Hepburn of the reading
        english:  {"eat": [396, ...], ...},                      # gloss words (lower-case)
        forms:    {"食べた": 396, "たべた": 396, ...}             # conjugated forms (see INDEXED_FORMS)
    }
    Every value is one numeric entry id, or a list of them when several entries
    share a key. Numeric ids are the 5-digit prefix of the entry id (unique).

    window.SEARCH_ENTRIES = {
        "396": ["00396_taberu", "{食|た}べる", "たべる", "to eat", "ichidan verb", "b"],
        ...
    }
    Positions: [id, headword (furigana notation, rendered to <ruby> client-side),
    reading, gloss, part of speech, tier letter b/c/g]. Text is HTML-escaped here
    because search.js renders it with innerHTML.

search-tags.js  (loaded only by advanced.html and curator.html)
    window.SEARCH_TAGS = {"396": {"pos": ["verb-ichidan"], "transitivity": "transitive", ...}, ...}
    Empty tag fields are omitted.
"""

import json
import html
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

from japanese_utils import (
    FURIGANA_PATTERN,
    hiragana_to_romaji,
    strip_furigana,
)

# Conjugated forms added to the `forms` map, as (label, column) pairs.
# Indexing every form for all 7,751 conjugating entries (kanji + kana surfaces)
# would cost about 14 MB raw, so only the forms learners most often meet in
# running text are indexed (about 4 MB raw). Set to None to index every form.
INDEXED_FORMS = [
    ('Past', 'affirmative'),
    ('て form', 'affirmative'),
    ('Present', 'negative'),
    ('Present polite', 'affirmative'),
    ('Past polite', 'affirmative'),
    ('Potential', 'affirmative'),
    ('Passive', 'affirmative'),
    ('Causative', 'affirmative'),
    ('Volitional', 'affirmative'),
    ('Conditional ば', 'affirmative'),
    ('Conditional たら', 'affirmative'),
    ('Adverbial', 'affirmative'),
]

# Function words dropped from the English index and (in search.js) from queries,
# so that "to eat" and "eat" behave the same. Keep in sync with search.js.
ENGLISH_STOPWORDS = {'to', 'a', 'an', 'the', 'of', 'or', 'and', 'in', 'on', 'be', 'for', 'with', 'by', 'at'}

TIER_LETTER = {'basic': 'b', 'core': 'c', 'general': 'g'}

_WORD_SPLIT = re.compile(r'[\s,;/]+')


def numeric_id(entry_id: str) -> int:
    """The 5-digit numeric part of an entry id ('00396_taberu' -> 396)."""
    return int(entry_id[:5])


def gloss_words(text: str):
    """Yield index words from a gloss string."""
    for word in _WORD_SPLIT.split(text.lower()):
        word = word.strip('()[]."\'!?:')
        if len(word) < 2 or word in ENGLISH_STOPWORDS:
            continue
        yield word


def furigana_to_kana(text: str) -> str:
    """'{食|た}べた' -> 'たべた' (reading-only version of a furigana string)."""
    return FURIGANA_PATTERN.sub(r'\2', text)


def _add(index: dict, key: str, num_id: int) -> None:
    ids = index.get(key)
    if ids is None:
        index[key] = [num_id]
    elif num_id not in ids:
        ids.append(num_id)


def _compact(index: dict) -> dict:
    """Store single-entry keys as a bare int instead of a one-element list."""
    return {k: (v[0] if len(v) == 1 else v) for k, v in index.items()}


def build_search_data(entries: list) -> tuple:
    """Return (index, entries_data, tags_data) — see the module docstring."""
    index = {'japanese': {}, 'romaji': {}, 'english': {}, 'forms': {}}
    entries_data = {}
    tags_data = {}

    for entry in entries:
        entry_id = entry['id']
        num = numeric_id(entry_id)
        headword = entry['headword']
        reading = entry['reading']
        gloss = entry.get('gloss', '')
        metadata = entry.get('metadata', {})
        tags = metadata.get('tags', {})
        tier = TIER_LETTER.get(metadata.get('vocabulary_tier', 'general'), 'g')

        entries_data[num] = [
            entry_id,
            html.escape(headword),
            html.escape(reading),
            html.escape(gloss),
            html.escape(entry.get('part_of_speech', '')),
            tier,
        ]

        tag_record = {}
        for field in ('pos', 'semantic', 'style', 'domain'):
            if tags.get(field):
                tag_record[field] = tags[field]
        for field in ('formality', 'politeness', 'transitivity'):
            if tags.get(field):
                tag_record[field] = tags[field]
        tags_data[num] = tag_record

        # Japanese: headword (furigana stripped) and reading
        headword_clean = strip_furigana(headword)
        _add(index['japanese'], headword_clean, num)
        _add(index['japanese'], reading, num)

        # Romaji of the reading
        _add(index['romaji'], hiragana_to_romaji(reading), num)

        # English gloss words (main gloss + per-sense glosses)
        glosses = [gloss] + [d['gloss'] for d in entry.get('definitions', []) if d.get('gloss')]
        for g in glosses:
            for word in gloss_words(g):
                _add(index['english'], word, num)

        # Conjugated forms that differ from the headword/reading
        conjugation = entry.get('conjugation') or {}
        for form in conjugation.get('forms', []):
            for column in ('affirmative', 'negative'):
                if INDEXED_FORMS is not None and (form.get('label'), column) not in INDEXED_FORMS:
                    continue
                surface = form.get(column)
                if not surface:
                    continue
                for variant in {strip_furigana(surface), furigana_to_kana(surface)}:
                    if variant and variant != headword_clean and variant != reading:
                        _add(index['forms'], variant, num)

    index = {name: _compact(table) for name, table in index.items()}
    return index, entries_data, tags_data


def generate_search_index(entries: list) -> str:
    """Generate search-index.js (compact index + display data)."""
    index, entries_data, _tags = build_search_data(entries)
    return generate_search_index_js(index, entries_data)


def generate_search_index_js(index: dict, entries_data: dict) -> str:
    return f'''// Auto-generated search index - do not edit manually
// Generated: {datetime.now(timezone.utc).isoformat()}
// SEARCH_INDEX: japanese/romaji/english/forms -> numeric entry id or list of ids
// SEARCH_ENTRIES: numeric id -> [id, headword, reading, gloss, part of speech, tier b/c/g]

window.SEARCH_INDEX = {json.dumps(index, ensure_ascii=False, separators=(',', ':'))};

window.SEARCH_ENTRIES = {json.dumps(entries_data, ensure_ascii=False, separators=(',', ':'))};
'''


def generate_search_tags_js(tags_data: dict) -> str:
    """Generate search-tags.js (tag data for the advanced/curator pages)."""
    return f'''// Auto-generated tag data for advanced.html / curator.html - do not edit manually
// Generated: {datetime.now(timezone.utc).isoformat()}
// SEARCH_TAGS: numeric id -> tag record (empty fields omitted)

window.SEARCH_TAGS = {json.dumps(tags_data, ensure_ascii=False, separators=(',', ':'))};
'''


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
