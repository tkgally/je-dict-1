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
    generate_tts_script,
    generate_goatcounter_script,
    process_word_links as _process_word_links_base,
    plain_japanese_text as _plain_japanese_text_base,
    unwrap_plain_braces,
    semantic_tag_slug,
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


def plain_japanese_text(text: str) -> str:
    """Plain Japanese text: links -> surface form, furigana -> base text."""
    return _plain_japanese_text_base(text, FURIGANA_PATTERN)


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


# ── Conjugation table rendering ──────────────────────────────────────────

# Row group boundaries for visual separators in the table.
_GROUP_LAST_ROWS = {'て form', 'ている past polite', 'Conditional たら', 'Volitional polite',
                     'Adverbial'}


def generate_conjugation_html(conjugation: dict) -> str:
    """
    Generate the <details> HTML block for a conjugation table.

    Works for both verbs and i-adjectives. Reads pre-computed forms from
    the entry's conjugation.forms array.
    Each form has: label, affirmative, negative (may be null).
    """
    forms = conjugation.get('forms', [])
    if not forms:
        return ''

    rows = []
    for form in forms:
        label = form.get('label', '')
        aff = form.get('affirmative', '')
        neg = form.get('negative')

        aff_html = process_furigana(aff) if aff else ''
        neg_html = process_furigana(neg) if neg else '—'
        group_end = ' class="conj-group-end"' if label in _GROUP_LAST_ROWS else ''
        rows.append(
            f'<tr{group_end}>'
            f'<td class="conj-label" lang="en">{html.escape(label)}</td>'
            f'<td class="conj-form">{aff_html}</td>'
            f'<td class="conj-form">{neg_html}</td>'
            f'</tr>'
        )

    table_html = '\n'.join(rows)
    return (
        '<details class="conjugation-details">\n'
        '<summary>Conjugation</summary>\n'
        '<div class="table-wrap">\n'
        '<table class="conjugation-table" lang="ja">\n'
        '<thead><tr>'
        '<th lang="en"></th><th lang="en">Affirmative</th><th lang="en">Negative</th>'
        '</tr></thead>\n'
        f'<tbody>\n{table_html}\n</tbody>\n'
        '</table>\n'
        '</div>\n'
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
            before_text = unwrap_plain_braces(text[last_end:match.start()])
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
        remaining = unwrap_plain_braces(text[last_end:])
        processed_remaining = []
        for char in remaining:
            if is_kanji(char):
                processed_remaining.append(wrap_kanji_in_link(char))
            else:
                processed_remaining.append(html.escape(char))
        parts.append(''.join(processed_remaining))

    return ''.join(parts)


# Notes section labels: an ALL-CAPS line ending in ':' (e.g. "USAGE:",
# "COMMON COLLOCATIONS:") becomes a heading; "USAGE: text..." becomes an
# inline label at the start of its paragraph.
NOTES_LABEL_PATTERN = re.compile(r"^([A-Z][A-Z0-9 /&'()\-]{2,}):(?:\s+(\S.*))?$")
# A short sentence-case label alone on a line ("Common collocations:", "Polite forms:")
# is also a heading, provided it is at most four words and contains no function
# word (so lead-in sentences such as "It can also mean:" stay paragraphs).
NOTES_SUBHEADING_PATTERN = re.compile(r"^([A-Z][a-z][A-Za-z /&'()\-]{1,40}):$")
_LABEL_FUNCTION_WORDS = {'is', 'are', 'can', 'also', 'the', 'a', 'an', 'to', 'of', 'in', 'with',
                         'for', 'and', 'or', 'it', 'this', 'that', 'be', 'as', 'by', 'on', 'has',
                         'have', 'when', 'from', 'used', 'means'}


def _plain_label_heading(line: str):
    """Return the heading text for a sentence-case label line, or None."""
    match = NOTES_SUBHEADING_PATTERN.match(line)
    if not match:
        return None
    words = match.group(1).split()
    if len(words) > 4 or any(w.lower() in _LABEL_FUNCTION_WORDS for w in words):
        return None
    return match.group(1)


# Words kept upper-case when a label is converted to sentence case.
_LABEL_ACRONYMS = {'JLPT', 'NHK', 'SNS', 'TV', 'PC', 'AI', 'IT', 'OK', 'NG', 'TPO', 'ATM',
                   'DIY', 'URL', 'USA', 'UK', 'US', 'CD', 'DVD', 'AC', 'DC',
                   'N1', 'N2', 'N3', 'N4', 'N5'}


def format_notes_label(label: str) -> str:
    """'COMMON COLLOCATIONS' -> 'Common collocations' (acronyms and symbols kept)."""
    words = []
    for i, word in enumerate(label.split(' ')):
        if word in _LABEL_ACRONYMS or not word.replace('-', '').isalpha():
            words.append(word)
        elif i == 0:
            words.append(word[:1] + word[1:].lower())
        else:
            words.append(word.lower())
    return ' '.join(words)


def process_notes_text(text: str, entries_dict: dict = None, relative_path: str = '../../') -> str:
    """
    Process notes text with proper formatting.

    Paragraphs are separated by blank lines. Within a paragraph, bullet lines
    ("- " or "・") become a list, ALL-CAPS label lines ("USAGE:") become
    <h3 class="notes-heading"> headings, and other consecutive lines are joined
    with <br> into one paragraph.

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

    result = []
    text_lines = []   # consecutive plain lines -> one <p>
    list_items = []   # consecutive bullet lines -> one <ul>

    def flush():
        if list_items:
            result.append(f'<ul>{"".join(list_items)}</ul>')
            list_items.clear()
        if text_lines:
            result.append(f'<p>{"<br>".join(text_lines)}</p>')
            text_lines.clear()

    for para in text.split('\n\n'):
        for line in para.split('\n'):
            trimmed = line.strip()
            if not trimmed:
                continue
            if trimmed.startswith('- ') or trimmed.startswith('・'):
                if text_lines:
                    flush()
                content = re.sub(r'^[-・]\s*', '', trimmed)
                list_items.append(f'<li>{process_text(content)}</li>')
                continue
            if list_items:
                flush()
            label_match = NOTES_LABEL_PATTERN.match(trimmed)
            if label_match:
                label = html.escape(format_notes_label(label_match.group(1)))
                rest = label_match.group(2)
                flush()
                if rest:
                    text_lines.append(f'<strong class="notes-label">{label}:</strong> {process_text(rest)}')
                else:
                    result.append(f'<h3 class="notes-heading">{label}</h3>')
                continue
            plain_heading = _plain_label_heading(trimmed)
            if plain_heading:
                flush()
                result.append(f'<h3 class="notes-heading">{html.escape(plain_heading)}</h3>')
                continue
            text_lines.append(process_text(trimmed))
        flush()

    return ''.join(result)


# Badge text for the transitivity tag: (Japanese term, English label)
TRANSITIVITY_BADGES = {
    'transitive': ('他動詞', 'transitive'),
    'intransitive': ('自動詞', 'intransitive'),
    'both': ('自他動詞', 'transitive / intransitive'),
}


def generate_tag_badges(entry: dict, relative_path: str = '../../') -> str:
    """Badges shown under the headword: transitivity, non-neutral formality,
    non-plain politeness, style, domain, and semantic tags (linked to the
    per-tag list pages under tags/)."""
    tags = entry.get('metadata', {}).get('tags', {}) or {}
    badges = []

    transitivity = tags.get('transitivity')
    if transitivity in TRANSITIVITY_BADGES:
        ja, en = TRANSITIVITY_BADGES[transitivity]
        badges.append(f'<span class="badge badge-transitivity"><span lang="ja">{ja}</span> {en}</span>')

    formality = tags.get('formality')
    if formality and formality != 'neutral':
        badges.append(f'<span class="badge badge-formality">{html.escape(formality)}</span>')

    politeness = tags.get('politeness')
    if politeness and politeness != 'plain':
        badges.append(f'<span class="badge badge-politeness">{html.escape(politeness)}</span>')

    for style in tags.get('style') or []:
        badges.append(f'<span class="badge badge-style">{html.escape(style)}</span>')

    for domain in tags.get('domain') or []:
        badges.append(f'<span class="badge badge-domain">{html.escape(domain)}</span>')

    for tag in tags.get('semantic') or []:
        if tag == 'general':
            continue  # uninformative catch-all
        slug = semantic_tag_slug(tag)
        label = html.escape(tag)
        if slug:
            badges.append(f'<a class="badge badge-semantic" href="{relative_path}tags/{slug}.html">{label}</a>')
        else:
            badges.append(f'<span class="badge badge-semantic">{label}</span>')

    if not badges:
        return ''
    return f'<div class="entry-badges">{"".join(badges)}</div>'


def render_examples(examples_list, entries_dict: dict, relative_path: str = '../../'):
    """Render a list of examples as HTML with word links and a read-aloud button."""
    parts = []
    for ex in examples_list:
        japanese = ex.get('japanese', '')
        english = ex.get('english', '')
        notes = ex.get('notes', '')
        # Use process_word_links to handle link markup (falls back to furigana if no links)
        japanese_html = process_word_links(japanese, entries_dict, relative_path)
        notes_html = process_word_links(notes, entries_dict, relative_path) if notes else ''
        # Read-aloud button (hidden by CSS unless a Japanese voice is available; see generate_tts_script)
        tts_button = (
            f'<button type="button" class="tts-btn" data-text="{html.escape(plain_japanese_text(japanese))}" '
            f'title="Listen" aria-label="Listen to this sentence">🔊</button>'
        )
        parts.append(f'''
                <div class="example-item">
                    <div class="example-japanese" lang="ja">{japanese_html}{tts_button}</div>
                    <div class="example-english">{html.escape(english)}</div>
                    {f'<div class="example-notes">{notes_html}</div>' if notes else ''}
                </div>
            ''')
    return ''.join(parts)


def generate_entry_html(entry: dict, entries_dict: dict, readings_to_entries: dict,
                        relative_path: str = '../../', article_map: dict = None) -> str:
    """Generate HTML content for a single entry page.

    Args:
        article_map: Optional dict mapping entry_id to list of articles that reference it.
                     Each article is {"article_id": str, "title": str}.
    """
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
            <h1 class="entry-headword" lang="ja">{process_headword_with_kanji_links(headword, relative_path)}</h1>
            <div class="entry-reading" lang="ja">{html.escape(reading)}</div>
            <div class="entry-pos">{html.escape(entry.get('part_of_speech', ''))}</div>
            <div class="entry-gloss">{html.escape(entry.get('gloss', ''))}</div>
            {generate_tag_badges(entry, relative_path)}
    ''')

    # Prominent see-also (high-visibility cross-references shown inside entry-header, above the border)
    prominent_refs = entry.get('prominent_see_also', [])
    if prominent_refs:
        html_parts.append('<div class="prominent-see-also" lang="ja">')
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

        html_parts.append(f'<span class="prominent-ref-label" lang="en">See also:</span> ')
        html_parts.append(', '.join(ref_links))
        html_parts.append('</div>')

    # Conjugation table (for verb and i-adjective entries with pre-computed forms)
    conjugation = entry.get('conjugation')
    if conjugation and conjugation.get('forms'):
        html_parts.append(generate_conjugation_html(conjugation))

    html_parts.append('</div>')  # Close entry-header

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

    # Article links (bidirectional: entry → article)
    if article_map and entry_id in article_map:
        entry_articles = article_map[entry_id]
        html_parts.append('<div class="entry-articles">')
        html_parts.append('<h2>Related Articles</h2>')
        for art in entry_articles:
            art_path = f"{relative_path}articles/{art['article_id']}.html"
            html_parts.append(
                f'<a href="{art_path}" class="entry-article-link">'
                f'{html.escape(art["title"])}</a>'
            )
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
    html_parts.append(generate_tts_script())
    html_parts.append(generate_goatcounter_script())
    html_parts.append('</body>')
    html_parts.append('</html>')

    return '\n'.join(html_parts)
