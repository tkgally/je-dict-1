#!/usr/bin/env python3
"""Score dictionary entry notes against POS-specific templates.

Reads entries and scores their notes (0-100) on structure, section
coverage, and — since 2026-09 — actual content signals.

RUBRIC (100 points; run with --rubric to print this block)
==========================================================

Structure (40)
  exists      10  notes field is non-empty
  length      10  displayed length vs the template's min_length (pro-rated)
  headers      5  at least one section header
  bullets      5  at least one bullet line (- / ・ / • / * / 1.)
  paragraphs   5  blank-line separation between blocks

Sections (30)  — detected only by header, see "Section detection" below
  required    20  pro-rated over the template's required sections
                  (a template with no required sections gets the full 20)
  optional    10  5 points per distinct optional section present, capped
                  at 10 (the notes skill says one or two optional sections
                  are enough; a template that lists none gets 10)

Furigana (5)
  furigana     5  no bare kanji in the displayed notes text (inline-link
                  base forms ⟦surface→base：id⟧ are never displayed and
                  are ignored)

Content (30)
  content_patterns  10  a section body contains at least one Japanese
                        pattern line: a bullet with kana or kanji in it
  content_contrast  10  a SIMILAR WORDS / RELATED WORDS section (or any of
                        their aliases: CONTRAST, ANTONYM, SYNONYMS, RELATED
                        TERMS, ...) has a line that names a Japanese term
                        and follows it with English
  content_prose     10  at least 120 characters of English prose outside
                        bullets and headers (pro-rated below 120)

Penalties
  bloat       -10  displayed notes longer than 2,000 characters for a
                   single-sense entry or 3,000 for a multi-sense entry
  dup_header   -5  the same standalone section header appears twice
                   (headers that differ only by a parenthetical, e.g.
                   "(sense 1)" and "(sense 2)", are distinct)

The score is clamped to 0..100.

Section detection
-----------------
build/data/note_headers.json is authoritative. A section counts as present
when a header equals its canonical name or one of its aliases —
case-insensitive, whitespace-collapsed, trailing colon ignored. A header is:

  * a block header: an ALL-CAPS line ending in ':' — a parenthetical is
    allowed, e.g. "ASPECT (ている):" or "COMMON COLLOCATIONS (sense 1):".
    A label that is a known canonical/alias is also accepted in other
    casing ("Common collocations:" in legacy notes); an unknown label
    counts as a header only in ALL-CAPS;
  * an inline header: "LABEL: text on the same line", accepted only when
    LABEL is exactly a canonical header or alias ("TRANSITIVITY: transitive",
    "REGISTER: formal, written");
  * a markdown header: "### Label".

Free-text matching is gone (the word "formal" in prose no longer earns
REGISTER credit, "compare" no longer earns SIMILAR WORDS, "error" no longer
earns WATCH OUT). Two content-based fallbacks remain because they are
reliable on their own:

  * TRANSITIVITY: the notes contain 自動詞 or 他動詞, or a line begins with
    "transitive"/"intransitive" (after any bullet marker or inline label);
  * ASPECT (ている): a line contains ている together with an explanation
    (progressive / resultative / state / habitual / ongoing / aspect /
    "means" / "indicates" ...), not merely a pattern that happens to use it.

Template section keys in build/note_templates.json are mapped to canonical
headers through the "template_sections" table of note_headers.json.
"""

import argparse
import json
import os
import re
import sys

# Add build dir to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from japanese_utils import FURIGANA_PATTERN, is_kanji

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEMPLATES_PATH = os.path.join(SCRIPT_DIR, 'note_templates.json')
DEFAULT_HEADERS_PATH = os.path.join(SCRIPT_DIR, 'data', 'note_headers.json')

# Rubric constants (kept in one place so the docstring, the scorer and the
# prioritizer agree).
POINTS = {
    'exists': 10, 'length': 10, 'headers': 5, 'bullets': 5, 'paragraphs': 5,
    'required': 20, 'optional': 10, 'furigana': 5,
    'content_patterns': 10, 'content_contrast': 10, 'content_prose': 10,
}
PENALTY_BLOAT = 10
PENALTY_DUP_HEADER = 5
PROSE_TARGET_CHARS = 120
OPTIONAL_FULL_CREDIT_COUNT = 2          # optional sections needed for the full 10
BLOAT_SINGLE_SENSE = 2000               # displayed characters
BLOAT_MULTI_SENSE = 3000

BREAKDOWN_KEYS = list(POINTS) + ['bloat', 'dup_header']

CONTRAST_SECTIONS = {'SIMILAR WORDS', 'RELATED WORDS'}


def load_templates(templates_path):
    """Load POS note templates from JSON file."""
    try:
        with open(templates_path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {templates_path}: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Canonical headers
# ---------------------------------------------------------------------------

def normalize_header(text):
    """Normalize a header label for alias matching.

    Upper-cases, collapses whitespace, unifies full-width parentheses and
    drops a trailing colon.
    """
    if not text:
        return ''
    t = text.replace('（', '(').replace('）', ')')
    t = re.sub(r'\s+', ' ', t).strip().upper()
    t = t.rstrip(':').strip()
    t = re.sub(r'\s*\(\s*', ' (', t)
    t = re.sub(r'\s*\)', ')', t)
    return t


class HeaderTable:
    """Alias table loaded from build/data/note_headers.json."""

    def __init__(self, data):
        self.canonical = {}          # canonical -> description
        self.alias_map = {}          # normalized label -> canonical
        for canon, info in (data.get('canonical') or {}).items():
            self.canonical[canon] = (info or {}).get('description', '')
            self.alias_map[normalize_header(canon)] = canon
            for alias in (info or {}).get('aliases', []) or []:
                self.alias_map.setdefault(normalize_header(alias), canon)
        self.template_sections = {
            k: v for k, v in (data.get('template_sections') or {}).items()
            if not k.startswith('_')
        }

    def canonical_for(self, label, paren=None):
        """Return the canonical header for a label (+ optional parenthetical), or None."""
        if paren:
            full = self.alias_map.get(normalize_header(f'{label} {paren}'))
            if full:
                return full
        norm = normalize_header(label)
        if norm in self.alias_map:
            return self.alias_map[norm]
        # "ASPECT (ている)" written without a space, or a label that itself
        # carries a parenthetical: try the part before the parenthesis.
        m = re.match(r'^(.*?)\s*\(', norm)
        if m and m.group(1) in self.alias_map:
            return self.alias_map[m.group(1)]
        return None

    def canonical_for_template_section(self, section_key):
        """Map a note_templates.json section key to a canonical header."""
        key = (section_key or '').strip().lower()
        if key in self.template_sections:
            return self.template_sections[key]
        upper = normalize_header(key)
        return self.alias_map.get(upper, upper)


_HEADER_TABLE = None


def load_headers(path=None):
    """Load (and cache) the canonical header table."""
    global _HEADER_TABLE
    if path is None:
        if _HEADER_TABLE is None:
            _HEADER_TABLE = HeaderTable(_read_json(DEFAULT_HEADERS_PATH))
        return _HEADER_TABLE
    return HeaderTable(_read_json(path))


def _read_json(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {path}: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# POS -> template
# ---------------------------------------------------------------------------

def normalize_pos(pos_value):
    """Map a POS value from an entry to a template key.

    Handles the wide variety of legacy POS formats in the dictionary
    by extracting the primary POS category.
    """
    if not pos_value:
        return '_default'

    pos = pos_value.lower().strip()

    # Direct matches first
    direct_keys = [
        'verb-ichidan', 'verb-godan', 'verb-suru', 'verb-kuru',
        'adjective-i', 'adjective-na', 'adjective-no', 'adjective-taru',
        'noun', 'adverb', 'particle', 'counter', 'expression',
    ]
    for key in direct_keys:
        if pos == key:
            if key == 'verb-kuru':
                return 'verb-irregular'
            return key

    # Verb detection — order matters: check specific types before generic
    if any(k in pos for k in ['ichidan', 'verb-ichidan']):
        return 'verb-ichidan'
    if any(k in pos for k in ['godan', 'verb-godan']):
        return 'verb-godan'
    if any(k in pos for k in ['suru verb', 'suru-verb', 'verb-suru', 'verb (suru)', 'verb (する)', 'する verb', 'する-verb']):
        return 'verb-suru'
    if any(k in pos for k in ['verb-kuru', 'kuru compound', 'verb (irregular)', 'verb-irregular']):
        return 'verb-irregular'
    # Word-boundary match: plain substring matching treats "adverb" as a verb.
    if pos.startswith('verb') or re.search(r'\bverb\b', pos.split(',')[0].strip()):
        # Generic verb — try to classify
        if 'intransitive' in pos or 'transitive' in pos:
            return 'verb-godan'  # Default unclassified verbs to godan template
        return 'verb-godan'

    # Adjective detection
    if 'i-adjective' in pos or 'adjective (i' in pos or 'adjective-i' in pos:
        return 'adjective-i'
    if 'na-adjective' in pos or 'adjective (na' in pos or 'adjective-na' in pos or 'な-adjective' in pos or 'adjectival noun' in pos:
        return 'adjective-na'
    if 'no-adjective' in pos or 'adjective (no' in pos or 'adjective-no' in pos or 'の-adjective' in pos:
        return 'adjective-no'
    if 'taru-adjective' in pos or 'adjective-taru' in pos or 'taru adjective' in pos or 'たる-adjective' in pos:
        return '_default'  # taru-adjectives use default
    if pos.startswith('adjective'):
        return 'adjective-na'  # Default unspecified adjectives to na

    # Expression detection
    if 'expression' in pos:
        return 'expression'

    # Counter detection
    if 'counter' in pos:
        return 'counter'

    # Particle detection
    if 'particle' in pos:
        return 'particle'

    # Noun detection (check after compound types that include noun)
    if 'noun' in pos:
        # Check if it's primarily a noun (not "noun, suru verb" which is verb-suru)
        parts = re.split(r'[,;/]', pos)
        primary = parts[0].strip()
        if 'noun' in primary:
            # Check if suru verb is part of the POS
            if any('suru' in p or 'する' in p for p in parts[1:]):
                return 'verb-suru'
            return 'noun'
        return 'noun'

    # Adverb detection
    if 'adverb' in pos:
        return 'adverb'

    # Fallback
    return '_default'


# Structured tags.pos values in the order that picks the most demanding
# template when an entry carries several (e.g. ["noun", "verb-suru"]).
_TAG_POS_PRIORITY = [
    ('verb-ichidan', 'verb-ichidan'), ('verb-godan', 'verb-godan'),
    ('verb-suru', 'verb-suru'), ('verb-kuru', 'verb-irregular'),
    ('verb-irregular', 'verb-irregular'),
    ('adjective-i', 'adjective-i'), ('adjective-na', 'adjective-na'),
    ('adjective-no', 'adjective-no'), ('particle', 'particle'),
    ('counter', 'counter'), ('expression', 'expression'),
    ('adverb', 'adverb'), ('noun', 'noun'),
]


def template_key_for_entry(entry_data):
    """Pick the template key for an entry.

    Prefers the structured metadata.tags.pos list (the schema-validated
    source of truth); falls back to the free-text part_of_speech field.
    """
    meta = entry_data.get('metadata') if isinstance(entry_data.get('metadata'), dict) else {}
    tags = meta.get('tags') if isinstance(meta.get('tags'), dict) else {}
    pos_tags = tags.get('pos') or []
    if isinstance(pos_tags, list) and pos_tags:
        for tag, key in _TAG_POS_PRIORITY:
            if tag in pos_tags:
                return key
    return normalize_pos(entry_data.get('part_of_speech', '') or '')


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

def strip_furigana_text(text):
    """Strip furigana markup from text, keeping kanji only."""
    if not text:
        return ''
    return FURIGANA_PATTERN.sub(r'\1', text)


# Baseform + entry-id tail of an inline word link: ⟦{surface|reading}→baseform：id⟧.
# The baseform is lookup metadata, never rendered, so by spec it carries no
# furigana — it must not count as bare kanji in the display text.
INLINE_LINK_TAIL_PATTERN = re.compile(r'→[^⟧]*⟧')


def has_bare_kanji(text):
    """Check if text contains kanji not covered by furigana markup."""
    if not text:
        return False
    # Drop the non-display tail of inline word links, then furigana-annotated portions
    stripped = INLINE_LINK_TAIL_PATTERN.sub('', text)
    stripped = FURIGANA_PATTERN.sub('', stripped)
    # Check remaining text for kanji
    for char in stripped:
        if is_kanji(char):
            return True
    return False


def display_text(text):
    """What the reader sees: link tails and furigana readings removed."""
    if not text:
        return ''
    t = INLINE_LINK_TAIL_PATTERN.sub('', text).replace('⟦', '')
    return FURIGANA_PATTERN.sub(r'\1', t)


JP_CHAR_RE = re.compile(r'[぀-ヿ㐀-䶿一-鿿豈-﫿々]')
BULLET_RE = re.compile(r'^\s*(?:[-*•・–—]\s*|\d+[.)]\s+)')
MD_HEADER_RE = re.compile(r'^\s*#{1,4}\s+(?P<label>.+?)\s*$')
# Header label (no markup, no colon) + optional parenthetical. Case is checked
# in _header_parts: an unknown label must be ALL-CAPS; a known alias may be
# written in any case ("Common collocations:" in legacy notes).
_LABEL = r'(?P<label>[^\n:{}|⟦⟧→#]{2,60}?)(?P<paren>\s*\([^()\n]*\))?'
BLOCK_HEADER_RE = re.compile(r'^\s*' + _LABEL + r'\s*:\s*$')
INLINE_HEADER_RE = re.compile(r'^\s*' + _LABEL + r'\s*:\s+(?P<rest>\S.*)$')
TRANSITIVITY_LINE_RE = re.compile(r'^\s*(?:in)?transitive\b', re.IGNORECASE)
ASPECT_EXPLAIN_RE = re.compile(
    r'progressive|resultative|resultant|\bstate\b|habitual|ongoing|continu|'
    r'in progress|aspect|currently|ha(?:s|ve) been|\bmeans\b|indicates|'
    r'expresses|describes|refers|implies|ている\s*form',
    re.IGNORECASE)


def _header_parts(line, table):
    """Classify a line as a header.

    Returns (kind, identity, canonical, rest) where kind is 'block',
    'inline' or 'md', identity is the normalized full label (used for the
    duplicate check), canonical is the canonical header or None, and rest is
    the text after an inline header (else '').  Returns None for non-headers.
    """
    m = MD_HEADER_RE.match(line)
    if m:
        label = m.group('label').rstrip(':').strip()
        pm = re.match(r'^(.*?)\s*(\([^()]*\))\s*$', label)
        if pm:
            canon = table.canonical_for(pm.group(1), pm.group(2))
        else:
            canon = table.canonical_for(label)
        return 'md', normalize_header(label), canon, ''

    m = BLOCK_HEADER_RE.match(line)
    kind = 'block'
    if not m:
        m = INLINE_HEADER_RE.match(line)
        kind = 'inline'
    if not m:
        return None
    label = m.group('label').strip()
    paren = (m.group('paren') or '').strip()
    canon = table.canonical_for(label, paren)
    identity = normalize_header(f'{label} {paren}' if paren else label)
    if kind == 'inline':
        # Inline headers are accepted only when the label is a known alias —
        # otherwise "Xを確認する: to confirm X" would look like a header.
        if canon is None:
            return None
        return 'inline', identity, canon, m.group('rest').strip()
    if canon is None:
        # Unknown labels count as headers only in the ALL-CAPS house style.
        if re.search(r'[a-z]', label) or not re.search(r'[A-Z]', label):
            return None
    return 'block', identity, canon, ''


def analyze_notes(notes_text, table=None):
    """Parse notes into headers, sections and content signals.

    Returns a dict with:
      headers        list of (identity, canonical) in order of appearance
      canonicals     set of canonical headers present (by header only)
      sections_found set of canonicals incl. the two content fallbacks
      has_header, has_bullet, has_blank_line, duplicate_header  bools
      pattern_line   a section body has a bullet with Japanese in it
      contrast_line  a SIMILAR/RELATED section names a term and glosses it
      prose_chars    English prose characters outside bullets and headers
      display_len    length of the displayed text
      contrast_terms raw Japanese terms found on contrast lines (for the
                     prioritizer's cross-reference check)
    """
    table = table or load_headers()
    result = {
        'headers': [], 'canonicals': set(), 'sections_found': set(),
        'has_header': False, 'has_bullet': False, 'has_blank_line': False,
        'duplicate_header': False, 'pattern_line': False,
        'contrast_line': False, 'prose_chars': 0, 'display_len': 0,
        'contrast_terms': [],
    }
    if not notes_text or not notes_text.strip():
        return result

    result['display_len'] = len(display_text(notes_text).strip())
    result['has_blank_line'] = '\n\n' in notes_text

    seen_identities = set()
    current = None                # canonical (or '_unknown') of the open section
    in_section = False
    transitivity = '自動詞' in notes_text or '他動詞' in notes_text
    aspect = False
    prose = 0

    for raw in notes_text.split('\n'):
        line = raw.rstrip()
        if not line.strip():
            continue
        header = _header_parts(line, table)
        body_text = None
        if header:
            kind, identity, canon, rest = header
            result['has_header'] = True
            result['headers'].append((identity, canon))
            if kind != 'inline':
                if identity in seen_identities:
                    result['duplicate_header'] = True
                seen_identities.add(identity)
            if canon:
                result['canonicals'].add(canon)
            current = canon or '_unknown'
            in_section = True
            if rest:
                body_text = rest
                is_bullet = False
            else:
                continue
        else:
            is_bullet = bool(BULLET_RE.match(line))
            body_text = BULLET_RE.sub('', line, count=1).strip() if is_bullet else line.strip()
            if is_bullet:
                result['has_bullet'] = True

        shown = display_text(body_text)
        if is_bullet and in_section and JP_CHAR_RE.search(shown):
            result['pattern_line'] = True
        if not is_bullet:
            prose += len(re.sub(r'[^\x20-\x7e]', '', shown).strip())
        if current in CONTRAST_SECTIONS:
            term = _leading_japanese_term(body_text)
            if term:
                result['contrast_line'] = True
                result['contrast_terms'].append(term)
        if not transitivity and TRANSITIVITY_LINE_RE.match(body_text):
            transitivity = True
        if not aspect and ('ている' in body_text or 'でいる' in body_text) \
                and ASPECT_EXPLAIN_RE.search(shown):
            aspect = True

    result['prose_chars'] = prose
    result['sections_found'] = set(result['canonicals'])
    if transitivity:
        result['sections_found'].add('TRANSITIVITY')
    if aspect:
        result['sections_found'].add('ASPECT (ている)')
    return result


LINK_RE = re.compile(r'⟦(?P<surface>[^⟧→]*)→(?P<base>[^⟧：]*)：(?P<id>[^⟧]*)⟧')
_TERM_CHARS = r'[぀-ヿ㐀-䶿一-鿿豈-﫿々ー〜～{}|]'
LEADING_TERM_RE = re.compile(r'^[\s「『(（]*(?P<term>' + _TERM_CHARS + r'+)')


def _leading_japanese_term(text):
    """The Japanese term a contrast line starts with, followed by English.

    Returns the term with markup intact (a ⟦…⟧ link is returned whole), or
    None when the line does not start with Japanese or has no English after
    the term.
    """
    if not text:
        return None
    t = text.lstrip(' \t「『(（〜～')
    if t.startswith('⟦'):
        m = LINK_RE.match(t)
        if not m:
            return None
        term = m.group(0)
        after = t[m.end():]
    else:
        m = LEADING_TERM_RE.match(t)
        if not m:
            return None
        term = m.group('term')
        after = t[m.end():]
    if not JP_CHAR_RE.search(term):
        return None
    after = display_text(after)
    if re.search(r'[A-Za-z]{3,}', after):
        return term
    return None


def find_sections(notes_text, section_names, table=None):
    """Return the subset of template section names present in the notes.

    Detection is header-based (canonical name or alias) plus the two
    content fallbacks for TRANSITIVITY and ASPECT (ている).
    """
    if not notes_text:
        return set()
    table = table or load_headers()
    analysis = analyze_notes(notes_text, table)
    found = set()
    for section in section_names:
        canon = table.canonical_for_template_section(section)
        if canon in analysis['sections_found']:
            found.add(section)
    return found


def bloat_threshold(entry_data):
    """Displayed-length ceiling above which notes count as bloated."""
    senses = entry_data.get('definitions') or entry_data.get('senses') or []
    return BLOAT_MULTI_SENSE if len(senses) > 1 else BLOAT_SINGLE_SENSE


def is_bloated(entry_data, notes_text=None):
    """True when the displayed notes exceed the bloat threshold."""
    notes = entry_data.get('notes', '') if notes_text is None else notes_text
    return len(display_text(notes or '').strip()) > bloat_threshold(entry_data)


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def _empty_breakdown():
    return {k: 0 for k in BREAKDOWN_KEYS}


def score_entry(entry_data, notes_text, template, table=None):
    """Score an entry's notes against its POS template. Returns (score, breakdown)."""
    breakdown = _empty_breakdown()

    # 1. Notes field exists and is non-empty
    if not (notes_text and notes_text.strip()):
        return 0, breakdown
    breakdown['exists'] = POINTS['exists']

    table = table or load_headers()
    analysis = analyze_notes(notes_text, table)

    # 2. Meets minimum length (pro-rated)
    min_len = template.get('min_length', 40) or 1
    ratio = min(1.0, analysis['display_len'] / min_len)
    breakdown['length'] = int(POINTS['length'] * ratio)

    # 3-5. Headers, bullets, blank-line separation
    breakdown['headers'] = POINTS['headers'] if analysis['has_header'] else 0
    breakdown['bullets'] = POINTS['bullets'] if analysis['has_bullet'] else 0
    breakdown['paragraphs'] = POINTS['paragraphs'] if analysis['has_blank_line'] else 0

    # 6. Required sections (pro-rated)
    required = template.get('required_sections', []) or []
    optional = template.get('optional_sections', []) or []
    found = analysis['sections_found']
    required_canon = []
    for s in required:
        c = table.canonical_for_template_section(s)
        if c not in required_canon:
            required_canon.append(c)
    if not required_canon:
        breakdown['required'] = POINTS['required']
    else:
        hits = sum(1 for c in required_canon if c in found)
        breakdown['required'] = int(round(POINTS['required'] * hits / len(required_canon)))

    # 7. Optional sections (2.5 each, capped)
    optional_canon = []
    for s in optional:
        c = table.canonical_for_template_section(s)
        if c not in optional_canon and c not in required_canon:
            optional_canon.append(c)
    if not optional_canon:
        breakdown['optional'] = POINTS['optional']
    else:
        per = POINTS['optional'] / min(len(optional_canon), OPTIONAL_FULL_CREDIT_COUNT)
        hits = sum(1 for c in optional_canon if c in found)
        breakdown['optional'] = min(POINTS['optional'], int(round(per * hits)))

    # 8. Furigana on kanji
    breakdown['furigana'] = 0 if has_bare_kanji(notes_text) else POINTS['furigana']

    # 9. Content
    breakdown['content_patterns'] = POINTS['content_patterns'] if analysis['pattern_line'] else 0
    breakdown['content_contrast'] = POINTS['content_contrast'] if analysis['contrast_line'] else 0
    prose_ratio = min(1.0, analysis['prose_chars'] / PROSE_TARGET_CHARS)
    breakdown['content_prose'] = int(POINTS['content_prose'] * prose_ratio)

    # 10. Penalties
    if analysis['display_len'] > bloat_threshold(entry_data):
        breakdown['bloat'] = -PENALTY_BLOAT
    if analysis['duplicate_header']:
        breakdown['dup_header'] = -PENALTY_DUP_HEADER

    total = sum(breakdown.values())
    total = max(0, min(100, total))
    return total, breakdown


def rubric_text():
    """The rubric block from the module docstring."""
    doc = __doc__ or ''
    start = doc.find('RUBRIC')
    return doc[start:].rstrip() if start >= 0 else doc


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def load_entries(entries_dir='entries'):
    """Load all entry files from the entries directory."""
    entries = []
    for range_dir in sorted(os.listdir(entries_dir)):
        range_path = os.path.join(entries_dir, range_dir)
        if not os.path.isdir(range_path):
            continue
        for fname in sorted(os.listdir(range_path)):
            if not fname.endswith('.json'):
                continue
            fpath = os.path.join(range_path, fname)
            try:
                with open(fpath) as f:
                    data = json.load(f)
                entry_id = fname.replace('.json', '')
                entries.append({
                    'id': entry_id,
                    'data': data,
                    'path': fpath,
                })
            except (json.JSONDecodeError, IOError):
                continue
    return entries


def main():
    parser = argparse.ArgumentParser(description='Score dictionary entry notes against POS templates')
    parser.add_argument('--tier', help='Filter by vocabulary tier (basic, core, general)')
    parser.add_argument('--pos', help='Filter by part of speech (e.g., verb-godan, noun)')
    parser.add_argument('--below', type=int, metavar='N', help='Show only entries scoring below N')
    parser.add_argument('--above', type=int, metavar='N', help='Show only entries scoring above N')
    parser.add_argument('--json', action='store_true', dest='json_output', help='Output as JSON')
    parser.add_argument('--summary', action='store_true', help='Show summary statistics only')
    parser.add_argument('--id', dest='entry_id', help='Score a single entry by ID')
    parser.add_argument('--rubric', action='store_true', help='Print the scoring rubric and exit')
    args = parser.parse_args()

    if args.rubric:
        print(rubric_text())
        return

    templates = load_templates(DEFAULT_TEMPLATES_PATH)
    table = load_headers()

    entries_dir = os.path.join(os.path.dirname(SCRIPT_DIR), 'entries')
    entries = load_entries(entries_dir)

    results = []
    for entry in entries:
        data = entry['data']
        entry_id = entry['id']

        # Filter by ID
        if args.entry_id:
            numeric_id = entry_id.split('_')[0] if '_' in entry_id else entry_id
            if numeric_id != args.entry_id and entry_id != args.entry_id:
                continue

        # Get metadata
        pos = data.get('part_of_speech', '') or ''
        tier = data.get('metadata', {}).get('vocabulary_tier', '') if isinstance(data.get('metadata'), dict) else ''
        headword = data.get('headword', '')

        # Filter by tier
        if args.tier and tier != args.tier:
            continue

        # Filter by POS (match against normalized key)
        template_key = template_key_for_entry(data)
        if args.pos:
            pos_filter = args.pos.lower()
            if template_key != pos_filter and pos_filter not in pos.lower():
                continue

        # Get template
        template = templates.get(template_key, templates['_default'])

        # Score
        notes = data.get('notes', '') or ''
        score, breakdown = score_entry(data, notes, template, table)

        # Filter by score
        if args.below is not None and score >= args.below:
            continue
        if args.above is not None and score <= args.above:
            continue

        row = {
            'id': entry_id,
            'headword': headword,
            'pos': pos,
            'pos_key': template_key,
            'tier': tier,
            'score': score,
            'breakdown': breakdown,
        }
        if args.json_output or args.entry_id:
            row['sections'] = sorted(analyze_notes(notes, table)['sections_found'])
        results.append(row)

    # Sort by score ascending (worst first)
    results.sort(key=lambda r: (r['score'], r['id']))

    if args.json_output:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    if args.summary:
        print_summary(results)
        return

    # Default: tabular output
    if not results:
        print("No entries matched the filters.")
        return

    print(f"{'Score':>5}  {'ID':<22} {'POS':<22} {'Tier':<10} Headword")
    for r in results:
        print(f"{r['score']:>5}  {r['id']:<22} {r['pos_key']:<22} {r['tier']:<10} {r['headword']}")
        if args.entry_id:
            print("       breakdown: " + ", ".join(f"{k}={v}" for k, v in r['breakdown'].items()))
            print("       sections:  " + (", ".join(r['sections']) or '(none)'))

    print(f"\n{len(results)} entries shown.")


def print_summary(results):
    """Print aggregated summary statistics."""
    if not results:
        print("No entries matched the filters.")
        return

    total = len(results)
    scores = [r['score'] for r in results]
    avg = sum(scores) / total

    print("NOTE QUALITY SUMMARY")
    print("====================")
    print()
    print(f"Total entries scored: {total:,}")
    print(f"Average score: {avg:.1f}")
    print()

    # Score distribution
    buckets = [(0, 19), (20, 39), (40, 59), (60, 79), (80, 100)]
    print("Score Distribution:")
    for lo, hi in buckets:
        count = sum(1 for s in scores if lo <= s <= hi)
        pct = 100 * count / total if total else 0
        print(f"  {lo:>3}-{hi:<3}:  {count:>6,} entries ({pct:>5.1f}%)")
    print()

    # Average by POS
    pos_groups = {}
    for r in results:
        key = r['pos_key']
        pos_groups.setdefault(key, []).append(r['score'])

    print("Average by POS:")
    for key in sorted(pos_groups, key=lambda k: sum(pos_groups[k]) / len(pos_groups[k])):
        grp = pos_groups[key]
        grp_avg = sum(grp) / len(grp)
        print(f"  {key:<22} {grp_avg:>5.1f}  ({len(grp):,} entries)")
    print()

    # Average by tier
    tier_groups = {}
    for r in results:
        t = r['tier'] or '(none)'
        tier_groups.setdefault(t, []).append(r['score'])

    print("Average by Tier:")
    for t in ['basic', 'core', 'general', '(none)']:
        if t in tier_groups:
            grp = tier_groups[t]
            grp_avg = sum(grp) / len(grp)
            print(f"  {t:<12} {grp_avg:>5.1f}  ({len(grp):,} entries)")
    print()

    # Bottom 10
    print("Lowest-Scoring Entries (bottom 10):")
    for r in results[:10]:
        print(f"  {r['id']:<26} {r['score']:>3}   {r['pos_key']:<18} {r['tier']}")


if __name__ == '__main__':
    main()
