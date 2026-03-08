# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-08
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
| Total entries | ~15,854 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,055 (open) |
| Candidate words | ~3,919 |
| Cross-references | ~3,400 |
| Example sentences | ~49,000 |
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

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 400)
Added 30 new dictionary entries (IDs 15769-15799) from candidate_words.json:

- **Nouns (15)**: {憎|にく}しみ (hatred), {差額|さがく} (difference), {隠|かく}し{事|ごと} (secret), {前払|まえばら}い (advance payment), {義兄|ぎけい} (brother-in-law), {定型文|ていけいぶん} (boilerplate text), {逃亡者|とうぼうしゃ} (fugitive), {銀貨|ぎんか} (silver coin), {濁流|だくりゅう} (muddy torrent), {原稿用紙|げんこうようし} (manuscript paper), {歓迎会|かんげいかい} (welcome party), {感電|かんでん} (electric shock), {整髪|せいはつ} (hairdressing), {無香料|むこうりょう} (fragrance-free), {内需|ないじゅ} (domestic demand)
- **Noun/adjective-no (1)**: {極上|ごくじょう} (finest quality)
- **Noun/verb-suru (3)**: {兼用|けんよう} (dual use), {開墾|かいこん} (land reclamation), {特急券|とっきゅうけん} (express ticket)
- **Noun/na-adjective (1)**: {意気地|いくじ}なし (coward)
- **Na-adjective (3)**: {丁重|ていちょう} (courteous), {庶民的|しょみんてき} (down-to-earth), {浅薄|せんぱく} (shallow)
- **Adjective-i (2)**: {古臭|ふるくさ}い (old-fashioned), おむつ → moved below
- **Verb-godan (1)**: {欲張|よくば}る (to be greedy)
- **Verb-ichidan (1)**: {押|お}しのける (to push aside)
- **Other nouns (3)**: おむつ (diaper), お{吸|す}い{物|もの} (clear soup), ひらめき (inspiration), {立|た}ち{回|まわ}り (maneuvering/fight scene)

Notable features:
- Daily-life cluster: おむつ, お{吸|す}い{物|もの}, {前払|まえばら}い, {特急券|とっきゅうけん}, {無香料|むこうりょう}
- Business: {差額|さがく}, {定型文|ていけいぶん}, {内需|ないじゅ}, {歓迎会|かんげいかい}
- Multi-sense entries: {古臭|ふるくさ}い (2: outdated + musty), {押|お}しのける (2: physical + figurative), {立|た}ち{回|まわ}り (2: social maneuvering + fight scene)
- New kanji: 2,522 → 2,523 ({墾|こん})

Total entries: ~15,824 → ~15,854 (approximate)
Remaining candidates: ~3,948 → ~3,919 (29 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 399)
Added 30 new dictionary entries (IDs 15739-15768) from candidate_words.json:

- **Nouns (12)**: {捕鯨|ほげい} (whaling), {洋室|ようしつ} (Western-style room), {受話器|じゅわき} (telephone receiver), {放送局|ほうそうきょく} (broadcasting station), {鉱山|こうざん} (mine), {初旬|しょじゅん} (early part of month), {嫌悪感|けんおかん} (revulsion), {不快感|ふかいかん} (discomfort), {湿布|しっぷ} (medicated patch), {質量|しつりょう} (mass), {物陰|ものかげ} (behind something), {運勢|うんせい} (fortune)
- **Noun/verb-suru (4)**: {模倣|もほう} (imitation), {忌避|きひ} (avoidance/recusal), {奮発|ふんぱつ} (splurging), {草案|そうあん} (draft)
- **Noun/na-adjective (2)**: {桁違|けたちが}い (on a different scale), {不仲|ふなか} (discord)
- **Na-adjective (2)**: {強靭|きょうじん} (tough/resilient), {無慈悲|むじひ} (merciless)
- **Noun (compound) (3)**: {競技場|きょうぎじょう} (stadium), {話|はな}し{方|かた} (way of speaking), {回|まわ}り{道|みち} (detour)
- **Noun (emotion) (1)**: {野心|やしん} (ambition)
- **Noun (unusual event) (1)**: {異変|いへん} (unusual event)
- **Verb-godan (3)**: {洗|あら}い{流|なが}す (to wash off), {取|と}り{壊|こわ}す (to demolish), {喘|あえ}ぐ (to gasp/struggle)
- **Verb-ichidan (1)**: かき{混|ま}ぜる (to stir)
- **Compound verb (1)**: {背負|せお}い{込|こ}む (to burden oneself with)

Notable features:
- Emotion/feeling cluster: {嫌悪感|けんおかん}, {不快感|ふかいかん}, {野心|やしん}, {無慈悲|むじひ}
- Physical/figurative duality: {喘|あえ}ぐ (2: gasping + struggling under hardship), {回|まわ}り{道|みち} (2: physical detour + roundabout approach), {奮発|ふんぱつ} (2: splurging + exerting oneself)
- Compound verbs: かき{混|ま}ぜる, {洗|あら}い{流|なが}す, {取|と}り{壊|こわ}す, {背負|せお}い{込|こ}む
- Legal: {忌避|きひ} (avoidance + legal recusal), {草案|そうあん}

Total entries: ~15,794 → ~15,824 (approximate)
Remaining candidates: ~3,978 → ~3,948 (30 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 398)
Added 30 new dictionary entries (IDs 15709-15738) from candidate_words.json:

- **Nouns (14)**: {軽食|けいしょく} (light meal), {身元|みもと} (identity), {領土|りょうど} (territory), {見晴|みは}らし (view), {一式|いっしき} (complete set), {猛獣|もうじゅう} (wild beast), {監獄|かんごく} (prison), {皇太子|こうたいし} (crown prince), {一区切|ひとくぎ}り (pause/milestone), {浅瀬|あさせ} (shoal), {自営業|じえいぎょう} (self-employment), {満室|まんしつ} (no vacancy), {縁起物|えんぎもの} (lucky charm), {速度制限|そくどせいげん} (speed limit)
- **Noun/verb-suru (7)**: {束縛|そくばく} (restraint), {冷遇|れいぐう} (cold treatment), {点呼|てんこ} (roll call), {団結|だんけつ} (unity), {脱獄|だつごく} (prison break), {投獄|とうごく} (imprisonment), {逆走|ぎゃくそう} (wrong-way driving)
- **Noun/na-adjective (1)**: {怠慢|たいまん} (negligence)
- **Na-adjective (1)**: {不確実|ふかくじつ} (uncertain)
- **Noun/yojijukugo (2)**: {音信不通|おんしんふつう} (loss of contact), {意気消沈|いきしょうちん} (dejection)
- **Verb-godan (2)**: {労|ねぎら}う (to appreciate labor), {眩|くら}む (to be dizzy/dazzled)
- **Expression (2)**: {全力|ぜんりょく}を{尽|つ}くす (to do one's best), {何食|なにく}わぬ{顔|かお} (innocent look)
- **Adverb (1)**: {平然|へいぜん}と (calmly, nonchalantly)

Notable features:
- Law/prison cluster: {監獄|かんごく}, {脱獄|だつごく}, {投獄|とうごく}
- Transportation: {逆走|ぎゃくそう}, {速度制限|そくどせいげん}
- Behavioral/emotional: {束縛|そくばく}, {意気消沈|いきしょうちん}, {何食|なにく}わぬ{顔|かお}, {平然|へいぜん}と
- Cultural: {縁起物|えんぎもの}, {皇太子|こうたいし}
- Multi-sense entry: {眩|くら}む (2: dizziness + being dazzled/blinded by greed)

Total entries: ~15,764 → ~15,794 (approximate)
Remaining candidates: ~4,008 → ~3,978 (30 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 397)
Added 30 new dictionary entries (IDs 15679-15708) from candidate_words.json:

- **Nouns (19)**: {苗木|なえぎ} (sapling), {感染症|かんせんしょう} (infectious disease), {平屋|ひらや} (one-story house), {備考|びこう} (remarks), {退職届|たいしょくとどけ} (resignation letter), {原本|げんぽん} (original document), {陶磁器|とうじき} (ceramics), {曲芸|きょくげい} (acrobatics), {密猟|みつりょう} (poaching), {潜水艦|せんすいかん} (submarine), {空母|くうぼ} (aircraft carrier), {異文化|いぶんか} (different culture), {茶托|ちゃたく} (teacup saucer), {定款|ていかん} (articles of incorporation), {被害届|ひがいとどけ} (damage report), {操縦席|そうじゅうせき} (cockpit), {箱推|はこお}し (supporting entire group), {四捨五入|ししゃごにゅう} (rounding), {踏|ふ}み{倒|たお}し (defaulting on debt)
- **Noun with two senses (2)**: {報|むく}い (reward/retribution), {死角|しかく} (blind spot)
- **Noun/na-adjective (1)**: {太|ふと}っ{腹|ぱら} (generous)
- **Adjective-i (1)**: {輝|かがや}かしい (brilliant)
- **Adjective-taru (1)**: {騒然|そうぜん} (tumultuous)
- **Pre-noun adjectival (1)**: ありふれた (commonplace)
- **Noun/verb-suru (3)**: {思索|しさく} (contemplation), {追憶|ついおく} (reminiscence), {一段落|いちだんらく} (reaching a stopping point)
- **Noun (family) (1)**: {母性|ぼせい} (motherhood)
- **Adverb (1)**: {存分|ぞんぶん}に (to one's heart's content)

Notable features:
- Business/legal cluster: {備考|びこう}, {退職届|たいしょくとどけ}, {原本|げんぽん}, {定款|ていかん}, {被害届|ひがいとどけ}, {踏|ふ}み{倒|たお}し
- Military: {潜水艦|せんすいかん}, {空母|くうぼ}
- Culture: {陶磁器|とうじき}, {茶托|ちゃたく}, {箱推|はこお}し, {異文化|いぶんか}
- Multi-sense entries: {報|むく}い (2: reward + retribution), {死角|しかく} (2: physical + figurative)
- New kanji: 2,520 → 2,522 ({托|たく}, {款|かん})

Total entries: ~15,734 → ~15,764 (approximate)
Remaining candidates: ~4,037 → ~4,008 (29 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 396)
Added 30 new dictionary entries (IDs 15649-15678) from candidate_words.json:

- **Nouns (18)**: {高齢者|こうれいしゃ} (elderly person), {焼|や}き{芋|いも} (roasted sweet potato), {遺失物|いしつぶつ} (lost property), {保険金|ほけんきん} (insurance money), {資産|しさん} (assets), {無力感|むりょくかん} (helplessness), {手|て}ほどき (basic instruction), {苦労人|くろうにん} (person of hardship), {半月|はんつき} (half a month), {四字熟語|よじじゅくご} (four-character idiom), {貴社|きしゃ} (your company), {装丁|そうてい} (book design), {診察室|しんさつしつ} (examination room), {窓枠|まどわく} (window frame), {小論文|しょうろんぶん} (short essay), {城塞|じょうさい} (fortress), {背表紙|せびょうし} (book spine), {情報源|じょうほうげん} (information source)
- **Noun/na-adjective (1)**: {不規則|ふきそく} (irregular)
- **Noun/verb-suru (6)**: {完敗|かんぱい} (complete defeat), {突発|とっぱつ} (sudden outbreak), {道案内|みちあんない} (giving directions), {遮断|しゃだん} (cutoff/blocking), {中休|なかやす}み (mid-break), {定期検診|ていきけんしん} (periodic checkup)
- **Noun (work) (3)**: {年次|ねんじ} (annual), {試用期間|しようきかん} (probation period), {不採用|ふさいよう} (rejection)
- **Verb-godan (1)**: {打|う}ち{負|ま}かす (to defeat)
- **Adverb (1)**: けろりと (nonchalantly; completely recovering)

Notable features:
- Business/work cluster: {年次|ねんじ}, {貴社|きしゃ}, {試用期間|しようきかん}, {不採用|ふさいよう}, {資産|しさん}, {保険金|ほけんきん}
- Medical: {診察室|しんさつしつ}, {定期検診|ていきけんしん}, {高齢者|こうれいしゃ}
- Books/publishing: {装丁|そうてい}, {背表紙|せびょうし}, {小論文|しょうろんぶん}
- Culture/food: {焼|や}き{芋|いも}, {四字熟語|よじじゅくご}
- Multi-sense entries: けろりと (2: nonchalant + complete recovery), {年次|ねんじ} (2: annual + year of service)

Total entries: ~15,704 → ~15,734 (approximate)
Remaining candidates: ~4,067 → ~4,037 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
