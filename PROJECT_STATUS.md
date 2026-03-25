# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-25
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-25 (Vocabulary Expansion - 35 New Entries, Session 495)
Added 35 new dictionary entries (IDs 19214-19248) from candidate_words.json.

- **Nouns (21)**: ふりかけ (dry rice seasoning), {国旗|こっき} (national flag), {犯罪者|はんざいしゃ} (criminal), {捜索|そうさく} (search/manhunt), {空軍|くうぐん} (air force), {補助金|ほじょきん} (subsidy), {推敲|すいこう} (polishing writing), {親近感|しんきんかん} (feeling of closeness), {前任者|ぜんにんしゃ} (predecessor), {協賛|きょうさん} (sponsorship), {老眼鏡|ろうがんきょう} (reading glasses), {検温|けんおん} (temperature check), {平地|へいち} (level ground), {不燃物|ふねんぶつ} (non-burnable waste), {展示品|てんじひん} (exhibit), {学芸員|がくげいいん} (curator), {防音室|ぼうおんしつ} (soundproof room), {軽量化|けいりょうか} (weight reduction), {観葉植物|かんようしょくぶつ} (houseplant), {表彰台|ひょうしょうだい} (victory podium), {駅構内|えきこうない} (station premises)
- **Nouns/Expressions (5)**: {根性|こんじょう} (willpower/disposition), {蚊帳|かや}の{外|そと} (being left out), {計算違|けいさんちが}い (miscalculation), {土足厳禁|どそくげんきん} (no shoes allowed), {消息|しょうそく} (whereabouts)
- **Suru verbs (3)**: {掲載|けいさい}する (to publish), {団結|だんけつ}する (to unite), {発行|はっこう}する (to issue)
- **Other nouns (6)**: {餌付|えづ}け (feeding animals), {営業職|えいぎょうしょく} (sales position), {息継|いきつ}ぎ (breathing pause), {写真映|しゃしんば}え (photogenic), {室内干|しつないぼ}し (indoor drying), {食習慣|しょくしゅうかん} (eating habits)
- **Multi-sense entries**: {根性|こんじょう} (2: willpower / temperament), {計算違|けいさんちが}い (2: arithmetic error / misjudgment)
- Removed 1 stale candidate ({終日|しゅうじつ} - already exists as entry 13807)
- Added 1 new kanji to index: 敲 (knock)

Topics covered: food, culture, law, military, finance, health, daily life, media, sports, nature, work
Total entries: ~19,023 → ~19,058 (approximate)
Remaining candidates: ~5,135 → ~5,099 (35 removed as entries + 1 stale candidate removed)

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 494)
Added 35 new dictionary entries (IDs 19179-19213) from candidate_words.json.

- **Nouns/Suru verbs (19)**: {覚醒|かくせい} (awakening), {増量|ぞうりょう} (increase in quantity), {排泄|はいせつ} (excretion), {遮音|しゃおん} (sound insulation), {誤審|ごしん} (misjudgment), {熱唱|ねっしょう} (passionate singing), {例証|れいしょう} (exemplification), {休耕|きゅうこう} (fallow farmland), {地盤沈下|じばんちんか} (ground subsidence), {伝道|でんどう} (evangelism), {炭化|たんか} (carbonization), {打鍵|だけん} (keystroke), {私有|しゆう} (private ownership), {吸音|きゅうおん} (sound absorption), {検死|けんし} (autopsy), {執刀|しっとう} (performing surgery), {在任|ざいにん} (tenure), {戦勝|せんしょう} (war victory), {行程|こうてい} (journey/process)
- **Nouns (11)**: {極致|きょくち} (pinnacle), {駐在所|ちゅうざいしょ} (police substation), {液状|えきじょう} (liquid state), {公職|こうしょく} (public office), {荷重|かじゅう} (load/weight), {行書|ぎょうしょ} (semi-cursive script), {草書|そうしょ} (cursive script), {情報漏洩|じょうほうろうえい} (data breach), {日本庭園|にほんていえん} (Japanese garden), {戦国時代|せんごくじだい} (Warring States period), {非常階段|ひじょうかいだん} (emergency staircase)
- **Other (5)**: {体外|たいがい} (outside the body), {床|とこ}ずれ (bedsore), {海獣|かいじゅう} (marine mammal), {禁錮|きんこ} (imprisonment), {拙劣|せつれつ} (clumsy/poor)
- **Multi-sense entries**: {覚醒|かくせい} (2: waking up / activation), {行程|こうてい} (2: journey / mechanical stroke), {地盤沈下|じばんちんか} (2: literal / figurative decline)
- Removed 1 stale candidate ({却下|かっか} - wrong reading, correct reading きゃっか already exists)
- Added 2 new kanji to index: 泄 (leak), 錮 (imprison)

Topics covered: medicine, law, acoustics, calligraphy, sports, history, culture, engineering, nature
Total entries: ~18,988 → ~19,023 (approximate)
Remaining candidates: ~5,171 → ~5,135 (35 removed as entries + 1 stale candidate removed)

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 493)
Added 35 new dictionary entries (IDs 19144-19178) from candidate_words.json.

- **Nouns (22)**: {都内|とない} (within Tokyo), {握|にぎ}り{寿司|ずし} (nigiri sushi), {熱帯魚|ねったいぎょ} (tropical fish), お{札|さつ} (banknote), {結納|ゆいのう} (betrothal gifts), {失点|しってん} (points lost), {班長|はんちょう} (group leader), {噴煙|ふんえん} (volcanic smoke), {薬学|やくがく} (pharmacy), {句点|くてん} (period/full stop), {食用油|しょくようゆ} (cooking oil), {交際費|こうさいひ} (entertainment expenses), {加盟国|かめいこく} (member state), {盛夏|せいか} (midsummer), {受取人|うけとりにん} (recipient), {遺骨|いこつ} (remains), {霊園|れいえん} (cemetery), {敷石|しきいし} (paving stone), {常備菜|じょうびさい} (make-ahead side dish), {制汗剤|せいかんざい} (antiperspirant), {砲弾|ほうだん} (shell/cannonball), {植物油|しょくぶつゆ} (vegetable oil)
- **Nouns/Suru verbs (7)**: {入籍|にゅうせき} (marriage registration), {追撃|ついげき} (pursuit), {布陣|ふじん} (formation), {出陣|しゅつじん} (going to battle), {同一視|どういつし} (equating), {脇見|わきみ} (looking away), {首謀者|しゅぼうしゃ} (ringleader)
- **Na-adjectives (2)**: {生理的|せいりてき} (physiological/visceral), {基礎的|きそてき} (fundamental)
- **Nouns (other, 2)**: {事務官|じむかん} (administrative official), {霜害|そうがい} (frost damage)
- **Adverb (1)**: {第一|だいいち}に (firstly)
- **Noun with cultural note (1)**: {動乱|どうらん} (upheaval)
- **Multi-sense entries**: {生理的|せいりてき} (2 senses: physiological / visceral aversion)

Topics covered: geography, food, culture, sports, government, science, daily life, agriculture, military
Total entries: ~18,953 → ~18,988 (approximate)
Remaining candidates: ~5,205 → ~5,171 (35 removed as entries)

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 492)
Added 35 new dictionary entries (IDs 19109-19143) from candidate_words.json.

- **Nouns (17)**: {冷|ひ}や{汗|あせ} (cold sweat), {得票|とくひょう} (votes obtained), {隣国|りんごく} (neighboring country), {開票|かいひょう} (ballot counting), {海抜|かいばつ} (above sea level), {前方|ぜんぽう} (front/forward), {後方|こうほう} (rear/behind), パンフレット (pamphlet), {諸説|しょせつ} (various theories), {夕闇|ゆうやみ} (evening darkness), お{姫様|ひめさま} (princess), {登山道|とざんどう} (mountain trail), {夕凪|ゆうなぎ} (evening calm), {遺書|いしょ} (will/testament), {身|み}の{上話|うえばなし} (life story), {博愛|はくあい} (philanthropy), {大将|たいしょう} (general/boss)
- **Nouns/Suru verbs (5)**: {審議|しんぎ} (deliberation), {放任|ほうにん} (laissez-faire), {急展開|きゅうてんかい} (sudden development), {拘泥|こうでい} (fixation), {甘受|かんじゅ} (acceptance)
- **Nouns/Na-adjectives (5)**: {切|き}れ{味|あじ} (sharpness), {少|すく}なめ (somewhat less), {安上|やすあ}がり (inexpensive), {軽量|けいりょう} (lightweight), {泥|どろ}まみれ (covered in mud)
- **Na-adjective (1)**: {安直|あんちょく} (cheap/simplistic)
- **Adjective-no (1)**: {無農薬|むのうやく} (pesticide-free)
- **I-adjectives (2)**: {途方|とほう}もない (extraordinary), {親|した}しみやすい (approachable)
- **Nouns (seasonal, 2)**: {冬休|ふゆやす}み (winter break), {春休|はるやす}み (spring break)
- **Other (2)**: {行|い}きつけ (regular place), {説法|せっぽう} (sermon/preaching)
- **Multi-sense entries**: {切|き}れ{味|あじ} (2), {安直|あんちょく} (2), {遺書|いしょ} (2), お{姫様|ひめさま} (2), {大将|たいしょう} (2), {途方|とほう}もない (2), {説法|せっぽう} (2)
- Removed 1 stale candidate ({問屋|どんや} - variant reading of existing {問屋|とんや} entry)

Topics covered: politics, nature, geography, food, daily life, culture, emotions, language
Total entries: ~18,918 → ~18,953 (approximate)
Remaining candidates: ~5,241 → ~5,205 (35 removed as entries + 1 stale candidate removed)

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 491)
Added 35 new dictionary entries (IDs 19074-19108) from candidate_words.json.

- **Nouns (15)**: {刑務所|けいむしょ} (prison), {研究所|けんきゅうじょ} (research institute), {上下関係|じょうげかんけい} (hierarchical relationship), {猛毒|もうどく} (deadly poison), {有力者|ゆうりょくしゃ} (influential person), {化石燃料|かせきねんりょう} (fossil fuel), {利|き}き{手|て} (dominant hand), {陸軍|りくぐん} (army), {立|た}ち{退|の}き (eviction), {我|わ}が{身|み} (oneself), {野犬|やけん} (stray dog), {万事|ばんじ} (everything), {塵取|ちりと}り (dustpan), {中級者|ちゅうきゅうしゃ} (intermediate-level person), {上級者|じょうきゅうしゃ} (advanced-level person)
- **Nouns/Suru verbs (5)**: {解凍|かいとう} (thawing/decompression), {保守|ほしゅ} (conservatism/maintenance), お{披露目|ひろめ} (debut/unveiling), {再検討|さいけんとう} (re-examination), {増強|ぞうきょう} (reinforcement)
- **Na-adjectives (3)**: {乱雑|らんざつ}な (messy), {神聖|しんせい}な (sacred), {不道徳|ふどうとく} (immoral)
- **Adverbs (4)**: {段々|だんだん}と (gradually), {急速|きゅうそく}に (rapidly), {遠回|とおまわ}しに (indirectly), {露骨|ろこつ}に (blatantly)
- **Nouns (specialized, 5)**: {遺言|いごん} (will/testament, legal reading), {株式会社|かぶしきがいしゃ} (corporation), {用水路|ようすいろ} (irrigation channel), {熟練工|じゅくれんこう} (skilled worker), ほうじ{茶|ちゃ} (roasted green tea)
- **Nouns (other, 2)**: {無糖|むとう} (sugar-free), {突然変異|とつぜんへんい} (mutation)
- **Verb (1)**: {消|き}え{去|さ}る (to vanish)
- **Multi-sense entries**: {解凍|かいとう} (2: thawing/decompression), {保守|ほしゅ} (2: conservatism/maintenance), {突然変異|とつぜんへんい} (2: genetic mutation/figurative)

Topics covered: law/justice, science, politics, food/drink, daily life, culture, communication, nature, business
Total entries: ~18,883 → ~18,918 (approximate)
Remaining candidates: ~5,276 → ~5,241 (35 removed as entries)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
