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

### 2026-04-20 (Vocabulary Expansion - 27 New Entries, Batch 12)
Added 27 new dictionary entries (IDs 24717-24743) from candidate_words.json. Mix of practical, technical, academic, and cultural vocabulary.

- **Technology (3)**: ディスプレー (display/monitor), クリックする (to click), サインアウト (sign out)
- **Transport / driving (4)**: {迎車|げいしゃ} (taxi pickup), バイク{便|びん} (motorcycle courier), {走行車線|そうこうしゃせん} (driving lane), {追越車線|おいこししゃせん} (passing lane)
- **Academic / formal (6)**: {産業化|さんぎょうか} (industrialization), {関連性|かんれんせい} (relevance), {真実性|しんじつせい} (truthfulness), {比喩|ひゆ}する (to use metaphor), {勢力範囲|せいりょくはんい} (sphere of influence), {鎮定|ちんてい} (pacification)
- **Business / law (2)**: {独占権|どくせんけん} (exclusive right), {献言|けんげん} (offering advice)
- **Daily life / culture (6)**: {紙|かみ}ナプキン (paper napkin), たばこ{屋|や} (tobacco shop), {合|あ}わせ{鏡|かがみ} (facing mirrors), ぬかみそ (rice-bran paste), {裁縫道具|さいほうどうぐ} (sewing tools), {午後便|ごごびん} (afternoon delivery)
- **Nature / general (4)**: {天然資源|てんねんしげん} (natural resources), {霧中|むちゅう} (in fog), {貴石|きせき} (precious stone), {間抜|まぬ}け{面|づら} (stupid face)
- **Sports (1)**: {不戦勝|ふせんが}ち (win by default)
- **Narrative (1)**: {場面転換|ばめんてんかん} (scene change)
- Conjugation tables auto-generated for 7 suru verb entries
- Removed 27 candidates that became entries

Total entries: 24,514 → 24,541.

### 2026-04-20 (Vocabulary Expansion - 26 New Entries, Batch 11)
Added 26 new dictionary entries (IDs 24691-24716) from candidate_words.json. Batch focusing on practical, business, cultural, and everyday vocabulary with detailed notes and collocations.

- **Business / work (4)**: {内部告発|ないぶこくはつ} (whistleblowing), {事後報告|じごほうこく} (after-the-fact report), {按分|あんぶん} (apportionment), {栄進|えいしん} (promotion)
- **Social / cultural (3)**: {縁故主義|えんこしゅぎ} (nepotism), {感情表出|かんじょうひょうしゅつ} (expression of emotion), {社会教育|しゃかいきょういく} (social education)
- **Finance / practical (3)**: {医療費|いりょうひ} (medical expenses), {予算内|よさんない} (within budget), {懐具合|ふところぐあい} (financial situation)
- **Daily life / household (3)**: {調理台|ちょうりだい} (kitchen counter), シミ{取|と}り (stain removal), {大|おお}あくび (big yawn)
- **Nature / body (3)**: {種苗|しゅびょう} (seeds and seedlings), {尾|お}びれ (tail fin), {擦|す}れ (chafing)
- **Places / description (3)**: {地柄|じがら} (character of an area), {不自然|ふしぜん}さ (unnaturalness), {傾向性|けいこうせい} (tendency)
- **Education / expression (3)**: {家庭学習|かていがくしゅう} (home study), {自己表現|じこひょうげん} (self-expression), {魚料理|さかなりょうり} (fish cuisine)
- **Other (4)**: {引|ひ}き{込|こ}み (drawing in), {打鍵音|だけんおん} (keystroke sound), {当日予約|とうじつよやく} (same-day reservation), {庫裏|くり} (temple kitchen)
- Conjugation tables auto-generated for 5 suru verb entries
- 1 new kanji added to index: 按
- Removed 1 stale candidate (えこひいきする — duplicate of entry 20939)

Total entries: 24,488 → 24,514.

### 2026-04-20 (Vocabulary Expansion - 30 New Entries, Batch 10)
Added 30 new dictionary entries (IDs 24661-24690) from candidate_words.json. Diverse batch focusing on practical, institutional, and cultural vocabulary across many domains.

- **Society / politics (4)**: {専制政治|せんせいせいじ} (despotism), {世論形成|よろんけいせい} (forming public opinion), {保護観察|ほごかんさつ} (probation), {新興宗教|しんこうしゅうきょう} (new religious movement)
- **Law / business (3)**: {営利法人|えいりほうじん} (for-profit corporation), {決議事項|けつぎじこう} (resolution items), {協同組合|きょうどうくみあい} (cooperative)
- **Health / medicine (2)**: {国民健康保険|こくみんけんこうほけん} (National Health Insurance), {静脈注射|じょうみゃくちゅうしゃ} (IV injection)
- **Daily life / practical (4)**: {通行禁止|つうこうきんし} (no passage), {台所仕事|だいどころしごと} (kitchen work), {発信履歴|はっしんりれき} (call history), {女子寮|じょしりょう} (women's dormitory)
- **Education / academic (3)**: {研究発表|けんきゅうはっぴょう} (research presentation), {教科課程|きょうかかてい} (curriculum), {出現頻度|しゅつげんひんど} (frequency of occurrence)
- **Technology (2)**: {文字認識|もじにんしき} (character recognition/OCR), {位置関係|いちかんけい} (spatial relationship)
- **Culture / personality (3)**: {義侠|ぎきょう} (chivalry), {自己中心|じこちゅうしん} (egocentrism), {念願成就|ねんがんじょうじゅ} (wish fulfillment)
- **Nature / agriculture (2)**: {害獣|がいじゅう} (pest animal), {防除|ぼうじょ} (pest control)
- **Other (7)**: {汽船|きせん} (steamship), {和英辞典|わえいじてん} (J-E dictionary), {消息不明|しょうそくふめい} (missing/whereabouts unknown), {風紀委員|ふうきいいん} (discipline committee), {汚名挽回|おめいばんかい} (restoring reputation), {美白効果|びはくこうか} (skin-whitening effect), {事後処理|じごしょり} (post-processing)
- Conjugation tables auto-generated for 7 suru verb entries

Total entries: 24,458 → 24,488.

### 2026-04-20 (Vocabulary Expansion - 26 New Entries, Batch 9)
Added 26 new dictionary entries (IDs 24635-24660) from candidate_words.json. Diverse batch covering media/publishing, politics/history, religion/culture, nature, medicine, business, and practical vocabulary.

- **Media / publishing (3)**: {論説|ろんせつ} (editorial), {図版|ずはん} (illustration/plate), {扉絵|とびらえ} (frontispiece)
- **Politics / history / military (3)**: {軍部|ぐんぶ} (military establishment), {文民統制|ぶんみんとうせい} (civilian control), {名誉回復|めいよかいふく} (restoration of honor)
- **Religion / culture (3)**: {本山|ほんざん} (head temple), {献納|けんのう} (dedication/offering), {滝行|たきぎょう} (waterfall meditation)
- **Nature / geography (3)**: {滝壺|たきつぼ} (plunge pool), {名瀑|めいばく} (famous waterfall), {鳥獣|ちょうじゅう} (birds and beasts)
- **Ceramics / food (3)**: {焼成|しょうせい} (firing/kiln), {素焼|すや}き (bisque/plain grill), {糖類|とうるい} (sugars/saccharides)
- **Business / finance (2)**: {経常利益|けいじょうりえき} (ordinary profit), {豪商|ごうしょう} (wealthy merchant)
- **Medicine (1)**: {梗塞|こうそく} (infarction)
- **Law / insurance (1)**: {物損|ぶっそん} (property damage)
- **Society (2)**: {婦人会|ふじんかい} (women's association), {私物化|しぶつか} (personal appropriation)
- **Education / daily life (3)**: {提出物|ていしゅつぶつ} (assignment), {年賀|ねんが}はがき (New Year's postcard), {感冒薬|かんぼうやく} (cold medicine)
- **Linguistics (1)**: {間投詞|かんとうし} (interjection)
- **Photography (1)**: {望遠|ぼうえん}レンズ (telephoto lens)
- Removed 1 stale candidate (おかみさん — variant of existing entry)
- 2 new kanji added to index: 壺, 瀑

Total entries: 24,432 → 24,458.

### 2026-04-20 (Vocabulary Expansion - 24 New Entries, Batch 8)
Added 24 new dictionary entries (IDs 24611-24634) from candidate_words.json. Diverse batch covering business, culture, science, law, sports, and practical vocabulary.

- **Business / organization (3)**: {総務課|そうむか} (general affairs section), {主幹|しゅかん} (chief editor/manager), {勢力図|せいりょくず} (power map)
- **Religion / culture (3)**: {崇拝者|すうはいしゃ} (worshipper/devotee), {彼岸会|ひがんえ} (higan memorial service), はかなさ (transience)
- **Science / math (2)**: {切片|せっぺん} (section/intercept), {果糖|かとう} (fructose)
- **Music / arts (2)**: {和声|わせい} (harmony), {合本|がっぽん} (combined volume)
- **Law / politics (3)**: {公序良俗|こうじょりょうぞく} (public order and morals), {不戦|ふせん} (non-combat/by default), {寡占|かせん} (oligopoly)
- **Economics / society (2)**: {期待感|きたいかん} (sense of expectation), {有志者|ゆうししゃ} (volunteer)
- **Technology / infrastructure (3)**: {接続口|せつぞくぐち} (connection port), {導線|どうせん} (conductor wire/flow line), {通用門|つうようもん} (service gate)
- **Education (1)**: {択一式|たくいつしき} (multiple-choice format)
- **Transport (1)**: {搭乗者|とうじょうしゃ} (passenger)
- **Construction (1)**: {部材|ぶざい} (structural member)
- **Sports (1)**: {完投|かんとう} (complete game)
- **Descriptive (2)**: {総覧|そうらん} (comprehensive survey), {露骨|ろこつ}さ (blatancy)

Total entries: 24,408 → 24,432.

### 2026-04-19 (Vocabulary Expansion - 22 New Entries, Batch 7)
Added 22 new dictionary entries (IDs 24589-24610) from candidate_words.json. A diverse batch covering history/culture, food/nature, academic/formal, medical, and practical vocabulary.

- **History / culture (5)**: {反面教師|はんめんきょうし} (negative example), {反物|たんもの} (bolt of cloth), {騎馬|きば} (horseback), {武具|ぶぐ} (arms and armor), {駕籠|かご} (palanquin)
- **Religion / spirituality (2)**: {汚|けが}れ (impurity/defilement), {布施|ふせ} (alms/offering)
- **Food / nature (3)**: {菜種|なたね} (rapeseed), {瓶詰|びんづめ} (bottled goods), {残熱|ざんねつ} (residual heat)
- **Academic / formal (4)**: {連関|れんかん} (interrelation), {沈思|ちんし} (deep thought), {奮励|ふんれい} (strenuous effort), {王権|おうけん} (royal authority)
- **Medical (1)**: {塗布|とふ} (application of ointment)
- **Business / education (2)**: {販売価格|はんばいかかく} (selling price), {勉強机|べんきょうづくえ} (study desk)
- **Language / sports (2)**: {日英|にちえい} (Japanese-English), {泳法|えいほう} (swimming stroke)
- **Color / place (2)**: {青緑|あおみどり} (blue-green), {裏手|うらて} (back side)
- **Multi-sense (1)**: {鼻薬|はなぐすり} (nasal medicine / bribe)

Total entries: 24,386 → 24,408.

### 2026-04-19 (Vocabulary Expansion - 30 New Entries, Batch 6)
Added 30 new dictionary entries (IDs 24559-24588) from candidate_words.json. A diverse batch covering academic/formal vocabulary, daily life, culture, sports, politics, and practical terms.

- **Academic / formal (4)**: {類似点|るいじてん} (point of similarity), {刊行物|かんこうぶつ} (publication), {印刷物|いんさつぶつ} (printed matter), {考証|こうしょう} (historical verification)
- **Society / politics (4)**: {不公正|ふこうせい} (unfair/unjust), {反対党|はんたいとう} (opposition party), {非核|ひかく} (non-nuclear), {尊厳死|そんげんし} (death with dignity)
- **Daily life / practical (4)**: {改装中|かいそうちゅう} (under renovation), {禁煙車|きんえんしゃ} (non-smoking car), {地階|ちかい} (basement floor), {収集車|しゅうしゅうしゃ} (garbage truck)
- **Culture / arts (4)**: {喜悦|きえつ} (joy/delight), お{銚子|ちょうし} (sake flask), {画室|がしつ} (artist's studio), {洗練|せんれん}さ (refinement/sophistication)
- **Military / history (1)**: {兵法|へいほう} (military strategy)
- **Sports (1)**: {本塁打|ほんるいだ} (home run)
- **Law / crime (2)**: {窃取|せっしゅ} (theft/pilferage), {公告|こうこく} (public notice)
- **Mathematics / science (1)**: {交点|こうてん} (intersection point)
- **Business / logistics (2)**: {荷積|にづ}み (cargo loading), {数十倍|すうじゅうばい} (tens of times)
- **Descriptive (4)**: {重|かさ}なり (overlap/coincidence), かすれ (hoarseness/blur), {尾|お}ひれ (tail fin / embellishments), {服従的|ふくじゅうてき} (submissive)
- **Work / colloquial (2)**: {午後一|ごごいち} (first thing in the afternoon), {振付家|ふりつけか} (choreographer)
- **Animals (1)**: {捨|す}て{犬|いぬ} (abandoned dog)
- 2 new kanji added to index: 悦, 銚

Total entries: 24,356 → 24,386.



_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
