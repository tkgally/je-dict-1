#!/usr/bin/env python3
"""Batch-add conjugation fields to verb entries missing them.

Processes entries in ID order, determines verb class, and adds conjugation
data + verb_class tag. Safe to re-run: skips entries that already have
a conjugation field.

Usage:
    python3 build/add_conjugations.py --start 1 --end 21000 [--dry-run]

The script handles most entries automatically but flags ambiguous cases
for manual review. See prompts/polish_verb_conjugations.md for the full
workflow.

POS Detection Notes (from real-world experience):
  - "adverb" contains "verb" — must use boundary-aware matching
  - "noun (verbal)" and "noun; noun (する)" are する verbs
  - "noun, する-verb" uses full-width する
  - Plain "noun" entries may have verb-suru in metadata.tags.pos
  - "expression, verb phrase" entries should get conjugation
  - "expression (proverb)" / "proverb" should NOT get conjugation
  - "expression (verb て-form + いる)" are already conjugated — skip
  - Noun forms of verbs (ending in り, し, etc.) should NOT get conjugation
"""

import json
import os
import re
import argparse
from datetime import datetime, timezone


def get_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def is_verb_entry(data):
    """Check if an entry is a verb that should receive conjugation data.

    Uses both part_of_speech string and metadata.tags.pos array.
    Carefully avoids "adverb" false positives.
    """
    pos = data.get('part_of_speech', '').lower()
    tags = data.get('metadata', {}).get('tags', {})
    verb_class = tags.get('verb_class', '')
    pos_tags = tags.get('pos', [])

    # Explicit verb-related POS substrings (order matters: check specific before generic)
    for indicator in ['godan', 'ichidan', 'suru verb', 'suru-verb', 'verb (suru)',
                       'kuru', 'verbal', 'する-verb', 'する verb', 'noun (する)']:
        if indicator in pos:
            return True

    # Check for "verb" but NOT "adverb" (adverb contains verb!)
    if re.search(r'(?<!ad)verb', pos):
        return True

    # Check tags array for verb-related entries
    if isinstance(pos_tags, list):
        for t in pos_tags:
            if re.search(r'(?<!ad)verb', t.lower()):
                return True

    # Check explicit verb_class tag
    if verb_class:
        return True

    return False


def determine_verb_class(data):
    """Determine verb class from entry data.

    Returns (type, details_dict) or None if ambiguous/not a verb.

    Priority order:
      1. Special cases (ある, する, 来る, 行く, くれる, いらっしゃる-group)
      2. POS tags array (verb-suru, etc.)
      3. POS string for suru/kuru indicators
      4. Explicit godan/ichidan in POS
      5. Reading-based heuristics for generic "verb"
    """
    pos = data.get('part_of_speech', '').lower()
    headword = data.get('headword', '')
    reading = data.get('reading', '')
    tags = data.get('metadata', {}).get('tags', {})
    verb_class_tag = tags.get('verb_class', '')
    pos_tags = tags.get('pos', [])

    # --- Special cases (check before general classification) ---

    # ある — special type with limited conjugation
    if reading == 'ある' and headword == 'ある':
        return ('aru', {})

    # 行く — godan-ku with irregular て/た forms
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

    # くれる — ichidan with irregular imperative (くれ not くれろ)
    if reading == 'くれる' and (headword == 'くれる' or headword == '{呉|く}れる'):
        stem = headword[:-1]  # Remove る
        return ('ichidan', {
            'stem': stem,
            'overrides': {
                "imperative_affirmative": stem
            }
        })

    # いらっしゃる, おっしゃる, くださる, なさる — irregular ます/imperative forms
    # ます stem uses い instead of り (e.g., いらっしゃい not いらっしゃり)
    # Imperative is also stem + い (e.g., いらっしゃい, ください, なさい)
    if reading in ('いらっしゃる', 'おっしゃる', 'くださる', 'なさる'):
        stem = headword[:-1]  # Remove る → いらっしゃ, おっしゃ, くださ, なさ
        masu_stem = stem + 'い'  # いらっしゃい, おっしゃい, ください, なさい
        return ('godan', {
            'ending': 'る',
            'stem': stem,
            'overrides': {
                "present_polite_affirmative": masu_stem + 'ます',
                "past_polite_affirmative": masu_stem + 'ました',
                "present_polite_negative": masu_stem + 'ません',
                "past_polite_negative": masu_stem + 'ませんでした',
                "volitional_polite": masu_stem + 'ましょう',
                "imperative_affirmative": masu_stem
            }
        })

    # する itself
    if reading == 'する' and (headword == 'する' or headword == '{為|す}る'):
        return ('suru', {'prefix': ''})

    # 来る itself
    if reading == 'くる' and ('{来|く}る' in headword or headword == 'くる'):
        return ('kuru', {'prefix': ''})

    # --- Check tags array for suru verbs ---
    # Many entries have POS="noun" but verb-suru in their tags
    if isinstance(pos_tags, list):
        for pt in pos_tags:
            if 'verb-suru' in pt.lower() or 'suru' in pt.lower():
                prefix = headword[:-2] if headword.endswith('する') else headword
                return ('suru', {'prefix': prefix})

    # --- Check POS string for suru verbs ---
    suru_indicators = [
        'suru verb', 'suru-verb', 'verb (suru)', 'verb-suru', 'verb (する)',
        'verbal', 'する-verb', 'する verb', 'noun (する)'
    ]
    if any(ind in pos for ind in suru_indicators) or headword.endswith('する'):
        if headword.endswith('する'):
            prefix = headword[:-2]
        else:
            prefix = headword
        return ('suru', {'prefix': prefix})

    # --- Check for kuru compounds ---
    if 'kuru' in pos or headword.endswith('{来|く}る') or headword.endswith('くる'):
        if headword.endswith('{来|く}る'):
            prefix = headword[:-len('{来|く}る')]
        elif headword.endswith('くる'):
            prefix = headword[:-2]
        else:
            prefix = ''
        return ('kuru', {'prefix': prefix})

    # --- Check explicit verb_class tag ---
    if verb_class_tag:
        if verb_class_tag.startswith('godan'):
            pass  # Fall through to godan detection below
        elif verb_class_tag == 'ichidan':
            return ('ichidan', {'stem': headword[:-1]})
        elif verb_class_tag == 'suru':
            prefix = headword[:-2] if headword.endswith('する') else headword
            return ('suru', {'prefix': prefix})
        elif verb_class_tag == 'kuru':
            return ('kuru', {'prefix': ''})

    # --- Explicit godan/ichidan in POS string ---
    is_godan = any(x in pos for x in ['godan', '五段', 'verb-godan'])
    is_ichidan = any(x in pos for x in ['ichidan', '一段', 'verb-ichidan'])

    if is_godan:
        ending = reading[-1]
        # Guard: verify ending is a valid godan dictionary-form kana
        if ending not in 'うくぐすつぬぶむる':
            return None  # Likely a noun form (e.g., 申し送り ending in り)
        return ('godan', {'ending': ending, 'stem': headword[:-1]})

    if is_ichidan:
        return ('ichidan', {'stem': headword[:-1]})

    # --- Generic "verb" or "expression, verb phrase" — use reading heuristics ---
    if 'verb' in pos or 'expression' in pos:
        if not reading:
            return None

        # Non-る endings are always godan
        if reading[-1] in 'うくぐすつぬぶむ':
            return ('godan', {'ending': reading[-1], 'stem': headword[:-1]})

        if reading[-1] == 'る' and len(reading) >= 2:
            prev_kana = reading[-2]

            # あ/う/お row before る → godan
            godan_rows = 'あかがさざただなはばぱまやらわうくぐすずつづぬふぶぷむゆるおこごそぞとどのほぼぽもよろを'
            if prev_kana in godan_rows:
                return ('godan', {'ending': 'る', 'stem': headword[:-1]})

            # え row before る → almost always ichidan
            e_row = 'えけげせぜてでねへべぺめれ'
            if prev_kana in e_row:
                return ('ichidan', {'stem': headword[:-1]})

            # い row before る → usually ichidan, but some are godan
            # Default to ichidan; known godan exceptions should be handled
            # by the verb_class tag or explicit POS
            i_row = 'いきぎしじちぢにひびぴみり'
            if prev_kana in i_row:
                return ('ichidan', {'stem': headword[:-1]})

        return None

    return None


def get_godan_verb_class_tag(ending):
    """Get verb_class tag for godan verb."""
    return {
        'う': 'godan-u', 'く': 'godan-ku', 'ぐ': 'godan-gu',
        'す': 'godan-su', 'つ': 'godan-tsu', 'ぬ': 'godan-nu',
        'ぶ': 'godan-bu', 'む': 'godan-mu', 'る': 'godan-ru'
    }.get(ending, 'godan')


def build_conjugation_field(verb_type, details):
    """Build the conjugation JSON object."""
    if verb_type == 'aru':
        return {"type": "aru"}
    elif verb_type == 'godan':
        result = {"type": "godan", "ending": details['ending'], "stem": details['stem']}
        if 'overrides' in details:
            result['overrides'] = details['overrides']
        return result
    elif verb_type == 'ichidan':
        result = {"type": "ichidan", "stem": details['stem']}
        if 'overrides' in details:
            result['overrides'] = details['overrides']
        return result
    elif verb_type == 'suru':
        return {"type": "suru", "prefix": details['prefix']}
    elif verb_type == 'kuru':
        return {"type": "kuru", "prefix": details['prefix']}
    return None


def add_conjugation_to_entry(data, conjugation, verb_class_tag, timestamp):
    """Add conjugation field to entry data, preserving key order.

    Places conjugation after 'gloss' and before 'definitions'.
    Also sets verb_class tag and updates modified timestamp.
    """
    new_data = {}
    inserted = False
    for key, value in data.items():
        new_data[key] = value
        if key == 'gloss' and not inserted:
            new_data['conjugation'] = conjugation
            inserted = True

    if not inserted:
        # gloss not found — insert before definitions
        new_data2 = {}
        for key, value in data.items():
            if key == 'definitions' and not inserted:
                new_data2['conjugation'] = conjugation
                inserted = True
            new_data2[key] = value
        new_data = new_data2

    # Set verb_class tag
    if 'metadata' in new_data and 'tags' in new_data['metadata']:
        new_data['metadata']['tags']['verb_class'] = verb_class_tag

    # Update timestamp
    if 'metadata' in new_data:
        new_data['metadata']['modified'] = timestamp

    return new_data


def process_entries(start_id, end_id, dry_run=False):
    """Process entries in the given ID range.

    Returns (updated, skipped_not_verb, skipped_has_conj, flagged).
    """
    timestamp = get_timestamp()
    updated = []
    skipped_not_verb = 0
    skipped_has_conj = 0
    flagged = []

    for entry_id in range(start_id, end_id + 1):
        range_dir = f"entries/{(entry_id // 500) * 500:05d}"
        if not os.path.isdir(range_dir):
            continue

        prefix = f"{entry_id:05d}_"
        matching = [f for f in os.listdir(range_dir)
                    if f.startswith(prefix) and f.endswith('.json')]

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
                flagged.append((fname, data.get('headword', ''),
                               data.get('reading', ''),
                               data.get('part_of_speech', '')))
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
                print(f"WOULD UPDATE: {fname}: {data.get('headword', '')} "
                      f"→ type={verb_type}, tag={vc_tag}")
                if verb_type == 'godan':
                    print(f"  stem={details['stem']}, ending={details['ending']}")
                elif verb_type == 'ichidan':
                    print(f"  stem={details['stem']}")
                elif verb_type in ('suru', 'kuru'):
                    print(f"  prefix={details.get('prefix', '')}")
            else:
                new_data = add_conjugation_to_entry(data, conjugation, vc_tag, timestamp)
                with open(filepath, 'w') as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=2)
                    f.write('\n')

            updated.append((fname, data.get('headword', ''), verb_type, vc_tag))

    return updated, skipped_not_verb, skipped_has_conj, flagged


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Add conjugation fields to verb entries missing them.')
    parser.add_argument('--start', type=int, required=True,
                        help='Starting entry ID (inclusive)')
    parser.add_argument('--end', type=int, required=True,
                        help='Ending entry ID (inclusive)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing files')
    args = parser.parse_args()

    updated, not_verb, has_conj, flagged = process_entries(
        args.start, args.end, args.dry_run)

    print(f"\n=== Results ===")
    print(f"Updated: {len(updated)}")
    print(f"Skipped (not verb): {not_verb}")
    print(f"Skipped (has conjugation): {has_conj}")
    print(f"Flagged (ambiguous): {len(flagged)}")

    if flagged:
        print(f"\n=== Flagged entries (need manual review) ===")
        for fname, hw, reading, pos in flagged:
            print(f"  {fname}: {hw} ({reading}) — POS: {pos}")
