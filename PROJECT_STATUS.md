# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-30
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

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 552)
Added 30 new dictionary entries (IDs 20893-20922) from candidate_words.json. A diverse mix of nouns, verbs, adjectives, and adverbs covering daily life, food, culture, finance, geography, technology, and society.

- **Nouns (14)**: {企|くわだ}て (plan/plot), {小銭入|こぜにい}れ (coin purse), {販売店|はんばいてん} (retail store), {油脂|ゆし} (fats and oils), お{茶請|ちゃう}け (tea snack), {陶芸家|とうげいか} (ceramist), {美容整形|びようせいけい} (cosmetic surgery), {北半球|きたはんきゅう} (Northern Hemisphere), {司令官|しれいかん} (commander), {甲殻類|こうかくるい} (crustaceans), {志願者|しがんしゃ} (volunteer/applicant), {輪廻転生|りんねてんしょう} (reincarnation), {不良債権|ふりょうさいけん} (bad debt), {保養地|ほようち} (health resort)
- **Suru verbs (6)**: {読破|どくは}する (to finish reading), {適合|てきごう} (conformity), {省力化|しょうりょくか} (labor-saving), {肩代|かたが}わりする (to take over a burden), {冠水|かんすい} (flooding), {脱臭|だっしゅう} (deodorization)
- **Na-adjectives (4)**: {短|みじか}め (somewhat short), {太|ふと}め (somewhat thick), {細|ほそ}め (somewhat thin), {同情的|どうじょうてき} (sympathetic)
- **Adverb (1)**: {公然|こうぜん} (openly/publicly)
- **Other (5)**: へたれ (wimp), {漫談|まんだん} (comic talk), フォント (font), {甘納豆|あまなっとう} (sweetened beans), {地域|ちいき}おこし (regional revitalization)

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 551)
Added 30 new dictionary entries (IDs 20863-20892) from candidate_words.json. A diverse mix of suru verbs, godan verb, nouns, na-adjectives, and expressions covering language, science, finance, culture, food, medicine, sports, and daily life.

- **Suru verbs (7)**: {連発|れんぱつ} (rapid repetition), {続発|ぞくはつ} (successive occurrence), {透過|とうか} (transmission/permeation), {帰属|きぞく} (belonging/attribution), {隷属|れいぞく} (subordination/servitude), {退色|たいしょく} (fading/discoloration), {注文生産|ちゅうもんせいさん} (made-to-order production — noun only)
- **Godan verb (1)**: {澄|す}み{切|き}る (to be crystal clear)
- **Nouns (14)**: {不成功|ふせいこう} (failure), {限度額|げんどがく} (credit limit), {無応答|むおうとう} (no response), {伝達力|でんたつりょく} (communication ability), {損害保険|そんがいほけん} (non-life insurance), {心理戦|しんりせん} (psychological warfare), {非推奨|ひすいしょう} (deprecated), {輝度|きど} (brightness/luminance), {防錆|ぼうせい} (rust prevention), {撥|ばち} (plectrum/drumstick), {兄貴分|あにきぶん} (big-brother figure), {葉菜|ようさい} (leafy vegetable), {獣医学|じゅういがく} (veterinary medicine), {注文服|ちゅうもんふく} (custom clothing), {副助詞|ふくじょし} (adverbial particle), {紆余|うよ} (winding/meandering)
- **Expressions (2)**: {品|ひん}がある (to have class), {予約困難|よやくこんなん} (hard to book)
- **Other (2)**: {拳闘|けんとう} (boxing), {浄化槽|じょうかそう} (septic tank), {脳神経|のうしんけい} (cranial nerve)
- Added 1 new kanji to index: 隷
- Removed 20 stale duplicate candidates from candidate_words.json

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 550)
Added 30 new dictionary entries (IDs 20833-20862) from candidate_words.json. A mix of verbs, i-adjectives, nouns, an adverb, and an interjection covering everyday actions, emotions, appearance, and literary expression.

- **Godan verbs (15)**: {覆|くつがえ}る (to be overturned), {絡|から}まる (to get tangled), ずらす (to shift), さする (to rub), {貪|むさぼ}る (to devour), {罵|ののし}る (to verbally abuse), {銘打|めいう}つ (to label as), {赤|あか}らむ (to redden), {裏返|うらがえ}る (to turn inside out), {反|そ}らす (to bend back), ねぶる (to lick), {胸躍|むねおど}る (thrilling), {赦|ゆる}す (to pardon), {退|しりぞ}く (to retreat), {採|と}る (to gather)
- **Ichidan verbs (3)**: {心得|こころえ}る (to understand), どける (to move aside), {縮|ちぢ}れる (to be curly), {癒|い}える (to heal)
- **I-adjectives (4)**: ごつい (rugged), {悪賢|わるがしこ}い (cunning), {欲深|よくふか}い (greedy), {篤|あつ}い (sincere)
- **Nouns (4)**: {移|うつ}ろい (change/passing), {色違|いろちが}い (different color), {嘘笑|うそわら}い (fake smile), {入園|にゅうえん} (entering kindergarten), {格下|かくさ}げ (downgrade)
- **Adverb (1)**: ごとく (like, as if)
- **Interjection (1)**: ふむ (hmm, I see)
- Removed 1 stale candidate (癒やす — duplicate of 癒す)

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 549)
Added 30 new dictionary entries (IDs 20803-20832) from candidate_words.json. A diverse mix of nouns, na-adjective, adverbs, expressions, suru verbs, and onomatopoeia covering prophecy, emotions, law, nature, food, culture, sports, and daily life.

- **Na-adjective (1)**: あからさま (blatant/obvious)
- **Adverbs (3)**: きゅうっと (tightly/squeezing), {嫌々|いやいや}ながら (reluctantly), ちょびちょび (little by little)
- **Expressions (2)**: ご{苦労|くろう}さまです (thank you for your work), {罠|わな}にかける (to trap/ensnare)
- **Suru verbs (5)**: {予言|よげん} (prophecy), {発狂|はっきょう} (going mad), {贖罪|しょくざい} (atonement), {調教|ちょうきょう} (training/taming), {是認|ぜにん} (approval), {大|だい}ヒット (big hit)
- **Onomatopoeia (1)**: ごそごそする (to rustle about/rummage)
- **Nouns (17)**: {企|たくら}み (plot/scheme), {給付金|きゅうふきん} (benefit payment), {美点|びてん} (virtue/merit), {樹海|じゅかい} (sea of trees), {議案|ぎあん} (bill/proposal), ホームラン (home run), {相続人|そうぞくにん} (heir), {改正案|かいせいあん} (revision bill), {地震速報|じしんそくほう} (earthquake alert), {献立表|こんだてひょう} (meal plan), みょうが (Japanese ginger), {赤血球|せっけっきゅう} (red blood cell), {原子炉|げんしろ} (nuclear reactor), {和裁|わさい} (Japanese sewing), サーカス (circus), {青|あお}じそ (green shiso), {分煙|ぶんえん} (smoking area separation)
- Added 1 new kanji to index: 贖
- Removed 30 candidates that now exist as entries

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 548)
Added 30 new dictionary entries (IDs 20773-20802) from candidate_words.json. A diverse mix of nouns, na-adjectives, and expressions covering food, culture, language, technology, daily life, weather, law, and emotions.

- **Na-adjective (1)**: {例外的|れいがいてき} (exceptional)
- **Expressions (3)**: {有終|ゆうしゅう}の{美|び} (finishing beautifully), {心|こころ}の{余裕|よゆう} (mental composure), {尻|しり}すぼみ (fizzling out)
- **Four-character idioms (2)**: {一致団結|いっちだんけつ} (unity/solidarity), {威風堂々|いふうどうどう} (majestic/dignified)
- **Nouns (24)**: {推論|すいろん} (inference), {失意|しつい} (dejection), {具体化|ぐたいか} (concretization), {短編小説|たんぺんしょうせつ} (short story), {入浴剤|にゅうよくざい} (bath additive), {常用漢字|じょうようかんじ} (regular-use kanji), {賃貸住宅|ちんたいじゅうたく} (rental housing), {焼|や}きうどん (fried udon), {金|きん}メダル (gold medal), {高速|こうそく}バス (express bus), {先端技術|せんたんぎじゅつ} (cutting-edge technology), {検事|けんじ} (public prosecutor), グレープフルーツ (grapefruit), {粒|つぶ}あん (chunky bean paste), こしあん (smooth bean paste), {科学技術|かがくぎじゅつ} (science and technology), ドライフルーツ (dried fruit), {探知|たんち} (detection), {悲哀|ひあい} (sorrow/grief), {長編小説|ちょうへんしょうせつ} (full-length novel), {特別警報|とくべつけいほう} (special warning), {避難指示|ひなんしじ} (evacuation order), {洋裁|ようさい} (dressmaking), リュックサック (backpack)
- Removed 30 candidates that now exist as entries




---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
