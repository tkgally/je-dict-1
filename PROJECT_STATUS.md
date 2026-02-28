# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-28
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
| Total entries | ~14,234 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~11,435 (open) |
| Candidate words | ~5,535 |
| Cross-references | ~3,400 |
| Example sentences | ~48,800 |
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

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 346)
Added 30 new dictionary entries (IDs 14149-14178) from candidate_words.json:

- **Nouns (14)**: {芸者|げいしゃ} (geisha), {街|まち}づくり (community development), {英国|えいこく} (Britain), {衆議院|しゅうぎいん} (House of Representatives), {痴話喧嘩|ちわげんか} (lovers' quarrel), {留飲|りゅういん} (vindication), {要塞|ようさい} (fortress), {見世物|みせもの} (spectacle), {規範|きはん} (norm), {観光地|かんこうち} (tourist spot), {試練|しれん} (trial/ordeal), {詰|つ}め{合|あ}わせ (assortment), {話|はな}し{合|あ}い (discussion), {誓|ちか}い (vow/oath)
- **Noun/suru verbs (7)**: {襲来|しゅうらい} (invasion), {見合|みあ}い (matchmaking), {解明|かいめい} (elucidation), {記載|きさい} (listing), {設立|せつりつ} (establishment), {許容|きょよう} (tolerance), {該当|がいとう} (applicable)
- **Noun (multi-sense) (1)**: {衣|ころも} (robe + batter)
- **Noun (1)**: {記者|きしゃ} (reporter), {親権|しんけん} (parental rights), {言|い}い{方|かた} (way of saying), {言葉|ことば}づかい (language use)
- **Ichidan verbs (3)**: {薄汚|うすよご}れる (to become grimy), {言|い}い{聞|き}かせる (to admonish), {詫|わ}びる (to apologize)
- **Godan verb (1)**: {託|たく}す (to entrust)

Notable features:
- Multi-sense entry: {衣|ころも} (2: robe/garment + batter/coating)
- Politics/law: {衆議院|しゅうぎいん}, {親権|しんけん}, {規範|きはん}, {該当|がいとう}
- Communication: {言|い}い{方|かた}, {言葉|ことば}づかい, {言|い}い{聞|き}かせる, {話|はな}し{合|あ}い, {詫|わ}びる, {誓|ちか}い
- Culture: {芸者|げいしゃ}, {見世物|みせもの}, {見合|みあ}い, {観光地|かんこうち}
- New kanji: 2,452 → 2,453 ({該|がい})

Total entries: 14,204 → 14,234 (approximate)
Remaining candidates: 5,565 → 5,535 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 345)
Added 30 new dictionary entries (IDs 14119-14148) from candidate_words.json:

- **Nouns (10)**: {茎|くき} (stem/stalk), {苦|くる}しみ (suffering), {行|おこな}い (behavior/deed), {荷台|にだい} (truck bed), {見覚|みおぼ}え (recognition), {親心|おやごころ} (parental love), {視界|しかい} (field of vision), {視線|しせん} (gaze), {若年|じゃくねん} (youth), {製造業|せいぞうぎょう} (manufacturing industry)
- **Noun/suru verbs (7)**: {行政|ぎょうせい} (administration), {表記|ひょうき} (notation), {襲撃|しゅうげき} (attack/raid), {要約|ようやく} (summary), {規定|きてい} (regulation), {観戦|かんせん} (spectating), {解消|かいしょう} (elimination/resolution), {解禁|かいきん} (lifting a ban)
- **Na-adjective (1)**: {親密|しんみつ} (intimate/close)
- **Godan verbs (5)**: {見失|みうしな}う (to lose sight of), {見積|みつ}もる (to estimate), {見舞|みま}う (to visit sick/to strike), {見開|みひら}く (to open eyes wide), {親|した}しむ (to become familiar with)
- **Ichidan verbs (2)**: {見捨|みす}てる (to abandon), {見据|みす}える (to stare at/keep in sight)
- **Nouns (other) (3)**: {藩|はん} (feudal domain), {言|い}い{伝|つた}え (legend), {言|い}い{回|まわ}し (phrasing)
- **Noun (1)**: {言動|げんどう} (words and actions)

Notable features:
- Multi-sense entries: {見舞|みま}う (2: visit sick + befall), {見据|みす}える (2: stare at + keep in sight)
- 見- compound verbs: {見失|みうしな}う, {見捨|みす}てる, {見据|みす}える, {見積|みつ}もる, {見舞|みま}う, {見開|みひら}く, {見覚|みおぼ}え
- Language/expression: {表記|ひょうき}, {言|い}い{伝|つた}え, {言|い}い{回|まわ}し, {言動|げんどう}, {要約|ようやく}
- Society/law: {行政|ぎょうせい}, {規定|きてい}, {解消|かいしょう}, {解禁|かいきん}, {襲撃|しゅうげき}
- Family/relationships: {親心|おやごころ}, {親密|しんみつ}, {親|した}しむ
- History: {藩|はん} (feudal domain)
- New kanji: 2,451 → 2,452 ({藩|はん})

Total entries: 14,174 → 14,204 (approximate)
Remaining candidates: 5,595 → 5,565 (30 removed)

### 2026-02-28 (Vocabulary Expansion - 30 New Entries, Session 344)
Added 30 new dictionary entries (IDs 14089-14118) from candidate_words.json:

- **Nouns (17)**: {草木|くさき} (plants/vegetation), {製菓|せいか} (confectionery making), {街路|がいろ} (street), {群像|ぐんぞう} (group portrait/ensemble), {表題|ひょうだい} (title/heading), {薬剤|やくざい} (pharmaceutical), {苦味|にがみ} (bitterness), {衣装|いしょう} (costume), {被害者|ひがいしゃ} (victim), {落|お}ち{葉|ば} (fallen leaves), {見|み}た{目|め} (appearance), {見|み}せ{場|ば} (highlight), {覇権|はけん} (hegemony), {褐色|かっしょく} (brown), {茶会|ちゃかい} (tea gathering), {英雄|えいゆう} (hero), {薪|まき} (firewood)
- **Noun/suru verbs (5)**: {装備|そうび} (equipment/equipping), {装飾|そうしょく} (decoration), {補助|ほじょ} (assistance/subsidy), {要望|ようぼう} (request/demand), {複合|ふくごう} (compound/composite)
- **Na-adjective (2)**: {荒唐無稽|こうとうむけい} (absurd), {美麗|びれい} (beautiful/gorgeous)
- **Noun (2 senses, 4)**: {裏打|うらう}ち (backing + substantiation), {群像|ぐんぞう} (art + ensemble), {要領|ようりょう} (knack + gist), {補助|ほじょ} (assistance + subsidy)
- **Ichidan verb (1)**: {薄|うす}れる (to fade/weaken)
- **Noun (other, 3)**: {薄給|はっきゅう} (low salary), {蒸|む}し{風呂|ぶろ} (steam bath), {絵巻|えまき} (picture scroll)

Notable features:
- Multi-sense entries: {裏打|うらう}ち (2: lining + substantiation), {装備|そうび} (2: equipment + equipping), {補助|ほじょ} (2: assistance + subsidy), {薄|うす}れる (2: physical fading + abstract weakening), {要領|ようりょう} (2: knack + gist)
- Four-character compound: {荒唐無稽|こうとうむけい}
- Food/taste: {苦味|にがみ}, {製菓|せいか}
- Arts/culture: {絵巻|えまき}, {群像|ぐんぞう}, {茶会|ちゃかい}, {美麗|びれい}
- Work/society: {薄給|はっきゅう}, {被害者|ひがいしゃ}, {覇権|はけん}, {要望|ようぼう}
- Nature/seasons: {草木|くさき}, {落|お}ち{葉|ば}
- New kanji: 2,449 → 2,451 ({薪|しん}, {褐|かつ})

Total entries: 14,144 → 14,174 (approximate)
Remaining candidates: 5,625 → 5,595 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 343)
Added 30 new dictionary entries (IDs 14059-14088) from candidate_words.json:

- **Godan verbs (3)**: {花開|はなひら}く (to bloom/flourish), {脱|ぬ}がす (to undress someone), {薄|うす}まる (to become diluted)
- **Ichidan verb (1)**: {舞|ま}い{降|お}りる (to swoop down)
- **Nouns (14)**: {神髄|しんずい} (essence), {禅宗|ぜんしゅう} (Zen Buddhism), {能楽|のうがく} (noh theater), {神事|しんじ} (Shinto ritual), {群青|ぐんじょう} (ultramarine blue), {肉筆|にくひつ} (handwriting), {習俗|しゅうぞく} (customs), {老年|ろうねん} (old age), {艦隊|かんたい} (fleet), {背徳|はいとく} (immorality), {神楽|かぐら} (kagura), {蘊蓄|うんちく} (extensive knowledge), {著書|ちょしょ} (written work), {蜜|みつ} (honey/nectar)
- **Noun/suru verbs (2)**: {補完|ほかん} (supplementation), {行使|こうし} (exercise of power)
- **Noun/na-adjectives (4)**: {美形|びけい} (good-looking), {縦横無尽|じゅうおうむじん} (freely in all directions), {荒削|あらけず}り (rough-hewn), {表裏一体|ひょうりいったい} (two sides of same coin)
- **Noun/verb-suru (1)**: {膝枕|ひざまくら} (lap pillow)
- **Noun/prefix (1)**: {自家|じか} (one's own/home-made)
- **Noun (business) (1)**: {自社|じしゃ} (one's own company)
- **Noun (cultural) (2)**: {茶室|ちゃしつ} (tea room), {茶|ちゃ}の{湯|ゆ} (tea ceremony)
- **Noun (political) (1)**: {草|くさ}の{根|ね} (grassroots)

Notable features:
- Multi-sense entries: {花開|はなひら}く (2: bloom + flourish), {荒削|あらけず}り (2: rough-hewn + unpolished talent)
- Japanese culture: {禅宗|ぜんしゅう}, {能楽|のうがく}, {神事|しんじ}, {神楽|かぐら}, {茶室|ちゃしつ}, {茶|ちゃ}の{湯|ゆ}
- Four-character compounds: {縦横無尽|じゅうおうむじん}, {表裏一体|ひょうりいったい}
- Arts/writing: {肉筆|にくひつ}, {群青|ぐんじょう}, {著書|ちょしょ}
- New kanji: 2,447 → 2,449 ({艦|かん}, {蘊|うん})

Total entries: 14,114 → 14,144 (approximate)
Remaining candidates: 5,655 → 5,625 (30 removed)

### 2026-02-27 (Vocabulary Expansion - 30 New Entries, Session 342)
Added 30 new dictionary entries (IDs 14029-14058) from candidate_words.json:

- **Noun/suru verbs (9)**: {蘇生|そせい} (resuscitation), {衰弱|すいじゃく} (debilitation), {融合|ゆうごう} (fusion), {補充|ほじゅう} (replenishment), {落下|らっか} (fall/drop), {表明|ひょうめい} (declaration), {補給|ほきゅう} (supply), {行|い}き{来|き} (coming and going), {落書|らくが}き (graffiti)
- **Nouns (11)**: {裏話|うらばなし} (behind-the-scenes story), {薬草|やくそう} (medicinal herb), {血縁|けつえん} (blood relation), {製法|せいほう} (manufacturing method), {街道|かいどう} (highway), {菜|な}の{花|はな} (rapeseed flower), {蜂蜜|はちみつ} (honey), {装束|しょうぞく} (costume), {衛生|えいせい} (hygiene), {薬物|やくぶつ} (drug), {英気|えいき} (vigor)
- **Noun/na-adjective (4)**: {裏腹|うらはら} (contrary), {行方不明|ゆくえふめい} (missing), {蒼白|そうはく} (pale/pallid), {裏返|うらがえ}し (inside out)
- **Na-adjective (1)**: {裕福|ゆうふく} (wealthy)
- **Noun (literary) (1)**: {装|よそお}い (attire/appearance)
- **Noun/suru verb (formal, 1)**: {虚偽|きょぎ} (falsehood)
- **Noun/suru verb (social, 1)**: {虐待|ぎゃくたい} (abuse)
- **Ichidan verb (1)**: {裏付|うらづ}ける (to substantiate)
- **Godan verb (1)**: {荒|あ}らす (to devastate)

Notable features:
- Multi-sense entries: {裏返|うらがえ}し (2: inside out + flip side), {装|よそお}い (2: attire + guise), {荒|あ}らす (2: devastate + ransack)
- Medical/health: {蘇生|そせい} (CPR), {衰弱|すいじゃく}, {衛生|えいせい}, {薬物|やくぶつ}, {薬草|やくそう}
- Legal/formal: {虚偽|きょぎ}, {虐待|ぎゃくたい}, {表明|ひょうめい}, {裏付|うらづ}ける
- Cultural: {街道|かいどう} (Edo highways), {装束|しょうぞく} (traditional costumes), {菜|な}の{花|はな} (spring tradition)
- Food: {蜂蜜|はちみつ}, {菜|な}の{花|はな}, {製法|せいほう}
- New kanji: 2,445 → 2,447 ({蒼|そう}, {虐|ぎゃく})

Total entries: 14,084 → 14,114 (approximate)
Remaining candidates: 5,685 → 5,655 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
