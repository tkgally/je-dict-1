# TKG Japanese-English Learner's Dictionary

This is the repository for a Japanese-English learner's dictionary delivered as a static website. Its production is being supervised by [Tom Gally](https://www.gally.net/about.html). All of the entry-writing and coding is being done by Claude Opus 4.5 in Claude Code for the Web, with some bug-hunting and improvement-suggesting by ChatGPT and Gemini.

This dictionary is licensed under Creative Commons Zero v1.0 Universal, and anyone is free to copy the data and code for whatever purpose they like, including commercial uses.

## Overview

This dictionary is designed for learners of Japanese as a second language. It uses an original three-tier vocabulary classification system:
- **Basic tier**: About one thousand fundamental words essential for basic communication
- **Core tier**: About two thousand needed for adult-level communication
- **General tier**: All other vocabulary useful for learners

Dictionary features include:

- **Explanatory definitions** that go beyond simple glosses
- **Natural example sentences** optimized for learning
- **Usage notes** covering grammar, register, and common patterns
- **Furigana support** with toggle to show/hide readings above kanji
- **Kanji index** linking each kanji in headwords to all other entries containing that kanji
- **Multiple interface modes**: Search, Browse, Recent, and Random views
- **Cross-reference linking** connecting related words, antonyms, and transitivity pairs
- **Transitivity and aspect information** for verbs
- **Collocation patterns** showing natural word combinations
- **Keigo (honorific) verb coverage** with usage guidance

Audio readings for example sentences will be added in the future.

## Current Status

- **Nearly 8,000 entries** with a target of about 10,000 entries
- **Vocabulary tiers assigned**: Basic (795), Core (1,998), General (4,926) - all new entries are added to general tier
- **Over 3,000 cross-references** linking related entries
- **Claude Code skills** for consistent entry creation and revision
- **Entry tracking system** with `entries_index.json` for current entries and `candidate_words.json` for future additions
- **Robust build system** with atomic builds, XSS protection, and comprehensive validation

**Live site**: https://www.tkgje.jp/

## Target Users

Intermediate learners of Japanese who:
- Can read hiragana and katakana fluently
- Know some kanji and are building vocabulary
- Want to understand words fully, not just look them up quickly

## Technology

The dictionary is built as a **completely static website**:
- No server required—just open `index.html` directly in your browser
- No external dependencies—pure HTML, CSS, and JavaScript
- Offline-capable—download and use anywhere

## Site Structure

The dictionary is built as a static HTML site at `docs/`:

- **Individual pages**: Each entry has its own standalone HTML file
- **Lightweight pages**: Each page loads only the content needed
- **Deep linking**: Direct URLs to specific entries

### URL Structure

Entry pages are organized by numeric ID ranges (500 entries per directory):
```
docs/
├── index.html           # Home page
├── search.html          # Search interface
├── browse.html          # Browse by kana row
├── recent.html          # Recently modified entries
├── random.html          # Random word cloud
├── entries/
│   ├── 00000/           # Entries 00000-00499
│   │   ├── 00396_taberu.html
│   │   └── 00499_sakana.html
│   ├── 00500/           # Entries 00500-00999
│   ├── 01000/           # Entries 01000-01499
│   └── ...
└── kanji/               # Kanji index pages
    ├── 00001_teki_mato_target.html
    ├── 00009_jin_hito_person.html
    └── ...              # One page per kanji
```

This numeric range structure allows the dictionary to scale to 10,000+ entries while staying within GitHub's 1,000 files per directory limit.

## Web Interface

The dictionary provides four different ways to explore entries:

### Search Mode
Quick lookup by Japanese, romaji, or English. The traditional dictionary experience for users who know what word they're looking for.

### Browse Mode
Explore entries organized by:
- **Starting Kana**: あ行, か行, さ行, etc.
- **Vocabulary Tier**: Basic (795 fundamental words), Core (1,998 adult-communication words), General (all other vocabulary)

The dictionary uses an original three-tier classification system instead of JLPT levels. All new entries are added to the general tier.

### Recent Mode
View the most recently added or revised entries (up to 250). Each entry shows:
- **NEW**: Newly created entries
- **REVISED**: Updated existing entries
- Date of addition/revision

Useful for tracking dictionary updates and discovering new content.

### Random Mode
A word cloud of randomly selected entries. Click any word to view its full entry. Great for serendipitous discovery and vocabulary review.

## Furigana System

The dictionary uses a custom notation for furigana (reading annotations above kanji):

### Format
```
{kanji|reading}
```

Examples:
- `{食|た}べる` → 食べる with た above 食
- `{友達|ともだち}` → 友達 with ともだち above it
- `{日本語|にほんご}が{分|わ}かる` → Multiple annotations in one sentence

### In the Web Interface
- Click the **Furigana** button in the header to toggle readings on/off
- When enabled, readings appear above kanji using HTML `<ruby>` tags
- Preference is saved in localStorage

## Kanji Index

The kanji index allows users to find all dictionary entries containing a specific kanji character.

### How It Works

1. **On entry pages**: Each kanji in the headword is a clickable link
2. **Hover tooltip**: Shows "Other words with this kanji" when hovering over a kanji
3. **Kanji page**: Clicking displays a page with the kanji and all entries containing it
4. **Entry list**: Sorted by hiragana reading order

### Kanji ID Format

Each kanji is identified by a unique ID:
```
{5-digit number}_{onyomi}_{kunyomi}_{gloss}
```

Examples:
- `00009_jin_hito_person` (人)
- `00116_kou_taka_tall` (高)
- `00431_yo_ama_surplus` (余)

The ID uses `none` when a kanji lacks on'yomi or kun'yomi.

### Technical Details

- **2,040 kanji** indexed from dictionary headwords
- **kanji_list.json**: Master mapping of kanji characters to IDs
- **Individual JSON files**: Entry lists for each kanji in `kanji/`
- **HTML pages**: Generated in `docs/kanji/` during site build
- **Automatic updates**: New kanji are detected and indexed when entries are added

## Project Structure

```
je-dict-1/
├── entries/              # Dictionary entries (one JSON file per word)
│   ├── 00000/            # Entries 00000-00499
│   ├── 00500/            # Entries 00500-00999
│   ├── 01000/            # Entries 01000-01499
│   └── ...               # (500 entries per directory)
├── kanji/                # Kanji index data
│   ├── kanji_list.json   # Master list mapping kanji to IDs
│   └── {kanji_id}.json   # Entry lists for each kanji
├── build/                # Build and management scripts
│   ├── schema.json       # JSON schema for entries
│   ├── validate.py       # Entry validation (schema, cross-refs)
│   ├── validate_tags.py  # Tag taxonomy validation
│   ├── build_flat.py     # Static HTML site generator (atomic builds)
│   ├── resolve_links.py  # Cross-reference resolution
│   ├── path_utils.py     # Shared path/prefix utilities
│   ├── japanese_utils.py # Hiragana/romaji/furigana utilities
│   ├── constants.py      # Centralized cross-reference type definitions
│   ├── update_entries_index.py   # Updates entries_index.json
│   ├── manage_candidates.py      # Manages candidate_words.json
│   ├── update_indexes.py         # Updates both index files
│   ├── get_entry_path.py         # Computes correct path for new entries
│   ├── get_timestamp.py          # Generates UTC timestamp for metadata
│   ├── check_duplicate.py        # Checks for duplicate entries
│   ├── verify_furigana.py        # Verifies furigana coverage
│   ├── harden_references.py      # Adds target_id to resolvable cross-refs
│   ├── extract_references.py     # Extracts cross-refs from notes
│   ├── tag_taxonomy.json         # Tag hierarchy definitions
│   ├── tag_statistics.py         # Tag usage statistics
│   ├── build_kanji_json.py       # Builds kanji entry list JSON files
│   ├── build_kanji_html.py       # Builds kanji index HTML pages
│   ├── update_kanji_index.py     # Updates kanji index for new entries
│   ├── verify_kanji_index.py     # Verifies kanji index integrity
│   └── requirements.txt  # Python 3.10+ dependencies
├── docs/                 # Generated output (served as static site)
│   ├── entries/          # Individual entry HTML files
│   │   ├── 00000/        # (same numeric range structure as entries/)
│   │   └── ...
│   └── kanji/            # Kanji index HTML pages
├── .claude/              # Claude Code configuration
│   ├── skills/           # Agent skills for entry guidelines (auto-loaded)
│   └── settings.json
├── entries_index.json    # Index of all dictionary entries
├── candidate_words.json  # Words to potentially add in future
├── project_specification_v2.md  # Quality standards from LLM evaluation
└── PROJECT_STATUS.md     # Session continuity file
```

### Entry Schema

Each entry is a JSON file with the following structure:

```json
{
  "id": "00396_taberu",
  "headword": "{食|た}べる",
  "reading": "たべる",
  "part_of_speech": "verb (ichidan)",
  "gloss": "to eat",
  "definitions": [
    {
      "sense_number": 1,
      "gloss": "to eat",
      "explanation": "The most common verb for eating..."
    }
  ],
  "examples": [
    {
      "id": "00396_taberu_ex1",
      "japanese": "{朝|あさ}ごはんを{食|た}べましたか。",
      "english": "Did you eat breakfast?",
      "notes": null,
      "sense_numbers": [1]
    }
  ],
  "notes": "Usage notes, grammar notes, etc.",
  "cross_references": [
    {
      "type": "pair",
      "reading": "たべもの",
      "headword": "{食|た}べ{物|もの}"
    }
  ],
  "metadata": {
    "created": "2026-01-05T10:00:00Z",
    "modified": "2026-01-05T10:00:00Z",
    "ai_model": "claude-opus-4-5",
    "vocabulary_tier": "basic"
  }
}
```

### Sense Numbers in Examples

The `sense_numbers` field on example sentences links each example to one or more definition senses:

- **Required for multi-sense entries**: Every example must specify which sense(s) it illustrates
- **Format**: Array of integers matching `sense_number` values in definitions (e.g., `[1]`, `[2]`, or `[1, 2]`)
- **Single-sense entries**: Use `[1]` for all examples
- **Multi-sense examples**: An example can illustrate multiple senses with `[1, 2]`

This enables future features like filtering examples by sense and helps learners understand which meaning each example demonstrates.

### File Naming Convention

Files use the format: `{id}_{romanized_reading}.json`

- IDs are 5-digit zero-padded numbers at the START of the filename
- Use Modified Hepburn romanization for the reading
- Long vowels follow kana spelling: 東京 → `toukyou`, not `tokyo`
- Katakana loanwords use hiragana reading (e.g., アルバイト → `arubaito`)

### Directory Placement

Files go in directories based on the numeric ID range (500 entries per directory):
- Entry 00396_taberu → `entries/00000/00396_taberu.json`
- Entry 00538_aruku → `entries/00500/00538_aruku.json`
- Entry 01186_mukau → `entries/01000/01186_mukau.json`

The directory name is determined by rounding down to the nearest 500:
- IDs 00000-00499 → `entries/00000/`
- IDs 00500-00999 → `entries/00500/`
- IDs 01000-01499 → `entries/01000/`

## Phased Roadmap

### Phase 1: Foundation ✓ COMPLETE
- [x] Project structure and schema
- [x] Build and validation scripts
- [x] Basic web interface
- [x] Furigana system with toggle

### Phase 2: Core Vocabulary ✓ COMPLETE
- [x] Basic vocabulary foundation (~761 entries)
- [x] Multi-model LLM evaluation
- [x] Quality specification v2
- [x] Entry revision to v2 standards

### Phase 3: Entry Enhancement ✓ COMPLETE
- [x] Add transitivity/aspect to all verbs
- [x] Expand particle entries with predicate lists
- [x] Add collocation patterns
- [x] Standardize adjective forms
- [x] Notes formatting with bullet points

### Phase 4: Vocabulary Expansion & Interface ✓ COMPLETE
- [x] Added ~7,000 additional vocabulary entries (7,719 total)
- [x] Multiple interface modes (Search, Browse, Recent, Random)
- [x] Sticky header with interface toggle and furigana button
- [x] Entry tracking system (`entries_index.json`, `candidate_words.json`)
- [x] Cross-reference linking system (3,195 references)
- [x] Static HTML site generation (flat HTML only)
- [x] Prefix-based subdirectory structure (scalable to 10,000+ entries)
- [x] Code quality improvements (shared utilities, deterministic builds)
- [x] Three-tier vocabulary system (basic 795, core 1,998, general 4,926)
- [x] Vocabulary tier realignment complete - all entries assigned
- [x] Tier-based filtering in Browse mode

### Phase 5: Continued Expansion (Current)
- [ ] Continue adding vocabulary toward 10,000 entries
- [ ] Add audio readings for example sentences
- [ ] Conjugation search indexing

### Phase 6: Polish and Distribution
- [ ] Offline package generation
- [ ] PWA features
- [ ] Export to Anki format
- [ ] Community feedback mechanism

## For AI Assistants

### Available Skills

The following skills are available in `.claude/skills/` and will be automatically invoked by Claude Code when relevant:

| Skill | Purpose |
|-------|---------|
| `entry-guidelines` | General quality standards for all entries |
| `verb-entry` | Requirements for verb entries (transitivity, aspect, collocations) |
| `adjective-entry` | Requirements for adjective entries (forms, conjugations) |
| `particle-entry` | Requirements for particle entries (predicate lists, contrasts) |
| `other-entries` | Requirements for nouns, counters, adverbs, expressions |
| `example-sentences` | Requirements for example sentences (counts, length, vocabulary) |
| `vocabulary-notes` | Formatting guidelines for notes field |
| `vocabulary-tiers` | Guidelines for the three-tier vocabulary system |
| `cross-reference-entry` | Guidelines for adding cross-references between entries |
| `find-candidates` | Guidelines for finding new candidate words to add |
| `revise-entries` | Checklist for revising existing entries to v2 standards |
| `polish-entries` | Systematic review and improvement of entries |
| `delete-entry` | Guidelines for safely deleting entries |
| `resolve-duplicates` | Guidelines for identifying and resolving duplicate entries |
| `kanji-index` | Guidelines for maintaining the kanji index feature |

Skills are automatically loaded when Claude determines they're relevant to the current task.

### Workflow for Creating/Editing Entries

1. **Read PROJECT_STATUS.md** to understand current state
2. **Claude will automatically load relevant skills** based on the entry type being created/revised
3. **Follow the guidelines** from the loaded skills
4. **Validate entries** after creation: `python3 build/validate.py`
5. **Place files correctly** based on the numeric ID range
6. **Update PROJECT_STATUS.md** at the end of each session

### Key Quality Standards (v2)

Based on multi-model LLM evaluation, these are HIGH PRIORITY for all entries:

**For Verbs:**
- Transitivity type and pair verb
- Aspect/ている behavior
- Common collocations

**For Particles:**
- List of predicates requiring this particle
- Contrast with similar particles

**For All Entries:**
- Examples progress from simple to complex
- At least one collocation or fixed phrase
- Consistent depth with similar entries

### Directory Structure Quick Reference

Entries are organized by numeric ID ranges (500 entries per directory):

| ID Range | Directory |
|----------|-----------|
| 00000-00499 | `entries/00000/` |
| 00500-00999 | `entries/00500/` |
| 01000-01499 | `entries/01000/` |
| ... | ... |

Use `python3 build/get_entry_path.py <reading> <entry_id>` to get the correct path for new entries.

## License

Creative Commons Zero v1.0 Universal

## Contributing

Email suggestions for enhancements to [Tom Gally](https://www.gally.net/about.html).
