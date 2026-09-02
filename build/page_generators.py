#!/usr/bin/env python3
"""
Navigation page generators for je-dict-1 dictionary.

Extracted from build_flat.py to keep the build script manageable.
Generates HTML content for navigation pages: index, advanced, browse,
recent, random, and pending.
"""

import html
import random
from collections import defaultdict
from datetime import datetime, timezone

from path_utils import get_directory_range
from japanese_utils import KANA_ROWS, strip_furigana, is_kanji, romaji_to_hiragana, romaji_to_katakana
from html_utils import (
    generate_nav_header,
    generate_furigana_script,
    generate_examples_script,
    generate_wordlinks_script,
    generate_goatcounter_script,
    generate_header_search_script,
    semantic_tag_slug,
)
from entry_renderer import (
    process_furigana,
    format_jst_datetime,
    generate_html_head,
    JST,
)


def generate_header_search_redirect_script() -> str:
    """Header search script for pages at the docs root (redirects to index.html?q=...).

    Kept under this name because article_renderer imports it; the script itself
    (no query-type heuristics, no index load) lives in html_utils.
    """
    return generate_header_search_script('')


def generate_index_page(entry_count: int, tier_counts: dict, example_count: int, build_time_jst: str) -> str:
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
            <input type="text" id="search-input" placeholder="Search Japanese, romaji, or English (e.g. 食べた, taberu, eat)" autocomplete="off">
            <button type="button" id="search-button">Search</button>
        </div>

        <div class="search-options">
            <label><input type="radio" name="search-type" value="auto" checked> Auto-detect</label>
            <label><input type="radio" name="search-type" value="japanese"> Japanese</label>
            <label><input type="radio" name="search-type" value="romaji"> Romaji</label>
            <label><input type="radio" name="search-type" value="english"> English</label>
        </div>

        <div class="home-nav-links">
            <a href="browse.html">Browse</a>
            <a href="kanji.html">Kanji</a>
            <a href="lists/index.html">Lists</a>
            <a href="articles/index.html">Articles</a>
            <a href="recent.html">Recent</a>
            <a href="advanced.html">Advanced</a>
        </div>

        <div id="results-section" class="results-section" style="display: none;">
            <h2 id="results-heading">Results</h2>
            <div id="results-list" class="results-list"></div>
            <button type="button" id="show-more-button" class="show-more-btn" style="display: none;">Show more</button>
        </div>

        <noscript>
            <div class="noscript-notice">
                <p>JavaScript is required for the search feature. You can still <a href="browse.html">browse entries</a> by kana row.</p>
            </div>
        </noscript>
    </section>

    <section class="intro" id="intro-section">
        <p>The TKG Japanese-English Learner's Dictionary (TKGJE) is an explanatory dictionary designed for learners of Japanese as a second language. It currently contains {entry_count:,} entries, including {basic_count:,} basic words for beginners and {core_count:,} core vocabulary for intermediate learners, as well as {example_count:,} natural example sentences optimized for learning. Each entry includes explanatory definitions; usage notes covering grammar, register, common patterns, and related expressions; and furigana readings for all kanji. The dictionary is under active development.</p>
    </section>
</main>

<script src="search-index.js"></script>
<script src="search.js"></script>

<footer>
    <p>TKG Japanese-English Learner's Dictionary</p>
    <p>Last update: {build_time_jst}</p>
</footer>
{generate_furigana_script()}
{generate_examples_script()}
{generate_wordlinks_script()}
{generate_goatcounter_script()}
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


def generate_tag_search_section(curator_tools: bool = False) -> str:
    """Generate the tag-based search section HTML.

    The public advanced page has the tag filter and the combined query; the
    curator page (curator.html, unlinked) adds tag statistics, missing-tag
    detection and CSV/JSON/ID export.
    """
    curator_modes = ''
    curator_panels = ''
    export_buttons = ''
    if curator_tools:
        curator_modes = '''
            <button class="mode-btn" data-mode="stats">Tag Statistics</button>
            <button class="mode-btn" data-mode="missing">Find Missing Tags</button>'''
        curator_panels = '''
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
'''
        export_buttons = '''
                <div class="tag-results-export">
                    <button type="button" id="export-csv">Export CSV</button>
                    <button type="button" id="export-json">Export JSON</button>
                    <button type="button" id="copy-ids">Copy IDs</button>
                </div>'''

    return f'''
    <!-- Tag-Based Search Section -->
    <section class="tag-search-section">
        <h2>Tag-Based Search</h2>

        <div class="tag-search-modes">
            <button class="mode-btn active" data-mode="filter">Filter by Tags</button>{curator_modes}
            <button class="mode-btn" data-mode="combined">Combined Query</button>
        </div>

        <!-- Filter Mode Panel -->
        <div id="filter-panel" class="tag-filter-panel">
            <div class="filter-actions">
                <button type="button" id="apply-filters" class="primary">Apply Filters</button>
                <button type="button" id="clear-filters">Clear All</button>
                <label style="display: inline-flex; align-items: center; gap: 0.25rem;">
                    <input type="checkbox" id="filter-and-mode" checked> Match all selected categories (AND)
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

{curator_panels}
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
                <span class="tag-results-count" id="tag-results-count"></span>{export_buttons}
            </div>
            <div id="tag-results-list" class="tag-results-list"></div>
            <div id="tag-pagination" class="pagination"></div>
        </div>
    </section>
'''


def generate_advanced_page(curator_tools: bool = False) -> str:
    """Generate advanced.html (public tag search) or curator.html (curator_tools=True).

    Both load the compact search index plus search-tags.js; the curator page is
    unlinked and marked noindex.
    """
    if curator_tools:
        title = 'Curator Tools'
        intro = ('Tag statistics, missing-tag detection and export for dictionary maintenance. '
                 'This page is not linked from the public navigation.')
        robots = '\n    <meta name="robots" content="noindex, nofollow">'
    else:
        title = 'Advanced Search'
        intro = ('Filter entries by vocabulary tier, part of speech, transitivity, formality and '
                 'other tags, or combine conditions in a query.')
        robots = ''

    # Custom head with tag search styles
    custom_head = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="TKG Japanese-English Learner's Dictionary - {title}">{robots}
    <title>{title} - TKG Japanese-English Learner's Dictionary</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23FFEA00'/><circle cx='50' cy='50' r='30' fill='%23FFC107'/><circle cx='42' cy='42' r='8' fill='white' opacity='0.4'/></svg>">
{generate_tag_search_styles()}
</head>'''

    return f'''{custom_head}
<body>
{generate_nav_header()}
<main class="search-page">
    <h1>{title}</h1>
    <p class="browse-intro">{intro}</p>

{generate_tag_search_section(curator_tools)}

    <noscript>
        <div class="noscript-notice">
            <p>JavaScript is required for the advanced search feature. You can still <a href="browse.html">browse entries</a> by kana row.</p>
        </div>
    </noscript>
</main>

<script src="search-index.js"></script>
<script src="search-tags.js"></script>
<script src="tag-search.js"></script>

<footer>
    <p><a href="index.html">TKG Japanese-English Learner's Dictionary</a></p>
</footer>
{generate_header_search_redirect_script()}
{generate_furigana_script()}
{generate_examples_script()}
{generate_wordlinks_script()}
{generate_goatcounter_script()}
</body>
</html>'''


def get_kana_folder_for_display(reading: str) -> str:
    """Get the kana row name for display purposes (browsing)."""
    if not reading:
        return 'a'
    first_char = reading[0]
    for row in KANA_ROWS:
        if first_char in row['kana']:
            return row['folder']
    return 'a'


def _page_footer_scripts(relative_path: str = '') -> str:
    """Footer, header-search redirect, toggle scripts and closing tags shared by list pages."""
    return '\n'.join([
        f'''
        <footer>
            <p><a href="{relative_path}index.html">TKG Japanese-English Learner's Dictionary</a></p>
        </footer>
    ''',
        generate_header_search_script(relative_path),
        generate_furigana_script(),
        generate_examples_script(),
        generate_wordlinks_script(),
        generate_goatcounter_script(),
        '</body>',
        '</html>',
    ])


def _entry_row_html(entry: dict, relative_path: str = '') -> str:
    """One headword / reading / gloss row linking to an entry (browse, lists, tag pages)."""
    dir_range = get_directory_range(entry['id'])
    return (
        f'<a href="{relative_path}entries/{dir_range}/{entry["id"]}.html" class="browse-entry">'
        f'<span class="browse-headword" lang="ja">{process_furigana(entry["headword"])}</span>'
        f'<span class="browse-reading" lang="ja">{html.escape(entry["reading"])}</span>'
        f'<span class="browse-gloss">{html.escape(entry.get("gloss", ""))}</span>'
        f'</a>'
    )


def group_entries_by_kana_row(entries: list) -> list:
    """Return [(row, entries sorted by reading), ...] for the non-empty KANA_ROWS."""
    grouped = {row['folder']: [] for row in KANA_ROWS}
    for entry in entries:
        reading = entry.get('reading', '')
        if not reading:
            continue
        for row in KANA_ROWS:
            if reading[0] in row['kana']:
                grouped[row['folder']].append(entry)
                break
    result = []
    for row in KANA_ROWS:
        row_entries = sorted(grouped[row['folder']], key=lambda e: e['reading'])
        if row_entries:
            result.append((row, row_entries))
    return result


def _kana_sections_html(entries: list, relative_path: str) -> str:
    """Entries grouped under one heading per kana row, with a jump bar."""
    grouped = group_entries_by_kana_row(entries)
    jump = ''.join(f'<a href="#row-{row["folder"]}">{row["name"]}</a>' for row, _ in grouped)
    parts = [f'<nav class="kana-jump" lang="ja" aria-label="Kana rows">{jump}</nav>']
    for row, row_entries in grouped:
        parts.append(
            f'<section class="kana-section" id="row-{row["folder"]}">'
            f'<h2 class="kana-row-heading"><span class="kana-name" lang="ja">{row["name"]}</span>'
            f'<span class="kana-count">{len(row_entries):,} entries</span></h2>'
            f'<div class="kana-entries">'
        )
        parts.extend(_entry_row_html(entry, relative_path) for entry in row_entries)
        parts.append('</div></section>')
    return '\n'.join(parts)


def generate_browse_page(entries: list, entries_dict: dict) -> str:
    """Generate browse.html: an index of kana rows, each linking to browse/<row>.html."""
    grouped = group_entries_by_kana_row(entries)
    html_parts = [
        generate_html_head("Browse"),
        '<body>',
        generate_nav_header(),
        '<main class="browse-page">',
        '<h1>Browse Entries</h1>',
        f'<p class="browse-intro">All {len(entries):,} entries, by the first kana of the reading. Choose a row.</p>',
        '<div class="browse-row-grid">',
    ]
    for row, row_entries in grouped:
        html_parts.append(
            f'<a href="browse/{row["folder"]}.html" class="browse-row-card">'
            f'<span class="browse-row-name" lang="ja">{row["name"]}</span>'
            f'<span class="browse-row-kana" lang="ja">{" ".join(row["kana"])}</span>'
            f'<span class="browse-row-count">{len(row_entries):,} entries</span>'
            f'</a>'
        )
    html_parts.append('</div>')
    html_parts.append('</main>')
    html_parts.append(_page_footer_scripts(''))
    return '\n'.join(html_parts)


def generate_browse_row_page(row: dict, row_entries: list) -> str:
    """Generate browse/<folder>.html: every entry whose reading starts in one kana row,
    sub-grouped by first kana with jump links."""
    relative_path = '../'
    by_kana = defaultdict(list)
    for entry in row_entries:
        by_kana[entry['reading'][0]].append(entry)
    kana_order = [k for k in row['kana'] if k in by_kana]

    jump = ''.join(f'<a href="#kana-{i}">{k}</a>' for i, k in enumerate(kana_order))
    html_parts = [
        generate_html_head(f"Browse {row['name']}", relative_path),
        '<body>',
        generate_nav_header(relative_path),
        '<main class="browse-page">',
        f'<h1><span lang="ja">{row["name"]}</span> — {len(row_entries):,} entries</h1>',
        '<p class="browse-intro"><a href="../browse.html">← All kana rows</a></p>',
        f'<nav class="kana-jump" lang="ja" aria-label="First kana">{jump}</nav>',
    ]
    for i, kana in enumerate(kana_order):
        kana_entries = by_kana[kana]
        html_parts.append(
            f'<section class="kana-section" id="kana-{i}">'
            f'<h2 class="kana-row-heading"><span class="kana-name" lang="ja">{kana}</span>'
            f'<span class="kana-count">{len(kana_entries):,} entries</span></h2>'
            f'<div class="kana-entries">'
        )
        html_parts.extend(_entry_row_html(entry, relative_path) for entry in kana_entries)
        html_parts.append('</div></section>')
    html_parts.append('</main>')
    html_parts.append(_page_footer_scripts(relative_path))
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
    html_parts.append(generate_goatcounter_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_random_page(entries: list, sample_size: int = 300) -> str:
    """Generate random.html with a random sample of headwords.

    The sample is drawn at build time (seeded by the build date, so rebuilds on
    the same day give the same page); the page shuffles it on every load.
    """
    rng = random.Random(datetime.now(JST).strftime('%Y-%m-%d'))
    sample = rng.sample(entries, min(sample_size, len(entries)))

    html_parts = [
        generate_html_head("Random"),
        '<body>',
        generate_nav_header(),
        '<main class="random-page">',
        '<h1>Random Word Cloud</h1>',
        f'<p class="random-intro">A random sample of {len(sample)} of the dictionary\'s {len(entries):,} entries, '
        'redrawn each time the site is rebuilt. Click any word to view its entry; reload the page for a new arrangement.</p>',
        '<div class="random-words" id="random-words" lang="ja">',
    ]

    for entry in sample:
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
    html_parts.append(generate_goatcounter_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_pending_page(candidates: list) -> str:
    """Generate the pending.html page showing candidate words."""
    html_parts = [
        generate_html_head("Pending", noindex=True),
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
    html_parts.append(generate_goatcounter_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


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


# Kanji index groups: (minimum headword count, label)
KANJI_COUNT_BUCKETS = [
    (100, '100 or more headwords'),
    (50, '50–99 headwords'),
    (20, '20–49 headwords'),
    (10, '10–19 headwords'),
    (5, '5–9 headwords'),
    (2, '2–4 headwords'),
    (1, '1 headword'),
]


def kanji_readings_kana(value: str, convert) -> list:
    """'kou, gou' -> ['コウ', 'ゴウ'] with the given romaji converter; 'none' -> []."""
    if not value or value == 'none':
        return []
    return [convert(part.strip()) for part in value.split(',') if part.strip()]


def generate_kanji_list_page(entries: list, kanji_list: dict) -> str:
    """Generate kanji.html: every headword kanji with its readings and meaning,
    grouped by how many headwords contain it, with a client-side filter box.

    Args:
        entries: List of all entry dicts (with 'headword' fields).
        kanji_list: The kanji_list.json data (with 'kanji' mapping; each record
            has kanji_id, onyomi, kunyomi, gloss in romaji/English).
    """
    # Count how many headwords contain each kanji (each kanji once per headword)
    kanji_counts = defaultdict(int)
    for entry in entries:
        plain = strip_furigana(entry['headword'])
        seen = set()
        for ch in plain:
            if is_kanji(ch) and ch not in seen:
                seen.add(ch)
                kanji_counts[ch] += 1

    # Only kanji in kanji_list have index pages
    kanji_map = kanji_list.get('kanji', {})
    kanji_with_counts = []
    for kanji_char, count in kanji_counts.items():
        if kanji_char in kanji_map:
            kanji_with_counts.append((kanji_char, count, kanji_map[kanji_char]))
    kanji_with_counts.sort(key=lambda x: (-x[1], x[0]))

    def card_html(kanji_char: str, count: int, info: dict) -> str:
        on_kana = kanji_readings_kana(info.get('onyomi'), romaji_to_katakana)
        kun_kana = kanji_readings_kana(info.get('kunyomi'), romaji_to_hiragana)
        readings = '・'.join(on_kana + kun_kana) or '—'
        gloss = info.get('gloss', '')
        search_text = ' '.join([kanji_char, *on_kana, *kun_kana,
                                info.get('onyomi', ''), info.get('kunyomi', ''), gloss]).lower()
        return (
            f'<a href="kanji/{html.escape(info["kanji_id"])}.html" class="kanji-card" '
            f'data-search="{html.escape(search_text)}">'
            f'<span class="kanji-card-char" lang="ja">{html.escape(kanji_char)}</span>'
            f'<span class="kanji-card-readings" lang="ja">{html.escape(readings)}</span>'
            f'<span class="kanji-card-gloss">{html.escape(gloss)}</span>'
            f'<span class="kanji-card-count">{count}</span>'
            f'</a>'
        )

    html_parts = [
        generate_html_head("Kanji Index"),
        '<body>',
        generate_nav_header(),
        '<main class="kanji-list-page">',
        '<h1>Kanji Index</h1>',
        f'<p class="kanji-list-intro">{len(kanji_with_counts):,} kanji used in headwords, grouped by how many '
        'headwords contain each. Cards show the on (katakana) and kun (hiragana) readings and a core meaning; '
        'the number in the corner is the headword count. Click a kanji for the list of words.</p>',
        '<div class="kanji-filter">'
        '<input type="search" id="kanji-filter" placeholder="Filter by kanji, reading (kana or romaji), or meaning" '
        'autocomplete="off" aria-label="Filter kanji">'
        '<span id="kanji-filter-count" class="kanji-filter-count"></span></div>',
    ]

    upper = None  # exclusive upper bound of the current bucket
    for minimum, label in KANJI_COUNT_BUCKETS:
        group = [(ch, count, info) for ch, count, info in kanji_with_counts
                 if count >= minimum and (upper is None or count < upper)]
        upper = minimum
        if not group:
            continue
        html_parts.append(f'<section class="kanji-group"><h2>{label} '
                          f'<span class="kanji-group-count">({len(group):,} kanji)</span></h2>'
                          '<div class="kanji-grid">')
        html_parts.extend(card_html(ch, count, info) for ch, count, info in group)
        html_parts.append('</div></section>')

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
    html_parts.append('''<script>
(function() {
    var input = document.getElementById('kanji-filter');
    if (!input) return;
    var cards = Array.prototype.slice.call(document.querySelectorAll('.kanji-card'));
    var groups = Array.prototype.slice.call(document.querySelectorAll('.kanji-group'));
    var countEl = document.getElementById('kanji-filter-count');
    function apply() {
        var q = input.value.trim().toLowerCase();
        var shown = 0;
        cards.forEach(function(card) {
            var match = !q || card.getAttribute('data-search').indexOf(q) !== -1;
            card.hidden = !match;
            if (match) shown++;
        });
        groups.forEach(function(group) {
            group.hidden = !group.querySelector('.kanji-card:not([hidden])');
        });
        if (countEl) countEl.textContent = q ? shown + ' of ' + cards.length + ' kanji' : '';
    }
    input.addEventListener('input', apply);
})();
</script>''')
    html_parts.append(generate_goatcounter_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


# ── Study lists (lists/) and semantic-tag lists (tags/) ─────────────────

LIST_TIERS = {
    'basic': ('Basic vocabulary',
              'Foundational words for beginners — the vocabulary every learner meets first.'),
    'core': ('Core vocabulary',
             'Words for essential everyday adult communication — the layer after the basic tier.'),
}


def collect_semantic_tag_pages(entries: list) -> dict:
    """Group entries by semantic tag for the tags/<slug>.html pages.

    Returns {slug: {'label': most common spelling, 'entries': [...]}} sorted by
    slug. Variant spellings ('daily life', 'daily_life') share one slug; the
    catch-all tag 'general' is skipped.
    """
    pages = {}
    spellings = defaultdict(lambda: defaultdict(int))
    for entry in entries:
        seen = set()
        for tag in entry.get('metadata', {}).get('tags', {}).get('semantic') or []:
            slug = semantic_tag_slug(tag)
            if not slug or slug == 'general' or slug in seen:
                continue
            seen.add(slug)
            pages.setdefault(slug, []).append(entry)
            spellings[slug][tag] += 1
    result = {}
    for slug in sorted(pages):
        label = max(spellings[slug].items(), key=lambda kv: kv[1])[0]
        result[slug] = {'label': label, 'entries': sorted(pages[slug], key=lambda e: e['reading'])}
    return result


def generate_list_page(tier: str, entries: list) -> str:
    """Generate lists/<tier>.html: every entry of one vocabulary tier, in kana order."""
    relative_path = '../'
    title, blurb = LIST_TIERS[tier]
    html_parts = [
        generate_html_head(title, relative_path, f'{title} — {blurb}'),
        '<body>',
        generate_nav_header(relative_path),
        '<main class="browse-page list-page">',
        f'<h1>{title}</h1>',
        f'<p class="browse-intro">{blurb} {len(entries):,} entries in kana order. '
        '<a href="index.html">All lists</a>.</p>',
        _kana_sections_html(entries, relative_path),
        '</main>',
        _page_footer_scripts(relative_path),
    ]
    return '\n'.join(html_parts)


def generate_tag_list_page(slug: str, label: str, entries: list) -> str:
    """Generate tags/<slug>.html: entries carrying one semantic tag, in kana order."""
    relative_path = '../'
    title = f'Words tagged “{label}”'
    html_parts = [
        generate_html_head(title, relative_path,
                           f'{len(entries)} dictionary entries with the semantic tag {label}'),
        '<body>',
        generate_nav_header(relative_path),
        '<main class="browse-page list-page">',
        f'<h1>{html.escape(title)}</h1>',
        f'<p class="browse-intro">{len(entries):,} entries in kana order. '
        '<a href="../lists/index.html">All lists</a>.</p>',
        _kana_sections_html(entries, relative_path),
        '</main>',
        _page_footer_scripts(relative_path),
    ]
    return '\n'.join(html_parts)


def generate_lists_index_page(tier_counts: dict, tag_pages: dict) -> str:
    """Generate lists/index.html: the study lists by tier plus the semantic-tag lists."""
    relative_path = '../'
    html_parts = [
        generate_html_head("Study Lists", relative_path,
                           "Vocabulary study lists by tier and by topic — TKG Japanese-English Learner's Dictionary"),
        '<body>',
        generate_nav_header(relative_path),
        '<main class="browse-page list-page">',
        '<h1>Study Lists</h1>',
        '<p class="browse-intro">Vocabulary lists by learning tier, and by topic (semantic tag). '
        'Each list shows the headword with furigana, its reading and a short gloss, linked to the full entry.</p>',
        '<div class="list-card-grid">',
    ]
    for tier, (title, blurb) in LIST_TIERS.items():
        html_parts.append(
            f'<a href="{tier}.html" class="list-card">'
            f'<span class="list-card-title">{title}</span>'
            f'<span class="list-card-desc">{blurb} {tier_counts.get(tier, 0):,} entries.</span>'
            f'</a>'
        )
    html_parts.append('</div>')

    if tag_pages:
        html_parts.append(f'<h2>By topic ({len(tag_pages):,} tags)</h2>')
        html_parts.append('<div class="tag-cloud">')
        for slug, info in sorted(tag_pages.items(), key=lambda kv: kv[1]['label'].lower()):
            html_parts.append(
                f'<a href="../tags/{slug}.html">{html.escape(info["label"])}'
                f'<span class="tag-count">{len(info["entries"]):,}</span></a>'
            )
        html_parts.append('</div>')

    html_parts.append('</main>')
    html_parts.append(_page_footer_scripts(relative_path))
    return '\n'.join(html_parts)


