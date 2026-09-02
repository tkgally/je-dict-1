#!/usr/bin/env python3
"""
Build kanji index HTML pages.

Generates HTML pages for each kanji showing all dictionary entries
that contain that kanji in their headword.
"""

import json
import html
from pathlib import Path

# Import shared utilities
from path_utils import get_directory_range
from japanese_utils import FURIGANA_PATTERN, romaji_to_hiragana, romaji_to_katakana
from html_utils import (
    process_furigana as _process_furigana,
    generate_nav_header as _generate_nav_header,
    generate_furigana_script,
    generate_examples_script,
    generate_header_search_script,
    generate_wordlinks_script,
    generate_goatcounter_script,
)


def process_furigana(text: str) -> str:
    """Convert furigana notation to HTML ruby tags."""
    return _process_furigana(text, FURIGANA_PATTERN)


def generate_nav_header(relative_path: str = '../') -> str:
    """Generate the (full) navigation header for kanji pages."""
    return _generate_nav_header(relative_path)


def readings_to_kana(value: str, convert) -> list:
    """'kou, gou' -> ['コウ', 'ゴウ'] using the given romaji converter; 'none' -> []."""
    if not value or value == 'none':
        return []
    return [convert(part.strip()) for part in value.split(',') if part.strip()]


def generate_kanji_page(kanji_data: dict, relative_path: str = '../') -> str:
    """Generate HTML for a kanji index page."""
    meta = kanji_data['metadata']
    entries = kanji_data['entries']

    kanji = meta['kanji']
    onyomi = meta['onyomi']
    kunyomi = meta['kunyomi']
    gloss = meta['gloss']
    entry_count = meta['entry_count']

    # Convert readings to Japanese script for display (comma-separated lists allowed)
    on_list = readings_to_kana(onyomi, romaji_to_katakana)
    kun_list = readings_to_kana(kunyomi, romaji_to_hiragana)
    onyomi_display = '、'.join(on_list) if on_list else '—'
    kunyomi_display = '、'.join(kun_list) if kun_list else '—'
    onyomi_romaji = f' <span class="reading-romaji">({html.escape(onyomi)})</span>' if on_list else ''
    kunyomi_romaji = f' <span class="reading-romaji">({html.escape(kunyomi)})</span>' if kun_list else ''

    title = f"{kanji} - Kanji Index"
    description = f"Dictionary entries containing the kanji {kanji} ({gloss})"

    html_parts = [
        f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html.escape(description)}">
    <title>{html.escape(title)} - TKG Japanese-English Learner's Dictionary</title>
    <link rel="stylesheet" href="{relative_path}styles.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23FFEA00'/><circle cx='50' cy='50' r='30' fill='%23FFC107'/><circle cx='42' cy='42' r='8' fill='white' opacity='0.4'/></svg>">
</head>
<body>''',
        generate_nav_header(relative_path),
        f'''
<main class="kanji-index-page">
    <div class="kanji-header">
        <div class="kanji-display-box">
            <span class="kanji-large" lang="ja">{html.escape(kanji)}</span>
        </div>
        <div class="kanji-info">
            <div class="kanji-readings">
                <div class="reading-row"><span class="reading-label"><span lang="ja">音</span> On:</span><span lang="ja">{onyomi_display}</span>{onyomi_romaji}</div>
                <div class="reading-row"><span class="reading-label"><span lang="ja">訓</span> Kun:</span><span lang="ja">{kunyomi_display}</span>{kunyomi_romaji}</div>
            </div>
            <div class="kanji-gloss">{html.escape(gloss)}</div>
            <div class="kanji-entry-count">{entry_count} headwords · <a href="{relative_path}kanji.html">all kanji</a></div>
        </div>
    </div>

    <section class="kanji-entries-section">
        <h2>Words containing <span lang="ja">{html.escape(kanji)}</span></h2>
        <ul class="kanji-entry-list" lang="ja">''',
    ]

    # Add each entry
    for entry in entries:
        entry_id = entry['id']
        headword = entry['headword']
        reading = entry['reading']
        entry_gloss = entry['gloss']
        dir_range = get_directory_range(entry_id)

        html_parts.append(f'''
            <li class="kanji-entry-item">
                <a href="{relative_path}entries/{dir_range}/{entry_id}.html">
                    <span class="entry-headword">{process_furigana(headword)}</span>
                    <span class="entry-reading">{html.escape(reading)}</span>
                    <span class="entry-gloss" lang="en">{html.escape(entry_gloss)}</span>
                </a>
            </li>''')

    html_parts.append(f'''
        </ul>
    </section>
</main>

<footer>
    <p><a href="{relative_path}index.html">TKG Japanese-English Learner's Dictionary</a></p>
</footer>
{generate_header_search_script(relative_path)}
{generate_furigana_script()}
{generate_examples_script()}
{generate_wordlinks_script()}
{generate_goatcounter_script()}
</body>
</html>''')

    return '\n'.join(html_parts)


def main():
    kanji_dir = Path('kanji')
    output_dir = Path('docs/kanji')
    output_dir.mkdir(exist_ok=True)

    # Load kanji list
    with open('kanji/kanji_list.json', 'r', encoding='utf-8') as f:
        kanji_list = json.load(f)

    count = 0
    for kanji_char, kanji_info in kanji_list['kanji'].items():
        kanji_id = kanji_info['kanji_id']
        json_path = kanji_dir / f'{kanji_id}.json'

        if not json_path.exists():
            print(f"Warning: Missing JSON for {kanji_char}: {json_path}")
            continue

        with open(json_path, 'r', encoding='utf-8') as f:
            kanji_data = json.load(f)

        html_content = generate_kanji_page(kanji_data)

        output_path = output_dir / f'{kanji_id}.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        count += 1

    print(f"Generated {count} kanji HTML pages in docs/kanji/")


if __name__ == '__main__':
    main()
