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

### 2026-04-01 (Vocabulary Expansion - 30 New Entries, Session 563)
Added 30 new dictionary entries (IDs 21254-21283) from candidate_words.json. A diverse mix of practical vocabulary covering daily life, weather, society, medicine, education, culture, and emotions.

- **Nouns (12)**: {洗顔|せんがん} (face washing), {交通事故|こうつうじこ} (traffic accident), {交通機関|こうつうきかん} (transportation system), {猛吹雪|もうふぶき} (heavy blizzard), {樹氷|じゅひょう} (rime ice), {革製品|かわせいひん} (leather goods), {記入欄|きにゅうらん} (entry field), {和装|わそう} (Japanese dress), {軍服|ぐんぷく} (military uniform), {唱歌|しょうか} (school song), {情報公開|じょうほうこうかい} (information disclosure), {近況報告|きんきょうほうこく} (status update)
- **Suru verbs (6)**: {無断欠席|むだんけっせき} (unexcused absence), {複雑化|ふくざつか} (complication), {高度化|こうどか} (advancement), {縫合|ほうごう} (suturing), {抜歯|ばっし} (tooth extraction), {過剰摂取|かじょうせっしゅ} (excessive intake), {因数分解|いんすうぶんかい} (factorization)
- **Na-adjectives (3)**: {本質的|ほんしつてき} (essential), {平然|へいぜん} (nonchalant), {決然|けつぜん} (resolute)
- **Adverbs (2)**: {毅然|きぜん}と (firmly), {率直|そっちょく}に (frankly)
- **Expressions (4)**: {責任|せきにん}を{果|は}たす (to fulfill responsibility), {身|み}をすくめる (to shrink back), {顔|かお}をほころばせる (to beam), {場|ば}をわきまえる (to read the room)
- **Other (1)**: {両目|りょうめ} (both eyes), {視界不良|しかいふりょう} (poor visibility)

### 2026-04-01 (Vocabulary Expansion - 27 New Entries, Session 562)
Added 27 new dictionary entries (IDs 21227-21253) from candidate_words.json. A diverse mix of practical vocabulary covering transportation, culture, society, weather, and abstract concepts.

- **Nouns (12)**: {難局|なんきょく} (crisis), {備忘録|びぼうろく} (memorandum), {座椅子|ざいす} (floor chair), {入|い}れ{替|か}え (replacement), {体育祭|たいいくさい} (sports festival), {海賊版|かいぞくばん} (pirated edition), {十二分|じゅうにぶん} (more than enough), {生存者|せいぞんしゃ} (survivor), {中型|ちゅうがた} (medium-sized), {勲章|くんしょう} (medal), {北風|きたかぜ} (north wind), {寒風|かんぷう} (cold wind)
- **Suru verbs (5)**: {乗|の}り{降|お}り (boarding/alighting), {乱闘|らんとう} (brawl), {失火|しっか} (accidental fire), {退却|たいきゃく} (retreat), {憂慮|ゆうりょ} (concern)
- **Na-adjectives (4)**: {自明|じめい} (self-evident), {強大|きょうだい} (powerful), {大|おお}きめ (rather large), {機能的|きのうてき} (functional)
- **Other (6)**: {極楽|ごくらく} (paradise), {所用|しょよう} (business/errand), {市民権|しみんけん} (citizenship), {打|う}つ{手|て}がない (no recourse), いちゃもん (complaint), {詭弁|きべん} (sophistry)
- Added 2 new kanji to index: 勲, 詭
- Removed 3 stale candidates (duplicate readings of existing entries)




---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
