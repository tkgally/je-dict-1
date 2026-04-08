# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-04
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

### 2026-04-08 (Vocabulary Expansion - 25 New Entries, Session 50)
Added 25 new dictionary entries (IDs 23168-23192) from candidate_words.json. A diverse mix of nouns, suru verbs, and a godan verb covering daily life, culture, food, language, politics, military, measurement, and more.

- **Nouns (14)**: テクニック (technique), {序論|じょろん} (introduction), {相談者|そうだんしゃ} (person seeking advice), {支配権|しはいけん} (control/dominion), {掴|つか}み{所|どころ} (defining characteristic), {蚊取|かと}り (mosquito repelling), {酒好|さけず}き (sake lover), ミリメートル (millimeter), {来館者|らいかんしゃ} (visitor to a facility), {言|い}い{様|よう} (way of saying), {悪感|あくかん} (ill will), ハマグリ (clam), ライ{麦|むぎ} (rye), {円弧|えんこ} (arc), {主翼|しゅよく} (main wing), {公印|こういん} (official seal), {工匠|こうしょう} (artisan)
- **Noun/suru verbs (4)**: {文書化|ぶんしょか} (documentation), {出撃|しゅつげき} (sortie), {毒殺|どくさつ} (poisoning to death), {敢闘|かんとう} (fighting bravely)
- **Noun/na-adjective (1)**: {酒好|さけず}き (fond of drinking)
- **Godan verb (1)**: {這|は}い{込|こ}む (to crawl into)
- **Noun with two senses (2)**: {門外|もんがい} (outside the gate / outside one's field), {終礼|しゅうれい} (end-of-day meeting)
- **Loanwords (3)**: テクニック, ミリメートル, ハマグリ (katakana standard)

### 2026-04-08 (Vocabulary Expansion - 30 New Entries, Session 49)
Added 30 new dictionary entries (IDs 23138-23167) from candidate_words.json. A mix of nouns, na-adjectives, suru verbs, and a counter covering culture, daily life, politics, law, nature, food, education, and society.

- **Nouns (16)**: {和式|わしき} (Japanese style), {期待外|きたいはず}れ (disappointment), {目|め}つき (look in eyes), {前代|ぜんだい} (previous generation), {営利|えいり} (profit-making), {党派|とうは} (political faction), {山水|さんすい} (landscape), {名画座|めいがざ} (repertory cinema), {手毬|てまり} (temari ball), {院卒|いんそつ} (graduate school grad), {供花|きょうか} (funeral flowers), {排水管|はいすいかん} (drainpipe), {輪番制|りんばんせい} (rotation system), {貸室|かししつ} (rental room), {年忌|ねんき} (memorial anniversary), {幼稚園児|ようちえんじ} (kindergartener)
- **Noun/na-adjective (3)**: {無表情|むひょうじょう} (expressionless), つむじまがり (contrarian), {激高|げきたか} (very expensive)
- **Noun/suru verbs (4)**: {水没|すいぼつ} (submersion), {出所|しゅっしょ} (release from prison), {急加速|きゅうかそく} (rapid acceleration), {駐留|ちゅうりゅう} (stationing)
- **Noun/adjective-no (3)**: {和式|わしき}, {期待外|きたいはず}れ, {水溶性|すいようせい} (water-soluble)
- **Other (2)**: とらわれ (obsession/fixation), すりごま (ground sesame)
- **Counter (1)**: {一冊|いっさつ} (one book)
- **Banking (1)**: {自動振込|じどうふりこみ} (automatic bank transfer)
- **Legal (1)**: {欠格|けっかく} (disqualification)
- **Nature (1)**: {雉|きじ} (pheasant — Japan's national bird)
- Added 2 new kanji to index: 毬 (ball), 雉 (pheasant)

### 2026-04-08 (Vocabulary Expansion - 30 New Entries, Session 48)
Added 30 new dictionary entries (IDs 23108-23137) from candidate_words.json. A diverse mix of nouns, expressions, adjectives, adverbs, and verbs covering society, language, medicine, culture, travel, personality, and daily life.

- **Nouns (12)**: {暴走族|ぼうそうぞく} (motorcycle gang), {連盟|れんめい} (league/federation), {支配者|しはいしゃ} (ruler), {臆病者|おくびょうもの} (coward), {発疹|ほっしん} (rash), {白血球|はっけっきゅう} (white blood cell), {用語集|ようごしゅう} (glossary), {土産物|みやげもの} (souvenir goods), {土産話|みやげばなし} (travel stories), {賓客|ひんきゃく} (honored guest), {加盟店|かめいてん} (member store), {真面目|まじめ}さ (seriousness)
- **Noun/suru verbs (2)**: {脱落|だつらく} (dropout/omission), {待|ま}ち{伏|ぶ}せ (ambush)
- **Na-adjectives (2)**: {不適当|ふてきとう} (inappropriate), {自由奔放|じゆうほんぽう} (free and unrestrained)
- **I-adjective (1)**: {真面目|まじめ}くさい (overly serious)
- **Expressions/verbs (4)**: {口|くち}を{閉|と}ざす (to clam up), {余韻|よいん}が{残|のこ}る (resonance lingers), {記憶|きおく}が{薄|うす}れる (memory fades), {罪|つみ}を{被|かぶ}せる (to frame someone)
- **Adverbs (3)**: {都合|つごう}よく (conveniently), {直前|ちょくぜん}に (immediately before), {適切|てきせつ}に (appropriately)
- **Loanwords (2)**: ホワイトボード (whiteboard), モーター (motor)
- **Verb (1)**: {向上|こうじょう}させる (to improve/enhance)
- **Other noun (1)**: {誤植|ごしょく} (misprint/typo), {前掛|まえか}け (traditional apron), {田園|でんえん} (countryside/pastoral)

### 2026-04-08 (Vocabulary Expansion - 30 New Entries, Session 47)
Added 30 new dictionary entries (IDs 23078-23107) from candidate_words.json. A diverse mix of loanwords, compound nouns, cultural terms, and adjectives covering daily life, food, sports, body, culture, science, weather, and business.

- **Katakana loanwords (13)**: スタミナ (stamina), フレッシュ (fresh), エゴ (ego), キャンディー (candy), ジャーナリズム (journalism), スキンケア (skin care), テナント (tenant), トートバッグ (tote bag), ミネラル (mineral), ボルト (bolt/volt), タンク (tank), ディップ (dip), ピラティス (Pilates)
- **Compound nouns (11)**: {冬服|ふゆふく} (winter clothes), {体長|たいちょう} (body length), {始点|してん} (starting point), {背筋|はいきん} (back muscles), {精肉店|せいにくてん} (butcher shop), {花器|かき} (flower vase), {事務作業|じむさぎょう} (clerical work), {間隙|かんげき} (gap), {沈降|ちんこう} (subsidence), {青紫|あおむらさき} (blue-purple), {天井裏|てんじょううら} (attic space)
- **Cultural/proper nouns (1)**: {甲子園|こうしえん} (Koshien)
- **Na-adjectives (2)**: フレッシュ (fresh/youthful), まめ (diligent/attentive)
- **Four-character compound (1)**: {立身出世|りっしんしゅっせ} (rising in the world)
- **Other nouns (2)**: {更衣|こうい} (changing clothes), いびり (bullying), {風向|ふうこう} (wind direction)

### 2026-04-08 (Vocabulary Expansion - 30 New Entries, Session 46)
Added 30 new dictionary entries (IDs 23048-23077) from candidate_words.json. A diverse mix of nouns, suru verbs, adverbs, and onomatopoeia covering daily life, culture, food, education, legal/business, nature, and people.

- **Nouns (17)**: {合羽|かっぱ} (raincoat), お{香|こう} (incense), {草花|くさばな} (flowers and grasses), {遊|あそ}び{場|ば} (playground), {空|あ}き{缶|かん} (empty can), {細道|ほそみち} (narrow path), {著名人|ちょめいじん} (celebrity), {香気|こうき} (fragrance), {外套|がいとう} (overcoat), {市区町村|しくちょうそん} (municipalities), {災厄|さいやく} (calamity), {合挽|あいび}き (mixed ground meat), {甘酢漬|あまずづ}け (sweet vinegar pickle), {維持費|いじひ} (maintenance cost), {案内係|あんないがかり} (guide), {足裏|あしうら} (sole of the foot), {合意書|ごういしょ} (agreement), {大金持|おおがねも}ち (rich person), ニュータウン (new town)
- **Noun/suru verbs (8)**: {委任|いにん} (delegation), {指南|しなん} (instruction), {相似|そうじ} (similarity), {制圧|せいあつ} (suppression), アニメ{化|か} (anime adaptation), {依拠|いきょ} (reliance), {講読|こうどく} (text study), {小口切|こぐちぎ}り (thin slicing)
- **Adverbs/onomatopoeia (2)**: きょとんと (blankly/puzzledly), あんぐり (gaping wide open)
- **Other (1)**: {悪行|あくぎょう} (evil deed)
- Added 1 new kanji to index: 套 (sheath)









