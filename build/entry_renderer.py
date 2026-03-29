#!/usr/bin/env python3
"""
Entry page HTML generation for je-dict-1 dictionary.

Extracted from build_flat.py to keep the build script manageable.
Generates HTML content for individual dictionary entry pages.
"""

import json
import re
import html
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone, timedelta

from path_utils import get_directory_range
from japanese_utils import FURIGANA_PATTERN, strip_furigana, is_kanji
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
else:
    print("Warning: kanji/kanji_list.json not found — kanji links will be disabled")


def process_furigana(text: str, show_furigana: bool = True) -> str:
    """Convert furigana notation to HTML ruby tags."""
    return _process_furigana_base(text, FURIGANA_PATTERN, show_furigana)


def process_word_links(text: str, entries_dict: dict, relative_path: str = '../../') -> str:
    """Process word link markup in text and generate HTML with links."""
    return _process_word_links_base(text, entries_dict, relative_path, FURIGANA_PATTERN)


def format_jst_datetime(iso_string: str) -> str:
    """Format an ISO datetime string to JST format: YYYY.M.D H:MM"""
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        dt_jst = dt.astimezone(JST)
        return f"{dt_jst.year}.{dt_jst.month}.{dt_jst.day} {dt_jst.hour}:{dt_jst.minute:02d}"
    except (ValueError, AttributeError):
        return ''


def generate_html_head(title: str, relative_path: str = '', description: str = '', noindex: bool = False) -> str:
    """Generate HTML head section."""
    desc = description or 'TKG Japanese-English Learner\'s Dictionary (TKGJE) - An explanatory dictionary for learners of Japanese'
    noindex_tag = '\n    <meta name="robots" content="noindex, nofollow">' if noindex else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html.escape(desc).replace('&#x27;', "'")}">{noindex_tag}
    <title>{html.escape(title)} - TKG Japanese-English Learner's Dictionary</title>
    <link rel="stylesheet" href="{relative_path}styles.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23FFEA00'/><circle cx='50' cy='50' r='30' fill='%23FFC107'/><circle cx='42' cy='42' r='8' fill='white' opacity='0.4'/></svg>">
</head>'''


# ── Verb conjugation table generation ──────────────────────────────────────

# Godan vowel rows keyed by dictionary-form ending kana
_GODAN_ROWS = {
    #  ending:  (a-row,   i-row,   u-row,  e-row,  o-row,  te/ta-base)
    'う': ('わ', 'い', 'う', 'え', 'お', 'っ'),
    'く': ('か', 'き', 'く', 'け', 'こ', 'い'),
    'ぐ': ('が', 'ぎ', 'ぐ', 'げ', 'ご', 'い'),
    'す': ('さ', 'し', 'す', 'せ', 'そ', 'し'),
    'つ': ('た', 'ち', 'つ', 'て', 'と', 'っ'),
    'ぬ': ('な', 'に', 'ぬ', 'ね', 'の', 'ん'),
    'ぶ': ('ば', 'び', 'ぶ', 'べ', 'ぼ', 'ん'),
    'む': ('ま', 'み', 'む', 'め', 'も', 'ん'),
    'る': ('ら', 'り', 'る', 'れ', 'ろ', 'っ'),
}

# te/ta suffix depends on ending
_GODAN_TE_TA = {
    'う': ('て', 'た'),   'く': ('て', 'た'),   'ぐ': ('で', 'だ'),
    'す': ('て', 'た'),   'つ': ('て', 'た'),   'ぬ': ('で', 'だ'),
    'ぶ': ('で', 'だ'),   'む': ('で', 'だ'),   'る': ('て', 'た'),
}


def _generate_godan_forms(stem: str, ending: str, overrides: dict) -> list:
    """Generate all conjugation forms for a godan verb."""
    a, i, _u, e, o, te_base = _GODAN_ROWS[ending]
    te_suf, ta_suf = _GODAN_TE_TA[ending]

    te = f'{stem}{te_base}{te_suf}'
    ta = f'{stem}{te_base}{ta_suf}'

    def ov(key, default):
        return overrides.get(key, default)

    return [
        # Group 1: Basic forms
        ('Present', ov('present_affirmative', f'{stem}{ending}'),
                    ov('present_negative', f'{stem}{a}ない')),
        ('Present polite', ov('present_polite_affirmative', f'{stem}{i}ます'),
                           ov('present_polite_negative', f'{stem}{i}ません')),
        ('Past', ov('past_affirmative', ta),
                 ov('past_negative', f'{stem}{a}なかった')),
        ('Past polite', ov('past_polite_affirmative', f'{stem}{i}ました'),
                        ov('past_polite_negative', f'{stem}{i}ませんでした')),
        ('て form', ov('te_affirmative', te),
                    ov('te_negative', f'{stem}{a}なくて')),
        # Group 2: Progressive (ている)
        ('ている present', ov('progressive_present_affirmative', f'{te}いる'),
                           ov('progressive_present_negative', f'{te}いない')),
        ('ている polite', ov('progressive_present_polite_affirmative', f'{te}います'),
                          ov('progressive_present_polite_negative', f'{te}いません')),
        ('ている past', ov('progressive_past_affirmative', f'{te}いた'),
                        ov('progressive_past_negative', f'{te}いなかった')),
        ('ている past polite', ov('progressive_past_polite_affirmative', f'{te}いました'),
                               ov('progressive_past_polite_negative', f'{te}いませんでした')),
        # Group 3: Conditional
        ('Conditional ば', ov('conditional_ba_affirmative', f'{stem}{e}ば'),
                          ov('conditional_ba_negative', f'{stem}{a}なければ')),
        ('Conditional たら', ov('conditional_tara_affirmative', f'{ta}ら'),
                            ov('conditional_tara_negative', f'{stem}{a}なかったら')),
        # Group 4: Volitional
        ('Volitional', ov('volitional_affirmative', f'{stem}{o}う'), None),
        ('Volitional polite', ov('volitional_polite', f'{stem}{i}ましょう'), None),
        # Group 5: Other forms
        ('Potential', ov('potential_affirmative', f'{stem}{e}る'),
                      ov('potential_negative', f'{stem}{e}ない')),
        ('Passive', ov('passive_affirmative', f'{stem}{a}れる'),
                    ov('passive_negative', f'{stem}{a}れない')),
        ('Causative', ov('causative_affirmative', f'{stem}{a}せる'),
                      ov('causative_negative', f'{stem}{a}せない')),
        ('Imperative', ov('imperative_affirmative', f'{stem}{e}'),
                       ov('imperative_negative', f'{stem}{ending}な')),
    ]


def _generate_ichidan_forms(stem: str, overrides: dict) -> list:
    """Generate all conjugation forms for an ichidan verb."""
    def ov(key, default):
        return overrides.get(key, default)

    return [
        ('Present', ov('present_affirmative', f'{stem}る'),
                    ov('present_negative', f'{stem}ない')),
        ('Present polite', ov('present_polite_affirmative', f'{stem}ます'),
                           ov('present_polite_negative', f'{stem}ません')),
        ('Past', ov('past_affirmative', f'{stem}た'),
                 ov('past_negative', f'{stem}なかった')),
        ('Past polite', ov('past_polite_affirmative', f'{stem}ました'),
                        ov('past_polite_negative', f'{stem}ませんでした')),
        ('て form', ov('te_affirmative', f'{stem}て'),
                    ov('te_negative', f'{stem}なくて')),
        ('ている present', ov('progressive_present_affirmative', f'{stem}ている'),
                           ov('progressive_present_negative', f'{stem}ていない')),
        ('ている polite', ov('progressive_present_polite_affirmative', f'{stem}ています'),
                          ov('progressive_present_polite_negative', f'{stem}ていません')),
        ('ている past', ov('progressive_past_affirmative', f'{stem}ていた'),
                        ov('progressive_past_negative', f'{stem}ていなかった')),
        ('ている past polite', ov('progressive_past_polite_affirmative', f'{stem}ていました'),
                               ov('progressive_past_polite_negative', f'{stem}ていませんでした')),
        ('Conditional ば', ov('conditional_ba_affirmative', f'{stem}れば'),
                          ov('conditional_ba_negative', f'{stem}なければ')),
        ('Conditional たら', ov('conditional_tara_affirmative', f'{stem}たら'),
                            ov('conditional_tara_negative', f'{stem}なかったら')),
        ('Volitional', ov('volitional_affirmative', f'{stem}よう'), None),
        ('Volitional polite', ov('volitional_polite', f'{stem}ましょう'), None),
        ('Potential', ov('potential_affirmative', f'{stem}られる'),
                      ov('potential_negative', f'{stem}られない')),
        ('Passive', ov('passive_affirmative', f'{stem}られる'),
                    ov('passive_negative', f'{stem}られない')),
        ('Causative', ov('causative_affirmative', f'{stem}させる'),
                      ov('causative_negative', f'{stem}させない')),
        ('Imperative', ov('imperative_affirmative', f'{stem}ろ'),
                       ov('imperative_negative', f'{stem}るな')),
    ]


def _generate_suru_forms(prefix: str, overrides: dict) -> list:
    """Generate all conjugation forms for a する verb."""
    p = prefix

    def ov(key, default):
        return overrides.get(key, default)

    return [
        ('Present', ov('present_affirmative', f'{p}する'),
                    ov('present_negative', f'{p}しない')),
        ('Present polite', ov('present_polite_affirmative', f'{p}します'),
                           ov('present_polite_negative', f'{p}しません')),
        ('Past', ov('past_affirmative', f'{p}した'),
                 ov('past_negative', f'{p}しなかった')),
        ('Past polite', ov('past_polite_affirmative', f'{p}しました'),
                        ov('past_polite_negative', f'{p}しませんでした')),
        ('て form', ov('te_affirmative', f'{p}して'),
                    ov('te_negative', f'{p}しなくて')),
        ('ている present', ov('progressive_present_affirmative', f'{p}している'),
                           ov('progressive_present_negative', f'{p}していない')),
        ('ている polite', ov('progressive_present_polite_affirmative', f'{p}しています'),
                          ov('progressive_present_polite_negative', f'{p}していません')),
        ('ている past', ov('progressive_past_affirmative', f'{p}していた'),
                        ov('progressive_past_negative', f'{p}していなかった')),
        ('ている past polite', ov('progressive_past_polite_affirmative', f'{p}していました'),
                               ov('progressive_past_polite_negative', f'{p}していませんでした')),
        ('Conditional ば', ov('conditional_ba_affirmative', f'{p}すれば'),
                          ov('conditional_ba_negative', f'{p}しなければ')),
        ('Conditional たら', ov('conditional_tara_affirmative', f'{p}したら'),
                            ov('conditional_tara_negative', f'{p}しなかったら')),
        ('Volitional', ov('volitional_affirmative', f'{p}しよう'), None),
        ('Volitional polite', ov('volitional_polite', f'{p}しましょう'), None),
        ('Potential', ov('potential_affirmative', f'{p}できる'),
                      ov('potential_negative', f'{p}できない')),
        ('Passive', ov('passive_affirmative', f'{p}される'),
                    ov('passive_negative', f'{p}されない')),
        ('Causative', ov('causative_affirmative', f'{p}させる'),
                      ov('causative_negative', f'{p}させない')),
        ('Imperative', ov('imperative_affirmative', f'{p}しろ'),
                       ov('imperative_negative', f'{p}するな')),
    ]


def _generate_kuru_forms(prefix: str, overrides: dict) -> list:
    """Generate all conjugation forms for a 来る verb."""
    p = prefix

    def ov(key, default):
        return overrides.get(key, default)

    return [
        ('Present', ov('present_affirmative', f'{p}{{来|く}}る'),
                    ov('present_negative', f'{p}{{来|こ}}ない')),
        ('Present polite', ov('present_polite_affirmative', f'{p}{{来|き}}ます'),
                           ov('present_polite_negative', f'{p}{{来|き}}ません')),
        ('Past', ov('past_affirmative', f'{p}{{来|き}}た'),
                 ov('past_negative', f'{p}{{来|こ}}なかった')),
        ('Past polite', ov('past_polite_affirmative', f'{p}{{来|き}}ました'),
                        ov('past_polite_negative', f'{p}{{来|き}}ませんでした')),
        ('て form', ov('te_affirmative', f'{p}{{来|き}}て'),
                    ov('te_negative', f'{p}{{来|こ}}なくて')),
        ('ている present', ov('progressive_present_affirmative', f'{p}{{来|き}}ている'),
                           ov('progressive_present_negative', f'{p}{{来|き}}ていない')),
        ('ている polite', ov('progressive_present_polite_affirmative', f'{p}{{来|き}}ています'),
                          ov('progressive_present_polite_negative', f'{p}{{来|き}}ていません')),
        ('ている past', ov('progressive_past_affirmative', f'{p}{{来|き}}ていた'),
                        ov('progressive_past_negative', f'{p}{{来|き}}ていなかった')),
        ('ている past polite', ov('progressive_past_polite_affirmative', f'{p}{{来|き}}ていました'),
                               ov('progressive_past_polite_negative', f'{p}{{来|き}}ていませんでした')),
        ('Conditional ば', ov('conditional_ba_affirmative', f'{p}{{来|く}}れば'),
                          ov('conditional_ba_negative', f'{p}{{来|こ}}なければ')),
        ('Conditional たら', ov('conditional_tara_affirmative', f'{p}{{来|き}}たら'),
                            ov('conditional_tara_negative', f'{p}{{来|こ}}なかったら')),
        ('Volitional', ov('volitional_affirmative', f'{p}{{来|こ}}よう'), None),
        ('Volitional polite', ov('volitional_polite', f'{p}{{来|き}}ましょう'), None),
        ('Potential', ov('potential_affirmative', f'{p}{{来|こ}}られる'),
                      ov('potential_negative', f'{p}{{来|こ}}られない')),
        ('Passive', ov('passive_affirmative', f'{p}{{来|こ}}られる'),
                    ov('passive_negative', f'{p}{{来|こ}}られない')),
        ('Causative', ov('causative_affirmative', f'{p}{{来|こ}}させる'),
                      ov('causative_negative', f'{p}{{来|こ}}させない')),
        ('Imperative', ov('imperative_affirmative', f'{p}{{来|こ}}い'),
                       ov('imperative_negative', f'{p}{{来|く}}るな')),
    ]


def _generate_aru_forms(overrides: dict) -> list:
    """Generate conjugation forms for ある (limited set)."""
    def ov(key, default):
        return overrides.get(key, default)

    return [
        ('Present', ov('present_affirmative', 'ある'),
                    ov('present_negative', 'ない')),
        ('Present polite', ov('present_polite_affirmative', 'あります'),
                           ov('present_polite_negative', 'ありません')),
        ('Past', ov('past_affirmative', 'あった'),
                 ov('past_negative', 'なかった')),
        ('Past polite', ov('past_polite_affirmative', 'ありました'),
                        ov('past_polite_negative', 'ありませんでした')),
        ('て form', ov('te_affirmative', 'あって'),
                    ov('te_negative', 'なくて')),
        ('Conditional ば', ov('conditional_ba_affirmative', 'あれば'),
                          ov('conditional_ba_negative', 'なければ')),
        ('Conditional たら', ov('conditional_tara_affirmative', 'あったら'),
                            ov('conditional_tara_negative', 'なかったら')),
    ]


# Row group boundaries for visual separators in the table.
# After these row labels, a group-separator class is added.
_GROUP_LAST_ROWS = {'て form', 'ている past polite', 'Conditional たら', 'Volitional polite'}


def generate_conjugation_html(conjugation: dict) -> str:
    """
    Generate the <details> HTML block for a verb conjugation table.

    Args:
        conjugation: The conjugation object from the entry JSON.

    Returns:
        HTML string for the conjugation details block, or empty string if
        the conjugation data is invalid.
    """
    conj_type = conjugation.get('type', '')
    overrides = conjugation.get('overrides', {})

    if conj_type == 'godan':
        ending = conjugation.get('ending', '')
        stem = conjugation.get('stem', '')
        if not ending or ending not in _GODAN_ROWS or stem is None:
            return ''
        forms = _generate_godan_forms(stem, ending, overrides)
    elif conj_type == 'ichidan':
        stem = conjugation.get('stem', '')
        if stem is None:
            return ''
        forms = _generate_ichidan_forms(stem, overrides)
    elif conj_type == 'suru':
        prefix = conjugation.get('prefix', '')
        if prefix is None:
            return ''
        forms = _generate_suru_forms(prefix, overrides)
    elif conj_type == 'kuru':
        prefix = conjugation.get('prefix', '')
        if prefix is None:
            return ''
        forms = _generate_kuru_forms(prefix, overrides)
    elif conj_type == 'aru':
        forms = _generate_aru_forms(overrides)
    else:
        return ''

    # Build table rows
    rows = []
    for label, aff, neg in forms:
        aff_html = process_furigana(aff) if aff else ''
        neg_html = process_furigana(neg) if neg else '—'
        group_end = ' class="conj-group-end"' if label in _GROUP_LAST_ROWS else ''
        rows.append(
            f'<tr{group_end}>'
            f'<td class="conj-label">{html.escape(label)}</td>'
            f'<td class="conj-form">{aff_html}</td>'
            f'<td class="conj-form">{neg_html}</td>'
            f'</tr>'
        )

    table_html = '\n'.join(rows)
    return (
        '<details class="conjugation-details">\n'
        '<summary>Conjugation</summary>\n'
        '<table class="conjugation-table">\n'
        '<thead><tr>'
        '<th></th><th>Affirmative</th><th>Negative</th>'
        '</tr></thead>\n'
        f'<tbody>\n{table_html}\n</tbody>\n'
        '</table>\n'
        '</details>'
    )


# ── End conjugation ───────────────────────────────────────────────────────


def process_headword_with_kanji_links(text: str, relative_path: str = '../../') -> str:
    """
    Process headword text with furigana AND kanji links.

    For headwords, kanji characters are wrapped in links to their kanji index pages.
    The links are styled to be invisible (no color change, no underline) but show
    a tooltip on hover.
    """
    if not text:
        return ''

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


def render_examples(examples_list, entries_dict: dict, relative_path: str = '../../'):
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
    ''')

    # Prominent see-also (high-visibility cross-references shown inside entry-header, above the border)
    prominent_refs = entry.get('prominent_see_also', [])
    if prominent_refs:
        html_parts.append('<div class="prominent-see-also">')
        ref_links = []
        for ref in prominent_refs:
            ref_reading = ref.get('reading', '')
            ref_headword = ref.get('headword', '')
            ref_note = ref.get('note', '')
            target_id = ref.get('target_id', '')

            # Resolve target
            if not target_id:
                candidates = readings_to_entries.get(ref_reading, [])
                if len(candidates) == 1:
                    target_id = candidates[0]['id']
                elif len(candidates) > 1 and ref_headword:
                    for candidate in candidates:
                        if candidate['headword'] == ref_headword:
                            target_id = candidate['id']
                            break

            display = process_furigana(ref_headword) if ref_headword else html.escape(ref_reading)
            note_text = f' ({html.escape(ref_note)})' if ref_note else ''

            if target_id and target_id in entries_dict:
                target_dir_range = get_directory_range(target_id)
                ref_links.append(
                    f'<a href="{relative_path}entries/{target_dir_range}/{target_id}.html"'
                    f' class="prominent-ref-link">{display}</a>{note_text}'
                )
            else:
                ref_links.append(f'<span class="prominent-ref-pending">{display}</span>{note_text}')

        html_parts.append(f'<span class="prominent-ref-label">See also:</span> ')
        html_parts.append(', '.join(ref_links))
        html_parts.append('</div>')

    html_parts.append('</div>')  # Close entry-header

    # Conjugation table (verbs only — rendered from the conjugation field)
    conjugation = entry.get('conjugation')
    if conjugation:
        conj_html = generate_conjugation_html(conjugation)
        if conj_html:
            html_parts.append(conj_html)

    # Definitions and Examples
    definitions = entry.get('definitions', [])
    examples = entry.get('examples', [])

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
                html_parts.append(render_examples(sense_examples, entries_dict, relative_path))
                html_parts.append('</div>')

            html_parts.append('</div>')  # Close sense-block

        # Add any "general" examples that weren't assigned to a specific sense
        general_examples = examples_by_sense.get(0, [])
        if general_examples:
            html_parts.append('<div class="examples general-examples">')
            html_parts.append(render_examples(general_examples, entries_dict, relative_path))
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
            html_parts.append(render_examples(examples, entries_dict, relative_path))
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
