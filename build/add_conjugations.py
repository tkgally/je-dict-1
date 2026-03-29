#!/usr/bin/env python3
"""
Add full conjugation tables to verb entries.

This script generates all conjugated forms for each verb and writes them
directly into the entry JSON files. The conjugation data is stored as a
list of form objects, each with a label, affirmative form, and (optionally)
negative form. All forms use furigana notation ({漢字|かんじ}).

Usage:
    python3 build/add_conjugations.py                  # Process all verbs
    python3 build/add_conjugations.py --start 0 --end 500  # ID range
    python3 build/add_conjugations.py --dry-run        # Preview without writing
    python3 build/add_conjugations.py --stats          # Just print statistics

The conjugation field structure written to each entry:

    "conjugation": {
      "type": "godan",          // verb class
      "forms": [
        {"label": "Present", "affirmative": "{読|よ}む", "negative": "{読|よ}まない"},
        {"label": "Present polite", "affirmative": "{読|よ}みます", "negative": "{読|よ}みません"},
        ...
      ]
    }
"""

import json
import sys
import os
import re
import glob
import argparse
from pathlib import Path
from datetime import datetime, timezone

# Ensure build/ is on path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from japanese_utils import strip_furigana

# ── Godan conjugation table ────────────────────────────────────────────────
# Maps dictionary ending → row of conjugation bases
# Columns: a-dan, i-dan, u-dan (dict), e-dan, o-dan, te/ta
_GODAN_ROWS = {
    'う': ('わ', 'い', 'う', 'え', 'お', 'って', 'った'),
    'く': ('か', 'き', 'く', 'け', 'こ', 'いて', 'いた'),
    'ぐ': ('が', 'ぎ', 'ぐ', 'げ', 'ご', 'いで', 'いだ'),
    'す': ('さ', 'し', 'す', 'せ', 'そ', 'して', 'した'),
    'つ': ('た', 'ち', 'つ', 'て', 'と', 'って', 'った'),
    'ぬ': ('な', 'に', 'ぬ', 'ね', 'の', 'んで', 'んだ'),
    'ぶ': ('ば', 'び', 'ぶ', 'べ', 'ぼ', 'んで', 'んだ'),
    'む': ('ま', 'み', 'む', 'め', 'も', 'んで', 'んだ'),
    'る': ('ら', 'り', 'る', 'れ', 'ろ', 'って', 'った'),
}


def _generate_godan_forms(stem: str, ending: str, is_iku: bool = False) -> list:
    """Generate all conjugation forms for a godan verb."""
    if ending not in _GODAN_ROWS:
        return []
    a, i, _u, e, o, te, ta = _GODAN_ROWS[ending]

    # Special case: 行く conjugates て/た as って/った (not いて/いた)
    if is_iku:
        te = 'って'
        ta = 'った'

    return [
        {'label': 'Present', 'affirmative': f'{stem}{ending}', 'negative': f'{stem}{a}ない'},
        {'label': 'Present polite', 'affirmative': f'{stem}{i}ます', 'negative': f'{stem}{i}ません'},
        {'label': 'Past', 'affirmative': f'{stem}{ta}', 'negative': f'{stem}{a}なかった'},
        {'label': 'Past polite', 'affirmative': f'{stem}{i}ました', 'negative': f'{stem}{i}ませんでした'},
        {'label': 'て form', 'affirmative': f'{stem}{te}', 'negative': f'{stem}{a}なくて'},
        {'label': 'ている present', 'affirmative': f'{stem}{te}いる', 'negative': f'{stem}{te}いない'},
        {'label': 'ている polite', 'affirmative': f'{stem}{te}います', 'negative': f'{stem}{te}いません'},
        {'label': 'ている past', 'affirmative': f'{stem}{te}いた', 'negative': f'{stem}{te}いなかった'},
        {'label': 'ている past polite', 'affirmative': f'{stem}{te}いました', 'negative': f'{stem}{te}いませんでした'},
        {'label': 'Conditional ば', 'affirmative': f'{stem}{e}ば', 'negative': f'{stem}{a}なければ'},
        {'label': 'Conditional たら', 'affirmative': f'{stem}{ta}ら', 'negative': f'{stem}{a}なかったら'},
        {'label': 'Volitional', 'affirmative': f'{stem}{o}う', 'negative': None},
        {'label': 'Volitional polite', 'affirmative': f'{stem}{i}ましょう', 'negative': None},
        {'label': 'Potential', 'affirmative': f'{stem}{e}る', 'negative': f'{stem}{e}ない'},
        {'label': 'Passive', 'affirmative': f'{stem}{a}れる', 'negative': f'{stem}{a}れない'},
        {'label': 'Causative', 'affirmative': f'{stem}{a}せる', 'negative': f'{stem}{a}せない'},
        {'label': 'Imperative', 'affirmative': f'{stem}{e}', 'negative': f'{stem}{ending}な'},
    ]


def _generate_ichidan_forms(stem: str) -> list:
    """Generate all conjugation forms for an ichidan verb."""
    s = stem
    return [
        {'label': 'Present', 'affirmative': f'{s}る', 'negative': f'{s}ない'},
        {'label': 'Present polite', 'affirmative': f'{s}ます', 'negative': f'{s}ません'},
        {'label': 'Past', 'affirmative': f'{s}た', 'negative': f'{s}なかった'},
        {'label': 'Past polite', 'affirmative': f'{s}ました', 'negative': f'{s}ませんでした'},
        {'label': 'て form', 'affirmative': f'{s}て', 'negative': f'{s}なくて'},
        {'label': 'ている present', 'affirmative': f'{s}ている', 'negative': f'{s}ていない'},
        {'label': 'ている polite', 'affirmative': f'{s}ています', 'negative': f'{s}ていません'},
        {'label': 'ている past', 'affirmative': f'{s}ていた', 'negative': f'{s}ていなかった'},
        {'label': 'ている past polite', 'affirmative': f'{s}ていました', 'negative': f'{s}ていませんでした'},
        {'label': 'Conditional ば', 'affirmative': f'{s}れば', 'negative': f'{s}なければ'},
        {'label': 'Conditional たら', 'affirmative': f'{s}たら', 'negative': f'{s}なかったら'},
        {'label': 'Volitional', 'affirmative': f'{s}よう', 'negative': None},
        {'label': 'Volitional polite', 'affirmative': f'{s}ましょう', 'negative': None},
        {'label': 'Potential', 'affirmative': f'{s}られる', 'negative': f'{s}られない'},
        {'label': 'Passive', 'affirmative': f'{s}られる', 'negative': f'{s}られない'},
        {'label': 'Causative', 'affirmative': f'{s}させる', 'negative': f'{s}させない'},
        {'label': 'Imperative', 'affirmative': f'{s}ろ', 'negative': f'{s}るな'},
    ]


def _generate_suru_forms(prefix: str) -> list:
    """Generate all conjugation forms for a する compound verb."""
    p = prefix
    return [
        {'label': 'Present', 'affirmative': f'{p}する', 'negative': f'{p}しない'},
        {'label': 'Present polite', 'affirmative': f'{p}します', 'negative': f'{p}しません'},
        {'label': 'Past', 'affirmative': f'{p}した', 'negative': f'{p}しなかった'},
        {'label': 'Past polite', 'affirmative': f'{p}しました', 'negative': f'{p}しませんでした'},
        {'label': 'て form', 'affirmative': f'{p}して', 'negative': f'{p}しなくて'},
        {'label': 'ている present', 'affirmative': f'{p}している', 'negative': f'{p}していない'},
        {'label': 'ている polite', 'affirmative': f'{p}しています', 'negative': f'{p}していません'},
        {'label': 'ている past', 'affirmative': f'{p}していた', 'negative': f'{p}していなかった'},
        {'label': 'ている past polite', 'affirmative': f'{p}していました', 'negative': f'{p}していませんでした'},
        {'label': 'Conditional ば', 'affirmative': f'{p}すれば', 'negative': f'{p}しなければ'},
        {'label': 'Conditional たら', 'affirmative': f'{p}したら', 'negative': f'{p}しなかったら'},
        {'label': 'Volitional', 'affirmative': f'{p}しよう', 'negative': None},
        {'label': 'Volitional polite', 'affirmative': f'{p}しましょう', 'negative': None},
        {'label': 'Potential', 'affirmative': f'{p}できる', 'negative': f'{p}できない'},
        {'label': 'Passive', 'affirmative': f'{p}される', 'negative': f'{p}されない'},
        {'label': 'Causative', 'affirmative': f'{p}させる', 'negative': f'{p}させない'},
        {'label': 'Imperative', 'affirmative': f'{p}しろ', 'negative': f'{p}するな'},
    ]


def _generate_kuru_forms(prefix: str) -> list:
    """Generate all conjugation forms for a 来る verb."""
    p = prefix
    return [
        {'label': 'Present', 'affirmative': f'{p}{{来|く}}る', 'negative': f'{p}{{来|こ}}ない'},
        {'label': 'Present polite', 'affirmative': f'{p}{{来|き}}ます', 'negative': f'{p}{{来|き}}ません'},
        {'label': 'Past', 'affirmative': f'{p}{{来|き}}た', 'negative': f'{p}{{来|こ}}なかった'},
        {'label': 'Past polite', 'affirmative': f'{p}{{来|き}}ました', 'negative': f'{p}{{来|き}}ませんでした'},
        {'label': 'て form', 'affirmative': f'{p}{{来|き}}て', 'negative': f'{p}{{来|こ}}なくて'},
        {'label': 'ている present', 'affirmative': f'{p}{{来|き}}ている', 'negative': f'{p}{{来|き}}ていない'},
        {'label': 'ている polite', 'affirmative': f'{p}{{来|き}}ています', 'negative': f'{p}{{来|き}}ていません'},
        {'label': 'ている past', 'affirmative': f'{p}{{来|き}}ていた', 'negative': f'{p}{{来|き}}ていなかった'},
        {'label': 'ている past polite', 'affirmative': f'{p}{{来|き}}ていました', 'negative': f'{p}{{来|き}}ていませんでした'},
        {'label': 'Conditional ば', 'affirmative': f'{p}{{来|く}}れば', 'negative': f'{p}{{来|こ}}なければ'},
        {'label': 'Conditional たら', 'affirmative': f'{p}{{来|き}}たら', 'negative': f'{p}{{来|こ}}なかったら'},
        {'label': 'Volitional', 'affirmative': f'{p}{{来|こ}}よう', 'negative': None},
        {'label': 'Volitional polite', 'affirmative': f'{p}{{来|き}}ましょう', 'negative': None},
        {'label': 'Potential', 'affirmative': f'{p}{{来|こ}}られる', 'negative': f'{p}{{来|こ}}られない'},
        {'label': 'Passive', 'affirmative': f'{p}{{来|こ}}られる', 'negative': f'{p}{{来|こ}}られない'},
        {'label': 'Causative', 'affirmative': f'{p}{{来|こ}}させる', 'negative': f'{p}{{来|こ}}させない'},
        {'label': 'Imperative', 'affirmative': f'{p}{{来|こ}}い', 'negative': f'{p}{{来|く}}るな'},
    ]


def _generate_zuru_forms(stem: str) -> list:
    """Generate all conjugation forms for a ずる verb (e.g., 断ずる → 断じる).

    ずる verbs are classical forms that conjugate with a じ stem in modern Japanese.
    The stem parameter is the part before ずる (e.g., {断|だん} for 断ずる).
    """
    s = stem
    return [
        {'label': 'Present', 'affirmative': f'{s}じる', 'negative': f'{s}じない'},
        {'label': 'Present polite', 'affirmative': f'{s}じます', 'negative': f'{s}じません'},
        {'label': 'Past', 'affirmative': f'{s}じた', 'negative': f'{s}じなかった'},
        {'label': 'Past polite', 'affirmative': f'{s}じました', 'negative': f'{s}じませんでした'},
        {'label': 'て form', 'affirmative': f'{s}じて', 'negative': f'{s}じなくて'},
        {'label': 'ている present', 'affirmative': f'{s}じている', 'negative': f'{s}じていない'},
        {'label': 'ている polite', 'affirmative': f'{s}じています', 'negative': f'{s}じていません'},
        {'label': 'ている past', 'affirmative': f'{s}じていた', 'negative': f'{s}じていなかった'},
        {'label': 'ている past polite', 'affirmative': f'{s}じていました', 'negative': f'{s}じていませんでした'},
        {'label': 'Conditional ば', 'affirmative': f'{s}じれば', 'negative': f'{s}じなければ'},
        {'label': 'Conditional たら', 'affirmative': f'{s}じたら', 'negative': f'{s}じなかったら'},
        {'label': 'Volitional', 'affirmative': f'{s}じよう', 'negative': None},
        {'label': 'Volitional polite', 'affirmative': f'{s}じましょう', 'negative': None},
        {'label': 'Potential', 'affirmative': f'{s}じられる', 'negative': f'{s}じられない'},
        {'label': 'Passive', 'affirmative': f'{s}じられる', 'negative': f'{s}じられない'},
        {'label': 'Causative', 'affirmative': f'{s}じさせる', 'negative': f'{s}じさせない'},
        {'label': 'Imperative', 'affirmative': f'{s}じろ', 'negative': f'{s}じるな'},
    ]


def _generate_aru_forms() -> list:
    """Generate conjugation forms for ある (limited set — no passive/causative/etc.)."""
    return [
        {'label': 'Present', 'affirmative': 'ある', 'negative': 'ない'},
        {'label': 'Present polite', 'affirmative': 'あります', 'negative': 'ありません'},
        {'label': 'Past', 'affirmative': 'あった', 'negative': 'なかった'},
        {'label': 'Past polite', 'affirmative': 'ありました', 'negative': 'ありませんでした'},
        {'label': 'て form', 'affirmative': 'あって', 'negative': 'なくて'},
        {'label': 'Conditional ば', 'affirmative': 'あれば', 'negative': 'なければ'},
        {'label': 'Conditional たら', 'affirmative': 'あったら', 'negative': 'なかったら'},
    ]


# ── Verb type detection ────────────────────────────────────────────────────

# Furigana pattern: {漢字|かんじ}
FURIGANA_RE = re.compile(r'\{([^|{}]+)\|([^|{}]+)\}')


def _detect_verb_type(entry: dict) -> tuple:
    """
    Detect verb type and extract stem/ending/prefix from an entry.

    Returns: (verb_type, details_dict) or (None, None) if not a verb.
    verb_type is one of: 'godan', 'ichidan', 'suru', 'kuru', 'aru'
    details_dict contains keys needed for conjugation generation.
    """
    pos = entry.get('part_of_speech', '').lower()
    headword = entry.get('headword', '')
    reading = entry.get('reading', '')
    tags = entry.get('metadata', {}).get('tags', {})
    verb_class = tags.get('verb_class', '')
    pos_tags = tags.get('pos', [])

    if not any('verb' in p for p in ([pos] + pos_tags)):
        return None, None

    # Check for ある specifically
    if reading == 'ある' and headword == 'ある':
        return 'aru', {}

    # Detect suru verbs
    if ('suru' in pos or 'verb-suru' in pos_tags or verb_class == 'suru'
            or headword.endswith('する') or reading.endswith('する')):
        # Extract prefix (everything before する)
        plain = strip_furigana(headword)
        if plain.endswith('する'):
            prefix = _strip_suffix_from_headword(headword, 'する')
        else:
            # Headword doesn't include する (e.g., がっかり for がっかりする)
            # The entire headword is the prefix
            prefix = headword

        return 'suru', {'prefix': prefix}

    # Detect kuru verbs — strict: only match if POS explicitly says kuru,
    # or headword contains 来る. Do NOT match on reading alone (つくる, おくる are godan).
    plain_hw = strip_furigana(headword)
    is_kuru = ('kuru' in pos and 'godan' not in pos) or 'verb-kuru' in pos_tags or plain_hw.endswith('来る')
    if is_kuru:
        plain = strip_furigana(headword)
        if plain.endswith('来る'):
            prefix = _strip_suffix_from_headword(headword, '{来|く}る')
            if prefix == headword:
                # Try alternate: maybe headword is just 来る
                prefix = _strip_suffix_from_headword(headword, '来る')
                if prefix == headword:
                    prefix = ''
        elif reading.endswith('くる'):
            prefix = _strip_suffix_from_headword(headword, 'くる')
            if prefix == headword:
                prefix = ''
        else:
            prefix = ''
        return 'kuru', {'prefix': prefix}

    # Detect ずる verbs (e.g., 断ずる, 案ずる, 準ずる) — must come before ichidan
    # These are classical verbs that conjugate with a じ stem in modern Japanese.
    # Be careful NOT to match godan verbs that happen to end in ずる (譲る, 削る,
    # 引きずる, さえずる, ぐずる, バズる, etc.) — those are godan-ru verbs.
    # Match only when: POS explicitly says ずる, OR reading ends in ずる and the
    # entry is NOT already tagged as godan.
    if 'ずる' in pos or (
        reading.endswith('ずる')
        and 'godan' not in pos
        and 'verb-godan' not in pos_tags
        and not (verb_class and 'godan' in verb_class)
    ):
        stem = _strip_suffix_from_headword(headword, 'ずる')
        if stem != headword:
            return 'zuru', {'stem': stem}

    # Detect ichidan verbs
    if ('ichidan' in pos or 'verb-ichidan' in pos_tags
            or (verb_class and 'ichidan' in verb_class)):
        # Stem = headword minus final る
        stem = _extract_ichidan_stem(headword, reading)
        if stem is not None:
            return 'ichidan', {'stem': stem}

    # Detect godan verbs
    if ('godan' in pos or 'verb-godan' in pos_tags
            or (verb_class and 'godan' in verb_class)):
        stem, ending = _extract_godan_stem_ending(headword, reading)
        if stem is not None and ending:
            return 'godan', {'stem': stem, 'ending': ending}

    # Fallback: try to detect from reading ending
    if reading and not any(t in pos for t in ['suru', 'kuru', 'ichidan']):
        # Check if it's a godan verb by reading ending
        last_char = reading[-1] if reading else ''
        if last_char in _GODAN_ROWS:
            stem, ending = _extract_godan_stem_ending(headword, reading)
            if stem is not None and ending:
                return 'godan', {'stem': stem, 'ending': ending}

    return None, None


def _strip_suffix_from_headword(headword: str, suffix: str) -> str:
    """Remove a suffix from headword, handling furigana notation."""
    if headword.endswith(suffix):
        return headword[:-len(suffix)]
    # Try stripping without furigana
    plain = strip_furigana(headword)
    plain_suffix = strip_furigana(suffix)
    if plain.endswith(plain_suffix):
        # Need to find where in the original headword the suffix starts
        # Work backwards through the headword
        target_len = len(plain) - len(plain_suffix)
        current_plain_len = 0
        i = 0
        while i < len(headword) and current_plain_len < target_len:
            if headword[i] == '{':
                # Skip furigana notation
                end = headword.index('}', i)
                pipe = headword.index('|', i)
                kanji_len = pipe - i - 1
                current_plain_len += kanji_len
                i = end + 1
            else:
                current_plain_len += 1
                i += 1
        return headword[:i]
    return headword


def _extract_ichidan_stem(headword: str, reading: str) -> str:
    """Extract ichidan verb stem (headword minus final る)."""
    plain = strip_furigana(headword)
    if not plain.endswith('る') or not reading.endswith('る'):
        return None

    # Remove trailing る from headword
    if headword.endswith('る'):
        return headword[:-1]

    # Headword might end with furigana containing る
    # e.g., {食|た}べる → {食|た}べ
    return _strip_suffix_from_headword(headword, 'る')


def _extract_godan_stem_ending(headword: str, reading: str) -> tuple:
    """Extract godan verb stem and ending."""
    if not reading:
        return None, None

    ending = reading[-1]
    if ending not in _GODAN_ROWS:
        return None, None

    # The stem is headword minus the final kana ending
    if headword.endswith(ending):
        stem = headword[:-1]
    else:
        # Headword might end with kanji+furigana that includes the ending
        plain = strip_furigana(headword)
        if plain.endswith(ending):
            stem = _strip_suffix_from_headword(headword, ending)
        else:
            # The ending is part of a furigana group
            # e.g., {行|い}く — ending is く, stem is {行|い}
            stem = _strip_suffix_from_headword(headword, ending)
            if stem == headword:
                return None, None

    return stem, ending


def _detect_passive_headword(entry: dict) -> bool:
    """Check if headword is already in passive form."""
    reading = entry.get('reading', '')
    headword = entry.get('headword', '')
    pos = entry.get('part_of_speech', '').lower()
    notes = entry.get('notes', '')

    # Common passive endings
    if reading.endswith('れる') or reading.endswith('られる'):
        # Check if notes mention passive
        if notes and ('passive' in notes.lower() or '受身' in notes or '受け身' in notes):
            return True
        if 'passive' in pos:
            return True

    return False


def generate_conjugation(entry: dict) -> dict:
    """
    Generate full conjugation data for a verb entry.

    Returns a dict with 'type' and 'forms' keys, or None if not a verb
    or type can't be determined.
    """
    verb_type, details = _detect_verb_type(entry)
    if verb_type is None:
        return None

    if verb_type == 'godan':
        # Detect 行く special case (て form is 行って, not 行いて)
        reading = entry.get('reading', '')
        is_iku = (reading == 'いく' or reading == 'ゆく') and details.get('ending') == 'く'
        forms = _generate_godan_forms(details['stem'], details['ending'], is_iku=is_iku)
    elif verb_type == 'ichidan':
        forms = _generate_ichidan_forms(details['stem'])
    elif verb_type == 'zuru':
        forms = _generate_zuru_forms(details['stem'])
    elif verb_type == 'suru':
        forms = _generate_suru_forms(details['prefix'])
    elif verb_type == 'kuru':
        forms = _generate_kuru_forms(details['prefix'])
    elif verb_type == 'aru':
        forms = _generate_aru_forms()
    else:
        return None

    if not forms:
        return None

    # Suppress passive row if headword is already passive
    if _detect_passive_headword(entry):
        forms = [f for f in forms if f['label'] != 'Passive']

    return {
        'type': verb_type,
        'forms': forms,
    }


def _infer_verb_class_tag(verb_type: str, details: dict) -> str:
    """Infer the verb_class tag value from detected type."""
    if verb_type == 'godan':
        ending = details.get('ending', '')
        ending_map = {
            'う': 'godan-u', 'く': 'godan-ku', 'ぐ': 'godan-gu',
            'す': 'godan-su', 'つ': 'godan-tsu', 'ぬ': 'godan-nu',
            'ぶ': 'godan-bu', 'む': 'godan-mu', 'る': 'godan-ru',
        }
        return ending_map.get(ending, '')
    elif verb_type == 'ichidan':
        return 'ichidan'
    elif verb_type == 'zuru':
        return 'ichidan'
    elif verb_type == 'suru':
        return 'suru'
    elif verb_type == 'kuru':
        return 'kuru'
    elif verb_type == 'aru':
        return 'irregular'
    return ''


def process_entry_file(filepath: str, dry_run: bool = False) -> dict:
    """
    Process a single entry file, adding conjugation data if it's a verb.

    Returns a status dict: {'status': 'added'|'skipped'|'error', 'type': ...}
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            entry = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        return {'status': 'error', 'error': str(e)}

    conjugation = generate_conjugation(entry)
    if conjugation is None:
        return {'status': 'skipped', 'reason': 'not a verb or undetectable type'}

    # Add conjugation field
    entry['conjugation'] = conjugation

    # Ensure verb_class tag is set
    verb_type, details = _detect_verb_type(entry)
    tags = entry.setdefault('metadata', {}).setdefault('tags', {})
    if not tags.get('verb_class') and verb_type:
        vc = _infer_verb_class_tag(verb_type, details)
        if vc:
            tags['verb_class'] = vc

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(entry, f, ensure_ascii=False, indent=2)
            f.write('\n')

    return {'status': 'added', 'type': conjugation['type']}


def main():
    parser = argparse.ArgumentParser(description='Add conjugation data to verb entries')
    parser.add_argument('--start', type=int, default=0, help='Start ID (inclusive)')
    parser.add_argument('--end', type=int, default=99999, help='End ID (inclusive)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--stats', action='store_true', help='Print statistics only')
    parser.add_argument('--force', action='store_true',
                        help='Overwrite existing conjugation data')
    args = parser.parse_args()

    entries_dir = Path(__file__).parent.parent / 'entries'
    files = sorted(glob.glob(str(entries_dir / '**' / '*.json'), recursive=True))

    counts = {'added': 0, 'skipped': 0, 'error': 0, 'already': 0}
    type_counts = {}

    for filepath in files:
        # Extract ID from filename
        basename = os.path.basename(filepath)
        match = re.match(r'^(\d{5})_', basename)
        if not match:
            continue
        entry_id = int(match.group(1))
        if entry_id < args.start or entry_id > args.end:
            continue

        # Check if already has conjugation data
        if not args.force:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if 'conjugation' in data and data['conjugation'].get('forms'):
                    counts['already'] += 1
                    continue
            except (json.JSONDecodeError, OSError):
                pass

        result = process_entry_file(filepath, dry_run=args.dry_run or args.stats)

        if result['status'] == 'added':
            counts['added'] += 1
            vtype = result.get('type', 'unknown')
            type_counts[vtype] = type_counts.get(vtype, 0) + 1
        elif result['status'] == 'skipped':
            counts['skipped'] += 1
        elif result['status'] == 'error':
            counts['error'] += 1
            print(f"  ERROR {filepath}: {result.get('error', '?')}", file=sys.stderr)

    # Print summary
    action = 'Would add' if (args.dry_run or args.stats) else 'Added'
    print(f"\n{action} conjugation to {counts['added']} entries")
    if counts['already']:
        print(f"Already had conjugation: {counts['already']}")
    print(f"Skipped (not verb): {counts['skipped']}")
    if counts['error']:
        print(f"Errors: {counts['error']}")

    if type_counts:
        print("\nBy verb type:")
        for vtype in sorted(type_counts):
            print(f"  {vtype}: {type_counts[vtype]}")


if __name__ == '__main__':
    main()
