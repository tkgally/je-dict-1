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

### 2026-03-25 (Vocabulary Expansion - 20 New Entries, Session 497)
Added 20 new dictionary entries (IDs 19279-19298) from candidate_words.json.

- **Nouns (13)**: {天丼|てんどん} (tempura rice bowl), {道順|みちじゅん} (route/directions), {厚紙|あつがみ} (cardboard), {子馬|こうま} (foal), {個数|こすう} (number of items), {専務|せんむ} (executive director), {濁音|だくおん} (voiced sound), {高卒|こうそつ} (high school graduate), {大卒|だいそつ} (university graduate), {無添加|むてんか} (additive-free), {非営利|ひえいり} (non-profit), {直属|ちょくぞく} (direct subordination), {愛護|あいご} (protection/welfare)
- **Suru verbs (4)**: {忘却|ぼうきゃく} (forgetting), {過食|かしょく} (overeating), {放電|ほうでん} (discharge), {想起|そうき} (recollection)
- **Multi-sense entries (3)**: {色気|いろけ} (2: sex appeal / ambition), {書|か}き{出|だ}し (2: opening sentence / data export), {黒星|くろぼし} (2: sports loss / black mark)

Topics covered: food, directions, education, business, animals, health, science, language, sports, society
Total entries: ~19,085 → ~19,105 (approximate)
Remaining candidates: ~5,072 → ~5,052 (20 entries created)

### 2026-03-25 (Vocabulary Expansion - 27 New Entries, Session 496)
Added 27 new dictionary entries (IDs 19249-19278) from candidate_words.json. Three candidates (限定, 拒絶, 抽出) were discovered as duplicates during validation and removed.

- **Nouns (11)**: {売|う}れ{筋|すじ} (best seller), {軽装|けいそう} (light clothing), {日刊|にっかん} (daily publication), {日当|にっとう} (daily allowance), {採寸|さいすん} (taking measurements), {万人|ばんにん}{受|う}け (mass appeal), {居住地|きょじゅうち} (place of residence), {俗説|ぞくせつ} (popular belief), {中編|ちゅうへん} (novella), {商号|しょうごう} (trade name), {最高潮|さいこうちょう} (climax)
- **Verbs/Expressions (9)**: {吹|ふ}っ{切|き}れる (to get over it), {思|おも}い{当|あ}たる (to come to mind), {買|か}い{叩|たた}く (to beat down price), {掛|か}け{違|ちが}える (to button wrongly/misunderstand), {浮|う}き{足|あし}{立|だ}つ (to panic), {振|ふ}り{出|だ}す (to issue), {一目|いちもく}{置|お}く (to acknowledge superiority), {感|かん}{極|きわ}まる (to be overcome with emotion), {板|いた}に{着|つ}く (to suit one well)
- **Adjective/Adverb (4)**: {常識的|じょうしきてき} (sensible), {何気|なにげ}なく (casually), {一端|いっぱし} (full-fledged), {汗|あせ}っかき (heavy sweater)
- **Other (3)**: {昼|ひる}どき (lunchtime), {定石|じょうせき} (standard approach), {平生|へいぜい} (ordinarily)
- **Multi-sense entries**: {限定|げんてい} duplicate removed, {掛|か}け{違|ちが}える (2: literal button/figurative misunderstanding), {中編|ちゅうへん} (2: novella/middle volume), {居住地|きょじゅうち} (2: address/residential area), {振|ふ}り{出|だ}す (2: issue check/shake out), {定石|じょうせき} (2: Go moves/established approach)

Topics covered: shopping, emotion, clothing, media, work, money, food, culture, literature, law, games
Total entries: ~19,058 → ~19,085 (approximate)
Remaining candidates: ~5,099 → ~5,072 (27 entries created)

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


---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
