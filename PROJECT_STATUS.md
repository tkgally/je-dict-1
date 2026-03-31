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

### 2026-03-31 (Vocabulary Expansion - 29 New Entries, Session 560)
Added 29 new dictionary entries (IDs 21168-21196) from candidate_words.json. A diverse mix covering time, safety, language, anatomy, nature, culture, fashion, food, and more.

- **Nouns (20)**: {幼少期|ようしょうき} (childhood), {防火|ぼうか} (fire prevention), {語法|ごほう} (diction), {気管|きかん} (windpipe), {日照|にっしょう} (sunshine), {見開|みひら}き (two-page spread), {村|むら}おこし (village revitalization), {渡|わた}し{舟|ぶね} (ferryboat), {公有|こうゆう} (public ownership), {兄嫁|あによめ} (sister-in-law), {橙|だいだい} (bitter orange), {柄物|がらもの} (patterned item), {回転|かいてん}ドア (revolving door), {保存|ほぞん}{容器|ようき} (storage container), {当|あ}て{推量|ずいりょう} (guesswork), {忌日|きじつ} (death anniversary), {密告者|みっこくしゃ} (informer), {猛寒|もうかん} (severe cold), {名校|めいこう} (famous school), {間諜|かんちょう} (spy)
- **Suru verbs (2)**: {補水|ほすい} (rehydration), {断煙|だんえん} (quitting smoking)
- **Na-adjectives (2)**: {堅固|けんご} (solid/firm), {儚|はかな}げ (seemingly fragile)
- **Noun/suffix (1)**: {圏|けん} (zone/sphere)
- **Noun/no-adjective (1)**: {対話型|たいわがた} (interactive)
- **Expression (1)**: {一丸|いちがん}となって (as one)
- **Other (2)**: {感謝|かんしゃ}{感激|かんげき} (deeply grateful), {綿入|わたい}れ (padded garment)
- Added 1 new kanji to index: 橙
- Removed 29 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 559)
Added 30 new dictionary entries (IDs 21138-21167) from candidate_words.json. Practical vocabulary covering verbs, nouns, and adjectives for everyday communication, finance, nature, and more.

- **Suru verbs (8)**: {説得|せっとく} (persuade), {分割|ぶんかつ} (divide), {分配|ぶんぱい} (distribute), {回収|かいしゅう} (collect/recall), {持参|じさん} (bring), {携帯|けいたい} (carry), {相当|そうとう} (correspond to), {匹敵|ひってき} (rival)
- **Godan verb (1)**: {書|か}き{残|のこ}す (leave in writing)
- **Nouns (17)**: {読|よ}み{書|か}き (literacy), {切|き}れ{端|はし} (scrap), {死後|しご} (after death), {自負|じふ} (pride), {休業日|きゅうぎょうび} (closed day), {衣料品|いりょうひん} (clothing), {乗組員|のりくみいん} (crew member), {遠征|えんせい} (expedition), {電話帳|でんわちょう} (phone book), {大群|たいぐん} (swarm), {金融機関|きんゆうきかん} (financial institution), {利率|りりつ} (interest rate), {地滑|じすべ}り (landslide), {同窓|どうそう} (alumnus), {照射|しょうしゃ} (irradiation), {苦慮|くりょ} (agonizing over), お{店|みせ} (shop), {島々|しまじま} (islands), {冒険者|ぼうけんしゃ} (adventurer)
- **Na-adjectives (2)**: {無防備|むぼうび} (defenseless), {敏捷|びんしょう} (agile)
- Added 1 new kanji to index: 捷
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 558)
Added 30 new dictionary entries (IDs 21108-21137) from candidate_words.json. A diverse mix covering culture, food, movement, emotions, finance, daily life, and formal/literary vocabulary.

- **Nouns (16)**: {切|き}り{身|み} (fillet), {脳裏|のうり} (one's mind), {白身魚|しろみざかな} (white fish), {民芸品|みんげいひん} (folk craft), {小走|こばし}り (trot), {早足|はやあし} (brisk walk), {出来上|できあ}がり (finished product), {医療保険|いりょうほけん} (medical insurance), {副収入|ふくしゅうにゅう} (side income), サラダ{油|あぶら} (cooking oil), {本館|ほんかん} (main building), {別館|べっかん} (annex), {島民|とうみん} (islander), カイロ (hand warmer), {耐熱|たいねつ} (heat-resistant), {仮設|かせつ} (temporary)
- **Suru verbs (4)**: {検閲|けんえつ} (censorship), {赤面|せきめん} (blushing), {欠落|けつらく} (omission), {常駐|じょうちゅう} (permanent stationing), {処遇|しょぐう} (treatment), {天日干|てんぴぼ}し (sun-drying)
- **Na-adjectives (2)**: {未曾有|みぞう} (unprecedented), {悠長|ゆうちょう} (leisurely)
- **I-adjective (1)**: {変|か}わりやすい (changeable)
- **Ichidan verb (1)**: {積|つ}み{立|た}てる (to save up)
- **Expression (2)**: {口|くち}をつぐむ (to keep silent), {火|ひ}を{見|み}るより{明|あき}らか (obvious beyond doubt)
- **Adverb (1)**: きっかり (exactly)
- **Other**: {荒涼|こうりょう} (desolate)
- Added 1 new kanji to index: 曾
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 557)
Added 30 new dictionary entries (IDs 21078-21107) from candidate_words.json. A mix of practical vocabulary covering communication, health, education, law, technology, culture, and everyday expressions.

- **Nouns (19)**: {口出|くちだ}し (meddling), {損傷|そんしょう} (damage), {余命|よめい} (remaining life expectancy), {校正|こうせい} (proofreading/calibration), {区切|くぎ}り (break/turning point), {納涼|のうりょう} (cooling off in summer), {許諾|きょだく} (permission), {本筋|ほんすじ} (main point), {可変|かへん} (variable), {照準|しょうじゅん} (aim/sighting), {既成事実|きせいじじつ} (fait accompli), {表層|ひょうそう} (surface layer), {高圧|こうあつ} (high pressure), {懲罰|ちょうばつ} (disciplinary punishment), {配点|はいてん} (point allocation), {禁欲|きんよく} (asceticism), {静音|せいおん} (silent operation), {帳面|ちょうめん} (notebook/ledger), {応用力|おうようりょく} (practical application skills)
- **Suru verbs (5)**: {習熟|しゅうじゅく} (becoming proficient), {扶助|ふじょ} (aid/support), {同梱|どうこん} (bundling/packing together), {論証|ろんしょう} (proof/argumentation), {噴霧|ふんむ} (spraying)
- **Ichidan verb (1)**: {見間違|みまちが}える (to mistake visually)
- **Na-adjective (1)**: {反抗的|はんこうてき} (rebellious)
- **Nouns (2)**: {伏兵|ふくへい} (ambush/dark horse), {養母|ようぼ} (adoptive mother)
- **Expression (1)**: {胸|むね}に{刺|さ}さる (to hit home)
- **Other**: {環境汚染|かんきょうおせん} (environmental pollution)
- Added 1 new kanji to index: 扶
- Removed 6 stale candidates (duplicates of existing entries)
- Removed 30 candidates that now exist as entries

### 2026-03-31 (Vocabulary Expansion - 30 New Entries, Session 556)
Added 30 new dictionary entries (IDs 21048-21077) from candidate_words.json. A practical mix covering emotions, food, family, places, daily life, and formal/business vocabulary.

- **Nouns (22)**: {感慨|かんがい} (deep emotion), {論点|ろんてん} (point of argument), {金賞|きんしょう} (gold prize), {里親|さとおや} (foster parent), {心残|こころのこ}り (lingering regret), {裏路地|うらろじ} (back alley), {酒類|しゅるい} (alcoholic beverages), {急務|きゅうむ} (urgent task), {粉|こな}ミルク (powdered milk), {練乳|れんにゅう} (condensed milk), {残雪|ざんせつ} (lingering snow), {人生観|じんせいかん} (view of life), {恥知|はじし}らず (shameless person), {固定費|こていひ} (fixed costs), {病室|びょうしつ} (hospital room), {凱旋|がいせん} (triumphal return), {養女|ようじょ} (adopted daughter), {実子|じっし} (biological child), {出入|でい}り{口|ぐち} (entrance/exit), {食生活|しょくせいかつ} (eating habits), {完全主義|かんぜんしゅぎ} (perfectionism), {人当|ひとあ}たり (manner with people)
- **Suru verbs (5)**: {失速|しっそく} (to stall/lose momentum), {散布|さんぷ} (to spray), {寄港|きこう} (to call at port), {子守|こも}り (babysitting), {駐車違反|ちゅうしゃいはん} (parking violation)
- **Godan verb (1)**: {聞|き}き{落|お}とす (to miss hearing)
- **I-adjective (1)**: {味気|あじけ}ない (dull/dreary)
- **Adverb (1)**: {後程|のちほど} (later on)
- Added 1 new kanji to index: 凱
- Removed 30 candidates that now exist as entries



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
