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

### 2026-03-31 (Cross-Reference System Overhaul)
Created a new systematic cross-reference review system and updated related documentation.

- **New prompt**: `prompts/add_cross-references.md` — systematically reviews entries and adds/verifies both `prominent_see_also` and `cross_references` links
- **New tracking file**: `prompts/add-cross-references-tracking.txt` — pre-populated with all 2,783 basic and core tier entries
- **Updated skill**: `.claude/skills/cross-reference-entry/SKILL.md` — expanded `prominent_see_also` guidance to cover transitive/intransitive pairs, N/Nする pairs, informal/formal pairs, and other closely related word groups; deprecated `pair` type in `cross_references` (transitive/intransitive pairs now use `prominent_see_also`)
- **Deleted**: `prompts/add_prominent_crossrefs.md` (superseded by new prompt)
- **Updated**: CLAUDE.md, README.md, metaprompt_list.md references

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 553)
Added 30 new dictionary entries (IDs 20939-20968) from candidate_words.json. A diverse mix covering social behavior, transportation, culture, nature, food, politics, history, law, arts, and daily life.

- **Nouns (19)**: {普通車|ふつうしゃ} (standard car/regular train car), {若年層|じゃくねんそう} (younger generation), {毒蛇|どくへび} (venomous snake), ポニーテール (ponytail), {祝儀袋|しゅうぎぶくろ} (gift money envelope), {豆板醤|とうばんじゃん} (chili bean paste), {雑穀|ざっこく} (mixed grains), {国会議員|こっかいぎいん} (Diet member), {左官|さかん} (plasterer), {控|ひか}え{選手|せんしゅ} (substitute player), {二輪車|にりんしゃ} (two-wheeled vehicle), {市外局番|しがいきょくばん} (area code), {正誤表|せいごひょう} (errata), {練習曲|れんしゅうきょく} (etude), {写本|しゃほん} (manuscript), {相談役|そうだんやく} (advisor), {遠隔地|えんかくち} (remote area), {絶景|ぜっけい}スポット (scenic viewpoint), {放物線|ほうぶつせん} (parabola)
- **Suru verbs (3)**: {依怙贔屓|えこひいき} (favoritism), {天下統一|てんかとういつ} (national unification), {成敗|せいばい} (punishment)
- **Na-adjectives (3)**: {草食|そうしょく} (herbivorous/passive), {合憲|ごうけん} (constitutional), {苦労性|くろうしょう} (worrywart)
- **Expressions (2)**: {眼鏡|めがね}をかける (to wear glasses), {何事|なにごと}も (everything)
- **Other (3)**: こら (hey!/stop that!), {自然遺産|しぜんいさん} (natural heritage), {宵|よい}の{明星|みょうじょう} (evening star)
- Added 1 new kanji to index: 怙

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 552)
Added 30 new dictionary entries (IDs 20893-20922) from candidate_words.json. A diverse mix of nouns, verbs, adjectives, and adverbs covering daily life, food, culture, finance, geography, technology, and society.

- **Nouns (14)**: {企|くわだ}て (plan/plot), {小銭入|こぜにい}れ (coin purse), {販売店|はんばいてん} (retail store), {油脂|ゆし} (fats and oils), お{茶請|ちゃう}け (tea snack), {陶芸家|とうげいか} (ceramist), {美容整形|びようせいけい} (cosmetic surgery), {北半球|きたはんきゅう} (Northern Hemisphere), {司令官|しれいかん} (commander), {甲殻類|こうかくるい} (crustaceans), {志願者|しがんしゃ} (volunteer/applicant), {輪廻転生|りんねてんしょう} (reincarnation), {不良債権|ふりょうさいけん} (bad debt), {保養地|ほようち} (health resort)
- **Suru verbs (6)**: {読破|どくは}する (to finish reading), {適合|てきごう} (conformity), {省力化|しょうりょくか} (labor-saving), {肩代|かたが}わりする (to take over a burden), {冠水|かんすい} (flooding), {脱臭|だっしゅう} (deodorization)
- **Na-adjectives (4)**: {短|みじか}め (somewhat short), {太|ふと}め (somewhat thick), {細|ほそ}め (somewhat thin), {同情的|どうじょうてき} (sympathetic)
- **Adverb (1)**: {公然|こうぜん} (openly/publicly)
- **Other (5)**: へたれ (wimp), {漫談|まんだん} (comic talk), フォント (font), {甘納豆|あまなっとう} (sweetened beans), {地域|ちいき}おこし (regional revitalization)

### 2026-03-30 (Vocabulary Expansion - 16 New Entries, Session 552)
Added 16 new dictionary entries (IDs 20923-20938) from candidate_words.json. A mix of compound verbs, suru verbs, nouns, and na-adjectives covering everyday actions, psychology, commerce, geography, and social interaction.

- **Godan verbs (4)**: {売|う}れ{残|のこ}る (to remain unsold), {作|つく}り{直|なお}す (to remake), {取|と}り{囲|かこ}む (to surround), {引|ひ}き{続|つづ}く (to continue)
- **Ichidan verb (1)**: {聞|き}かせる (to tell/let hear)
- **Suru verbs (5)**: {披露|ひろう} (to unveil/present), {出現|しゅつげん} (to appear/emerge), {執着|しゅうちゃく} (to cling to), {固執|こしつ} (to persist stubbornly), {拘束|こうそく} (to restrain/detain)
- **Nouns (3)**: ふれあい (interaction/togetherness), {失神|しっしん} (fainting), {市内|しない} (within the city)
- **Na-adjectives (2)**: {世界的|せかいてき} (worldwide/global), {苛烈|かれつ} (fierce/severe)
- **Other (1)**: {国外|こくがい} (outside the country)
- Removed 16 candidates that now exist as entries

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 551)
Added 30 new dictionary entries (IDs 20863-20892) from candidate_words.json. A diverse mix of suru verbs, godan verb, nouns, na-adjectives, and expressions covering language, science, finance, culture, food, medicine, sports, and daily life.

- **Suru verbs (7)**: {連発|れんぱつ} (rapid repetition), {続発|ぞくはつ} (successive occurrence), {透過|とうか} (transmission/permeation), {帰属|きぞく} (belonging/attribution), {隷属|れいぞく} (subordination/servitude), {退色|たいしょく} (fading/discoloration), {注文生産|ちゅうもんせいさん} (made-to-order production — noun only)
- **Godan verb (1)**: {澄|す}み{切|き}る (to be crystal clear)
- **Nouns (14)**: {不成功|ふせいこう} (failure), {限度額|げんどがく} (credit limit), {無応答|むおうとう} (no response), {伝達力|でんたつりょく} (communication ability), {損害保険|そんがいほけん} (non-life insurance), {心理戦|しんりせん} (psychological warfare), {非推奨|ひすいしょう} (deprecated), {輝度|きど} (brightness/luminance), {防錆|ぼうせい} (rust prevention), {撥|ばち} (plectrum/drumstick), {兄貴分|あにきぶん} (big-brother figure), {葉菜|ようさい} (leafy vegetable), {獣医学|じゅういがく} (veterinary medicine), {注文服|ちゅうもんふく} (custom clothing), {副助詞|ふくじょし} (adverbial particle), {紆余|うよ} (winding/meandering)
- **Expressions (2)**: {品|ひん}がある (to have class), {予約困難|よやくこんなん} (hard to book)
- **Other (2)**: {拳闘|けんとう} (boxing), {浄化槽|じょうかそう} (septic tank), {脳神経|のうしんけい} (cranial nerve)
- Added 1 new kanji to index: 隷
- Removed 20 stale duplicate candidates from candidate_words.json



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
