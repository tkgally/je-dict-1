# je-dict-1 Project Status

**Last updated**: 2026-01-06
**Last session**: Implemented furigana system with toggle, added terminal display bug workaround

## Current State

### Phase
**Phase 1: Foundation** - Complete. Furigana system implemented. Ready to begin Phase 2 (Core Vocabulary expansion).

### Infrastructure Status
- [x] Directory structure created (`entries/`, `variants/`, `build/`, `web/`, `dist/`)
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build.py`)
- [x] Web interface functional with search
- [x] Sidebar entry browser (grouped by kana row)
- [x] Static data embedding (works without server)
- [x] **Furigana system** with `{kanji|reading}` notation
- [x] **Furigana toggle button** in web interface
- [x] README.md created
- [x] PROJECT_STATUS.md created
- [x] .gitignore configured

### Content Status
- **Total entries**: 47
- **Verified entries**: 47
- **Draft entries**: 0
- **Entries with furigana**: In progress (converting all entries)
- **N5 coverage**: ~47/800 words (~6%)
- **N4 coverage**: 0/700 words (0%)

### Entry Breakdown by Type
| Type | Count | Examples |
|------|-------|----------|
| Verbs | 21 | taberu, nomu, iku, kuru, miru, suru, aru, kaku, yomu, kiku, hanasu, kau, au, matsu, motsu, tsukau, tsukuru, shiru, omou, wakaru, iru |
| Nouns | 10 | mizu, hon, gakkou, hito, jikan, hi, toshi, kyou, ashita, tomodachi |
| Adjectives | 7 | ookii, chiisai, ii, atarashii, furui, takai, yasui |
| Particles | 9 | ha, ga, wo, ni, de, to, mo, kara, made |

### Entry Breakdown by Directory
| Directory | Count | Entries |
|-----------|-------|---------|
| `/a/` | 9 | iku, ookii, ii, aru, au, omou, iru, ashita, atarashii |
| `/ka/` | 8 | kuru, gakkou, ga, kaku, kiku, kau, kyou, kara |
| `/sa/` | 3 | suru, shiru, jikan |
| `/ta/` | 9 | taberu, chiisai, tsukau, tsukuru, toshi, tomodachi, takai, de, to |
| `/na/` | 2 | nomu, ni |
| `/ha/` | 6 | hon, ha, hanasu, hito, hi, furui |
| `/ma/` | 6 | miru, mizu, matsu, motsu, mo, made |
| `/ya/` | 2 | yomu, yasui |
| `/ra/` | 0 | (none yet) |
| `/wa/` | 2 | wo, wakaru |

### Recent Changes (This Session)
1. Implemented furigana notation system `{kanji|reading}` for all entries
2. Added furigana toggle button to web interface header
3. Toggle saves preference to localStorage
4. Updated README.md with furigana documentation
5. Added terminal display bug workaround documentation

## Furigana System

### Notation Format
```
{kanji|reading}
```

### Rules
1. All kanji must have readings in hiragana
2. No romaji — readings are always in hiragana
3. Apply to all fields: headword, examples, notes, explanations
4. Compound readings: mark entire compound `{友達|ともだち}` not individual kanji

### Web Interface
- Toggle button labeled "Furigana" in header
- Converts `{kanji|reading}` to HTML `<ruby>` tags
- Preference saved in localStorage

## Known Issues

### Terminal Display Bug (Claude Code)
**Issue**: Claude Code crashes when displaying Japanese text containing `{kanji|reading}` notation in the terminal output.

**Error**: `byte index N is not a char boundary` — a UTF-8 string slicing error in Rust.

**Workaround**:
- Write Japanese dictionary content to files rather than displaying in terminal
- Only show brief English-only status messages
- Bug has been reported to Claude Code team

**Impact**: Does not affect JSON files or web interface — only terminal display.

## Next Steps

### Immediate (Next Session)
1. **Convert remaining entries** to use furigana notation consistently
2. **Expand vocabulary**: Add 30-50 more N5 words (target: 100 entries)
3. **Priority words to add**:
   - Common verbs: iu, kaeru, hairu, deru, neru, okiru, hataraku, oshieru, narau
   - Common nouns: namae, denwa, shigoto, heya, eki, mise, michi, kuruma, densha
   - Common adjectives: tooi, chikai, nagai, mijikai, hayai, osoi, muzukashii, yasashii
   - Question words: nani, dare, doko, itsu, naze, dou, dore, dono

### Upcoming (Future Sessions)
- Reach critical mass of 500-1000 entries
- Implement conjugation search (tabete -> taberu)
- Add cross-references between related entries
- Consider AI-assisted batch entry generation via OpenRouter

## Technical Notes

### Build Commands
```bash
# Validate entries
python3 build/validate.py

# Build dictionary
python3 build/build.py

# View dictionary
open dist/index.html
```

### File Naming Convention
- Format: `{romanized_reading}_{5-digit-id}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
  - toukyou (not tokyo)
  - keiki
- Directory: Based on first kana of reading
  - ga-row -> `/ka/`, ba-row -> `/ha/`, etc.

### ID Assignment
Next available IDs by directory:
- `/a/`: 00010
- `/ka/`: 00009
- `/sa/`: 00004
- `/ta/`: 00010
- `/na/`: 00003
- `/ha/`: 00007
- `/ma/`: 00007
- `/ya/`: 00003
- `/ra/`: 00001
- `/wa/`: 00003

## Notes for AI Assistants

### Quality Standards
- Every entry should have 2-3 example sentences minimum
- Definitions should explain nuance, not just provide translations
- Notes should cover grammar patterns, common mistakes, and usage tips
- Particles deserve especially thorough explanations
- Use natural, conversational example sentences
- **All kanji must have furigana notation**

### Terminal Display Crash Prevention (CRITICAL)
**Claude Code crashes** when Japanese text appears in response output (UTF-8 slicing bug in Rust renderer).

**ZERO TOLERANCE PROTOCOL**:
1. NEVER include ANY Japanese characters in responses - not even in "quotes" or code blocks
2. Write all Japanese content directly to files via Write/Edit tools
3. Use ONLY romanized names and file paths in status messages
4. No previews of entry content - direct users to open files in editor
5. Subprocess output (validate.py, build.py) is safe - only Claude's response text triggers crash

**Examples**:
- BAD: "Created entry for taberu (to eat)" followed by showing the headword
- GOOD: "Created entry: entries/ta/taberu_00001.json - open in editor to review"

This crash has occurred 3+ times. Previous vague guidance failed. Zero Japanese in responses is the ONLY safe approach.

### Key Technical Decisions
1. **Static embedding**: Data is in `data.js`, not fetched via AJAX. This allows `file://` usage.
2. **No server required**: Just open `dist/index.html` in browser
3. **Single index file**: All search data in one file (optimize later if needed)
4. **Kana-row grouping**: Sidebar groups entries by a-row, ka-row, etc.
5. **Furigana notation**: `{kanji|reading}` converted to `<ruby>` tags in browser

### Entry Template
```json
{
  "id": "{romaji}_{5-digit-number}",
  "headword": "{kanji|reading}form",
  "reading": "hiragana",
  "part_of_speech": "verb (ichidan)|verb (godan)|noun|adjective (i-adjective)|particle|etc.",
  "gloss": "brief English equivalent",
  "definitions": [
    {
      "sense_number": 1,
      "gloss": "short gloss",
      "explanation": "Detailed explanation with nuance..."
    }
  ],
  "examples": [
    {
      "japanese": "{kanji|reading}example sentence.",
      "english": "English translation.",
      "notes": "Optional notes about this example"
    }
  ],
  "notes": "Grammar notes, usage notes, cultural notes, etc.",
  "cross_references": [],
  "metadata": {
    "created": "2026-01-06T12:00:00Z",
    "modified": "2026-01-06T12:00:00Z",
    "ai_model": "claude-opus-4-5",
    "confidence": "high",
    "review_status": "verified",
    "jlpt_level": "N5",
    "frequency_rank": null
  }
}
```
