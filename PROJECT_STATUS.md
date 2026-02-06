# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-06
**Current phase**: Phase 4 - Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

> **Note**: Older change history is archived in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).

## Current State

### Phase
**Phase 4: Vocabulary Expansion & Interface Enhancement** - Adding vocabulary while maintaining v2 quality standards, plus new web interface features. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Infrastructure Status
- [x] Directory structure created (prefix-based subdirectories for scalability)
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build_flat.py`)
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
- [x] Atomic build process (temp directory swap prevents broken states)
- [x] Centralized cross-reference type definitions (`build/cross_ref_types.py`)
- [x] Centralized furigana pattern and utilities (`build/japanese_utils.py`)
- [x] Enhanced validation with structured return types
- [x] Improved security (XSS prevention, no auto-install)

### Content Status
- **Total entries**: 10,306
- **Vocabulary tier assignment**: Basic: 801 | Core: 1,998 | General: 7,507 | Unassigned: 0 ✓
- **Candidate words**: 183 words tracked in `candidate_words.json`
- **Cross-references**: 3,313 total across 2,680 entries
- **Example sentences**: 40,185 total
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 801 entries (target: 600-800) - fundamental words for basic communication
- **Core**: 1,998 entries (target: 1,600-2,000) - words for adult-level communication
- **General**: 7,507 entries (no limit) - all other vocabulary useful for learners

**Tier realignment completed 2026-01-19.** All entries have tier assignments meeting target ranges. The basic and core tiers are curated to ensure semantic group integrity.

**Policy for new entries:** All new entries must be assigned to the **general** tier. The basic and core tiers are considered stable and should not be modified unless explicitly requested.

### Entry Breakdown by Type
| Type | Count | Notes |
|------|-------|-------|
| Verbs | ~1,200 | Includes transitivity and aspect info |
| Nouns | ~2,500 | Includes katakana loanwords |
| Adjectives | ~400 | I-adjectives and na-adjectives |
| Adverbs | ~200 | Time, manner, degree adverbs |
| Particles | 10 | Core particles with predicate lists |
| Counters | ~50 | Common counting patterns |
| Keigo verbs | 12 | Honorific and humble forms |
| Other | ~1,100 | Expressions, onomatopoeia, suffixes, etc. |

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
| `find-candidates` | Finding new candidate words for the dictionary |
| `resolve-duplicates` | Identifying and resolving duplicate entries |
| `delete-entry` | Safely deleting entries with proper cleanup |

## Recent Changes

### 2026-02-06 (Vocabulary Expansion - 30 New Entries, Session 220)
Added 30 new dictionary entries from candidate_words.json, covering a wide variety of useful general vocabulary:

- **Nouns (12)**: お{気|き}に{入|い}り (favorite), お{笑|わら}い (comedy), お{願|ねが}い (request/please), かき{氷|ごおり} (shaved ice), かまぼこ (fish cake), からくり (mechanism/trick), きっかけ (trigger/opportunity), くじ (lottery), {粥|かゆ} (rice porridge), {胡椒|こしょう} (pepper), {繰|く}り{返|かえ}し (repetition), ご{無沙汰|ぶさた} (long silence)
- **Verbs (6)**: {匿|かくま}う (to shelter), {庇|かば}う (to protect), {被|かぶ}せる (to cover), {潜|くぐ}る (to pass through), くっつく (to stick to), こだわる (to be particular about)
- **Na-adjectives (4)**: {微|かす}か (faint/slight), {気|き}まま (free-spirited), こまめ (frequent/diligent), ささやか (modest/humble)
- **I-adjective (1)**: くどい (persistent/heavy taste)
- **Adverbs (7)**: かつて (formerly), きっちり (precisely), きょとん (blankly), がらり (completely/drastically), {散々|さんざん} (severely/terribly), ごく (very/extremely), {繰|く}り{返|かえ}し (repeatedly)

Notable entry features:
- Multi-sense entries: かつて (past/never with negative), {被|かぶ}せる (cover/put on/blame), こだわる (quality standards/fixation), がらり (dramatic change/sliding sound)
- Food-related cluster: かき{氷|ごおり}, かまぼこ, {粥|かゆ}, {胡椒|こしょう}, かぼちゃ
- Cultural notes: かき{氷|ごおり} (summer tradition), {粥|かゆ} ({七草|ななくさ}{粥|がゆ}), かまぼこ (おせち{料理|りょうり}), からくり ({江戸時代|えどじだい} automata)
- Transitivity pairs: くっつく/くっつける, {被|かぶ}せる/{被|かぶ}る

Total entries: 10,276 → 10,306
Remaining candidates: 183 → 153
New kanji: 2,245 → 2,249 ({匿|とく}, {庇|ひ}, {椒|しょう}, {粥|しゅく})

### 2026-02-05 (Vocabulary Expansion - 30 New Entries, Session 219)
Added 30 new dictionary entries from candidate_words.json, covering casual expressions, household items, administrative documents, finance, social media, and daily life:

- **Casual Expressions/Interjections (2)**: しまった (oh no!), やった (yay!)
- **Mimetic/Onomatopoeia (3)**: いちゃいちゃ (flirting), ちやほや (pampering), のりのり (in high spirits)
- **Adjective (1)**: {怪|あや}しい (suspicious/dubious)
- **Social/Cultural (3)**: {合|ごう}コン (group blind date), お{一人|ひとり}{様|さま} (solo customer), おばちゃん (auntie/middle-aged woman)
- **Household Items (4)**: お{箸|はし} (chopsticks), {三角|さんかく}コーナー (sink strainer), {水切|みずき}りかご (dish drainer), レンジ{対応|たいおう} (microwave-safe)
- **Administrative Documents (5)**: {転居届|てんきょとどけ} (change of address), {印鑑証明|いんかんしょうめい} (seal certificate), {戸籍謄本|こせきとうほん} (family register copy), {訂正印|ていせいいん} (correction seal), {二重線|にじゅうせん} (double strikethrough)
- **Finance/Business (4)**: {不均衡|ふきんこう} (imbalance), {仲介手数料|ちゅうかいてすうりょう} (brokerage fee), {比較検討|ひかくけんとう} (comparative evaluation), {反落|はんらく} (reactionary drop)
- **Daily Life/Labels (3)**: {年度始|ねんどはじ}め (start of fiscal year), {保存方法|ほぞんほうほう} (storage instructions), バーコード (barcode)
- **Transportation (1)**: {弱冷房車|じゃくれいぼうしゃ} (mildly air-conditioned car)
- **Technology/SNS (3)**: タグ{付|づ}け (tagging), {既読|きどく}スルー (leaving on read), メモる (to jot down)
- **Reference (1)**: {取扱説明書|とりあつかいせつめいしょ} (user manual)

Notable entry features:
- Multi-sense entries: {怪|あや}しい (suspicious/dubious), お{一人|ひとり}{様|さま} (service/cultural), おばちゃん (family/general)
- Administrative document trio: {転居届|てんきょとどけ}, {印鑑証明|いんかんしょうめい}, {戸籍謄本|こせきとうほん}
- Correction process pair: {訂正印|ていせいいん} + {二重線|にじゅうせん}
- Modern Japanese terms: {既読|きどく}スルー, タグ{付|づ}け, メモる

Total entries: 10,246 → 10,276
Remaining candidates: 141 → 112
New kanji: 2,242 → 2,245 ({怪|かい}, {訂|てい}, {謄|とう})

### 2026-02-05 (Vocabulary Expansion - 30 New Entries, Session 218)
Added 30 new dictionary entries from candidate_words.json, focusing on daily life, food, family, and practical vocabulary:

- **Na-adjectives (2)**: うってつけ (ideal/perfect for), {虚|うつ}ろ (hollow/vacant)
- **I-adjectives (2)**: {惜|お}しい (regrettable/close), {惜|お}しげもなく (without hesitation)
- **Food (5)**: うに (sea urchin), オクラ (okra), お{浸|ひた}し (boiled greens), おむすび (rice ball), レトルト (retort pouch food)
- **Family (3)**: おふくろ (mother informal), おやじ (father informal), {乙女|おとめ} (maiden)
- **Daily Life Items (4)**: {上履|うわば}き (indoor shoes), ストロー (straw), ナプキン (napkin), カート (cart)
- **Signs/Status (2)**: {点検中|てんけんちゅう} (under inspection), {清掃中|せいそうちゅう} (cleaning in progress)
- **Business/Finance (4)**: {内税|うちぜい} (tax-inclusive), {外税|そとぜい} (tax-exclusive), {擦|す}り{合|あ}わせ (coordination), お{墨付|すみつ}き (seal of approval)
- **Other (8)**: おい (hey), {折|おり} (occasion), お{好|この}み{焼|や}き (okonomiyaki), お{客|きゃく}さん (guest/customer), {思|おも}い (thought/feeling), {咳|せ}き{込|こ}む (coughing fit), {決|き}め{付|つ}け (jumping to conclusions), {赤面症|せきめんしょう} (tendency to blush)

Notable entry features:
- Multi-sense entries: {虚|うつ}ろ (hollow/vacant), {惜|お}しい (regrettable/close), ナプキン (table/sanitary), おやじ (father/shop owner), カート (shopping/go-kart)
- Informal family terms: おふくろ, おやじ (commonly used by men)
- Practical daily life vocabulary useful for living in Japan
- Tax terminology pair: {内税|うちぜい}/{外税|そとぜい}

Total entries: 10,216 → 10,246
Remaining candidates: 170 → 141

### 2026-02-05 (Vocabulary Expansion - 30 New Entries, Session 217)
Added 30 new dictionary entries from candidate_words.json, focusing on common vocabulary, grammar, and daily life:

- **Food (4)**: アサリ (short-neck clam), {小豆|あずき} (azuki bean), {餡|あん} (sweet bean paste), インゲン (green beans)
- **Verbs (7)**: あしらう (to treat/garnish), {当|あ}てはまる (to apply to), {当|あ}てはめる (to apply), ありふれる (to be common), あてがう (to allot), {伺|うかが}う (to visit/ask, humble)
- **Adverbs (8)**: あたかも (as if), {如何|いかが} (how, polite), {如何|いか}に (how, no matter how), {生|い}き{生|い}き (lively), {至|いた}って (very), {未|いま}だ (still/yet), うっすら (faintly)
- **Adjectives (3)**: {有難|ありがた}い (grateful), {嫌|いや} (unpleasant), いやらしい (nasty/vulgar)
- **Nouns (8)**: あだ{名|な} (nickname), あの{世|よ} (afterlife), あらすじ (synopsis), ありったけ (all one has), {在|あ}り{方|かた} (ideal state), {出|い}で{立|た}ち (attire), {暇|いとま} (spare time/leave), {今時|いまどき} (nowadays), {芋|いも} (potato)
- **Prank/Mischief (1)**: {悪戯|いたずら} (prank/mischief)

Notable entry features:
- Multi-sense entries: あしらう (treat/garnish), {餡|あん} (sweet paste/thick sauce), {如何|いか}に (how/no matter how), {悪戯|いたずら} (prank/tampering), {暇|いとま} (time/leave), あてがう (apply/allot)
- Humble language: {伺|うかが}う (to visit/ask)
- Formal vocabulary: あたかも, {如何|いかが}, {如何|いか}に, {未|いま}だ
- 3 new kanji added to kanji index: {伺|shi}, {戯|gi}, {芋|u}

Total entries: 10,041 → 10,071
Remaining candidates: 200 → 170
New kanji: 2,239 → 2,242

### 2026-02-05 (Vocabulary Expansion - 30 New Entries, Session 216)
Added 30 new dictionary entries from candidate_words.json, focusing on technology, daily life, business, travel, and literary vocabulary:

- **Technology (3)**: {外部機器|がいぶきき} (external device), {入力装置|にゅうりょくそうち} (input device), {出力装置|しゅつりょくそうち} (output device)
- **Academic (2)**: {論文発表|ろんぶんはっぴょう} (paper presentation), {学位|がくい} (academic degree)
- **Food/Culture (2)**: {鉄板焼|てっぱんや}き (teppanyaki), お{品書|しなが}き (menu)
- **Urban/Transportation (5)**: {立体駐車場|りったいちゅうしゃじょう} (multi-story parking), {山手|やまのて} (uptown area), {通勤時間|つうきんじかん} (commute time), {網棚|あみだな} (luggage rack), {精算機|せいさんき} (fare adjustment machine)
- **Weather (2)**: {真夏日|まなつび} (hot summer day), {熱帯夜|ねったいや} (tropical night)
- **Daily Life/Items (3)**: {乾電池|かんでんち} (battery), {両替機|りょうがえき} (change machine), {新発売|しんはつばい} (new release)
- **Community (2)**: {回覧板|かいらんばん} (neighborhood circular), {町内会|ちょうないかい} (neighborhood association)
- **Business/Finance (4)**: {年末調整|ねんまつちょうせい} (year-end tax adjustment), {立替|たてか}え (advance payment), {年度末|ねんどまつ} (end of fiscal year), {減給|げんきゅう} (salary cut)
- **Literary/Time (2)**: {薄暮|はくぼ} (dusk), {黎明|れいめい} (dawn)
- **Personality/Ability (2)**: {持|も}ち{味|あじ} (distinctive quality), {得手|えて} (forte)
- **Travel (2)**: {預|あず}け{荷物|にもつ} (checked baggage), {機内持|きないも}ち{込|こ}み (carry-on)
- **Verbs (1)**: {蹴落|けお}とす (to kick down/defeat rivals)

Notable entry features:
- Multi-sense entries: {黎明|れいめい} (dawn/beginning of era)
- Practical daily life vocabulary for living in Japan
- Weather and seasonal terms used in forecasts
- Business and tax terminology
- 2 new kanji added to kanji index: {穂|sui}, {黎|rei}

Total entries: 10,011 → 10,041
Remaining candidates: 177 → 148
New kanji: 2,237 → 2,239

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).


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
4. Place file in correct directory based on numeric ID range:
   - Directory: `entries/{range}/` where `{range}` is based on the 5-digit ID:
     - IDs 00001-00499 → `entries/00000/`
     - IDs 00500-00999 → `entries/00500/`
     - IDs 01000-01499 → `entries/01000/`
     - etc. (500 entries per directory)
   - Example: `entries/00000/00396_taberu.json`
5. File naming: `{5-digit-id}_{romaji}.json`

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
python3 build/validate.py --id 00396_taberu

# Merge new audio files (from audio-to-add/)
python3 build/merge_audio.py

# Build dictionary
python3 build/build_flat.py

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
- Format: `{5-digit-id}_{romanized_reading}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: `entries/{range}/` where `{range}` is based on the numeric ID:
  - IDs 00001-00499 → `entries/00000/`
  - IDs 00500-00999 → `entries/00500/`
  - IDs 01000-01499 → `entries/01000/`
  - etc. (500 entries per directory)
- Example: `entries/00000/00396_taberu.json`
- Katakana loanwords: Use hiragana reading (e.g., アルバイト → あるばいと)

### Entry and Candidate Tracking
- **entries_index.json**: Auto-generated index of all dictionary entries
- **candidate_words.json**: Words to potentially add (each has unique ID like C00001)
- Run `python build/update_indexes.py` after modifying entries to keep indexes in sync

## Notes for AI Assistants

### Before Starting Work
1. Read this file to understand current state
2. Relevant skills will be auto-loaded based on task type (see Claude Code Skills table above)
3. Use the `entry-guidelines` skill for general quality standards

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase
- Katakana loanwords use hiragana in reading field
- **sense_numbers required**: All examples must have `sense_numbers` field populated
  - Single-sense entries: use `[1]` for all examples
  - Multi-sense entries: each example must specify which sense(s) it illustrates

### Quality Standards
See the `entry-guidelines` skill for comprehensive guidelines. Key points:
- **Verbs**: Transitivity type, pair verb, aspect/ている behavior, collocations
- **Particles**: Predicates requiring particle, contrast with similar particles
- **Adjectives**: Forms (adverbial, noun), similar word distinctions
- **All entries**: Consistent depth with similar entries

### After Each Session
Update the "Recent Changes" section in this file with:
- Entries added/revised
- Any issues encountered

**Note**: Keep only the 5 most recent change entries. When adding a new entry, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
