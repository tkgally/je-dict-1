# Kanji Index Implementation - Step 5: Build Kanji HTML Pages

## Overview

Create a script that generates HTML pages for each kanji index, showing the kanji and all dictionary entries containing it.

## Prerequisites

- `kanji/kanji_list.json` must be complete
- Individual kanji JSON files exist in `kanji/` (created in Step 4)
- `build/build_flat.py` exists (for reference on HTML generation patterns)

## Task

Create `build/build_kanji_html.py`:

### Page Design

Each kanji page (`docs/kanji/{kanji_id}.html`) has:

1. **Header** - Standard navigation (same as entry pages)
2. **Kanji Display** - Large kanji character in a square box at upper right
3. **Entry List** - All entries containing this kanji, sorted by reading
4. **Footer** - Standard footer

### HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Dictionary entries containing the kanji 人 (person)">
    <title>人 - Kanji Index - TKG Japanese-English Learner's Dictionary</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
<!-- Standard nav header -->
<header class="nav-header">...</header>

<main class="kanji-index-page">
    <div class="kanji-display">
        <div class="kanji-character">人</div>
        <div class="kanji-info">
            <div class="kanji-readings">
                <span class="onyomi">音: ジン・ニン</span>
                <span class="kunyomi">訓: ひと</span>
            </div>
            <div class="kanji-meaning">person</div>
        </div>
    </div>

    <div class="kanji-entries">
        <h2>Entries with 人 (245 words)</h2>
        <ul class="entry-list">
            <li>
                <a href="../entries/01000/01234_akunin.html">
                    <span class="entry-headword">{悪|あく}{人|にん}</span>
                    <span class="entry-reading">あくにん</span>
                    <span class="entry-gloss">villain, bad person</span>
                </a>
            </li>
            <!-- More entries... -->
        </ul>
    </div>
</main>

<footer>...</footer>
</body>
</html>
```

### Script Structure

```python
#!/usr/bin/env python3
"""
Build kanji index HTML pages.

Generates HTML pages for each kanji showing all dictionary entries
that contain that kanji in their headword.
"""

import json
import html
import re
from pathlib import Path
from datetime import datetime, timezone

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
    # Simplified conversion for display purposes
    conversions = {
        'a': 'ア', 'i': 'イ', 'u': 'ウ', 'e': 'エ', 'o': 'オ',
        'ka': 'カ', 'ki': 'キ', 'ku': 'ク', 'ke': 'ケ', 'ko': 'コ',
        'sa': 'サ', 'shi': 'シ', 'su': 'ス', 'se': 'セ', 'so': 'ソ',
        'ta': 'タ', 'chi': 'チ', 'tsu': 'ツ', 'te': 'テ', 'to': 'ト',
        'na': 'ナ', 'ni': 'ニ', 'nu': 'ヌ', 'ne': 'ネ', 'no': 'ノ',
        'ha': 'ハ', 'hi': 'ヒ', 'fu': 'フ', 'he': 'ヘ', 'ho': 'ホ',
        'ma': 'マ', 'mi': 'ミ', 'mu': 'ム', 'me': 'メ', 'mo': 'モ',
        'ya': 'ヤ', 'yu': 'ユ', 'yo': 'ヨ',
        'ra': 'ラ', 'ri': 'リ', 'ru': 'ル', 're': 'レ', 'ro': 'ロ',
        'wa': 'ワ', 'wo': 'ヲ', 'n': 'ン',
        'ga': 'ガ', 'gi': 'ギ', 'gu': 'グ', 'ge': 'ゲ', 'go': 'ゴ',
        'za': 'ザ', 'ji': 'ジ', 'zu': 'ズ', 'ze': 'ゼ', 'zo': 'ゾ',
        'da': 'ダ', 'di': 'ヂ', 'du': 'ヅ', 'de': 'デ', 'do': 'ド',
        'ba': 'バ', 'bi': 'ビ', 'bu': 'ブ', 'be': 'ベ', 'bo': 'ボ',
        'pa': 'パ', 'pi': 'ピ', 'pu': 'プ', 'pe': 'ペ', 'po': 'ポ',
        'kya': 'キャ', 'kyu': 'キュ', 'kyo': 'キョ',
        'sha': 'シャ', 'shu': 'シュ', 'sho': 'ショ',
        'cha': 'チャ', 'chu': 'チュ', 'cho': 'チョ',
        'nya': 'ニャ', 'nyu': 'ニュ', 'nyo': 'ニョ',
        'hya': 'ヒャ', 'hyu': 'ヒュ', 'hyo': 'ヒョ',
        'mya': 'ミャ', 'myu': 'ミュ', 'myo': 'ミョ',
        'rya': 'リャ', 'ryu': 'リュ', 'ryo': 'リョ',
        'gya': 'ギャ', 'gyu': 'ギュ', 'gyo': 'ギョ',
        'ja': 'ジャ', 'ju': 'ジュ', 'jo': 'ジョ',
        'bya': 'ビャ', 'byu': 'ビュ', 'byo': 'ビョ',
        'pya': 'ピャ', 'pyu': 'ピュ', 'pyo': 'ピョ',
    }
    # Handle long vowels (ou -> オウ)
    result = romaji.lower()
    # Sort by length (longer first) to avoid partial replacements
    for rom, kata in sorted(conversions.items(), key=lambda x: -len(x[0])):
        result = result.replace(rom, kata)
    return result

def romaji_to_hiragana(romaji: str) -> str:
    """Convert romaji to hiragana for kun'yomi display."""
    conversions = {
        'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
        'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
        'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
        'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
        'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
        'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
        'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
        'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
        'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
        'wa': 'わ', 'wo': 'を', 'n': 'ん',
        'ga': 'が', 'gi': 'ぎ', 'gu': 'ぐ', 'ge': 'げ', 'go': 'ご',
        'za': 'ざ', 'ji': 'じ', 'zu': 'ず', 'ze': 'ぜ', 'zo': 'ぞ',
        'da': 'だ', 'di': 'ぢ', 'du': 'づ', 'de': 'で', 'do': 'ど',
        'ba': 'ば', 'bi': 'び', 'bu': 'ぶ', 'be': 'べ', 'bo': 'ぼ',
        'pa': 'ぱ', 'pi': 'ぴ', 'pu': 'ぷ', 'pe': 'ぺ', 'po': 'ぽ',
        # Add more as needed
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
    kanji_id = meta['kanji_id']
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
        <div class="kanji-info">
            <div class="kanji-readings">
                <div class="reading-row"><span class="reading-label">音:</span> <span class="reading-value">{html.escape(onyomi_display)}</span></div>
                <div class="reading-row"><span class="reading-label">訓:</span> <span class="reading-value">{html.escape(kunyomi_display)}</span></div>
            </div>
            <div class="kanji-gloss">{html.escape(gloss)}</div>
        </div>
    </div>

    <section class="kanji-entries-section">
        <h2>Entries containing {html.escape(kanji)} ({entry_count} words)</h2>
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
```

### CSS Additions

Add to `docs/styles.css` the styles for kanji index pages:

```css
/* Kanji Index Page Styles */
.kanji-index-page {
    max-width: 900px;
    margin: 0 auto;
    padding: 1rem;
}

.kanji-header {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
}

.kanji-display-box {
    width: 120px;
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    border: 2px solid #dee2e6;
    border-radius: 8px;
    flex-shrink: 0;
}

.kanji-large {
    font-size: 72px;
    font-family: "Noto Sans JP", "Hiragino Kaku Gothic Pro", sans-serif;
    line-height: 1;
}

.kanji-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.kanji-readings {
    margin-bottom: 0.5rem;
}

.reading-row {
    margin-bottom: 0.25rem;
}

.reading-label {
    font-weight: bold;
    margin-right: 0.5rem;
}

.kanji-gloss {
    font-size: 1.25rem;
    color: #495057;
}

.kanji-entries-section h2 {
    margin-bottom: 1rem;
    font-size: 1.25rem;
}

.kanji-entry-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.kanji-entry-item {
    border-bottom: 1px solid #dee2e6;
}

.kanji-entry-item a {
    display: flex;
    gap: 1rem;
    padding: 0.75rem 0;
    text-decoration: none;
    color: inherit;
}

.kanji-entry-item a:hover {
    background: #f8f9fa;
}

.kanji-entry-item .entry-headword {
    font-weight: bold;
    min-width: 120px;
}

.kanji-entry-item .entry-reading {
    color: #6c757d;
    min-width: 100px;
}

.kanji-entry-item .entry-gloss {
    color: #495057;
    flex: 1;
}
```

## Usage

```bash
python3 build/build_kanji_html.py
```

## Verification

1. Check `docs/kanji/` contains HTML files
2. Open a few pages in browser to verify layout
3. Test links to entry pages work correctly
4. Verify entries are sorted by reading

## Next Step

Proceed to `06_modify_entry_build.md` to add kanji links to entry headwords.
