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

### 2026-04-29 (Vocabulary Expansion - 25 New Entries, Batch 62)
Added 25 new dictionary entries (IDs 26146-26170) from candidate_words.json. Mixed batch covering daily life, business, culture, health, and modern technology.

- **Food/culture (2)**: {柏|かしわ} (oak leaf / chicken in Kansai), お{惣菜屋|そうざいや} (deli, prepared-food shop)
- **Business/finance (5)**: {稟議書|りんぎしょ} (approval document), {着金|ちゃっきん} (payment received), {価格上昇|かかくじょうしょう} (price increase), {部品代|ぶひんだい} (parts cost), {印刷会社|いんさつがいしゃ} (printing company)
- **Technology/modern life (3)**: キャッシュレス{決済|けっさい} (cashless payment), オンライン{取引|とりひき} (online transaction), {重低音|じゅうていおん} (deep bass)
- **Health/body (2)**: {便|べん} (stool), {半月板|はんげつばん} (meniscus)
- **Transportation (3)**: {車内広告|しゃないこうこく} (in-train ads), {移動距離|いどうきょり} (travel distance), {走行速度|そうこうそくど} (travel speed)
- **Daily life/practical (5)**: {建築中|けんちくちゅう} (under construction), {巻|ま}き{取|と}り (winding/reeling), {連|つ}れて{帰|かえ}る (bring someone home), {淡|あわ}い{色|いろ} (pale color), {適正使用|てきせいしよう} (proper use)
- **Language/culture (3)**: こいつら (these guys), {色欲|しきよく} (lust), ネガ (negative film/pessimistic)
- **Education (1)**: {発声練習|はっせいれんしゅう} (vocal practice)
- **Counter (1)**: {一通|いっつう} (one letter/document)
- Conjugation tables auto-generated for 4 suru-verb entries
- 25 candidates synced from candidate list

Total entries: 25,938 → 25,963.

### 2026-04-29 (Vocabulary Expansion - 21 New Entries, Batch 61)
Added 21 new dictionary entries (IDs 26125-26145) from candidate_words.json. Diverse batch covering psychology, cooking, science, medicine, law, history, and grammar.

- **Psychology/cognition (2)**: {内観|ないかん} (introspection), {妄想癖|もうそうへき} (habit of fantasizing)
- **Cooking/food (4)**: {丸揚|まるあ}げ (whole deep-frying), {醤油焼|しょうゆや}き (soy sauce grilling), {丸煮|まるに} (simmered whole), {生豆|なままめ} (raw/green beans)
- **Science/geology (2)**: {火成岩|かせいがん} (igneous rock), {変成岩|へんせいがん} (metamorphic rock)
- **Medical (3)**: {低体温症|ていたいおんしょう} (hypothermia), {癒合|ゆごう} (bone healing/fusion), {抗菌薬|こうきんやく} (antibacterial drug)
- **Law/politics (3)**: {不敬罪|ふけいざい} (lese-majeste), {免官|めんかん} (dismissal from office), {脱会|だっかい} (withdrawal from organization)
- **Practical/daily life (3)**: {防寒具|ぼうかんぐ} (cold-weather gear), {国名|こくめい} (country name), {操業中|そうぎょうちゅう} (in operation)
- **Education/grammar (1)**: {普通体|ふつうたい} (plain style)
- **Culture/history (1)**: {孔子|こうし} (Confucius)
- **Other (2)**: {救助者|きゅうじょしゃ} (rescuer), {相対性|そうたいせい} (relativity)
- Conjugation tables auto-generated for 4 suru-verb entries
- 21 candidates synced from candidate list

Total entries: 25,917 → 25,938.

### 2026-04-29 (Vocabulary Expansion - 30 New Entries, Batch 60)
Added 30 new dictionary entries (IDs 26095-26124) from candidate_words.json. Mixed batch covering politics, food, language, business, travel, culture, and daily life topics.

- **Verbs (3)**: {好|す}かれる (to be liked), {腹|はら}{減|へ}る (to be hungry, casual), {規模|きぼ}{拡大|かくだい}する (to scale up)
- **Food/culture (3)**: {炒|い}り{卵|たまご} (scrambled eggs), {和食器|わしょっき} (Japanese tableware), {仲居|なかい}さん (ryokan waitress)
- **Politics/society (3)**: {急進|きゅうしん} (radicalism), {政党|せいとう}{政治|せいじ} (party politics), {成員|せいいん} (member)
- **Business/admin (5)**: {専門職|せんもんしょく} (professional occupation), {文書|ぶんしょ}{作成|さくせい} (document creation), {登録|とうろく}{番号|ばんごう} (registration number), {識別|しきべつ}{番号|ばんごう} (ID number), {消費財|しょうひざい} (consumer goods)
- **Language/education (3)**: {書|か}き{順|じゅん} (stroke order), {普通語|ふつうご} (standard language), {学生|がくせい}{生活|せいかつ} (student life)
- **Literature/science (2)**: {娯楽|ごらく}{小説|しょうせつ} (popular fiction), {空想|くうそう}{科学|かがく} (science fiction)
- **Travel/transport (2)**: {出発|しゅっぱつ}ロビー (departure lobby), {専用車|せんようしゃ} (dedicated vehicle)
- **Daily life/tech (5)**: {料理法|りょうりほう} (cooking method), {説明図|せつめいず} (explanatory diagram), {転送先|てんそうさき} (forwarding destination), {交換|こうかん}{部品|ぶひん} (replacement part), {表示板|ひょうじばん} (display board)
- **Other (4)**: {年間|ねんかん}{予定|よてい} (annual schedule), {発光体|はっこうたい} (luminous body), {趣味人|しゅみじん} (hobbyist), {性行為|せいこうい} (sexual activity)
- Conjugation tables auto-generated for 6 verb entries (3 godan, 1 ichidan, 2 suru)
- Removed 2 stale candidates (思い遣る variant of existing 思いやる, 嫌な variant of existing 嫌)
- 30 candidates synced from candidate list

Total entries: 25,887 → 25,917.

### 2026-04-29 (Vocabulary Expansion - 30 New Entries, Batch 59)
Added 30 new dictionary entries (IDs 26065-26094) from candidate_words.json. Mixed batch of practical vocabulary, expressions, and onomatopoeia for intermediate learners.

- **Expressions (8)**: {影響|えいきょう}を{与|あた}える (to influence), {左右|さゆう}される (to be swayed), {目|め}を{覚|さ}ます (to wake up / come to senses), けちをつける (to find fault / jinx), {工夫|くふう}を{凝|こ}らす (to devise cleverly), {時間|じかん}がかかる (to take time), {楽|らく}になる (to become easier), {冗談|じょうだん}を{言|い}う (to joke)
- **Nouns (11)**: {総合病院|そうごうびょういん} (general hospital), {長期休暇|ちょうききゅうか} (long vacation), {害悪|がいあく} (harm), {始発駅|しはつえき} (starting station), {最高気温|さいこうきおん} (highest temperature), {問題解決|もんだいかいけつ} (problem solving), {一割|いちわり} (10%), {話題性|わだいせい} (newsworthiness), {時間制限|じかんせいげん} (time limit), {記録映画|きろくえいが} (documentary), {選挙運動|せんきょうんどう} (election campaign)
- **Nouns continued (4)**: {最終段階|さいしゅうだんかい} (final stage), {視覚障害|しかくしょうがい} (visual impairment), {人生哲学|じんせいてつがく} (philosophy of life), {火鍋|ひなべ} (Chinese hot pot)
- **Adverbs (3)**: {故意|こい}に (intentionally), {勢|いきお}いよく (vigorously), じっと{見|み}る (to stare fixedly)
- **Onomatopoeia (2)**: ぽんぽん (tapping / in succession / tummy), ぷくぷく (plump / bubbling)
- **Adjective-no (2)**: {極小|きょくしょう} (extremely small), {可燃|かねん} (flammable)
- Conjugation table auto-generated for 1 suru-verb entry
- Removed 5 stale candidates (duplicates/variants of existing entries)
- 30 candidates synced from candidate list

Total entries: 25,857 → 25,887.

### 2026-04-28 (Vocabulary Expansion - 30 New Entries, Batch 58)
Added 30 new dictionary entries (IDs 26005-26034) from candidate_words.json. Varied batch of practical vocabulary for intermediate learners.

- **Expressions (1)**: {目|め}をつぶる (to close one's eyes / to overlook)
- **People/education (3)**: {優等生|ゆうとうせい} (honor student), {見知|みし}らぬ{人|ひと} (stranger), {人物像|じんぶつぞう} (character profile)
- **Culture/history (4)**: {鍛冶屋|かじや} (blacksmith), {銘文|めいぶん} (inscription), {町工場|まちこうば} (small factory), {昔日|せきじつ} (former times)
- **Anonymous reference (2)**: {某社|ぼうしゃ} (a certain company), {某所|ぼうしょ} (a certain place)
- **Body/health (3)**: {涙腺|るいせん} (tear gland), {声|こえ}がれ (hoarseness), {低血糖|ていけっとう} — skipped, not in final set
- **Nature/seasons (2)**: {初秋|しょしゅう} (early autumn), {巣箱|すばこ} (nest box)
- **Action/observation (2)**: {盗|ぬす}み{見|み} (sneaking a look), {覗|のぞ}き{見|み} (peeking)
- **Abstract/academic (3)**: {相反|あいはん} (contradiction), {慎重|しんちょう}さ (prudence), {跡形|あとかた} (trace)
- **Practical/daily life (5)**: {手作|てづく}り{感|かん} (handmade feel), {内容物|ないようぶつ} (contents), {抜|ぬ}き{打|う}ち (surprise inspection), {専門外|せんもんがい} (outside one's specialty), {資格証|しかくしょう} (qualification certificate)
- **Science/tech (3)**: {巨大化|きょだいか} (becoming enormous), {断電|だんでん} (power outage), {桁数|けたすう} (number of digits)
- **Other (2)**: {格上|かくじょう} (upgrading), よもやま{話|ばなし} (miscellaneous chat), {宇宙船|うちゅうせん} (spaceship)
- Conjugation tables auto-generated for 6 suru-verb entries
- 30 candidates synced from candidate list

Total entries: 25,797 → 25,827.

### 2026-04-28 (Vocabulary Expansion - 30 New Entries, Batch 57)
Added 30 new dictionary entries (IDs 25959-25988) from candidate_words.json. Diverse batch of useful vocabulary for intermediate learners including expressions, cultural terms, travel/transport vocabulary, and language-related words.

- **Expressions (5)**: よろしければ (if you don't mind), {岐路|きろ}に{立|た}つ (to stand at a crossroads), {衝撃|しょうげき}を{受|う}ける (to be shocked), とにもかくにも (at any rate), あれやこれや (this and that)
- **Travel/transport (5)**: {宿泊費|しゅくはくひ} (accommodation costs), {旅行会社|りょこうがいしゃ} (travel agency), {寝台列車|しんだいれっしゃ} (sleeper train), {特急列車|とっきゅうれっしゃ} (limited express train), {急行列車|きゅうこうれっしゃ} (express train)
- **Language (4)**: {書|か}き{言葉|ことば} (written language), {早口言葉|はやくちことば} (tongue twister), イントネーション (intonation), スペイン{語|ご} (Spanish language)
- **Culture (2)**: {七夕祭|たなばたまつ}り (Tanabata festival), {鼓|つづみ} (hand drum)
- **Politics/society (3)**: {問題提起|もんだいていき} (raising an issue), {標榜|ひょうぼう} (professing/claiming), {党員|とういん} (party member)
- **Body/health (2)**: {鼓膜|こまく} (eardrum), {呻|うめ}き{声|ごえ} (groan)
- **Other (9)**: {後知恵|あとぢえ} (hindsight), {出張費|しゅっちょうひ} (business trip expenses), {年齢層|ねんれいそう} (age group), {合格点|ごうかくてん} (passing score), {名物料理|めいぶつりょうり} (local specialty dish), あちらこちら (here and there), {結論|けつろん}づける (to conclude), {緑地|りょくち} (green space), バランス{感覚|かんかく} (sense of balance)
- Conjugation tables auto-generated for 3 verb entries (2 suru, 1 ichidan)
- 1 new kanji added to index: 榜
- Removed 3 stale candidates (洗練された duplicate, 苦虫をかみつぶしたよう variant, 年中行事 variant reading)
- 30 candidates synced from candidate list

Total entries: 25,751 → 25,781.

### 2026-04-28 (Vocabulary Expansion - 16 New Entries, Batch 57)
Added 16 new dictionary entries (IDs 25989-26004) from candidate_words.json. Curated batch of useful vocabulary spanning multiple domains.

- **Culture/arts (2)**: {話芸|わげい} (art of storytelling), {再結成|さいけっせい} (reunion/reforming of a group)
- **Spatial/physical (3)**: {下段|げだん} (lower level/low guard), {砂岩|さがん} (sandstone), {経線|けいせん} (meridian)
- **Practical/daily life (4)**: {常用薬|じょうようやく} (regular medication), {肌質|はだしつ} (skin type), {相乗|あいの}り (ride-sharing), {売札|うりふだ} (price tag)
- **Academic/technical (2)**: {導出|どうしゅつ} (derivation), {数列|すうれつ} (number sequence)
- **Society/evaluation (3)**: {無冠|むかん} (uncrowned/titleless), {無回答|むかいとう} (no answer), {風波|ふうは} (trouble/discord)
- **Other (2)**: {紙片|しへん} (scrap of paper), {再刊|さいかん} (republication)
- Conjugation tables auto-generated for 4 suru-verb entries
- 15 candidates synced from candidate list

Total entries: 25,781 → 25,797.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
