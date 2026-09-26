# je-dict-1 — Session Context Brief

Quick-reference for AI assistants at session start. For full history, see [PROJECT_STATUS.md](PROJECT_STATUS.md).

## Current Counts

| Metric | Value |
|--------|-------|
| Total entries | 30,867 |
| Basic tier | 801 (closed) |
| Core tier | 1,982 (closed) |
| General tier | 28,084 (open — all new entries here) |
| Next entry ID | 31077 |
| Candidate words | 113 |
| Cross-references | ~77,800 |
| Example sentences | ~120,000 |

## Critical Rules

1. **All new entries → general tier.** Basic and core are frozen.
2. **All kanji must have furigana**: `{漢字|かんじ}` — in headwords, examples, AND notes.
3. **Readings are always hiragana**, never katakana.
4. **New entries include** `"schema_version": "2.0"` in metadata.
5. **Run duplicate check before creating any entry**: `python3 build/check_duplicate.py --skip-candidates "word" "reading"`
6. **Timestamps from script only**: `python3 build/get_timestamp.py`
7. **Inline links are placed by `build/auto_link.py`**, never by hand (CLAUDE.md, Entry rules).

## Essential Commands

```bash
python3 build/get_next_id.py                      # Fresh ID, immediately before each new entry
python3 build/get_entry_path.py <id> <romaji>     # Correct file path for an entry
python3 build/get_timestamp.py                    # UTC timestamp for metadata
python3 build/check_duplicate.py --skip-candidates "word" "reading"   # Duplicate check
make mechanical IDS=<ids>  # After changing entries: notes, links, cross-references, validation
make gate                  # The checks CI runs on a PR
make index                 # Indexes, kanji, has_audio flags (last step before commit)
make report                # Dictionary health dashboard
```

## File Placement

- Path: `entries/{range}/{id}_{romaji}.json`
- Range = ID rounded down to nearest 500 (e.g., 31077 → `entries/31000/`)
- Use `python3 build/get_entry_path.py <id> <romaji>` to confirm

## Vocabulary Tier Policy

- **Basic** (801): Foundational words. Closed — do not add or modify.
- **Core** (1,982): Essential adult communication. Closed — do not add or modify.
- **General** (28,084+): All other vocabulary. All new entries go here.

## Skills

Detailed task instructions live in `.claude/skills/`. Start with `entry-guidelines` for general quality standards. Use `verb-entry`, `adjective-entry`, `particle-entry`, or `other-entries` for type-specific guidance.

## Finishing a Session

Follow CLAUDE.md ("Sessions: start, work, finish"): `make gate`, then `make index`, commit
everything, push, open the PR, wait for CI, squash-merge. Do not run `make build` or commit
`docs/`: GitHub Actions builds and deploys the site after the merge.
