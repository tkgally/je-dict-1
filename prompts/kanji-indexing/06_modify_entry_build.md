# Kanji Index Implementation - Step 6: Modify Entry Build for Kanji Links

## Overview

Modify `build/build_flat.py` to add invisible links from kanji in entry headwords to their kanji index pages.

## Prerequisites

- `kanji/kanji_list.json` must be complete
- Kanji HTML pages exist in `docs/kanji/`
- Current `build/build_flat.py` works correctly

## Task

Modify `build/build_flat.py` to:

1. **Load** `kanji/kanji_list.json` at startup
2. **Modify** `process_furigana()` to wrap kanji in links to their kanji index pages
3. **Add** CSS for unobtrusive kanji links
4. **Ensure** links have title attribute: "Other words with this kanji"

### Key Changes to build_flat.py

#### 1. Load kanji list at startup

Add near the top of the file:

```python
# Load kanji index for headword linking
KANJI_LIST = {}
kanji_list_path = Path(__file__).parent.parent / 'kanji' / 'kanji_list.json'
if kanji_list_path.exists():
    with open(kanji_list_path, 'r', encoding='utf-8') as f:
        kanji_data = json.load(f)
        KANJI_LIST = kanji_data.get('kanji', {})
```

#### 2. Create new function for headword processing

Add a new function specifically for headword kanji linking:

```python
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
```

#### 3. Modify generate_entry_html to use the new function

In `generate_entry_html()`, change the headword line from:

```python
<h1 class="entry-headword">{process_furigana(headword)}</h1>
```

To:

```python
<h1 class="entry-headword">{process_headword_with_kanji_links(headword, relative_path)}</h1>
```

**Important**: Only the headword gets kanji links. Examples and notes should continue using the regular `process_furigana()` function.

### CSS Additions

Add to `docs/styles.css`:

```css
/* Kanji Index Links in Headwords */
.kanji-link {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
}

.kanji-link:hover {
    /* Subtle indication without changing appearance */
    text-decoration: none;
}

/* Optional: very subtle hover effect */
.entry-headword .kanji-link:hover {
    background: rgba(0, 0, 0, 0.05);
    border-radius: 2px;
}
```

### Title Attribute

The links include `title="Other words with this kanji"` which creates a browser tooltip on hover.

### Complete Modified Section

Here's what the entry header section should look like after modification:

```python
# Entry header with kanji links in headword
html_parts.append(f'''
    <div class="entry-header">
        <h1 class="entry-headword">{process_headword_with_kanji_links(headword, relative_path)}</h1>
        <div class="entry-reading">{html.escape(reading)}</div>
        <div class="entry-pos">{html.escape(entry.get('part_of_speech', ''))}</div>
        <div class="entry-gloss">{html.escape(entry.get('gloss', ''))}</div>
    </div>
''')
```

## Testing

After modification:

1. Run `python3 build/build_flat.py`
2. Open an entry page with kanji (e.g., `docs/entries/00000/00001_amaru.html`)
3. Verify:
   - Kanji in headword are wrapped in links
   - Links are invisible (same color as text)
   - Hovering shows "Other words with this kanji" tooltip
   - Clicking navigates to the kanji index page
   - Examples and notes do NOT have kanji links

## Edge Cases

- **Kanji not in index**: If a kanji appears in a headword but isn't in `kanji_list.json`, it should be displayed normally without a link
- **Empty kanji list**: If `kanji/kanji_list.json` doesn't exist or is empty, headwords should render normally
- **Mixed text**: Headwords with kanji, hiragana, katakana, and punctuation should all render correctly

## Verification

```bash
# Rebuild all entry pages
python3 build/build_flat.py

# Check a specific entry
grep "kanji-link" docs/entries/00000/00001_amaru.html

# Should see links like:
# <a href="../../kanji/00123_yo_ama_remain.html" class="kanji-link" title="Other words with this kanji">余</a>
```

## Next Step

Proceed to `07_update_entry_scripts.md` to modify entry creation scripts to update the kanji index.
