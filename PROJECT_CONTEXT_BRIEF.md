# je-dict-1 — Session Context Brief

Quick-reference for AI assistants at session start. For full history, see [PROJECT_STATUS.md](PROJECT_STATUS.md).

## Current Counts

| Metric | Value |
|--------|-------|
| Total entries | 11,016 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | 8,217 (open — all new entries here) |
| Next entry ID | 11025 |
| Candidate words | 160 |
| Cross-references | ~3,332 |
| Example sentences | ~41,820 |

## Critical Rules

1. **All new entries → general tier.** Basic and core are frozen.
2. **All kanji must have furigana**: `{漢字|かんじ}` — in headwords, examples, AND notes.
3. **Readings are always hiragana**, never katakana.
4. **New entries include** `"schema_version": "2.0"` in metadata.
5. **Run duplicate check before creating any entry**: `python3 build/check_duplicate.py --skip-candidates "word" "reading"`
6. **Timestamps from script only**: `python3 build/get_timestamp.py`
7. **Never add inline word links (⟦...⟧) during entry creation** — those are added in a separate polishing step.

## Essential Commands

```bash
make validate              # Validate all entries
make build                 # Full pipeline: validate + update_indexes + build
make quick                 # Incremental build (changed entries only)
make report                # Dictionary health dashboard
python3 build/get_entry_path.py <reading> <id>   # Correct file path for an entry
python3 build/get_timestamp.py                    # UTC timestamp for metadata
python3 build/check_duplicate.py "word" "reading" # Duplicate check
```

## File Placement

- Path: `entries/{range}/{id}_{romaji}.json`
- Range = ID rounded down to nearest 500 (e.g., 10327 → `entries/10000/`)
- Use `python3 build/get_entry_path.py <reading> <id>` to confirm

## Vocabulary Tier Policy

- **Basic** (801): Foundational words. Closed — do not add or modify.
- **Core** (1,998): Essential adult communication. Closed — do not add or modify.
- **General** (7,504+): All other vocabulary. All new entries go here.

## Skills

Detailed task instructions live in `.claude/skills/`. Start with `entry-guidelines` for general quality standards. Use `verb-entry`, `adjective-entry`, `particle-entry`, or `other-entries` for type-specific guidance.

## After Each Session

1. Run `make build` (or `make quick` for incremental).
2. Update `PROJECT_STATUS.md` Recent Changes section (keep only 5 most recent; rotate oldest to archive).
3. Commit and push.
