# je-dict-1 Project Status

**Last updated**: 2026-01-07
**Last session**: Added 50 new entries with "New" tag system in sidebar

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 2: Core Vocabulary** - In progress. Adding common N5 words.

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
- [x] **"New" tag system** in sidebar (tracks recently added entries)
- [x] README.md created
- [x] PROJECT_STATUS.md created
- [x] .gitignore configured

### Content Status
- **Total entries**: 97
- **Verified entries**: 97
- **Draft entries**: 0
- **Entries with furigana**: 97/97 (100% complete)
- **N5 coverage**: ~97/800 words (~12%)
- **N4 coverage**: 0/700 words (0%)

### Entry Breakdown by Type
| Type | Count | Examples |
|------|-------|----------|
| Verbs | 41 | taberu, nomu, iku, kuru, miru, suru, aru, iu, okiru, oshieru, aruku, oyogu, ageru, asobu, kaeru, deru, hataraku, hairu, hashiru, neru, narau, tomaru, dekiru, wasureru, morau... |
| Nouns | 27 | mizu, hon, gakkou, hito, jikan, eki, kuruma, kawa, ki, shigoto, denwa, densha, namae, heya, mise, michi, umi, onna, otoko, yama, hana... |
| Adjectives | 17 | ookii, chiisai, ii, atarashii, furui, takai, yasui, osoi, tooi, chikai, nagai, mijikai, hayai, muzukashii, yasashii... |
| Particles | 9 | ha, ga, wo, ni, de, to, mo, kara, made |
| Question words | 8 | nani, dare, doko, itsu, naze, dou, dore, dono |

### Entry Breakdown by Directory
| Directory | Count | Entries |
|-----------|-------|---------|
| `/a/` | 22 | iku, ookii, ii, aru, au, omou, iru, ashita, atarashii, iu, okiru, oshieru, eki, osoi, itsu, aruku, oyogu, ageru, asobu, umi, onna, otoko |
| `/ka/` | 12 | kuru, gakkou, ga, kaku, kiku, kau, kyou, kara, kaeru, kuruma, kawa, ki |
| `/sa/` | 4 | suru, shiru, jikan, shigoto |
| `/ta/` | 21 | taberu, chiisai, tsukau, tsukuru, toshi, tomodachi, takai, de, to, deru, denwa, densha, tooi, chikai, dare, doko, dou, dore, dono, tomaru, dekiru |
| `/na/` | 8 | nomu, ni, neru, narau, namae, nagai, nani, naze |
| `/ha/` | 12 | hon, ha, hanasu, hito, hi, furui, hairu, hataraku, heya, hayai, hashiru, hana |
| `/ma/` | 11 | miru, mizu, matsu, motsu, mo, made, mise, michi, mijikai, muzukashii, morau |
| `/ya/` | 4 | yomu, yasui, yasashii, yama |
| `/ra/` | 0 | (none yet) |
| `/wa/` | 3 | wo, wakaru, wasureru |

### Recent Changes (This Session)
1. Implemented "New" tag system in sidebar for recently added entries
2. Added 50 new dictionary entries (verbs, nouns, adjectives, question words)
3. Updated build system to support new entries list (`build/new_entries.txt`)
4. Total entries increased from 47 to 97

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

## "New" Tag System

The sidebar now shows a red "New" tag next to recently added entries:
- Controlled by `build/new_entries.txt` file
- Add entry IDs (one per line) to mark them as new
- Clear the file when starting a new batch of entries
- Tags only appear in the sidebar, not in the entry display

## Next Steps

### Immediate (Next Session)
1. **Continue vocabulary expansion**: Add more N5 words (target: 150 entries)
2. **Priority words to add**:
   - More common verbs: nomu (drink) variants, benkyousuru, etc.
   - Time words: asa, yoru, gogo, gozen, etc.
   - Family terms: chichi, haha, ani, ane, etc.
   - Basic counters: ~nin, ~ko, ~mai, etc.

### Upcoming (Future Sessions)
- Reach critical mass of 500-1000 entries
- Implement conjugation search (tabete -> taberu)
- Add cross-references between related entries
- Consider AI-assisted batch entry generation via OpenRouter
- Clear "New" tags from current batch when adding next batch

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
- `/a/`: 00023
- `/ka/`: 00013
- `/sa/`: 00005
- `/ta/`: 00022
- `/na/`: 00009
- `/ha/`: 00013
- `/ma/`: 00012
- `/ya/`: 00005
- `/ra/`: 00001
- `/wa/`: 00004

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
