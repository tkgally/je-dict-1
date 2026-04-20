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

### 2026-04-20 (Vocabulary Expansion - 30 New Entries, Batch 15)
Added 30 new dictionary entries (IDs 24786-24815) from candidate_words.json. Diverse batch covering military, history, culture, science, language, sports, daily life, and modern society.

- **Military / security (3)**: {匍匐|ほふく} (crawling), {着弾|ちゃくだん} (projectile impact), {化学|かがく}{兵器|へいき} (chemical weapon)
- **History / culture (5)**: {後宮|こうきゅう} (inner palace), {武家屋敷|ぶけやしき} (samurai residence), {文化勲章|ぶんかくんしょう} (Order of Culture), {進上|しんじょう} (formal gift-giving), {貴公|きこう} (archaic "you")
- **Science / education (3)**: {化学式|かがくしき} (chemical formula), {仮定形|かていけい} (hypothetical form), {化学|かがく}{薬品|やくひん} (chemicals)
- **Sports / entertainment (3)**: {白星|しろぼし}を{挙|あ}げる (score a win), {通|とお}し{稽古|げいこ} (full rehearsal), {着|き}せ{替|か}え{人形|にんぎょう} (dress-up doll)
- **Modern society (3)**: {転売|てんばい}{禁止|きんし} (resale prohibition), {命名権|めいめいけん} (naming rights), {入場|にゅうじょう}{禁止|きんし} (no admittance)
- **Health / daily life (4)**: {体脂肪率|たいしぼうりつ} (body fat percentage), {生理用品|せいりようひん} (sanitary products), {入院|にゅういん}{患者|かんじゃ} (inpatient), {滞在|たいざい}{日数|にっすう} (length of stay)
- **Language / register (2)**: てめえ (vulgar "you"), {返|かえ}し (comeback/sauce)
- **Other (7)**: ホワイトアウト (whiteout), {地場|じば}{産業|さんぎょう} (local industry), {追悼式|ついとうしき} (memorial service), {粒度|りゅうど} (granularity), {跳|は}ね{返|かえ}し (rebound), {素性|すじょう}が{知|し}れる (background revealed), {筋骨|きんこつ}たくましい (muscular)

Total entries: 24,583 → 24,613.

### 2026-04-20 (Vocabulary Expansion - 17 New Entries, Batch 14)
Added 17 new dictionary entries (IDs 24769-24785) from candidate_words.json. Diverse batch covering business/finance, culture, food, nature, geography, and daily life.

- **Business / finance (4)**: {売|う}り{手|て} (seller), {買|か}い{手|て} (buyer), {証券会社|しょうけんがいしゃ} (securities company), {信用金庫|しんようきんこ} (credit union)
- **Culture / history (4)**: {宿場町|しゅくばまち} (post town), {護符|ごふ} (protective talisman), {呪術|じゅじゅつ} (sorcery), {日帰|ひがえ}り{温泉|おんせん} (day-trip hot spring)
- **Food (1)**: {味噌漬|みそづ}け (miso pickles)
- **Nature (1)**: {雛鳥|ひなどり} (baby bird)
- **Formal / meetings (2)**: {散会|さんかい} (adjournment), {政令|せいれい} (cabinet order)
- **Other (5)**: {最終日|さいしゅうび} (final day), {浄水器|じょうすいき} (water purifier), {弟分|おとうとぶん} (younger-brother figure), {中間色|ちゅうかんしょく} (intermediate color), {放射状|ほうしゃじょう} (radial pattern)
- Conjugation table auto-generated for 1 suru verb entry (散会)
- Removed 1 stale candidate (他人事/たにんごと, covered by existing entry 09570)

Total entries: 24,566 → 24,583.

### 2026-04-20 (Vocabulary Expansion - 25 New Entries, Batch 13)
Added 25 new dictionary entries (IDs 24744-24768) from candidate_words.json. Diverse batch covering cultural practices, daily life, finance, history, medical, and general vocabulary.

- **Culture / religion (4)**: {厄除|やくよ}け (warding off bad luck), {十五夜|じゅうごや} (harvest moon), {初宮参|はつみやまい}り (baby's first shrine visit), {赤口|しゃっこう} (rokuyo unlucky day)
- **Daily life (4)**: {室内履|しつないば}き (indoor shoes), {鼻紙|はながみ} (tissue paper), {氷嚢|ひょうのう} (ice bag), {洋食器|ようしょっき} (Western tableware)
- **Finance / business (4)**: {公債|こうさい} (government bond), {相場師|そうばし} (speculator), {量産品|りょうさんひん} (mass-produced product), {承継|しょうけい} (succession)
- **History / politics (3)**: {入植|にゅうしょく} (settlement/colonization), {官営|かんえい} (government-operated), {皇宮|こうぐう} (imperial palace)
- **Geography / nature (2)**: {高山|こうざん} (high mountain), {側溝|そっこう} (roadside gutter)
- **Medical (1)**: {心停止|しんていし} (cardiac arrest)
- **Society (2)**: {元締|もとじ}め (boss/ringleader), {剥奪感|はくだつかん} (sense of deprivation)
- **Other (5)**: {殺虫|さっちゅう} (insect extermination), {遺骸|いがい} (remains/corpse), {乳牛|にゅうぎゅう} (dairy cow), {貨物車|かもつしゃ} (freight car), {速歩|そくほ} (fast walking/trot)
- Conjugation tables auto-generated for 2 suru verb entries
- 1 new kanji added to index: 嚢
- Removed 25 candidates that became entries

Total entries: 24,541 → 24,566.

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
