# Resume Working on je-dict-1

Point an AI assistant to this file when resuming work on this project.

---

## Quick Summary

**je-dict-1** is a Japanese-English learner's dictionary delivered as a static website. It emphasizes quality over quantity - fewer entries, but each with rich explanations, natural examples, and usage notes.

## Current Status

- **Phase**: Phase 1 Complete - N5 Vocabulary Coverage achieved
- **Entries**: 764 (verbs, nouns, adjectives, adverbs, particles, counters, demonstratives, conjunctions, expressions) - all with furigana
- **N5 Coverage**: ~95% (764/800 words)
- **Infrastructure**: Fully functional (build scripts, web interface, sidebar browser)
- **Live site**: https://tkgally.github.io/je-dict-1/
- **Next goal**: Quality improvements and N4 vocabulary expansion

## Session History

| Session | Entries Added | Total | Focus Areas |
|---------|---------------|-------|-------------|
| 1 | 97 | 97 | Foundation + "New" tag system |
| 2 | 102 | 199 | Time, family, body, food, places, weather, colors, adverbs |
| 3 | 100 | 299 | Verbs, days of week, months, seasons, directions, counters, nature, everyday items |
| 4 | 52 | 351 | Numbers 1-10, time expressions, adjectives, verbs, stationery, nature, clothing, furniture |
| 5 | 68 | 419 | Body parts, family, school/education, food, verbs, transport, household, adjectives, numbers, health, adverbs |
| 6 | 100 | 519 | Verbs, shopping/commerce, nature, food, time, adjectives, adverbs |
| 7 | 101 | 620 | Colors, family terms, question words, numbers 11-50, counters, time expressions, positional words, body parts, demonstratives, conjunctions, common expressions |
| 8 | 80 | 700 | Common expressions, clothing, food/drinks, kitchen/household, buildings/places, transportation, school/education, work/business |
| 9 | 64 | 764 | Work/business, verbs, i-adjectives, na-adjectives, adverbs, miscellaneous essential words - completing N5 coverage |

## Key Files to Read

1. **`PROJECT_STATUS.md`** - Detailed current state, next steps, and technical notes
2. **`N5_REMAINING_VOCABULARY.md`** - Remaining N5 words to add
3. **`project_specification.md`** - Full project specification and design decisions
4. **`build/schema.json`** - Entry JSON schema
5. **`build/new_entries.txt`** - List of entries to mark as "New" in sidebar
6. **`README.md`** - Usage instructions

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

**Next available IDs**: Use IDs >= 00111 in any directory to avoid conflicts.

See `PROJECT_STATUS.md` for the entry template and detailed ID assignment.

## Future Work

Phase 1 (N5 coverage) is now complete with 764 entries. Future sessions may focus on:

1. **Quality improvements**:
   - Review and enhance existing entries
   - Add more example sentences where needed
   - Add cross-references between related entries
2. **Feature improvements**:
   - Implement conjugation search (tabete -> taberu)
   - Add audio pronunciations
3. **N4 Vocabulary expansion** (Phase 2):
   - Add N4 level words
   - Focus on intermediate grammar patterns

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

## Creating Pull Requests

The `gh` CLI often fails due to authentication issues. Use this reliable method instead:

1. **Commit and push** your changes to the feature branch:
   ```bash
   git add -A
   git commit -m "Session N: Add X new N5 dictionary entries"
   git push -u origin <branch-name>
   ```

2. **Construct the PR URL directly** using this format:
   ```
   https://github.com/tkgally/je-dict-1/pull/new/<branch-name>
   ```

3. **Provide the URL to the user** - they can click it to create the PR in GitHub's web interface.

Example: For branch `claude/add-entries-ABC123`, the PR URL is:
```
https://github.com/tkgally/je-dict-1/pull/new/claude/add-entries-ABC123
```

---

*For full details, read `PROJECT_STATUS.md`*
