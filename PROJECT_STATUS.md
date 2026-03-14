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
| Total entries | ~16,874 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,075 (open) |
| Candidate words | ~2,905 |
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

### 2026-03-14 (Vocabulary Expansion - 45 New Entries, Session 432)
Added 45 new dictionary entries (IDs 16825-16869) from candidate_words.json:

- **Adjectives (i-adj, 6)**: {子供|こども}っぽい (childish), {胡散臭|うさんくさ}い (shady), {重苦|おもぐる}しい (oppressive), {注意深|ちゅういぶか}い (careful), {湿|しめ}っぽい (damp/gloomy), {流暢|りゅうちょう} (fluent)
- **Adjectives (na-adj, 7)**: {理性的|りせいてき} (rational), {非力|ひりき} (powerless), {意図的|いとてき} (intentional), {好都合|こうつごう} (convenient), {不公平|ふこうへい} (unfair), {内気|うちき} (shy), {優柔不断|ゆうじゅうふだん} (indecisive)
- **Nouns (17)**: {洗脳|せんのう} (brainwashing), {全額|ぜんがく} (full amount), {片思|かたおも}い (unrequited love), {絶景|ぜっけい} (superb view), {万引|まんび}き (shoplifting), {悪影響|あくえいきょう} (bad influence), {古典的|こてんてき} (classical), {鳴|な}き{声|ごえ} (animal cry), {節目|ふしめ} (turning point), {敵意|てきい} (hostility), {駄作|ださく} (poor work), {等身大|とうしんだい} (life-size), {靴紐|くつひも} (shoelace), {運動靴|うんどうぐつ} (sneakers), {朝型|あさがた} (morning person), {見頃|みごろ} (peak viewing season), {梅酒|うめしゅ} (plum wine)
- **Adverbs (4)**: {心|こころ}から (sincerely), いずれも (all/any of them), {不意|ふい}に (unexpectedly), {反射的|はんしゃてき} (reflexively)
- **Suru verbs (4)**: {精進|しょうじん}する (to devote oneself), お{参|まい}り (shrine visit), {勧誘|かんゆう} (solicitation), {挙手|きょしゅ} (show of hands)
- **Other (7)**: おもてなし (hospitality), お{粥|かゆ} (rice porridge), まなざし (gaze), {故意|こい} (intent), {寒|さむ}がり (cold-sensitive person), {暑|あつ}がり (heat-sensitive person), {自撮|じど}り (selfie)

Notable features:
- Multi-sense: {湿|しめ}っぽい (2: damp + gloomy), {古典的|こてんてき} (2: classical + old-fashioned), {等身大|とうしんだい} (2: life-size + authentic)
- Antonym pair: {寒|さむ}がり/{暑|あつ}がり
- Cultural: おもてなし, お{参|まい}り, {梅酒|うめしゅ}, お{粥|かゆ}, {見頃|みごろ}
- Modern: {自撮|じど}り, {洗脳|せんのう}, {朝型|あさがた}
- Four-character compound: {優柔不断|ゆうじゅうふだん}
- New kanji: 2,544 → 2,545 (暢)

Total entries: ~16,874 → ~16,919 (approximate)
Remaining candidates: ~2,905 → ~2,860 (45 removed)

### 2026-03-14 (Vocabulary Expansion - 45 New Entries, Session 431)
Added 45 new dictionary entries (IDs 16779-16824) from candidate_words.json:

- **Nouns (24)**: {行|い}き{先|さき} (destination), {反対側|はんたいがわ} (opposite side), {会議中|かいぎちゅう} (in a meeting), {毒素|どくそ} (toxin), {作業服|さぎょうふく} (work clothes), {本革|ほんがわ} (genuine leather), {伝言板|でんごんばん} (message board), {可燃物|かねんぶつ} (burnable items), {染|し}み{抜|ぬ}き (stain removal), {客船|きゃくせん} (passenger ship), {受信箱|じゅしんばこ} (inbox), {会員制|かいいんせい} (membership system), {千代紙|ちよがみ} (chiyogami paper), {献杯|けんぱい} (memorial toast), {土産物屋|みやげものや} (souvenir shop), {昆布|こんぶ}だし (kelp stock), {催事場|さいじじょう} (event hall), {固定資産|こていしさん} (fixed assets), {養親|ようしん} (adoptive parent), {情操|じょうそう} (sentiment), {到来物|とうらいもの} (gift received), {知能指数|ちのうしすう} (IQ), {基礎代謝|きそたいしゃ} (basal metabolism), {産婦人科|さんふじんか} (OB/GYN)
- **Nouns/suru verbs (4)**: {完遂|かんすい} (completion), {乗船|じょうせん} (boarding a ship), {重要視|じゅうようし} (regarding as important), {製材|せいざい} (lumbering)
- **Na-adjectives (3)**: {持続的|じぞくてき} (sustainable), {枢要|すうよう} (pivotal), {繁多|はんた} (extremely busy)
- **Adverbs/expressions (5)**: {予想通|よそうどお}り (as expected), {何|なん}としても (no matter what), {力一杯|ちからいっぱい} (with all one's strength), {口一杯|くちいっぱい} (mouthful), {他日|たじつ} (another day)
- **Verbs (2)**: すすり{泣|な}く (to sob), {飼|か}い{慣|な}らす (to tame)
- **Other nouns (5)**: {和文|わぶん} (Japanese text), {住民税|じゅうみんぜい} (resident tax), {極道|ごくどう} (gangster), {解毒剤|げどくざい} (antidote), {行|い}き{道|みち} (the way there)
- **Multi-sense entries (2)**: {湯冷|ゆざ}まし (cooled water + tea vessel), {不治|ふじ}の{病|やまい} (incurable disease)

Notable features:
- Life in Japan: {可燃物|かねんぶつ}, {住民税|じゅうみんぜい}, {会員制|かいいんせい}, {催事場|さいじじょう}
- Food/cooking: {昆布|こんぶ}だし, {湯冷|ゆざ}まし
- Medical: {産婦人科|さんふじんか}, {毒素|どくそ}, {解毒剤|げどくざい}, {基礎代謝|きそたいしゃ}
- Travel: {客船|きゃくせん}, {乗船|じょうせん}, {土産物屋|みやげものや}, {行|い}き{先|さき}
- Cultural: {献杯|けんぱい}, {千代紙|ちよがみ}, {極道|ごくどう}, {到来物|とうらいもの}
- Multi-sense: {極道|ごくどう} (2: gangster + delinquent), {湯冷|ゆざ}まし (2: cooled water + vessel)

Total entries: ~16,828 → ~16,874 (approximate)
Remaining candidates: ~2,951 → ~2,905 (46 removed)

### 2026-03-14 (Vocabulary Expansion - 45 New Entries, Session 430)
Added 45 new dictionary entries (IDs 16734-16778) from candidate_words.json:

- **Verbs (8)**: {追|お}いかける (to chase), うっとうしい (gloomy/annoying, i-adj), {老|ふ}ける (to age), {上|あ}がりこむ (to enter someone's house), やり{遂|と}げる (to accomplish), {切|き}り{抜|ぬ}ける (to get through), {積|つ}み{込|こ}む (to load), {反|そ}り{返|かえ}る (to bend backward)
- **Nouns (17)**: {焼|や}きたて (freshly baked), {揚|あ}げたて (freshly fried), うつ{伏|ぶ}せ (prone position), {総菜|そうざい} (deli food), タメ{口|ぐち} (casual speech), お{代|か}わり (seconds/refill), {開封|かいふう} (opening), びしょ{濡|ぬ}れ (soaking wet), {秋雨|あきさめ} (autumn rain), {贈呈|ぞうてい} (presentation), {大安|たいあん} (lucky day), {仏滅|ぶつめつ} (unlucky day), {波風|なみかぜ} (trouble), {造成|ぞうせい} (land development), {網焼|あみや}き (net-grilled), {不信感|ふしんかん} (distrust), {懇意|こんい} (friendship)
- **Nouns/suru verbs (5)**: {哀願|あいがん} (supplication), {贈呈|ぞうてい} (presentation), {類推|るいすい} (analogy), {迎撃|げいげき} (interception), {自己主張|じこしゅちょう} (self-assertion)
- **Adverbs (4)**: {極力|きょくりょく} (as much as possible), その{都度|つど} (each time), {割|わり}に (comparatively), {徹頭徹尾|てっとうてつび} (thoroughly)
- **Expressions (2)**: {念|ねん}のため (just in case), {日|ひ}が{暮|く}れる (the sun sets)
- **Other nouns (9)**: {常設|じょうせつ} (permanent), {近日|きんじつ} (soon), {公共料金|こうきょうりょうきん} (utility bills), {試供品|しきょうひん} (free sample), {祝杯|しゅくはい} (celebratory toast), {敬老|けいろう} (respect for elders), {言付|ことづ}け (verbal message), {不衛生|ふえいせい} (unsanitary), {運転席|うんてんせき} (driver's seat)

Notable features:
- Cultural pairs: {大安|たいあん}/{仏滅|ぶつめつ} (lucky/unlucky days in rokuyo calendar)
- Food & cooking: {焼|や}きたて, {揚|あ}げたて, {総菜|そうざい}, {網焼|あみや}き, お{代|か}わり
- Multi-sense: {追|お}いかける (2: physical + figurative), うっとうしい (2: gloomy + annoying), {波風|なみかぜ} (2: figurative + literal), {反|そ}り{返|かえ}る (2: body + warping), {割|わり}に (2: comparatively + considering)
- Daily life: {公共料金|こうきょうりょうきん}, {試供品|しきょうひん}, {運転席|うんてんせき}, {開封|かいふう}
- Social/cultural: タメ{口|ぐち}, {自己主張|じこしゅちょう}, {敬老|けいろう}
- Four-character compound: {徹頭徹尾|てっとうてつび}

Total entries: ~16,783 → ~16,828 (approximate)
Remaining candidates: ~2,996 → ~2,951 (45 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
