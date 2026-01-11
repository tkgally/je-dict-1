# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-11
**Current phase**: Phase 4 - N4 Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 4: N4 Vocabulary Expansion & Interface Enhancement** - Adding N4 vocabulary while maintaining v2 quality standards, plus new web interface features.

### Infrastructure Status
- [x] Directory structure created (prefix-based subdirectories for scalability)
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build.py`)
- [x] Static HTML site generation (`build/build_flat.py`)
- [x] Furigana system with toggle
- [x] Claude Code skills for entry guidelines
- [x] Quality specification v2 from multi-model evaluation
- [x] Vocabulary-notes skill for formatting guidelines
- [x] Notes field supports paragraph breaks and bullet points
- [x] Multiple interface modes (Search, Browse, Recent, Random)
- [x] Sticky header with interface toggle
- [x] Last updated date in footer
- [x] Cross-reference linking system with UI navigation (567 refs, 97% resolved)
- [x] Audio pronunciation for example sentences (1,028 audio files)
- [x] Prefix-based subdirectory structure for entries and audio (scalable to 10,000+ entries)
- [x] Shared utility modules (`path_utils.py`, `japanese_utils.py`)
- [x] Audio integrity validation in `validate.py`
- [x] Deterministic build output (clean before build)

### Content Status
- **Total entries**: 2,244
- **JLPT N5 coverage**: ~95% complete
- **JLPT N4 coverage**: ~430 entries added
- **JLPT N3 vocabulary**: ~175 entries added
- **Candidate words**: ~1,816 words tracked in `candidate_words.json`
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Entry Breakdown by JLPT Level
| Level | Count | Status |
|-------|-------|--------|
| N5 | ~761 | Complete |
| N4 | ~392 | In progress |

### Entry Breakdown by Type
| Type | Count | Notes |
|------|-------|-------|
| Verbs | ~220 | Includes 95 N4 verbs with transitivity info |
| Nouns | ~430 | Includes N4 nouns, katakana loanwords |
| Adjectives | ~100 | I-adjectives and na-adjectives |
| Adverbs | ~56 | Includes 11 new N4 adverbs |
| Particles | 10 | Core particles with predicate lists |
| Counters | ~21 | Common counting patterns |
| Keigo verbs | 12 | Honorific and humble forms |
| Other | ~150 | Expressions, suffixes, etc. |

## v2 Quality Standards

Based on multi-model LLM evaluation (Claude Haiku 4.5, GPT-5.2, Gemini 3 Flash), these are the priority enhancements:

### HIGH PRIORITY
1. **Verb transitivity** - Add 自動詞/他動詞 and pair verbs to all verb entries
2. **Aspect notes** - Explain ている behavior for verbs with non-obvious meanings
3. **Particle predicate lists** - List verbs/adjectives requiring each particle
4. **Collocation patterns** - Add common noun-verb pairings

### MEDIUM PRIORITY
1. **Register labels** - Mark casual/neutral/formal for all entries
2. **Similar words** - Add contrastive sections for semantic neighbors
3. **Adjective forms** - Add adverbial (〜く/〜に) and noun forms (〜さ)
4. **Example progression** - Ensure simple → complex ordering

### LOW PRIORITY
1. **Kanji orthography notes** - When to use kanji vs. hiragana
2. **Cultural notes** - Expand where significant
3. **Keigo references** - Link to honorific forms

## Claude Code Skills

Available in `.claude/skills/` (automatically loaded when relevant):

| Skill | Use When |
|-------|----------|
| `entry-guidelines` | Creating any entry |
| `verb-entry` | Creating/revising verb entries |
| `adjective-entry` | Creating/revising adjective entries |
| `particle-entry` | Creating/revising particle entries |
| `other-entries` | Creating nouns, counters, adverbs, expressions |
| `revise-entries` | Revising existing entries to v2 standards |
| `vocabulary-notes` | Formatting notes field content |
| `cross-reference-entry` | Adding cross-references between entries |

## Recent Changes

### 2026-01-11 (Vocabulary Expansion - 33 New Entries, Session 3)
- Added 33 new dictionary entries (2,211 → 2,244 total)
- Resolved 5 pending cross-references:
  - 絵 (え) - picture
  - 行き (いき) - going, outward journey
  - 損害 (そんがい) - damage
  - 需要 (じゅよう) - demand
  - 混んでいる (こんでいる) - to be crowded
- Added ~28 high-priority N3/N4 vocabulary including:
  - Nouns: 金, 髪の毛, 活用, 過程, 間隔, 記入, 片付け, 泳ぎ, 外交, 学歴, 癌, 機関, 生地, 気体, 協議, 笑い
  - Adjectives: 苦しい, 急激, 急速, 優しい, もったいない, 最高, 最低
  - Verbs: 苦しむ, 亡くなる, 無くなる
- Cross-references increased from 526 to 567 (97% resolution rate)
- Removed 25 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 47 New Entries, Session 2)
- Added 47 new dictionary entries (2,164 → 2,211 total)
- Resolved 11 pending cross-references:
  - Nouns: 終了, 恩人, 担当, 縮小, 負け, 視聴者, 被害, 研究者
  - Verbs: 転がる, 混む, くつろぐ
  - Adverb: つい
  - Expression: 本当は
- Added ~35 high-priority N3/N2 vocabulary candidates including:
  - Nouns: 勘定, 画家, 寄付, 恐怖, 休息, 救助, 教授, 共通, 共同, 株, 感覚, 依頼, 汚染, 絵画, 規制, 供給, 強調, 仮定, 加減, 解釈, 学問, 会合, 競技, 額, 吸収, 柄, 籠, 貸し, 借り
  - Adjectives: 巨大, 温暖, かわいそう, 気の毒
  - Pronoun: あなた
  - Expression: おしゃれ
- Cross-references increased from 491 to 526 (98% resolution rate)
- Removed 35 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 47 New Entries)
- Added 47 new dictionary entries (2,117 → 2,164 total)
- Resolved 16 pending cross-references:
  - Nouns: あさねぼう, おゆ, しょうさい, とうちゃく, ふよう, ぼうりょく, りこん, 会員, 会計, 観客, 休暇, 詳細, etc.
  - Verbs: えんきする, かんせいさせる, きえる, ころがす, まげる, りらっくす, すいている
  - Adjectives: しおからい
  - Adverbs/Expressions: じつは, およそ, いつの間にか, 思わず
- Added ~30 high-priority N3/N4 vocabulary candidates including:
  - Nouns: 恩, 覚悟, 係, 拡大, 活気, 感じ, 歓迎, 観察, 感心, 完了, 火災, 驚き, 活躍, 勝ち, etc.
  - Other: お前 (pronoun), 決まり (rule)
- Cross-references increased from 437 to 491 (96% resolution rate)
- Removed 34 candidates from candidate_words.json

### 2026-01-11 (Vocabulary Expansion - 42 New Entries)
- Added 42 new dictionary entries (2,074 → 2,116 total)
- Resolved pending cross-references including へ particle entry
- New entries include:
  - Particle: へ (direction marker)
  - Nouns: はじまり, とかい, やかん, はやおき, きんちょう, けっせき, まんぞく, ふまん, ゆうき, しんじん, こうはい, ひみつ, あいさつ, きずな, たいおう, たいさく, けっこん, etc.
  - Verbs: にがす, ゆらす, おくらせる
  - Adjectives: なつかしい, くわしい, しょっぱい, ふひつよう, らんぼう
  - Adverbs: たいてい, なかなか, ぜひ, まもなく, おそらく, とくに
- Cross-references increased from 400 to 437 (96% resolution rate)
- Removed 18 candidates from candidate_words.json

### 2026-01-11 (Code Quality Improvements)
- Created shared utility modules:
  - `build/path_utils.py`: Consolidated `get_entry_prefix()` from 5 files
  - `build/japanese_utils.py`: Hiragana/romaji conversion, kana mappings
- Made cross-reference resolution deterministic (headword disambiguation for 132 homophone readings)
- Added audio integrity check to `validate.py` (checks for missing/orphaned audio files)
- Made build output deterministic (cleans all generated files before rebuild)
- Fixed double-loading in validation (eliminated ~2074 redundant file reads)
- Migrated all cross-references to structured format (removed legacy string format from schema)
- Updated Python version requirement to 3.10+

### 2026-01-11 (Prefix-Based Subdirectory Reorganization)
- Reorganized entries into prefix-based subdirectories to avoid GitHub's 1,000 file/directory limit
- Entry structure: `entries/{kana}/{prefix}/{id}.json` (prefix = first 2 chars of entry ID)
- HTML output: `docs/entries/{kana}/{prefix}/{id}.html`
- Audio structure: `audio/{kana}/{prefix}/{id}-exN.mp3`
- Updated validation to check prefix directory placement
- Simplified `build/build.py` (SPA version removed, flat HTML is now the only output)
- All 2,074 entries migrated successfully
- Scalable to 10,000+ entries

### 2026-01-10 (Flat HTML Site Build)
- Static HTML site generation (`build/build_flat.py`)
- Each entry gets its own standalone HTML page
- Navigation pages: index.html, search.html, browse.html, recent.html, random.html
- Compact search index with minimal entry data for fast loading
- Works without JavaScript (native HTML5 audio controls, expandable browse sections)
- Cross-reference links work between entry pages

### 2026-01-10 (Audio Pronunciation Support)
- Implemented audio playback for example sentences
- Audio files stored as MP3 in `audio/{kana}/{prefix}/` directory structure
- Web interface shows play/stop buttons for examples with audio
- Created `build/merge_audio.py` for processing new audio files
- Build process copies audio to `docs/audio/` preserving folder structure
- Audio integrity validation added to `validate.py`

### 2026-01-10 (Cross-Reference Linking System)
- Implemented structured cross-reference schema (type, reading, headword, label)
- Added link resolution in build pipeline (`build/resolve_links.py`)
- Added "Related Words" section to entry display in web interface
- Added validation for cross-reference format
- Created `cross-reference-entry` skill for systematic additions
- Reference types: pair, synonym, antonym, keigo, related, see_also, contrast
- Deterministic resolution with headword disambiguation for homophones

### 2026-01-09 (N3 Vocabulary Expansion)
- Added 50 new N3 vocabulary entries from candidate_words.json
- New entries include: na-adjectives (完全, 様々, 正直, 真剣, 深刻, 地味, 重要, 清潔, 積極的, 適切, 奇妙, 公平), nouns (完成, 区別, 現在, 種類, 事件, 状況, 人類, 専攻, 当時, 昼食, 残り, 維持, 一種, 差別, 財産, 使用, 性質, 重大), adverbs (じっと, 既に, 相当, 当然, 常に, 非常, ますます, 主に, 大いに, さて, ただ, 多少, のんびり), verbs (まとまる, 見かける), and other types
- Updated entries_index.json (1,880 entries total)
- Removed 49 added words from candidate_words.json (2,117 remaining)

### 2026-01-08 (Entry Tracking System)
- Created `entries_index.json` listing all 1,153 entries with key metadata
- Created `candidate_words.json` with 1,992 candidate words for future addition
- Added build scripts: `update_entries_index.py`, `manage_candidates.py`, `update_indexes.py`
- Removed N3_VOCABULARY_TO_ADD.md and N4_VOCABULARY_TO_ADD.md (data now in candidate_words.json)

### 2026-01-08 (N4 Vocabulary Expansion)
- Added 183 new N4 vocabulary entries (nouns, katakana loanwords, adverbs, counters, suffixes)
- Total entries now 1,153
- Removed 34 duplicate entries from N3 vocabulary list

### 2026-01-09 (Interface Refinements)
- Removed Compare mode
- Added Recent mode showing most recently added/revised entries (250 entries)
- Added Random mode with word cloud display
- Fixed Browse mode display on narrow screens

### 2026-01-08 (Web Interface Update)
- Added multiple interface modes: Search, Browse
- Sticky header with interface toggle and furigana button
- Browse mode with filters for JLPT level, part of speech, starting kana

### Previous Sessions
- Added 62 N4 vocabulary entries (adverbs, keigo verbs, nouns, katakana loanwords)
- Removed "New" tag functionality from dictionary
- Added vocabulary-notes skill for formatting guidelines
- Updated web interface to handle paragraph breaks and bullet points in notes
- Reformatted 154 entries with proper bullet point formatting

## Next Steps

### Ongoing (Vocabulary Expansion)
1. Continue adding vocabulary from `candidate_words.json` (see workflow below)
2. Maintain v2 quality standards for all new entries
3. Add cross-references when creating new entries

### Future Enhancements
1. Add conjugation search
2. Export to Anki format
3. Create automated test suite for build scripts
4. Add PWA features for offline use

## Workflow: Adding Entries from Candidates

Follow this step-by-step process when adding new dictionary entries from `candidate_words.json`:

### Step 1: Select Candidates
1. Review `candidate_words.json` to choose words to add
2. Prioritize by JLPT level (N5 → N4 → N3) or thematic groups
3. Check that the candidate hasn't already been added to the dictionary

### Step 2: Create Entry Files
1. Create the JSON entry file following the schema (`build/schema.json`)
2. Use the appropriate Claude skill based on entry type:
   - Verbs: `verb-entry` skill
   - Adjectives: `adjective-entry` skill
   - Particles: `particle-entry` skill
   - Others: `other-entries` skill
3. Follow `vocabulary-notes` skill for notes formatting
4. Place file in correct directory based on reading and ID:
   - Directory: `entries/{kana}/{prefix}/` where:
     - `{kana}`: Based on first kana of reading (あ行 → `a/`, か行 → `ka/`, etc.)
     - `{prefix}`: First 2 characters of entry ID (e.g., `taberu_00001` → `ta/`)
   - Example: `entries/ta/ta/taberu_00001.json`
5. File naming: `{romaji}_{5-digit-id}.json`

### Step 3: Validate Entry
```bash
python3 build/validate.py --id {entry_id}
# Or validate all:
python3 build/validate.py
```

### Step 4: Update Indexes
**IMPORTANT: Run this after adding ANY entries:**
```bash
python3 build/update_indexes.py
```
This will:
- Update `entries_index.json` with the new entry
- Remove added words from `candidate_words.json` (sync)

### Step 5: Rebuild Website
**IMPORTANT: Run this to update the GitHub Pages site:**
```bash
python3 build/build_flat.py
```
This regenerates all HTML files in `docs/` which GitHub Pages serves. Without this step, new entries won't appear on the live site.

### Step 6: Add Cross-References
1. Use the `cross-reference-entry` skill for guidelines
2. Add structured references for:
   - Transitivity pairs (for verbs)
   - Keigo equivalents
   - Antonyms/opposites
   - Related vocabulary mentioned in notes
3. References can point to entries that don't exist yet

### Step 7: Commit Changes
Commit all changes including:
- New entry JSON files in `entries/`
- Updated `entries_index.json` and `candidate_words.json`
- Rebuilt `docs/` folder (required for GitHub Pages to update)

## Workflow: Adding Audio Files

### Step 1: Prepare Audio Files
Place MP3 files in `audio-to-add/` with the naming convention:
```
{entry_id}-ex{number}.mp3
```
Example: `taberu_00001-ex1.mp3` for the first example of entry `taberu_00001`

### Step 2: Merge Audio
```bash
python3 build/merge_audio.py
```
This will:
- Copy MP3 files to `audio/{kana}/{prefix}/` directory
- Update entry files to set `has_audio: true` on examples

### Step 3: Build and Test
```bash
python3 build/build.py
# Open docs/index.html to verify audio plays correctly
```

### Audio Directory Structure
Audio files are organized by kana and prefix (matching entries/):
```
audio/
├── a/           # あ行
│   ├── a_/      # Entries starting with 'a_'
│   ├── am/      # Entries starting with 'am'
│   └── ...
├── ka/          # か行
│   ├── ka/      # Entries starting with 'ka'
│   └── ...
└── ...
```

## Workflow: Adding Cross-References to Entries

### Cross-Reference Format
```json
"cross_references": [
  {
    "type": "pair",
    "reading": "しまる",
    "headword": "{閉|し}まる",
    "label": "intransitive"
  }
]
```

### Reference Types
| Type | Use For | Example |
|------|---------|---------|
| `pair` | Transitivity pairs | 閉める → 閉まる |
| `antonym` | Opposites | 大きい → 小さい |
| `keigo` | Honorific/humble | 食べる → 召し上がる |
| `synonym` | Similar meaning | 分かる → 理解する |
| `contrast` | Easily confused | は → が |
| `related` | Semantically connected | 食べる → 食べ物 |
| `see_also` | General reference | - |

## Technical Notes

### Build Commands
```bash
# Validate entries (includes schema, cross-refs, audio integrity)
python3 build/validate.py

# Validate a single entry
python3 build/validate.py --id taberu_00001

# Merge new audio files (from audio-to-add/)
python3 build/merge_audio.py

# Build dictionary
python3 build/build.py

# Update index files (after adding/removing entries)
python3 build/update_indexes.py

# Manage candidate words
python3 build/manage_candidates.py stats    # Show statistics
python3 build/manage_candidates.py add "漢字" "かんじ" "notes"  # Add candidate

# Cross-reference resolution report
python3 build/resolve_links.py

# View locally
open docs/index.html
```

### File Naming Convention
- Format: `{romanized_reading}_{5-digit-id}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: `entries/{kana}/{prefix}/` where:
  - `{kana}`: Based on first kana of reading (あ → `a/`, か → `ka/`, etc.)
  - `{prefix}`: First 2 characters of entry ID (e.g., `taberu` → `ta/`)
- Example: `entries/ta/ta/taberu_00001.json`
- Katakana loanwords: Use hiragana reading (e.g., アルバイト → あるばいと)

### Entry and Candidate Tracking
- **entries_index.json**: Auto-generated index of all dictionary entries
- **candidate_words.json**: Words to potentially add (each has unique ID like C00001)
- Run `python build/update_indexes.py` after modifying entries to keep indexes in sync

## Notes for AI Assistants

### Before Starting Work
1. Read this file to understand current state
2. Check `project_specification_v2.md` for detailed quality standards
3. Relevant skills will be auto-loaded based on task type

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase
- Katakana loanwords use hiragana in reading field

### Quality Standards
See `project_specification_v2.md` for comprehensive guidelines. Key points:
- **Verbs**: Transitivity type, pair verb, aspect/ている behavior, collocations
- **Particles**: Predicates requiring particle, contrast with similar particles
- **Adjectives**: Forms (adverbial, noun), similar word distinctions
- **All entries**: Consistent depth with similar entries

### After Each Session
Update this file with:
- Entries added/revised
- Any issues encountered
- Next steps
