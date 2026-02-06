# je-dict-1 — Japanese-English Learner's Dictionary

A dictionary for intermediate learners of Japanese who can read kana and are building vocabulary. The live site is at https://www.tkgje.jp/. It is a completely static site (HTML/CSS/JS, no server) hosted on GitHub Pages.

## Project structure

```
entries/          # Source dictionary entries as JSON (subdirs by ID range, 500 per dir)
docs/             # Generated static website (do NOT edit by hand — rebuilt by build_flat.py)
build/            # Python build, validation, and utility scripts
kanji/            # Kanji index data (JSON files mapping kanji to entries)
candidate_words.json   # Words queued for future entry creation
entries_index.json     # Master index of all entries (rebuilt by update_indexes.py)
PROJECT_STATUS.md      # Session continuity notes and project roadmap
.claude/skills/        # Reusable skill prompts for entry creation and maintenance
```

## Entry basics

- Each entry is a JSON file at `entries/{range}/{id}_{romaji}.json`
- Range directory = ID rounded down to nearest 500 (e.g., ID 01186 → `entries/01000/`)
- Use `python3 build/get_entry_path.py <reading> <entry_id>` to get the correct path
- Entries must validate against `build/schema.json`
- All kanji must have furigana: `{漢字|かんじ}` — in headwords, examples, AND notes
- Readings are always hiragana, never katakana
- All new entries go in the **general** vocabulary tier

## Essential commands

```bash
python3 build/validate.py                 # Validate all entries
python3 build/verify_furigana.py <id>     # Check furigana coverage for one entry
python3 build/check_duplicate.py "word" "reading"  # Check before creating an entry
python3 build/get_entry_path.py <reading> <id>     # Get correct file path for an entry
python3 build/get_timestamp.py            # Get current UTC timestamp for metadata
python3 build/update_indexes.py           # Update entries_index.json and candidate list
python3 build/build_flat.py               # Rebuild the static site (required for changes to appear)
```

After creating or revising entries, always run: validate → update_indexes → build_flat.

## Vocabulary tiers

- **Basic** (795 entries) — foundational words; closed, do not add
- **Core** (1,998 entries) — essential adult communication; closed, do not add
- **General** (7,500+ entries) — all other vocabulary; all new entries go here

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
- `revise-entries` / `polish-entries` — improving existing entries
- `delete-entry` / `resolve-duplicates` — safe removal and deduplication

Invoke a skill with `/<skill-name>` (e.g., `/verb-entry`) to load its full instructions.
