#!/usr/bin/env python3
"""
Build script for flat HTML version of je-dict-1 dictionary.

Generates static HTML pages for each dictionary entry, plus navigation pages.
This version works without JavaScript and is SEO-friendly.
"""

import json
import os
import re
import shutil
import html
import sys
import subprocess
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional

from path_utils import get_directory_range
from japanese_utils import (
    hiragana_to_romaji, KANA_ROWS,
    FURIGANA_PATTERN, strip_furigana
)
from constants import get_cross_ref_label
from html_utils import (
    process_furigana as _process_furigana_base,
    generate_nav_header,
    generate_furigana_script,
    generate_examples_script,
    generate_header_search_script,
    generate_wordlinks_script,
    process_word_links as _process_word_links_base
)

# Japan Standard Time (UTC+9)
JST = timezone(timedelta(hours=9))

# Load kanji index for headword linking
KANJI_LIST = {}
kanji_list_path = Path(__file__).parent.parent / 'kanji' / 'kanji_list.json'
if kanji_list_path.exists():
    with open(kanji_list_path, 'r', encoding='utf-8') as f:
        kanji_data = json.load(f)
        KANJI_LIST = kanji_data.get('kanji', {})

# Canonical CNAME for GitHub Pages custom domain
# This ensures the CNAME file is always restored even if accidentally deleted
GITHUB_PAGES_CNAME = "www.tkgje.jp"


def process_furigana(text: str, show_furigana: bool = True) -> str:
    """Convert furigana notation to HTML ruby tags."""
    return _process_furigana_base(text, FURIGANA_PATTERN, show_furigana)


def process_word_links(text: str, entries_dict: dict, relative_path: str = '../../') -> str:
    """Process word link markup in text and generate HTML with links."""
    return _process_word_links_base(text, entries_dict, relative_path, FURIGANA_PATTERN)


def process_headword_with_kanji_links(text: str, relative_path: str = '../../') -> str:
    """
    Process headword text with furigana AND kanji links.

    For headwords, kanji characters are wrapped in links to their kanji index pages.
    The links are styled to be invisible (no color change, no underline) but show
    a tooltip on hover.
    """
    if not text:
        return ''

    def is_kanji(char: str) -> bool:
        code = ord(char)
        return (
            (0x4E00 <= code <= 0x9FFF) or
            (0x3400 <= code <= 0x4DBF) or
            (0xF900 <= code <= 0xFAFF)
        )

    def wrap_kanji_in_link(kanji_char: str) -> str:
        """Wrap a single kanji in a link to its index page."""
        if kanji_char in KANJI_LIST:
            kanji_id = KANJI_LIST[kanji_char]['kanji_id']
            return (
                f'<a href="{relative_path}kanji/{kanji_id}.html" '
                f'class="kanji-link" '
                f'title="Other words with this kanji">{html.escape(kanji_char)}</a>'
            )
        return html.escape(kanji_char)

    def replace_furigana_with_links(match):
        """Process furigana, adding links to individual kanji."""
        kanji_group = match.group(1)  # The kanji part
        reading = html.escape(match.group(2))

        # Process each character in the kanji group
        kanji_html_parts = []
        for char in kanji_group:
            if is_kanji(char):
                kanji_html_parts.append(wrap_kanji_in_link(char))
            else:
                kanji_html_parts.append(html.escape(char))

        kanji_html = ''.join(kanji_html_parts)
        return f'<ruby>{kanji_html}<rp>(</rp><rt>{reading}</rt><rp>)</rp></ruby>'

    # Process furigana patterns
    parts = []
    last_end = 0
    for match in FURIGANA_PATTERN.finditer(text):
        # Add text before this match
        if match.start() > last_end:
            before_text = text[last_end:match.start()]
            # Process any kanji outside furigana notation
            processed_before = []
            for char in before_text:
                if is_kanji(char):
                    processed_before.append(wrap_kanji_in_link(char))
                else:
                    processed_before.append(html.escape(char))
            parts.append(''.join(processed_before))
        # Add the processed furigana
        parts.append(replace_furigana_with_links(match))
        last_end = match.end()

    # Add any remaining text after the last match
    if last_end < len(text):
        remaining = text[last_end:]
        processed_remaining = []
        for char in remaining:
            if is_kanji(char):
                processed_remaining.append(wrap_kanji_in_link(char))
            else:
                processed_remaining.append(html.escape(char))
        parts.append(''.join(processed_remaining))

    return ''.join(parts)


def process_notes_text(text: str, entries_dict: dict = None, relative_path: str = '../../') -> str:
    """
    Process notes text with proper formatting.

    Args:
        text: The notes text to process
        entries_dict: Optional dict of entries for word link processing
        relative_path: Path prefix for entry links

    Returns:
        Formatted HTML string with furigana (and word links if entries_dict provided)
    """
    if not text:
        return ''

    # Choose processing function based on whether word links are enabled
    def process_text(t):
        if entries_dict is not None:
            return process_word_links(t, entries_dict, relative_path)
        return process_furigana(t)

    paragraphs = text.split('\n\n')
    result = []

    for para in paragraphs:
        lines = para.split('\n')
        has_bullets = any(line.strip().startswith('- ') or line.strip().startswith('・') for line in lines)

        if has_bullets:
            html_parts = []
            list_items = []

            for line in lines:
                trimmed = line.strip()
                if trimmed.startswith('- ') or trimmed.startswith('・'):
                    content = re.sub(r'^[-・]\s*', '', trimmed)
                    list_items.append(f'<li>{process_text(content)}</li>')
                elif trimmed:
                    if list_items:
                        html_parts.append(f'<ul>{"".join(list_items)}</ul>')
                        list_items = []
                    html_parts.append(f'<p>{process_text(trimmed)}</p>')

            if list_items:
                html_parts.append(f'<ul>{"".join(list_items)}</ul>')

            result.append(''.join(html_parts))
        else:
            processed = '<br>'.join(
                process_text(line.strip())
                for line in lines
                if line.strip()
            )
            result.append(f'<p>{processed}</p>')

    return ''.join(result)


def format_jst_datetime(iso_string: str) -> str:
    """Format an ISO datetime string to JST format: YYYY.M.D H:MM"""
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        dt_jst = dt.astimezone(JST)
        return f"{dt_jst.year}.{dt_jst.month}.{dt_jst.day} {dt_jst.hour}:{dt_jst.minute:02d}"
    except (ValueError, AttributeError):
        return ''


def generate_header_search_redirect_script() -> str:
    """Generate a lightweight header search script that redirects to index.html.

    This is for main pages (advanced, browse, recent, random, pending) that
    don't need the full search functionality - they just redirect to index.html
    with the query parameters.
    """
    return '''<script>
(function() {
    'use strict';

    var searchInput = document.getElementById('header-search-input');
    var searchButton = document.getElementById('header-search-button');

    if (!searchInput || !searchButton) return;

    function detectQueryType(query) {
        if (/[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]/.test(query)) {
            return 'japanese';
        }
        if (/^[a-z]+$/i.test(query)) {
            return query.length <= 10 ? 'romaji' : 'english';
        }
        return 'english';
    }

    function performSearch() {
        var query = searchInput.value.trim();
        if (!query) return;

        // Redirect to index.html with search parameter
        var searchType = detectQueryType(query);
        window.location.href = 'index.html?q=' + encodeURIComponent(query) + '&type=' + searchType;
    }

    searchButton.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') performSearch();
    });
})();
</script>'''


def generate_html_head(title: str, relative_path: str = '', description: str = '') -> str:
    """Generate HTML head section."""
    desc = description or 'TKG Japanese-English Learner\'s Dictionary (TKGJE) - An explanatory dictionary for learners of Japanese'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html.escape(desc).replace('&#x27;', "'")}">
    <title>{html.escape(title)} - TKG Japanese-English Learner's Dictionary</title>
    <link rel="stylesheet" href="{relative_path}styles.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23FFEA00'/><circle cx='50' cy='50' r='30' fill='%23FFC107'/><circle cx='42' cy='42' r='8' fill='white' opacity='0.4'/></svg>">
</head>'''


def generate_entry_html(entry: dict, entries_dict: dict, readings_to_entries: dict,
                        relative_path: str = '../../') -> str:
    """Generate HTML content for a single entry page."""
    entry_id = entry['id']
    headword = entry['headword']
    reading = entry['reading']
    dir_range = get_directory_range(entry_id)

    # Build title
    headword_plain = strip_furigana(headword)
    title = f"{headword_plain} ({reading})"
    description = f"{headword_plain} - {entry['gloss']}. Japanese-English dictionary entry with definitions and examples."

    html_parts = [
        generate_html_head(title, relative_path, description),
        '<body>',
        generate_nav_header(relative_path, show_all_links=False),
        '<main class="entry-page">',
        '<article class="entry-display">',
    ]

    # Entry header with kanji links in headword
    html_parts.append(f'''
        <div class="entry-header">
            <h1 class="entry-headword">{process_headword_with_kanji_links(headword, relative_path)}</h1>
            <div class="entry-reading">{html.escape(reading)}</div>
            <div class="entry-pos">{html.escape(entry.get('part_of_speech', ''))}</div>
            <div class="entry-gloss">{html.escape(entry.get('gloss', ''))}</div>
        </div>
    ''')

    # Definitions and Examples
    definitions = entry.get('definitions', [])
    examples = entry.get('examples', [])

    # Helper function to render examples
    def render_examples(examples_list):
        """Render a list of examples as HTML with word links."""
        parts = []
        for ex in examples_list:
            japanese = ex.get('japanese', '')
            english = ex.get('english', '')
            notes = ex.get('notes', '')
            # Use process_word_links to handle link markup (falls back to furigana if no links)
            japanese_html = process_word_links(japanese, entries_dict, relative_path)
            notes_html = process_word_links(notes, entries_dict, relative_path) if notes else ''
            parts.append(f'''
                <div class="example-item">
                    <div class="example-japanese">{japanese_html}</div>
                    <div class="example-english">{html.escape(english)}</div>
                    {f'<div class="example-notes">{notes_html}</div>' if notes else ''}
                </div>
            ''')
        return ''.join(parts)

    # Determine if we should group examples by sense (only for multi-sense entries)
    has_multiple_senses = len(definitions) > 1

    if has_multiple_senses:
        # Group examples by sense number
        examples_by_sense = defaultdict(list)
        for ex in examples:
            sense_numbers = ex.get('sense_numbers', [])
            if sense_numbers:
                for sense_num in sense_numbers:
                    examples_by_sense[sense_num].append(ex)
            else:
                # Examples without sense_numbers go to a "general" bucket (sense 0)
                examples_by_sense[0].append(ex)

        # Render definitions with their corresponding examples
        html_parts.append('<div class="definitions-with-examples">')
        for defn in definitions:
            sense = defn.get('sense_number', '')
            gloss = defn.get('gloss', '')
            explanation = defn.get('explanation', '')

            html_parts.append(f'''
                <div class="sense-block">
                    <div class="definition-item">
                        <span class="definition-number">{sense}.</span>
                        <span class="definition-gloss">{html.escape(gloss)}</span>
                        {f'<div class="definition-explanation">{process_furigana(explanation)}</div>' if explanation else ''}
                    </div>
            ''')

            # Add examples for this sense
            sense_examples = examples_by_sense.get(sense, [])
            if sense_examples:
                html_parts.append('<div class="sense-examples examples">')
                html_parts.append(render_examples(sense_examples))
                html_parts.append('</div>')

            html_parts.append('</div>')  # Close sense-block

        # Add any "general" examples that weren't assigned to a specific sense
        general_examples = examples_by_sense.get(0, [])
        if general_examples:
            html_parts.append('<div class="examples general-examples">')
            html_parts.append(render_examples(general_examples))
            html_parts.append('</div>')

        html_parts.append('</div>')  # Close definitions-with-examples
    else:
        # Single sense or no senses: use original layout (definitions then examples)
        if definitions:
            html_parts.append('<div class="definitions">')
            for defn in definitions:
                sense = defn.get('sense_number', '')
                gloss = defn.get('gloss', '')
                explanation = defn.get('explanation', '')
                html_parts.append(f'''
                    <div class="definition-item">
                        <span class="definition-number">{sense}.</span>
                        <span class="definition-gloss">{html.escape(gloss)}</span>
                        {f'<div class="definition-explanation">{process_furigana(explanation)}</div>' if explanation else ''}
                    </div>
                ''')
            html_parts.append('</div>')

        if examples:
            html_parts.append('<div class="examples">')
            html_parts.append(render_examples(examples))
            html_parts.append('</div>')

    # Notes
    notes = entry.get('notes', '')
    if notes:
        processed_notes = process_notes_text(notes, entries_dict, relative_path)
        html_parts.append(f'''
            <div class="entry-notes">
                <div class="notes-content">{processed_notes}</div>
            </div>
        ''')

    # Cross-references
    cross_refs = entry.get('cross_references', [])
    if cross_refs:
        html_parts.append('<div class="cross-references"><h2>Related Words</h2>')
        for ref in cross_refs:
            if isinstance(ref, str):
                # String reference is an entry ID
                ref_type = 'see_also'
                target_id = ref
                resolved = target_id in entries_dict
                if resolved:
                    target = entries_dict[target_id]
                    ref_headword = target['headword']
                    ref_reading = target['reading']
                else:
                    ref_headword = ''
                    ref_reading = ''
                label = ''
            else:
                # Object reference
                ref_type = ref.get('type', 'see_also')
                ref_reading = ref.get('reading', '')
                ref_headword = ref.get('headword', '')
                label = ref.get('label', '')

                # Priority 1: Check for hardcoded target_id
                target_id = ref.get('target_id', '')

                if target_id:
                    # Use target_id directly
                    resolved = target_id in entries_dict
                    if resolved and not ref_headword:
                        # Fill in headword from target entry if not provided
                        target = entries_dict[target_id]
                        ref_headword = target['headword']
                else:
                    # Priority 2: Fall back to reading/headword resolution
                    candidates = readings_to_entries.get(ref_reading, [])

                    if len(candidates) == 1:
                        # Only one entry with this reading
                        # If headword specified, verify it matches (for homonym disambiguation)
                        if ref_headword and candidates[0]['headword'] != ref_headword:
                            # Headword mismatch - this is likely a homonym not yet in dictionary
                            target_id = ''  # Leave unresolved
                        else:
                            target_id = candidates[0]['id']
                    elif len(candidates) > 1 and ref_headword:
                        # Multiple entries - try to match by headword
                        for candidate in candidates:
                            if candidate['headword'] == ref_headword:
                                target_id = candidate['id']
                                break

                    resolved = target_id in entries_dict

                # If still no headword, use reading for display
                if not ref_headword:
                    ref_headword = ref_reading

            type_label = get_cross_ref_label(ref_type)
            display = process_furigana(ref_headword) if ref_headword else html.escape(ref_reading)
            label_text = f' ({html.escape(label)})' if label else ''

            if resolved and target_id:
                target_dir_range = get_directory_range(target_id)
                html_parts.append(f'''
                    <div class="cross-ref">
                        <span class="cross-ref-type">{html.escape(type_label)}:</span>
                        <a href="{relative_path}entries/{target_dir_range}/{target_id}.html" class="cross-ref-link">
                            {display}{label_text}
                        </a>
                    </div>
                ''')
            else:
                html_parts.append(f'''
                    <div class="cross-ref pending">
                        <span class="cross-ref-type">{html.escape(type_label)}:</span>
                        <span class="cross-ref-pending">{display}{label_text}</span>
                    </div>
                ''')
        html_parts.append('</div>')

    # Metadata
    metadata = entry.get('metadata', {})
    created = metadata.get('created', '')
    modified = metadata.get('modified', '')
    created_str = format_jst_datetime(created)
    modified_str = format_jst_datetime(modified)
    is_revised = created and modified and created != modified
    vocabulary_tier = metadata.get('vocabulary_tier', '')

    date_display = ''
    if created_str:
        date_display = f'Added {created_str}'
        if is_revised and modified_str:
            date_display += f' · Revised {modified_str}'

    file_path = f'{dir_range}/{entry_id}'

    html_parts.append(f'''
        <div class="entry-metadata">
            <div class="metadata-row">
                <div class="metadata-badges">
                    {f'<span class="badge tier-{vocabulary_tier}">{vocabulary_tier}</span>' if vocabulary_tier else ''}
                </div>
                <div class="metadata-dates">{date_display}</div>
                <div class="metadata-file">{html.escape(file_path)}</div>
            </div>
        </div>
    ''')

    html_parts.append('</article>')
    html_parts.append('</main>')

    # Footer
    html_parts.append(f'''
        <footer>
            <p><a href="{relative_path}index.html">TKG Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')

    html_parts.append(generate_header_search_script(relative_path))
    html_parts.append(generate_furigana_script())
    html_parts.append(generate_examples_script())
    html_parts.append(generate_wordlinks_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_index_page(entry_count: int, tier_counts: dict, build_time_jst: str) -> str:
    """Generate the main index.html page."""
    basic_count = tier_counts.get('basic', 0)
    core_count = tier_counts.get('core', 0)
    general_count = tier_counts.get('general', 0)

    return f'''{generate_html_head("Home")}
<body>
{generate_nav_header()}
<main class="home-page">
    <div class="hero">
        <h1>TKG Japanese-English Learner's Dictionary</h1>
    </div>

    <section class="search-section">
        <div class="search-form">
            <input type="text" id="search-input" placeholder="Search Japanese, English, or romaji..." autocomplete="off">
            <button type="button" id="search-button">Search</button>
        </div>

        <div class="search-options">
            <label><input type="radio" name="search-type" value="auto" checked> Auto-detect</label>
            <label><input type="radio" name="search-type" value="japanese"> Japanese</label>
            <label><input type="radio" name="search-type" value="english"> English</label>
            <label><input type="radio" name="search-type" value="romaji"> Romaji</label>
        </div>

        <div id="results-section" class="results-section" style="display: none;">
            <h2 id="results-heading">Results</h2>
            <div id="results-list" class="results-list"></div>
        </div>

        <noscript>
            <div class="noscript-notice">
                <p>JavaScript is required for the search feature. You can still <a href="browse.html">browse entries</a> by kana row.</p>
            </div>
        </noscript>
    </section>

    <section class="intro">
        <p>The TKG Japanese-English Learner's Dictionary (TKGJE) is an explanatory dictionary designed for learners of Japanese as a second language. It currently contains {entry_count:,} entries organized into three vocabulary tiers: {basic_count:,} basic words for beginners, {core_count:,} core vocabulary for intermediate learners, and {general_count:,} general vocabulary for advanced study. Each entry includes explanatory definitions, natural example sentences optimized for learning, usage notes covering grammar, register, and common patterns, and furigana readings for all kanji. The dictionary is under active development.</p>
    </section>
</main>

<script src="search-index.js"></script>
<script src="search.js"></script>

<footer>
    <p>TKG Japanese-English Learner's Dictionary - Under Development</p>
    <p>Last update: {build_time_jst}</p>
</footer>
{generate_furigana_script()}
{generate_examples_script()}
{generate_wordlinks_script()}
</body>
</html>'''


def generate_tag_search_styles() -> str:
    """Generate CSS styles for the tag-based search UI."""
    return '''
    <style>
        /* Tag Search UI Styles */
        .tag-search-section {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 2px solid #ddd;
        }
        .tag-search-section h2 { margin-bottom: 1rem; }
        .tag-search-modes {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }
        .tag-search-modes button {
            padding: 0.5rem 1rem;
            border: 1px solid #ccc;
            background: #f5f5f5;
            cursor: pointer;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        .tag-search-modes button.active {
            background: #4a90d9;
            color: white;
            border-color: #4a90d9;
        }
        .tag-filter-panel {
            background: #f9f9f9;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        }
        .filter-group { margin-bottom: 1.5rem; }
        .filter-group:last-child { margin-bottom: 0; }
        .filter-group h3 {
            margin: 0 0 0.5rem 0;
            font-size: 1rem;
            color: #333;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .filter-group h3 .count {
            font-size: 0.8rem;
            color: #666;
            font-weight: normal;
        }
        .filter-options {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .filter-options label {
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.25rem 0.5rem;
            background: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85rem;
        }
        .filter-options label:hover { background: #f0f0f0; }
        .filter-options label.checked {
            background: #e3f2fd;
            border-color: #4a90d9;
        }
        .filter-note {
            font-size: 0.8rem;
            color: #e67e22;
            margin-top: 0.25rem;
            font-style: italic;
        }
        .filter-actions {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }
        .filter-actions button {
            padding: 0.5rem 1rem;
            border: 1px solid #ccc;
            background: white;
            cursor: pointer;
            border-radius: 4px;
            font-size: 0.9rem;
        }
        .filter-actions button:hover { background: #f0f0f0; }
        .filter-actions button.primary {
            background: #4a90d9;
            color: white;
            border-color: #4a90d9;
        }
        .filter-actions button.primary:hover { background: #3a7bc8; }
        .tag-results { margin-top: 1.5rem; }
        .tag-results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .tag-results-count { font-weight: bold; color: #333; }
        .tag-results-export { display: flex; gap: 0.5rem; }
        .tag-results-export button {
            padding: 0.25rem 0.5rem;
            border: 1px solid #ccc;
            background: white;
            cursor: pointer;
            border-radius: 4px;
            font-size: 0.8rem;
        }
        .tag-results-list { display: grid; gap: 0.5rem; }
        .tag-result-item {
            display: grid;
            grid-template-columns: 1fr 1fr 2fr auto;
            gap: 1rem;
            padding: 0.75rem;
            background: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            text-decoration: none;
            color: inherit;
            align-items: center;
        }
        .tag-result-item:hover {
            background: #f5f5f5;
            border-color: #4a90d9;
        }
        .tag-result-headword { font-weight: bold; }
        .tag-result-reading { color: #666; }
        .tag-result-gloss { color: #333; }
        .tag-result-tags { font-size: 0.75rem; color: #888; }
        .stats-panel { display: none; }
        .stats-panel.active { display: block; }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        .stats-card {
            background: #f9f9f9;
            padding: 1rem;
            border-radius: 8px;
        }
        .stats-card h3 { margin: 0 0 0.75rem 0; font-size: 1rem; }
        .stats-item {
            display: flex;
            justify-content: space-between;
            padding: 0.25rem 0;
            border-bottom: 1px solid #eee;
            font-size: 0.9rem;
        }
        .stats-item:last-child { border-bottom: none; }
        .stats-value { font-weight: bold; }
        .stats-bar {
            width: 60px;
            height: 8px;
            background: #eee;
            border-radius: 4px;
            overflow: hidden;
            display: inline-block;
            vertical-align: middle;
            margin-left: 0.5rem;
        }
        .stats-bar-fill { height: 100%; background: #4a90d9; }
        .missing-panel { display: none; }
        .missing-panel.active { display: block; }
        .missing-selector {
            background: #f9f9f9;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .missing-selector h3 { margin: 0 0 0.5rem 0; font-size: 1rem; }
        .missing-options {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .missing-options label {
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.25rem 0.5rem;
            background: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85rem;
        }
        .combined-panel { display: none; }
        .combined-panel.active { display: block; }
        .query-builder {
            background: #f9f9f9;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
        }
        .query-builder textarea {
            width: 100%;
            min-height: 100px;
            font-family: monospace;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-bottom: 0.5rem;
        }
        .query-examples { font-size: 0.85rem; color: #666; }
        .query-examples code {
            background: #e9e9e9;
            padding: 0.1rem 0.3rem;
            border-radius: 3px;
        }
        .pagination {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        .pagination button {
            padding: 0.5rem 1rem;
            border: 1px solid #ccc;
            background: white;
            cursor: pointer;
            border-radius: 4px;
        }
        .pagination button:disabled { opacity: 0.5; cursor: not-allowed; }
        .pagination button.current {
            background: #4a90d9;
            color: white;
            border-color: #4a90d9;
        }
        .page-info { padding: 0.5rem 1rem; color: #666; }
        @media (max-width: 768px) {
            .tag-result-item { grid-template-columns: 1fr; gap: 0.25rem; }
            .stats-grid { grid-template-columns: 1fr; }
        }
    </style>
'''


def generate_tag_search_section() -> str:
    """Generate the tag-based search section HTML."""
    return '''
    <!-- Tag-Based Search Section -->
    <section class="tag-search-section">
        <h2>Tag-Based Search</h2>

        <div class="tag-search-modes">
            <button class="mode-btn active" data-mode="filter">Filter by Tags</button>
            <button class="mode-btn" data-mode="stats">Tag Statistics</button>
            <button class="mode-btn" data-mode="missing">Find Missing Tags</button>
            <button class="mode-btn" data-mode="combined">Combined Query</button>
        </div>

        <!-- Filter Mode Panel -->
        <div id="filter-panel" class="tag-filter-panel">
            <div class="filter-actions">
                <button type="button" id="apply-filters" class="primary">Apply Filters</button>
                <button type="button" id="clear-filters">Clear All</button>
                <label style="display: inline-flex; align-items: center; gap: 0.25rem;">
                    <input type="checkbox" id="filter-and-mode"> AND mode (require all)
                </label>
            </div>

            <div class="filter-group">
                <h3>Vocabulary Tier <span class="count" id="tier-count"></span></h3>
                <div class="filter-options" id="tier-filters">
                    <label><input type="checkbox" name="tier" value="basic"> basic</label>
                    <label><input type="checkbox" name="tier" value="core"> core</label>
                    <label><input type="checkbox" name="tier" value="general"> general</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Part of Speech <span class="count" id="pos-count"></span></h3>
                <div class="filter-options" id="pos-filters">
                    <label><input type="checkbox" name="pos" value="noun"> noun</label>
                    <label><input type="checkbox" name="pos" value="verb-godan"> verb-godan</label>
                    <label><input type="checkbox" name="pos" value="verb-ichidan"> verb-ichidan</label>
                    <label><input type="checkbox" name="pos" value="verb-suru"> verb-suru</label>
                    <label><input type="checkbox" name="pos" value="verb-kuru"> verb-kuru</label>
                    <label><input type="checkbox" name="pos" value="verb-irregular"> verb-irregular</label>
                    <label><input type="checkbox" name="pos" value="adjective-i"> adjective-i</label>
                    <label><input type="checkbox" name="pos" value="adjective-na"> adjective-na</label>
                    <label><input type="checkbox" name="pos" value="adjective-no"> adjective-no</label>
                    <label><input type="checkbox" name="pos" value="adjective-taru"> adjective-taru</label>
                    <label><input type="checkbox" name="pos" value="adverb"> adverb</label>
                    <label><input type="checkbox" name="pos" value="particle"> particle</label>
                    <label><input type="checkbox" name="pos" value="conjunction"> conjunction</label>
                    <label><input type="checkbox" name="pos" value="interjection"> interjection</label>
                    <label><input type="checkbox" name="pos" value="pronoun"> pronoun</label>
                    <label><input type="checkbox" name="pos" value="counter"> counter</label>
                    <label><input type="checkbox" name="pos" value="prefix"> prefix</label>
                    <label><input type="checkbox" name="pos" value="suffix"> suffix</label>
                    <label><input type="checkbox" name="pos" value="expression"> expression</label>
                    <label><input type="checkbox" name="pos" value="pre-noun-adjectival"> pre-noun-adjectival</label>
                    <label><input type="checkbox" name="pos" value="number"> number</label>
                    <label><input type="checkbox" name="pos" value="auxiliary"> auxiliary</label>
                    <label><input type="checkbox" name="pos" value="onomatopoeia"> onomatopoeia</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Transitivity (Verbs) <span class="count" id="transitivity-count"></span></h3>
                <div class="filter-options" id="transitivity-filters">
                    <label><input type="checkbox" name="transitivity" value="transitive"> transitive</label>
                    <label><input type="checkbox" name="transitivity" value="intransitive"> intransitive</label>
                    <label><input type="checkbox" name="transitivity" value="both"> both</label>
                    <label><input type="checkbox" name="transitivity" value="_missing"> (missing)</label>
                </div>
                <div class="filter-note">⚠️ Transitivity tagging is incomplete (~8% coverage). Many verbs still need tagging.</div>
            </div>

            <div class="filter-group">
                <h3>Formality <span class="count" id="formality-count"></span></h3>
                <div class="filter-options" id="formality-filters">
                    <label><input type="checkbox" name="formality" value="formal"> formal</label>
                    <label><input type="checkbox" name="formality" value="neutral"> neutral</label>
                    <label><input type="checkbox" name="formality" value="informal"> informal</label>
                    <label><input type="checkbox" name="formality" value="vulgar"> vulgar</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Politeness <span class="count" id="politeness-count"></span></h3>
                <div class="filter-options" id="politeness-filters">
                    <label><input type="checkbox" name="politeness" value="honorific"> honorific</label>
                    <label><input type="checkbox" name="politeness" value="humble"> humble</label>
                    <label><input type="checkbox" name="politeness" value="polite"> polite</label>
                    <label><input type="checkbox" name="politeness" value="plain"> plain</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Semantic Categories <span class="count" id="semantic-count"></span></h3>
                <div class="filter-options" id="semantic-filters">
                    <label><input type="checkbox" name="semantic" value="time-day-of-week"> time-day-of-week</label>
                    <label><input type="checkbox" name="semantic" value="time-month"> time-month</label>
                    <label><input type="checkbox" name="semantic" value="time-season"> time-season</label>
                    <label><input type="checkbox" name="semantic" value="time-period"> time-period</label>
                    <label><input type="checkbox" name="semantic" value="time-general"> time-general</label>
                    <label><input type="checkbox" name="semantic" value="animal-mammal"> animal-mammal</label>
                    <label><input type="checkbox" name="semantic" value="animal-bird"> animal-bird</label>
                    <label><input type="checkbox" name="semantic" value="animal-fish"> animal-fish</label>
                    <label><input type="checkbox" name="semantic" value="animal-insect"> animal-insect</label>
                    <label><input type="checkbox" name="semantic" value="animal-general"> animal-general</label>
                    <label><input type="checkbox" name="semantic" value="plant-tree"> plant-tree</label>
                    <label><input type="checkbox" name="semantic" value="plant-flower"> plant-flower</label>
                    <label><input type="checkbox" name="semantic" value="plant-general"> plant-general</label>
                    <label><input type="checkbox" name="semantic" value="weather"> weather</label>
                    <label><input type="checkbox" name="semantic" value="geography"> geography</label>
                    <label><input type="checkbox" name="semantic" value="body-part"> body-part</label>
                    <label><input type="checkbox" name="semantic" value="body-internal"> body-internal</label>
                    <label><input type="checkbox" name="semantic" value="family"> family</label>
                    <label><input type="checkbox" name="semantic" value="person"> person</label>
                    <label><input type="checkbox" name="semantic" value="occupation"> occupation</label>
                    <label><input type="checkbox" name="semantic" value="emotion"> emotion</label>
                    <label><input type="checkbox" name="semantic" value="color"> color</label>
                    <label><input type="checkbox" name="semantic" value="number"> number</label>
                    <label><input type="checkbox" name="semantic" value="direction"> direction</label>
                    <label><input type="checkbox" name="semantic" value="size"> size</label>
                    <label><input type="checkbox" name="semantic" value="quantity"> quantity</label>
                    <label><input type="checkbox" name="semantic" value="food"> food</label>
                    <label><input type="checkbox" name="semantic" value="clothing"> clothing</label>
                    <label><input type="checkbox" name="semantic" value="building"> building</label>
                    <label><input type="checkbox" name="semantic" value="transportation"> transportation</label>
                    <label><input type="checkbox" name="semantic" value="tool"> tool</label>
                    <label><input type="checkbox" name="semantic" value="furniture"> furniture</label>
                    <label><input type="checkbox" name="semantic" value="electronics"> electronics</label>
                    <label><input type="checkbox" name="semantic" value="movement"> movement</label>
                    <label><input type="checkbox" name="semantic" value="communication"> communication</label>
                    <label><input type="checkbox" name="semantic" value="cognition"> cognition</label>
                    <label><input type="checkbox" name="semantic" value="existence"> existence</label>
                    <label><input type="checkbox" name="semantic" value="creation"> creation</label>
                    <label><input type="checkbox" name="semantic" value="consumption"> consumption</label>
                    <label><input type="checkbox" name="semantic" value="greeting"> greeting</label>
                    <label><input type="checkbox" name="semantic" value="education"> education</label>
                    <label><input type="checkbox" name="semantic" value="work"> work</label>
                    <label><input type="checkbox" name="semantic" value="leisure"> leisure</label>
                    <label><input type="checkbox" name="semantic" value="proverb"> proverb</label>
                    <label><input type="checkbox" name="semantic" value="idiom"> idiom</label>
                    <label><input type="checkbox" name="semantic" value="general"> general</label>
                    <label><input type="checkbox" name="semantic" value="action"> action</label>
                    <label><input type="checkbox" name="semantic" value="descriptive"> descriptive</label>
                    <label><input type="checkbox" name="semantic" value="grammatical"> grammatical</label>
                    <label><input type="checkbox" name="semantic" value="expression"> expression</label>
                    <label><input type="checkbox" name="semantic" value="onomatopoeia"> onomatopoeia</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Style <span class="count" id="style-count"></span></h3>
                <div class="filter-options" id="style-filters">
                    <label><input type="checkbox" name="style" value="written"> written</label>
                    <label><input type="checkbox" name="style" value="spoken"> spoken</label>
                    <label><input type="checkbox" name="style" value="literary"> literary</label>
                    <label><input type="checkbox" name="style" value="archaic"> archaic</label>
                    <label><input type="checkbox" name="style" value="slang"> slang</label>
                </div>
            </div>

            <div class="filter-group">
                <h3>Domain <span class="count" id="domain-count"></span></h3>
                <div class="filter-options" id="domain-filters">
                    <label><input type="checkbox" name="domain" value="business"> business</label>
                    <label><input type="checkbox" name="domain" value="academic"> academic</label>
                    <label><input type="checkbox" name="domain" value="technical"> technical</label>
                    <label><input type="checkbox" name="domain" value="legal"> legal</label>
                    <label><input type="checkbox" name="domain" value="medical"> medical</label>
                    <label><input type="checkbox" name="domain" value="colloquial"> colloquial</label>
                    <label><input type="checkbox" name="domain" value="internet"> internet</label>
                </div>
            </div>
        </div>

        <!-- Stats Panel -->
        <div id="stats-panel" class="stats-panel">
            <div class="stats-grid" id="stats-grid"></div>
        </div>

        <!-- Missing Tags Panel -->
        <div id="missing-panel" class="missing-panel">
            <div class="missing-selector">
                <h3>Find Entries Missing:</h3>
                <div class="missing-options">
                    <label><input type="checkbox" name="missing" value="pos"> POS tags</label>
                    <label><input type="checkbox" name="missing" value="formality"> Formality</label>
                    <label><input type="checkbox" name="missing" value="politeness"> Politeness</label>
                    <label><input type="checkbox" name="missing" value="semantic"> Semantic tags</label>
                    <label><input type="checkbox" name="missing" value="transitivity"> Transitivity (verbs only)</label>
                </div>
                <div class="filter-actions">
                    <button type="button" id="find-missing" class="primary">Find Missing</button>
                </div>
            </div>
        </div>

        <!-- Combined Query Panel -->
        <div id="combined-panel" class="combined-panel">
            <div class="query-builder">
                <h3>Query Builder</h3>
                <textarea id="query-input" placeholder="Enter query (e.g., pos:verb-ichidan AND semantic:food)"></textarea>
                <div class="query-examples">
                    <strong>Examples:</strong><br>
                    <code>pos:noun AND semantic:food</code> - Food-related nouns<br>
                    <code>pos:verb-ichidan OR pos:verb-godan</code> - All main verbs<br>
                    <code>tier:basic AND pos:verb-suru</code> - Basic tier suru verbs<br>
                    <code>formality:formal AND politeness:humble</code> - Humble formal words<br>
                    <code>NOT transitivity:*</code> - Verbs without transitivity tag<br>
                    <code>semantic:emotion OR semantic:cognition</code> - Emotion/cognition words
                </div>
                <div class="filter-actions">
                    <button type="button" id="run-query" class="primary">Run Query</button>
                </div>
            </div>
        </div>

        <!-- Results Area -->
        <div id="tag-results" class="tag-results" style="display: none;">
            <div class="tag-results-header">
                <span class="tag-results-count" id="tag-results-count"></span>
                <div class="tag-results-export">
                    <button type="button" id="export-csv">Export CSV</button>
                    <button type="button" id="export-json">Export JSON</button>
                    <button type="button" id="copy-ids">Copy IDs</button>
                </div>
            </div>
            <div id="tag-results-list" class="tag-results-list"></div>
            <div id="tag-pagination" class="pagination"></div>
        </div>
    </section>
'''


def generate_advanced_page() -> str:
    """Generate the advanced.html page with tag-based search."""
    # Custom head with tag search styles
    custom_head = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="TKG Japanese-English Learner's Dictionary - Advanced tag-based search">
    <title>Advanced Search - TKG Japanese-English Learner's Dictionary</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23FFEA00'/><circle cx='50' cy='50' r='30' fill='%23FFC107'/><circle cx='42' cy='42' r='8' fill='white' opacity='0.4'/></svg>">
{generate_tag_search_styles()}
</head>'''

    return f'''{custom_head}
<body>
{generate_nav_header()}
<main class="search-page">
    <h1>Advanced Search</h1>

{generate_tag_search_section()}

    <noscript>
        <div class="noscript-notice">
            <p>JavaScript is required for the advanced search feature. You can still <a href="browse.html">browse entries</a> by kana row.</p>
        </div>
    </noscript>
</main>

<script src="search-index.js"></script>
<script src="tag-search.js"></script>

<footer>
    <p><a href="index.html">TKG Japanese-English Learner's Dictionary</a></p>
</footer>
{generate_header_search_redirect_script()}
{generate_furigana_script()}
{generate_examples_script()}
{generate_wordlinks_script()}
</body>
</html>'''


def generate_search_js() -> str:
    """Generate the search.js JavaScript file."""
    js_path = Path(__file__).parent / 'templates' / 'search.js'
    return js_path.read_text(encoding='utf-8')


def generate_tag_search_js() -> str:
    """Generate the tag-search.js JavaScript file for tag-based filtering."""
    js_path = Path(__file__).parent / 'templates' / 'tag-search.js'
    return js_path.read_text(encoding='utf-8')


def get_kana_folder_for_display(reading: str) -> str:
    """Get the kana row name for display purposes (browsing)."""
    if not reading:
        return 'a'
    first_char = reading[0]
    for row in KANA_ROWS:
        if first_char in row['kana']:
            return row['folder']
    return 'a'


def generate_browse_page(entries: list, entries_dict: dict) -> str:
    """Generate the browse.html page with entries organized by kana."""
    # Group entries by kana row
    grouped = {row['name']: [] for row in KANA_ROWS}

    for entry in entries:
        reading = entry['reading']
        if not reading:
            continue
        first_char = reading[0]
        for row in KANA_ROWS:
            if first_char in row['kana']:
                grouped[row['name']].append(entry)
                break

    # Sort each group
    for row_name in grouped:
        grouped[row_name].sort(key=lambda e: e['reading'])

    # Generate HTML
    html_parts = [
        generate_html_head("Browse"),
        '<body>',
        generate_nav_header(),
        '<main class="browse-page">',
        '<h1>Browse Entries</h1>',
        '<p class="browse-intro">Click on a kana row to expand and see entries.</p>',
    ]

    for row in KANA_ROWS:
        row_entries = grouped[row['name']]
        if not row_entries:
            continue

        html_parts.append(f'''
            <details class="kana-section">
                <summary class="kana-header">
                    <span class="kana-name">{row['name']}</span>
                    <span class="kana-count">{len(row_entries)} entries</span>
                </summary>
                <div class="kana-entries">
        ''')

        for entry in row_entries:
            dir_range = get_directory_range(entry['id'])
            headword_html = process_furigana(entry['headword'])
            html_parts.append(f'''
                <a href="entries/{dir_range}/{entry['id']}.html" class="browse-entry">
                    <span class="browse-headword">{headword_html}</span>
                    <span class="browse-reading">{html.escape(entry['reading'])}</span>
                    <span class="browse-gloss">{html.escape(entry.get('gloss', ''))}</span>
                </a>
            ''')

        html_parts.append('</div></details>')

    html_parts.append('</main>')
    html_parts.append('''
        <footer>
            <p><a href="index.html">TKG Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_header_search_redirect_script())
    html_parts.append(generate_furigana_script())
    html_parts.append(generate_examples_script())
    html_parts.append(generate_wordlinks_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_recent_page(recent_entries: list, entries_dict: dict) -> str:
    """Generate the recent.html page."""
    html_parts = [
        generate_html_head("Recent Entries"),
        '<body>',
        generate_nav_header(),
        '<main class="recent-page">',
        '<h1>Recent Entries</h1>',
        '<p class="recent-intro">Most recently added or revised entries.</p>',
        '<div class="recent-list">',
    ]

    for item in recent_entries:
        entry_id = item['id']
        if entry_id not in entries_dict:
            continue

        entry = entries_dict[entry_id]
        dir_range = get_directory_range(entry_id)
        headword_html = process_furigana(item.get('headword', entry['headword']))
        status = item.get('status', 'NEW')
        date = item.get('date', '')
        gloss = item.get('gloss', entry.get('gloss', ''))

        status_class = status.lower()

        html_parts.append(f'''
            <a href="entries/{dir_range}/{entry_id}.html" class="recent-item">
                <span class="recent-headword">{headword_html}</span>
                <span class="recent-gloss">{html.escape(gloss)}</span>
                <span class="recent-status {status_class}">{status}</span>
                <span class="recent-date">{html.escape(date)}</span>
            </a>
        ''')

    html_parts.append('</div>')
    html_parts.append('</main>')
    html_parts.append('''
        <footer>
            <p><a href="index.html">TKG Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_header_search_redirect_script())
    html_parts.append(generate_furigana_script())
    html_parts.append(generate_examples_script())
    html_parts.append(generate_wordlinks_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_random_page(entries: list) -> str:
    """Generate the random.html page."""
    html_parts = [
        generate_html_head("Random"),
        '<body>',
        generate_nav_header(),
        '<main class="random-page">',
        '<h1>Random Word Cloud</h1>',
        '<p class="random-intro">Click any word to view its entry. Refresh the page for a new arrangement.</p>',
        '<div class="random-words" id="random-words">',
    ]

    for entry in entries:
        dir_range = get_directory_range(entry['id'])
        headword_html = process_furigana(entry['headword'])
        html_parts.append(f'''
            <a href="entries/{dir_range}/{entry['id']}.html" class="random-word">{headword_html}</a>
        ''')

    html_parts.append('</div>')
    html_parts.append('</main>')
    html_parts.append('''
        <footer>
            <p><a href="index.html">TKG Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_header_search_redirect_script())
    html_parts.append(generate_furigana_script())
    html_parts.append(generate_examples_script())
    html_parts.append(generate_wordlinks_script())
    # Add shuffle script for random arrangement on page load
    html_parts.append('''<script>
(function() {
    var container = document.getElementById('random-words');
    if (!container) return;
    var words = Array.from(container.children);
    // Fisher-Yates shuffle
    for (var i = words.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = words[i];
        words[i] = words[j];
        words[j] = temp;
    }
    // Re-append in shuffled order
    words.forEach(function(word) {
        container.appendChild(word);
    });
})();
</script>''')
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_pending_page(candidates: list) -> str:
    """Generate the pending.html page showing candidate words."""
    html_parts = [
        generate_html_head("Pending"),
        '<body>',
        generate_nav_header(),
        '<main class="pending-page">',
        '<h1>Pending Words</h1>',
        f'<p class="pending-intro">Candidate words awaiting dictionary entry creation ({len(candidates):,} words). Most recently added appear first.</p>',
        '<div class="pending-list">',
    ]

    # Sort by date added, most recent first
    sorted_candidates = sorted(
        candidates,
        key=lambda x: x.get('added', ''),
        reverse=True
    )

    for candidate in sorted_candidates:
        # Use 'or' to handle both missing keys and explicit None values
        word = html.escape(candidate.get('word') or '')
        reading = html.escape(candidate.get('reading') or '')
        notes = html.escape(candidate.get('notes') or '')

        html_parts.append(f'''
            <div class="pending-item">
                <span class="pending-word">{word}</span>
                <span class="pending-reading">{reading}</span>
                <span class="pending-notes">{notes}</span>
            </div>
        ''')

    html_parts.append('</div>')
    html_parts.append('</main>')
    html_parts.append('''
        <footer>
            <p><a href="index.html">TKG Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_header_search_redirect_script())
    html_parts.append(generate_furigana_script())
    html_parts.append(generate_examples_script())
    html_parts.append(generate_wordlinks_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


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


def generate_stylesheet() -> str:
    """Generate the shared CSS stylesheet for the flat site."""
    css_path = Path(__file__).parent / 'templates' / 'styles.css'
    return css_path.read_text(encoding='utf-8')


def load_entry(file_path: Path) -> dict:
    """Load a single entry file.

    Raises:
        ValueError: If the JSON file is malformed, with the file path included in the error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {file_path}: {e}") from e


def build_recent_entries(entries: list, limit: int = 250) -> list:
    """Build a list of recently added or modified entries."""
    def get_modified_date(entry):
        try:
            dt = datetime.fromisoformat(entry['metadata']['modified'].replace('Z', '+00:00'))
            # Handle timezone-naive datetimes (assume UTC)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except (KeyError, ValueError):
            # Return timezone-aware fallback to avoid mixing with aware datetimes
            return datetime.min.replace(tzinfo=timezone.utc)

    sorted_entries = sorted(entries, key=get_modified_date, reverse=True)

    recent = []
    for entry in sorted_entries[:limit]:
        metadata = entry.get('metadata', {})
        modified = metadata.get('modified', '')
        created = metadata.get('created', '')
        status = 'NEW' if created == modified else 'REVISED'
        date_str = format_jst_datetime(modified)

        recent.append({
            'id': entry['id'],
            'headword': entry['headword'],
            'gloss': entry['gloss'],
            'status': status,
            'date': date_str
        })

    return recent


def build_flat(project_root: Path) -> int:
    """
    Build the flat HTML version of the dictionary.
    Returns 0 on success, 1 on failure.
    """
    docs_dir = project_root / 'docs'
    entries_dir = project_root / 'entries'

    print("\nFlat HTML Build")
    print("=" * 50)

    # Step 1: Load all entries
    print("\n[1/6] Loading entries...")
    entries = []
    for file_path in entries_dir.glob('**/*.json'):
        entry = load_entry(file_path)
        entry['_source_file'] = str(file_path)
        entries.append(entry)

    # Sort entries by reading
    entries.sort(key=lambda e: e['reading'])
    print(f"  Loaded {len(entries)} entries")

    # Check for duplicate IDs before creating dictionary
    seen_ids = {}
    for e in entries:
        entry_id = e['id']
        if entry_id in seen_ids:
            print(f"  ERROR: Duplicate entry ID '{entry_id}' found!")
            print(f"    First occurrence: {seen_ids[entry_id]}")
            print(f"    Second occurrence: {e.get('_source_file', 'unknown')}")
            sys.exit(1)
        else:
            seen_ids[entry_id] = e.get('_source_file', 'unknown')

    # Create entries dictionary for cross-reference lookups
    entries_dict = {e['id']: e for e in entries}

    # Create reading-to-entries mapping for resolving cross-references
    # Maps reading -> list of {id, headword} for deterministic resolution
    readings_to_entries = defaultdict(list)
    for e in entries:
        readings_to_entries[e['reading']].append({
            'id': e['id'],
            'headword': e.get('headword', '')
        })

    # Step 2: Create output directories (atomic build pattern)
    print("\n[2/6] Creating output directories...")

    # Build to a temporary directory first, then swap atomically
    # This ensures a failed build doesn't leave docs/ in a broken state
    temp_dir = project_root / 'docs_build_temp'
    backup_dir = project_root / 'docs_backup'
    preserved_dirs = {'flat', 'kanji'}  # Directories to preserve
    preserved_files = {'about.html', 'CNAME'}  # Files to preserve (not overwritten by build)

    # Clean up any leftover temp/backup dirs from previous failed builds
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    if backup_dir.exists():
        shutil.rmtree(backup_dir)

    temp_dir.mkdir(parents=True, exist_ok=True)

    # Copy preserved directories from existing docs/ to temp build dir
    if docs_dir.exists():
        for preserved in preserved_dirs:
            src = docs_dir / preserved
            if src.exists():
                shutil.copytree(src, temp_dir / preserved)
        # Copy preserved files
        for preserved_file in preserved_files:
            src = docs_dir / preserved_file
            if src.exists():
                shutil.copy2(src, temp_dir / preserved_file)

    # Ensure about.html exists with content (manually-edited file, not generated)
    # If missing or empty, try to restore from git history
    about_path = temp_dir / 'about.html'
    if not about_path.exists() or about_path.stat().st_size == 0:
        print(f"  WARNING: about.html is missing or empty - attempting git restore")
        try:
            import subprocess
            # Get about.html from the most recent commit where it had content
            result = subprocess.run(
                ['git', 'log', '--oneline', '--diff-filter=M', '-1', '--', 'docs/about.html'],
                capture_output=True, text=True, cwd=project_root
            )
            if result.returncode == 0 and result.stdout.strip():
                commit_hash = result.stdout.strip().split()[0]
                # Try to get content from parent of deletion commit
                restore_result = subprocess.run(
                    ['git', 'show', f'{commit_hash}:docs/about.html'],
                    capture_output=True, text=True, cwd=project_root
                )
                if restore_result.returncode == 0 and restore_result.stdout.strip():
                    with open(about_path, 'w', encoding='utf-8') as f:
                        f.write(restore_result.stdout)
                    print(f"  Restored about.html from git commit {commit_hash}")
                else:
                    print(f"  ERROR: Could not restore about.html from git - file may need manual restoration")
            else:
                print(f"  ERROR: Could not find about.html in git history - file may need manual restoration")
        except Exception as e:
            print(f"  ERROR: Git restore failed for about.html: {e}")

    # Always ensure CNAME file exists with canonical content
    # This protects against accidental deletion of the custom domain config
    cname_path = temp_dir / 'CNAME'
    if not cname_path.exists():
        print(f"  WARNING: CNAME file was missing - restoring from canonical value")
        with open(cname_path, 'w', encoding='utf-8') as f:
            f.write(GITHUB_PAGES_CNAME + '\n')
    else:
        # Verify CNAME has correct content
        with open(cname_path, 'r', encoding='utf-8') as f:
            current_cname = f.read().strip()
        if current_cname != GITHUB_PAGES_CNAME:
            print(f"  WARNING: CNAME had unexpected content '{current_cname}' - fixing")
            with open(cname_path, 'w', encoding='utf-8') as f:
                f.write(GITHUB_PAGES_CNAME + '\n')

    # Use temp_dir for all build output (reassign docs_dir for the build)
    original_docs_dir = docs_dir
    docs_dir = temp_dir

    # Entry directories will be created dynamically with range subdirectories
    entries_output_dir = docs_dir / 'entries'

    print(f"  Created {docs_dir}")

    # Step 3: Generate entry pages
    print("\n[3/6] Generating entry pages...")
    for entry in entries:
        dir_range = get_directory_range(entry['id'])
        entry_html = generate_entry_html(entry, entries_dict, readings_to_entries)
        # Create directory structure: entries/{range}/
        output_dir = entries_output_dir / dir_range
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{entry['id']}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(entry_html)
    print(f"  Generated {len(entries)} entry pages")

    # Count vocabulary tiers
    tier_counts = {'basic': 0, 'core': 0, 'general': 0, 'unassigned': 0}
    for entry in entries:
        tier = entry.get('metadata', {}).get('vocabulary_tier', '')
        if tier in ('basic', 'core', 'general'):
            tier_counts[tier] += 1
        else:
            tier_counts['unassigned'] += 1

    # Generate build timestamp in JST
    build_time = datetime.now(JST)
    build_time_jst = f"{build_time.year}.{build_time.month}.{build_time.day} {build_time.hour}:{build_time.minute:02d}"

    # Step 4: Generate navigation pages
    print("\n[4/6] Generating navigation pages...")

    # Index page (with search form)
    with open(docs_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(generate_index_page(len(entries), tier_counts, build_time_jst))

    # Advanced search page (tag-based)
    with open(docs_dir / 'advanced.html', 'w', encoding='utf-8') as f:
        f.write(generate_advanced_page())

    # Browse page
    with open(docs_dir / 'browse.html', 'w', encoding='utf-8') as f:
        f.write(generate_browse_page(entries, entries_dict))

    # Recent page
    recent_entries = build_recent_entries(entries)
    with open(docs_dir / 'recent.html', 'w', encoding='utf-8') as f:
        f.write(generate_recent_page(recent_entries, entries_dict))

    # Random page
    with open(docs_dir / 'random.html', 'w', encoding='utf-8') as f:
        f.write(generate_random_page(entries))

    # Pending page (candidate words)
    candidate_file = project_root / 'candidate_words.json'
    if candidate_file.exists():
        with open(candidate_file, 'r', encoding='utf-8') as f:
            candidate_data = json.load(f)
            candidates = candidate_data.get('candidates', [])
        with open(docs_dir / 'pending.html', 'w', encoding='utf-8') as f:
            f.write(generate_pending_page(candidates))

    print("  Generated index.html, advanced.html, browse.html, recent.html, random.html, pending.html")

    # Step 5: Generate search index and JavaScript
    print("\n[5/6] Generating search index...")
    with open(docs_dir / 'search-index.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_index(entries))

    with open(docs_dir / 'search.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_js())

    with open(docs_dir / 'tag-search.js', 'w', encoding='utf-8') as f:
        f.write(generate_tag_search_js())

    print("  Generated search-index.js, search.js, tag-search.js")

    # Step 6: Generate stylesheet
    print("\n[6/6] Generating stylesheet...")
    with open(docs_dir / 'styles.css', 'w', encoding='utf-8') as f:
        f.write(generate_stylesheet())
    print("  Generated styles.css")

    # Atomic swap: replace original docs/ with newly built temp_dir
    # Use shutil.move() instead of Path.rename() to handle cross-device moves
    print("\n[Swap] Atomically replacing output directory...")
    try:
        # Move original docs/ to backup (if it exists)
        if original_docs_dir.exists():
            shutil.move(str(original_docs_dir), str(backup_dir))

        # Move temp build to docs/
        shutil.move(str(docs_dir), str(original_docs_dir))

        # Remove backup after successful swap
        if backup_dir.exists():
            shutil.rmtree(backup_dir)

        print("  Swap complete")
    except OSError as e:
        print(f"  ERROR: Failed to swap directories: {e}")
        print(f"  Build output remains in: {temp_dir}")
        # Try to restore backup if swap failed midway
        if backup_dir.exists() and not original_docs_dir.exists():
            shutil.move(str(backup_dir), str(original_docs_dir))
        return 1

    # Final about.html verification (safety check after swap)
    final_about_path = original_docs_dir / 'about.html'
    if not final_about_path.exists() or final_about_path.stat().st_size == 0:
        print("\n[about.html] WARNING: about.html is missing or empty after build!")
        print("  This is a manually-edited file. Please restore it from git:")
        print("  git show HEAD~1:docs/about.html > docs/about.html")
    else:
        print("\n[about.html] Verified: About page file intact")

    # Final CNAME verification (safety check after swap)
    final_cname_path = original_docs_dir / 'CNAME'
    if not final_cname_path.exists():
        print("\n[CNAME] ERROR: CNAME file missing after build - restoring!")
        with open(final_cname_path, 'w', encoding='utf-8') as f:
            f.write(GITHUB_PAGES_CNAME + '\n')
        print(f"  Restored CNAME with: {GITHUB_PAGES_CNAME}")
    else:
        with open(final_cname_path, 'r', encoding='utf-8') as f:
            final_cname = f.read().strip()
        if final_cname != GITHUB_PAGES_CNAME:
            print(f"\n[CNAME] WARNING: CNAME has wrong content - fixing!")
            with open(final_cname_path, 'w', encoding='utf-8') as f:
                f.write(GITHUB_PAGES_CNAME + '\n')
            print(f"  Fixed CNAME: '{final_cname}' -> '{GITHUB_PAGES_CNAME}'")
        else:
            print("\n[CNAME] Verified: GitHub Pages custom domain file intact")

    # Rebuild kanji index HTML pages
    print("\n[Kanji] Rebuilding kanji index pages...")
    import subprocess
    import sys
    kanji_json_script = project_root / 'build' / 'build_kanji_json.py'
    kanji_html_script = project_root / 'build' / 'build_kanji_html.py'
    if kanji_json_script.exists() and kanji_html_script.exists():
        try:
            subprocess.run([sys.executable, str(kanji_json_script)], check=True, cwd=str(project_root))
            subprocess.run([sys.executable, str(kanji_html_script)], check=True, cwd=str(project_root))
            print("  Kanji index pages rebuilt.")
        except subprocess.CalledProcessError as e:
            print(f"  ERROR: Kanji rebuild failed: {e}")
            print("  Build cannot continue without kanji index pages.")
            return 1
    else:
        print("  ERROR: Kanji build scripts not found!")
        print("  Build cannot continue without kanji index pages.")
        return 1

    # Verify kanji HTML files were created
    kanji_html_dir = original_docs_dir / 'kanji'
    if not kanji_html_dir.exists():
        print("  ERROR: docs/kanji/ directory was not created!")
        return 1
    kanji_html_count = len(list(kanji_html_dir.glob('*.html')))
    kanji_list_path = project_root / 'kanji' / 'kanji_list.json'
    if kanji_list_path.exists():
        with open(kanji_list_path, 'r', encoding='utf-8') as f:
            expected_count = len(json.load(f).get('kanji', {}))
        if kanji_html_count != expected_count:
            print(f"  ERROR: Expected {expected_count} kanji HTML files but found {kanji_html_count}")
            return 1
        print(f"  Verified: {kanji_html_count} kanji HTML files created")

    # Generate sitemap and robots.txt
    from build_sitemap import build_sitemap
    sitemap_result = build_sitemap(project_root)
    if sitemap_result != 0:
        print("  WARNING: Sitemap generation had issues")

    # Summary
    print("\n" + "=" * 50)
    print("Build complete!")
    print(f"  Total entries: {len(entries)}")
    print(f"  Output: {original_docs_dir}")
    print("\nTo view the dictionary:")
    print(f"  Open {original_docs_dir / 'index.html'} in your browser")

    return 0


def main():
    """Main entry point."""
    import sys
    import subprocess
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    # Verify kanji index before building
    print("Verifying kanji index...")
    result = subprocess.run(
        [sys.executable, str(script_dir / 'verify_kanji_index.py'), '--quick'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("Kanji index verification failed:")
        print(result.stdout)
        print(result.stderr)
        print("\nFix issues before building.")
        sys.exit(1)

    sys.exit(build_flat(project_root))


if __name__ == '__main__':
    main()
