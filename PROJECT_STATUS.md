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

### 2026-04-19 (Vocabulary Expansion - 30 New Entries, Batch 3)
Added 30 new dictionary entries (IDs 24479-24508) from candidate_words.json. A diverse batch covering daily life, cultural practices, education, food, and practical vocabulary.

- **Cultural / religious (3)**: {御霊前|ごれいぜん} (condolence offering), {香典袋|こうでんぶくろ} (condolence envelope), {盂蘭盆会|うらぼんえ} (Obon festival)
- **Education (3)**: {経済学部|けいざいがくぶ} (faculty of economics), {理学部|りがくぶ} (faculty of science), {工学部|こうがくぶ} (faculty of engineering)
- **Food / cooking (2)**: {寿司酢|すしず} (sushi vinegar), {穀物酢|こくもつす} (grain vinegar)
- **Daily life / practical (5)**: {家具店|かぐてん} (furniture store), {停車中|ていしゃちゅう} (stopped/parked), {遺失届|いしつとどけ} (lost property report), {日付印|ひづけいん} (date stamp), {自動販売|じどうはんばい} (automatic vending)
- **Social / drinking culture (2)**: {二軒目|にけんめ} (second bar/stop), {秘密話|ひみつばなし} (secret talk)
- **People (2)**: {応援者|おうえんしゃ} (supporter), {泳者|えいしゃ} (swimmer)
- **Business (2)**: {会議所|かいぎしょ} (chamber of commerce), {先行発売|せんこうはつばい} (advance sale)
- **Language/grammar patterns (3)**: {諸問題|しょもんだい} (various problems), {低|ひく}め (somewhat low), {数軒|すうけん} (several houses)
- **Legal (1)**: {保釈金|ほしゃくきん} (bail money)
- **Loanwords (3)**: バン (van), ワンピ (dress), インスリン (insulin)
- **Culture / martial arts (1)**: {抜刀|ばっとう} (drawing a sword)
- **Descriptive (1)**: {波状|はじょう} (wavy/undulating)
- **Animals (1)**: {仔猫|こねこ} (kitten)
- **Multi-sense (1)**: {先付|さきづ}け (postdating / kaiseki appetizer)
- 3 new kanji added to index: 仔, 盂, 蘭

Total entries: 24,276 → 24,306.

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

### 2026-04-19 (Vocabulary Expansion - 25 New Entries)
Added 25 new dictionary entries (IDs 24429-24453) from candidate_words.json. A diverse batch covering nature, culture, food, disaster terminology, workplace vocabulary, and technical terms.

- **Disaster / weather (2)**: {雪害|せつがい} (snow damage), {半焼|はんしょう} (partial fire damage)
- **Culture / history (4)**: {侠客|きょうかく} (chivalrous outlaw), {門人|もんじん} (disciple), {神霊|しんれい} (divine spirit), {正字|せいじ} (orthodox kanji form)
- **Workplace / society (3)**: {訓告|くんこく} (official reprimand), {属人|ぞくじん} (person-dependent), {世故|せこ} (worldly wisdom)
- **Infrastructure / tech (3)**: {配水|はいすい} (water distribution), {防壁|ぼうへき} (defensive wall), {圧送|あっそう} (pressure pumping)
- **Nature / agriculture (3)**: {花芯|かしん} (flower center), {育苗|いくびょう} (raising seedlings), {発根|はっこん} (root emergence)
- **Food (1)**: {半生|はんなま} (half-raw/medium-rare)
- **People / culture (3)**: {俊才|しゅんさい} (prodigy), {曲芸師|きょくげいし} (acrobat), {見舞金|みまいきん} (sympathy money)
- **Body / language (2)**: {禿|はげ} (baldness), {糞|ふん} (dung/droppings)
- **Aesthetics / morality (2)**: {絶美|ぜつび} (exquisite beauty), {清白|せいはく} (purity/innocence)
- **Medical (1)**: {昏倒|こんとう} (fainting/collapse)
- **Logistics (1)**: {船荷|ふなに} (ship cargo)
- Also removed 2 stale candidates (粉骨砕身する, 羽化する — both already exist as entries)
- 1 new kanji added to index: 糞
- Conjugation tables auto-generated for 7 suru-verb entries

Total entries: 24,226 → 24,251.

### 2026-04-19 (Vocabulary Expansion - 24 New Entries)
Added 24 new dictionary entries (IDs 24404-24428, excluding 24427 which was a duplicate) from candidate_words.json. This batch focuses on common loanwords and practical vocabulary useful for intermediate learners.

- **Technology (5)**: ディスク (disk), デスクトップ (desktop), フォルダー (folder), ミラーレス (mirrorless camera), ポート (port/connector)
- **Daily life (3)**: ランドリー (laundry/laundromat), コインパーキング (pay parking lot), ルームメイト (roommate)
- **Education (3)**: チョーク (chalk), ロールプレイ (role play), ゼミナール (seminar)
- **Sports (2)**: メダリスト (medalist), キーパー (goalkeeper)
- **Media / culture (3)**: ナレーション (narration), キリスト (Christ), グレー (gray/gray area)
- **General vocabulary (5)**: ランク (rank), リーフレット (leaflet), インターン (internship), インナー (innerwear), スプリング (spring)
- **Math (1)**: {百分率|ひゃくぶんりつ} (percentage)
- Also removed 1 stale candidate ({能力給|のうりょくきゅう}, duplicate of existing entry)
- All entries follow v2 standards with structured notes, collocations, similar words, and full furigana

Total entries: 24,202 → 24,226.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
