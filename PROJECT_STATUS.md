# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-19
**Current phase**: Phase 4 - Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

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
- **Total entries**: 7,389
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 4,596 | Unassigned: 0 ✓
- **Candidate words**: ~533 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 795 entries (target: 600-800) - fundamental words for basic communication
- **Core**: 1,998 entries (target: 1,600-2,000) - words for adult-level communication
- **General**: 4,566+ entries (no limit) - all other vocabulary useful for learners

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

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 133)
Added 30 new dictionary entries from candidate_words.json, focusing on body-part idioms, expressions about skills/strangers, fate/destiny vocabulary, and abstract nouns:

- **Compound verbs (3)**: {湧|わ}き{出|で}る (to gush out), {突|つ}き{落|お}とす (to push down), {差|さ}し{戻|もど}す (to send back)
- **Body-part idioms (9)**: {息|いき}を{潜|ひそ}める (to hold one's breath), {唇|くちびる}を{噛|か}む (to bite one's lip), {目|め}を{丸|まる}くする (to be wide-eyed), {鼻|はな}で{笑|わら}う (to sneer), {手|て}を{打|う}つ (to take measures), {手|て}を{染|そ}める (to get involved), {腕|うで}を{振|ふ}るう (to show skill), {腕|うで}を{磨|みが}く (to hone skills), {目|め}を{奪|うば}われる (to be captivated)
- **Stranger/newcomer vocabulary (5)**: {赤|あか}の{他人|たにん} (complete stranger), {見|み}ず{知|し}らず (total stranger), {古株|ふるかぶ} (old-timer), {新顔|しんがお} (newcomer), {一見|いちげん} (first-time customer)
- **Fate/destiny nouns (2)**: {因縁|いんねん} (fate/karma), {定|さだ}め (fate/destiny)
- **Yojijukugo (2)**: {大同小異|だいどうしょうい} (essentially the same), {不可思議|ふかしぎ} (mysterious)
- **Abstract nouns (8)**: {取|と}り{締|し}まり (crackdown), {巻|ま}き{添|ぞ}え (getting caught up in), {心得|こころえ} (knowledge), {手腕|しゅわん} (skill), {固定観念|こていかんねん} (preconception), {勝|か}ち{気|き} (competitive spirit), {自己嫌悪|じこけんお} (self-loathing), {別|わか}れ{際|ぎわ} (moment of parting)
- **Humble gift noun (1)**: {粗品|そしな} (small gift)

Notable entry features:
- Body-part idiom group with 手, 目, 鼻, 唇, 息, 腕 covering emotions and actions
- Skill-related expressions: {腕|うで}を{振|ふ}るう ↔ {腕|うで}を{磨|みが}く (show vs. hone)
- Stranger vocabulary: {赤|あか}の{他人|たにん} ↔ {見|み}ず{知|し}らず (both mean complete stranger, with etymology notes)
- {古株|ふるかぶ} ↔ {新顔|しんがお} antonym pair for workplace veterans/newcomers
- {一見|いちげん}さんお{断|ことわ}り cultural note about Japanese establishments
- Buddhist origin notes for {因縁|いんねん} and {不可思議|ふかしぎ}
- {粗品|そしな} with Japanese gift-giving culture context

Total entries: 7,359 → 7,389
Remaining candidates: ~563 → ~533

### 2026-01-19 (Vocabulary Tier Realignment Complete - Phase 4 & 5)
Completed the vocabulary tier realignment project (Phases 4 and 5):

**Phase 4: Assigned 200 unassigned entries**
- All previously unassigned entries have been assigned to the general tier
- Categories included: four-character idioms (yojijukugo), proverbs, traditional Japanese items, modern tech/business terms, medical terms, work terms, -teki adjectives, onomatopoeia, and compound verbs

**Phase 5: Validation and finalization**
- Verified final tier counts meet targets:
  - Basic: 795 (target: 600-800) ✓
  - Core: 1,998 (target: 1,600-2,000) ✓
  - General: 4,566 (no limit) ✓
  - Unassigned: 0 (target: 0) ✓
- Ran full validation (7,357/7,359 entries valid)
- Updated indexes and rebuilt flat HTML
- Updated PROJECT_STATUS.md

The tier realignment project is now complete. All 7,359 dictionary entries have vocabulary tier assignments that meet the target ranges specified in the vocabulary-tiers skill guidelines.

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 132)
Added 30 new dictionary entries from candidate_words.json, focusing on verbs describing physical/state changes, language/dialect vocabulary, suru-verbs for social dynamics, and idiomatic expressions:

- **Verbs (7)**: {錆|さ}びる (to rust), {軋|きし}む (to creak), {籠|こ}もる (to shut oneself in), {溜|た}め{込|こ}む (to hoard), {染|し}み{付|つ}く (to become ingrained), {引|ひ}っ{込|こ}む (to withdraw), {燻|くすぶ}る (to smolder)
- **Language/dialect nouns (3)**: {方言|ほうげん} (dialect), {訛|なま}り (accent), {標準語|ひょうじゅんご} (standard language)
- **Suru-verbs for social dynamics (9)**: {妥協|だきょう} (compromise), {傍観|ぼうかん} (looking on), {介入|かいにゅう} (intervention), {同調|どうちょう} (conformity), {停滞|ていたい} (stagnation), {衰退|すいたい} (decline), {躍進|やくしん} (rapid advance), {逡巡|しゅんじゅん} (hesitation), {迷走|めいそう} (straying)
- **Other nouns (5)**: {音色|ねいろ} (tone/timbre), {配偶者|はいぐうしゃ} (spouse), {仕入|しい}れ (stocking), {仕上|しあ}がり (finish), {手持|ても}ち (on hand)
- **Mimetic (1)**: むしゃむしゃ (munching)
- **Adverbs (2)**: まして (let alone), たいして (not very)
- **Idiomatic expressions (3)**: {舌|した}を{巻|ま}く (to be amazed), {手|て}を{焼|や}く (to have trouble with), {頭|あたま}を{抱|かか}える (to be at a loss)

Notable entry features:
- Complete language/dialect vocabulary group with cross-references: {方言|ほうげん}, {訛|なま}り, {標準語|ひょうじゅんご}
- Social dynamics suru-verbs with antonym pairs: {傍観|ぼうかん} ↔ {介入|かいにゅう}, {停滞|ていたい} ↔ {躍進|やくしん}, {衰退|すいたい} ↔ {繁栄|はんえい}
- Body-part idioms: {舌|した}を{巻|ま}く, {手|て}を{焼|や}く, {頭|あたま}を{抱|かか}える
- {同調圧力|どうちょうあつりょく} (peer pressure) cultural note in {同調|どうちょう} entry
- Verbs describing physical changes: {錆|さ}びる (rusting), {軋|きし}む (creaking), {燻|くすぶ}る (smoldering) with figurative uses

Total entries: 7,329 → 7,359
Remaining candidates: ~592 → ~563

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 131)
Added 30 new dictionary entries from candidate_words.json, focusing on progress/process verbs, emotional adjectives, speech-related nouns, status expressions, and mimetics:

- **Verbs (7)**: {煮詰|につ}まる (to boil down/be stuck), うつむく (to look down), {拗|こじ}れる (to get complicated), {揉|も}める (to have trouble), {捗|はかど}る (to make progress), {滞|とどこお}る (to stagnate), {凌|しの}ぐ (to endure/surpass)
- **I-adjectives (3)**: やるせない (helpless/forlorn), {空|むな}しい (empty/futile), しんどい (tiring/exhausting)
- **Na-adjectives (2)**: {不用意|ふようい} (careless), {不可解|ふかかい} (incomprehensible)
- **Speech/words nouns (4)**: {寝言|ねごと} (sleep-talking), たわ{言|ごと} (nonsense), {繰|く}り{言|ごと} (repetitive complaints), {減|へ}らず{口|ぐち} (backtalk)
- **Social/everyday nouns (7)**: {待|ま}ち{合|あ}わせ (meeting up), {後回|あとまわ}し (putting off), お{手上|てあ}げ (giving up), {巡|めぐ}り{合|あ}わせ (fate/chance), {宿命|しゅくめい} (destiny), {井戸端会議|いどばたかいぎ} (gossip session), {二枚目|にまいめ}/{三枚目|さんまいめ} (handsome man/comedian from kabuki)
- **Status nouns (2)**: {格上|かくうえ} (higher rank), {格下|かくした} (lower rank)
- **Mimetics/Adverbs (5)**: ちらちら (flickering/glancing), めきめき (rapidly improving), ぴりぴり (tingling/tense), {晴|は}れ{晴|ば}れ (cheerfully)

Notable entry features:
- Progress/stagnation verbs as antonym pair: {捗|はかど}る ↔ {滞|とどこお}る with cross-references
- Emotional vocabulary: やるせない (with etymology from {遣|や}る{瀬|せ}), {空|むな}しい (empty/futile)
- Japanese speech patterns: 〜{言|ごと} suffix words ({寝言|ねごと}, たわ{言|ごと}, {繰|く}り{言|ごと})
- Kabuki terminology: {二枚目|にまいめ}/{三枚目|さんまいめ} with historical context
- しんどい with Kansai dialect origin note
- Mimetics covering visual (ちらちら), progress (めきめき), sensation (ぴりぴり), and emotion ({晴|は}れ{晴|ば}れ)

Total entries: 7,299 → 7,329
Remaining candidates: ~622 → ~592

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 130)
Added 30 new dictionary entries from candidate_words.json, focusing on expressive verbs, emotions/personality adjectives, adverbs, weather/disaster vocabulary, and common expressions:

- **Expressive verbs** (14): ぼやく (complain), からかう (tease), むくむ (swell), うずく (ache), たじろぐ (flinch), なびく (sway), ひるむ (cower), とどろく (roar), いたわる (care for), おののく (tremble), ひらめく (flash), ときめく (flutter), さえずる (chirp), つるむ (hang out)
- **I-adjectives** (4): ぎこちない (awkward), ややこしい (complicated), いたましい (pitiful), けだるい (languid)
- **Adverbs** (2): おもむろに (slowly/deliberately), たちまち (instantly)
- **Facilities/Places** (3): {物置|ものお}き (storage shed), {待合室|まちあいしつ} (waiting room), {避難所|ひなんじょ} (evacuation shelter)
- **Weather/Nature** (3): {紫外線|しがいせん} (UV rays), {濃霧|のうむ} (dense fog), {落雷|らくらい} (lightning strike)
- **Business/Technology** (2): {添付|てんぷ} (attachment), {進捗|しんちょく} (progress)
- **Expressions** (2): しかたがない (it can't be helped), しょうがない (it can't be helped - colloquial)

Notable entry features:
- Strong coverage of expressive/onomatopoeic verbs: body sensations (むくむ, うずく), emotions (ときめく, おののく), sounds (とどろく, さえずる)
- Fear/hesitation verbs: たじろぐ, ひるむ with nuance distinctions
- Adjectives for describing awkwardness and emotional states: ぎこちない, ややこしい, けだるい
- おもむろに with note about common misunderstanding (often mistakenly believed to mean "suddenly")
- Disaster/emergency vocabulary: {避難所|ひなんじょ}, {落雷|らくらい} with safety notes
- Commonly used expressions: しかたがない/しょうがない pair with cross-references

Total entries: 7,269 → 7,299
Remaining candidates: ~651 → ~622

### 2026-01-19 (New Candidates - 104 Words Added, Session 129)
Added 104 new candidate words to `candidate_words.json` with balanced coverage across multiple categories:

**Expressions & Adverbs** (~10 words):
- しかたがない/しょうがない (it can't be helped), 案の定 (as expected), ぞんざい (careless/rude), おもむろに (slowly), たちまち (instantly)

**Adjectives - Personality & Emotions** (~25 words):
- Negative traits: ぎこちない (awkward), ややこしい (complicated), こすい (cunning), せこい (stingy), けばい (gaudy)
- Emotional states: いたましい (pitiful), けだるい (languid), ものがなしい (melancholy), いまいましい (annoying), おぞましい (loathsome)
- Character descriptions: さりげない (casual), よそよそしい (distant), あっけない (anticlimactic), そっけない (curt), たどたどしい (faltering)
- Intensity: すさまじい (tremendous), おびただしい (numerous), ものものしい (imposing), なまめかしい (alluring)

**Verbs - Expressive & Onomatopoeic** (~30 words):
- Speech/communication: ぼやく (complain), からかう (tease), ねだる (beg), ほざく (babble), あざける (mock), おだてる (flatter), あおる (provoke)
- Physical states: むくむ (swell), うずく (ache), ぼける (become senile), ふやける (become soggy)
- Body language: うなだれる (hang head), はにかむ (be shy), たじろぐ (flinch), ひるむ (cower), よどむ (stagnate)
- Movement/sound: なびく (sway), とどろく (roar), かすれる (become hoarse), どよめく (stir), きらめく (glitter), ひらめく (flash), ときめく (flutter), ざわめく (rustle), さえずる (chirp)
- Relationships: つるむ (hang out), いたわる (care for), おとずれる (visit), おののく (tremble)

**Nouns - Places & Facilities** (~15 words):
- Buildings: 物置 (storage shed), 土間 (dirt floor), 軒下 (under eaves), 表口 (front entrance), 待合室 (waiting room), 作業場 (workshop), 集会所 (meeting hall)
- Infrastructure: 配線 (wiring), 避難所 (evacuation shelter)

**Nouns - Weather & Nature** (~10 words):
- 寒暖差 (temperature difference), 紫外線 (UV rays), 日射 (solar radiation), 濃霧 (dense fog), 朝靄 (morning mist), 氷点下 (below freezing), 暴風雨 (storm), 落雷 (lightning strike)

**Nouns - Abstract & Business** (~10 words):
- 添付 (attachment), 進捗 (progress), 黒酢 (black vinegar), 物資 (supplies), 備蓄 (stockpile), 配給 (distribution), 救援 (relief), 復興 (reconstruction)

**Other vocabulary** (~5 words):
- ものぐさ (lazy), かわいげ (lovability), うとい (unfamiliar), あさましい (despicable), ちっぽけ (tiny)

Notable features:
- Strong coverage of expressive verbs describing emotions, body language, and sounds
- Comprehensive adjective vocabulary for describing personalities and situations
- Weather and natural phenomenon vocabulary
- Practical facility and infrastructure terms
- Emergency/disaster-related vocabulary: 避難所, 物資, 備蓄, 救援, 復興

Candidate count: 547 → 651

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 128)
Added 30 new dictionary entries from candidate_words.json, covering practical everyday vocabulary, cultural/hobby terms, transportation, and business expressions:

- **Keigo/honorific** (1): お{越|こ}し (coming - honorific)
- **Social/group** (1): {仲間入|なかまい}り (joining a group)
- **Reading/communication** (1): {行間|ぎょうかん} (line spacing; between the lines)
- **Hobbies/entertainment** (7): パチンコ (pachinko), {同人誌|どうじんし} (doujinshi), コレクション (collection), プラモデル (plastic model), ゲーセン (game center), {天体観測|てんたいかんそく} (astronomical observation), {利|き}き{酒|ざけ} (sake tasting)
- **Outdoor/sports** (2): {釣|つ}り{竿|ざお} (fishing rod), {登山靴|とざんぐつ} (hiking boots)
- **Car parts** (2): バックミラー (rearview mirror), ワイパー (windshield wiper)
- **Household** (2): {排水溝|はいすいこう} (drain), {靴棚|くつだな} (shoe rack)
- **Adverbs** (3): ともあれ (anyway), ひょっと (possibly), {明|あき}らかに (clearly)
- **Occupations** (1): {運転士|うんてんし} (train driver)
- **Medical** (1): {切|き}り{傷|きず} (cut wound)
- **Technology** (2): リンク (link/URL), スキャン (scan)
- **Business/shipping** (4): {払戻|はらいもど}し (refund), {返送|へんそう} (return shipping), {送付|そうふ} (sending), {取消|とりけし} (cancellation)
- **Crafts/games** (3): {型紙|かたがみ} (pattern/template), {双六|すごろく} (sugoroku), ラジコン (radio-controlled)

Notable entry features:
- Japanese cultural vocabulary: パチンコ with gambling context, {同人誌|どうじんし} with otaku culture notes, {双六|すごろく} as traditional New Year game
- Hobby vocabulary group: コレクション, プラモデル, ゲーセン, {天体観測|てんたいかんそく}, ラジコン
- Business correspondence: {送付|そうふ}/{返送|へんそう} contrast pair, {払戻|はらいもど}し, {取消|とりけし}
- Practical everyday vocabulary: car parts, household items, medical terms
- Adverbs with common patterns: ともあれ, ひょっと (with ひょっとしたら/ひょっとして)

Total entries: 7,239 → 7,269
Remaining candidates: ~577 → ~547

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 127)
Added 30 new dictionary entries from candidate_words.json, focusing on personality traits, social relationships, consideration/care vocabulary, and useful adjectives:

- **Friendliness/charm** (3): {愛想|あいそう} (amiability), {愛嬌|あいきょう} (charm), {無愛想|ぶあいそう} (unfriendly)
- **Care/consideration** (4): {気遣|きづか}い (concern), {心遣|こころづか}い (thoughtfulness), {心配|こころくば}り (attentive care), {目配|めくば}り (watchfulness)
- **Skill vocabulary** (3): {腕前|うでまえ} (skill), {凄腕|すごうで} (expert), {敏腕|びんわん} (capable)
- **Age/status** (2): {年上|としうえ} (older), {年下|としした} (younger)
- **Familiarity** (3): {馴染|なじ}み (familiarity), {顔馴染|かおなじ}み (familiar face), {初対面|しょたいめん} (first meeting)
- **Attitude/behavior** (4): {強|つよ}がり (bravado), {負|ま}け{惜|お}しみ (sour grapes), お{節介|せっかい} (meddlesome), {気|き}まぐれ (capricious)
- **Abstract nouns** (3): {無駄遣|むだづか}い (waste), {成|な}り{行|ゆ}き (course of events), {先入観|せんにゅうかん} (preconception)
- **I-adjectives** (5): {奥深|おくぶか}い (profound), {生|なま}ぬるい (lukewarm), {潔|いさぎよ}い (graceful in defeat), {程|ほど}よい (moderate), {差|さ}し{出|で}がましい (presumptuous)
- **Na-adjectives** (2): {理不尽|りふじん} (unreasonable), {横柄|おうへい} (arrogant)
- **Expression** (1): やむを{得|え}ない (unavoidable)

Notable entry features:
- Complete care/consideration vocabulary group with cross-references: {気遣|きづか}い, {心遣|こころづか}い, {心配|こころくば}り, {目配|めくば}り
- Skill words: {腕前|うでまえ} → {凄腕|すごうで} → {敏腕|びんわん} with nuance distinctions
- Friendliness/unfriendliness: {愛想|あいそう}/{愛嬌|あいきょう}/{無愛想|ぶあいそう} as antonym pairs
- Useful adjectives for describing personalities and situations
- Expressions for social situations: {初対面|しょたいめん}, お{節介|せっかい}, {差|さ}し{出|で}がましい

Total entries: 7,209 → 7,239
Remaining candidates: ~607 → ~577

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 126)
Added 30 new dictionary entries from candidate_words.json, focusing on compound verbs, comfort/worth expressions, physical sensations, and useful vocabulary:

- **Compound verbs** (6): {繰|く}り{下|さ}げる (to postpone), {沸|わ}き{上|あ}がる (to well up), {突|つ}き{当|あ}たる (to run into), {差|さ}し{伸|の}べる (to extend), {突|つ}き{進|すす}む (to push forward), {切|き}り{下|さ}げる (to cut down)
- **～{心地|ごこち} comfort words** (4): {乗|の}り{心地|ごこち} (ride comfort), {着心地|きごこち} (wearing comfort), {寝心地|ねごこち} (sleeping comfort), {使|つか}い{心地|ごこち} (ease of use)
- **～{応|ごた}え worth expressions** (4): {歯応|はごた}え (chewiness), {読|よ}み{応|ごた}え (worth reading), {見応|みごた}え (worth seeing), {聞|き}き{応|ごた}え (worth listening)
- **Physical sensations** (5): {痺|しび}れ (numbness), むくみ (swelling), かゆみ (itchiness), {凝|こ}り (stiffness), {持病|じびょう} (chronic illness)
- **Everyday vocabulary** (4): {口癖|くちぐせ} (verbal habit), {励|はげ}み (encouragement), {張|は}り{合|あ}い (motivation), {日頃|ひごろ} (usually)
- **Abstract/business** (3): {裁量|さいりょう} (discretion), {目処|めど} (prospect), {大筋|おおすじ} (outline)
- **Yojijukugo** (3): {日常茶飯事|にちじょうさはんじ} (everyday occurrence), {紆余曲折|うよきょくせつ} (twists and turns), {自己満足|じこまんぞく} (self-satisfaction)
- **Noun** (1): {虚栄心|きょえいしん} (vanity)

Notable entry features:
- Complete ～{心地|ごこち} pattern: 4 related words showing how this suffix creates comfort expressions
- Complete ～{応|ごた}え pattern: 4 expressions describing worth/satisfaction across different senses
- Physical sensation vocabulary: common body-related words for describing discomfort
- Compound verbs with {繰|く}り～, {突|つ}き～, {切|き}り～ patterns
- Three yojijukugo with character breakdown and usage notes

Total entries: 7,179 → 7,209
Remaining candidates: ~637 → ~607

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 125)
Added 30 new dictionary entries from candidate_words.json, covering adverbs, adjectives, compound verbs, and practical vocabulary:

- **Adverbs** (5): {互|たが}いに (mutually), {意外|いがい}と (unexpectedly), {思|おも}いがけず (unexpectedly), {仕方|しかた}なく (reluctantly), {思|おも}い{切|き}って (resolutely)
- **Na-adjectives** (5): {巧|たく}み (skillful), {気|き}さく (friendly), {気楽|きらく} (carefree), {些細|ささい} (trivial), {手軽|てがる} (easy)
- **I-adjectives** (3): {気持|きも}ち{悪|わる}い (creepy), {我慢強|がまんづよ}い (patient), {粘|ねば}り{強|づよ}い (tenacious)
- **Nouns** (10): {打|う}ち{合|あ}わせ (meeting), {調理|ちょうり} (cooking), レシピ (recipe), {落|お}ち{着|つ}き (composure), プレッシャー (pressure), {諦|あきら}め (resignation), {決意|けつい} (determination), {仕組|しく}み (mechanism), {手遅|ておく}れ (too late), {手入|てい}れ (maintenance)
- **Compound verbs** (7): {見渡|みわた}す (to survey), {見届|みとど}ける (to see through), {見極|みきわ}める (to discern), {思|おも}い{知|し}る (to learn from experience), {思|おも}い{直|なお}す (to reconsider), {手間取|てまど}る (to take time), {使|つか}いこなす (to master)

Notable entry features:
- Strong adverb coverage: manner expressions ({互|たが}いに, {仕方|しかた}なく) and unexpectedness ({意外|いがい}と, {思|おも}いがけず)
- Personality/character adjectives: {気|き}さく, {気楽|きらく}, {我慢強|がまんづよ}い, {粘|ねば}り{強|づよ}い with nuance distinctions
- {見|み}る compound verbs: {見渡|みわた}す, {見届|みとど}ける, {見極|みきわ}める showing visual perception patterns
- {思|おも}う compound verbs: {思|おも}い{切|き}って, {思|おも}い{知|し}る, {思|おも}い{直|なお}す showing mental processes
- {手|て} compounds: {手遅|ておく}れ, {手入|てい}れ, {手軽|てがる}, {手間取|てまど}る with practical meanings
- Business/work vocabulary: {打|う}ち{合|あ}わせ, プレッシャー, {調理|ちょうり}, レシピ

Total entries: 7,149 → 7,179
Remaining candidates: ~667 → ~637

---

**Archive Note**: Only the 10 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

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

**Note**: Keep only the 10 most recent change entries. When adding a new entry, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
