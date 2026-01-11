# Japanese-English Learner's Dictionary

A Japanese-English learner's dictionary emphasizing quality over quantity, delivered as a static website. It is being produced by [Tom Gally](https://www.gally.net/about.html).

## Overview

This dictionary is designed for learners of Japanese as a second language. Its features include:

- **Explanatory definitions** that go beyond simple glosses
- **Natural example sentences** optimized for learning
- **Usage notes** covering grammar, register, and common patterns
- **Rich particle and auxiliary verb entries** crucial for learners
- **Furigana support** with toggle to show/hide readings above kanji
- **Audio pronunciation** for some example sentences with play/stop controls (More will be added in the future.)
- **Multiple interface modes**: Search, Browse, Recent, and Random views
- **Transitivity and aspect information** for verbs
- **Collocation patterns** showing natural word combinations
- **Keigo (honorific) verb coverage** with usage guidance

## Current Status

- **2,834 entries** covering N5 vocabulary (complete), N4 vocabulary (in progress), and N3 vocabulary (started)
- **1,028 audio files** with pronunciation for example sentences
- **Claude Code skills** for consistent entry creation and revision
- **Entry tracking system** with `entries_index.json` for current entries and `candidate_words.json` for future additions
- **400 cross-references** with 95% resolution rate

**Live site**: https://tkgally.github.io/je-dict-1/

## Target Users

Intermediate learners of Japanese who:
- Can read hiragana and katakana fluently
- Know some kanji and are building vocabulary
- Want to deeply understand words, not just look them up quickly

## Technology

The dictionary is built as a **completely static website**:
- No server required—just open `index.html` directly in your browser
- No external dependencies—pure HTML, CSS, and JavaScript
- Offline-capable—download and use anywhere

## Site Structure

The dictionary is built as a static HTML site at `docs/`:

- **Individual pages**: Each entry has its own standalone HTML file
- **Works without JavaScript**: Core functionality requires no JS
- **Lightweight pages**: Each page loads only the content needed
- **Deep linking**: Direct URLs to specific entries
- **Native audio controls**: HTML5 audio elements for pronunciation

### URL Structure

Entry pages are organized by kana row and prefix (first 2 characters of entry ID):
```
docs/
├── index.html           # Home page
├── search.html          # Search interface
├── browse.html          # Browse by kana row
├── recent.html          # Recently modified entries
├── random.html          # Random word cloud
├── entries/
│   ├── a/               # あ行 entries
│   │   ├── a_/          # Entries with IDs starting 'a_'
│   │   │   └── a_00412.html
│   │   ├── ar/          # Entries with IDs starting 'ar'
│   │   │   └── aru_00001.html
│   │   └── ...
│   ├── ka/              # か行 entries
│   ├── sa/              # さ行 entries
│   └── ...
└── audio/               # Audio files (same structure)
    ├── a/
    │   ├── a_/
    │   └── ...
    └── ...
```

This prefix-based subdirectory structure allows the dictionary to scale to 10,000+ entries while staying within GitHub's 1,000 files per directory limit.

## Web Interface

The dictionary provides four different ways to explore entries:

### Search Mode
Quick lookup by Japanese, romaji, or English. The traditional dictionary experience for users who know what word they're looking for.

### Browse Mode
Filter and explore entries by:
- **JLPT Level**: N5, N4, or all
- **Part of Speech**: verbs, nouns, adjectives, adverbs, particles, counters, other
- **Starting Kana**: あ行, か行, さ行, etc.

Ideal for systematic vocabulary study or exploring categories.

### Recent Mode
View the most recently added or revised entries (up to 250). Each entry shows:
- **NEW**: Newly created entries
- **REVISED**: Updated existing entries
- Date of addition/revision

Useful for tracking dictionary updates and discovering new content.

### Random Mode
A word cloud of randomly selected entries. Click any word to view its full entry. Great for serendipitous discovery and vocabulary review.

More interface features will be added in the weeks ahead.

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

## Project Structure

```
je-dict-1/
├── entries/              # Dictionary entries (one JSON file per word)
│   ├── a/                # あ行 (a, i, u, e, o)
│   │   ├── a_/           # Entries with IDs starting 'a_'
│   │   ├── ar/           # Entries with IDs starting 'ar'
│   │   └── ...           # (prefix = first 2 chars of entry ID)
│   ├── ka/               # か行 (includes が行)
│   ├── sa/               # さ行 (includes ざ行)
│   ├── ta/               # た行 (includes だ行)
│   ├── na/               # な行
│   ├── ha/               # は行 (includes ば行, ぱ行)
│   ├── ma/               # ま行
│   ├── ya/               # や行
│   ├── ra/               # ら行
│   └── wa/               # わ行 (includes を, ん)
├── audio/                # Audio pronunciation files (MP3)
│   ├── a/                # あ行 entries
│   │   ├── a_/           # (same prefix structure as entries/)
│   │   └── ...
│   ├── ka/               # か行 entries
│   └── ...
├── audio-to-add/         # Staging directory for new audio files
├── build/                # Build and management scripts
│   ├── schema.json       # JSON schema for entries
│   ├── validate.py       # Entry validation (schema, cross-refs, audio integrity)
│   ├── build.py          # Main build script
│   ├── build_flat.py     # Static HTML site generator
│   ├── resolve_links.py  # Cross-reference resolution
│   ├── merge_audio.py    # Merges audio files into entries
│   ├── path_utils.py     # Shared path/prefix utilities
│   ├── japanese_utils.py # Hiragana/romaji conversion, kana mappings
│   ├── update_entries_index.py   # Updates entries_index.json
│   ├── manage_candidates.py      # Manages candidate_words.json
│   ├── update_indexes.py         # Updates both index files
│   └── requirements.txt  # Python 3.10+ dependencies
├── docs/                 # Generated output (served by GitHub Pages)
│   ├── entries/          # Individual entry HTML files
│   │   ├── a/            # (same prefix structure as entries/)
│   │   └── ...
│   └── audio/            # Built audio files (copied from audio/)
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
  "id": "taberu_00001",
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
      "japanese": "{朝|あさ}ごはんを{食|た}べましたか。",
      "english": "Did you eat breakfast?",
      "notes": null
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
    "confidence": "high",
    "review_status": "verified",
    "jlpt_level": "N5",
    "frequency_rank": null
  }
}
```

### File Naming Convention

Files use the format: `{romanized_reading}_{id}.json`

- Use Modified Hepburn romanization
- Long vowels follow kana spelling: 東京 → `toukyou`, not `tokyo`
- IDs are 5-digit zero-padded numbers
- Katakana loanwords use hiragana reading (e.g., アルバイト → `arubaito`)

### Directory Placement

Files go in directories based on the reading's first kana and the entry ID prefix:
- 食べる (たべる) → `entries/ta/ta/taberu_00001.json`
  - `ta/` = た行 (based on reading)
  - `ta/` = first 2 chars of `taberu_00001`
- 水 (みず) → `entries/ma/mi/mizu_00001.json`
  - `ma/` = ま行 (based on reading)
  - `mi/` = first 2 chars of `mizu_00001`

## Adding Audio Files

Audio pronunciation files can be added for example sentences. The web interface displays play/stop buttons for examples that have audio.

### Audio File Format

- **Format**: MP3 files
- **Filename**: `{entry_id}-ex{number}.mp3`
  - `entry_id`: The entry's ID (e.g., `taberu_00001`)
  - `number`: Example number (1-based, e.g., `ex1`, `ex2`, `ex3`)
- **Example**: `taberu_00001-ex1.mp3` for the first example of the entry `taberu_00001`

### Adding Audio Workflow

1. Place MP3 files in the `audio-to-add/` directory:
   ```
   audio-to-add/
   ├── taberu_00001-ex1.mp3
   ├── taberu_00001-ex2.mp3
   └── mizu_00001-ex1.mp3
   ```

2. Run the merge script to process the audio files:
   ```bash
   python3 build/merge_audio.py
   ```
   This will:
   - Copy MP3 files to `audio/{kana}/` (organized by entry reading)
   - Update entry files to set `has_audio: true` on the corresponding examples

3. Build the dictionary:
   ```bash
   python3 build/build.py
   ```
   This copies audio files to `docs/audio/` for the web interface.

### Directory Structure

Audio files are organized by kana and prefix (same as entries):
```
audio/
├── a/                    # あ行 entries
│   ├── a_/               # Entries with IDs starting 'a_'
│   │   └── a_00412-ex1.mp3
│   ├── am/               # Entries with IDs starting 'am'
│   │   └── ame_00044-ex1.mp3
│   └── ...
├── ka/                   # か行 entries
├── sa/                   # さ行 entries
└── ...
```

## Phased Roadmap

### Phase 1: Foundation ✓ COMPLETE
- [x] Project structure and schema
- [x] Build and validation scripts
- [x] Basic web interface
- [x] Furigana system with toggle

### Phase 2: Core Vocabulary ✓ COMPLETE
- [x] N5 vocabulary (~761 entries, 95% coverage)
- [x] Multi-model LLM evaluation
- [x] Quality specification v2
- [x] Entry revision to v2 standards

### Phase 3: Entry Enhancement ✓ COMPLETE
- [x] Add transitivity/aspect to all verbs
- [x] Expand particle entries with predicate lists
- [x] Add collocation patterns
- [x] Standardize adjective forms
- [x] Notes formatting with bullet points

### Phase 4: N4 Expansion & Interface (Current)
- [x] Added 392 N4 vocabulary entries
- [x] Multiple interface modes (Search, Browse, Recent, Random)
- [x] Sticky header with interface toggle and furigana button
- [x] Entry tracking system (`entries_index.json`, `candidate_words.json`)
- [x] Cross-reference linking system (400 references, 95% resolved)
- [x] Audio pronunciation for 1,028 example sentences
- [x] Static HTML site generation (flat HTML only)
- [x] Prefix-based subdirectory structure (scalable to 10,000+ entries)
- [x] Code quality improvements (shared utilities, deterministic builds)
- [ ] Continue adding vocabulary from candidate list (~1,980 candidates)
- [ ] Conjugation search indexing

### Phase 5: Polish and Distribution
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
| `revise-entries` | Checklist for revising existing entries to v2 standards |
| `vocabulary-notes` | Formatting guidelines for notes field |
| `cross-reference-entry` | Guidelines for adding cross-references between entries |

Skills are automatically loaded when Claude determines they're relevant to the current task.

### Workflow for Creating/Editing Entries

1. **Read PROJECT_STATUS.md** to understand current state
2. **Claude will automatically load relevant skills** based on the entry type being created/revised
3. **Follow the guidelines** from the loaded skills
4. **Validate entries** after creation: `python3 build/validate.py`
5. **Place files correctly** based on the reading's first kana
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

### Romanization Quick Reference

| Kana | Romaji | Directory |
|------|--------|-----------|
| あいうえお | a i u e o | /a/ |
| かきくけこ | ka ki ku ke ko | /ka/ |
| がぎぐげご | ga gi gu ge go | /ka/ |
| さしすせそ | sa shi su se so | /sa/ |
| たちつてと | ta chi tsu te to | /ta/ |
| なにぬねの | na ni nu ne no | /na/ |
| はひふへほ | ha hi fu he ho | /ha/ |
| まみむめも | ma mi mu me mo | /ma/ |
| やゆよ | ya yu yo | /ya/ |
| らりるれろ | ra ri ru re ro | /ra/ |
| わをん | wa wo n | /wa/ |

## License

TBD

## Contributing

Contributions by invitation only. The maintainer controls what gets merged to ensure quality standards are maintained.
