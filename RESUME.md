# Resume Working on je-dict-1

Point an AI assistant to this file when resuming work on this project.

---

## Quick Summary

**je-dict-1** is a Japanese-English learner's dictionary delivered as a static website. It emphasizes quality over quantity - fewer entries, but each with rich explanations, natural examples, and usage notes.

## Current Status

- **Phase**: Phase 2 - Core Vocabulary Expansion
- **Entries**: 519 (verbs, nouns, adjectives, adverbs, particles, counters) - all with furigana
- **N5 Coverage**: ~65% (519/800 words)
- **Infrastructure**: Fully functional (build scripts, web interface, sidebar browser)
- **Live site**: https://tkgally.github.io/je-dict-1/
- **Target**: 600-700 entries for substantial N5 coverage

## Session History

| Session | Entries Added | Total | Focus Areas |
|---------|---------------|-------|-------------|
| 1 | 97 | 97 | Foundation + "New" tag system |
| 2 | 102 | 199 | Time, family, body, food, places, weather, colors, adverbs |
| 3 | 100 | 299 | Verbs, days of week, months, seasons, directions, counters, nature, everyday items |
| 4 | 52 | 351 | Numbers 1-10, time expressions, adjectives, verbs, stationery, nature, clothing, furniture |
| 5 | 68 | 419 | Body parts, family, school/education, food, verbs, transport, household, adjectives, numbers, health, adverbs |
| 6 | 100 | 519 | Verbs, shopping/commerce, nature, food, time, adjectives, adverbs |

## Key Files to Read

1. **`PROJECT_STATUS.md`** - Detailed current state, next steps, and technical notes
2. **`project_specification.md`** - Full project specification and design decisions
3. **`build/schema.json`** - Entry JSON schema
4. **`build/new_entries.txt`** - List of entries to mark as "New" in sidebar
5. **`README.md`** - Usage instructions

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

**Next available IDs**: Use IDs >= 00096 in any directory to avoid conflicts.

See `PROJECT_STATUS.md` for the entry template and detailed ID assignment.

## Session 7 Tasks (Next Session)

1. **Clear new_entries.txt** at start (removes "New" tags from Session 6 entries)
2. **Add ~100 more N5 entries** targeting:
   - More verbs: modoru, tsunagu, nobasu, etc.
   - Weather/seasons: remaining seasonal vocabulary
   - Actions: remaining common verbs
   - More adjectives: remaining N5 adjectives
   - More adverbs: remaining N5 adverbs
   - Common expressions and set phrases
3. **Update new_entries.txt** with new entry IDs
4. **Build and validate**
5. **Update PROJECT_STATUS.md** with new counts
6. **Target**: Reach ~620 entries (~78% N5 coverage)

## Important Conventions

- **Furigana notation**: All kanji must have readings: `{漢字|かんじ}`
- Romanization follows kana, not pronunciation: とうきょう → `toukyou`
- Each entry needs 2-3 example sentences minimum
- Particles get especially detailed explanations
- Data embeds in `data.js` at build time (no server required)
- Output goes to `docs/` (for GitHub Pages compatibility)

## "New" Tag System

- Controlled by `build/new_entries.txt`
- Add entry IDs (one per line) to mark them as new
- Clear the file at the START of each new session
- Tags appear only in sidebar, not in entry display

---

*For full details, read `PROJECT_STATUS.md`*
