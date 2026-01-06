# Resume Working on je-dict-1

Point an AI assistant to this file when resuming work on this project.

---

## Quick Summary

**je-dict-1** is a Japanese-English learner's dictionary delivered as a static website. It emphasizes quality over quantity - fewer entries, but each with rich explanations, natural examples, and usage notes.

## Current Status

- **Phase**: Foundation complete, ready for content expansion
- **Entries**: 47 (verbs, nouns, adjectives, particles) - all with furigana
- **Infrastructure**: Fully functional (build scripts, web interface, sidebar browser)
- **Live site**: https://tkgally.github.io/je-dict-1/
- **Target**: 500-1000 entries for "critical mass"

## Key Files to Read

1. **`PROJECT_STATUS.md`** - Detailed current state, next steps, and technical notes
2. **`project_specification.md`** - Full project specification and design decisions
3. **`build/schema.json`** - Entry JSON schema
4. **`README.md`** - Usage instructions

## Quick Start Commands

```bash
# Validate all entries
python3 build/validate.py

# Build the dictionary
python3 build/build.py

# View locally (no server needed)
open docs/index.html

# Or view the live site: https://tkgally.github.io/je-dict-1/
```

## Creating New Entries

Entries go in `entries/{kana-row}/` directories:
- あ行 → `/a/`, か行 → `/ka/`, さ行 → `/sa/`, etc.
- Voiced consonants stay with their row: が→`/ka/`, ば→`/ha/`

File naming: `{romaji}_{5-digit-id}.json`
- Example: 食べる (たべる) → `entries/ta/taberu_00001.json`

See `PROJECT_STATUS.md` for the entry template and next available IDs.

## Suggested Next Tasks

1. **Add more entries** - Priority: common N5 verbs, nouns, question words
2. **Reach 100 entries** - Good milestone for testing
3. **Consider**: More particle/grammar entries, conjugation search

## Important Conventions

- **Furigana notation**: All kanji must have readings: `{漢字|かんじ}`
- Romanization follows kana, not pronunciation: とうきょう → `toukyou`
- Each entry needs 2-3 example sentences minimum
- Particles get especially detailed explanations
- Data embeds in `data.js` at build time (no server required)
- Output goes to `docs/` (for GitHub Pages compatibility)

---

*For full details, read `PROJECT_STATUS.md`*
