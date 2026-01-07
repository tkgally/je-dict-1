# je-dict-1 Project Status

**Last updated**: 2026-01-07
**Last session**: Session 4 - Added 52 new entries (351 total)

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
- **Total entries**: 351
- **Verified entries**: 351
- **Draft entries**: 0
- **Entries with furigana**: 351/351 (100% complete)
- **N5 coverage**: ~351/800 words (~44%)
- **N4 coverage**: 0/700 words (0%)

### Entry Breakdown by Type
| Type | Count | Examples |
|------|-------|----------|
| Verbs | ~100 | taberu, nomu, iku, kuru, miru, suru, aru, tsuku, noboru, magaru, shinu, sumu, warau, naku, utau, okiru, tomaru, motsu, kiku, au, matsu, agaru, kakaru, kawaru, naoru, tobu, tsukeru, haku, hareru, kumoru, komu, suku, kaburu, yobu, oboeru, okuru, kureru, suwaru, tatsu, aku, shimaru, toru... |
| Nouns | ~140 | mizu, hon, gakkou, eiga, ongaku, kippu, kaban, yama, kawa, umi, hana, ki, tori, neko, inu, haru, natsu, aki, fuyu, shashin, enpitsu, boorupen, keshigomu, hasami, kami, nooto, kitte, hagaki, keitai, nimotsu, ryokou, kaigi, kumo, hoshi, tsuki, oto, koe, boushi, kutsu, kutsushita, fuku, isu, tsukue... |
| Adjectives | ~60 | ookii, chiisai, ii, samui, atsui, amai, karai, tsumetai, atatakai, suzushii, nagai, mijikai, hayai, osoi, akarui, kurai, oishii, mazui, urusai, shizuka, kirei, genki, dame, jouzu, heta, taisetsu, kantan, yasashii, hiroi, semai, usui, atsui (thick)... |
| Adverbs | ~15 | totemo, taihen, chotto, sukoshi, takusan, zenzen, itsumo, tokidoki, yoku, mou, mada, amari... |
| Particles | 9 | ha, ga, wo, ni, de, to, mo, kara, made |
| Question words | 8 | nani, dare, doko, itsu, naze, dou, dore, dono |
| Counters | 8 | nin, hitori, futari, ko, mai, hon, satsu, dai |
| Days/Months | 19 | getsuyoubi, kayoubi..., ichigatsu, nigatsu... |
| Numbers | 10 | ichi, ni, san, yon, go, roku, nana, hachi, kyuu, juu |
| Time expressions | 13 | mainichi, maishuu, maitsuki, maitoshi, kyonen, kotoshi, rainen, senshuu, konshuu, raishuu, sengetsu, kongetsu, raigetsu |

### Entry Breakdown by Directory
| Directory | Count |
|-----------|-------|
| `/a/` | ~60 |
| `/ka/` | ~60 |
| `/sa/` | ~45 |
| `/ta/` | ~55 |
| `/na/` | ~30 |
| `/ha/` | ~45 |
| `/ma/` | ~35 |
| `/ya/` | ~25 |
| `/ra/` | ~8 |
| `/wa/` | ~5 |

### Session History
| Session | Date | Entries Added | Total After |
|---------|------|---------------|-------------|
| 1 | 2026-01-07 | 97 (initial + 50 new) | 97 |
| 2 | 2026-01-07 | 102 | 199 |
| 3 | 2026-01-07 | 100 | 299 |
| 4 | 2026-01-07 | 52 (86 created, 14 duplicates removed) | 351 |

### Recent Changes (Session 4)
1. Added 52 new unique N5 entries including:
   - Numbers: ichi, ni, san, yon, go, roku, nana, hachi, kyuu, juu (1-10)
   - Time expressions: mainichi, maishuu, maitsuki, maitoshi, kyonen, kotoshi, rainen, senshuu, konshuu, raishuu, sengetsu, kongetsu, raigetsu
   - Adjectives: oishii, mazui, urusai, shizuka, kirei, genki, dame, jouzu, heta, taisetsu, kantan, yasashii, hiroi, semai, usui, atsui (thick)
   - Verbs: kakaru, kawaru, naoru, tobu, tsukeru, haku, okureru, hareru, kumoru, komu, suku, kaburu, yobu, oboeru, okuru, kureru, suwaru, tatsu, aku, shimaru, toru
   - Stationery: shashin, enpitsu, boorupen, keshigomu, hasami, kami, nooto
   - Communication: kitte, hagaki, keitai
   - Travel/work: nimotsu, ryokou, kaigi
   - Nature: kumo, hoshi, tsuki, oto, koe
   - Clothing: boushi, kutsu, kutsushita, fuku
   - Furniture: isu, tsukue
2. Removed 14 duplicate entries that conflicted with existing entries
3. Total entries increased from 299 to 351

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

### Session 5 (Next Session)
1. **Clear new_entries.txt** at start of session (marks Session 4 entries as no longer new)
2. **Add ~100 more N5 entries** targeting:
   - More verbs: kowareru, nureru, kawaku, ageru (different from agaru), sageru, etc.
   - Family terms: kazoku, ryoushin, sofu, sobo, etc.
   - School/education: jugyou, shukudai, kyoushitsu, etc.
   - Food: kudamono, yasai (vegetables), gohan, niku, sakana, etc.
   - Body parts: karada, kao, me, hana, kuchi, mimi, etc.
3. **Target**: Reach ~450 entries (~56% N5 coverage)

### Upcoming (Future Sessions)
- Sessions 6-8: Continue adding ~100 entries per session
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
Next available IDs by directory (after Session 4):
- `/a/`: 00094
- `/ka/`: 00094
- `/sa/`: 00094
- `/ta/`: 00094
- `/na/`: 00094
- `/ha/`: 00094
- `/ma/`: 00094
- `/ya/`: 00094
- `/ra/`: 00094
- `/wa/`: 00094

Note: Use IDs >= 00094 for new entries in any directory to avoid conflicts.

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
