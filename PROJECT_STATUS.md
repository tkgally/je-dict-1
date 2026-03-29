# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-29
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

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 541)
Added 30 new dictionary entries (IDs 20583-20612) from candidate_words.json. A diverse mix of practical vocabulary including verbs, nouns, adjectives, and adverbs for intermediate learners.

- **Verbs (2)**: {儲|もう}ける (to make a profit), のぼせる (to feel flushed/to be infatuated)
- **Na-adjectives (2)**: {非公式|ひこうしき} (informal/unofficial), {怪奇|かいき} (mysterious/eerie)
- **Adverb (1)**: あたふた (in a fluster/hurriedly)
- **Nouns (25)**: {綱渡|つなわた}り (tightrope walking), {農場|のうじょう} (farm), {真冬|まふゆ} (midwinter), {民意|みんい} (public will), {俗語|ぞくご} (slang), {上陸|じょうりく} (landing), {牽制|けんせい} (check/restraint), {企画書|きかくしょ} (proposal), {入眠|にゅうみん} (falling asleep), {師範|しはん} (master instructor), {口外|こうがい} (disclosing), {平衡|へいこう} (equilibrium), {先達|せんだつ} (pioneer), {土木|どぼく} (civil engineering), {大慌|おおあわ}て (great panic), {含|ふく}み{笑|わら}い (smothered laugh), {画風|がふう} (artistic style), {元金|がんきん} (principal), {表舞台|おもてぶたい} (public spotlight), {放牧|ほうぼく} (grazing), {奇人|きじん} (eccentric), {言語化|げんごか} (verbalization), {背面|はいめん} (back side), {後発|こうはつ} (latecomer), {降車|こうしゃ} (getting off vehicle)
- Added 1 new kanji to index: 儲
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 540)
Added 30 new dictionary entries (IDs 20553-20582) from candidate_words.json. A diverse mix of practical vocabulary covering adjectives, adverbs, verbs, and nouns for intermediate learners.

- **Na-adjectives (5)**: {悪質|あくしつ} (malicious/poor quality), むやみ (reckless/excessive), {風変|ふうが}わり (eccentric), {移|うつ}り{気|ぎ} (fickle), ぶかぶか (baggy/too loose)
- **Adverbs (3)**: たった{今|いま} (just now), いっそのこと (might as well), もうそろそろ (pretty soon)
- **Suru-verbs (2)**: {緊張|きんちょう}する (to get nervous), {降伏|こうふく}する (to surrender)
- **Nouns (20)**: {検疫|けんえき} (quarantine), {富豪|ふごう} (wealthy person), {民話|みんわ} (folk tale), {家計簿|かけいぼ} (household budget book), {閣僚|かくりょう} (cabinet minister), {細部|さいぶ} (details), {原文|げんぶん} (original text), {冒険家|ぼうけんか} (adventurer), {刑罰|けいばつ} (criminal punishment), {文具|ぶんぐ} (stationery), {座右|ざゆう}の{銘|めい} (personal motto), {世代|せだい}{交代|こうたい} (generational change), {寓話|ぐうわ} (fable), {重心|じゅうしん} (center of gravity), {釣|つ}り{合|あ}い (balance), {眼前|がんぜん} (before one's eyes), {原動力|げんどうりょく} (driving force), {注意書|ちゅういが}き (cautionary note), {致死量|ちしりょう} (lethal dose), けなげさ (admirable courage)
- Added 1 new kanji to index: 寓
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 538)
Added 30 new dictionary entries (IDs 20493-20522) from candidate_words.json. A diverse mix of practical vocabulary including mimetic adverbs, everyday nouns, cultural terms, and formal expressions.

- **Adverbs (5)**: もりもり (heartily/vigorously), どっさり (in heaps), がっぽり (raking it in), みっちり (thoroughly/tightly packed), {目下|もっか} (at present)
- **Nouns (25)**: {上質|じょうしつ} (high quality), {栄光|えいこう} (glory), {漁業|ぎょぎょう} (fishing industry), {切断|せつだん} (cutting/severing), {量販店|りょうはんてん} (mass retailer), {品行|ひんこう} (conduct), {岩石|がんせき} (rock), {入札|にゅうさつ} (bidding), {頓珍漢|とんちんかん} (nonsensical), {大理石|だいりせき} (marble), {付|つ}け{焼|や}き{刃|ば} (superficial knowledge), {多発|たはつ} (frequent occurrence), {招待券|しょうたいけん} (invitation ticket), {横長|よこなが} (landscape-oriented), {旧知|きゅうち} (old acquaintance), {清純|せいじゅん} (pure/innocent), {蛍光|けいこう} (fluorescence), {準急|じゅんきゅう} (semi-express), {万物|ばんぶつ} (all things), {数日|すうじつ} (several days), {位置|いち}づけ (positioning), {残響|ざんきょう} (reverberation), {弾劾|だんがい} (impeachment), {上水|じょうすい} (water supply), {歌人|かじん} (waka poet)
- Added 1 new kanji to index: 劾
- Removed 1 stale duplicate candidate (却下)
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 537)
Added 30 new dictionary entries (IDs 20463-20492) from candidate_words.json. A diverse mix of everyday vocabulary, cultural terms, and practical words for intermediate learners.

- **Na-adjective (1)**: {不活発|ふかっぱつ} (inactive/sluggish)
- **Suru-verbs (2)**: {洗髪|せんぱつ} (hair washing), {盗撮|とうさつ} (secret photography)
- **Nouns (27)**: {夜型|よるがた} (night owl), {甘|あま}い{物|もの} (sweets), {名刺交換|めいしこうかん} (exchanging business cards), {置時計|おきどけい} (desk clock), {神社仏閣|じんじゃぶっかく} (shrines and temples), {封建制|ほうけんせい} (feudalism), {副会長|ふくかいちょう} (vice-chairperson), {司会者|しかいしゃ} (emcee), {住所録|じゅうしょろく} (address book), {通用口|つうようぐち} (service entrance), {健康状態|けんこうじょうたい} (health condition), {滞在期間|たいざいきかん} (period of stay), リンス (conditioner), {二十代|にじゅうだい} (one's twenties), {寄宿舎|きしゅくしゃ} (dormitory), {目的語|もくてきご} (object in grammar), {異種|いしゅ} (different kind), {廃品|はいひん} (waste/scrap), {押|お}しボタン (push button), {荷物置|にもつお}き (luggage storage), {拡張現実|かくちょうげんじつ} (augmented reality), {地吹雪|じふぶき} (ground blizzard), {心筋梗塞|しんきんこうそく} (heart attack), {群青色|ぐんじょういろ} (ultramarine), {空言|そらごと} (empty words), {突然死|とつぜんし} (sudden death), {神職|しんしょく} (Shinto priest)
- Added 1 new kanji to index: 梗
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 536)
Added 30 new dictionary entries (IDs 20433-20462) from candidate_words.json. A mix of idioms, expressions, practical nouns, and adverbs for intermediate learners.

- **Expressions (8)**: さじを{投|な}げる (to give up), {満面|まんめん}の{笑|え}み (beaming smile), {似|に}たり{寄|よ}ったり (much the same), {胸|むね}が{熱|あつ}くなる (to be deeply moved), {恩|おん}を{仇|あだ}で{返|かえ}す (to repay kindness with evil), {継続|けいぞく}は{力|ちから}なり (persistence pays off)
- **Adverbs (2)**: ともすれば (apt to/tending to), {何度|なんど}も (many times)
- **Nouns (20)**: {紙一重|かみひとえ} (paper-thin difference), {自己責任|じこせきにん} (self-responsibility), {予告編|よこくへん} (trailer/preview), {候補者|こうほしゃ} (candidate), {応募者|おうぼしゃ} (applicant), {責任感|せきにんかん} (sense of responsibility), ひねり (twist/ingenuity), {窓辺|まどべ} (by the window), {冷|ひ}え{込|こ}み (cold snap), {好景気|こうけいき} (economic boom), {自主性|じしゅせい} (independence/initiative), {柑橘|かんきつ} (citrus), {直営店|ちょくえいてん} (company-operated store), {発疹|はっしん} (rash), {分別|ふんべつ} (discretion), {経済成長|けいざいせいちょう} (economic growth), {遠隔操作|えんかくそうさ} (remote operation), {調理法|ちょうりほう} (cooking method), {薄毛|うすげ} (thinning hair), {新参|しんざん} (newcomer), {記入漏|きにゅうも}れ (omission in form), {自己負担|じこふたん} (out-of-pocket expense)
- Removed 30 candidates that now exist as entries




---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
