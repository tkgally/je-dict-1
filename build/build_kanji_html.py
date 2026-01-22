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
from japanese_utils import FURIGANA_PATTERN


def process_furigana(text: str) -> str:
    """Convert furigana notation to HTML ruby tags."""
    if not text:
        return ''

    def replace_furigana(match):
        kanji = html.escape(match.group(1))
        reading = html.escape(match.group(2))
        return f'<ruby>{kanji}<rp>(</rp><rt>{reading}</rt><rp>)</rp></ruby>'

    parts = []
    last_end = 0
    for match in FURIGANA_PATTERN.finditer(text):
        if match.start() > last_end:
            parts.append(html.escape(text[last_end:match.start()]))
        parts.append(replace_furigana(match))
        last_end = match.end()
    if last_end < len(text):
        parts.append(html.escape(text[last_end:]))

    return ''.join(parts)


def generate_nav_header(relative_path: str = '../') -> str:
    """Generate navigation header HTML."""
    return f'''<header class="nav-header">
    <nav class="nav-links">
        <a href="{relative_path}index.html" class="nav-link">Home</a>
        <a href="{relative_path}advanced.html" class="nav-link">Advanced</a>
        <a href="{relative_path}browse.html" class="nav-link">Browse</a>
        <a href="{relative_path}recent.html" class="nav-link">Recent</a>
        <a href="{relative_path}random.html" class="nav-link">Random</a>
        <a href="{relative_path}pending.html" class="nav-link">Pending</a>
        <a href="{relative_path}about.html" class="nav-link">About</a>
    </nav>
</header>'''


def romaji_to_katakana(romaji: str) -> str:
    """Convert romaji to katakana for on'yomi display."""
    if not romaji or romaji == 'none':
        return ''

    conversions = {
        # Three-character combinations first
        'shi': 'シ', 'chi': 'チ', 'tsu': 'ツ',
        'sha': 'シャ', 'shu': 'シュ', 'sho': 'ショ',
        'cha': 'チャ', 'chu': 'チュ', 'cho': 'チョ',
        'nya': 'ニャ', 'nyu': 'ニュ', 'nyo': 'ニョ',
        'hya': 'ヒャ', 'hyu': 'ヒュ', 'hyo': 'ヒョ',
        'mya': 'ミャ', 'myu': 'ミュ', 'myo': 'ミョ',
        'rya': 'リャ', 'ryu': 'リュ', 'ryo': 'リョ',
        'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ',
        'gya': 'ギャ', 'gyu': 'ギュ', 'gyo': 'ギョ',
        'bya': 'ビャ', 'byu': 'ビュ', 'byo': 'ビョ',
        'pya': 'ピャ', 'pyu': 'ピュ', 'pyo': 'ピョ',
        'ja': 'ジャ', 'ju': 'ジュ', 'jo': 'ジョ',
        # Basic syllables (two-character)
        'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ', 'ko': 'コ',
        'sa': 'サ', 'su': 'ス', 'se': 'セ', 'so': 'ソ',
        'ta': 'タ', 'te': 'テ', 'to': 'ト',
        'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
        'ha': 'ハ', 'hi': 'ヒ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ',
        'ma': 'マ', 'mi': 'ミ', 'mu': 'ム', 'me': 'メ', 'mo': 'モ',
        'ya': 'ヤ', 'yu': 'ユ', 'yo': 'ヨ',
        'ra': 'ラ', 'ri': 'リ', 'ru': 'ル', 're': 'レ', 'ro': 'ロ',
        'wa': 'ワ', 'wo': 'ヲ',
        'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
        'za': 'ザ', 'ji': 'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ',
        'da': 'ダ', 'di': 'ヂ', 'du': 'ヅ', 'de': 'デ', 'do': 'ド',
        'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ',
        'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ',
        # Single vowels (must come after longer patterns)
        'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ',
        'n': 'ン',
    }

    result = romaji.lower()
    # Sort by length (longer first) to avoid partial replacements
    for rom, kata in sorted(conversions.items(), key=lambda x: -len(x[0])):
        result = result.replace(rom, kata)
    return result


def romaji_to_hiragana(romaji: str) -> str:
    """Convert romaji to hiragana for kun'yomi display."""
    if not romaji or romaji == 'none':
        return ''

    conversions = {
        # Three-character combinations first
        'shi': 'し', 'chi': 'ち', 'tsu': 'つ',
        'sha': 'しゃ', 'shu': 'しゅ', 'sho': 'しょ',
        'cha': 'ちゃ', 'chu': 'ちゅ', 'cho': 'ちょ',
        'nya': 'にゃ', 'nyu': 'にゅ', 'nyo': 'にょ',
        'hya': 'ひゃ', 'hyu': 'ひゅ', 'hyo': 'ひょ',
        'mya': 'みゃ', 'myu': 'みゅ', 'myo': 'みょ',
        'rya': 'りゃ', 'ryu': 'りゅ', 'ryo': 'りょ',
        'kya': 'きゃ', 'kyu': 'きゅ', 'kyo': 'きょ',
        'gya': 'ぎゃ', 'gyu': 'ぎゅ', 'gyo': 'ぎょ',
        'bya': 'びゃ', 'byu': 'びゅ', 'byo': 'びょ',
        'pya': 'ぴゃ', 'pyu': 'ぴゅ', 'pyo': 'ぴょ',
        'ja': 'じゃ', 'ju': 'じゅ', 'jo': 'じょ',
        # Basic syllables (two-character)
        'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
        'sa': 'さ', 'su': 'す', 'se': 'せ', 'so': 'そ',
        'ta': 'た', 'te': 'て', 'to': 'と',
        'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
        'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
        'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
        'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
        'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
        'wa': 'わ', 'wo': 'を',
        'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
        'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
        'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
        'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
        'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
        # Single vowels (must come after longer patterns)
        'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
        'n': 'ん',
    }

    result = romaji.lower()
    for rom, hira in sorted(conversions.items(), key=lambda x: -len(x[0])):
        result = result.replace(rom, hira)
    return result


def generate_kanji_page(kanji_data: dict, relative_path: str = '../') -> str:
    """Generate HTML for a kanji index page."""
    meta = kanji_data['metadata']
    entries = kanji_data['entries']

    kanji = meta['kanji']
    onyomi = meta['onyomi']
    kunyomi = meta['kunyomi']
    gloss = meta['gloss']
    entry_count = meta['entry_count']

    # Convert readings to Japanese script for display
    onyomi_display = romaji_to_katakana(onyomi) if onyomi != 'none' else '—'
    kunyomi_display = romaji_to_hiragana(kunyomi) if kunyomi != 'none' else '—'

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
            <span class="kanji-large">{html.escape(kanji)}</span>
        </div>
    </div>

    <section class="kanji-entries-section">
        <ul class="kanji-entry-list">''',
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
                    <span class="entry-gloss">{html.escape(entry_gloss)}</span>
                </a>
            </li>''')

    html_parts.append('''
        </ul>
    </section>
</main>

<footer>
    <p><a href="../index.html">TKG Japanese-English Learner's Dictionary</a></p>
</footer>
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
