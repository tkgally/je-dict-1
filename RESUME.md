# Resume Working on je-dict-1

Point an AI assistant to this file when resuming work on this project.

---
## ⚠️ CRASH PREVENTION - READ FIRST ⚠️

**Claude Code has a known bug** that causes crashes when Japanese text appears in Claude's response output. This project has crashed 3+ times from this bug.

### STRICT RULE: Zero Japanese in Responses

1. **NEVER** output Japanese characters (hiragana, katakana, kanji) in your responses
2. **NEVER** preview or quote entry content - write directly to files
3. **ONLY** use romanized names and file paths in status messages
4. Code blocks do NOT help - the crash happens in response rendering

**Safe example**: "Created entries/ta/taberu_00001.json - open in editor to review"

**Unsafe example**: Any response containing Japanese characters

See PROJECT_STATUS.md "Terminal Display Crash Prevention" section for full details.

---

## Quick Summary

**je-dict-1** is a Japanese-English learner's dictionary delivered as a static website. It emphasizes quality over quantity - fewer entries, but each with rich explanations, natural examples, and usage notes.

## Current Status

- **Phase**: Foundation complete, ready for content expansion
- **Entries**: 47 (verbs, nouns, adjectives, particles)
- **Infrastructure**: Fully functional (build scripts, web interface, sidebar browser)
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

# View in browser (no server needed)
open dist/index.html
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

- Romanization follows kana, not pronunciation: とうきょう → `toukyou`
- Each entry needs 2-3 example sentences minimum
- Particles get especially detailed explanations
- Data embeds in `data.js` at build time (no server required)

---

*For full details, read `PROJECT_STATUS.md`*
