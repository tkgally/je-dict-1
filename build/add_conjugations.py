#!/usr/bin/env python3
"""Batch-add conjugation fields to verb entries missing them.

This script processes entries in ID order and adds conjugation data based on
the verb class. It uses heuristics + a known-godan list for ambiguous -ru verbs.

Usage:
    python3 build/add_conjugations.py --start 00001 --end 00499 [--dry-run]
"""

import json
import os
import re
import sys
import argparse
from datetime import datetime, timezone


# Known godan verbs ending in -iru/-eru (ambiguous cases)
KNOWN_GODAN_RU = {
    "あまる", "いる", "かえる", "はしる", "しる", "はいる", "きる", "へる",
    "ちる", "ける", "ねる", "にぎる", "かぎる", "すべる", "あせる",
    "しゃべる", "てる", "とがる", "ひねる", "まいる", "ほる",
    # Add readings for specific entries
    "かたむく",  # not -ru but included for safety
    # Common godan -ru
    "なる", "のる", "おる", "とる", "つる", "よる", "わたる", "まわる",
    "おくる", "かかる", "さわる", "つくる", "うつる", "かわる", "まもる",
    "もどる", "おこる", "うまる", "こまる", "とまる", "はかる", "はまる",
    "あたる", "あずかる", "うかる", "おわる", "かぶる", "くだる", "くばる",
    "さがる", "しばる", "しまる", "すわる", "たまる", "ちぎる", "つまる",
    "てらす", "なおる", "ながる", "なぐる", "ねばる", "はかどる", "ひかる",
    "ふとる", "まぎる", "まさる", "まざる", "みなぎる", "むしる", "めぐる",
    "もる", "やぶる", "わかる", "いじる", "いばる", "うなる", "えぐる",
    "おどる", "かじる", "かする", "くもる", "けずる", "こする", "こる",
    "さえぎる", "ざる", "しげる", "しぼる", "すぎる",  # すぎる is actually ichidan
    "そる", "つぶる", "なめる",  # なめる is ichidan
    "にごる", "のぼる", "ひる", "ふる", "まじる", "みのる", "もぐる",
    "よみがえる", "ゆする",
}

# Override: these -ru verbs are definitely ichidan
KNOWN_ICHIDAN_RU = {
    "たべる", "みる", "おきる", "ねる", "いる", "でる", "あげる", "さげる",
    "つける", "あける", "しめる", "いれる", "でかける", "きえる", "みえる",
    "おしえる", "かんがえる", "つたえる", "こたえる", "まける", "うける",
    "わすれる", "おぼえる", "あつめる", "はじめる", "つづける", "やめる",
    "きめる", "たすける", "とめる", "かえる",  # 変える is ichidan
    "ふえる", "へる",  # 減る is godan, but 経る can be ichidan...
    "くれる", "うまれる", "たおれる", "こわれる", "われる", "きれる",
    "ぬれる", "はれる", "かれる", "つかれる", "よごれる", "おくれる",
    "かたづける", "にげる", "のせる", "むける", "よせる",
}


def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract_furigana_text(headword):
    """Extract plain reading from headword with furigana notation."""
    # {漢字|かんじ} → かんじ, plain kana stays
    result = ""
    i = 0
    while i < len(headword):
        if headword[i] == '{':
            # Find the pipe and closing brace
            pipe = headword.index('|', i)
            close = headword.index('}', pipe)
            result += headword[pipe+1:close]
            i = close + 1
        elif headword[i] == '⟦':
            # Skip inline links
            close = headword.index('⟧', i)
            i = close + 1
        else:
            result += headword[i]
            i += 1
    return result


def is_verb_entry(data):
    """Check if an entry is a verb."""
    pos = data.get('part_of_speech', '').lower()
    tags = data.get('metadata', {}).get('tags', {})
    verb_class = tags.get('verb_class', '')
    pos_tags = tags.get('pos', [])

    # Use word-boundary-aware checks to avoid matching "adverb" as "verb"
    import re
    for indicator in ['godan', 'ichidan', 'suru verb', 'suru-verb', 'verb (suru)', 'kuru', 'verbal']:
        if indicator in pos:
            return True
    # Check for "verb" but not "adverb"
    if re.search(r'(?<!ad)verb', pos):
        return True
    if isinstance(pos_tags, list):
        for t in pos_tags:
            if re.search(r'(?<!ad)verb', t.lower()):
                return True
    if verb_class:
        return True
    return False


def determine_verb_class(data):
    """Determine verb class from entry data. Returns (type, details) or None."""
    pos = data.get('part_of_speech', '').lower()
    headword = data.get('headword', '')
    reading = data.get('reading', '')
    tags = data.get('metadata', {}).get('tags', {})
    verb_class_tag = tags.get('verb_class', '')

    # Check for ある special case
    if reading == 'ある' and headword == 'ある':
        return ('aru', {})

    # Check for する itself
    if reading == 'する' and (headword == 'する' or headword == '{為|す}る'):
        return ('suru', {'prefix': ''})

    # Check for 来る itself
    if reading == 'くる' and ('{来|く}る' in headword or headword == 'くる'):
        return ('kuru', {'prefix': ''})

    # Check for 行く (irregular te/ta forms)
    if reading == 'いく' and '{行|い}く' in headword:
        stem = '{行|い}'
        return ('godan', {
            'ending': 'く',
            'stem': stem,
            'overrides': {
                "te_affirmative": f"{stem}って",
                "past_affirmative": f"{stem}った",
                "past_negative": f"{stem}かなかった",
                "conditional_tara_affirmative": f"{stem}ったら",
                "conditional_tara_negative": f"{stem}かなかったら",
                "progressive_present_affirmative": f"{stem}っている",
                "progressive_present_negative": f"{stem}っていない",
                "progressive_present_polite_affirmative": f"{stem}っています",
                "progressive_present_polite_negative": f"{stem}っていません",
                "progressive_past_affirmative": f"{stem}っていた",
                "progressive_past_negative": f"{stem}っていなかった",
                "progressive_past_polite_affirmative": f"{stem}っていました",
                "progressive_past_polite_negative": f"{stem}っていませんでした"
            }
        })

    # Check for くれる (irregular imperative: くれ not くれろ)
    if reading == 'くれる' and (headword == 'くれる' or headword == '{呉|く}れる'):
        stem = headword[:-1]  # Remove る → くれ or {呉|く}れ
        return ('ichidan', {
            'stem': stem,
            'overrides': {
                "imperative_affirmative": stem
            }
        })

    # Check for いらっしゃる, おっしゃる, くださる, なさる (irregular ます forms)
    if reading in ('いらっしゃる', 'おっしゃる', 'くださる', 'なさる'):
        stem = headword[:-1]  # Remove る
        # The ます stem uses い instead of り
        masu_stem = stem[:-1] + 'い' if stem[-1] == 'り' else stem + 'い'
        # For kana-only verbs
        reading_stem = reading[:-1]
        reading_masu = reading_stem[:-1] + 'い'
        if headword == reading:
            # Kana-only
            return ('godan', {
                'ending': 'る',
                'stem': reading_stem,
                'overrides': {
                    "present_polite_affirmative": reading_masu + 'ます',
                    "past_polite_affirmative": reading_masu + 'ました',
                    "present_polite_negative": reading_masu + 'ません',
                    "past_polite_negative": reading_masu + 'ませんでした',
                    "volitional_polite": reading_masu + 'ましょう'
                }
            })
        return ('godan', {
            'ending': 'る',
            'stem': stem,
            'overrides': {
                "present_polite_affirmative": masu_stem + 'ます',
                "past_polite_affirmative": masu_stem + 'ました',
                "present_polite_negative": masu_stem + 'ません',
                "past_polite_negative": masu_stem + 'ませんでした',
                "volitional_polite": masu_stem + 'ましょう'
            }
        })

    # Check for suru verbs via POS tags
    pos_tags = tags.get('pos', [])
    if isinstance(pos_tags, list):
        for pt in pos_tags:
            if 'verb-suru' in pt.lower() or 'suru' in pt.lower():
                prefix = headword[:-2] if headword.endswith('する') else headword
                return ('suru', {'prefix': prefix})

    # Check for suru verbs via POS string
    suru_indicators = ['suru verb', 'suru-verb', 'verb (suru)', 'verb-suru', 'verb (する)', 'verbal', 'する-verb', 'する verb', 'noun (する)']
    is_suru = any(ind in pos for ind in suru_indicators)
    if is_suru or headword.endswith('する'):
        # Extract prefix (everything before する)
        if headword.endswith('する'):
            prefix = headword[:-2]
        else:
            # The headword might not end in する if POS says suru
            # In that case, the prefix is the whole headword
            prefix = headword
        return ('suru', {'prefix': prefix})

    # Check for kuru compounds
    if 'kuru' in pos or headword.endswith('{来|く}る') or headword.endswith('くる'):
        if headword.endswith('{来|く}る'):
            prefix = headword[:-len('{来|く}る')]
        elif headword.endswith('くる'):
            prefix = headword[:-2]
        else:
            prefix = ''
        return ('kuru', {'prefix': prefix})

    # Check explicit verb class tag
    if verb_class_tag:
        if verb_class_tag.startswith('godan'):
            pass  # Fall through to godan detection
        elif verb_class_tag == 'ichidan':
            # Extract stem (everything before る)
            stem = headword[:-1]  # Remove る
            return ('ichidan', {'stem': stem})
        elif verb_class_tag == 'suru':
            prefix = headword[:-2] if headword.endswith('する') else headword
            return ('suru', {'prefix': prefix})
        elif verb_class_tag == 'kuru':
            return ('kuru', {'prefix': ''})

    # Explicit godan/ichidan in POS
    is_godan = any(x in pos for x in ['godan', '五段', 'verb-godan'])
    is_ichidan = any(x in pos for x in ['ichidan', '一段', 'verb-ichidan'])

    if is_godan:
        # Extract ending (last kana of reading) and stem
        ending = reading[-1]
        # Verify ending is a valid godan ending
        valid_endings = 'うくぐすつぬぶむる'
        if ending not in valid_endings:
            return None  # Not a conjugatable verb form (might be noun form)
        stem = headword[:-1]  # Remove last character (the ending kana)
        return ('godan', {'ending': ending, 'stem': stem})

    if is_ichidan:
        stem = headword[:-1]  # Remove る
        return ('ichidan', {'stem': stem})

    # Generic "verb" or "expression, verb" or "verb phrase" — need to determine class
    if 'verb' in pos or 'expression' in pos:
        # Check if ending is unambiguously godan
        if reading and reading[-1] in 'うくぐすつぬぶむ':
            ending = reading[-1]
            stem = headword[:-1]
            return ('godan', {'ending': ending, 'stem': stem})

        if reading and reading[-1] == 'る':
            # Ambiguous -ru verb - check known lists
            if reading in KNOWN_GODAN_RU:
                stem = headword[:-1]
                return ('godan', {'ending': 'る', 'stem': stem})

            # Check if the kana before る is in あ/う/お row → likely godan
            if len(reading) >= 2:
                prev_kana = reading[-2]
                a_row = 'あかがさざただなはばぱまやらわ'
                u_row = 'うくぐすずつづぬふぶぷむゆる'
                o_row = 'おこごそぞとどのほぼぽもよろを'

                if prev_kana in a_row or prev_kana in u_row or prev_kana in o_row:
                    # Likely godan
                    stem = headword[:-1]
                    return ('godan', {'ending': 'る', 'stem': stem})

                # e-row before る → almost always ichidan
                e_row = 'えけげせぜてでねへべぺめれ'
                if prev_kana in e_row:
                    stem = headword[:-1]
                    return ('ichidan', {'stem': stem})

                # i-row before る → could be either, default ichidan unless in known godan
                i_row = 'いきぎしじちぢにひびぴみり'
                if prev_kana in i_row:
                    # Default to ichidan for unknown -iru verbs
                    stem = headword[:-1]
                    return ('ichidan', {'stem': stem})

        return None

    return None


def get_godan_verb_class_tag(ending):
    """Get verb_class tag for godan verb."""
    mapping = {
        'う': 'godan-u', 'く': 'godan-ku', 'ぐ': 'godan-gu',
        'す': 'godan-su', 'つ': 'godan-tsu', 'ぬ': 'godan-nu',
        'ぶ': 'godan-bu', 'む': 'godan-mu', 'る': 'godan-ru'
    }
    return mapping.get(ending, 'godan')


def build_conjugation_field(verb_type, details):
    """Build the conjugation JSON object."""
    if verb_type == 'aru':
        return {"type": "aru"}
    elif verb_type == 'godan':
        result = {
            "type": "godan",
            "ending": details['ending'],
            "stem": details['stem']
        }
        if 'overrides' in details:
            result['overrides'] = details['overrides']
        return result
    elif verb_type == 'ichidan':
        result = {
            "type": "ichidan",
            "stem": details['stem']
        }
        if 'overrides' in details:
            result['overrides'] = details['overrides']
        return result
    elif verb_type == 'suru':
        return {
            "type": "suru",
            "prefix": details['prefix']
        }
    elif verb_type == 'kuru':
        return {
            "type": "kuru",
            "prefix": details['prefix']
        }
    return None


def add_conjugation_to_entry(data, conjugation, verb_class_tag, timestamp):
    """Add conjugation field to entry data, preserving key order."""
    new_data = {}
    for key, value in data.items():
        new_data[key] = value
        if key == 'gloss':
            new_data['conjugation'] = conjugation

    if 'conjugation' not in new_data:
        # gloss not found, add before definitions
        new_data2 = {}
        for key, value in data.items():
            if key == 'definitions':
                new_data2['conjugation'] = conjugation
            new_data2[key] = value
        new_data = new_data2

    # Update verb_class tag
    if 'metadata' in new_data and 'tags' in new_data['metadata']:
        new_data['metadata']['tags']['verb_class'] = verb_class_tag

    # Update timestamp
    if 'metadata' in new_data:
        new_data['metadata']['modified'] = timestamp

    return new_data


def process_entries(start_id, end_id, dry_run=False):
    """Process entries in the given ID range."""
    timestamp = get_timestamp()
    updated = []
    skipped_not_verb = 0
    skipped_has_conj = 0
    flagged = []

    for entry_id in range(start_id, end_id + 1):
        # Find the entry file
        range_dir = f"entries/{(entry_id // 500) * 500:05d}"
        if not os.path.isdir(range_dir):
            continue

        # Find file matching this ID
        prefix = f"{entry_id:05d}_"
        matching = [f for f in os.listdir(range_dir) if f.startswith(prefix) and f.endswith('.json')]

        if not matching:
            continue

        for fname in matching:
            filepath = os.path.join(range_dir, fname)
            with open(filepath) as f:
                data = json.load(f)

            if not is_verb_entry(data):
                skipped_not_verb += 1
                continue

            if 'conjugation' in data:
                skipped_has_conj += 1
                continue

            result = determine_verb_class(data)
            if result is None:
                flagged.append((fname, data.get('headword', ''), data.get('reading', ''), data.get('part_of_speech', '')))
                continue

            verb_type, details = result
            conjugation = build_conjugation_field(verb_type, details)

            # Determine verb_class tag
            if verb_type == 'godan':
                vc_tag = get_godan_verb_class_tag(details['ending'])
            elif verb_type == 'ichidan':
                vc_tag = 'ichidan'
            elif verb_type == 'suru':
                vc_tag = 'suru'
            elif verb_type == 'kuru':
                vc_tag = 'kuru'
            elif verb_type == 'aru':
                vc_tag = 'irregular'
            else:
                vc_tag = ''

            if dry_run:
                print(f"WOULD UPDATE: {fname}: {data.get('headword','')} → type={verb_type}, tag={vc_tag}")
                if verb_type == 'godan':
                    print(f"  stem={details['stem']}, ending={details['ending']}")
                elif verb_type == 'ichidan':
                    print(f"  stem={details['stem']}")
                elif verb_type == 'suru':
                    print(f"  prefix={details['prefix']}")
                updated.append((fname, data.get('headword', ''), verb_type, ''))
            else:
                new_data = add_conjugation_to_entry(data, conjugation, vc_tag, timestamp)
                with open(filepath, 'w') as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=2)
                    f.write('\n')
                updated.append((fname, data.get('headword', ''), verb_type, vc_tag))

    return updated, skipped_not_verb, skipped_has_conj, flagged


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--end', type=int, required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    updated, not_verb, has_conj, flagged = process_entries(args.start, args.end, args.dry_run)

    print(f"\n=== Results ===")
    print(f"Updated: {len(updated)}")
    print(f"Skipped (not verb): {not_verb}")
    print(f"Skipped (has conjugation): {has_conj}")
    print(f"Flagged (ambiguous): {len(flagged)}")

    if flagged:
        print(f"\n=== Flagged entries (need manual review) ===")
        for fname, hw, reading, pos in flagged:
            print(f"  {fname}: {hw} ({reading}) — POS: {pos}")
