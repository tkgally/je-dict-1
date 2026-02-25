#!/usr/bin/env python3
"""LLM Brainstorming Pipeline for je-dict-1 Dictionary Candidates.

Selects seed words from the brainstorming file, sends them to an LLM
via OpenRouter, and collects new candidate word suggestions.

Usage:
    python3 brainstorm/llm_brainstorm.py                  # Run 1 batch
    python3 brainstorm/llm_brainstorm.py -n 5             # Run 5 batches
    python3 brainstorm/llm_brainstorm.py --stats           # Show statistics
    python3 brainstorm/llm_brainstorm.py --reset-checked   # Reset all checked flags
"""

import json
import random
import sys
import os
import datetime
import time
import re
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install with: pip install requests")
    sys.exit(1)

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config.json"
BRAINSTORM_FILE = BASE_DIR / "entries_and_candidates_for_LLM_brainstorming.json"


def load_config():
    """Load configuration from config.json."""
    if not CONFIG_FILE.exists():
        print(f"Error: Config file not found: {CONFIG_FILE}")
        print("Copy config.json and fill in your API key and model name.")
        sys.exit(1)

    with open(CONFIG_FILE) as f:
        config = json.load(f)

    if config["openrouter_api_key"] == "YOUR_OPENROUTER_API_KEY_HERE":
        print("Error: Please set your OpenRouter API key in config.json")
        sys.exit(1)

    if config["model"] == "MODEL_NAME_HERE":
        print("Error: Please set the model name in config.json")
        print("Examples: google/gemini-2.0-flash, google/gemini-2.5-pro, etc.")
        sys.exit(1)

    return config


def load_brainstorm_data():
    """Load the brainstorming JSON file."""
    if not BRAINSTORM_FILE.exists():
        print(f"Error: Brainstorming file not found: {BRAINSTORM_FILE}")
        print("Place entries_and_candidates_for_LLM_brainstorming.json in the brainstorm/ directory.")
        sys.exit(1)

    with open(BRAINSTORM_FILE) as f:
        return json.load(f)


def save_brainstorm_data(data):
    """Save the brainstorming JSON file (to update checked flags)."""
    with open(BRAINSTORM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def get_output_file(config):
    """Determine output file path based on model name."""
    model = config["model"]
    # Extract a clean model name: "google/gemini-2.0-flash" -> "gemini-2.0-flash"
    model_short = model.split("/")[-1]
    # Sanitize for filename
    model_short = re.sub(r'[^a-zA-Z0-9._-]', '_', model_short)
    return BASE_DIR / f"new_candidates_by_{model_short}.json"


def select_seed_words(data, batch_size=15):
    """Select a batch of unchecked words as seeds."""
    unchecked = [entry for entry in data if entry.get("checked", 0) == 0]
    if not unchecked:
        return []
    batch_size = min(batch_size, len(unchecked))
    return random.sample(unchecked, batch_size)


def build_prompt(seed_words, config):
    """Build the LLM prompt for brainstorming related words."""
    seed_list = "\n".join(
        f"- {w['headword']} ({w['reading']}): {w['gloss']}"
        for w in seed_words
    )

    relation_types = config.get("relation_types", [
        "synonyms and near-synonyms",
        "antonyms",
        "same semantic field",
        "same-kanji compounds",
        "register variants",
        "collocational partners",
        "situationally related words",
    ])
    relation_list = "\n".join(f"- **{r}**" for r in relation_types)

    prompt = f"""You are helping build a Japanese-English learner's dictionary for intermediate learners who can read kana and are building vocabulary. The dictionary currently has about 13,500 entries covering basic through advanced vocabulary.

Below are {len(seed_words)} Japanese words from the dictionary. For each word, think of related Japanese words that might be missing from the dictionary. Consider these types of relationships:

{relation_list}

**Seed words:**
{seed_list}

**Selection criteria — include a word ONLY if it meets ALL of these:**
1. It is a real, commonly used Japanese word (not archaic, dialect-only, or highly technical)
2. It would be useful for an intermediate-to-advanced Japanese learner
3. It is stable vocabulary (not ephemeral slang or trendy internet terms)
4. It is NOT a proper noun (no place names, personal names, brand names, company names)
5. It is a single lexical item (not a full sentence or long phrase)

**Output format:** Return a JSON array of objects. Each object must have exactly these fields:
- "headword": the word as normally written (kanji + kana as appropriate)
- "reading": the full reading in hiragana (MUST be hiragana, never katakana)
- "gloss": a brief English meaning (2-8 words)
- "seed": the headword of the seed word that inspired this suggestion

Return ONLY the JSON array, no other text. Aim for 5-15 suggestions per seed word, but prioritize quality over quantity. It is fine to suggest fewer if the seed word does not have many good related words.

Example output format:
[
  {{"headword": "温厚", "reading": "おんこう", "gloss": "gentle, mild-mannered", "seed": "穏やか"}},
  {{"headword": "激怒", "reading": "げきど", "gloss": "fury, rage", "seed": "怒る"}}
]"""

    return prompt


def call_openrouter(prompt, config):
    """Call the LLM via OpenRouter API with retry logic."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {config['openrouter_api_key']}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": config["model"],
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": config.get("temperature", 0.8),
        "max_tokens": config.get("max_tokens", 4096),
    }

    max_retries = 4
    backoff_seconds = [2, 4, 8, 16]

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=120)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            if attempt < max_retries:
                wait = backoff_seconds[attempt]
                print(f"  Network error (attempt {attempt + 1}): {e}")
                print(f"  Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
        except requests.exceptions.HTTPError as e:
            # Don't retry on 4xx errors (auth, bad request, etc.)
            if response.status_code < 500:
                raise
            if attempt < max_retries:
                wait = backoff_seconds[attempt]
                print(f"  Server error {response.status_code} (attempt {attempt + 1})")
                print(f"  Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise


def parse_llm_response(response_text):
    """Parse the JSON array from the LLM response."""
    text = response_text.strip()

    # Handle markdown code blocks
    if "```json" in text:
        text = text.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in text:
        text = text.split("```", 1)[1].split("```", 1)[0].strip()

    try:
        candidates = json.loads(text)
        if not isinstance(candidates, list):
            print(f"  Warning: LLM response was not a JSON array, got {type(candidates).__name__}")
            return []
        return candidates
    except json.JSONDecodeError as e:
        print(f"  Error parsing LLM response as JSON: {e}")
        print(f"  Response preview: {text[:300]}...")
        return []


def validate_candidate(candidate):
    """Basic validation of a candidate entry."""
    required_fields = ["headword", "reading", "gloss"]
    for field in required_fields:
        if field not in candidate or not str(candidate[field]).strip():
            return False, f"missing or empty '{field}'"

    # Reading should not be empty
    reading = str(candidate["reading"]).strip()
    if not reading:
        return False, "empty reading"

    # Check that reading contains Japanese characters (hiragana/katakana)
    has_kana = any('\u3040' <= c <= '\u309f' or '\u30a0' <= c <= '\u30ff' for c in reading)
    if not has_kana:
        return False, f"reading '{reading}' contains no kana"

    return True, ""


def build_existing_set(brainstorm_data):
    """Build a set of (headword, reading) pairs for fast lookup."""
    return set(
        (entry["headword"], entry["reading"])
        for entry in brainstorm_data
    )


def filter_against_existing(candidates, existing_set):
    """Remove candidates that already exist in the brainstorming file."""
    new_candidates = []
    filtered_count = 0
    for c in candidates:
        key = (c.get("headword", ""), c.get("reading", ""))
        if key in existing_set:
            filtered_count += 1
        else:
            new_candidates.append(c)

    if filtered_count > 0:
        print(f"  Filtered out {filtered_count} candidates already in dictionary/candidates")

    return new_candidates


def load_output_data(output_file):
    """Load existing output data or return empty structure."""
    if output_file.exists():
        with open(output_file) as f:
            return json.load(f)
    return None


def deduplicate_against_output(candidates, output_data):
    """Remove candidates already in the output file from previous runs."""
    if output_data is None:
        return candidates

    existing_keys = set(
        (entry["headword"], entry["reading"])
        for entry in output_data.get("candidates", [])
    )

    new_candidates = []
    dedup_count = 0
    for c in candidates:
        key = (c.get("headword", ""), c.get("reading", ""))
        if key in existing_keys:
            dedup_count += 1
        else:
            new_candidates.append(c)

    if dedup_count > 0:
        print(f"  Deduplicated {dedup_count} candidates from previous runs")

    return new_candidates


def save_results(new_candidates, output_file, output_data, model_name):
    """Append new candidates to the output file."""
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    if output_data is None:
        output_data = {
            "metadata": {
                "description": f"Candidate words brainstormed by {model_name}",
                "model": model_name,
                "created": timestamp,
                "total_candidates": 0,
                "total_runs": 0,
            },
            "candidates": [],
        }

    for c in new_candidates:
        c["added"] = timestamp
        c["run"] = output_data["metadata"]["total_runs"] + 1

    output_data["candidates"].extend(new_candidates)
    output_data["metadata"]["total_candidates"] = len(output_data["candidates"])
    output_data["metadata"]["total_runs"] += 1
    output_data["metadata"]["last_updated"] = timestamp

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    return output_data


def mark_seeds_checked(brainstorm_data, seed_words):
    """Mark seed words as checked in the brainstorming data."""
    seed_keys = set((w["headword"], w["reading"]) for w in seed_words)
    count = 0
    for entry in brainstorm_data:
        if (entry["headword"], entry["reading"]) in seed_keys:
            entry["checked"] = 1
            count += 1
    return count


def run_batch(brainstorm_data, existing_set, output_file, output_data, config, batch_num, total_batches):
    """Run a single batch of the pipeline. Returns (new_candidate_count, updated_output_data)."""
    batch_size = config.get("batch_size", 15)

    print(f"\n{'=' * 60}")
    print(f"Batch {batch_num}/{total_batches}")
    print(f"{'=' * 60}")

    # Select seeds
    seeds = select_seed_words(brainstorm_data, batch_size)
    if not seeds:
        print("All entries have been checked. Nothing to do.")
        return 0, output_data

    print(f"Selected {len(seeds)} seed words:")
    for s in seeds:
        print(f"  - {s['headword']} ({s['reading']}): {s['gloss']}")

    # Build prompt and call LLM
    prompt = build_prompt(seeds, config)
    print(f"\nCalling {config['model']}...")

    try:
        response = call_openrouter(prompt, config)
    except Exception as e:
        print(f"  Error calling LLM: {e}")
        # Still mark seeds as checked to avoid getting stuck
        mark_seeds_checked(brainstorm_data, seeds)
        save_brainstorm_data(brainstorm_data)
        return 0, output_data

    # Parse response
    candidates = parse_llm_response(response)
    print(f"  LLM suggested {len(candidates)} candidates")

    if not candidates:
        mark_seeds_checked(brainstorm_data, seeds)
        save_brainstorm_data(brainstorm_data)
        return 0, output_data

    # Validate
    valid_candidates = []
    invalid_count = 0
    for c in candidates:
        ok, reason = validate_candidate(c)
        if ok:
            valid_candidates.append(c)
        else:
            invalid_count += 1
    if invalid_count > 0:
        print(f"  {invalid_count} candidates failed validation")

    # Filter against existing entries/candidates
    new_candidates = filter_against_existing(valid_candidates, existing_set)

    # Deduplicate against previous output
    new_candidates = deduplicate_against_output(new_candidates, output_data)

    print(f"  {len(new_candidates)} new candidates after filtering")

    if new_candidates:
        output_data = save_results(new_candidates, output_file, output_data, config["model"])

        # Add new candidates to existing_set so subsequent batches dedup against them
        for c in new_candidates:
            existing_set.add((c["headword"], c["reading"]))

        # Show new candidates
        print("\n  New candidates:")
        for c in new_candidates:
            seed_info = f" [from: {c.get('seed', '?')}]" if 'seed' in c else ""
            print(f"    + {c['headword']} ({c['reading']}): {c['gloss']}{seed_info}")

    # Mark seeds as checked
    marked = mark_seeds_checked(brainstorm_data, seeds)
    save_brainstorm_data(brainstorm_data)
    print(f"  Marked {marked} seeds as checked")

    remaining = sum(1 for e in brainstorm_data if e.get("checked", 0) == 0)
    print(f"  Remaining unchecked: {remaining}")

    return len(new_candidates), output_data


def run_pipeline(num_batches=1):
    """Run the brainstorming pipeline for the specified number of batches."""
    config = load_config()
    output_file = get_output_file(config)

    print(f"Model: {config['model']}")
    print(f"Output: {output_file.name}")
    print(f"Batches: {num_batches}")
    print(f"Batch size: {config.get('batch_size', 15)} seeds")

    print(f"\nLoading brainstorming data...")
    brainstorm_data = load_brainstorm_data()
    total = len(brainstorm_data)
    unchecked = sum(1 for e in brainstorm_data if e.get("checked", 0) == 0)
    print(f"  Total entries: {total}")
    print(f"  Unchecked: {unchecked}")

    if unchecked == 0:
        print("\nAll entries have been checked. Nothing to do.")
        print("Use --reset-checked to start over.")
        return

    # Build lookup set once
    existing_set = build_existing_set(brainstorm_data)

    # Load existing output
    output_data = load_output_data(output_file)

    total_new = 0
    for batch_num in range(1, num_batches + 1):
        count, output_data = run_batch(
            brainstorm_data, existing_set, output_file, output_data,
            config, batch_num, num_batches
        )
        total_new += count

        # Check if all words are checked
        remaining = sum(1 for e in brainstorm_data if e.get("checked", 0) == 0)
        if remaining == 0:
            print("\nAll entries have now been checked.")
            break

    print(f"\n{'=' * 60}")
    print(f"Pipeline complete. New candidates this session: {total_new}")
    if output_file.exists():
        with open(output_file) as f:
            data = json.load(f)
        print(f"Total candidates in {output_file.name}: {data['metadata']['total_candidates']}")
        print(f"Total runs: {data['metadata']['total_runs']}")


def show_stats():
    """Show pipeline statistics."""
    if not BRAINSTORM_FILE.exists():
        print(f"Brainstorming file not found: {BRAINSTORM_FILE}")
        return

    data = load_brainstorm_data()
    total = len(data)
    checked = sum(1 for e in data if e.get("checked", 0) == 1)
    unchecked = total - checked

    print(f"Brainstorming file: {total} entries")
    print(f"  Checked:   {checked:>6} ({checked * 100 / total:.1f}%)")
    print(f"  Unchecked: {unchecked:>6} ({unchecked * 100 / total:.1f}%)")

    # Check for output files
    output_files = sorted(BASE_DIR.glob("new_candidates_by_*.json"))
    if output_files:
        print()
        for f in output_files:
            with open(f) as fh:
                out_data = json.load(fh)
            meta = out_data["metadata"]
            print(f"{f.name}:")
            print(f"  Model:            {meta.get('model', '?')}")
            print(f"  Total candidates: {meta['total_candidates']}")
            print(f"  Total runs:       {meta['total_runs']}")
            print(f"  Last updated:     {meta.get('last_updated', '?')}")
    else:
        print("\nNo output files found yet.")


def reset_checked():
    """Reset all checked flags to 0."""
    if not BRAINSTORM_FILE.exists():
        print(f"Brainstorming file not found: {BRAINSTORM_FILE}")
        return

    data = load_brainstorm_data()
    for entry in data:
        entry["checked"] = 0

    save_brainstorm_data(data)
    print(f"Reset {len(data)} entries to unchecked.")


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="LLM Brainstorming Pipeline for Dictionary Candidates"
    )
    parser.add_argument(
        "--batches", "-n", type=int, default=1,
        help="Number of batches to run (default: 1)"
    )
    parser.add_argument(
        "--stats", action="store_true",
        help="Show statistics and exit"
    )
    parser.add_argument(
        "--reset-checked", action="store_true",
        help="Reset all checked flags to 0"
    )
    args = parser.parse_args()

    if args.stats:
        show_stats()
        return

    if args.reset_checked:
        reset_checked()
        return

    run_pipeline(num_batches=args.batches)


if __name__ == "__main__":
    main()
