# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-31
**Current phase**: Phase 6 - Continued Expansion & Polish

**Live site**: https://www.tkgje.jp/

> **Full history**: Older change logs are archived in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
> **Quick reference**: See [PROJECT_CONTEXT_BRIEF.md](PROJECT_CONTEXT_BRIEF.md) for a concise session-start overview.
> **Project setup**: See [CLAUDE.md](CLAUDE.md) for commands, file placement, and skills.

## Current State

**Phase 6: Continued Expansion & Polish** — Adding vocabulary while maintaining v2 quality standards, with an automated pipeline for batch maintenance tasks. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Content Status

These counts are approximate. Run `make report` for accurate, up-to-date numbers.

| Metric | Value |
|--------|-------|
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
| Audio files | 1,028 |

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

## Recent Changes

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 568)
Added 30 new dictionary entries (IDs 21391-21420) from candidate_words.json. A diverse mix of practical vocabulary covering verbs, expressions, nouns, and adjectives useful for intermediate learners.

- **Suru verbs (5)**: {加速|かそく}する (to accelerate), {下車|げしゃ}する (to alight), {反省|はんせい}する (to reflect/feel remorse), {組織化|そしきか} (systematization), {充足|じゅうそく} (sufficiency)
- **Godan verbs (2)**: {込|こ}み{合|あ}う (to be crowded), {連|つ}れ{去|さ}る (to take away forcibly)
- **Expressions (4)**: {声|こえ}を{出|だ}す (to speak up), {手|て}をつく (to place hands on ground), {息|いき}を{止|と}める (to hold one's breath), {申|もう}し{訳|わけ}ありません (I'm very sorry)
- **Nouns (13)**: {朝方|あさがた} (early morning), {引|ひ}っ{張|ぱ}りだこ (in great demand), {辛|から}さ (spiciness), {数十|すうじゅう} (several tens), {自家用|じかよう} (private use), {新学年|しんがくねん} (new school year), モラル (morals), {東南|とうなん} (southeast), {孤立感|こりつかん} (feeling of isolation), {大盤振|おおばんぶ}る{舞|ま}い (lavish spending), お{得意様|とくいさま} (valued customer), {度量|どりょう} (magnanimity), {解析力|かいせきりょく} (analytical ability)
- **Counter/noun (1)**: {一着|いっちゃく} (first place/one suit)
- **Na-adjective (1)**: {不自然|ふしぜん}な (unnatural)
- **Other nouns (4)**: {零点|れいてん} (zero points), {混合物|こんごうぶつ} (mixture), {拘留|こうりゅう} (detention), {感覚神経|かんかくしんけい} (sensory nerve)

### 2026-04-02 (Vocabulary Expansion - 17 New Entries, Session 567)
Added 17 new dictionary entries (IDs 21374-21390) from candidate_words.json. Focused on practical verbs and expressions useful for intermediate learners.

- **Suru verbs (10)**: {加速|かそく} (to accelerate), {公表|こうひょう} (to announce publicly), {依頼|いらい} (to request), {対面|たいめん} (to meet face-to-face), {白状|はくじょう} (to confess), {仲介|ちゅうかい} (to mediate), {流入|りゅうにゅう} (to flow in), {追及|ついきゅう} (to press for answers), {詰問|きつもん} (to interrogate), {出力|しゅつりょく} (to output), {習熟|しゅうじゅく} (to become proficient), {注文|ちゅうもん} (to order)
- **Godan verbs (3)**: {沸|わ}き{立|た}つ (to boil up/surge), {連|つ}れ{込|こ}む (to bring someone in), {誘|さそ}い{出|だ}す (to lure out)
- **Ichidan verb (1)**: {見下|みさ}げる (to look down on)
- **Expression (1)**: {後|あと}を{追|お}う (to follow after)
- Removed 1 stale candidate (軽視する — already existed as entry 18776)
- Removed 5 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 29 New Entries, Session 566)
Added 29 new dictionary entries (IDs 21344-21373) from candidate_words.json. A thematic mix spanning nature/weather, food/cooking, wedding vocabulary, and abstract concepts.

- **Nature/weather nouns (5)**: {極寒|ごっかん} (extreme cold), {朝霧|あさぎり} (morning fog), {夕靄|ゆうもや} (evening haze), {冷気|れいき} (cold air), さざなみ (ripples)
- **Food/cooking nouns (6)**: {甘露煮|かんろに} (candied/simmered in sweet syrup), {味噌煮|みそに} (simmered in miso), {丸焼|まるや}き (whole roast), {細巻|ほそま}き (thin sushi roll), {出汁巻|だしま}き (dashi omelette), {固|かた}ゆで (hard-boiled)
- **Na-adjectives (3)**: {清涼|せいりょう} (cool and refreshing), {急峻|きゅうしゅん} (steep/precipitous), {無骨|ぶこつ} (rough/unsophisticated)
- **Suru verbs (2)**: {貫通|かんつう} (penetration), {熟知|じゅくち} (thorough knowledge)
- **Godan verb (1)**: {嫉|そね}む (to envy/begrudge)
- **Cultural/other nouns (6)**: {甘|あま}さ (sweetness/leniency), {花婿|はなむこ} (groom), {婚礼|こんれい} (wedding ceremony), {和尚|おしょう} (Buddhist priest), {甘露|かんろ} (sweet dew/nectar), {勉強部屋|べんきょうべや} (study room)
- **Other (6)**: ガチンコ (for real/serious fight), {手際|てぎわ}よく (skillfully), {九死一生|きゅうしいっしょう} (narrow escape from death), {節食|せっしょく} (dietary restraint), {挽|ひ}きたて (freshly ground)
- Added 1 new kanji to index: 峻
- Removed 1 duplicate candidate (凝視する — 凝視 already existed)
- Removed 29 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 565)
Added 30 new dictionary entries (IDs 21314-21343) from candidate_words.json. A practical mix of common verbs, adjectives, nouns, and expressions useful for intermediate learners.

- **Suru verbs (12)**: {駆除|くじょ} (extermination), {分解|ぶんかい} (disassembly/decomposition), {撤去|てっきょ} (removal), {返金|へんきん} (refund), {返却|へんきゃく} (returning), {解消|かいしょう} (resolution), {停車|ていしゃ} (stopping), {回復|かいふく} (recovery), {拒否|きょひ} (refusal), {容認|ようにん} (tolerance), {離婚|りこん} (divorce), {湯煎|ゆせん} (water bath)
- **Na-adjectives (4)**: {謙虚|けんきょ} (humble), {控|ひか}えめ (reserved), {高圧的|こうあつてき} (overbearing), {威圧的|いあつてき} (intimidating)
- **Nouns (9)**: {表現力|ひょうげんりょく} (expressive ability), {未使用|みしよう} (unused), {断面|だんめん} (cross-section), {登山者|とざんしゃ} (mountaineer), {王座|おうざ} (throne), {愚|おろ}か{者|もの} (fool), {基本給|きほんきゅう} (base salary), {植|う}え{付|つ}け (planting), {収穫期|しゅうかくき} (harvest season)
- **Godan verb (1)**: {取|と}り{逃|のが}す (to miss catching)
- **Adverb (1)**: {一般的|いっぱんてき}に (generally)
- **Expression (1)**: {構|かま}わない (don't mind)
- **Other nouns (2)**: {作務衣|さむえ} (samue work clothes), {成長期|せいちょうき} (growth period)
- Removed 30 candidates that now exist as entries

### 2026-04-01 (Vocabulary Expansion - 30 New Entries, Session 564)
Added 30 new dictionary entries (IDs 21284-21313) from candidate_words.json. A diverse mix of practical vocabulary covering everyday language, formal expressions, idioms, grammar, and specialized terms.

- **Nouns (8)**: {微風|びふう} (gentle breeze), {称賛|しょうさん} (praise), {戦況|せんきょう} (war situation), {建築物|けんちくぶつ} (building), {猜疑心|さいぎしん} (suspiciousness), {盤面|ばんめん} (board surface), {周期表|しゅうきひょう} (periodic table), {耐用年数|たいようねんすう} (service life)
- **Na-adjectives (3)**: {利己的|りこてき} (selfish), {殺伐|さつばつ} (bleak/hostile), {不熱心|ふねっしん} (unenthusiastic)
- **Verb (1)**: {明|あ}ける (to dawn)
- **Nouns with suru (3)**: {独断専行|どくだんせんこう} (acting alone), {精錬|せいれん} (refining), {修飾語|しゅうしょくご} (modifier)
- **Everyday nouns (3)**: {水道屋|すいどうや} (plumber), {船着|ふなつ}き{場|ば} (boat landing), {乗降口|じょうこうぐち} (boarding entrance), {濃|こ}い{味|あじ} (strong flavor)
- **Expressions (8)**: {一通|ひととお}り (roughly/once through), {一筋縄|ひとすじなわ}ではいかない (not straightforward), {余韻|よいん}に{浸|ひた}る (to bask in the afterglow), {人目|ひとめ}を{忍|しの}ぶ (to avoid being seen), {文句|もんく}を{言|い}う (to complain), {食欲|しょくよく}をそそる (appetizing), {多忙|たぼう}を{極|きわ}める (to be extremely busy), {便宜|べんぎ}を{図|はか}る (to provide accommodation), {配慮|はいりょ}に{欠|か}ける (to lack consideration), {合図|あいず}を{送|おく}る (to give a signal)
- **Other**: {惜別|せきべつ} (reluctant farewell)
- Added 1 new kanji to index: 猜
- Removed 4 stale candidates (duplicates of existing entries)




---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
