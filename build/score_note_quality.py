#!/usr/bin/env python3
"""Score dictionary entry notes against POS-specific templates.

Reads entries and scores their notes (0-100) based on structure,
length, section coverage, and formatting quality.
"""

import argparse
import json
import os
import re
import sys

# Add build dir to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from japanese_utils import FURIGANA_PATTERN, is_kanji


def load_templates(templates_path):
    """Load POS note templates from JSON file."""
    try:
        with open(templates_path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {templates_path}: {e}", file=sys.stderr)
        sys.exit(1)


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


def find_sections(notes_text, section_names):
    """Find which sections are present in the notes text.

    Matches flexibly against section headers:
    - SECTION_NAME: (uppercase with colon)
    - ### Section Name (markdown header)
    - Natural text mentions
    """
    if not notes_text:
        return set()

    found = set()
    notes_lower = notes_text.lower()

    for section in section_names:
        section_lower = section.lower()
        # Build patterns to match
        patterns = [
            # UPPERCASE HEADER: pattern
            re.compile(r'^' + re.escape(section_lower).replace(r'\ ', r'[\s/]+') + r'\s*:', re.MULTILINE | re.IGNORECASE),
            # ### Markdown header
            re.compile(r'^#{1,4}\s+' + re.escape(section_lower).replace(r'\ ', r'[\s/]+'), re.MULTILINE | re.IGNORECASE),
        ]

        # Special variant matching
        variants = {
            'transitivity': [r'transitiv', r'transitive/intransitive', r'{自動詞', r'{他動詞', r'intransitive\b', r'\btransitive\b'],
            'common patterns': [r'common pattern', r'patterns?:'],
            'aspect': [r'aspect', r'ている', r'te-iru', r'te iru'],
            'usage': [r'usage', r'how to use', r'using\b'],
            'functions': [r'function', r'uses?:'],
            'counting patterns': [r'count', r'counting'],
            'similar verbs': [r'similar verb', r'related verb', r'compare'],
            'similar adjectives': [r'similar adj', r'compare'],
            'similar words': [r'similar word', r'related word', r'compare'],
            'similar adverbs': [r'similar adverb', r'compare'],
            'similar expressions': [r'similar express', r'compare'],
            'similar counters': [r'similar counter', r'compare'],
            'collocations': [r'collocation', r'common combination'],
            'common expressions': [r'common express', r'common phrase'],
            'compounds': [r'compound'],
            'cultural context': [r'cultural', r'culture'],
            'register': [r'register', r'formality', r'formal', r'informal', r'polite'],
            'forms': [r'forms?:', r'conjugat'],
            'predicate vs. modifier': [r'predicate', r'modifier', r'predicative'],
            'negative usage': [r'negative', r'ない form'],
            'keigo': [r'keigo', r'honorific', r'humble', r'polite form'],
            'particles': [r'particle'],
            'contrasts': [r'contrast', r'vs\.?\s', r'difference'],
            'common mistakes': [r'common mistake', r'mistake', r'error', r'confusion'],
            'position in sentence': [r'position', r'word order', r'placement'],
            'range': [r'range', r'how many', r'extent'],
            'exceptions': [r'exception', r'irregular'],
            'usage context': [r'usage context', r'when to use', r'context'],
            'formality': [r'formality', r'formal', r'casual'],
        }

        for pat in patterns:
            if pat.search(notes_text):
                found.add(section)
                break
        else:
            # Try variant patterns
            if section_lower in variants:
                for variant in variants[section_lower]:
                    if re.search(variant, notes_lower):
                        found.add(section)
                        break

    return found


def score_entry(entry_data, notes_text, template):
    """Score an entry's notes against its POS template. Returns (score, breakdown)."""
    breakdown = {}
    total = 0

    # 1. Notes field exists and is non-empty (10 points)
    if notes_text and notes_text.strip():
        breakdown['exists'] = 10
        total += 10
    else:
        breakdown['exists'] = 0
        breakdown['length'] = 0
        breakdown['headers'] = 0
        breakdown['bullets'] = 0
        breakdown['paragraphs'] = 0
        breakdown['required'] = 0
        breakdown['optional'] = 0
        breakdown['furigana'] = 0
        return 0, breakdown

    clean_text = strip_furigana_text(notes_text).strip()
    text_len = len(clean_text)

    # 2. Meets minimum length (15 points)
    min_len = template.get('min_length', 40)
    if text_len >= min_len:
        breakdown['length'] = 15
        total += 15
    else:
        # Partial credit proportional to how close
        ratio = text_len / min_len if min_len > 0 else 1
        pts = int(15 * ratio)
        breakdown['length'] = pts
        total += pts

    # 3. Has section headers (10 points)
    has_headers = bool(re.search(r'^[A-Z][A-Z /().-]+:', notes_text, re.MULTILINE)) or \
                  bool(re.search(r'^#{1,4}\s+', notes_text, re.MULTILINE))
    if has_headers:
        breakdown['headers'] = 10
        total += 10
    else:
        breakdown['headers'] = 0

    # 4. Has bullet points (10 points)
    if '\n- ' in notes_text or notes_text.startswith('- '):
        breakdown['bullets'] = 10
        total += 10
    else:
        breakdown['bullets'] = 0

    # 5. Has paragraph breaks (5 points)
    if '\n\n' in notes_text:
        breakdown['paragraphs'] = 5
        total += 5
    else:
        breakdown['paragraphs'] = 0

    # 6. Required sections (30 points)
    required = template.get('required_sections', [])
    optional = template.get('optional_sections', [])
    all_sections = required + optional
    found_sections = find_sections(notes_text, all_sections)

    if not required:
        breakdown['required'] = 30
        total += 30
    else:
        per_section = 30 / len(required)
        found_required = sum(1 for s in required if s in found_sections)
        pts = int(per_section * found_required)
        breakdown['required'] = pts
        total += pts

    # 7. Optional sections (15 points)
    if not optional:
        breakdown['optional'] = 15
        total += 15
    else:
        per_section = 15 / len(optional)
        found_optional = sum(1 for s in optional if s in found_sections)
        pts = min(15, int(per_section * found_optional))
        breakdown['optional'] = pts
        total += pts

    # 8. Furigana on kanji (5 points)
    if not has_bare_kanji(notes_text):
        breakdown['furigana'] = 5
        total += 5
    else:
        breakdown['furigana'] = 0

    return total, breakdown


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
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_path = os.path.join(script_dir, 'note_templates.json')
    templates = load_templates(templates_path)

    entries_dir = os.path.join(os.path.dirname(script_dir), 'entries')
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
        pos = data.get('part_of_speech', '')
        tier = data.get('metadata', {}).get('vocabulary_tier', '') if isinstance(data.get('metadata'), dict) else ''
        headword = data.get('headword', '')

        # Filter by tier
        if args.tier and tier != args.tier:
            continue

        # Filter by POS (match against normalized key)
        template_key = normalize_pos(pos)
        if args.pos:
            pos_filter = args.pos.lower()
            if template_key != pos_filter and pos_filter not in pos.lower():
                continue

        # Get template
        template = templates.get(template_key, templates['_default'])

        # Score
        notes = data.get('notes', '') or ''
        score, breakdown = score_entry(data, notes, template)

        # Filter by score
        if args.below is not None and score >= args.below:
            continue
        if args.above is not None and score <= args.above:
            continue

        results.append({
            'id': entry_id,
            'headword': headword,
            'pos': pos,
            'pos_key': template_key,
            'tier': tier,
            'score': score,
            'breakdown': breakdown,
        })

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
