"""
Shared HTML generation utilities for je-dict-1 build scripts.

This module centralizes HTML generation functions that were previously
duplicated between build_flat.py and build_kanji_html.py.
"""

import html
import re
from typing import Optional

from constants import LINK_OPEN, LINK_CLOSE, LINK_ARROW, LINK_COLON, NOENTRY


# A brace group with no pipe, e.g. `{カタカナ}` or `{...}`. These are stray
# wrappers in source text (no reading attached); render them as the bare
# content rather than as literal braces.
NOPIPE_BRACE_PATTERN = re.compile(r'\{([^{}|]*)\}')


def semantic_tag_slug(tag: str) -> str:
    """File-name slug for a semantic tag: lower-case, [a-z0-9-] only.

    'daily-life', 'daily life' and 'daily_life' all map to 'daily-life', so
    variant spellings share one list page. Returns '' if nothing usable remains.
    """
    slug = re.sub(r'[^a-z0-9]+', '-', (tag or '').lower()).strip('-')
    return slug


def unwrap_plain_braces(text: str) -> str:
    """Replace `{X}` (no pipe) with `X`. Furigana `{kanji|reading}` is untouched."""
    if not text or '{' not in text:
        return text
    return NOPIPE_BRACE_PATTERN.sub(r'\1', text)


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
            parts.append(html.escape(unwrap_plain_braces(text[last_end:match.start()])))
        # Add the ruby element
        parts.append(replace_furigana(match))
        last_end = match.end()
    # Add any remaining text
    if last_end < len(text):
        parts.append(html.escape(unwrap_plain_braces(text[last_end:])))

    return ''.join(parts)


def plain_japanese_text(text: str, furigana_pattern: re.Pattern) -> str:
    """Reduce marked-up Japanese to plain text (for speech synthesis).

    Inline word links ⟦surface→base：id⟧ become their surface form,
    furigana {漢字|かんじ} becomes 漢字, and stray `{X}` wrappers become X.
    """
    if not text:
        return ''

    def link_surface(match):
        info = LINK_INFO_PATTERN.match(match.group(1))
        return info.group(1) if info else match.group(1)

    text = LINK_BLOCK_PATTERN.sub(link_surface, text)
    text = furigana_pattern.sub(r'\1', text)
    return unwrap_plain_braces(text)


def generate_nav_header(relative_path: str = '', show_all_links: bool = True) -> str:
    """
    Generate navigation header HTML.

    Args:
        relative_path: Path prefix to reach the root docs directory
        show_all_links: Retained for compatibility; every page now shows the
            full navigation (Home · Browse · Kanji · Lists · Articles · Recent ·
            Random · About). Curator pages (pending, curator) are reachable by
            URL only.
    """
    # Determine the base path to the flat root
    base = relative_path if relative_path else ''

    # Home icon SVG (replaces "Home" text)
    home_icon = '''<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' width='2em' height='2em' style='vertical-align:middle;margin-right:0.25em;'><circle cx='50' cy='50' r='50' fill='#FFEA00'/><circle cx='50' cy='50' r='30' fill='#FFC107'/><circle cx='42' cy='42' r='8' fill='white' opacity='0.4'/></svg>'''

    nav_links = f'''
        <a href="{base}index.html" class="nav-link nav-home" title="Home" aria-label="Home">{home_icon}</a>
        <a href="{base}browse.html" class="nav-link">Browse</a>
        <a href="{base}kanji.html" class="nav-link">Kanji</a>
        <a href="{base}lists/index.html" class="nav-link">Lists</a>
        <a href="{base}articles/index.html" class="nav-link">Articles</a>
        <a href="{base}recent.html" class="nav-link">Recent</a>
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
        <button id="wordlinks-toggle" class="toggle-btn wordlinks-toggle-btn active" type="button" aria-pressed="true" title="Toggle word links (click words to see their entries)">
            <span class="toggle-icon">🔗</span>
            <span class="toggle-label">Links</span>
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
    """Generate the header search JavaScript for pages other than index.html.

    The header box does not search locally: it only redirects to index.html
    with the query, and search.js there loads the index and auto-detects the
    query type. (No search-index.js is loaded on these pages.)
    """
    base = relative_path if relative_path else ''
    return f'''<script>
(function() {{
    'use strict';

    var searchInput = document.getElementById('header-search-input');
    var searchButton = document.getElementById('header-search-button');

    if (!searchInput || !searchButton) return;

    function performSearch() {{
        var query = searchInput.value.trim();
        if (!query) return;

        // Redirect to index.html; search.js there auto-detects the query type
        window.location.href = '{base}index.html?q=' + encodeURIComponent(query);
    }}

    searchButton.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', function(e) {{
        if (e.key === 'Enter') performSearch();
    }});
}})();
</script>'''


# Regex patterns for word link parsing
# Link block pattern: matches ⟦...⟧
LINK_BLOCK_PATTERN = re.compile(r'⟦([^⟧]+)⟧')
# Link info pattern: matches surface→baseform：entry_id
LINK_INFO_PATTERN = re.compile(r'^(.+?)→(.+?)：(.+)$')


def process_word_links(
    text: str,
    entries_dict: dict,
    relative_path: str,
    furigana_pattern: re.Pattern
) -> str:
    """
    Process word link markup in text and generate HTML.

    Parses the format: ⟦surface_form→baseform：entry_id⟧
    - If entry_id exists in entries_dict, generates a link
    - If entry_id is 'noentry' or doesn't exist, generates plain text
    - Furigana in surface_form is processed to ruby tags

    Args:
        text: Text containing word link markup
        entries_dict: Dict mapping entry IDs to entry data
        relative_path: Path prefix to reach the flat root (e.g., '../../')
        furigana_pattern: Compiled regex for furigana notation

    Returns:
        HTML string with word links processed
    """
    if not text:
        return ''

    def process_surface_furigana(surface: str) -> str:
        """Process furigana in surface form to ruby tags (also unwraps `{X}`)."""
        return process_furigana(surface, furigana_pattern, True)

    def replace_link_block(match):
        """Replace a single ⟦...⟧ block with HTML."""
        content = match.group(1)

        # Parse the link info
        info_match = LINK_INFO_PATTERN.match(content)
        if not info_match:
            # Invalid format - just return the content with furigana processed
            return process_surface_furigana(content)

        surface = info_match.group(1)
        baseform = info_match.group(2)
        entry_id = info_match.group(3)

        # Process furigana in surface form
        surface_html = process_surface_furigana(surface)

        # Determine if we should create a link
        if entry_id == NOENTRY or entry_id not in entries_dict:
            # No link - just return the surface form
            return surface_html

        # Create link HTML
        # Calculate the path to the entry
        dir_range = f"{(int(entry_id[:5]) // 500) * 500:05d}"
        entry_path = f"{relative_path}entries/{dir_range}/{entry_id}.html"

        return (
            f'<a class="word-link" href="{entry_path}" '
            f'data-baseform="{html.escape(baseform)}">{surface_html}</a>'
        )

    # Process all link blocks
    result = []
    last_end = 0

    for match in LINK_BLOCK_PATTERN.finditer(text):
        # Add text before this link block (with furigana processed)
        if match.start() > last_end:
            before_text = text[last_end:match.start()]
            result.append(process_surface_furigana(before_text))

        # Process the link block
        result.append(replace_link_block(match))
        last_end = match.end()

    # Add remaining text after the last link block
    if last_end < len(text):
        result.append(process_surface_furigana(text[last_end:]))

    return ''.join(result)


def generate_wordlinks_script() -> str:
    """Generate the word links toggle JavaScript."""
    return '''<script>
(function() {
    var btn = document.getElementById('wordlinks-toggle');
    if (!btn) return;

    // Check saved preference - default to shown (toggle ON)
    var hidden = false;
    try { hidden = localStorage.getItem('wordLinksHidden') === 'true'; } catch (e) {}

    function updateState() {
        document.body.classList.toggle('word-links-hidden', hidden);
        btn.setAttribute('aria-pressed', !hidden);
        btn.classList.toggle('active', !hidden);
    }

    // Apply initial state
    updateState();

    // Toggle on click
    btn.addEventListener('click', function() {
        hidden = !hidden;
        try { localStorage.setItem('wordLinksHidden', hidden); } catch (e) {}
        updateState();
    });
})();
</script>'''


def generate_tts_script() -> str:
    """Generate the example-sentence read-aloud script (Web Speech API).

    Each example carries a `button.tts-btn[data-text]`. The buttons stay
    hidden (CSS) unless speechSynthesis exists and a Japanese voice is
    available; voices often load asynchronously, so `voiceschanged` is
    observed too.
    """
    return '''<script>
(function() {
    if (!('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') return;
    var synth = window.speechSynthesis;
    var jaVoice = null;

    function findJaVoice() {
        var voices = synth.getVoices() || [];
        for (var i = 0; i < voices.length; i++) {
            if (/^ja([-_]|$)/i.test(voices[i].lang)) return voices[i];
        }
        return null;
    }

    function enable() {
        jaVoice = findJaVoice();
        if (jaVoice) document.body.classList.add('tts-available');
    }

    enable();
    if (typeof synth.onvoiceschanged !== 'undefined') {
        synth.addEventListener('voiceschanged', enable);
    }

    document.addEventListener('click', function(e) {
        var btn = e.target.closest ? e.target.closest('.tts-btn') : null;
        if (!btn || !btn.dataset.text) return;
        e.preventDefault();
        if (synth.speaking) synth.cancel();
        var u = new SpeechSynthesisUtterance(btn.dataset.text);
        u.lang = 'ja-JP';
        try { if (jaVoice) u.voice = jaVoice; } catch (err) {}
        u.rate = 0.9;
        synth.speak(u);
    });
})();
</script>'''


def generate_goatcounter_script() -> str:
    """Generate the GoatCounter analytics script tag.

    This should be emitted on every built page immediately before </body>.
    """
    return '<script data-goatcounter="https://tkgje.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
