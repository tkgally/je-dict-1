# je-dict-1 Project Status

**Last updated**: 2026-01-07
**Last session**: Session 2 - Added 102 new entries (199 total)

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
- **Total entries**: 199
- **Verified entries**: 199
- **Draft entries**: 0
- **Entries with furigana**: 199/199 (100% complete)
- **N5 coverage**: ~199/800 words (~25%)
- **N4 coverage**: 0/700 words (0%)

### Entry Breakdown by Type
| Type | Count | Examples |
|------|-------|----------|
| Verbs | ~65 | taberu, nomu, iku, kuru, miru, suru, aru, benkyousuru, akeru, shimeru, tsukeru, kesu, hajimeru, owaru, noru, oriru, aruku, hashiru, hataraku, yasumu, asobu, narau... |
| Nouns | ~80 | mizu, hon, gakkou, asa, yoru, chichi, haha, atama, kao, te, ashi, gohan, pan, niku, sakana, eki, densha, byouin, ginkou, kaisha, shigoto, tomodachi, nihongo... |
| Adjectives | ~30 | ookii, chiisai, ii, akai, aoi, shiroi, kuroi, omoshiroi, tsumaranai, isogashii, hima... |
| Adverbs | ~15 | totemo, taihen, chotto, sukoshi, takusan, zenzen, itsumo, tokidoki, yoku, mou, mada, amari... |
| Particles | 9 | ha, ga, wo, ni, de, to, mo, kara, made |
| Question words | 8 | nani, dare, doko, itsu, naze, dou, dore, dono |

### Entry Breakdown by Directory
| Directory | Count |
|-----------|-------|
| `/a/` | ~35 |
| `/ka/` | ~25 |
| `/sa/` | ~15 |
| `/ta/` | ~40 |
| `/na/` | ~15 |
| `/ha/` | ~20 |
| `/ma/` | ~20 |
| `/ya/` | ~15 |
| `/ra/` | 0 |
| `/wa/` | ~3 |

### Session History
| Session | Date | Entries Added | Total After |
|---------|------|---------------|-------------|
| 1 | 2026-01-07 | 97 (initial + 50 new) | 97 |
| 2 | 2026-01-07 | 102 | 199 |

### Recent Changes (Session 2)
1. Added 102 new N5 entries including:
   - Verbs: benkyousuru, akeru, shimeru, tsukeru, kesu, hajimeru, owaru, noru, oriru, aruku, hashiru, hataraku, yasumu, asobu, narau, etc.
   - Time nouns: asa, yoru, hiru, ban, gogo, gozen
   - Family terms: chichi, haha, ani, ane, otouto, imouto, kazoku, kodomo
   - Body parts: atama, kao, me, mimi, kuchi, te, ashi
   - Food: gohan, pan, niku, sakana, yasai, kudamono, tamago, ocha, mizu
   - Places: byouin, ginkou, yuubinkyoku, toshokan, kouen, eki, densha, mise
   - Weather: tenki, ame, yuki, sora
   - Colors: akai, aoi, shiroi, kuroi
   - Adjectives: omoshiroi, tsumaranai, isogashii, hima
   - Adverbs: totemo, taihen, chotto, sukoshi, takusan, zenzen, itsumo, tokidoki, yoku, mou, mada, amari
   - Other nouns: shigoto, kaisha, gakkou, daigaku, sensei, gakusei, tomodachi, okane, jikan, namae, denwa, kuruma, ie, heya, machi, kuni, nihongo
2. Updated new_entries.txt with 102 new entry IDs
3. Total entries increased from 97 to 199

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

### Session 3 (Next Session)
1. **Clear new_entries.txt** at start of session (marks Session 2 entries as no longer new)
2. **Add ~100 more N5 entries** targeting:
   - More verbs: tsuku (arrive), noboru (climb), magaru (turn), shinu (die), sumu (live), warau (laugh), naku (cry), utau (sing), etc.
   - Numbers and counters: ~nin, ~ko, ~mai, ~hon, ~satsu, etc.
   - Days of week: getsuyoubi, kayoubi, etc.
   - Months: ichigatsu, nigatsu, etc.
   - More common nouns: eiga (movie), ongaku (music), kippu (ticket), kaban (bag), etc.
   - More adjectives: samui (cold), atsui (hot), amai (sweet), karai (spicy), etc.
3. **Target**: Reach ~300 entries (~38% N5 coverage)

### Upcoming (Future Sessions)
- Sessions 4-7: Continue adding ~100 entries per session
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
Next available IDs by directory (after Session 2):
- `/a/`: 00091
- `/ka/`: 00091
- `/sa/`: 00091
- `/ta/`: 00091
- `/na/`: 00091
- `/ha/`: 00091
- `/ma/`: 00091
- `/ya/`: 00091
- `/ra/`: 00001
- `/wa/`: 00004

Note: Use IDs >= 00091 for new entries in any directory to avoid conflicts.

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
