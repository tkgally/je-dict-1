# je-dict-1 Project Status

**Last updated**: 2026-01-06
**Last session**: Migrated to GitHub, added furigana to all entries, configured GitHub Pages

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 1: Foundation** - Complete. Furigana system implemented. Ready to begin Phase 2 (Core Vocabulary expansion).

### Infrastructure Status
- [x] Directory structure created (`entries/`, `variants/`, `build/`, `web/`, `docs/`)
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
- **Entries with furigana**: 47/47 (100% complete)
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
1. Migrated project to GitHub for continued development
2. Removed terminal bug workaround documentation (not needed on GitHub)
3. Cleaned up duplicate files from root directory
4. Added furigana notation to all 26 entries that were missing it
5. Renamed `dist/` to `docs/` for GitHub Pages compatibility
6. Configured GitHub Pages to serve from `docs/` folder
7. Site is now live at https://tkgally.github.io/je-dict-1/

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

## Next Steps

### Immediate (Next Session)
1. **Expand vocabulary**: Add 30-50 more N5 words (target: 100 entries)
2. **Priority words to add**:
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

# View dictionary locally
open docs/index.html

# Or view the live site
# https://tkgally.github.io/je-dict-1/
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

### Key Technical Decisions
1. **Static embedding**: Data is in `data.js`, not fetched via AJAX. This allows `file://` usage.
2. **No server required**: Just open `docs/index.html` in browser (or use GitHub Pages)
3. **GitHub Pages**: Site served from `docs/` folder on main branch
4. **Single index file**: All search data in one file (optimize later if needed)
5. **Kana-row grouping**: Sidebar groups entries by a-row, ka-row, etc.
6. **Furigana notation**: `{kanji|reading}` converted to `<ruby>` tags in browser

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
