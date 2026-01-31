"""
Shared HTML generation utilities for je-dict-1 build scripts.

This module centralizes HTML generation functions that were previously
duplicated between build_flat.py and build_kanji_html.py.
"""

import html
import re
from typing import Optional


def process_furigana(text: str, furigana_pattern: re.Pattern, show_furigana: bool = True) -> str:
    """
    Convert furigana notation to HTML ruby tags.

    Args:
        text: Text containing furigana notation {kanji|reading}
        furigana_pattern: Compiled regex pattern for furigana
        show_furigana: If True, generate ruby tags. If False, show only kanji.

    Returns:
        HTML string with ruby tags for furigana display
    """
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
    for match in furigana_pattern.finditer(text):
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


def generate_nav_header(relative_path: str = '', show_all_links: bool = True) -> str:
    """
    Generate navigation header HTML.

    Args:
        relative_path: Path prefix to reach the root docs directory
        show_all_links: If True, show all nav links. If False, show only Home, Random, About
    """
    # Determine the base path to the flat root
    base = relative_path if relative_path else ''

    # Build navigation links based on show_all_links parameter
    if show_all_links:
        nav_links = f'''
        <a href="{base}index.html" class="nav-link">Home</a>
        <a href="{base}advanced.html" class="nav-link">Advanced</a>
        <a href="{base}browse.html" class="nav-link">Browse</a>
        <a href="{base}recent.html" class="nav-link">Recent</a>
        <a href="{base}random.html" class="nav-link">Random</a>
        <a href="{base}pending.html" class="nav-link">Pending</a>
        <a href="{base}about.html" class="nav-link">About</a>'''
    else:
        nav_links = f'''
        <a href="{base}index.html" class="nav-link">Home</a>
        <a href="{base}random.html" class="nav-link">Random</a>
        <a href="{base}about.html" class="nav-link">About</a>'''

    # Header search box (shown on all pages)
    header_search = f'''
    <div class="header-search">
        <input type="text" id="header-search-input" class="header-search-input" placeholder="Search..." autocomplete="off">
        <button type="button" id="header-search-button" class="header-search-button" title="Search">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.35-4.35"></path></svg>
        </button>
    </div>'''

    return f'''<header class="nav-header">
    <nav class="nav-links">{nav_links}
    </nav>
    <div class="toggle-buttons">
        {header_search}
        <button id="examples-toggle" class="toggle-btn examples-toggle-btn" type="button" aria-pressed="true" title="Toggle example sentences">
            <span class="toggle-icon">例</span>
            <span class="toggle-label">Examples</span>
        </button>
        <button id="furigana-toggle" class="toggle-btn furigana-toggle-btn" type="button" aria-pressed="false" title="Toggle furigana (reading annotations above kanji)">
            <span class="toggle-icon">振</span>
            <span class="toggle-label">Furigana</span>
        </button>
    </div>
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


def generate_examples_script() -> str:
    """Generate the examples toggle JavaScript."""
    return '''<script>
(function() {
    var btn = document.getElementById('examples-toggle');
    if (!btn) return;

    // Check saved preference - default to showing examples (hidden = false)
    var hidden = localStorage.getItem('examplesHidden') === 'true';

    function updateState() {
        document.body.classList.toggle('examples-hidden', hidden);
        btn.setAttribute('aria-pressed', !hidden);
        btn.classList.toggle('active', !hidden);
    }

    // Apply initial state
    updateState();

    // Toggle on click
    btn.addEventListener('click', function() {
        hidden = !hidden;
        localStorage.setItem('examplesHidden', hidden);
        updateState();
    });
})();
</script>'''


def generate_header_search_script(relative_path: str = '') -> str:
    """Generate the header search JavaScript for entry/kanji pages."""
    base = relative_path if relative_path else ''
    return f'''<script src="{base}search-index.js"></script>
<script>
(function() {{
    'use strict';

    var searchInput = document.getElementById('header-search-input');
    var searchButton = document.getElementById('header-search-button');

    if (!searchInput || !searchButton) return;

    function detectQueryType(query) {{
        if (/[\\u3040-\\u309f\\u30a0-\\u30ff\\u4e00-\\u9faf]/.test(query)) {{
            return 'japanese';
        }}
        if (/^[a-z]+$/i.test(query)) {{
            return query.length <= 10 ? 'romaji' : 'english';
        }}
        return 'english';
    }}

    function performSearch() {{
        var query = searchInput.value.trim();
        if (!query) return;

        // Redirect to index.html with search parameter
        var searchType = detectQueryType(query);
        window.location.href = '{base}index.html?q=' + encodeURIComponent(query) + '&type=' + searchType;
    }}

    searchButton.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {{
        if (e.key === 'Enter') performSearch();
    }});
}})();
</script>'''
