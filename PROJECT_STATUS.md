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

### 2026-04-17 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 24066-24095) from candidate_words.json. A diverse batch of two-kanji compound words covering transportation, household, administration, finance, science, culture, and military vocabulary.

- **Transportation / location (2)**: {南口|みなみぐち} (south exit), {東口|ひがしぐち} (east exit) — essential station navigation vocabulary
- **Household / everyday (3)**: {油性|ゆせい} (oil-based), {顆粒|かりゅう} (granules), {取|と}っ{手|て} (handle; knob)
- **Administration / law (3)**: {要項|ようこう} (guidelines; essentials), {減免|げんめん} (reduction and exemption), {職権|しょっけん} (official authority)
- **Finance / business (2)**: {社債|しゃさい} (corporate bond), {積算|せきさん} (accumulation; cost estimation — two senses)
- **Housing / infrastructure (1)**: {漏水|ろうすい} (water leak)
- **Science / industry (3)**: {圧搾|あっさく} (compression; pressing), {減圧|げんあつ} (decompression), {製鉄|せいてつ} (ironmaking)
- **Architecture / history (3)**: {御殿|ごてん} (palace; mansion), {城郭|じょうかく} (castle compound), {上層|じょうそう} (upper layer/stratum)
- **Culture / education (4)**: {学芸|がくげい} (arts and sciences), {射的|しゃてき} (shooting gallery), {任侠|にんきょう} (chivalry), {増刊|ぞうかん} (special issue)
- **Mathematics (2)**: {立方|りっぽう} (cubic; cube), {音信|おんしん} (correspondence — most common in {音信|おんしん}{不通|ふつう})
- **Military / conflict (3)**: {軍縮|ぐんしゅく} (disarmament), {死闘|しとう} (fierce battle), {防備|ぼうび} (defense preparations)
- **Social (2)**: {宴席|えんせき} (banquet), {慰問|いもん} (consolation visit)
- **Abstract (1)**: {純潔|じゅんけつ} (purity; chastity)
- 2 new kanji added to index: 侠 (chivalry), 顆 (grain)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 23,864 → 23,894.

### 2026-04-17 (Vocabulary Expansion - 13 New Entries)
Added 13 new dictionary entries (IDs 24053-24065) from candidate_words.json. A varied batch covering formal abstract nouns, news/legal vocabulary, sports vocabulary, anatomy, traffic accidents, set expressions, and one loanword adjective.

- **Formal abstract / news (3)**: {提起|ていき} (raising an issue; filing a lawsuit — two senses), {転覆|てんぷく} (capsizing; toppling a regime — two senses), {鑑識|かんしき} (forensics; expert appraisal — two senses)
- **Loanword adjective (1)**: リスキー (risky — na-adjective)
- **Crime / law (1)**: {賭博|とばく} (gambling — formal term, cross-linked with informal {博打|ばくち})
- **Architecture / sports (1)**: ドーム (dome / domed stadium)
- **Sports / abstract (1)**: {攻守|こうしゅ} (offense and defense — two senses, literal and figurative)
- **Anatomy (1)**: {頬骨|ほほぼね} (cheekbone)
- **Set expressions (2)**: {喫緊|きっきん}の{課題|かだい} (urgent issue), {殺伐|さつばつ}とした (bleak; grim — taru-form modifier)
- **Transportation / law (2)**: {路上駐車|ろじょうちゅうしゃ} (on-street parking — also verb-suru), {追突事故|ついとつじこ} (rear-end collision)
- **Society (1)**: {徒党|ととう} (clique; faction — appears chiefly in {徒党|ととう}を{組|く}む)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, sense-number annotations, and full conjugation tables for verb-suru entries

Total entries: 23,851 → 23,864.

### 2026-04-16 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 24043-24052) from candidate_words.json. A balanced set spanning body-part, age, religion, academia, science, expressions, and music/verb vocabulary.

- **Body-part (1)**: {足|あし}の{親指|おやゆび} (big toe — includes full toe-naming table)
- **Age / demographics (1)**: {四十代|よんじゅうだい} (one's forties — mirrors the 三十代/二十代 pattern)
- **Academia (1)**: {文学部|ぶんがくぶ} (Faculty of Letters; Faculty of Humanities — covers typical departments and cultural context)
- **Religion (2)**: {旧約聖書|きゅうやくせいしょ} (Old Testament), {新約聖書|しんやくせいしょ} (New Testament) — cross-linked pair, both tied to the existing 聖書 entry
- **Science (1)**: アミノ{酸|さん} (amino acid — nutrition/cosmetics/chemistry contexts)
- **Expressions / adverbials (2)**: {歴史上|れきしじょう} (historically; in history — noun/adverbial use with の and bare forms), {最後|さいご}には (in the end; ultimately — distinguished from 最後に, ついに, 結局, 最終的に)
- **Communication (1)**: {書|か}きぶり (writing style; manner of writing — contrasts with 話しぶり, 書き方, 文体, 筆致)
- **Verb (1)**: かき{鳴|な}らす (to strum; to play loudly — godan-su with full conjugation table; transitive, for stringed instruments)
- All entries follow v2 standards: progressive-length examples (3+ per sense), structured notes with USAGE / COMMON COLLOCATIONS / SIMILAR WORDS sections, full furigana coverage, and sense-number annotations

Total entries: 23,841 → 23,851.

### 2026-04-15 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 24027-24042) from candidate_words.json. A mixed batch covering emotion, communication, geography, weather, agriculture, real estate, transportation, and entertainment vocabulary.

- **Emotion / abstract (3)**: {愛欲|あいよく} (lust; carnal desire), {形式主義|けいしきしゅぎ} (formalism), {現象的|げんしょうてき} (phenomenal; on the surface) [adjective-na]
- **Communication / humor (1)**: {駄洒落|だじゃれ}る (to make a corny pun) [verb-ichidan]
- **Geography / weather (2)**: {不毛地帯|ふもうちたい} (barren land; wasteland), {湿雪|しっせつ} (wet snow)
- **Agriculture / nature (3)**: {真珠貝|しんじゅがい} (pearl oyster), りんご{園|えん} (apple orchard), りんご{農家|のうか} (apple farmer)
- **Society / people (1)**: {余所様|よそさま} (other people; polite)
- **Real estate / construction (1)**: {敷地面積|しきちめんせき} (site area; lot area)
- **Transport / safety (3)**: {車検証|しゃけんしょう} (vehicle inspection certificate), {除氷|じょひょう} (de-icing; ice removal), {散乱物|さんらんぶつ} (scattered debris)
- **Food / tableware (1)**: {盛|も}り{皿|ざら} (serving plate)
- **Entertainment (1)**: {漫才|まんざい}コンビ (manzai duo)

Total entries: 23,825 → 23,841.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








