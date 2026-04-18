# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-17
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

### 2026-04-18 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 24214-24236) from candidate_words.json. A mix of loanwords, formal kanji compounds, and practical vocabulary.

- **Food (2)**: ピーナッツ (peanut), ロールケーキ (Swiss roll)
- **Household / tools (3)**: カッター (utility knife), タオルケット (towel blanket), サインペン (felt-tip pen)
- **Clothing / accessories (2)**: ストール (stole/shawl), {装身具|そうしんぐ} (jewelry/accessories)
- **Travel / outdoors (2)**: ランタン (lantern), トランク (trunk/suitcase)
- **Sports / entertainment (2)**: ラウンド (round of golf/boxing), パフォーマー (performer)
- **Hotels / general (1)**: ダブル (double room/double-breasted)
- **Technology (1)**: メモリー (memory/storage)
- **Abstract / academic (4)**: {類型|るいけい} (typology), {等価|とうか} (equivalence), {均整|きんせい} (proportion), {無感動|むかんどう} (unmoved)
- **People / culture (2)**: {鬼才|きさい} (genius), {教徒|きょうと} (religious follower)
- **Other (1)**: {漫歩|まんぽ} (stroll), {耐水|たいすい} (water resistance), {防腐|ぼうふ} (antisepsis), {甲斐性|かいしょう} (competence)
- Conjugation tables auto-generated for suru-verbs ({漫歩|まんぽ}, ラウンド)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,012 → 24,035.

### 2026-04-18 (Vocabulary Expansion - 25 New Entries)
Added 25 new dictionary entries (IDs 24189-24213) from candidate_words.json. A diverse batch covering everyday vocabulary, cultural terms, literary expressions, and specialized terminology.

- **Direction / spatial (2)**: {右側|みぎがわ} (right side), {右記|うき} (the above — in vertical writing)
- **Color (2)**: {緑色|みどりいろ} (green color), {朱|しゅ} (vermillion)
- **Food (2)**: {食肉|しょくにく} (meat for eating), {麩|ふ} (wheat gluten)
- **Medical / health (3)**: {飛沫感染|ひまつかんせん} (droplet infection), {臨終|りんじゅう} (deathbed), {大便|だいべん} (stool)
- **Travel / outdoors (3)**: バックパック (backpack), {宿営|しゅくえい} (encampment), {露営|ろえい} (bivouac)
- **History / culture (3)**: {本丸|ほんまる} (castle keep / main target), {名跡|めいせき} (historic site / stage name), {体操着|たいそうぎ} (gym clothes)
- **Expressions (4)**: {異議|いぎ}なし (no objection), {注意|ちゅうい}を{向|む}ける (to pay attention), {鼻歌|はなうた}を{歌|うた}う (to hum), どれだけ (how much)
- **Evaluation / degree (2)**: {卓絶|たくぜつ} (transcendent), {全数|ぜんすう} (total count)
- **Nature / weather (2)**: {波濤|はとう} (billowing waves), {寒冬|かんとう} (cold winter)
- **Photography (1)**: {映|うつ}り (image quality)
- **Emotion / body (1)**: {顔面蒼白|がんめんそうはく} (deathly pale)
- 1 new kanji added to index: 濤 (billows)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 23,987 → 24,012.

### 2026-04-17 (Vocabulary Expansion - 17 New Entries)
Added 17 new dictionary entries (IDs 24142-24158) from candidate_words.json. A diverse batch covering body/health, food, business, religion, industry, communication, and abstract concepts.

- **Body / health (2)**: {脂汗|あぶらあせ} (cold sweat), {誤飲|ごいん} (accidental ingestion)
- **Food / cooking (2)**: ほぐし (loosening; shredded), {焼|や}き{栗|ぐり} (roasted chestnuts)
- **Religion / culture (2)**: {崇敬|すうけい} (reverence), {経典|きょうてん} (scripture)
- **Industry / science (3)**: {製錬|せいれん} (smelting), {冶金|やきん} (metallurgy), {不凍|ふとう} (non-freezing)
- **Business / communication (3)**: {社外秘|しゃがいひ} (confidential), {切電|せつでん} (hanging up), {電工|でんこう} (electrician)
- **Entertainment (1)**: {旧作|きゅうさく} (older work)
- **Abstract (2)**: {内在|ないざい} (inherence), ありよう (way of being)
- **Onomatopoeia (1)**: しゅっと (sleekly; swiftly)
- **Totality (1)**: {合切|がっさい} (all; everything)
- 1 new kanji added to index: 冶 (smelt)
- 2 stale candidates removed (ばっかり duplicate of ばかり, 露わに duplicate of 露に)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 23,940 → 23,957.

### 2026-04-17 (Vocabulary Expansion - 25 New Entries)
Added 25 new dictionary entries (IDs 24117-24141) from candidate_words.json. A practical batch covering work/business, food/cooking, daily life, education, arts, and nature vocabulary.

- **Work / business (6)**: {中小企業|ちゅうしょうきぎょう} (SME), {理容師|りようし} (barber), インターンシップ (internship), {同業者|どうぎょうしゃ} (industry peer), {作業着|さぎょうぎ} (work clothes), {作業員|さぎょういん} (worker)
- **Time / weather (3)**: {例年通|れいねんどお}り (as usual), {平年|へいねん} (average year), {勤務時間|きんむじかん} (working hours)
- **Food / cooking (2)**: {長芋|ながいも} (Chinese yam), {自然薯|じねんじょ} (wild yam)
- **Safety / expressions (2)**: {安全第一|あんぜんだいいち} (safety first), {時間|じかん}が{経|た}つ (time passes)
- **Nature / geography (2)**: {河川敷|かせんしき} (riverside area), {砦|とりで} (fortress)
- **Shopping / products (2)**: {純正品|じゅんせいひん} (genuine product), {濃色|のうしょく} (dark color)
- **Academics / arts (2)**: {総論|そうろん} (general overview), {受賞作|じゅしょうさく} (award-winning work)
- **Body / literary (2)**: {掌|たなごころ} (palm — literary), {館|やかた} (mansion)
- **Daily life / education (3)**: {竿|さお} (pole/rod), {校外|こうがい} (off-campus), {交友関係|こうゆうかんけい} (circle of friends)
- **Herbicide (1)**: {除草剤|じょそうざい} (herbicide)
- 2 new kanji added to index: 砦 (fortress), 薯 (yam)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 23,915 → 23,940.

### 2026-04-17 (Vocabulary Expansion - 21 New Entries)
Added 21 new dictionary entries (IDs 24096-24116) from candidate_words.json. A practical batch covering commerce, law, travel, culture, safety, and daily-life vocabulary useful for intermediate learners.

- **Commerce (3)**: {古物|こぶつ} (secondhand goods/antiques), {取扱店|とりあつかいてん} (authorized dealer), {卸売店|おろしうりてん} (wholesale shop)
- **Finance / business (3)**: {収益率|しゅうえきりつ} (rate of return), {項目別|こうもくべつ} (by item/category), {好成績|こうせいせき} (excellent performance)
- **Travel / daily life (3)**: {日帰|ひがえ}り{旅行|りょこう} (day trip), {預|あず}かり{所|じょ} (checkroom/storage), {紛失物|ふんしつぶつ} (lost property)
- **Culture / art (3)**: {書画|しょが} (calligraphy and painting), {伝統産業|でんとうさんぎょう} (traditional industry), {異邦人|いほうじん} (foreigner/stranger — literary)
- **Safety / law (3)**: {自己防衛|じこぼうえい} (self-defense), {権利者|けんりしゃ} (rights holder), {耐震構造|たいしんこうぞう} (earthquake-resistant structure)
- **Politics / society (2)**: {支配力|しはいりょく} (controlling power/dominance), {視察団|しさつだん} (inspection delegation)
- **Medicine (1)**: {整骨|せいこつ} (bonesetting/osteopathic treatment)
- **Transportation (1)**: {黄信号|きしんごう} (yellow light — literal and figurative)
- **Abstract (1)**: {欠|か}かせない (indispensable — i-adjective)
- **Animals (1)**: {迷|まよ}い{犬|いぬ} (lost dog)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana
- Conjugation tables auto-generated for verb-suru (自己防衛) and i-adjective (欠かせない) entries

Total entries: 23,894 → 23,915.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








