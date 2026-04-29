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

### 2026-04-28 (Vocabulary Expansion - 28 New Entries, Batch 56)
Added 28 new dictionary entries (IDs 25931-25958) from candidate_words.json. Mix of na-adjectives (～的), compound nouns, loanwords, and an adverb useful for intermediate learners.

- **Na-adjectives with 的 (10)**: {感動的|かんどうてき} (moving), {挑戦的|ちょうせんてき} (challenging/provocative), {戦略的|せんりゃくてき} (strategic), {都会的|とかいてき} (urban/cosmopolitan), {魅惑的|みわくてき} (enchanting), {敵対的|てきたいてき} (hostile), {空想的|くうそうてき} (fanciful/visionary), {創作的|そうさくてき} (creative), {反発的|はんぱつてき} (resistant/defiant), {反逆的|はんぎゃくてき} (rebellious)
- **Compound nouns (13)**: {中古車|ちゅうこしゃ} (used car), {牢獄|ろうごく} (prison/dungeon), {防波堤|ぼうはてい} (breakwater), {食料費|しょくりょうひ} (food expenses), {郵便局員|ゆうびんきょくいん} (postal clerk), {衝撃波|しょうげきは} (shock wave), {緊急警報|きんきゅうけいほう} (emergency alert), {木管楽器|もっかんがっき} (woodwind instrument), {覗|のぞ}き{穴|あな} (peephole), {最低気温|さいていきおん} (minimum temperature), {画像認識|がぞうにんしき} (image recognition), {原始時代|げんしじだい} (prehistoric times), {情報機器|じょうほうきき} (IT equipment)
- **Loanwords (2)**: バケツリレー (bucket relay), フィルタリング (filtering)
- **Other (3)**: {学術会議|がくじゅつかいぎ} (academic conference), {立体映像|りったいえいぞう} (3D image), {刻々|こっこく}と (moment by moment)
- 27 candidates synced from candidate list

Total entries: 25,723 → 25,751.

### 2026-04-28 (Vocabulary Expansion - 28 New Entries, Batch 55)
Added 28 new dictionary entries (IDs 25903-25930) from candidate_words.json. Diverse batch of expressions, cultural vocabulary, and descriptive terms useful for intermediate learners.

- **Expressions (8)**: {今日|きょう}このごろ (these days), {余|あま}すところなく (completely), {期待|きたい}に{満|み}ちる (full of anticipation), {苦虫|にがむし}を{噛|か}み{潰|つぶ}したよう (looking sour), {目|め}に{遭|あ}う (to suffer), これより (from this point on), ジロリと{見|み}る (to glare), ぴんぴんしている (lively and well)
- **Na-adjectives (2)**: {誘惑|ゆうわく}{的|てき} (tempting/seductive), {肉感|にっかん}{的|てき} (voluptuous)
- **Nouns (12)**: {周|まわ}り{中|じゅう} (all around), {秘密|ひみつ}{主義|しゅぎ} (secretiveness), {大|だい}{音響|おんきょう} (loud sound), {読|よ}み{飛|と}ばし (skimming), {小物|こもの}{入|い}れ (accessory case), {伝送|でんそう} (transmission), {御|お}{祝儀|しゅうぎ}{袋|ぶくろ} (gift envelope), {括弧|かっこ}{書|が}き (parenthetical), {預言者|よげんしゃ} (prophet), {原稿料|げんこうりょう} (manuscript fee), {金銀|きんぎん}{財宝|ざいほう} (gold and treasure), {溺死|できし} (drowning), {機嫌|きげん}{屋|や} (moody person), {五十代|ごじゅうだい} (one's fifties), {高級|こうきゅう}{料亭|りょうてい} (high-class restaurant), {脚線美|きゃくせんび} (beautiful legs)
- **Pronoun (1)**: あの{人|ひと} (that person; he/she)
- **Verb (1)**: {引|ひ}きずられる (to be dragged/swayed)
- Conjugation tables auto-generated for 4 verb entries (2 suru, 1 ichidan, 1 godan)
- Removed 2 stale candidates (出す duplicate, 世渡り下手 variant reading)
- 27 candidates synced from candidate list

Total entries: 25,695 → 25,723.


### 2026-04-27 (Vocabulary Expansion - 28 New Entries, Batch 53)
Added 28 new dictionary entries (IDs 25831-25858) from candidate_words.json. Focused batch of expressions, verbs, and cultural vocabulary useful for intermediate learners.

- **Social expressions (8)**: {気|き}を{遣|つか}う (to be considerate), {席|せき}を{外|はず}す (to step away), {顔|かお}を{立|た}てる (to save face), {恩|おん}を{売|う}る (to put someone in one's debt), {手|て}を{借|か}りる (to get help), {当|あ}てにする (to count on), {気|き}が{済|す}む (to be satisfied), お{茶|ちゃ}を{濁|にご}す (to be evasive)
- **Verbs (5)**: {引|ひ}き{戻|もど}す (to pull back), おもねる (to flatter), {思|おも}いやる (to empathize), しくじる (to fail/blunder), あやかる (to share in good fortune)
- **Expressions/adverbs (7)**: {思|おも}い{通|どお}り (as one wishes), {思|おも}うがまま (as one pleases), いかにして (how; by what means), たかが (merely; at most), そぐわない (to not suit), {腑|ふ}に{落|お}ちない (to not make sense), {身|み}を{乗|の}り{出|だ}す (to lean forward eagerly)
- **Cultural (3)**: {心|こころ}を{無|む}にする (to clear one's mind), {物心|ものごころ}つく (to reach age of awareness), {故郷|こきょう}を{離|はな}れる (to leave hometown)
- **Nouns (3)**: {滞留|たいりゅう} (stagnation/lingering), {傍点|ぼうてん} (emphasis dots), {目障|めざわ}り (eyesore)
- **Other (2)**: ぐずぐずする (to dawdle), {頭|あたま}を{柔|やわ}らかくする (to think flexibly)
- Conjugation tables auto-generated for 7 verb entries (5 godan, 2 suru)
- Removed 1 stale candidate (残存/ざんそん, variant of existing ざんぞん entry)
- 11 candidates synced from candidate list

Total entries: 25,623 → 25,651.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
