# Quick State Recovery for Polishing Sessions

This file helps new sessions quickly understand the current state and continue work.

## Finding Where to Continue

### 1. Check the Latest Session Log

```bash
ls -t polishing/sessions/ | head -1
```

Read that file—it contains:
- The exact next entry number to start from
- Context and patterns from the previous session
- Any pending tasks or notes

### 2. Quick Progress Check

```bash
# Total progress
python3 -c "import json; p=json.load(open('polishing/progress.json')); print(f\"Reviewed: {p['statistics']['reviewed']}/{p['statistics']['total_entries']} ({100*p['statistics']['reviewed']/p['statistics']['total_entries']:.1f}%)\")"

# Current batch start
python3 -c "import json; p=json.load(open('polishing/progress.json')); print(f\"Current batch starts at: {p['statistics'].get('current_batch_start', 'unknown')}\")"
```

### 3. Entry Directory Structure

Entries are in 500-entry directories:
- `entries/00000/` contains 00001-00499
- `entries/00500/` contains 00500-00999
- `entries/01000/` contains 01000-01499
- etc.

## Critical Reminders for Every Session

### Timestamps Are Per-Entry

**NEVER** generate one timestamp and reuse it for multiple entries. Each modified entry needs its own unique timestamp:

```bash
# Run this IMMEDIATELY BEFORE saving EACH entry you modify
python3 build/get_timestamp.py
```

### Verify ALL Fields (Not Just Examples)

The most common oversight is focusing only on examples. Always verify:
- **Semantic tags** match the word's actual meaning (watch for template artifacts like "building", "transportation" on unrelated words)
- **Formality/politeness** reflect the word's inherent register
- **Part of speech** and related tags are accurate

### Session Log is Your Handoff Document

Your session log in `polishing/sessions/` is how the next session knows where to continue. Always include:
- Entry range reviewed
- The **exact** next entry ID to process
- Any patterns discovered
- Any pending issues

## Common Commands

```bash
# Validation (run after each batch)
python3 build/validate.py
python3 build/validate_tags.py

# Check a word's tier
python3 build/check_duplicate.py "word" "reading"

# Add missing cross-reference target to candidates
python3 build/manage_candidates.py add "headword" "reading" "brief note"

# Update indexes after modifying entries
python3 build/update_indexes.py

# Build static site for review
python3 build/build_flat.py
```

## Workflow Summary

1. Read latest session log in `polishing/sessions/`
2. Review ~10 entries per batch
3. For each entry: verify all fields, fix issues, update timestamp (per-entry!)
4. Run validation scripts
5. Update session log with continuation notes
6. Commit changes
7. Repeat or create PR based on context remaining
