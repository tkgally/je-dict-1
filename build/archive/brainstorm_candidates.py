#!/usr/bin/env python3
"""
Brainstorm new dictionary candidates via OpenRouter LLM API.

This script manages the brainstorming data file and calls an external LLM
to discover candidate words for the je-dict-1 dictionary.

Usage:
    python3 build/brainstorm_candidates.py init                    # Create/update brainstorming data file
    python3 build/brainstorm_candidates.py brainstorm -n 5         # Run 5 brainstorming batches
    python3 build/brainstorm_candidates.py stats                   # Show statistics
    python3 build/brainstorm_candidates.py reset-checked           # Reset all checked flags
    python3 build/brainstorm_candidates.py add-results             # Add results to candidate_words.json

Configuration is passed via command-line arguments (model, temperature, etc.)
and the OPENROUTER_API_KEY environment variable.
"""

import argparse
import json
import os
import random
import re
import sys
import time

import requests

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ENTRIES_INDEX = os.path.join(PROJECT_ROOT, 'entries_index.json')
CANDIDATES_FILE = os.path.join(PROJECT_ROOT, 'candidate_words.json')
BRAINSTORM_DATA = os.path.join(PROJECT_ROOT, 'prompts',
                               'entries-and-candidates-for-brainstorming.md')
OLD_BRAINSTORM_DATA = os.path.join(PROJECT_ROOT, 'brainstorming',
                                   'entries_and_candidates_for_LLM_brainstorming_old.json')
RESULTS_FILE = os.path.join(PROJECT_ROOT, 'prompts', 'brainstorm_results.json')
CHECKED_SEEDS_FILE = os.path.join(PROJECT_ROOT, 'brainstorming', 'checked_seeds.json')

sys.path.insert(0, SCRIPT_DIR)
from japanese_utils import normalize_reading, strip_furigana


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def load_checked_seeds():
    """Load the persistent set of checked seed (headword, reading) pairs.

    This file is committed to the repo so checked state survives across
    sessions, even when the large brainstorm data file is gitignored.
    """
    if os.path.exists(CHECKED_SEEDS_FILE):
        try:
            data = load_json(CHECKED_SEEDS_FILE)
            return {(item[0], item[1]) for item in data}
        except (json.JSONDecodeError, TypeError, IndexError):
            return set()
    return set()


def save_checked_seeds(checked_set):
    """Persist the checked seed set to a committed JSON file."""
    os.makedirs(os.path.dirname(CHECKED_SEEDS_FILE), exist_ok=True)
    data = sorted([list(pair) for pair in checked_set])
    save_json(CHECKED_SEEDS_FILE, data)


# ---------------------------------------------------------------------------
# Flexible deduplication
# ---------------------------------------------------------------------------

def normalize_headword(hw):
    """Normalize a headword for comparison."""
    hw = strip_furigana(hw)
    # Strip leading/trailing wave dash variants
    hw = hw.strip('〜～~')
    return hw


def normalize_for_dedup(headword, reading):
    """
    Generate a set of normalized (headword, reading) tuples for flexible
    matching.  This catches:
      - furigana notation in headwords
      - katakana vs hiragana readings
      - leading/trailing 〜 / ～ / ~ marks
      - kana-only vs kanji headword when reading matches
    """
    forms = set()
    hw = normalize_headword(headword)
    rd = normalize_reading(reading).strip('〜～~')

    # Primary normalized form
    if hw and rd:
        forms.add((hw, rd))

    # Kana-only form (treat the reading itself as a headword)
    if rd:
        forms.add((rd, rd))

    # If headword contains no kanji, add the raw headword too
    if hw and hw == rd:
        forms.add((hw, rd))

    return forms


def build_dedup_index(brainstorm_data, candidates_data, entries_data):
    """
    Build a comprehensive set of normalized (headword, reading) tuples
    from all known words (entries, candidates, brainstorm list).
    """
    index = set()

    for item in brainstorm_data:
        for form in normalize_for_dedup(item['headword'], item['reading']):
            index.add(form)

    for cand in candidates_data.get('candidates', []):
        for form in normalize_for_dedup(cand.get('word', ''), cand.get('reading', '')):
            index.add(form)

    for entry in entries_data.get('entries', []):
        hw = strip_furigana(entry.get('headword', ''))
        reading = entry.get('reading', '')
        for form in normalize_for_dedup(hw, reading):
            index.add(form)

    return index


def is_duplicate(headword, reading, dedup_index):
    """Check if a word matches any known word using flexible normalization."""
    return bool(normalize_for_dedup(headword, reading) & dedup_index)


# ---------------------------------------------------------------------------
# Init / update brainstorming data file
# ---------------------------------------------------------------------------

def init_brainstorm_data():
    """Create or update prompts/entries-and-candidates-for-brainstorming.md."""
    entries_data = load_json(ENTRIES_INDEX)
    candidates_data = load_json(CANDIDATES_FILE)

    # Collect all current words: (headword, reading) -> gloss
    current_words = {}
    for entry in entries_data.get('entries', []):
        hw = strip_furigana(entry.get('headword', ''))
        reading = entry.get('reading', '')
        gloss = entry.get('gloss', '')
        current_words[(hw, reading)] = gloss

    for cand in candidates_data.get('candidates', []):
        word = cand.get('word', '')
        reading = cand.get('reading', '')
        gloss = cand.get('notes', '')
        if (word, reading) not in current_words:
            current_words[(word, reading)] = gloss

    # Load persistent checked seeds (committed to repo — survives across sessions)
    checked_seeds = load_checked_seeds()

    # On first run, also import from the old brainstorming file
    if not checked_seeds and os.path.exists(OLD_BRAINSTORM_DATA):
        old_data = load_json(OLD_BRAINSTORM_DATA)
        for item in old_data:
            if item.get('checked', 0) == 1:
                checked_seeds.add((item.get('headword', ''), item.get('reading', '')))
        if checked_seeds:
            save_checked_seeds(checked_seeds)
            print(f"Imported {len(checked_seeds)} checked seeds from old brainstorming file.")

    # Build the combined list
    brainstorm_data = []
    for (hw, reading), gloss in sorted(current_words.items(),
                                       key=lambda x: (x[0][1] or '', x[0][0] or '')):
        checked = 1 if (hw, reading) in checked_seeds else 0
        brainstorm_data.append({
            'headword': hw,
            'reading': reading,
            'gloss': gloss or '',
            'checked': checked
        })

    save_json(BRAINSTORM_DATA, brainstorm_data)

    total = len(brainstorm_data)
    checked_count = sum(1 for item in brainstorm_data if item['checked'] == 1)
    print(f"Brainstorm data updated: {total} words "
          f"({checked_count} checked, {total - checked_count} unchecked)")
    return brainstorm_data


# ---------------------------------------------------------------------------
# Seed selection
# ---------------------------------------------------------------------------

def select_seeds(brainstorm_data, batch_size=15):
    """Select a random batch of unchecked seed words."""
    unchecked = [item for item in brainstorm_data if item.get('checked') == 0]
    if not unchecked:
        print("All words have been checked. Run 'reset-checked' to start over.")
        return []
    batch = random.sample(unchecked, min(batch_size, len(unchecked)))
    return batch


# ---------------------------------------------------------------------------
# OpenRouter API call
# ---------------------------------------------------------------------------

def call_openrouter(seeds, config):
    """Send seed words to OpenRouter and return parsed suggestions."""
    api_key = config['openrouter_api_key']

    seed_list = "\n".join(
        f"- {s['headword']} ({s['reading']}): {s['gloss']}"
        for s in seeds
    )

    relation_list = "\n".join(f"- {r}" for r in config['relation_types'])

    prompt = f"""You are helping build a Japanese-English learner's dictionary. Given the seed words below, brainstorm related Japanese words that a learner might need.

For each seed word, suggest 5-15 related words exploring these relationship types:
{relation_list}

SEED WORDS:
{seed_list}

REQUIREMENTS:
- Each suggestion must be a real, commonly used Japanese word
- Useful for intermediate-to-advanced Japanese learners
- Stable vocabulary (not ephemeral slang)
- Proper nouns ARE allowed when collocationally/semantically rich and known to
  every Japanese speaker (major places, canonical historical figures, key
  organizations); mark them "proper noun (place/person/organization/work/event/brand)"
- Single lexical items (not full sentences or long phrases)
- Not archaic, dialect-only, or highly specialized jargon
- Verbs should be in dictionary form (e.g. 食べる not 食べ)
- Adjectives should be in dictionary form (e.g. 美しい not 美しく)

OUTPUT FORMAT:
Return a JSON array of objects. Each object must have exactly these fields:
- "headword": the word as normally written (kanji + kana as appropriate)
- "reading": the full reading in hiragana only (never katakana, never romaji)
- "gloss": a brief English meaning (2-8 words)
- "seed": the headword of the seed word that inspired this suggestion

Return ONLY the JSON array, no other text or markdown formatting. Example:
[
  {{"headword": "食欲", "reading": "しょくよく", "gloss": "appetite", "seed": "食べる"}}
]"""

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://www.tkgje.jp/',
        'X-Title': 'je-dict-1 candidate brainstorming'
    }

    payload = {
        'model': config['model'],
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': config['temperature'],
        'max_tokens': config['max_tokens']
    }

    for attempt in range(4):
        try:
            response = requests.post(
                'https://openrouter.ai/api/v1/chat/completions',
                headers=headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            result = response.json()
            content = result['choices'][0]['message']['content']

            # Extract JSON array from response (handles markdown code blocks)
            json_match = re.search(r'\[[\s\S]*\]', content)
            if json_match:
                return json.loads(json_match.group())
            else:
                print(f"  WARNING: Could not parse JSON from LLM response")
                return []

        except requests.exceptions.HTTPError as e:
            status = getattr(e.response, 'status_code', None)
            wait = 2 ** (attempt + 1)
            print(f"  Attempt {attempt + 1} failed (HTTP {status}): {e}")
            if attempt < 3:
                print(f"  Retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"  All retries exhausted.")
                return []
        except (requests.RequestException, json.JSONDecodeError, KeyError, IndexError) as e:
            wait = 2 ** (attempt + 1)
            print(f"  Attempt {attempt + 1} failed: {e}")
            if attempt < 3:
                print(f"  Retrying in {wait}s...")
                time.sleep(wait)
            else:
                print(f"  All retries exhausted.")
                return []


# ---------------------------------------------------------------------------
# Main brainstorm loop
# ---------------------------------------------------------------------------

def brainstorm(config, num_batches=5):
    """Run the full brainstorming pipeline."""
    brainstorm_data = init_brainstorm_data()
    entries_data = load_json(ENTRIES_INDEX)
    candidates_data = load_json(CANDIDATES_FILE)

    dedup_index = build_dedup_index(brainstorm_data, candidates_data, entries_data)

    batch_size = config.get('batch_size', 15)
    all_new = []

    for batch_num in range(1, num_batches + 1):
        print(f"\n--- Batch {batch_num}/{num_batches} ---")

        seeds = select_seeds(brainstorm_data, batch_size)
        if not seeds:
            break

        seed_names = ', '.join(s['headword'] for s in seeds)
        print(f"Seeds: {seed_names}")

        print(f"Calling {config['model']}...")
        suggestions = call_openrouter(seeds, config)
        print(f"  LLM returned {len(suggestions)} suggestions")

        # Filter and deduplicate
        batch_new = []
        for sug in suggestions:
            hw = sug.get('headword', '').strip()
            reading = sug.get('reading', '').strip()
            gloss = sug.get('gloss', '').strip()

            if not hw or not reading or not gloss:
                continue

            # Normalize reading (katakana -> hiragana)
            reading = normalize_reading(reading)

            if not is_duplicate(hw, reading, dedup_index):
                batch_new.append({
                    'headword': hw,
                    'reading': reading,
                    'gloss': gloss,
                    'seed': sug.get('seed', '')
                })
                # Expand dedup index so later batches skip these too
                for form in normalize_for_dedup(hw, reading):
                    dedup_index.add(form)

        print(f"  {len(batch_new)} survived deduplication")
        all_new.extend(batch_new)

        # Mark seeds as checked in both the local data and the persistent file
        seed_keys = {(s['headword'], s['reading']) for s in seeds}
        for item in brainstorm_data:
            if (item['headword'], item['reading']) in seed_keys:
                item['checked'] = 1

        # Persist checked seeds to the committed file (survives across sessions)
        checked_seeds = load_checked_seeds()
        checked_seeds.update(seed_keys)
        save_checked_seeds(checked_seeds)

        # Also persist the local brainstorm data file for crash recovery
        save_json(BRAINSTORM_DATA, brainstorm_data)

    print(f"\n=== RESULTS ===")
    print(f"Total new candidates from this run: {len(all_new)}")

    if all_new:
        save_json(RESULTS_FILE, all_new)
        print(f"Results saved to: {RESULTS_FILE}")
    else:
        print("No new candidates found.")

    return all_new


# ---------------------------------------------------------------------------
# Add results to candidate_words.json
# ---------------------------------------------------------------------------

def add_results():
    """
    Add brainstorm results to candidate_words.json, using manage_candidates
    duplicate checking for each word.
    """
    if not os.path.exists(RESULTS_FILE):
        print("No results file found. Run 'brainstorm' first.")
        return 0

    results = load_json(RESULTS_FILE)
    if not results:
        print("Results file is empty.")
        return 0

    # Load current data for duplicate checking
    entries_data = load_json(ENTRIES_INDEX)
    candidates_data = load_json(CANDIDATES_FILE)

    # Build lookup sets for exact match checking (matches manage_candidates logic)
    entry_set = set()
    for entry in entries_data.get('entries', []):
        hw = strip_furigana(entry.get('headword', ''))
        reading = entry.get('reading', '')
        entry_set.add((hw, reading))

    candidate_set = set()
    for cand in candidates_data.get('candidates', []):
        candidate_set.add((cand.get('word', ''), cand.get('reading', '')))

    # Also build flexible index
    all_known = build_dedup_index([], candidates_data, entries_data)

    added = 0
    skipped_dup = 0
    skipped_fuzzy = 0

    # Get next candidate ID
    next_id = candidates_data['metadata'].get('next_id', 1)

    for item in results:
        hw = item['headword']
        reading = normalize_reading(item['reading'])
        gloss = item.get('gloss', '')

        # Exact match check
        if (hw, reading) in entry_set or (hw, reading) in candidate_set:
            skipped_dup += 1
            continue

        # Flexible match check
        if is_duplicate(hw, reading, all_known):
            skipped_fuzzy += 1
            continue

        # Add to candidates
        candidate = {
            'id': f'C{next_id:05d}',
            'word': hw,
            'reading': reading,
            'notes': gloss,
            'added': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        }
        candidates_data['candidates'].append(candidate)
        print(f"  + {hw} ({reading}): {gloss}")
        next_id += 1
        added += 1

        # Update dedup sets for subsequent items
        candidate_set.add((hw, reading))
        for form in normalize_for_dedup(hw, reading):
            all_known.add(form)

    # Update metadata
    candidates_data['metadata']['next_id'] = next_id
    candidates_data['metadata']['last_updated'] = time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    candidates_data['metadata']['total_candidates'] = len(candidates_data['candidates'])

    save_json(CANDIDATES_FILE, candidates_data)

    print(f"Added: {added}")
    print(f"Skipped (exact duplicate): {skipped_dup}")
    print(f"Skipped (fuzzy match): {skipped_fuzzy}")
    print(f"Total candidates now: {len(candidates_data['candidates'])}")

    # Clean up results file after successful import
    if added > 0:
        os.remove(RESULTS_FILE)
        print(f"Removed {RESULTS_FILE} after successful import.")

    return added


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def show_stats():
    """Show statistics about the brainstorming data file."""
    checked_seeds = load_checked_seeds()
    print(f"Persistent checked seeds (brainstorming/checked_seeds.json): {len(checked_seeds)}")

    if os.path.exists(BRAINSTORM_DATA):
        data = load_json(BRAINSTORM_DATA)
        total = len(data)
        checked = sum(1 for item in data if item.get('checked') == 1)
        unchecked = total - checked

        print(f"\nLocal brainstorm data file:")
        print(f"  Total words: {total}")
        print(f"  Checked (already used as seeds): {checked} ({100 * checked / total:.1f}%)")
        print(f"  Unchecked (available as seeds):  {unchecked} ({100 * unchecked / total:.1f}%)")
    else:
        print("\nLocal brainstorm data file does not exist yet (will be created by 'init').")

    if os.path.exists(RESULTS_FILE):
        results = load_json(RESULTS_FILE)
        print(f"\nPending results not yet imported: {len(results)}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Brainstorm dictionary candidates via OpenRouter LLM.')
    parser.add_argument('command',
                        choices=['init', 'brainstorm', 'stats', 'reset-checked',
                                 'add-results'],
                        help='Command to run')
    parser.add_argument('-n', '--num-batches', type=int, default=5,
                        help='Number of batches to run (default: 5)')
    parser.add_argument('--model', default='openai/gpt-4.1-mini',
                        help='OpenRouter model ID (default: openai/gpt-4.1-mini)')
    parser.add_argument('--temperature', type=float, default=0.8,
                        help='LLM temperature (default: 0.8)')
    parser.add_argument('--max-tokens', type=int, default=4096,
                        help='Max response tokens (default: 4096)')
    parser.add_argument('--batch-size', type=int, default=15,
                        help='Seeds per batch (default: 15)')

    args = parser.parse_args()

    if args.command == 'init':
        init_brainstorm_data()

    elif args.command == 'stats':
        show_stats()

    elif args.command == 'reset-checked':
        # Reset the persistent checked seeds file
        save_checked_seeds(set())
        print(f"Cleared {CHECKED_SEEDS_FILE}")

        # Also reset the local brainstorm data file if it exists
        if os.path.exists(BRAINSTORM_DATA):
            data = load_json(BRAINSTORM_DATA)
            for item in data:
                item['checked'] = 0
            save_json(BRAINSTORM_DATA, data)
            print(f"Reset {len(data)} entries to unchecked in local data file.")
        else:
            print("Local brainstorm data file does not exist (not needed — "
                  "checked_seeds.json is the source of truth).")

    elif args.command == 'add-results':
        add_results()

    elif args.command == 'brainstorm':
        api_key = os.environ.get('OPENROUTER_API_KEY', '')
        if not api_key:
            print("ERROR: OPENROUTER_API_KEY environment variable is not set.")
            sys.exit(1)

        config = {
            'openrouter_api_key': api_key,
            'model': args.model,
            'temperature': args.temperature,
            'max_tokens': args.max_tokens,
            'batch_size': args.batch_size,
            'relation_types': [
                "synonyms and near-synonyms (same meaning, different register or nuance)",
                "antonyms (direct opposites)",
                "same semantic field (words in the same category)",
                "same-kanji compounds (other common words using the same kanji)",
                "register variants (formal/informal pairs, written/spoken variants)",
                "collocational partners (words that naturally pair with the seed)",
                "situationally related (words a learner would need in the same context)"
            ]
        }

        brainstorm(config, args.num_batches)


if __name__ == '__main__':
    main()
