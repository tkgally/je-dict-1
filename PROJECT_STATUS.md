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

### 2026-04-22 (Vocabulary Expansion - 30 New Entries, Batch 22)
Added 30 new dictionary entries (IDs 24963-24992) from candidate_words.json. Diverse batch covering culture, food, science, professions, language, and daily life vocabulary.

- **Culture / religion (5)**: {一寸法師|いっすんぼうし} (Issun-bōshi folk tale), {禰宜|ねぎ} (Shinto priest), {仏具|ぶつぐ} (Buddhist altar fittings), {義侠心|ぎきょうしん} (chivalrous spirit), {融通無碍|ゆうずうむげ} (unhindered flexibility)
- **Food / cooking (3)**: {粕汁|かすじる} (sake lees soup), {餅粉|もちこ} (glutinous rice flour), {莢|さや} (pod/shell)
- **Science / tech (3)**: {不活性|ふかっせい} (inertness), {伝導|でんどう} (conduction), {梅雨前線|つゆぜんせん} (seasonal rain front)
- **Professions / government (3)**: {建築士|けんちくし} (architect), {補佐官|ほさかん} (aide/adviser), {乗員|じょういん} (crew member)
- **Arts / craft (3)**: {彫金|ちょうきん} (metal engraving), {活版|かっぱん} (letterpress), {幻術|げんじゅつ} (illusionism)
- **Language / reference (2)**: {見出|みだ}し{語|ご} (headword/lemma), {客観視|きゃっかんし} (objective viewpoint)
- **Body / description (1)**: {中肉中背|ちゅうにくちゅうせい} (medium build)
- **Housing (1)**: {床下|ゆかした} (under the floor)
- **Education / society (3)**: {受験料|じゅけんりょう} (exam fee), {共同生活|きょうどうせいかつ} (communal living), {席次|せきじ} (seating order)
- **Expressions / abstract (3)**: {若気の至り|わかげのいたり} (youthful indiscretion), {無二|むに} (peerless), {深考|しんこう} (deep thought)
- **History / military (2)**: {兵営|へいえい} (barracks), {通話中|つうわちゅう} (on a call)
- Conjugation tables auto-generated for 5 suru verb entries
- 3 new kanji added to index: 碍, 禰, 莢
- 30 candidates synced from candidate list

Total entries: 24,760 → 24,790.

### 2026-04-21 (Vocabulary Expansion - 25 New Entries, Batch 21)
Added 25 new dictionary entries (IDs 24938-24962) from candidate_words.json. Thematic batch covering health/medical, daily life/travel, Japan-specific culture, business/legal, and technical vocabulary.

- **Health / medical (3)**: {禁断症状|きんだんしょうじょう} (withdrawal symptoms), {予防医療|よぼういりょう} (preventive medicine), {姿勢矯正|しせいきょうせい} (posture correction)
- **Daily life / travel (5)**: {電話予約|でんわよやく} (phone reservation), {荷物置|にもつお}き{場|ば} (luggage storage area), クーポン{券|けん} (coupon), グリーン{券|けん} (green car ticket), {貴重品入|きちょうひんい}れ (valuables locker)
- **Japan-specific culture (4)**: {耐震設計|たいしんせっけい} (earthquake-resistant design), {精進弁当|しょうじんべんとう} (vegetarian bento), {山葵漬|わさびづ}け (wasabi pickles), {襖紙|ふすまがみ} (fusuma paper)
- **Business / legal (5)**: {提携店|ていけいてん} (partner store), {子会社化|こがいしゃか} (subsidiarization), {被選挙権|ひせんきょけん} (right to run for office), {除籍|じょせき} (removal from register), {私文書|しぶんしょ} (private document)
- **Technical / practical (3)**: {予備電源|よびでんげん} (backup power source), {手信号|てしんごう} (hand signal), {耐震強度|たいしんきょうど} (seismic strength)
- **Other (5)**: {連載終了|れんさいしゅうりょう} (end of serialization), {奇妙|きみょう}さ (strangeness), {努力給|どりょくきゅう} (effort-based pay), {限定免許|げんていめんきょ} (restricted license), {旧校舎|きゅうこうしゃ} (old school building)
- 25 candidates synced from candidate list

Total entries: 24,735 → 24,760.

### 2026-04-21 (Vocabulary Expansion - 24 New Entries, Batch 20)
Added 24 new dictionary entries (IDs 24914-24937) from candidate_words.json. Mixed batch covering health/beauty, society, education, finance, food, science, and daily life vocabulary.

- **Health / beauty (3)**: {脱毛|だつもう} (hair removal/loss), {除毛|じょもう} (surface hair removal), {幻聴|げんちょう} (auditory hallucination)
- **Society / people (4)**: {蹂躙|じゅうりん} (trampling/violation), {放浪者|ほうろうしゃ} (wanderer), {支援者|しえんしゃ} (supporter), {最強者|さいきょうしゃ} (the strongest)
- **Education (1)**: {定期試験|ていきしけん} (regular exam)
- **Finance / commerce (3)**: {借金返済|しゃっきんへんさい} (debt repayment), {掛|か}け{金|きん} (premium/stake), {現在価格|げんざいかかく} (current price)
- **Food / science (3)**: {加水|かすい} (adding water), {注水|ちゅうすい} (water injection), {食品保存|しょくひんほぞん} (food preservation)
- **Health / fitness (2)**: {運動量|うんどうりょう} (amount of exercise), {異常値|いじょうち} (abnormal value)
- **Daily life / expressions (4)**: {気分|きぶん}が{悪|わる}い (feel sick/bad), ご{自宅|じたく} (your home, honorific), {携帯品|けいたいひん} (personal belongings), {最弱|さいじゃく} (weakest)
- **Na-adjectives (2)**: {抵抗的|ていこうてき} (resistant/defiant), {感性的|かんせいてき} (emotional/aesthetic)
- **Government / travel (2)**: {入国管理局|にゅうこくかんりきょく} (immigration bureau), {連勝記録|れんしょうきろく} (winning streak record)
- Conjugation tables auto-generated for 4 suru verb entries
- 2 new kanji added to index: 蹂, 躙
- 24 candidates synced from candidate list

Total entries: 24,711 → 24,735.

### 2026-04-21 (Vocabulary Expansion - 20 New Entries, Batch 19)
Added 20 new dictionary entries (IDs 24894-24913) from candidate_words.json. Mixed batch covering community life, culture, science, law, language, and daily vocabulary.

- **Community / daily life (4)**: {町会|ちょうかい} (neighborhood association), {掃除用具|そうじようぐ} (cleaning tools), {都外|とがい} (outside Tokyo), {予約券|よやくけん} (reservation ticket)
- **Food / culture (2)**: {切り餅|きりもち} (block mochi), {趣向|しゅこう} (creative twist)
- **Science / environment (3)**: {寒冷化|かんれいか} (cooling/climate shift), {炭素排出|たんそはいしゅつ} (carbon emissions), {推力|すいりょく} (thrust)
- **Technology (1)**: ショートする (to short-circuit)
- **Law / religion / philosophy (3)**: {制定法|せいていほう} (statute law), {常住|じょうじゅう} (permanence/permanent residence), {色情|しきじょう} (lust/sensuality)
- **Language / literature (2)**: {典故|てんこ} (classical allusion), {発行所|はっこうしょ} (publishing office)
- **History / nature (2)**: {軍馬|ぐんば} (war horse), {波面|はめん} (wave surface)
- **Expressions (2)**: {交換券|こうかんけん} (exchange coupon), ふくれっつら (sulky face), {経過点|けいかてん} (waypoint/milestone)
- Conjugation tables auto-generated for 3 suru verb entries
- Removed 1 stale candidate (博士号 はかせごう, variant of existing entry 16350)
- 20 candidates synced from candidate list

Total entries: 24,691 → 24,711.

### 2026-04-21 (Vocabulary Expansion - 22 New Entries, Batch 18)
Added 22 new dictionary entries (IDs 24872-24893) from candidate_words.json. Mixed batch covering social/cultural concepts, education, politics, infrastructure, health, sports, and practical vocabulary.

- **Social / cultural (3)**: {嫌|きら}われる (to be disliked), {報|むく}われない (unrewarded), {通過儀礼|つうかぎれい} (rite of passage)
- **Education / research (4)**: {黒板消|こくばんけ}し (blackboard eraser), {試験監督|しけんかんとく} (exam proctor), {採点者|さいてんしゃ} (grader), {聞|き}き{取|と}り{調査|ちょうさ} (interview survey)
- **Politics / government (3)**: {超大国|ちょうたいこく} (superpower), {出入国|しゅつにゅうこく} (immigration/emigration), {禁止解除|きんしかいじょ} (lifting a ban)
- **Math / business (2)**: {概数|がいすう} (approximate number), {加算|かさん} (addition/surcharge)
- **Infrastructure / tech (3)**: {配電盤|はいでんばん} (electrical panel), {送風機|そうふうき} (blower), {焼却場|しょうきゃくじょう} (incineration plant)
- **Transport / urban (2)**: {停留|ていりゅう} (stopping), {通過点|つうかてん} (waypoint/milestone)
- **Nature / health / sports (3)**: {植栽|しょくさい} (planting/landscaping), {扁平足|へんぺいそく} (flat feet), {陸上選手|りくじょうせんしゅ} (track athlete)
- **Other (2)**: {助言者|じょげんしゃ} (advisor), {音楽隊|おんがくたい} (band/music corps)
- Conjugation tables auto-generated for 6 suru verbs and 1 ichidan verb, 1 i-adjective
- 1 new kanji added to index: 扁
- 22 candidates removed from candidate list

Total entries: 24,669 → 24,691.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
