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

### 2026-04-03 (Vocabulary Expansion - 22 New Entries)
Added 22 new dictionary entries (IDs 21735-21756) from candidate_words.json. A practical mix including suru verbs, nouns, a godan verb, and an expression.

- **Suru verbs (9)**: {利用|りよう}する (to use/utilize), {提供|ていきょう}する (to provide), {発送|はっそう}する (to ship), {配送|はいそう}する (to deliver), {適用|てきよう}する (to apply), {落下|らっか}する (to fall), {奪回|だっかい}する (to recapture), {貫通|かんつう}する (to penetrate), {開墾|かいこん}する (to reclaim land)
- **Godan verb (1)**: {行|い}き{止|ど}まる (to come to a dead end)
- **Nouns (11)**: {季節外|きせつはず}れ (out of season), {暖冬|だんとう} (mild winter), {新興国|しんこうこく} (emerging nation), {求職者|きゅうしょくしゃ} (job seeker), {持続性|じぞくせい} (sustainability), {水圧|すいあつ} (water pressure), {水流|すいりゅう} (water current), テレビ{会議|かいぎ} (video conference), {作詞家|さくしか} (lyricist), {経済政策|けいざいせいさく} (economic policy), {防犯対策|ぼうはんたいさく} (crime prevention measures)
- **Expression (1)**: {何|なん}と{言|い}うか (how should I say)
- Removed 22 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 580)
Added 30 new dictionary entries (IDs 21705-21734) from candidate_words.json. A practical mix of vocabulary for intermediate learners including verbs, nouns, adverbs, and food terms.

- **Suru verbs (5)**: {触発|しょくはつ}する (to trigger/inspire), {誘導|ゆうどう}する (to guide/induce), {回想|かいそう}する (to reminisce), {整理|せいり}する (to organize), {改変|かいへん} (alteration)
- **Ichidan verb (1)**: {生|い}き{延|の}びる (to survive)
- **Na-adjectives (2)**: {無敵|むてき} (invincible), {過小|かしょう} (too small)
- **Nouns (16)**: {略語|りゃくご} (abbreviation), {輝|かがや}き (brilliance), {周期|しゅうき} (cycle), {漆黒|しっこく} (jet black), {初春|しょしゅん} (early spring), {料亭|りょうてい} (high-class restaurant), {降雨|こうう} (rainfall), {低気圧|ていきあつ} (low pressure), {文通|ぶんつう} (correspondence), {壇上|だんじょう} (on stage), {並立|へいりつ} (coexistence), {年頭|ねんとう} (start of year), {火照|ほて}り (flushing), {深度|しんど} (depth), {書類選考|しょるいせんこう} (document screening), {音域|おんいき} (vocal range)
- **Adverbs/Other (4)**: たじたじ (flinching), まずまず (fairly), {風雨|ふうう} (wind and rain), {話術|わじゅつ} (speaking skill)
- **Food (1)**: はんぺん (steamed fish cake)
- **Culture (1)**: お{墓|はか} (grave)
- Removed 10 stale duplicate candidates

### 2026-04-02 (Vocabulary Expansion - 28 New Entries, Session 579)
Added 28 new dictionary entries (IDs 21677-21704) from candidate_words.json. A practical mix of commonly used vocabulary for intermediate learners including verbs, adjectives, nouns, and expressions.

- **Suru verbs (10)**: {印刷|いんさつ}する (to print), {解散|かいさん}する (to disband), {集合|しゅうごう}する (to gather), {宣言|せんげん}する (to declare), {上昇|じょうしょう}する (to rise), {貢献|こうけん}する (to contribute), {敗北|はいぼく}する (to be defeated), {強調|きょうちょう}する (to emphasize), ぼんやりする (to be absent-minded), {帯電|たいでん} (electrification)
- **Ichidan verb (1)**: {食|た}べ{過|す}ぎる (to overeat)
- **Na-adjectives (2)**: {頑丈|がんじょう}な (sturdy), スリム (slim)
- **Nouns (12)**: {暖|あたた}かさ (warmth), {純正|じゅんせい} (genuine), {代理店|だいりてん} (agency), {老婆心|ろうばしん} (motherly concern), {超絶|ちょうぜつ} (transcendent), {最後尾|さいこうび} (end of line), {過半|かはん} (majority), {別注|べっちゅう} (special order), {横腹|よこばら} (flank), {岩穴|いわあな} (cave), {打|う}ち{消|け}し (negation), {毒|どく}ガス (poison gas)
- **Other (3)**: お{釜|かま} (pot/rear-end collision), {嘘|うそ}だろ (no way!), {値|あたい} (value)
- Removed 28 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 30 New Entries, Session 578)
Added 30 new dictionary entries (IDs 21647-21676) from candidate_words.json. A diverse mix of practical vocabulary for intermediate learners covering everyday life, sports, culture, medicine, fashion, and more.

- **Ichidan verb (1)**: {突|つ}き{抜|ぬ}ける (to pierce through)
- **Na-adjectives (2)**: {強健|きょうけん} (robust), {不誠実|ふせいじつ} (insincere)
- **Noun/verb-suru (5)**: {休刊|きゅうかん} (suspension of publication), {現実化|げんじつか} (actualization), {健康管理|けんこうかんり} (health management), {盛装|せいそう} (full dress), {図式|ずしき} (diagram/schema)
- **Nouns (16)**: {引|ひ}っ{越|こ}し{先|さき} (new place to move to), {総菜屋|そうざいや} (deli), {寝坊助|ねぼうすけ} (sleepyhead), {慰|なぐさ}め (comfort), {大逆転|だいぎゃくてん} (dramatic comeback), {空気入|くうきい}れ (air pump), {初戦|しょせん} (first match), {西口|にしぐち} (west exit), デニム (denim), {劇薬|げきやく} (powerful medicine), {猛火|もうか} (raging fire), {殺|ころ}し{屋|や} (hitman), {噺家|はなしか} (rakugo storyteller), {腹部|ふくぶ} (abdomen), {修正点|しゅうせいてん} (point to revise), {化学反応|かがくはんのう} (chemical reaction)
- **Expressions (4)**: {身|み}を{投|とう}じる (to devote oneself), {議論|ぎろん}を{呼|よ}ぶ (to spark debate), {通好|つうごの}み (connoisseur's taste), {膿|うみ} (pus/corruption)
- **Sports (2)**: {外野手|がいやしゅ} (outfielder), {論考|ろんこう} (essay/treatise)
- Added 1 new kanji to index: 噺
- Removed 30 candidates that now exist as entries

### 2026-04-02 (Vocabulary Expansion - 20 New Entries, Session 577)
Added 20 new dictionary entries (IDs 21627-21646) from candidate_words.json. A thematic set focused on emotions, states of mind, and expressive vocabulary useful for intermediate learners.

- **Onomatopoeia/suru verbs (6)**: ドキドキする (nervous/excited), ふらふらする (dizzy/wander), おどおどする (timid), びくびくする (apprehensive), うっとりする (entranced), {敬服|けいふく}する (to admire deeply)
- **Ichidan verbs (2)**: うろたえる (to be flustered), {巻|ま}き{込|こ}まれる (to be caught up in)
- **Godan verb (1)**: {立|た}ち{会|あ}う (to be present at)
- **Na-adjectives (2)**: {穏健|おんけん} (moderate), {重篤|じゅうとく} (critical/grave)
- **I-adjective (1)**: {別|わか}れ{惜|お}しい (reluctant to part)
- **Nouns (2)**: {本格|ほんかく} (full-scale/authentic), {原油|げんゆ} (crude oil), {拒否|きょひ}{反応|はんのう} (rejection reaction)
- **Adverb (1)**: {粛然|しゅくぜん} (solemnly)
- **Expressions (3)**: ひょっとしたら (perhaps), {涼|すず}しい{顔|かお} (nonchalant look), {肝|きも}を{冷|ひ}やす (to be terrified), {先|さき}を{越|こ}される (to be beaten to it)








---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
