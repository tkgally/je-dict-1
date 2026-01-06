# je-dict-1

A Japanese-English learner's dictionary emphasizing quality over quantity, delivered as a static website.

## Overview

**je-dict-1** is a dictionary designed for learners of Japanese as a second language. Unlike comprehensive resources like Jisho.org or JMdict, this dictionary prioritizes **depth and quality**—fewer entries, but each one carefully crafted with:

- **Explanatory definitions** that go beyond simple glosses
- **Natural example sentences** optimized for learning
- **Usage notes** covering grammar, register, and common patterns
- **Rich particle and auxiliary verb entries** crucial for learners
- **Furigana support** with toggle to show/hide readings above kanji

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
- Data is embedded in JavaScript at build time for maximum portability

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

### Rules for Entry Authors
1. **All kanji must have readings in hiragana** — we assume readers know hiragana/katakana but may not know kanji readings
2. **No romaji** — readings are always in hiragana, never romanized
3. **Apply to all fields** — headword, examples, notes, and explanations should all use furigana notation
4. **Compound readings** — for jukugo (kanji compounds), mark the entire compound: `{友達|ともだち}` not `{友|とも}{達|だち}`

## Project Structure

```
je-dict-1/
├── entries/          # Dictionary entries (one JSON file per word)
│   ├── a/            # あ行 (a, i, u, e, o)
│   ├── ka/           # か行 (includes が行)
│   ├── sa/           # さ行 (includes ざ行)
│   ├── ta/           # た行 (includes だ行)
│   ├── na/           # な行
│   ├── ha/           # は行 (includes ば行, ぱ行)
│   ├── ma/           # ま行
│   ├── ya/           # や行
│   ├── ra/           # ら行
│   └── wa/           # わ行 (includes を, ん)
├── variants/         # Alternate reading entries
├── build/            # Build scripts
│   ├── schema.json   # JSON schema for entries
│   ├── validate.py   # Entry validation script
│   ├── build.py      # Main build script
│   └── requirements.txt
├── web/              # Web application source
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── dist/             # Generated output (gitignored)
└── PROJECT_STATUS.md # Session continuity file
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd je-dict-1
   ```

2. Install Python dependencies:
   ```bash
   pip install -r build/requirements.txt
   ```

### Building the Dictionary

1. Validate all entries:
   ```bash
   python3 build/validate.py
   ```

2. Build the dictionary:
   ```bash
   python3 build/build.py
   ```

3. View locally:
   ```bash
   open dist/index.html
   ```
   Or just double-click `dist/index.html` in Finder. No server required!

## Creating Entries

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
  "cross_references": [],
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

### Directory Placement

Files go in directories based on the first kana of the reading:
- 食べる (たべる) → `entries/ta/taberu_00001.json`
- 水 (みず) → `entries/ma/mizu_00001.json`

## Phased Roadmap

### Phase 1: Foundation (Current)
- [x] Project structure and schema
- [x] Build and validation scripts
- [x] Basic web interface
- [x] Sample entries (47 entries)
- [x] Furigana system with toggle

### Phase 2: Core Vocabulary
- [ ] Complete N5 vocabulary (~800 words)
- [ ] Begin N4 vocabulary
- [ ] Reach critical mass (500-1000 entries)

### Phase 3: Conjugation and Search
- [ ] Implement conjugation indexing
- [ ] Enhanced search (better partial matching)
- [ ] Performance optimization if needed

### Phase 4: Content Expansion
- [ ] Complete N4, begin N3 vocabulary
- [ ] Implement cross-references
- [ ] Refine AI generation workflow

### Phase 5: Polish and Distribution
- [ ] Offline package generation
- [ ] PWA features
- [ ] Community feedback mechanism

## For AI Assistants

When creating or editing entries:

1. **Read PROJECT_STATUS.md first** to understand current state
2. **Validate entries** after creation: `python3 build/validate.py`
3. **Follow the schema** defined in `build/schema.json`
4. **Place files correctly** based on the reading's first kana
5. **Update PROJECT_STATUS.md** at the end of each session
6. **Use furigana notation** for all kanji: `{漢字|かんじ}`

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
