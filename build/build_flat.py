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
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional

from path_utils import get_entry_prefix
from japanese_utils import (
    hiragana_to_romaji, KANA_ROWS, KANA_TO_FOLDER, get_kana_folder,
    FURIGANA_PATTERN, strip_furigana
)
from constants import get_cross_ref_label

# Japan Standard Time (UTC+9)
JST = timezone(timedelta(hours=9))


def process_furigana(text: str, show_furigana: bool = True) -> str:
    """Convert furigana notation to HTML ruby tags."""
    if not text:
        return ''

    def replace_furigana(match):
        kanji = html.escape(match.group(1))
        reading = html.escape(match.group(2))
        if show_furigana:
            return f'<ruby>{kanji}<rp>(</rp><rt>{reading}</rt><rp>)</rp></ruby>'
        else:
            return kanji

    # First escape any HTML in non-furigana parts
    parts = []
    last_end = 0
    for match in FURIGANA_PATTERN.finditer(text):
        # Escape text before this match
        if match.start() > last_end:
            parts.append(html.escape(text[last_end:match.start()]))
        # Add the ruby element
        parts.append(replace_furigana(match))
        last_end = match.end()
    # Add any remaining text
    if last_end < len(text):
        parts.append(html.escape(text[last_end:]))

    return ''.join(parts)


def process_notes_text(text: str) -> str:
    """Process notes text with proper formatting."""
    if not text:
        return ''

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
                    list_items.append(f'<li>{process_furigana(content)}</li>')
                elif trimmed:
                    if list_items:
                        html_parts.append(f'<ul>{"".join(list_items)}</ul>')
                        list_items = []
                    html_parts.append(f'<p>{process_furigana(trimmed)}</p>')

            if list_items:
                html_parts.append(f'<ul>{"".join(list_items)}</ul>')

            result.append(''.join(html_parts))
        else:
            processed = '<br>'.join(
                process_furigana(line.strip())
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




def generate_nav_header(relative_path: str = '') -> str:
    """Generate navigation header HTML."""
    # Determine the base path to the flat root
    if relative_path:
        base = relative_path
    else:
        base = ''

    return f'''<header class="nav-header">
    <nav class="nav-links">
        <a href="{base}index.html" class="nav-link">Home</a>
        <a href="{base}search.html" class="nav-link">Search</a>
        <a href="{base}browse.html" class="nav-link">Browse</a>
        <a href="{base}recent.html" class="nav-link">Recent</a>
        <a href="{base}random.html" class="nav-link">Random</a>
        <a href="{base}pending.html" class="nav-link">Pending</a>
    </nav>
    <button id="furigana-toggle" class="furigana-toggle-btn" type="button" aria-pressed="false" title="Toggle furigana (reading annotations above kanji)">
        <span class="furigana-icon">振</span>
        <span class="furigana-label">Furigana</span>
    </button>
</header>'''


def generate_furigana_script() -> str:
    """Generate the furigana toggle JavaScript."""
    return '''<script>
(function() {
    var btn = document.getElementById('furigana-toggle');
    if (!btn) return;

    // Check saved preference
    var hidden = localStorage.getItem('furiganaHidden') === 'true';

    function updateState() {
        document.body.classList.toggle('furigana-hidden', hidden);
        btn.setAttribute('aria-pressed', !hidden);
        btn.classList.toggle('active', !hidden);
    }

    // Apply initial state
    updateState();

    // Toggle on click
    btn.addEventListener('click', function() {
        hidden = !hidden;
        localStorage.setItem('furiganaHidden', hidden);
        updateState();
    });
})();
</script>'''


def generate_html_head(title: str, relative_path: str = '', description: str = '') -> str:
    """Generate HTML head section."""
    desc = description or 'Japanese-English learner\'s dictionary with detailed explanations and examples'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html.escape(desc)}">
    <title>{html.escape(title)} - Japanese-English Dictionary</title>
    <link rel="stylesheet" href="{relative_path}styles.css">
</head>'''


def generate_entry_html(entry: dict, entries_dict: dict, readings_to_entries: dict, relative_path: str = '../../../') -> str:
    """Generate HTML content for a single entry page."""
    entry_id = entry['id']
    headword = entry['headword']
    reading = entry['reading']
    folder = get_kana_folder(reading)
    prefix = get_entry_prefix(entry_id)

    # Build title
    headword_plain = strip_furigana(headword)
    title = f"{headword_plain} ({reading})"
    description = f"{headword_plain} - {entry['gloss']}. Japanese-English dictionary entry with definitions and examples."

    html_parts = [
        generate_html_head(title, relative_path, description),
        '<body>',
        generate_nav_header(relative_path),
        '<main class="entry-page">',
        '<article class="entry-display">',
    ]

    # Entry header
    html_parts.append(f'''
        <div class="entry-header">
            <h1 class="entry-headword">{process_furigana(headword)}</h1>
            <div class="entry-reading">{html.escape(reading)}</div>
            <div class="entry-pos">{html.escape(entry.get('part_of_speech', ''))}</div>
            <div class="entry-gloss">{html.escape(entry.get('gloss', ''))}</div>
        </div>
    ''')

    # Definitions
    definitions = entry.get('definitions', [])
    if definitions:
        html_parts.append('<div class="definitions"><h2>Definitions</h2>')
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

    # Examples
    examples = entry.get('examples', [])
    if examples:
        html_parts.append('<div class="examples"><h2>Examples</h2>')
        for idx, ex in enumerate(examples):
            japanese = ex.get('japanese', '')
            english = ex.get('english', '')
            notes = ex.get('notes', '')

            html_parts.append(f'''
                <div class="example-item">
                    <div class="example-japanese">{process_furigana(japanese)}</div>
                    <div class="example-english">{html.escape(english)}</div>
                    {f'<div class="example-notes">{process_furigana(notes)}</div>' if notes else ''}
                </div>
            ''')
        html_parts.append('</div>')

    # Notes
    notes = entry.get('notes', '')
    if notes:
        html_parts.append(f'''
            <div class="entry-notes">
                <h2>Notes</h2>
                <div class="notes-content">{process_notes_text(notes)}</div>
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
                # Object reference - look up by reading with headword disambiguation
                ref_type = ref.get('type', 'see_also')
                ref_reading = ref.get('reading', '')
                ref_headword = ref.get('headword', '')
                label = ref.get('label', '')

                # Find matching entries by reading
                candidates = readings_to_entries.get(ref_reading, [])
                target_id = ''

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
                # If still no match and we have a headword, use it for display
                if not ref_headword:
                    ref_headword = ref_reading
                resolved = target_id in entries_dict

            type_label = get_cross_ref_label(ref_type)
            display = process_furigana(ref_headword) if ref_headword else html.escape(ref_reading)
            label_text = f' ({html.escape(label)})' if label else ''

            if resolved and target_id:
                target_folder = get_kana_folder(entries_dict[target_id]['reading'])
                target_prefix = get_entry_prefix(target_id)
                html_parts.append(f'''
                    <div class="cross-ref">
                        <span class="cross-ref-type">{html.escape(type_label)}:</span>
                        <a href="{relative_path}entries/{target_folder}/{target_prefix}/{target_id}.html" class="cross-ref-link">
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
    review_status = metadata.get('review_status', 'draft')

    date_display = ''
    if created_str:
        date_display = f'Added {created_str}'
        if is_revised and modified_str:
            date_display += f' · Revised {modified_str}'

    file_path = f'{folder}/{prefix}/{entry_id}'

    html_parts.append(f'''
        <div class="entry-metadata">
            <div class="metadata-row">
                <div class="metadata-badges">
                    {f'<span class="badge tier">{vocabulary_tier}</span>' if vocabulary_tier else ''}
                    <span class="badge status-{review_status}">{review_status}</span>
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
            <p><a href="{relative_path}index.html">Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')

    html_parts.append(generate_furigana_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_index_page(entry_count: int) -> str:
    """Generate the main index.html page."""
    return f'''{generate_html_head("Home")}
<body>
{generate_nav_header()}
<main class="home-page">
    <div class="hero">
        <h1>Japanese-English Learner's Dictionary</h1>
        <p class="subtitle">A quality-focused dictionary for learners of Japanese</p>
    </div>

    <section class="intro">
        <h2>About This Dictionary</h2>
        <p>This dictionary is designed for learners of Japanese as a second language. Unlike comprehensive resources, this dictionary prioritizes <strong>depth and quality</strong> over quantity.</p>

        <p>Each entry includes:</p>
        <ul>
            <li><strong>Explanatory definitions</strong> that go beyond simple glosses</li>
            <li><strong>Natural example sentences</strong> optimized for learning</li>
            <li><strong>Usage notes</strong> covering grammar, register, and common patterns</li>
            <li><strong>Furigana readings</strong> for all kanji</li>
        </ul>
    </section>

    <section class="stats-section">
        <h2>Dictionary Statistics</h2>
        <div class="stats-grid">
            <div class="stat-item">
                <span class="stat-number">{entry_count:,}</span>
                <span class="stat-label">Entries</span>
            </div>
        </div>
    </section>

    <section class="navigation-section">
        <h2>Explore the Dictionary</h2>
        <div class="nav-cards">
            <a href="search.html" class="nav-card">
                <h3>Search</h3>
                <p>Look up words in Japanese, English, or romaji</p>
            </a>
            <a href="browse.html" class="nav-card">
                <h3>Browse</h3>
                <p>Explore entries by kana row</p>
            </a>
            <a href="recent.html" class="nav-card">
                <h3>Recent</h3>
                <p>View recently added or revised entries</p>
            </a>
            <a href="random.html" class="nav-card">
                <h3>Random</h3>
                <p>Discover entries at random</p>
            </a>
            <a href="pending.html" class="nav-card">
                <h3>Pending</h3>
                <p>View candidate words awaiting entry creation</p>
            </a>
        </div>
    </section>
</main>

<footer>
    <p>Japanese-English Learner's Dictionary - Under Development</p>
</footer>
{generate_furigana_script()}
</body>
</html>'''


def generate_search_page() -> str:
    """Generate the search.html page."""
    return f'''{generate_html_head("Search")}
<body>
{generate_nav_header()}
<main class="search-page">
    <h1>Search the Dictionary</h1>

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
</main>

<script src="search-index.js"></script>
<script src="search.js"></script>

<footer>
    <p><a href="index.html">Japanese-English Learner's Dictionary</a></p>
</footer>
{generate_furigana_script()}
</body>
</html>'''


def generate_search_js() -> str:
    """Generate the search.js JavaScript file."""
    return '''(function() {
    'use strict';

    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const resultsSection = document.getElementById('results-section');
    const resultsHeading = document.getElementById('results-heading');
    const resultsList = document.getElementById('results-list');

    function detectQueryType(query) {
        if (/[\\u3040-\\u309f\\u30a0-\\u30ff\\u4e00-\\u9faf]/.test(query)) {
            return 'japanese';
        }
        if (/^[a-z]+$/i.test(query)) {
            return query.length <= 10 ? 'romaji' : 'english';
        }
        return 'english';
    }

    function performSearch(query, searchType) {
        if (!window.SEARCH_INDEX) return [];

        const index = window.SEARCH_INDEX;
        const entryIds = new Set();

        if (searchType === 'auto') {
            searchType = detectQueryType(query);
        }

        const queryLower = query.toLowerCase();

        if (searchType === 'japanese') {
            Object.keys(index.japanese).forEach(key => {
                if (key.includes(query)) {
                    index.japanese[key].forEach(id => entryIds.add(id));
                }
            });
        } else if (searchType === 'romaji') {
            Object.keys(index.romaji).forEach(key => {
                if (key.startsWith(queryLower)) {
                    index.romaji[key].forEach(id => entryIds.add(id));
                }
            });
        } else {
            const words = queryLower.split(/\\s+/);
            words.forEach(word => {
                Object.keys(index.english).forEach(key => {
                    if (key.startsWith(word)) {
                        index.english[key].forEach(id => entryIds.add(id));
                    }
                });
            });
        }

        // Get entry data
        const results = [];
        entryIds.forEach(id => {
            if (window.SEARCH_ENTRIES && window.SEARCH_ENTRIES[id]) {
                results.push(window.SEARCH_ENTRIES[id]);
            }
        });

        return results.sort((a, b) => a.reading.localeCompare(b.reading, 'ja'));
    }

    function displayResults(query, results) {
        resultsSection.style.display = 'block';

        if (results.length === 0) {
            resultsHeading.textContent = 'No results for "' + query + '"';
            resultsList.innerHTML = '<p class="no-results">Try a different search term.</p>';
        } else {
            resultsHeading.textContent = results.length + ' result' + (results.length === 1 ? '' : 's') + ' for "' + query + '"';
            resultsList.innerHTML = results.map(function(entry) {
                const folder = entry.folder || 'a';
                const prefix = entry.prefix || entry.id.substring(0, 2);
                return '<a href="entries/' + folder + '/' + prefix + '/' + entry.id + '.html" class="result-item">' +
                    '<div class="result-headword">' + entry.headword + '</div>' +
                    '<div class="result-reading">' + entry.reading + '</div>' +
                    '<div class="result-gloss">' + entry.gloss + '</div>' +
                '</a>';
            }).join('');
        }
    }

    function handleSearch() {
        const query = searchInput.value.trim();
        if (!query) return;

        const searchType = document.querySelector('input[name="search-type"]:checked').value;
        const results = performSearch(query, searchType);
        displayResults(query, results);
    }

    searchButton.addEventListener('click', handleSearch);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') handleSearch();
    });
})();'''


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
            folder = get_kana_folder(entry['reading'])
            prefix = get_entry_prefix(entry['id'])
            headword_html = process_furigana(entry['headword'])
            html_parts.append(f'''
                <a href="entries/{folder}/{prefix}/{entry['id']}.html" class="browse-entry">
                    <span class="browse-headword">{headword_html}</span>
                    <span class="browse-reading">{html.escape(entry['reading'])}</span>
                    <span class="browse-gloss">{html.escape(entry.get('gloss', ''))}</span>
                </a>
            ''')

        html_parts.append('</div></details>')

    html_parts.append('</main>')
    html_parts.append('''
        <footer>
            <p><a href="index.html">Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_furigana_script())
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
        folder = get_kana_folder(entry['reading'])
        prefix = get_entry_prefix(entry_id)
        headword_html = process_furigana(item.get('headword', entry['headword']))
        status = item.get('status', 'NEW')
        date = item.get('date', '')
        gloss = item.get('gloss', entry.get('gloss', ''))

        status_class = status.lower()

        html_parts.append(f'''
            <a href="entries/{folder}/{prefix}/{entry_id}.html" class="recent-item">
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
            <p><a href="index.html">Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_furigana_script())
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
        folder = get_kana_folder(entry['reading'])
        prefix = get_entry_prefix(entry['id'])
        headword_html = process_furigana(entry['headword'])
        html_parts.append(f'''
            <a href="entries/{folder}/{prefix}/{entry['id']}.html" class="random-word">{headword_html}</a>
        ''')

    html_parts.append('</div>')
    html_parts.append('</main>')
    html_parts.append('''
        <footer>
            <p><a href="index.html">Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_furigana_script())
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
            <p><a href="index.html">Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''')
    html_parts.append(generate_furigana_script())
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
        folder = get_kana_folder(reading)
        prefix = get_entry_prefix(entry_id)

        # Store minimal entry data for display
        # Note: headword is HTML-escaped by process_furigana(); gloss and reading
        # are escaped here to prevent XSS when rendered via innerHTML in search.js
        entries_data[entry_id] = {
            'id': entry_id,
            'headword': process_furigana(headword),
            'reading': html.escape(reading),
            'romaji': hiragana_to_romaji(reading),
            'gloss': html.escape(gloss),
            'folder': folder,
            'prefix': prefix
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
    return '''/* Japanese-English Dictionary - Flat Site Stylesheet */

:root {
    --color-bg: #fafafa;
    --color-surface: #ffffff;
    --color-text: #1a1a1a;
    --color-text-secondary: #666666;
    --color-border: #e0e0e0;
    --color-accent: #2563eb;
    --color-accent-hover: #1d4ed8;
    --color-accent-light: #dbeafe;
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-jp: "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif;
    --max-width: 900px;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-sans);
    font-size: 16px;
    line-height: 1.6;
    color: var(--color-text);
    background-color: var(--color-bg);
}

/* Navigation Header */
.nav-header {
    background-color: var(--color-surface);
    border-bottom: 1px solid var(--color-border);
    padding: var(--spacing-sm) var(--spacing-md);
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: var(--spacing-md);
}

.nav-links {
    display: flex;
    gap: var(--spacing-sm);
    flex-wrap: wrap;
}

.nav-link {
    color: var(--color-text-secondary);
    text-decoration: none;
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: 4px;
    transition: all 0.2s;
}

.nav-link:hover {
    color: var(--color-accent);
    background-color: var(--color-accent-light);
}

/* Furigana Toggle Button */
.furigana-toggle-btn {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    padding: 0.4rem 0.7rem;
    background-color: var(--color-bg);
    border: 1px solid var(--color-border);
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.85rem;
    color: var(--color-text-secondary);
    transition: all 0.2s;
    white-space: nowrap;
}

.furigana-toggle-btn:hover {
    border-color: var(--color-accent);
    color: var(--color-accent);
}

.furigana-toggle-btn.active {
    background-color: var(--color-accent-light);
    border-color: var(--color-accent);
    color: var(--color-accent);
}

.furigana-icon {
    font-family: var(--font-jp);
    font-size: 1rem;
}

.furigana-label {
    font-size: 0.8rem;
}

/* Furigana Hidden State */
.furigana-hidden ruby rt {
    visibility: hidden;
    font-size: 0;
}

.furigana-hidden ruby rp {
    display: none;
}

/* Main Content */
main {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: var(--spacing-lg);
}

/* Home Page */
.hero {
    text-align: center;
    padding: var(--spacing-xl) 0;
    border-bottom: 1px solid var(--color-border);
    margin-bottom: var(--spacing-xl);
}

.hero h1 {
    font-size: 2rem;
    margin-bottom: var(--spacing-sm);
}

.hero .subtitle {
    color: var(--color-text-secondary);
    font-style: italic;
}

.intro, .stats-section, .navigation-section {
    margin-bottom: var(--spacing-xl);
}

.intro h2, .stats-section h2, .navigation-section h2 {
    margin-bottom: var(--spacing-md);
    font-size: 1.3rem;
}

.intro ul {
    margin-left: var(--spacing-lg);
}

.intro li {
    margin-bottom: var(--spacing-sm);
}

.stats-grid {
    display: flex;
    gap: var(--spacing-lg);
    justify-content: center;
}

.stat-item {
    text-align: center;
    padding: var(--spacing-lg);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 600;
    color: var(--color-accent);
}

.stat-label {
    color: var(--color-text-secondary);
}

.nav-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: var(--spacing-md);
}

.nav-card {
    display: block;
    padding: var(--spacing-lg);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    text-decoration: none;
    color: inherit;
    transition: all 0.2s;
}

.nav-card:hover {
    border-color: var(--color-accent);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.nav-card h3 {
    color: var(--color-accent);
    margin-bottom: var(--spacing-sm);
}

.nav-card p {
    font-size: 0.9rem;
    color: var(--color-text-secondary);
}

/* Entry Page */
.entry-page {
    padding: var(--spacing-lg);
}

.entry-display {
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: var(--spacing-lg);
}

.entry-header {
    margin-bottom: var(--spacing-lg);
    padding-bottom: var(--spacing-md);
    border-bottom: 1px solid var(--color-border);
}

.entry-headword {
    font-family: var(--font-jp);
    font-size: 2.5rem;
    font-weight: 500;
    line-height: 1.4;
}

.entry-reading {
    font-family: var(--font-jp);
    font-size: 1.2rem;
    color: var(--color-text-secondary);
    margin-top: var(--spacing-sm);
}

.entry-pos {
    font-size: 0.9rem;
    color: var(--color-text-secondary);
    font-style: italic;
    margin-top: var(--spacing-sm);
}

.entry-gloss {
    font-size: 1.1rem;
    margin-top: var(--spacing-sm);
}

/* Definitions */
.definitions {
    margin-top: var(--spacing-lg);
}

.definitions h2 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: var(--spacing-md);
    color: var(--color-text-secondary);
}

.definition-item {
    margin-bottom: var(--spacing-md);
    padding-left: var(--spacing-md);
}

.definition-number {
    font-weight: 600;
    color: var(--color-accent);
}

.definition-gloss {
    font-weight: 500;
}

.definition-explanation {
    color: var(--color-text-secondary);
    margin-top: 0.25rem;
}

/* Examples */
.examples {
    margin-top: var(--spacing-lg);
}

.examples h2 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: var(--spacing-md);
    color: var(--color-text-secondary);
}

.example-item {
    margin-bottom: var(--spacing-md);
    padding: var(--spacing-md);
    background-color: var(--color-bg);
    border-radius: 6px;
}

.example-japanese {
    font-family: var(--font-jp);
    font-size: 1.1rem;
    line-height: 2;
    margin-bottom: 0.25rem;
}

.example-english {
    color: var(--color-text-secondary);
    font-size: 0.95rem;
}

.example-notes {
    color: var(--color-text-secondary);
    font-size: 0.85rem;
    font-style: italic;
    margin-top: 0.25rem;
}

/* Notes */
.entry-notes {
    margin-top: var(--spacing-lg);
    padding: var(--spacing-md);
    background-color: #f0f7ff;
    border-radius: 6px;
    border-left: 3px solid var(--color-accent);
}

.entry-notes h2 {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: var(--spacing-sm);
    color: var(--color-accent);
}

.notes-content p {
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: var(--spacing-sm);
}

.notes-content p:last-child {
    margin-bottom: 0;
}

.notes-content ul {
    margin: var(--spacing-sm) 0;
    padding-left: 1.5rem;
}

.notes-content li {
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 0.25rem;
}

/* Cross-References */
.cross-references {
    margin-top: var(--spacing-lg);
    padding: var(--spacing-md);
    background-color: #f8f9fa;
    border-radius: 6px;
    border-left: 3px solid #6c757d;
}

.cross-references h2 {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: var(--spacing-sm);
    color: #495057;
}

.cross-ref {
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    margin-bottom: 0.4rem;
    font-size: 0.95rem;
    line-height: 1.5;
}

.cross-ref:last-child {
    margin-bottom: 0;
}

.cross-ref-type {
    color: #6c757d;
    min-width: 80px;
    flex-shrink: 0;
}

.cross-ref-link {
    color: var(--color-accent);
    text-decoration: none;
}

.cross-ref-link:hover {
    text-decoration: underline;
}

.cross-ref.pending .cross-ref-pending {
    color: #999;
    font-style: italic;
}

.cross-ref.pending .cross-ref-pending::after {
    content: " (not yet in dictionary)";
    font-size: 0.85em;
    color: #aaa;
}

/* Metadata */
.entry-metadata {
    margin-top: var(--spacing-lg);
    padding-top: var(--spacing-md);
    border-top: 1px solid var(--color-border);
    font-size: 0.85rem;
    color: var(--color-text-secondary);
}

.metadata-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--spacing-md);
    flex-wrap: wrap;
}

.metadata-badges {
    display: flex;
    gap: var(--spacing-sm);
}

.badge {
    padding: 0.2rem 0.5rem;
    background-color: var(--color-bg);
    border-radius: 4px;
    font-size: 0.8rem;
}

.badge.tier {
    background-color: #dbeafe;
    color: #1e40af;
}

.badge.status-verified {
    background-color: #dcfce7;
    color: #166534;
}

.badge.status-reviewed {
    background-color: #fef9c3;
    color: #854d0e;
}

.badge.status-draft {
    background-color: #fee2e2;
    color: #991b1b;
}

.metadata-dates {
    text-align: center;
    flex: 1;
}

.metadata-file {
    font-family: monospace;
    font-size: 0.8rem;
}

/* Search Page */
.search-page h1 {
    text-align: center;
    margin-bottom: var(--spacing-lg);
}

.search-form {
    display: flex;
    gap: var(--spacing-sm);
    margin-bottom: var(--spacing-md);
}

.search-form input {
    flex: 1;
    padding: 0.75rem 1rem;
    font-size: 1.1rem;
    font-family: var(--font-jp);
    border: 2px solid var(--color-border);
    border-radius: 6px;
    outline: none;
}

.search-form input:focus {
    border-color: var(--color-accent);
}

.search-form button {
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 500;
    color: white;
    background-color: var(--color-accent);
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

.search-form button:hover {
    background-color: var(--color-accent-hover);
}

.search-options {
    display: flex;
    gap: var(--spacing-md);
    flex-wrap: wrap;
    margin-bottom: var(--spacing-lg);
}

.search-options label {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    font-size: 0.9rem;
    color: var(--color-text-secondary);
    cursor: pointer;
}

.results-section {
    margin-top: var(--spacing-lg);
}

.results-section h2 {
    margin-bottom: var(--spacing-md);
}

.results-list {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-sm);
}

.result-item {
    display: block;
    padding: var(--spacing-md);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 6px;
    text-decoration: none;
    color: inherit;
    transition: all 0.2s;
}

.result-item:hover {
    border-color: var(--color-accent);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.result-headword {
    font-family: var(--font-jp);
    font-size: 1.3rem;
    font-weight: 500;
    line-height: 2;
}

.result-reading {
    font-family: var(--font-jp);
    color: var(--color-text-secondary);
    font-size: 0.95rem;
}

.result-gloss {
    color: var(--color-text-secondary);
    font-size: 0.95rem;
    margin-top: 0.25rem;
}

.noscript-notice {
    padding: var(--spacing-lg);
    background-color: #fef9c3;
    border: 1px solid #fbbf24;
    border-radius: 6px;
    margin-top: var(--spacing-lg);
}

/* Browse Page */
.browse-page h1 {
    margin-bottom: var(--spacing-sm);
}

.browse-intro {
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-lg);
}

.kana-section {
    margin-bottom: var(--spacing-md);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    overflow: hidden;
}

.kana-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--spacing-md);
    cursor: pointer;
    background-color: var(--color-bg);
    font-weight: 500;
}

.kana-header:hover {
    background-color: var(--color-accent-light);
}

.kana-name {
    font-family: var(--font-jp);
    font-size: 1.1rem;
}

.kana-count {
    font-size: 0.85rem;
    color: var(--color-text-secondary);
}

.kana-entries {
    padding: var(--spacing-sm);
    display: flex;
    flex-direction: column;
}

.browse-entry {
    display: flex;
    gap: var(--spacing-md);
    align-items: baseline;
    padding: var(--spacing-sm) var(--spacing-md);
    border-radius: 4px;
    text-decoration: none;
    color: inherit;
}

.browse-entry:hover {
    background-color: var(--color-bg);
}

.browse-headword {
    font-family: var(--font-jp);
    font-size: 1rem;
    min-width: 120px;
    line-height: 2;
}

.browse-reading {
    font-family: var(--font-jp);
    font-size: 0.85rem;
    color: var(--color-text-secondary);
    min-width: 80px;
}

.browse-gloss {
    font-size: 0.9rem;
    color: var(--color-text-secondary);
    flex: 1;
}

/* Recent Page */
.recent-page h1 {
    margin-bottom: var(--spacing-sm);
}

.recent-intro {
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-lg);
}

.recent-list {
    display: flex;
    flex-direction: column;
}

.recent-item {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 0.5rem 1rem;
    padding: 0.6rem var(--spacing-md);
    border-bottom: 1px solid var(--color-border);
    text-decoration: none;
    color: inherit;
    transition: background-color 0.15s;
}

.recent-item:hover {
    background-color: var(--color-bg);
}

.recent-item:last-child {
    border-bottom: none;
}

.recent-headword {
    font-family: var(--font-jp);
    font-size: 1.1rem;
    font-weight: 500;
    line-height: 2;
}

.recent-gloss {
    font-size: 1rem;
    color: var(--color-text);
    flex: 1;
    min-width: 200px;
}

.recent-status {
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}

.recent-status.new {
    color: var(--color-accent);
}

.recent-status.revised {
    color: #8b5cf6;
}

.recent-date {
    font-size: 0.85rem;
    color: var(--color-text-secondary);
}

/* Random Page */
.random-page h1 {
    text-align: center;
    margin-bottom: var(--spacing-sm);
}

.random-intro {
    text-align: center;
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-lg);
}

.random-words {
    font-family: var(--font-jp);
    font-size: 1.2rem;
    line-height: 2.8;
    padding: var(--spacing-lg);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    overflow: hidden;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.random-word {
    display: inline-block;
    text-decoration: none;
    color: inherit;
    padding: 0.1rem 0.3rem;
    margin-right: 0.5em;
    margin-bottom: 0.2em;
    border-radius: 4px;
    white-space: nowrap;
    transition: background-color 0.15s;
}

.random-word:hover {
    background-color: var(--color-accent-light);
}

/* Pending Page */
.pending-page h1 {
    margin-bottom: var(--spacing-sm);
}

.pending-intro {
    color: var(--color-text-secondary);
    margin-bottom: var(--spacing-lg);
}

.pending-list {
    display: flex;
    flex-direction: column;
    font-family: var(--font-jp);
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    overflow: hidden;
}

.pending-item {
    display: flex;
    gap: 1.5rem;
    padding: 0.5rem var(--spacing-md);
    border-bottom: 1px solid var(--color-border);
    font-size: 1rem;
    line-height: 1.8;
}

.pending-item:last-child {
    border-bottom: none;
}

.pending-item:nth-child(odd) {
    background-color: rgba(0, 0, 0, 0.02);
}

.pending-word {
    font-weight: 500;
    min-width: 100px;
}

.pending-reading {
    color: var(--color-text-secondary);
    min-width: 100px;
}

.pending-notes {
    color: var(--color-text);
    flex: 1;
}

/* Ruby/Furigana Styling */
ruby {
    ruby-align: center;
}

ruby rt {
    font-size: 0.55em;
    font-family: var(--font-jp);
    color: var(--color-accent);
    font-weight: 400;
}

.entry-headword ruby rt {
    font-size: 0.45em;
}

/* Footer */
footer {
    text-align: center;
    padding: var(--spacing-lg);
    border-top: 1px solid var(--color-border);
    margin-top: var(--spacing-xl);
    color: var(--color-text-secondary);
    font-size: 0.85rem;
}

footer a {
    color: var(--color-text-secondary);
    text-decoration: none;
}

footer a:hover {
    color: var(--color-accent);
}

/* Responsive */
@media (max-width: 600px) {
    .nav-header {
        flex-wrap: wrap;
        justify-content: center;
        gap: var(--spacing-sm);
    }

    .nav-links {
        width: 100%;
        justify-content: center;
        order: 2;
    }

    .nav-link {
        padding: var(--spacing-sm);
        font-size: 0.9rem;
    }

    .furigana-toggle-btn {
        order: 1;
    }

    .furigana-label {
        display: none;
    }

    .entry-headword {
        font-size: 2rem;
    }

    .search-form {
        flex-direction: column;
    }

    .search-form button {
        width: 100%;
    }

    .browse-entry {
        flex-direction: column;
        gap: 0.25rem;
    }

    .browse-headword,
    .browse-reading {
        min-width: auto;
    }

    .metadata-row {
        flex-direction: column;
        align-items: flex-start;
    }

    .metadata-dates {
        text-align: left;
    }
}
'''


def load_entry(file_path: Path) -> dict:
    """Load a single entry file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_recent_entries(entries: list, limit: int = 250) -> list:
    """Build a list of recently added or modified entries."""
    def get_modified_date(entry):
        try:
            return datetime.fromisoformat(entry['metadata']['modified'].replace('Z', '+00:00'))
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
            print(f"  WARNING: Duplicate entry ID '{entry_id}' found!")
            print(f"    First occurrence: {seen_ids[entry_id]}")
            print(f"    Second occurrence: {e.get('_source_file', 'unknown')}")
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
    preserved_dirs = {'flat'}  # Directories to preserve

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

    # Use temp_dir for all build output (reassign docs_dir for the build)
    original_docs_dir = docs_dir
    docs_dir = temp_dir

    # Entry directories will be created dynamically with prefix subdirectories
    entries_output_dir = docs_dir / 'entries'

    print(f"  Created {docs_dir}")

    # Step 3: Generate entry pages
    print("\n[3/6] Generating entry pages...")
    for entry in entries:
        folder = get_kana_folder(entry['reading'])
        prefix = get_entry_prefix(entry['id'])
        entry_html = generate_entry_html(entry, entries_dict, readings_to_entries)
        # Create directory structure: entries/{kana}/{prefix}/
        output_dir = entries_output_dir / folder / prefix
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{entry['id']}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(entry_html)
    print(f"  Generated {len(entries)} entry pages")

    # Step 4: Generate navigation pages
    print("\n[4/6] Generating navigation pages...")

    # Index page
    with open(docs_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(generate_index_page(len(entries)))

    # Search page
    with open(docs_dir / 'search.html', 'w', encoding='utf-8') as f:
        f.write(generate_search_page())

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

    print("  Generated index.html, search.html, browse.html, recent.html, random.html, pending.html")

    # Step 5: Generate search index and JavaScript
    print("\n[5/6] Generating search index...")
    with open(docs_dir / 'search-index.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_index(entries))

    with open(docs_dir / 'search.js', 'w', encoding='utf-8') as f:
        f.write(generate_search_js())

    print("  Generated search-index.js, search.js")

    # Step 6: Generate stylesheet
    print("\n[6/6] Generating stylesheet...")
    with open(docs_dir / 'styles.css', 'w', encoding='utf-8') as f:
        f.write(generate_stylesheet())
    print("  Generated styles.css")

    # Atomic swap: replace original docs/ with newly built temp_dir
    print("\n[Swap] Atomically replacing output directory...")
    try:
        # Move original docs/ to backup (if it exists)
        if original_docs_dir.exists():
            original_docs_dir.rename(backup_dir)

        # Move temp build to docs/
        docs_dir.rename(original_docs_dir)

        # Remove backup after successful swap
        if backup_dir.exists():
            shutil.rmtree(backup_dir)

        print("  Swap complete")
    except OSError as e:
        print(f"  ERROR: Failed to swap directories: {e}")
        print("  Build output remains in: {temp_dir}")
        # Try to restore backup if swap failed midway
        if backup_dir.exists() and not original_docs_dir.exists():
            backup_dir.rename(original_docs_dir)
        return 1

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
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    sys.exit(build_flat(project_root))


if __name__ == '__main__':
    main()
