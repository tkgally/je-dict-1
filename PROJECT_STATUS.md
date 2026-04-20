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

### 2026-04-19 (Vocabulary Expansion - 20 New Entries, Batch 5)
Added 20 new dictionary entries (IDs 24539-24558) from candidate_words.json. A diverse batch covering conflict/diplomacy, law enforcement, weather/geography, arts/culture, and practical vocabulary.

- **War / diplomacy (2)**: {停戦|ていせん} (ceasefire), {講和|こうわ} (peace treaty)
- **Law enforcement (3)**: {署長|しょちょう} (station chief), {警部|けいぶ} (police inspector), {弁論|べんろん} (oral argument/debate)
- **Weather / geography (3)**: {風速|ふうそく} (wind speed), {雨量|うりょう} (rainfall), {岩礁|がんしょう} (reef)
- **Nature / places (2)**: {川岸|かわぎし} (riverbank), {花園|はなぞの} (flower garden)
- **Arts / culture (2)**: {舞踏|ぶとう} (dance/ball), {世俗|せぞく} (worldly/secular)
- **Construction / materials (2)**: {鉄骨|てっこつ} (steel frame), {塗料|とりょう} (paint/coating)
- **Descriptive (3)**: {潤沢|じゅんたく} (abundant), {突出|とっしゅつ} (protruding/outstanding), {可憐|かれん} (lovely/pitiful)
- **Other (3)**: {搬送|はんそう} (transport), {不断|ふだん} (constant), {覇者|はしゃ} (champion)

Total entries: 24,336 → 24,356.

### 2026-04-19 (Vocabulary Expansion - 30 New Entries, Batch 4)
Added 30 new dictionary entries (IDs 24509-24538) from candidate_words.json. Diverse batch covering health/medicine, business/finance, culture, education, nature/science, and daily life.

- **Health / medicine (4)**: {動脈硬化|どうみゃくこうか} (arteriosclerosis), {高血糖|こうけっとう} (high blood sugar), {降圧薬|こうあつやく} (antihypertensive drug), {抗加齢|こうかれい} (anti-aging)
- **Business / finance (3)**: {終身雇用制|しゅうしんこようせい} (lifetime employment), {貸借対照表|たいしゃくたいしょうひょう} (balance sheet), {損益計算書|そんえきけいさんしょ} (income statement)
- **Society / politics (4)**: デモ{行進|こうしん} (demonstration march), {訪問介護|ほうもんかいご} (home care), {福祉施設|ふくししせつ} (welfare facility), {男女別学|だんじょべつがく} (single-sex education)
- **Nature / science (3)**: {海洋生物|かいようせいぶつ} (marine life), {雑食動物|ざっしょくどうぶつ} (omnivore), {鍾乳石|しょうにゅうせき} (stalactite)
- **Culture / arts (5)**: フランス{語|ご} (French language), フランス{料理|りょうり} (French cuisine), クラシック{音楽|おんがく} (classical music), {吟詠|ぎんえい} (poetry chanting), {内面描写|ないめんびょうしゃ} (psychological depiction)
- **Daily life (4)**: {判断|はんだん}ミス (judgment error), {黄色信号|きいろしんごう} (yellow light / warning sign), {新居祝|しんきょいわ}い (housewarming gift), {世界各地|せかいかくち} (various places worldwide)
- **Emotion / character (2)**: {徒労感|とろうかん} (sense of futility), おどけ{者|もの} (joker/clown)
- **Other (5)**: {不品行|ふひんこう} (misconduct), {優秀作|ゆうしゅうさく} (excellent work), {要領|ようりょう}よく (efficiently), {直方体|ちょくほうたい} (cuboid), {佳品|かひん} (fine article)

Total entries: 24,306 → 24,336.


### 2026-04-19 (Vocabulary Expansion - 25 New Entries, Batch 2)
Added 25 new dictionary entries (IDs 24454-24478) from candidate_words.json. A diverse batch with good variety across practical daily life, cultural, business, and academic vocabulary.

- **Cultural (4)**: {朱印|しゅいん} (red seal stamp), {賽銭箱|さいせんばこ} (offertory box), {友引|ともびき} (rokuyo calendar day), お{食|く}い{初|ぞ}め (baby's first meal ceremony)
- **Business / workplace (4)**: フレックスタイム (flextime), {添付|てんぷ}ファイル (email attachment), {法的|ほうてき}{措置|そち} (legal action), {来訪|らいほう}{者|しゃ} (visitor)
- **Education / communication (4)**: {生徒|せいと}{会長|かいちょう} (student council president), {口頭|こうとう}{発表|はっぴょう} (oral presentation), {言語|げんご}{交換|こうかん} (language exchange), {文学|ぶんがく}{作品|さくひん} (literary work)
- **Daily life / practical (3)**: {満|まん}タン (full tank), できるだけ{早|はや}く (ASAP), {広報|こうほう}{誌|し} (newsletter)
- **Formal vocabulary (4)**: {未了|みりょう} (pending/unfinished), {不可分|ふかぶん} (indivisible), {誤認|ごにん} (misidentification), {予期|よき}せず (unexpectedly)
- **Nature / science (1)**: {自然|しぜん}{現象|げんしょう} (natural phenomenon)
- **Emotions / literature (1)**: むせび{泣|な}く (to sob)
- **People (1)**: {門番|もんばん} (gatekeeper)
- **Math / finance (1)**: {切|き}り{上|あ}げ (rounding up / revaluation)
- **Idiom (1)**: タヌキ{寝入|ねい}り (pretending to be asleep)
- **Keigo (1)**: ご{来店|らいてん} (visiting a store, honorific)
- Conjugation tables auto-generated for 7 verb entries (5 suru, 2 godan)

Total entries: 24,251 → 24,276.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
