# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-13
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
| Total entries | ~16,603 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,804 (open) |
| Candidate words | ~3,175 |
| Cross-references | ~3,400 |
| Example sentences | ~49,900 |
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

### 2026-03-13 (Vocabulary Expansion - 30 New Entries, Session 424)
Added 30 new dictionary entries (IDs 16493-16523) from candidate_words.json:

- **Nouns (14)**: {麦茶|むぎちゃ} (barley tea), {玄米茶|げんまいちゃ} (brown rice tea), {隅々|すみずみ} (every nook and cranny), {秘境|ひきょう} (unexplored region), {連歌|れんが} (linked verse), {料理長|りょうりちょう} (head chef), {領空|りょうくう} (territorial airspace), {伴走者|ばんそうしゃ} (guide runner), {大衆文学|たいしゅうぶんがく} (popular fiction), {古代文明|こだいぶんめい} (ancient civilization), {蔵造|くらづく}り (warehouse architecture), {蔵屋敷|くらやしき} (domain warehouse), {避暑地|ひしょち} (summer resort), {発酵食品|はっこうしょくひん} (fermented food)
- **Nouns/suru verbs (6)**: {訂正|ていせい} (correction), {窒息|ちっそく} (suffocation), {逆上|ぎゃくじょう} (frenzy), {増水|ぞうすい} (rising water), {溺愛|できあい} (doting), {搬入|はんにゅう} (carrying in)
- **Nouns/suru verbs (2)**: {都落|みやこお}ち (fleeing the capital), {一気飲|いっきの}み (chugging)
- **Noun/suru verb (special) (2)**: {突|つ}き{指|ゆび} (jammed finger), お{試|ため}し{期間|きかん} (trial period)
- **Noun (compound) (3)**: {就職氷河期|しゅうしょくひょうがき} (employment ice age), {千秋楽|せんしゅうらく} (final day), {限界集落|げんかいしゅうらく} (dying village)
- **Cultural (2)**: {端午|たんご}の{節句|せっく} (Boys' Day), {桃|もも}の{節句|せっく} (Girls' Day)
- **Expression (1)**: {愛想|あいそ}がいい (amiable)
- **Food culture (1)**: {幕の内弁当|まくのうちべんとう} (traditional boxed lunch)

Notable features:
- Food/drink: {麦茶|むぎちゃ}, {玄米茶|げんまいちゃ}, {発酵食品|はっこうしょくひん}, {幕の内弁当|まくのうちべんとう}, {一気飲|いっきの}み, {料理長|りょうりちょう}
- Japanese culture: {千秋楽|せんしゅうらく}, {端午|たんご}の{節句|せっく}, {桃|もも}の{節句|せっく}, {連歌|れんが}, {蔵造|くらづく}り, {蔵屋敷|くらやしき}
- Society: {就職氷河期|しゅうしょくひょうがき}, {限界集落|げんかいしゅうらく}, {大衆文学|たいしゅうぶんがく}
- Safety/medical: {窒息|ちっそく}, {逆上|ぎゃくじょう}, {突|つ}き{指|ゆび}
- Geography/travel: {秘境|ひきょう}, {避暑地|ひしょち}, {領空|りょうくう}
- Multi-sense: {伴走者|ばんそうしゃ} (2: guide runner + supportive companion)

Total entries: ~16,542 → ~16,573 (approximate)
Remaining candidates: ~3,236 → ~3,205 (31 removed)

### 2026-03-13 (Vocabulary Expansion - 30 New Entries, Session 423)
Added 30 new dictionary entries (IDs 16463-16492) from candidate_words.json:

- **Nouns (16)**: {注意報|ちゅういほう} (advisory), {新刊|しんかん} (new publication), {千鳥足|ちどりあし} (drunken stagger), {悩|なや}み{事|ごと} (troubles), {喉越|のどご}し (mouthfeel), {飾|かざ}り{物|もの} (ornament), {食費|しょくひ} (food expenses), {生演奏|なまえんそう} (live performance), {植物園|しょくぶつえん} (botanical garden), {鮮魚|せんぎょ} (fresh fish), {煮魚|にざかな} (simmered fish), {凶作|きょうさく} (bad harvest), {観光名所|かんこうめいしょ} (tourist attraction), {加工品|かこうひん} (processed goods), {路面|ろめん} (road surface), {宿泊施設|しゅくはくしせつ} (lodging)
- **Nouns/suru verbs (5)**: {驚嘆|きょうたん} (amazement), {決議|けつぎ} (resolution), {節税|せつぜい} (tax saving), {避暑|ひしょ} (summer retreat), {竣工|しゅんこう} (construction completion)
- **Nouns (multi-sense) (3)**: {筋書|すじが}き (2: plot + scenario), {飾|かざ}り{物|もの} (2: decoration + figurehead), {歪|ひず}み (2: physical strain + social strain)
- **Noun/suru verb (2)**: {思案|しあん} (pondering), {仮住|かりず}まい (temporary residence)
- **Adverb (1)**: {一向|いっこう}に (not at all)
- **Verb (1)**: {捻|ね}じれる (to be twisted)
- **Expression (1)**: {体調|たいちょう}を{崩|くず}す (to fall ill)
- **Noun/adjective (1)**: {蝶結|ちょうむす}び (bowknot)

Notable features:
- Food/drink: {喉越|のどご}し, {鮮魚|せんぎょ}, {煮魚|にざかな}, {加工品|かこうひん}, {食費|しょくひ}
- Travel/places: {観光名所|かんこうめいしょ}, {宿泊施設|しゅくはくしせつ}, {避暑|ひしょ}, {植物園|しょくぶつえん}
- Infrastructure: {路面|ろめん}, {竣工|しゅんこう}
- Daily life: {悩|なや}み{事|ごと}, {蝶結|ちょうむす}び, {仮住|かりず}まい, {体調|たいちょう}を{崩|くず}す
- Formal/political: {決議|けつぎ}, {捻|ね}じれる (twisted Diet), {驚嘆|きょうたん}
- New kanji: 2,536 → 2,537 (竣)

Total entries: ~16,512 → ~16,542 (approximate)
Remaining candidates: ~3,266 → ~3,236 (30 removed)

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 422)
Added 30 new dictionary entries (IDs 16433-16462) from candidate_words.json:

- **Na-adjectives (3)**: {柔軟|じゅうなん}な (flexible), {無責任|むせきにん}な (irresponsible), {肥沃|ひよく}な (fertile)
- **Nouns (20)**: {電子書籍|でんししょせき} (e-book), {金網|かなあみ} (wire mesh), {薄化粧|うすげしょう} (light makeup), {病床|びょうしょう} (sickbed), {協調性|きょうちょうせい} (cooperativeness), {関係者|かんけいしゃ} (person concerned), {怨恨|えんこん} (grudge), {全体像|ぜんたいぞう} (big picture), {撥水|はっすい} (water repellent), {行楽地|こうらくち} (tourist spot), {最新版|さいしんばん} (latest version), {山腹|さんぷく} (mountainside), {詳報|しょうほう} (detailed report), {健康維持|けんこういじ} (health maintenance), {中道|ちゅうどう} (centrism), {群舞|ぐんぶ} (group dance), {個体差|こたいさ} (individual variation), {逆転劇|ぎゃくてんげき} (dramatic comeback), {一網打尽|いちもうだじん} (wholesale roundup), {逆転負|ぎゃくてんま}け (come-from-behind loss)
- **Nouns/suru verbs (5)**: {代用|だいよう} (substitution), {再確認|さいかくにん} (reconfirmation), {数値化|すうちか} (quantification), {再雇用|さいこよう} (re-employment), {定年退職|ていねんたいしょく} (mandatory retirement)
- **Nouns (multi-sense) (2)**: {無風|むふう} (2: windless + uncontested), {一般道|いっぱんどう} (public road)

Notable features:
- Work/society: {協調性|きょうちょうせい}, {定年退職|ていねんたいしょく}, {再雇用|さいこよう}, {関係者|かんけいしゃ}, {無責任|むせきにん}な
- Technology/modern: {電子書籍|でんししょせき}, {最新版|さいしんばん}, {数値化|すうちか}, {撥水|はっすい}
- Sports/politics: {逆転劇|ぎゃくてんげき}, {逆転負|ぎゃくてんま}け, {中道|ちゅうどう}, {無風|むふう}
- Nature/geography: {山腹|さんぷく}, {肥沃|ひよく}な
- Four-character idiom: {一網打尽|いちもうだじん}
- New kanji: 2,534 → 2,536 (撥, 沃)

Total entries: ~16,482 → ~16,512 (approximate)
Remaining candidates: ~3,296 → ~3,266 (30 removed)

### 2026-03-12 (Vocabulary Expansion - 30 New Entries, Session 421)
Added 30 new dictionary entries (IDs 16403-16432) from candidate_words.json:

- **Nouns (18)**: {野次馬|やじうま} (onlooker), {評論家|ひょうろんか} (critic), {新書|しんしょ} (pocket-sized book), {山積|やまづ}み (huge pile), {物腰|ものごし} (demeanor), {幼虫|ようちゅう} (larva), {絶壁|ぜっぺき} (precipice), {厚化粧|あつげしょう} (heavy makeup), {無駄話|むだばなし} (idle talk), {帰宅部|きたくぶ} (go-home club), {月謝|げっしゃ} (monthly tuition), {爪先|つまさき} (tiptoe), {天袋|てんぶくろ} (overhead cupboard), {鏡台|きょうだい} (dressing table), {画廊|がろう} (art gallery), {好感|こうかん} (good impression), {荒天|こうてん} (stormy weather), {焼香|しょうこう} (burning incense)
- **Nouns/suru verbs (3)**: {減点|げんてん} (deducting points), {戦慄|せんりつ} (shudder), {大歓迎|だいかんげい} (warm welcome)
- **Nouns (multi-sense) (3)**: {担任|たんにん} (homeroom teacher/person in charge), {修羅|しゅら} (carnage/Asura), {不意打|ふいう}ち (surprise attack)
- **Noun/na-adjective (2)**: {不条理|ふじょうり} (absurdity), {謙譲|けんじょう} (humility)
- **Adjective-i (2)**: {物珍|ものめずら}しい (novel/curious), {計算高|けいさんだか}い (calculating)
- **Adverb (1)**: さながら (just like)
- **Verb (1)**: {言|い}い{返|かえ}す (to talk back)

Notable features:
- School/education: {担任|たんにん}, {帰宅部|きたくぶ}, {月謝|げっしゃ}, {減点|げんてん}
- Culture: {焼香|しょうこう} (Buddhist funerals), {新書|しんしょ} (publishing format), {鏡台|きょうだい} (traditional furniture)
- Literary/formal: さながら, {戦慄|せんりつ}, {修羅|しゅら}, {謙譲|けんじょう}, {荒天|こうてん}
- Daily life: {爪先|つまさき}, {厚化粧|あつげしょう}, {無駄話|むだばなし}, {野次馬|やじうま}
- Multi-sense: {担任|たんにん} (2), {修羅|しゅら} (2), {大歓迎|だいかんげい} (2)
- New kanji: 2,533 → 2,534 (慄)

Total entries: ~16,452 → ~16,482 (approximate)
Remaining candidates: ~3,326 → ~3,296 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
