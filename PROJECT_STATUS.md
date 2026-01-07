# je-dict-1 Project Status

**Last updated**: 2026-01-07
**Last session**: Session 9 - Added 64 new entries (764 total)

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
- **Total entries**: 764
- **Verified entries**: 764
- **Draft entries**: 0
- **Entries with furigana**: 764/764 (100% complete)
- **N5 coverage**: ~764/800 words (~95%)
- **N4 coverage**: 0/700 words (0%)

### Entry Breakdown by Type
| Type | Count | Examples |
|------|-------|----------|
| Verbs | ~130 | taberu, nomu, iku, kuru, miru, suru, aru, arau, ugoku, umareru, uru, erabu, okoru, kangaeru, kakeru, kimeru, komaru, korobu, suteru, tasukeru, tetsudau, tsuzuku, tsukareru, todoku, naosu, nareru, hajimaru, hirou, furu, yameru, wareru, dekakeru, tsutomeru... |
| Nouns | ~330 | mizu, hon, gakkou, eiga, ongaku, iro, ike, iwa, otsuri, kangae, kaigan, kaimono, kyaku, kusa, gomi, sakura, sara, shio, shima, shitsumon, shumi, shinamono, satou, suna, tenin, nedan, nioi, hatake, basho, fukuro, mori, mushi, mizuumi, youji, yoyaku, ryouri, reji, nami, katachi, jiko, koppu, supuun, fuooku, aji, mune, koshi, hiza, ude, nodo, tonari, aida, shatsu, zubon, sukaato, miso, biiru, wain, konbini, reizouko, shinkansen, teikiken, koukou, gakki, shachou, zangyou... |
| Adjectives | ~93 | ookii, chiisai, ii, samui, benri, fuben, nigiyaka, okashii, tadashii, warui, kawaii, kowai, sabishii, nemui, hazukashii, hitsuyou, fuan, teinei, raku, kiiroi, chairoi... |
| Adverbs | ~45 | totemo, taihen, zehi, tashika, kitto, daitai, nakanaka, dandan, toutou, yatto, zutto, massugu, yukkuri, saisho, saigo, hotondo, doushite, tatoeba, mata... |
| Particles | 9 | ha, ga, wo, ni, de, to, mo, kara, made |
| Question words | 11 | nani, dare, doko, itsu, naze, dou, dore, dono, ikutsu, ikura, dochira |
| Counters | 20 | nin, hitori, futari, ko, mai, hon, satsu, dai, kai, kagetsu, shuukan, fun, byou, hai, hiki, wa, soku, tsu... |
| Days/Months | 19 | getsuyoubi, kayoubi..., ichigatsu, nigatsu... |
| Numbers | 31 | ichi, ni, san, yon, go, roku, nana, hachi, kyuu, juu, juuichi-juukyuu, nijuu, sanjuu, yonjuu, gojuu, hyaku, sen, nisen, sanzen, man, en, rei, zero |
| Time expressions | 29 | mainichi, maishuu, maitsuki, maitoshi, kyonen, kotoshi, rainen, senshuu, konshuu, raishuu, sengetsu, kongetsu, raigetsu, kinou, ototoi, asatte, saikin, ima, nanji, goro, maiasa, maiban, yuugata, yonaka, ichijikan, hanjikan, ichinichi... |
| Demonstratives | 12 | kore, sore, are, kono, sono, ano, koko, soko, asoko, kochira, sochira, achira |
| Conjunctions | 10 | soshite, demo, shikashi, dakara, desukara, sorekara, sorede, tokorode, tatoeba, mata |
| Expressions | 15 | arigatou, sumimasen, gomennasai, onegaishimasu, itadakimasu, gochisousama, hajimemashite, ittekimasu, itterasshai, tadaima, okaerinasai, yoroshiku, omedetou, ganbatte, kiwotsukete |

### Entry Breakdown by Directory
| Directory | Count |
|-----------|-------|
| `/a/` | ~90 |
| `/ka/` | ~95 |
| `/sa/` | ~80 |
| `/ta/` | ~85 |
| `/na/` | ~45 |
| `/ha/` | ~70 |
| `/ma/` | ~50 |
| `/ya/` | ~35 |
| `/ra/` | ~12 |
| `/wa/` | ~8 |

### Session History
| Session | Date | Entries Added | Total After |
|---------|------|---------------|-------------|
| 1 | 2026-01-07 | 97 (initial + 50 new) | 97 |
| 2 | 2026-01-07 | 102 | 199 |
| 3 | 2026-01-07 | 100 | 299 |
| 4 | 2026-01-07 | 52 (86 created, 34 duplicates removed) | 351 |
| 5 | 2026-01-07 | 68 (100 created, 32 duplicates removed) | 419 |
| 6 | 2026-01-07 | 100 | 519 |
| 7 | 2026-01-07 | 101 | 620 |
| 8 | 2026-01-07 | 80 | 700 |
| 9 | 2026-01-07 | 64 | 764 |

### Recent Changes (Session 9)
1. Added 64 new unique N5 entries to complete N5 coverage:
   - Work/Business (4): shucchou, meishi, shorui, mensetsu
   - Verbs (13): oku, dasu, ireru, hakobu, naraberu, kaeru (変える), nakunaru, nakusu, shinjiru, tanomu, kotaeru, machigaeru, modoru
   - I-Adjectives (14): katai, yawarakai, subarashii, hidoi, sugoi, itai, tsurai, hoshii, kibishii, kusai, utsukushii, sukunai, ooi, nai
   - Na-Adjectives (10): yuumei, tokubetsu, shinsetsu, fukuzatsu, jiyuu, anzen, kiken, joubu, rippa, hen
   - Adverbs (8): ichiban, kanari, taitei, sou, kou, aa, nantoka, betsuni
   - Miscellaneous Essential Words (15): koto, mono, tokoro, hou, tame, hazu, tsumori, you, wake, imi, riyuu, setsumei, junbi, keikaku, keiken
2. Total entries increased from 700 to 764
3. N5 coverage now at ~95%
4. Phase 1 (N5 vocabulary) essentially complete

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

### Phase 1 Complete!
N5 vocabulary coverage is now at ~95% with 764 entries. The dictionary now covers the essential vocabulary for JLPT N5 level learners.

### Future Enhancements (Phase 2 and beyond)
1. **Quality improvements**:
   - Review and enhance existing entries
   - Add more example sentences where needed
   - Improve cross-references between related entries
2. **Feature improvements**:
   - Implement conjugation search (tabete -> taberu)
   - Add audio pronunciations
   - Implement spaced repetition study mode
3. **N4 Vocabulary expansion** (Phase 2):
   - Add ~700 N4 level words
   - Focus on intermediate grammar patterns
   - Include more complex vocabulary and usage notes

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
Next available IDs by directory (after Session 9):
- `/a/`: 00108
- `/ka/`: 00111
- `/sa/`: 00111
- `/ta/`: 00107
- `/na/`: 00104
- `/ha/`: 00107
- `/ma/`: 00104
- `/ya/`: 00102
- `/ra/`: 00101
- `/wa/`: 00100

Note: Use IDs >= 00111 for new entries in any directory to avoid conflicts.

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
