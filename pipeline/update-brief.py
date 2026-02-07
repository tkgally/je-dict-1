#!/usr/bin/env python3
"""
Regenerate PROJECT_CONTEXT_BRIEF.md from current project state.

Reads entries_index.json (enriched with tier, POS, cross-reference, and
example data) and candidate_words.json to produce up-to-date counts
without loading individual entry files.

Usage:
    python3 pipeline/update-brief.py            # regenerate the brief
    python3 pipeline/update-brief.py --dry-run   # show what would be written
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
INDEX_FILE = PROJECT_DIR / "entries_index.json"
CANDIDATES_FILE = PROJECT_DIR / "candidate_words.json"
POLISHING_DIR = PROJECT_DIR / "polishing" / "tasks"
BRIEF_FILE = PROJECT_DIR / "PROJECT_CONTEXT_BRIEF.md"


def load_index() -> dict:
    """Load entries_index.json."""
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_candidates() -> dict:
    """Load candidate_words.json."""
    if not CANDIDATES_FILE.exists():
        return {"metadata": {"total_candidates": 0}, "candidates": []}
    with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def compute_stats(index_data: dict) -> dict:
    """Compute project statistics from the enriched index."""
    entries = index_data.get("entries", [])

    # Tier counts
    tier_counts = Counter()
    for entry in entries:
        tier = entry.get("vocabulary_tier", "unknown")
        tier_counts[tier] += 1

    # Total cross-references and examples
    total_xrefs = sum(entry.get("cross_reference_count", 0) for entry in entries)
    total_examples = sum(entry.get("example_count", 0) for entry in entries)

    # Next entry ID: find the max numeric ID and add 1
    max_numeric_id = 0
    for entry in entries:
        entry_id = entry.get("id", "")
        # Extract numeric prefix (e.g., "01234_abc" -> 1234)
        match = re.match(r"(\d+)", entry_id)
        if match:
            num = int(match.group(1))
            if num > max_numeric_id:
                max_numeric_id = num
    next_id = max_numeric_id + 1

    return {
        "total": len(entries),
        "basic": tier_counts.get("basic", 0),
        "core": tier_counts.get("core", 0),
        "general": tier_counts.get("general", 0),
        "next_id": next_id,
        "xrefs": total_xrefs,
        "examples": total_examples,
    }


def get_polishing_progress() -> dict[str, str]:
    """Read polishing progress.txt files and return task -> next ID mapping."""
    progress = {}
    if not POLISHING_DIR.exists():
        return progress
    for task_dir in sorted(POLISHING_DIR.iterdir()):
        progress_file = task_dir / "progress.txt"
        if progress_file.exists():
            content = progress_file.read_text().strip()
            # Parse "next: 01234" format
            match = re.match(r"next:\s*(\S+)", content)
            if match:
                progress[task_dir.name] = match.group(1)
    return progress


def round_to_approx(n: int) -> str:
    """Round to a nice approximate number for display (e.g., 3313 -> ~3,300)."""
    if n < 100:
        return str(n)
    if n < 1000:
        rounded = (n // 50) * 50
        return f"~{rounded:,}"
    rounded = (n // 100) * 100
    return f"~{rounded:,}"


def generate_brief(stats: dict, candidate_count: int) -> str:
    """Generate the PROJECT_CONTEXT_BRIEF.md content."""
    next_id_padded = f"{stats['next_id']:05d}" if stats["next_id"] < 100000 else str(stats["next_id"])
    next_range = (stats["next_id"] // 500) * 500

    lines = [
        "# je-dict-1 — Session Context Brief",
        "",
        "Quick-reference for AI assistants at session start. For full history, see [PROJECT_STATUS.md](PROJECT_STATUS.md).",
        "",
        "## Current Counts",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total entries | {stats['total']:,} |",
        f"| Basic tier | {stats['basic']:,} (closed) |",
        f"| Core tier | {stats['core']:,} (closed) |",
        f"| General tier | {stats['general']:,} (open — all new entries here) |",
        f"| Next entry ID | {next_id_padded} |",
        f"| Candidate words | {candidate_count:,} |",
        f"| Cross-references | {round_to_approx(stats['xrefs'])} |",
        f"| Example sentences | {round_to_approx(stats['examples'])} |",
        "",
        "## Critical Rules",
        "",
        "1. **All new entries → general tier.** Basic and core are frozen.",
        "2. **All kanji must have furigana**: `{漢字|かんじ}` — in headwords, examples, AND notes.",
        "3. **Readings are always hiragana**, never katakana.",
        '4. **New entries include** `"schema_version": "2.0"` in metadata.',
        '5. **Run duplicate check before creating any entry**: `python3 build/check_duplicate.py --skip-candidates "word" "reading"`',
        "6. **Timestamps from script only**: `python3 build/get_timestamp.py`",
        "7. **Never add inline word links (⟦...⟧) during entry creation** — those are added in a separate polishing step.",
        "",
        "## Essential Commands",
        "",
        "```bash",
        "make validate              # Validate all entries",
        "make build                 # Full pipeline: validate + update_indexes + build",
        "make quick                 # Incremental build (changed entries only)",
        "make report                # Dictionary health dashboard",
        "python3 build/get_entry_path.py <reading> <id>   # Correct file path for an entry",
        "python3 build/get_timestamp.py                    # UTC timestamp for metadata",
        'python3 build/check_duplicate.py "word" "reading" # Duplicate check',
        "```",
        "",
        "## File Placement",
        "",
        "- Path: `entries/{range}/{id}_{romaji}.json`",
        f"- Range = ID rounded down to nearest 500 (e.g., {next_id_padded} → `entries/{next_range:05d}/`)",
        "- Use `python3 build/get_entry_path.py <reading> <id>` to confirm",
        "",
        "## Vocabulary Tier Policy",
        "",
        f"- **Basic** ({stats['basic']:,}): Foundational words. Closed — do not add or modify.",
        f"- **Core** ({stats['core']:,}): Essential adult communication. Closed — do not add or modify.",
        f"- **General** ({stats['general']:,}+): All other vocabulary. All new entries go here.",
        "",
        "## Skills",
        "",
        "Detailed task instructions live in `.claude/skills/`. Start with `entry-guidelines` for general quality standards. Use `verb-entry`, `adjective-entry`, `particle-entry`, or `other-entries` for type-specific guidance.",
        "",
        "## After Each Session",
        "",
        "1. Run `make build` (or `make quick` for incremental).",
        "2. Update `PROJECT_STATUS.md` Recent Changes section (keep only 5 most recent; rotate oldest to archive).",
        "3. Commit and push.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate PROJECT_CONTEXT_BRIEF.md from current project state"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the generated content without writing the file",
    )
    args = parser.parse_args()

    # Load data
    if not INDEX_FILE.exists():
        print(f"Error: {INDEX_FILE} not found. Run 'python3 build/update_indexes.py' first.", file=sys.stderr)
        return 1

    index_data = load_index()
    candidates_data = load_candidates()
    candidate_count = len(candidates_data.get("candidates", []))

    stats = compute_stats(index_data)
    brief = generate_brief(stats, candidate_count)

    if args.dry_run:
        print(brief)
        print(f"\n--- Dry run: would write {len(brief)} bytes to {BRIEF_FILE} ---")
    else:
        BRIEF_FILE.write_text(brief, encoding="utf-8")
        print(f"Updated {BRIEF_FILE}")
        print(f"  Total entries: {stats['total']:,}")
        print(f"  Tiers: {stats['basic']} basic, {stats['core']} core, {stats['general']} general")
        print(f"  Candidates: {candidate_count}")
        print(f"  Next ID: {stats['next_id']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
