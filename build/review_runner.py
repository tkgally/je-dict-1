#!/usr/bin/env python3
"""Multi-model review runner for dictionary entry proofreading.

Sends entries to external models via OpenRouter API to cross-check
furigana readings. Supports a two-pass pipeline:

  Pass 1 (screening): Cheap model flags potentially problematic entries.
  Pass 2 (deep review): Strong models verify flagged entries in detail.

Usage:
    # Original mode (both models, detailed review)
    python3 build/review_runner.py --range 1 100
    python3 build/review_runner.py --ids 00123,00456,00789
    python3 build/review_runner.py --range 1 100 --model openai/gpt-4.1
    python3 build/review_runner.py --range 1 100 --dry-run
    python3 build/review_runner.py --report

    # Two-pass pipeline (Phase 2)
    python3 build/review_runner.py --pass screening --range 1 1000
    python3 build/review_runner.py --pass screening --range 1 1000 --budget 5.00
    python3 build/review_runner.py --pass deep --range 1 1000
    python3 build/review_runner.py --pass deep --ids 00123,00456
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    import urllib.error
    HAS_REQUESTS = False

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
REVIEWS_DIR = PROJECT_ROOT / "reviews"
SCREENING_DIR = REVIEWS_DIR / "screening"
INDEX_FILE = PROJECT_ROOT / "entries_index.json"

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

DEFAULT_MODELS = ["openai/gpt-4.1", "google/gemini-2.5-flash"]
SCREENING_MODEL = "google/gemini-2.5-flash"
DEEP_MODELS = ["openai/gpt-4.1", "google/gemini-2.5-pro"]

FURIGANA_RE = re.compile(r"\{([^|{}]+)\|([^}]+)\}")

# Rate limiting: max 10 requests per minute per model
RATE_LIMIT_INTERVAL = 6.0  # seconds between requests per model

# Approximate cost per 1K tokens (USD) for budget estimation
MODEL_COSTS = {
    "google/gemini-2.5-flash": {"input": 0.00015, "output": 0.0006},
    "google/gemini-2.5-pro": {"input": 0.00125, "output": 0.005},
    "openai/gpt-4.1": {"input": 0.002, "output": 0.008},
    "openai/gpt-4.1-mini": {"input": 0.0004, "output": 0.0016},
}


def get_api_key():
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        print("ERROR: OPENROUTER_API_KEY environment variable is not set.", file=sys.stderr)
        print("Set it with: export OPENROUTER_API_KEY='your-key-here'", file=sys.stderr)
        sys.exit(1)
    return key


def load_entries_index():
    with open(INDEX_FILE) as f:
        return json.load(f)


def find_entry_file(entry_id_str):
    """Find the entry JSON file given a numeric ID string like '00001'."""
    id_num = int(entry_id_str)
    range_dir = f"{(id_num // 500) * 500:05d}"
    entry_dir = ENTRIES_DIR / range_dir
    if not entry_dir.exists():
        return None
    for f in entry_dir.iterdir():
        if f.name.startswith(entry_id_str + "_") and f.suffix == ".json":
            return f
    return None


def load_entry(path):
    with open(path) as f:
        return json.load(f)


def extract_furigana_pairs(entry):
    """Extract all {kanji|reading} pairs from an entry."""
    pairs = []

    def scan_field(field_name, text):
        if not text or not isinstance(text, str):
            return
        for m in FURIGANA_RE.finditer(text):
            # Capture surrounding context (up to 24 chars after the match).
            # Kept generous so trim_context() has room to cut back to a
            # wrapper boundary instead of showing a half-wrapper.
            after = text[m.end():m.end()+24]
            pairs.append({
                "field": field_name,
                "text": m.group(0),
                "kanji": m.group(1),
                "reading": m.group(2),
                "context_after": after,
            })

    # Headword
    scan_field("headword", entry.get("headword"))

    # Examples
    for i, ex in enumerate(entry.get("examples", [])):
        scan_field(f"examples[{i}].japanese", ex.get("japanese"))
        scan_field(f"examples[{i}].notes", ex.get("notes"))

    # Notes
    scan_field("notes", entry.get("notes"))

    # Definitions (explanation text sometimes has furigana)
    for i, defn in enumerate(entry.get("definitions", [])):
        scan_field(f"definitions[{i}].explanation", defn.get("explanation"))

    # Conjugation forms
    conj = entry.get("conjugation", {})
    for i, form in enumerate(conj.get("forms", [])):
        scan_field(f"conjugation.forms[{i}].affirmative", form.get("affirmative"))
        scan_field(f"conjugation.forms[{i}].negative", form.get("negative"))

    # Prominent see_also
    for i, ref in enumerate(entry.get("prominent_see_also", [])):
        scan_field(f"prominent_see_also[{i}].headword", ref.get("headword"))

    # Cross references
    for i, ref in enumerate(entry.get("cross_references", [])):
        scan_field(f"cross_references[{i}].headword", ref.get("headword"))

    return pairs


def trim_context(ctx, limit=18):
    """Trim following-context text so it never ends inside a {kanji|reading} wrapper.

    The context is shown to the model as "(followed by: ...)". A window that cuts
    mid-wrapper produces text like `{協議会|きょうぎか)` — which reads as a complete
    wrapper holding a truncated reading, and models reliably flag it as an
    incomplete reading. Cutting back to the last wrapper boundary removes that
    whole false-positive family.
    """
    if not ctx:
        return ""
    first = ctx.split("\n")[0][:limit]
    brace = first.rfind("{")
    if brace != -1 and "}" not in first[brace:]:
        first = first[:brace]
    return first


def deduplicate_pairs(pairs):
    """Deduplicate pairs by (kanji, reading) — keep field info from first occurrence."""
    seen = {}
    unique = []
    for p in pairs:
        key = (p["kanji"], p["reading"])
        if key not in seen:
            seen[key] = p
            unique.append(p)
    return unique


def estimate_cost(model, prompt_tokens, completion_tokens=200):
    """Estimate API call cost in USD."""
    costs = MODEL_COSTS.get(model, {"input": 0.002, "output": 0.008})
    return (prompt_tokens / 1000 * costs["input"] +
            completion_tokens / 1000 * costs["output"])


def rough_token_count(text):
    """Rough token estimate: ~4 chars per token for mixed JP/EN text."""
    return len(text) // 4


def build_screening_prompt(entry, pairs):
    """Build a lightweight screening prompt for Pass 1."""
    word = entry.get("headword", "")
    reading = entry.get("reading", "")
    pos = entry.get("part_of_speech", "")

    unique_pairs = deduplicate_pairs(pairs)
    pair_lines = []
    for i, p in enumerate(unique_pairs, 1):
        ctx = trim_context(p.get("context_after", ""))
        display = f'{p["kanji"]} → {p["reading"]}'
        if ctx:
            display += f'  (followed by: 「{ctx}」)'
        pair_lines.append(f'{i}. {display}')

    pairs_text = "\n".join(pair_lines)

    prompt = f"""Check these furigana readings from a Japanese dictionary entry for errors.

Entry: {word} ({reading}) — {pos}

Format: {{kanji|reading}}okurigana — the reading covers ONLY the kanji portion.
Example: {{走|はし}}る means 走=はし (correct), る is okurigana outside the markup.
Do NOT flag partial readings as errors — they are correct by design.

Known-correct patterns — do NOT flag any of these:
- Rendaku (sequential voicing) in compounds and suffixes: 会社→がいしゃ inside 株式会社, 好き→ずき in the 〜好き suffix (甘いもの好き), 小屋→ごや in 山小屋.
- Standalone noun readings that differ from compound readings: 話→はなし as a noun.
- Compound readings split before okurigana: 先行→さきゆ followed by き (先行き=さきゆき).
- Counter and numeral sound changes: 一本→いっぽん, 三階→さんがい.
Judge ONLY the "kanji → reading" pair itself. The 「...」 context after a pair is a
short excerpt cut to a fixed length for display; it may stop early. Never infer
that a reading is truncated or incomplete from that excerpt.
If you are not confident a reading is actually wrong, do not flag it.

Pairs:
{pairs_text}

Are there any incorrect kanji-reading mappings? Respond with JSON:
{{"flagged": true/false, "concerns": ["description of each concern"], "confidence": 0.0-1.0}}

If all readings look correct, respond: {{"flagged": false, "concerns": [], "confidence": 1.0}}
Respond ONLY with JSON."""

    return prompt, unique_pairs


def load_screening_status():
    """Load screening status tracking file."""
    status_file = SCREENING_DIR / "screening_status.json"
    if status_file.exists():
        with open(status_file) as f:
            return json.load(f)
    return {"screened": {}, "last_updated": None}


def save_screening_status(status):
    """Save screening status tracking file."""
    SCREENING_DIR.mkdir(parents=True, exist_ok=True)
    status["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    status_file = SCREENING_DIR / "screening_status.json"
    with open(status_file, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2, ensure_ascii=False)


def save_screening_result(result):
    """Save a screening result to the screening directory."""
    SCREENING_DIR.mkdir(parents=True, exist_ok=True)
    path = SCREENING_DIR / f"{result['entry_id']}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    return path


def parse_screening_response(response_data):
    """Extract screening JSON from model response."""
    content = extract_message_text(response_data)
    if content is None:
        return None
    content = strip_code_fences(content)

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        print(f"  Failed to parse screening response: {content[:200]}...", file=sys.stderr)
        return None


def run_screening_pass(entry_ids, api_key, model, dry_run=False, budget=None):
    """Run Pass 1: screening with a cheap model."""
    print(f"SCREENING PASS — model: {model}")
    print(f"Processing {len(entry_ids)} entries")
    if budget is not None:
        print(f"Budget limit: ${budget:.2f}")
    if dry_run:
        print("DRY RUN — prompts will be printed but not sent.\n")

    status = load_screening_status()
    total_cost = 0.0
    screened = 0
    flagged_count = 0
    skipped = 0

    for entry_id_str in entry_ids:
        # Budget check
        if budget is not None and total_cost >= budget:
            print(f"\nBudget limit reached (${total_cost:.4f} >= ${budget:.2f}). Stopping.")
            break

        # Skip already screened
        if entry_id_str in status.get("screened", {}) and not dry_run:
            skipped += 1
            continue

        entry_path = find_entry_file(entry_id_str)
        if not entry_path:
            skipped += 1
            continue

        entry = load_entry(entry_path)
        pairs = extract_furigana_pairs(entry)
        if not pairs:
            status.setdefault("screened", {})[entry_id_str] = "no_pairs"
            skipped += 1
            continue

        prompt, unique_pairs = build_screening_prompt(entry, pairs)

        if dry_run:
            print(f"\n{'='*60}")
            print(f"Entry: {entry_id_str} — {entry.get('headword', '')} ({entry.get('reading', '')})")
            print(f"Furigana pairs: {len(pairs)} total, {len(unique_pairs)} unique")
            print(f"{'='*60}")
            print(prompt)
            print(f"{'='*60}\n")
            continue

        # Estimate cost
        prompt_tokens = rough_token_count(prompt)
        est_cost = estimate_cost(model, prompt_tokens, 100)
        total_cost += est_cost

        print(f"  Screening {entry_id_str}: {entry.get('headword', '')} "
              f"({len(unique_pairs)} pairs, ~${est_cost:.4f})")

        response = call_openrouter(api_key, model, prompt)
        parsed = parse_screening_response(response)

        if parsed is None:
            print(f"    WARNING: Failed to parse response, marking as flagged")
            parsed = {"flagged": True, "concerns": ["Parse failure"], "confidence": 0.0}

        result = {
            "entry_id": entry_id_str,
            "screened_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "model": model,
            "flagged": parsed.get("flagged", False),
            "concerns": parsed.get("concerns", []),
            "confidence": parsed.get("confidence", 0.5),
        }

        save_screening_result(result)
        status.setdefault("screened", {})[entry_id_str] = "flagged" if result["flagged"] else "ok"
        screened += 1

        if result["flagged"]:
            flagged_count += 1
            concerns = "; ".join(result["concerns"][:2]) if result["concerns"] else "no details"
            print(f"    FLAGGED (confidence: {result['confidence']:.1f}): {concerns}")
        else:
            print(f"    OK")

        # Rate limit
        if entry_id_str != entry_ids[-1]:
            time.sleep(RATE_LIMIT_INTERVAL)

    if not dry_run:
        save_screening_status(status)
        print(f"\nScreening complete. Screened: {screened}, Flagged: {flagged_count}, "
              f"Skipped: {skipped}, Est. cost: ${total_cost:.4f}")
        print(f"Results saved to: {SCREENING_DIR}/")

        # Report cost estimate for full dictionary
        total_entries_est = len(list(ENTRIES_DIR.glob("**/*.json")))
        remaining = total_entries_est - len(status.get("screened", {}))
        if screened > 0:
            cost_per_entry = total_cost / screened
            full_est = cost_per_entry * remaining
            print(f"\nCost estimate for remaining {remaining} entries: ~${full_est:.2f}")


def get_flagged_entry_ids():
    """Get entry IDs flagged during screening."""
    flagged = []
    if not SCREENING_DIR.exists():
        return flagged
    for f in sorted(SCREENING_DIR.glob("*.json")):
        if f.name == "screening_status.json":
            continue
        try:
            with open(f) as fh:
                data = json.load(fh)
            if data.get("flagged"):
                flagged.append(data["entry_id"])
        except (json.JSONDecodeError, IOError):
            pass
    return flagged


def run_deep_pass(entry_ids, api_key, models, dry_run=False, budget=None):
    """Run Pass 2: deep review with strong models on flagged entries."""
    print(f"DEEP REVIEW PASS — models: {', '.join(models)}")

    # If no explicit IDs given, use flagged entries from screening
    if not entry_ids:
        entry_ids = get_flagged_entry_ids()
        print(f"Using {len(entry_ids)} flagged entries from screening")

    if not entry_ids:
        print("No entries to review. Run screening pass first or specify --ids.")
        return

    print(f"Processing {len(entry_ids)} entries")
    if budget is not None:
        print(f"Budget limit: ${budget:.2f}")
    if dry_run:
        print("DRY RUN — prompts will be printed but not sent.\n")

    total_cost = 0.0
    reviewed = 0
    flagged_total = 0
    skipped = 0

    for entry_id_str in entry_ids:
        if budget is not None and total_cost >= budget:
            print(f"\nBudget limit reached (${total_cost:.4f} >= ${budget:.2f}). Stopping.")
            break

        entry_path = find_entry_file(entry_id_str)
        if not entry_path:
            print(f"  {entry_id_str}: Entry file not found, skipping.")
            skipped += 1
            continue

        entry = load_entry(entry_path)
        pairs = extract_furigana_pairs(entry)
        if not pairs:
            print(f"  {entry_id_str}: No furigana pairs found, skipping.")
            skipped += 1
            continue

        print(f"Deep review {entry_id_str}: {entry.get('headword', '')} ({entry.get('reading', '')})")

        prompt, unique_pairs = build_review_prompt(entry, pairs)

        if dry_run:
            print(f"  {len(unique_pairs)} unique pairs, {len(models)} models")
            continue

        # Estimate cost for all models
        prompt_tokens = rough_token_count(prompt)
        for model in models:
            total_cost += estimate_cost(model, prompt_tokens, 500)

        report = review_entry(entry, entry_id_str, api_key, models, dry_run=False)
        if report:
            # Add screening context if available
            screening_file = SCREENING_DIR / f"{entry_id_str}.json"
            if screening_file.exists():
                with open(screening_file) as sf:
                    report["screening"] = json.load(sf)

            save_report(report)
            flagged = report["summary"]["flagged"]
            flagged_total += flagged
            status = f"✓ {report['summary']['total_checked']} pairs"
            if flagged:
                status += f", {flagged} flagged"
            print(f"  {entry_id_str}: {status}")
            reviewed += 1

        if entry_id_str != entry_ids[-1]:
            time.sleep(RATE_LIMIT_INTERVAL)

    if not dry_run:
        print(f"\nDeep review complete. Reviewed: {reviewed}, Flagged: {flagged_total}, "
              f"Skipped: {skipped}, Est. cost: ${total_cost:.4f}")


def build_review_prompt(entry, pairs):
    """Build the review prompt to send to the external model."""
    word = entry.get("headword", "")
    reading = entry.get("reading", "")
    pos = entry.get("part_of_speech", "")

    # Deduplicate for the review prompt to avoid redundant checks
    unique_pairs = deduplicate_pairs(pairs)

    pair_lines = []
    for i, p in enumerate(unique_pairs, 1):
        ctx = trim_context(p.get("context_after", ""))
        # Show the kanji with its reading and trailing context for okurigana visibility
        display = f'{p["kanji"]} → {p["reading"]}'
        if ctx:
            display += f'  (followed by: 「{ctx}」)'
        pair_lines.append(f'{i}. Field: {p["field"]} — {display}')

    pairs_text = "\n".join(pair_lines)

    prompt = f"""You are reviewing furigana readings in a Japanese-English dictionary entry.

Entry: {word} ({reading}) — {pos}

IMPORTANT — Furigana format in this dictionary:
The format is {{kanji|reading}}okurigana, where the reading covers ONLY the kanji portion.
The hiragana that follows outside the braces is okurigana (verb/adjective endings).
For example:
- {{走|はし}}る → 走 is read as はし, る is okurigana → full word is はしる (to run). はし is CORRECT.
- {{食|た}}べる → 食 is read as た, べる is okurigana → full word is たべる (to eat). た is CORRECT.
- {{美|うつく}}しい → 美 is read as うつく, しい is okurigana → full word is うつくしい (beautiful). うつく is CORRECT.
- {{気持|きも}}ち → 気持 is read as きも, ち is okurigana → full word is きもち (feeling). きも is CORRECT.
- {{値下|ねさ}}げ → 値下 is read as ねさ, げ is okurigana → full word is ねさげ (price cut). ねさ is CORRECT.
- {{一休|ひとやす}}み → 一休 is read as ひとやす, み is okurigana → full word is ひとやすみ (a rest). ひとやす is CORRECT.
- {{首飾|くびかざ}}り → 首飾 is read as くびかざ, り is okurigana → full word is くびかざり (necklace). くびかざ is CORRECT.
DO NOT flag these partial readings as errors — they are correct by design.

The 「...」 "followed by" context after each pair shows what comes after the furigana
markup. If the text after shows hiragana that completes a word, those are okurigana.
That excerpt is cut to a fixed display length and may stop early — judge only the
"kanji → reading" pair itself, and never infer a truncated or incomplete reading
from the excerpt.

Pairs to check:
{pairs_text}

For each pair, respond with a JSON array:
[
  {{
    "index": 1,
    "kanji": "漢字",
    "reading": "かんじ",
    "correct": true,
    "concern": null
  }}
]

Rules:
- CRITICAL: Readings cover only the kanji portion. Okurigana (hiragana endings) appear separately outside the markup. Do NOT flag a reading as wrong just because it is a "partial" reading of a verb/adjective/compound.
- Only flag genuinely incorrect readings where the kanji-to-reading mapping is wrong.
- Standard readings for common words are acceptable (e.g., 今日 as きょう, 明日 as あした, 大人 as おとな).
- Context-dependent readings: consider the part of speech and example sentence context when judging.
- Rendaku (sequential voicing) in compounds is normal (e.g., 小屋 as ごや in 山小屋).
- On'yomi vs. kun'yomi: verify the correct reading type for the context.
- If a reading is incorrect or questionable, set "correct" to false and explain in "concern".
- IMPORTANT: Before flagging a reading, double-check that your concern matches the SPECIFIC kanji-reading pair at that index. Do not confuse readings from different pairs.
- IMPORTANT: Compound words may have non-standard readings. For example, 見栄っ張り reads 張 as ぱ — this is correct.
- When in doubt, mark the reading as correct. Only flag readings you are confident are wrong.

Respond ONLY with the JSON array, no other text."""

    return prompt, unique_pairs


def call_openrouter(api_key, model, prompt, timeout=60):
    """Call the OpenRouter API and return the parsed response."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/tkgally/je-dict-1",
        "X-Title": "je-dict-1 furigana review",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 4096,
    }

    for attempt in range(3):
        try:
            if HAS_REQUESTS:
                resp = requests.post(
                    OPENROUTER_API_URL,
                    headers=headers,
                    json=payload,
                    timeout=timeout,
                )
                if resp.status_code == 429 or resp.status_code >= 500:
                    wait = 2 ** (attempt + 1)
                    print(f"  HTTP {resp.status_code}, retrying in {wait}s...", file=sys.stderr)
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                return resp.json()
            else:
                data = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    OPENROUTER_API_URL,
                    data=data,
                    headers=headers,
                    method="POST",
                )
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            if attempt < 2:
                wait = 2 ** (attempt + 1)
                print(f"  Error: {e}, retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"  Failed after 3 attempts: {e}", file=sys.stderr)
                return None
    return None


def extract_message_text(response_data):
    """Return the model's text output, or None.

    Defensive against the failure modes observed in production:
    - 2026-06-09: content is None (gemini null response) -> .strip() crashed.
    - 2026-06-10: gemini-2.5-pro returns empty content with the actual text in
      the message's 'reasoning' field via OpenRouter.
    """
    if not response_data:
        return None
    try:
        msg = response_data["choices"][0]["message"]
    except (KeyError, IndexError, TypeError):
        return None
    if not isinstance(msg, dict):
        return None
    content = msg.get("content")
    if not isinstance(content, str) or not content.strip():
        content = msg.get("reasoning")
    if not isinstance(content, str) or not content.strip():
        return None
    return content.strip()


def strip_code_fences(content):
    if content.startswith("```json"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    return content.strip()


def parse_model_response(response_data):
    """Extract JSON array from the model's response text."""
    content = extract_message_text(response_data)
    if content is None:
        print("  Failed to parse response: empty or missing content", file=sys.stderr)
        return None
    content = strip_code_fences(content)

    parsed = None
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        # Try to find JSON array in the text
        match = re.search(r'\[.*\]', content, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
            except json.JSONDecodeError:
                pass
    if parsed is None:
        print(f"  Failed to parse response: {content[:200]}...", file=sys.stderr)
        return None
    # Some models wrap the array in an object despite instructions.
    if isinstance(parsed, dict):
        for key in ("results", "issues", "pairs"):
            if isinstance(parsed.get(key), list):
                return parsed[key]
    return parsed


def classify_severity(results_by_model, unique_pairs):
    """Classify each pair's severity based on model agreement."""
    issues = []

    for i, pair in enumerate(unique_pairs):
        idx = i + 1  # 1-based index
        flags = {}  # model -> (correct, concern)

        for model, results in results_by_model.items():
            if results is None:
                continue
            for r in results:
                if r.get("index") == idx:
                    flags[model] = (r.get("correct", True), r.get("concern"))
                    break

        incorrect_count = sum(1 for correct, _ in flags.values() if not correct)
        total_models = len(flags)

        if total_models == 0:
            severity = "ok"
        elif incorrect_count == 0:
            severity = "ok"
        elif incorrect_count == 1 and total_models > 1:
            severity = "warning"
        else:
            severity = "error"

        for model, (correct, concern) in flags.items():
            issues.append({
                "field": pair["field"],
                "kanji": pair["kanji"],
                "reading": pair["reading"],
                "model": model,
                "correct": correct,
                "concern": concern,
                "severity": severity,
            })

    return issues


def review_entry(entry, entry_id_str, api_key, models, dry_run=False):
    """Review a single entry and return the report."""
    pairs = extract_furigana_pairs(entry)
    if not pairs:
        print(f"  {entry_id_str}: No furigana pairs found, skipping.")
        return None

    prompt, unique_pairs = build_review_prompt(entry, pairs)

    if dry_run:
        print(f"\n{'='*60}")
        print(f"Entry: {entry_id_str} — {entry.get('headword', '')} ({entry.get('reading', '')})")
        print(f"Furigana pairs: {len(pairs)} total, {len(unique_pairs)} unique")
        print(f"{'='*60}")
        print(prompt)
        print(f"{'='*60}\n")
        return None

    results_by_model = {}
    for model in models:
        print(f"  Querying {model}...")
        response = call_openrouter(api_key, model, prompt)
        parsed = parse_model_response(response)
        if parsed is None:
            print(f"  WARNING: Failed to get valid response from {model}")
        results_by_model[model] = parsed
        # Rate limiting
        if model != models[-1]:
            time.sleep(RATE_LIMIT_INTERVAL)

    issues = classify_severity(results_by_model, unique_pairs)

    flagged = [i for i in issues if not i["correct"]]
    ok = [i for i in issues if i["correct"]]

    # Count unique flagged pairs
    flagged_pairs = set()
    for i in flagged:
        flagged_pairs.add((i["kanji"], i["reading"]))

    # Count models agreeing on flags
    models_agreeing = 0
    for kanji, reading in flagged_pairs:
        flagging_models = set()
        for i in issues:
            if i["kanji"] == kanji and i["reading"] == reading and not i["correct"]:
                flagging_models.add(i["model"])
        if len(flagging_models) > 1:
            models_agreeing += 1

    report = {
        "entry_id": entry_id_str,
        "word": entry.get("headword", ""),
        "reading": entry.get("reading", ""),
        "reviewed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "models_used": models,
        "furigana_pairs_checked": len(unique_pairs),
        "issues": issues,
        "summary": {
            "total_checked": len(unique_pairs),
            "flagged": len(flagged_pairs),
            "ok": len(unique_pairs) - len(flagged_pairs),
            "models_agreeing_on_flags": models_agreeing,
        },
    }

    return report


def save_report(report):
    """Save a review report to the reviews directory."""
    REVIEWS_DIR.mkdir(exist_ok=True)
    path = REVIEWS_DIR / f"{report['entry_id']}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    return path


def generate_summary_report():
    """Summarize all existing review results, including screening stats."""
    # Screening stats
    if SCREENING_DIR.exists():
        screening_files = [f for f in sorted(SCREENING_DIR.glob("*.json"))
                           if f.name != "screening_status.json"]
        screened_total = len(screening_files)
        screened_flagged = 0
        for f in screening_files:
            try:
                with open(f) as fh:
                    data = json.load(fh)
                if data.get("flagged"):
                    screened_flagged += 1
            except (json.JSONDecodeError, IOError):
                pass

        total_entries_est = len(list(ENTRIES_DIR.glob("**/*.json")))
        print(f"Screening Status")
        print(f"{'='*40}")
        print(f"Entries screened:      {screened_total}")
        print(f"Entries flagged:       {screened_flagged}")
        print(f"Total entries:         {total_entries_est}")
        pct = (screened_total / total_entries_est * 100) if total_entries_est else 0
        print(f"Screening coverage:    {pct:.1f}%")
        if screened_total > 0:
            flag_rate = screened_flagged / screened_total * 100
            print(f"Flag rate:             {flag_rate:.1f}%")
        print()

    # Deep review stats
    if not REVIEWS_DIR.exists():
        print("No reviews directory found.")
        return

    json_files = sorted(f for f in REVIEWS_DIR.glob("*.json")
                         if f.parent == REVIEWS_DIR)
    if not json_files:
        print("No deep review files found.")
        return

    total_entries = 0
    total_pairs = 0
    total_flagged = 0
    total_ok = 0
    flagged_entries = []
    model_agreement = 0
    model_disagreement = 0

    for f in json_files:
        with open(f) as fh:
            report = json.load(fh)

        total_entries += 1
        s = report.get("summary", {})
        total_pairs += s.get("total_checked", 0)
        total_flagged += s.get("flagged", 0)
        total_ok += s.get("ok", 0)

        if s.get("models_agreeing_on_flags", 0) > 0:
            model_agreement += s["models_agreeing_on_flags"]
        flagged_count = s.get("flagged", 0)
        if flagged_count > s.get("models_agreeing_on_flags", 0):
            model_disagreement += flagged_count - s.get("models_agreeing_on_flags", 0)

        if s.get("flagged", 0) > 0:
            flagged_entries.append(report)

    print(f"Deep Review Summary")
    print(f"{'='*40}")
    print(f"Entries reviewed:      {total_entries}")
    print(f"Total pairs checked:   {total_pairs}")
    print(f"Pairs OK:              {total_ok}")
    print(f"Pairs flagged:         {total_flagged}")
    print(f"Entries with flags:    {len(flagged_entries)}")
    if model_agreement + model_disagreement > 0:
        agree_pct = model_agreement / (model_agreement + model_disagreement) * 100
        print(f"Model agreement rate:  {agree_pct:.1f}%")
    print()

    if flagged_entries:
        print(f"Flagged entries:")
        print(f"{'-'*40}")
        for report in flagged_entries:
            entry_id = report["entry_id"]
            word = report.get("word", "")
            flagged_issues = [i for i in report["issues"] if not i["correct"]]
            for issue in flagged_issues:
                severity = issue["severity"]
                model = issue["model"]
                concern = issue.get("concern", "")
                print(f"  {entry_id} {word}: {issue['kanji']}→{issue['reading']} "
                      f"[{severity}] ({model}) {concern or ''}")


def resolve_entry_ids(args):
    """Resolve command-line arguments to a list of entry ID strings."""
    ids = []
    if args.ids:
        for id_str in args.ids.split(","):
            id_str = id_str.strip()
            if id_str:
                ids.append(id_str.zfill(5))
    elif args.range:
        start, end = args.range
        for i in range(start, end + 1):
            ids.append(f"{i:05d}")
    return ids


def main():
    parser = argparse.ArgumentParser(
        description="Multi-model review runner for furigana correctness."
    )
    parser.add_argument("--range", nargs=2, type=int, metavar=("START", "END"),
                        help="Review entries in ID range (inclusive)")
    parser.add_argument("--ids", type=str,
                        help="Comma-separated entry IDs to review")
    parser.add_argument("--dry-run", action="store_true",
                        help="Format prompts and print them without sending")
    parser.add_argument("--model", type=str,
                        help="Use only one model (for testing)")
    parser.add_argument("--pass", dest="review_pass", type=str, choices=["screening", "deep"],
                        help="Review pass type: 'screening' (cheap, bulk) or 'deep' (multi-model)")
    parser.add_argument("--budget", type=float, metavar="AMOUNT",
                        help="Stop processing when estimated cost exceeds AMOUNT (USD)")
    parser.add_argument("--report", action="store_true",
                        help="Summarize existing review results")

    args = parser.parse_args()

    if args.report:
        generate_summary_report()
        return

    # Two-pass pipeline
    if args.review_pass == "screening":
        if not args.range and not args.ids:
            print("ERROR: --pass screening requires --range or --ids", file=sys.stderr)
            return
        api_key = None if args.dry_run else get_api_key()
        model = args.model or SCREENING_MODEL
        entry_ids = resolve_entry_ids(args)
        run_screening_pass(entry_ids, api_key, model, dry_run=args.dry_run, budget=args.budget)
        return

    if args.review_pass == "deep":
        api_key = None if args.dry_run else get_api_key()
        models = [args.model] if args.model else DEEP_MODELS
        if args.ids:
            # Explicit IDs are reviewed as given.
            entry_ids = resolve_entry_ids(args)
        elif args.range:
            # A range restricts the screening-flagged set — it does NOT deep-
            # review every entry in the range (that burned ~10x the intended
            # budget in the 2026-06-10 test run before being caught).
            lo, hi = args.range
            flagged = get_flagged_entry_ids()
            entry_ids = [e for e in flagged
                         if e.isdigit() and lo <= int(e) <= hi]
            print(f"Deep pass over range {lo}-{hi}: "
                  f"{len(entry_ids)} screening-flagged entries")
            if not entry_ids:
                print("No screening-flagged entries in range. "
                      "Run the screening pass first, or use --ids.")
                return
        else:
            entry_ids = []
        run_deep_pass(entry_ids, api_key, models, dry_run=args.dry_run, budget=args.budget)
        return

    # Original mode (no --pass flag)
    if not args.range and not args.ids:
        parser.print_help()
        return

    api_key = None
    if not args.dry_run:
        api_key = get_api_key()

    models = DEFAULT_MODELS
    if args.model:
        models = [args.model]

    entry_ids = resolve_entry_ids(args)
    print(f"Processing {len(entry_ids)} entries with models: {', '.join(models)}")
    if args.dry_run:
        print("DRY RUN — prompts will be printed but not sent.\n")

    reviewed = 0
    skipped = 0
    flagged_total = 0

    for entry_id_str in entry_ids:
        entry_path = find_entry_file(entry_id_str)
        if not entry_path:
            print(f"  {entry_id_str}: Entry file not found, skipping.")
            skipped += 1
            continue

        entry = load_entry(entry_path)
        print(f"Reviewing {entry_id_str}: {entry.get('headword', '')} ({entry.get('reading', '')})")

        report = review_entry(entry, entry_id_str, api_key, models, dry_run=args.dry_run)

        if report:
            save_report(report)
            flagged = report["summary"]["flagged"]
            flagged_total += flagged
            status = f"✓ {report['summary']['total_checked']} pairs"
            if flagged:
                status += f", {flagged} flagged"
            print(f"  {entry_id_str}: {status}")
            reviewed += 1

        # Rate limit between entries
        if not args.dry_run and entry_id_str != entry_ids[-1]:
            time.sleep(RATE_LIMIT_INTERVAL)

    if not args.dry_run:
        print(f"\nDone. Reviewed: {reviewed}, Skipped: {skipped}, Total flagged: {flagged_total}")
        print(f"Reports saved to: {REVIEWS_DIR}/")


if __name__ == "__main__":
    main()
