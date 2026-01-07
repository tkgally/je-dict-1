# je-dict-1 Project Status

**Last updated**: 2026-01-07
**Last session**: Session 6 - Added 100 new entries (519 total)

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
- [x] Claude Code auto-accept settings configured

### Content Status
- **Total entries**: 519
- **Verified entries**: 519
- **Draft entries**: 0
- **Entries with furigana**: 519/519 (100% complete)
- **N5 coverage**: ~519/800 words (~65%)
- **N4 coverage**: 0/700 words (0%)

### Entry Breakdown by Type
| Type | Count | Examples |
|------|-------|----------|
| Verbs | ~130 | taberu, nomu, iku, kuru, miru, suru, aru, arau, ugoku, umareru, uru, erabu, okoru, kangaeru, kakeru, kimeru, komaru, korobu, suteru, tasukeru, tetsudau, tsuzuku, tsukareru, todoku, naosu, nareru, hajimaru, hirou, furu, yameru, wareru, dekakeru, tsutomeru... |
| Nouns | ~220 | mizu, hon, gakkou, eiga, ongaku, iro, ike, iwa, otsuri, kangae, kaigan, kaimono, kyaku, kusa, gomi, sakura, sara, shio, shima, shitsumon, shumi, shinamono, satou, suna, tenin, nedan, nioi, hatake, basho, fukuro, mori, mushi, mizuumi, youji, yoyaku, ryouri, reji, nami, katachi, jiko, koppu, supuun, fuooku, aji... |
| Adjectives | ~90 | ookii, chiisai, ii, samui, benri, fuben, nigiyaka, okashii, tadashii, warui, kawaii, kowai, sabishii, nemui, hazukashii, hitsuyou, fuan, teinei, raku... |
| Adverbs | ~35 | totemo, taihen, zehi, tashika, kitto, daitai, nakanaka, dandan, toutou, yatto, zutto, massugu, yukkuri, saisho, saigo, hotondo, doushite... |
| Particles | 9 | ha, ga, wo, ni, de, to, mo, kara, made |
| Question words | 8 | nani, dare, doko, itsu, naze, dou, dore, dono |
| Counters | 8 | nin, hitori, futari, ko, mai, hon, satsu, dai |
| Days/Months | 19 | getsuyoubi, kayoubi..., ichigatsu, nigatsu... |
| Numbers | 14 | ichi, ni, san, yon, go, roku, nana, hachi, kyuu, juu, hyaku, sen, man, en |
| Time expressions | 17 | mainichi, maishuu, maitsuki, maitoshi, kyonen, kotoshi, rainen, senshuu, konshuu, raishuu, sengetsu, kongetsu, raigetsu, kinou, ototoi, asatte, saikin |

### Entry Breakdown by Directory
| Directory | Count |
|-----------|-------|
| `/a/` | ~74 |
| `/ka/` | ~77 |
| `/sa/` | ~63 |
| `/ta/` | ~70 |
| `/na/` | ~38 |
| `/ha/` | ~59 |
| `/ma/` | ~39 |
| `/ya/` | ~30 |
| `/ra/` | ~11 |
| `/wa/` | ~7 |

### Session History
| Session | Date | Entries Added | Total After |
|---------|------|---------------|-------------|
| 1 | 2026-01-07 | 97 (initial + 50 new) | 97 |
| 2 | 2026-01-07 | 102 | 199 |
| 3 | 2026-01-07 | 100 | 299 |
| 4 | 2026-01-07 | 52 (86 created, 34 duplicates removed) | 351 |
| 5 | 2026-01-07 | 68 (100 created, 32 duplicates removed) | 419 |
| 6 | 2026-01-07 | 100 | 519 |

### Recent Changes (Session 6)
1. Added 100 new unique N5 entries including:
   - Verbs (25): arau, tsukareru, hajimaru, tsuzuku, komaru, naosu, suteru, hirou, yameru, erabu, ugoku, tetsudau, dekakeru, tasukeru, korobu, okoru, wareru, nareru, umareru, kangaeru, todoku, kakeru, kimeru, furu, uru
   - Shopping/Commerce (10): nedan, otsuri, kaimono, tenin, kyaku, fukuro, reji, sara, koppu, supuun
   - Nature (12): mori, ike, suna, iwa, shima, kusa, mushi, mizuumi, sakura, hatake, nami, kaigan
   - Food/Cooking (3): ryouri, satou, shio
   - Time expressions (4): kinou, ototoi, asatte, saikin
   - Other nouns (13): basho, youji, yoyaku, shitsumon, henji, kangae, gomi, jiko, nioi, iro, katachi, shumi, shinamono
   - Adjectives (16): benri, fuben, nigiyaka, okashii, tadashii, warui, kawaii, kowai, sabishii, nemui, hazukashii, hitsuyou, fuan, teinei, raku, aji
   - Adverbs (15): zehi, tashika, kitto, daitai, nakanaka, dandan, toutou, yatto, zutto, massugu, yukkuri, saisho, saigo, hotondo, doushite
   - Other: fuooku (fork), tsutomeru (to work for)
2. Total entries increased from 419 to 519
3. N5 coverage now at ~65%

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

### Session 7 (Next Session)
1. **Clear new_entries.txt** at start of session (marks Session 6 entries as no longer new)
2. **Add ~100 more N5 entries** targeting:
   - More verbs: modoru, tsunagu, nobasu, etc.
   - Weather/seasons: remaining seasonal vocabulary
   - Actions: remaining common verbs
   - More adjectives: remaining N5 adjectives
   - More adverbs: remaining N5 adverbs
   - Common expressions and set phrases
3. **Target**: Reach ~620 entries (~78% N5 coverage)

### Upcoming (Future Sessions)
- Sessions 7-8: Continue adding ~100 entries per session
- Target 600-700 entries for substantial N5 coverage
- Implement conjugation search (tabete -> taberu)
- Add cross-references between related entries
- Consider AI-assisted batch entry generation

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
Next available IDs by directory (after Session 6):
- `/a/`: 00096
- `/ka/`: 00096
- `/sa/`: 00096
- `/ta/`: 00096
- `/na/`: 00096
- `/ha/`: 00096
- `/ma/`: 00096
- `/ya/`: 00096
- `/ra/`: 00096
- `/wa/`: 00096

Note: Use IDs >= 00096 for new entries in any directory to avoid conflicts.

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
    "created": "2026-01-07T12:00:00Z",
    "modified": "2026-01-07T12:00:00Z",
    "ai_model": "claude-opus-4-5",
    "confidence": "high",
    "review_status": "verified",
    "jlpt_level": "N5",
    "frequency_rank": null
  }
}
```
