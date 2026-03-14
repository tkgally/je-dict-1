# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-14
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
| Total entries | ~16,783 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,984 (open) |
| Candidate words | ~2,996 |
| Cross-references | ~3,400 |
| Example sentences | ~50,000 |
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

### 2026-03-14 (Vocabulary Expansion - 45 New Entries, Session 429)
Added 45 new dictionary entries (IDs 16689-16733) from candidate_words.json:

- **Nouns (19)**: {北極|ほっきょく} (North Pole), {仲人|なこうど} (matchmaker), {役場|やくば} (town hall), {家柄|いえがら} (family lineage), {寝息|ねいき} (sleeping breath), {秒読|びょうよ}み (countdown), {新記録|しんきろく} (new record), {安定感|あんていかん} (sense of stability), {稼|かせ}ぎ{時|どき} (peak earning time), {真横|まよこ} (right beside), {真向|まむ}かい (directly opposite), {難題|なんだい} (difficult problem), {成金|なりきん} (nouveau riche), {平社員|ひらしゃいん} (rank-and-file employee), {足止|あしど}め (being stranded), {口先|くちさき} (lip service), {滑舌|かつぜつ} (articulation), {神主|かんぬし} (Shinto priest), {太|ふと}もも (thigh)
- **Nouns/suru verbs (7)**: {完備|かんび} (fully equipped), {造園|ぞうえん} (landscaping), {野営|やえい} (camping), {設営|せつえい} (setting up), {終息|しゅうそく} (ending), {当惑|とうわく} (bewilderment), {節制|せっせい} (moderation)
- **Nouns/na-adj (5)**: {短命|たんめい} (short-lived), {上出来|じょうでき} (well done), {不出来|ふでき} (poorly done), {互角|ごかく} (evenly matched), {好評|こうひょう} (favorable reception)
- **Nouns + other (3)**: {後|うし}ろ{向|む}き (backward/pessimistic), {的外|まとはず}れ (off the mark), {実物大|じつぶつだい} (life-size)
- **Noun/suru verb (1)**: {酷評|こくひょう} (harsh criticism)
- **Noun/suru verb (1)**: {金縛|かなしば}り (sleep paralysis)
- **Noun/suru verb (1)**: {寝坊|ねぼう}する (to oversleep)
- **Noun/suru verb (1)**: {息抜|いきぬ}き (breather)
- **Noun (1)**: {気晴|きば}らし (diversion)
- **Noun (1)**: {初夢|はつゆめ} (first dream of year)
- **Noun (1)**: {軽|けい}トラ (kei truck)
- **Adverb (1)**: {何|なん}だか (somehow)
- **Verb (ichidan) (1)**: うなされる (to have a nightmare)
- **Verb (ichidan) (1)**: {色|いろ}あせる (to fade)
- **Verb (godan) (1)**: {買|か}い{取|と}る (to buy up)

Notable features:
- Multi-sense: {後|うし}ろ{向|む}き (2: physical + figurative), {金縛|かなしば}り (2: sleep paralysis + bound), {成金|なりきん} (2: nouveau riche + shogi), {口先|くちさき} (2: lip service + way of speaking), {色|いろ}あせる (2: physical fading + figurative)
- Antonym pairs: {上出来|じょうでき}/{不出来|ふでき}, {好評|こうひょう}/{酷評|こくひょう}
- Near-synonym pair: {息抜|いきぬ}き/{気晴|きば}らし
- Cultural: {初夢|はつゆめ}, {仲人|なこうど}, {成金|なりきん}, {神主|かんぬし}
- Body parts: {太|ふと}もも, {滑舌|かつぜつ}
- Daily life: {寝坊|ねぼう}する, {足止|あしど}め, {軽|けい}トラ

Total entries: ~16,738 → ~16,783 (approximate)
Remaining candidates: ~3,041 → ~2,996 (45 removed)

### 2026-03-14 (Vocabulary Expansion - 45 New Entries, Session 428)
Added 45 new dictionary entries (IDs 16644-16688) from candidate_words.json:

- **Nouns (28)**: {源氏|げんじ} (Genji clan), {遊女|ゆうじょ} (courtesan), {連用形|れんようけい} (continuative form), {玩具|がんぐ} (toy, formal), {日系企業|にっけいきぎょう} (Japanese company overseas), {上水道|じょうすいどう} (water supply), {一党|いっとう} (faction), {中間報告|ちゅうかんほうこく} (interim report), {収容人数|しゅうようにんずう} (capacity), {潜伏期間|せんぷくきかん} (incubation period), {直流|ちょくりゅう} (direct current), {教材費|きょうざいひ} (teaching materials cost), {自己推薦|じこすいせん} (self-recommendation), {広告媒体|こうこくばいたい} (advertising medium), {酸素|さんそ}ボンベ (oxygen tank), {事務机|じむづくえ} (office desk), {学習机|がくしゅうづくえ} (study desk), {月度|げつど} (monthly period), {本籍地|ほんせきち} (registered domicile), {種本|たねほん} (source book), {指導案|しどうあん} (lesson plan), {豆電球|まめでんきゅう} (miniature bulb), {氷菓子|こおりがし} (frozen treat), {湯沸|ゆわ}かし{器|き} (water heater), {話題作|わだいづく}り (creating buzz), {格助詞|かくじょし} (case particle), {産学連携|さんがくれんけい} (industry-academia), {聖徳太子|しょうとくたいし} (Prince Shotoku)
- **Nouns (business pair)**: {小売業|こうりぎょう} (retail trade), {卸売業|おろしうりぎょう} (wholesale trade)
- **Nouns (speed pair)**: {秒速|びょうそく} (per second), {分速|ふんそく} (per minute)
- **Nouns (other)**: {一昨日|いっさくじつ} (day before yesterday, formal), {愛想笑|あいそわら}い (forced smile), {暇|ひま}つぶし (killing time), {一時間半|いちじかんはん} (hour and a half)
- **Nouns/no-adj (3)**: {粒状|りゅうじょう} (granular), {煎|い}り{立|た}て (freshly roasted), {防|ぼう}カビ (anti-mold)
- **Na-adjective/noun (1)**: {爆安|ばくやす} (dirt cheap)
- **Pre-noun adjectival (1)**: {適|てき}した (suitable)
- **Adverbs (2)**: ああして (like that), {年々歳々|ねんねんさいさい} (year after year)
- **Verb (1)**: {見向|みむ}く (to look toward)
- **Noun (historical) (1)**: どん{尻|じり} (dead last)

Notable features:
- Multi-sense: {源氏|げんじ} (2: Minamoto clan + Tale of Genji)
- Grammar/linguistics: {連用形|れんようけい}, {格助詞|かくじょし}
- Historical/cultural: {聖徳太子|しょうとくたいし}, {源氏|げんじ}, {遊女|ゆうじょ}
- Modern life: {爆安|ばくやす}, {日系企業|にっけいきぎょう}, {話題作|わだいづく}り
- Paired entries: {小売業|こうりぎょう}/{卸売業|おろしうりぎょう}, {秒速|びょうそく}/{分速|ふんそく}, {事務机|じむづくえ}/{学習机|がくしゅうづくえ}
- New kanji: 2,543 → 2,544 (玩)

Total entries: ~16,693 → ~16,738 (approximate)
Remaining candidates: ~3,086 → ~3,041 (45 removed)

### 2026-03-14 (Vocabulary Expansion - 60 New Entries, Session 427)
Added 60 new dictionary entries (IDs 16584-16643) from candidate_words.json:

- **Nouns (30)**: マドンナ (belle), {浄瑠璃|じょうるり} (joruri), {文芸誌|ぶんげいし} (literary magazine), {各層|かくそう} (all strata), {毛髪|もうはつ} (hair), {麦芽|ばくが} (malt), {障子紙|しょうじがみ} (shoji paper), {三十代|さんじゅうだい} (one's thirties), {修士号|しゅうしごう} (master's degree), {学士号|がくしごう} (bachelor's degree), {共通語|きょうつうご} (common language), {接尾辞|せつびじ} (suffix), {接頭辞|せっとうじ} (prefix), {千円札|せんえんさつ} (1000-yen bill), {大奥|おおおく} (women's quarters), {美容液|びようえき} (beauty serum), {乾燥肌|かんそうはだ} (dry skin), インド{洋|よう} (Indian Ocean), {画伯|がはく} (master painter), {暗号資産|あんごうしさん} (crypto assets), {鵝鳥|がちょう} (goose), {猛禽類|もうきんるい} (birds of prey), {条文|じょうぶん} (text of a law), {共産主義|きょうさんしゅぎ} (communism), {民俗学|みんぞくがく} (folklore studies), {児童書|じどうしょ} (children's book), {偽札|にせさつ} (counterfeit bill), {脊髄|せきずい} (spinal cord), {学籍|がくせき} (school enrollment), {避難勧告|ひなんかんこく} (evacuation advisory)
- **Nouns/suru verbs (6)**: {搬出|はんしゅつ} (carrying out), {受粉|じゅふん} (pollination), {加圧|かあつ} (pressurization), {煮炊|にた}き (cooking), {焼|や}き{増|ま}し (reprint), {他所見|よそみ} (looking away)
- **Nouns/na-adj (3)**: {非公開|ひこうかい} (private), {近代的|きんだいてき} (modern), {充実|じゅうじつ}した (fulfilling)
- **Counter/suffix (2)**: {時間目|じかんめ} (period), {出席率|しゅっせきりつ} (attendance rate)
- **Seasonal (2)**: {春季|しゅんき} (spring season), {秋季|しゅうき} (autumn season)
- **Adverbs/adjectives (3)**: ああいう (that kind of), {密|みつ}に (closely/secretly), {対面|たいめん}で (face-to-face)
- **Compounds (5)**: {転売|てんばい}ヤー (reseller/scalper), {前々月|ぜんぜんげつ} (month before last), {布団|ふとん}カバー (futon cover), {炭酸割|たんさんわ}り (mixed with soda), {格|かく}ゲー (fighting game)
- **Verbs (2)**: {繰|く}り{戻|もど}す (to carry back), {打|う}ちつける (to strike against)
- **Expressions (3)**: っていうか (or rather), あの{方|かた} (that person polite), {五目並|ごもくなら}べ (gomoku game)
- **Education (2)**: {初等教育|しょとうきょういく} (elementary education), {借家人|しゃくやにん} (tenant)
- **Language (2)**: {広東語|かんとんご} (Cantonese), {共通語|きょうつうご} (common language)

Notable features:
- Double-sized batch: 60 entries in one session
- Multi-sense: {共通語|きょうつうご} (2: lingua franca + standard Japanese), {密|みつ}に (2: closely + secretly), {打|う}ちつける (2: strike + nail down)
- Modern vocabulary: {暗号資産|あんごうしさん}, {転売|てんばい}ヤー, {格|かく}ゲー
- Cultural: {浄瑠璃|じょうるり}, {大奥|おおおく}, {五目並|ごもくなら}べ
- New kanji: 2,539 → 2,543 (瑠, 璃, 禽, 鵝)

Total entries: ~16,633 → ~16,693 (approximate)
Remaining candidates: ~3,145 → ~3,086 (59 removed)

### 2026-03-14 (Vocabulary Expansion - 30 New Entries, Session 426)
Added 30 new dictionary entries (IDs 16554-16583) from candidate_words.json:

- **Nouns (11)**: {読者|どくしゃ} (reader), {青少年|せいしょうねん} (youth), {体型|たいけい} (body type), {接続詞|せつぞくし} (conjunction), {専業主婦|せんぎょうしゅふ} (full-time housewife), {目論見|もくろみ} (plan/scheme), {結|むす}び{目|め} (knot), {一苦労|ひとくろう} (quite a struggle), {配信者|はいしんしゃ} (streamer), {要所|ようしょ} (key point), {脱字|だつじ} (omitted character)
- **Nouns/suru verbs (6)**: {中毒|ちゅうどく} (poisoning/addiction), {登校|とうこう} (attending school), {視察|しさつ} (inspection), {徴収|ちょうしゅう} (collection/levy), {嗚咽|おえつ} (sobbing), {黙殺|もくさつ} (ignoring)
- **Nouns/na-adj (2)**: スケベ (lewd/pervert), {軽微|けいび} (slight/minor)
- **Nouns/suru verbs + na-adj (1)**: {懇談|こんだん} (informal talk)
- **Adverbs (5)**: {着々|ちゃくちゃく}と (steadily), {必死|ひっし}に (desperately), {一気|いっき}に (in one go), {順次|じゅんじ} (sequentially), ひょっこり (unexpectedly)
- **Nouns (special) (2)**: {小悪魔|こあくま} (flirtatious person), {口止|くちど}め (silencing)
- **Verbs (2)**: {締|し}め{付|つ}ける (to tighten), {澄|す}ます (to clear/strain)
- **Expression (1)**: おやすみなさい (good night)

Notable features:
- Diverse POS coverage: nouns, verbs, adverbs, adjectives, expressions
- Multi-sense: {中毒|ちゅうどく} (2: poisoning + addiction), {一気|いっき}に (2: in one go + suddenly), {締|し}め{付|つ}ける (2: physical + figurative), {澄|す}ます (2: strain senses + look composed), スケベ (2: noun + adjective), {小悪魔|こあくま} (2: literal + figurative)
- Modern vocabulary: {配信者|はいしんしゃ} (streamer/content creator)
- Grammar term: {接続詞|せつぞくし}
- New kanji: 2,537 → 2,539 (咽, 嗚)

Total entries: ~16,603 → ~16,633 (approximate)
Remaining candidates: ~3,175 → ~3,145 (30 removed)

### 2026-03-13 (Vocabulary Expansion - 30 New Entries, Session 425)
Added 30 new dictionary entries (IDs 16524-16553) from candidate_words.json:

- **Nouns (13)**: {複合機|ふくごうき} (multi-function printer), {進入禁止|しんにゅうきんし} (no entry), {駐車券|ちゅうしゃけん} (parking ticket), {物損事故|ぶっそんじこ} (property damage accident), {奥地|おくち} (hinterland), {葉物|はもの} (leafy vegetables), {水産物|すいさんぶつ} (marine products), {軽傷|けいしょう} (minor injury), {接触不良|せっしょくふりょう} (loose connection), {取|と}り{合|あ}わせ (assortment), {電動自転車|でんどうじてんしゃ} (e-bike), {心|こころ}の{底|そこ} (bottom of one's heart), {五目寿司|ごもくずし} (mixed sushi)
- **Nouns/suru verbs (5)**: {急速充電|きゅうそくじゅうでん} (rapid charging), {裏工作|うらこうさく} (backroom dealings), {組閣|そかく} (cabinet formation), {隠蔽工作|いんぺいこうさく} (cover-up), {補導|ほどう} (juvenile guidance)
- **Nouns/pre-noun adjectivals (2)**: {家庭用|かていよう} (for home use), {体験型|たいけんがた} (hands-on)
- **Nouns/adverbs (2)**: {世界一|せかいいち} (best in the world), {小粒|こつぶ} (small grain)
- **Nouns/adjectives (1)**: {片手落|かたてお}ち (one-sided)
- **Verbs (2)**: {垂|た}れ{流|なが}す (to discharge), {払|はら}い{戻|もど}す (to refund)
- **Expressions (4)**: {暗礁|あんしょう}に{乗|の}り{上|あ}げる (to hit a snag), {影響|えいきょう}を{及|およ}ぼす (to exert influence), {差|さ}し{支|つか}えなければ (if you don't mind), それじゃあ (well then)
- **Conjunction (1)**: それじゃあ (well then)

Notable features:
- Technology/modern life: {複合機|ふくごうき}, {急速充電|きゅうそくじゅうでん}, {電動自転車|でんどうじてんしゃ}, {接触不良|せっしょくふりょう}
- Legal/news: {物損事故|ぶっそんじこ}, {裏工作|うらこうさく}, {隠蔽工作|いんぺいこうさく}, {補導|ほどう}, {組閣|そかく}
- Daily life/food: {駐車券|ちゅうしゃけん}, {葉物|はもの}, {五目寿司|ごもくずし}, {水産物|すいさんぶつ}
- Useful expressions: {差|さ}し{支|つか}えなければ, {影響|えいきょう}を{及|およ}ぼす, {暗礁|あんしょう}に{乗|の}り{上|あ}げる
- Multi-sense: {垂|た}れ{流|なが}す (2: literal discharge + figurative spewing), {暗礁|あんしょう}に{乗|の}り{上|あ}げる (2: literal + figurative), {小粒|こつぶ} (2: size + figurative), それじゃあ (2: transitional + parting)

Total entries: ~16,573 → ~16,603 (approximate)
Remaining candidates: ~3,205 → ~3,175 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
