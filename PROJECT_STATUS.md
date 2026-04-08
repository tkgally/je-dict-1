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

### 2026-04-08 (Vocabulary Expansion - 30 New Entries, Session 45)
Added 30 new dictionary entries (IDs 23018-23047) from candidate_words.json. A diverse mix of nouns, expressions, and cultural terms covering language, safety, culture, society, science, sports, food, philosophy, and daily life.

- **Nouns (22)**: {含蓄|がんちく} (implication/depth), {刀剣|とうけん} (swords), {過疎地|かそち} (depopulated area), {同胞|どうほう} (compatriots), {月報|げっぽう} (monthly report), {浮力|ふりょく} (buoyancy), {場外|じょうがい} (outside the venue), {邸|てい} (mansion), {御朱印帳|ごしゅいんちょう} (stamp book), {失|う}せ{物|もの} (lost article), {統治者|とうちしゃ} (ruler), ひねくれ{者|もの} (contrarian), {消毒薬|しょうどくやく} (disinfectant), {工賃|こうちん} (labor cost), {予想違|よそうちが}い (wrong prediction), レモン{汁|じる} (lemon juice), {上段|じょうだん} (upper level), {鑑定書|かんていしょ} (appraisal certificate), {仁|じん} (benevolence), {拾得物|しゅうとくぶつ} (found property), {飲|の}み{屋街|やがい} (bar district), {藍染|あいぞ}め (indigo dyeing)
- **Noun/suru verbs (6)**: {防護|ぼうご} (protection), {卒倒|そっとう} (fainting), {残存|ざんぞん} (remaining), {固着|こちゃく} (fixation), {代走|だいそう} (pinch runner), {長期滞在|ちょうきたいざい} (long-term stay)
- **Adverb (1)**: {年毎|としごと} (year by year)
- **Expression (1)**: {口先|くちさき}だけ (all talk)
- Added 1 new kanji to index: 仁 (benevolence)

### 2026-04-08 (Vocabulary Expansion - 29 New Entries, Session 44)
Added 29 new dictionary entries (IDs 22988-23017) from candidate_words.json. A practical mix of suru verbs, expressions, and nouns covering daily life, communication, nature, commerce, culture, and more.

- **Noun/suru verbs (10)**: {信頼|しんらい}する (to trust), {予約|よやく}する (to reserve), {終了|しゅうりょう}する (to end), {練習|れんしゅう}する (to practice), {行|い}き{来|き}する (to come and go), {深読|ふかよ}みする (to overinterpret), {建造|けんぞう} (construction), {直送|ちょくそう}する (to ship directly), {辞去|じきょ}する (to take one's leave), {整然|せいぜん}とする (to be orderly)
- **Suru verbs (onomatopoeia) (2)**: からっとする (dry and refreshing), カチンとする (to get irritated), そっとする (to leave alone)
- **Expressions (2)**: {都合|つごう}が{悪|わる}い (inconvenient), {都合|つごう}がいい (convenient)
- **Nouns (12)**: {戦線|せんせん} (front line), {乙|おつ} (second rank/nice), {峰|みね} (peak), {札|ふだ} (tag/card), {筋立|すじた}て (plot/storyline), ビリ (last place), {羅針盤|らしんばん} (compass), {敵陣|てきじん} (enemy camp), {語義|ごぎ} (word meaning), {折|お}れ{線|せん} (broken line), アトピー (atopy), {下弦|かげん} (last quarter moon), {月齢|げつれい} (moon age), {徳|とく} (virtue), {壇|だん} (platform)
- Removed 1 stale candidate (格式高い — duplicate of 21042)








