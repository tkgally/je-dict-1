# je-dict-1 — Japanese-English Learner's Dictionary

A dictionary for intermediate learners of Japanese who can read kana and are building vocabulary. The live site is at https://www.tkgje.jp/. It is a completely static site (HTML/CSS/JS, no server) hosted on GitHub Pages. Over 12,000 entries as of early 2026.

## Project structure

```
entries/          # Source dictionary entries as JSON (subdirs by ID range, 500 per dir)
docs/             # Generated static website (do NOT edit by hand — rebuilt by build_flat.py)
build/            # Python build, validation, and utility scripts
  build/templates/    # Standalone CSS and JS templates (styles.css, search.js, tag-search.js)
  build/tests/        # Unit tests (pytest)
  build/archive/      # One-time migration scripts (no longer used in regular operation)
  build/schema.json             # JSON schema for entry validation
  build/entry_renderer.py       # Entry page HTML generation
  build/page_generators.py      # Navigation page generation (index, browse, recent, etc.)
  build/search_index_builder.py # Search index and JS generation
  build/report.py               # Dictionary health dashboard
  build/generate_word_lookup.py # Builds word_id_lookup.json for inline link lookups
  build/manage_candidates.py    # Add/remove/check candidates in candidate_words.json
  build/find_missing_furigana.py # Scan entries for kanji missing furigana
  build/update_kanji_index.py   # Rebuild kanji JSON files; --check-new finds new kanji
  build/validate_tags.py        # Validate semantic/POS tag consistency
  build/get_next_id.py          # Get next available entry ID (scans filesystem)
kanji/            # Kanji index data (JSON files mapping kanji to entries)
pipeline/         # Automated task pipeline (run-pipeline.sh, validation gates, status tracking)
polishing/        # Progress tracking for entry polishing tasks
  polishing/tasks/{task}/progress.txt  # Next entry ID to process per task
  polishing/sessions/                  # Session logs (what was checked/changed)
prompts/          # Task prompts for interactive sessions
  prompts/batch/      # Shell runner scripts for non-interactive `claude --print` execution
  prompts/refactoring/  # Code refactoring prompts for build scripts
  prompts/expand-short-notes-tracking.txt  # Separate tracking file for expand-short-notes task
candidate_words.json   # Words queued for future entry creation
entries_index.json     # Master index of all entries (rebuilt by update_indexes.py)
build/word_id_lookup.json  # Pre-built word→entry_id map (for inline link lookups)
PROJECT_STATUS.md      # Session continuity notes and recent change log (keep 5 most recent)
PROJECT_CONTEXT_BRIEF.md # Quick-reference counts and rules for session start
.claude/skills/        # Reusable skill prompts for entry creation and maintenance
.github/workflows/     # GitHub Actions CI (validate.yml) and pipeline (pipeline.yml)
.githooks/             # Git hooks (pre-commit entry validation)
Makefile               # Build runner (make validate, make build, make quick, etc.)
```

## Entry basics

- Each entry is a JSON file at `entries/{range}/{id}_{romaji}.json`
- Range directory = ID rounded down to nearest 500 (e.g., ID 01186 → `entries/01000/`)
- Use `python3 build/get_entry_path.py <id> <romaji>` to get the correct path
- Entries must validate against `build/schema.json`
- All kanji must have furigana: `{漢字|かんじ}` — in headwords, examples, AND notes
- Readings are always hiragana, never katakana
- All new entries go in the **general** vocabulary tier
- New entries should include `"schema_version": "2.0"` in their metadata
- All explanations must be in English — Japanese text appears only in example phrases, collocations, and patterns
- Never add inline word links (⟦...⟧) during entry creation — those are added in a separate polishing step
- **Entry IDs must be unique.** Always run `python3 build/get_next_id.py` before creating each new entry to get the next available ID. This script scans the filesystem, so it is accurate even mid-session. Do not read `entries_index.json` or `PROJECT_CONTEXT_BRIEF.md` for the next ID — those may be stale. Do not reuse a previous result of `get_next_id.py` — run it fresh each time.
- **Never renumber existing entries.** The five-digit IDs form part of the entry's URL on the live site. Changing an ID would break external links and search-engine indexes.

## Essential commands

```bash
# Validation and building
python3 build/validate.py                 # Validate all entries against schema
python3 build/validate_tags.py            # Validate semantic/POS tag consistency
python3 build/update_indexes.py           # Update entries_index.json, candidate list, word lookup
python3 build/build_flat.py               # Full rebuild of the static site
python3 build/build_flat.py --quick       # Incremental build — only changed entries

# Entry creation helpers
python3 build/get_next_id.py                                     # Get next available entry ID (ALWAYS run before each new entry)
python3 build/check_duplicate.py "word" "reading"                # Check before creating an entry
python3 build/check_duplicate.py --skip-candidates "word" "reading"  # When creating FROM candidates
python3 build/get_entry_path.py <id> <romaji>       # Get correct file path for an entry
python3 build/get_timestamp.py            # Get current UTC timestamp for metadata

# Furigana and kanji
python3 build/verify_furigana.py <id>     # Check furigana coverage for one entry
python3 build/find_missing_furigana.py    # Scan all entries for missing furigana (pipe to head)
python3 build/update_kanji_index.py --check-new  # Check for new kanji needing IDs after entry creation

# Candidate management
python3 build/manage_candidates.py add "word" "reading" "gloss"   # Add a candidate
python3 build/manage_candidates.py check "word" "reading"         # Check if word exists as entry or candidate
python3 build/manage_candidates.py sync                           # Remove candidates that now exist as entries
python3 build/manage_candidates.py stats                          # Show candidate list statistics

# Reports
python3 build/report.py                   # Dictionary health dashboard

# Makefile shortcuts (recommended)
make build                                # validate + update_indexes + full build
make quick                                # validate + update_indexes + incremental build
make validate                             # validate only
make report                               # health dashboard
make check-furigana                       # find_missing_furigana scan
make check-kanji                          # verify kanji index integrity
make stats                                # tag statistics
make word-lookup                          # rebuild word_id_lookup.json
```

After creating or revising entries, always run: `make build` (or validate → update_indexes → build_flat).

## Post-creation validation sequence

After creating new entries (used by newentries prompts):

```bash
python3 build/validate.py                                # Fix any errors first
python3 build/find_missing_furigana.py | head -60        # Check for missing furigana
python3 build/update_indexes.py                          # Sync indexes and candidate list
python3 build/update_kanji_index.py --check-new          # Check for new kanji needing IDs
python3 build/build_flat.py                              # Rebuild the static site
```

If `find_missing_furigana.py` shows entries from the current session, fix them before building. If new kanji are found, assign on'yomi, kun'yomi, and gloss before building.

## Vocabulary tiers

- **Basic** (~800 entries) — foundational words; closed, do not add
- **Core** (~2,000 entries) — essential adult communication; closed, do not add
- **General** (9,000+ entries, growing) — all other vocabulary; all new entries go here

## Task prompts

The `prompts/` directory contains detailed instructions for each type of session task. Start a task by reading the prompt file (e.g., "Read prompts/newentries.md and follow the instructions"). Shell runner scripts in `prompts/batch/` automate tasks for non-interactive `claude --print` execution. `prompts/metaprompt_list.md` is a reference listing all available prompts with usage examples.

**Dictionary building:**
- `newentries.md` — create 30 entries from candidate_words.json
- `newcandidates.md` — find new candidate words to add
- `corpus_harvesting.md` — process corpus words into candidates (progress tracked in `corpus_harvesting_next_entry_number.txt`)
- `clean_up_candidates_list.md` — review and clean candidate_words.json
- `polish_add_entries_for_noentry_example_words.md` — create entries for words marked `noentry` in inline links

**Polishing (progress-tracked):**
- `polish_add_inline_links.md` — add ⟦...⟧ cross-reference links to examples/notes
- `polish_example_sentences.md` — check example count, quality, and vocabulary tier compliance
- `polish_furigana_completeness.md` — find and add missing furigana
- `polish_furigana_correctness.md` — verify existing furigana readings are correct
- `polish_semantic_labels.md` — verify semantic tags match word meanings
- `expand-short-notes.md` — expand inadequate notes (tracking in `prompts/expand-short-notes-tracking.txt`)

Polishing tasks track progress in `polishing/tasks/{task-name}/progress.txt` (format: `next: XXXXX`). They automatically resume where the previous session left off. Each session should commit in batches and write a session log to `polishing/sessions/`.

## Skills (detailed guidelines)

Detailed instructions for specific tasks live in `.claude/skills/`. Key ones:

- `entry-guidelines` — quality standards, file placement, metadata, tags (start here)
- `verb-entry` — transitivity, aspect/ている, particle patterns
- `adjective-entry` — forms, conjugations, predicate vs. modifier usage
- `particle-entry` — predicate lists, particle contrasts, fixed patterns
- `other-entries` — nouns, counters, adverbs, expressions
- `example-sentences` — minimum counts, progressive length, tier vocabulary restrictions
- `vocabulary-notes` — formatting and structure for the notes field
- `cross-reference-entry` — adding and maintaining cross-references
- `inline-word-links` — `⟦surface→base：entry_id⟧` links in examples and notes
- `find-candidates` — discovering new words to add to candidate_words.json
- `vocabulary-tiers` — tier criteria, word counts, self-containment principles
- `kanji-index` — kanji ID assignment, index updates
- `revise-entries` / `polish-entries` — improving existing entries
- `delete-entry` / `resolve-duplicates` — safe removal and deduplication

Invoke a skill with `/<skill-name>` (e.g., `/verb-entry`) to load its full instructions.
