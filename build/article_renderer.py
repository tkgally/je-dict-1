#!/usr/bin/env python3
"""
Article page HTML generation for je-dict-1 dictionary.

Renders article JSON files into HTML pages, including:
- Markdown-to-HTML conversion (with furigana support)
- Related entries sidebar
- Article index page
"""

import html
import json
import re
from pathlib import Path

from japanese_utils import FURIGANA_PATTERN
from html_utils import (
    process_furigana as _process_furigana_base,
    generate_nav_header,
    generate_furigana_script,
    generate_examples_script,
    generate_wordlinks_script,
    generate_goatcounter_script,
)
from entry_renderer import (
    generate_html_head,
    format_jst_datetime,
)
from page_generators import generate_header_search_redirect_script
from path_utils import get_directory_range


def process_furigana(text: str) -> str:
    """Convert furigana notation to HTML ruby tags."""
    return _process_furigana_base(text, FURIGANA_PATTERN)


def markdown_to_html(text: str) -> str:
    """Convert simple markdown to HTML with furigana support.

    Supports:
    - ## headings (h2) and ### headings (h3)
    - **bold** text
    - Markdown tables (| col1 | col2 |)
    - Unordered lists (- item)
    - Ordered lists (1. item)
    - Blank-line-separated paragraphs
    - {kanji|reading} furigana notation
    """
    lines = text.split('\n')
    result = []
    in_list = False
    in_ol = False
    in_table = False
    table_has_header = False

    def close_list():
        nonlocal in_list, in_ol
        if in_list:
            result.append('</ul>')
            in_list = False
        if in_ol:
            result.append('</ol>')
            in_ol = False

    def close_table():
        nonlocal in_table, table_has_header
        if in_table:
            result.append('</tbody></table></div>')
            in_table = False
            table_has_header = False

    def process_inline(text: str) -> str:
        """Process inline formatting: bold and furigana."""
        # Process furigana first (this HTML-escapes non-furigana text,
        # so bold markers must be converted after to avoid escaping)
        text = process_furigana(text)
        # Process bold second (** markers survive html.escape)
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        return text

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Empty line
        if not stripped:
            close_list()
            close_table()
            i += 1
            continue

        # H2 heading
        if stripped.startswith('## ') and not stripped.startswith('### '):
            close_list()
            close_table()
            heading_text = process_inline(stripped[3:])
            result.append(f'<h2>{heading_text}</h2>')
            i += 1
            continue

        # H3 heading
        if stripped.startswith('### '):
            close_list()
            close_table()
            heading_text = process_inline(stripped[4:])
            result.append(f'<h3>{heading_text}</h3>')
            i += 1
            continue

        # Table row
        if stripped.startswith('|') and stripped.endswith('|'):
            close_list()
            cells = [c.strip() for c in stripped.strip('|').split('|')]

            # Check if next line is a separator (|---|---|)
            is_separator = all(re.match(r'^[-:]+$', c.strip()) for c in cells)

            if is_separator:
                # This is a header separator — skip it
                table_has_header = True
                i += 1
                continue

            if not in_table:
                in_table = True
                table_has_header = False
                result.append('<div class="table-wrap"><table class="article-table"><thead>')
                cell_html = ''.join(f'<th>{process_inline(c)}</th>' for c in cells)
                result.append(f'<tr>{cell_html}</tr>')
                # Peek ahead to see if next line is separator
                if i + 1 < len(lines):
                    next_stripped = lines[i + 1].strip()
                    if next_stripped.startswith('|') and next_stripped.endswith('|'):
                        next_cells = [c.strip() for c in next_stripped.strip('|').split('|')]
                        if all(re.match(r'^[-:]+$', c.strip()) for c in next_cells):
                            # Next line is separator — this row is the header
                            result.append('</thead><tbody>')
                            i += 2  # skip separator
                            continue
                # No separator follows — treat as body
                result.append('</thead><tbody>')
                i += 1
                continue
            else:
                # Body row
                cell_html = ''.join(f'<td>{process_inline(c)}</td>' for c in cells)
                result.append(f'<tr>{cell_html}</tr>')
                i += 1
                continue

        # Unordered list
        if stripped.startswith('- '):
            close_table()
            if not in_list:
                close_list()
                in_list = True
                result.append('<ul>')
            item_text = process_inline(stripped[2:])
            result.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Ordered list
        ol_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if ol_match:
            close_table()
            if not in_ol:
                close_list()
                in_ol = True
                result.append('<ol>')
            item_text = process_inline(ol_match.group(2))
            result.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Regular paragraph
        close_list()
        close_table()
        para_text = process_inline(stripped)
        result.append(f'<p>{para_text}</p>')
        i += 1

    close_list()
    close_table()

    return '\n'.join(result)


def generate_article_html(article: dict, entries_dict: dict) -> str:
    """Generate HTML content for a single article page."""
    article_id = article['id']
    title_en = article['title']['english']
    title_ja = article['title']['japanese']

    description = f"{title_en} — An explanatory article from the TKG Japanese-English Learner's Dictionary."

    # Articles live at docs/articles/{id}.html, so relative path to root is ../
    relative_path = '../'

    html_parts = [
        generate_html_head(title_en, relative_path, description),
        '<body>',
        generate_nav_header(relative_path, show_all_links=True),
        '<main class="article-page">',
        '<article class="article-display">',
    ]

    # Article header
    title_ja_html = process_furigana(title_ja)
    html_parts.append(f'''
        <div class="article-header">
            <h1 class="article-title">{html.escape(title_en)}</h1>
            <div class="article-title-ja" lang="ja">{title_ja_html}</div>
        </div>
    ''')

    # Article body (markdown → HTML)
    body_html = markdown_to_html(article['body'])
    html_parts.append(f'''
        <div class="article-content">
            {body_html}
        </div>
    ''')

    # Related entries
    related = article.get('related_entries', [])
    if related:
        html_parts.append('<div class="article-related">')
        html_parts.append('<h2>Related Dictionary Entries</h2>')
        html_parts.append('<div class="article-related-list">')
        for ref in related:
            entry_id = ref['entry_id']
            headword_raw = ref['headword']
            note = ref.get('note', '')
            headword_html = process_furigana(headword_raw)
            note_html = f' <span class="article-related-note">({html.escape(note)})</span>' if note else ''

            if entry_id in entries_dict:
                dir_range = get_directory_range(entry_id)
                entry_path = f"{relative_path}entries/{dir_range}/{entry_id}.html"
                html_parts.append(
                    f'<a href="{entry_path}" class="article-related-link">'
                    f'{headword_html}{note_html}</a>'
                )
            else:
                html_parts.append(
                    f'<span class="article-related-pending">'
                    f'{headword_html}{note_html}</span>'
                )
        html_parts.append('</div>')
        html_parts.append('</div>')

    # Metadata
    metadata = article.get('metadata', {})
    created_str = format_jst_datetime(metadata.get('created', ''))
    modified_str = format_jst_datetime(metadata.get('modified', ''))

    date_display = ''
    if created_str:
        date_display = f'Published {created_str}'
        if modified_str and metadata.get('created') != metadata.get('modified'):
            date_display += f' · Updated {modified_str}'

    html_parts.append(f'''
        <div class="article-metadata">
            <div class="article-meta-row">
                <div class="article-meta-dates">{date_display}</div>
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

    html_parts.append(generate_header_search_redirect_script())
    html_parts.append(generate_furigana_script())
    html_parts.append(generate_examples_script())
    html_parts.append(generate_wordlinks_script())
    html_parts.append(generate_goatcounter_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)


def generate_article_index_html(articles: list) -> str:
    """Generate the articles index page listing all articles."""
    relative_path = '../'

    html_parts = [
        generate_html_head("Articles", relative_path,
                          "Expository articles about Japanese language topics — TKG Japanese-English Learner's Dictionary"),
        '<body>',
        generate_nav_header(relative_path, show_all_links=True),
        '<main class="article-index-page">',
        '<h1>Articles</h1>',
        '<p class="article-index-intro">In-depth articles about Japanese language topics that go beyond individual dictionary entries.</p>',
        '<div class="article-index-list">',
    ]

    for article in sorted(articles, key=lambda a: a['title']['english']):
        article_id = article['id']
        title_en = article['title']['english']
        title_ja = article['title']['japanese']
        title_ja_html = process_furigana(title_ja)
        tags = article.get('tags', [])
        related_count = len(article.get('related_entries', []))

        tags_html = ''
        if tags:
            tags_html = '<div class="article-card-tags">' + ''.join(
                f'<span class="article-card-tag">{html.escape(t)}</span>' for t in tags
            ) + '</div>'

        html_parts.append(f'''
            <a href="{article_id}.html" class="article-card">
                <div class="article-card-title">{html.escape(title_en)}</div>
                <div class="article-card-title-ja" lang="ja">{title_ja_html}</div>
                {tags_html}
                <div class="article-card-meta">{related_count} related entries</div>
            </a>
        ''')

    html_parts.append('</div>')
    html_parts.append('</main>')

    html_parts.append(f'''
        <footer>
            <p><a href="{relative_path}index.html">TKG Japanese-English Learner's Dictionary</a></p>
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


def build_article_to_entry_map(articles: list) -> dict:
    """Build a mapping from entry_id to list of articles that reference it.

    Returns dict: {entry_id: [{"article_id": ..., "title": ...}, ...]}
    """
    entry_to_articles = {}
    for article in articles:
        article_info = {
            'article_id': article['id'],
            'title': article['title']['english'],
        }
        for ref in article.get('related_entries', []):
            entry_id = ref['entry_id']
            if entry_id not in entry_to_articles:
                entry_to_articles[entry_id] = []
            entry_to_articles[entry_id].append(article_info)
    return entry_to_articles
