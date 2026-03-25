# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-25
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-25 (Vocabulary Expansion - 30 New Entries, Session 500)
Added 30 new dictionary entries (IDs 19337-19366) from candidate_words.json. A diverse mix of single-kanji words, common nouns, verbs, and expressions.

- **Single-kanji nouns (18)**: {鮭|さけ} (salmon), {串|くし} (skewer), {芝|しば} (turf), {刃|やいば} (blade), {芸|げい} (art/trick), {吉|きち} (good fortune), {凶|きょう} (bad luck), {乳|ちち} (milk/breast), {腸|ちょう} (intestine), {雫|しずく} (droplet), {虜|とりこ} (captive/devotee), {某|ぼう} (a certain), {黄|き} (yellow), {王|おう} (king), {的|まと} (target), {要|かなめ} (linchpin), {魔|ま} (demon), {栓|せん} (stopper)
- **Multi-sense nouns (3)**: {錠|じょう} (lock/tablet, 2 senses), {節|せつ} (section/season/moderation, 3 senses), {表|ひょう} (table/chart)
- **Verbs (2)**: {難航|なんこう}する (to run into difficulties), {始動|しどう}する (to start up)
- **Other (7)**: {旧|きゅう} (old/former, prefix), {暦|こよみ} (calendar), {際|きわ} (edge/verge), {空模様|そらもよう} (weather conditions), {目|め}を{閉|と}じる (to close one's eyes), {抵抗感|ていこうかん} (reluctance), {主|あるじ} (master/host)
- **Multi-sense entries**: {刃|やいば} (2: blade/sword), {芸|げい} (2: art/trick), {乳|ちち} (2: milk/breast), {虜|とりこ} (2: captive/devotee), {王|おう} (2: king/champion), {際|きわ} (2: edge/critical moment), {魔|ま} (2: demon/magic), {錠|じょう} (2: lock/tablet), {節|せつ} (3: section/season/moderation)

4 new kanji added to kanji index: 某, 虜, 雫, 鮭
Topics covered: food, culture, nature, body, tool, emotion, language, society, time, religion
Total entries: ~19,141 → ~19,171 (approximate)
Remaining candidates: ~5,015 → ~4,985 (30 entries created)

### 2026-03-25 (Vocabulary Expansion - 19 New Entries, Session 499)
Added 19 new dictionary entries (IDs 19317-19336) from candidate_words.json. One candidate ({重宝|ちょうほう}する) was discovered as a duplicate of entry 14415 and removed.

- **Nouns (5)**: {興味津々|きょうみしんしん} (very interested), {瓜|うり}{二|ふた}つ (spitting image), {茶飯事|さはんじ} (everyday occurrence), {大吉|だいきち} (great fortune), {隔月|かくげつ} (every other month)
- **Noun/Adjective (2)**: {手付|てつ}かず (untouched), {出不精|でぶしょう} (homebody)
- **Verbs (6)**: {一息|ひといき}つく (to take a breather), {差|さ}し{迫|せま}る (to be imminent), {飛|と}び{立|た}つ (to take off), {恩|おん}に{着|き}る (to feel grateful), {教|おし}え{込|こ}む (to instill), ほころぶ (to come apart/bloom/smile)
- **Adverbs (3)**: {心|こころ}なしか (somehow/perhaps), よっぽど (considerably), {折|おり}しも (just then)
- **Other (2)**: {気|き}が{晴|は}れる (to feel refreshed), {飲|の}み{歩|ある}く (to go bar-hopping), いかなる (what kind of/any)
- **Multi-sense entries**: ほころぶ (3: seam splitting / bud opening / breaking into smile), {飛|と}び{立|た}つ (2: take flight / set out), よっぽど (2: considerably / almost), いかなる (2: what kind of / whatever)

Topics covered: emotion, daily life, culture, time, food-drink, nature, education, language
Total entries: ~19,122 → ~19,141 (approximate)
Remaining candidates: ~5,035 → ~5,015 (19 entries created + 1 duplicate removed)

### 2026-03-25 (Vocabulary Expansion - 17 New Entries, Session 498)
Added 17 new dictionary entries (IDs 19299-19316) from candidate_words.json. One candidate (献身) was discovered as a duplicate of entry 10892 and removed.

- **Nouns (12)**: {第一印象|だいいちいんしょう} (first impression), {食洗機|しょくせんき} (dishwasher), {即効|そっこう} (immediate effect), {別料金|べつりょうきん} (extra charge), {好印象|こういんしょう} (good impression), {婚約指輪|こんやくゆびわ} (engagement ring), {義実家|ぎじっか} (in-laws' home), {重箱読|じゅうばこよ}み (on+kun reading), アライグマ (raccoon), {革|かわ} (leather), {日銀|にちぎん} (Bank of Japan), {順風|じゅんぷう} (tailwind)
- **Suru verbs (3)**: {公私混同|こうしこんどう} (mixing public/private), {方針転換|ほうしんてんかん} (policy shift), {自己|じこ}ＰＲ (self-promotion)
- **Verb (1)**: {息|いき}が{詰|つ}まる (to feel suffocated)
- **Suru verb (1)**: {転向|てんこう} (conversion/switching)
- **Multi-sense entries**: {息|いき}が{詰|つ}まる (2: physical choking / figurative stifling), {順風|じゅんぷう} (2: tailwind / smooth sailing), {転向|てんこう} (2: ideological conversion / switching fields)

Topics covered: social, household, money, relationships, language, nature, finance, politics, work, animals
Total entries: ~19,105 → ~19,122 (approximate)
Remaining candidates: ~5,052 → ~5,035 (17 entries created + 1 duplicate removed)

### 2026-03-25 (Vocabulary Expansion - 20 New Entries, Session 497)
Added 20 new dictionary entries (IDs 19279-19298) from candidate_words.json.

- **Nouns (13)**: {天丼|てんどん} (tempura rice bowl), {道順|みちじゅん} (route/directions), {厚紙|あつがみ} (cardboard), {子馬|こうま} (foal), {個数|こすう} (number of items), {専務|せんむ} (executive director), {濁音|だくおん} (voiced sound), {高卒|こうそつ} (high school graduate), {大卒|だいそつ} (university graduate), {無添加|むてんか} (additive-free), {非営利|ひえいり} (non-profit), {直属|ちょくぞく} (direct subordination), {愛護|あいご} (protection/welfare)
- **Suru verbs (4)**: {忘却|ぼうきゃく} (forgetting), {過食|かしょく} (overeating), {放電|ほうでん} (discharge), {想起|そうき} (recollection)
- **Multi-sense entries (3)**: {色気|いろけ} (2: sex appeal / ambition), {書|か}き{出|だ}し (2: opening sentence / data export), {黒星|くろぼし} (2: sports loss / black mark)

Topics covered: food, directions, education, business, animals, health, science, language, sports, society
Total entries: ~19,085 → ~19,105 (approximate)
Remaining candidates: ~5,072 → ~5,052 (20 entries created)

### 2026-03-25 (Vocabulary Expansion - 27 New Entries, Session 496)
Added 27 new dictionary entries (IDs 19249-19278) from candidate_words.json. Three candidates (限定, 拒絶, 抽出) were discovered as duplicates during validation and removed.

- **Nouns (11)**: {売|う}れ{筋|すじ} (best seller), {軽装|けいそう} (light clothing), {日刊|にっかん} (daily publication), {日当|にっとう} (daily allowance), {採寸|さいすん} (taking measurements), {万人|ばんにん}{受|う}け (mass appeal), {居住地|きょじゅうち} (place of residence), {俗説|ぞくせつ} (popular belief), {中編|ちゅうへん} (novella), {商号|しょうごう} (trade name), {最高潮|さいこうちょう} (climax)
- **Verbs/Expressions (9)**: {吹|ふ}っ{切|き}れる (to get over it), {思|おも}い{当|あ}たる (to come to mind), {買|か}い{叩|たた}く (to beat down price), {掛|か}け{違|ちが}える (to button wrongly/misunderstand), {浮|う}き{足|あし}{立|だ}つ (to panic), {振|ふ}り{出|だ}す (to issue), {一目|いちもく}{置|お}く (to acknowledge superiority), {感|かん}{極|きわ}まる (to be overcome with emotion), {板|いた}に{着|つ}く (to suit one well)
- **Adjective/Adverb (4)**: {常識的|じょうしきてき} (sensible), {何気|なにげ}なく (casually), {一端|いっぱし} (full-fledged), {汗|あせ}っかき (heavy sweater)
- **Other (3)**: {昼|ひる}どき (lunchtime), {定石|じょうせき} (standard approach), {平生|へいぜい} (ordinarily)
- **Multi-sense entries**: {限定|げんてい} duplicate removed, {掛|か}け{違|ちが}える (2: literal button/figurative misunderstanding), {中編|ちゅうへん} (2: novella/middle volume), {居住地|きょじゅうち} (2: address/residential area), {振|ふ}り{出|だ}す (2: issue check/shake out), {定石|じょうせき} (2: Go moves/established approach)

Topics covered: shopping, emotion, clothing, media, work, money, food, culture, literature, law, games
Total entries: ~19,058 → ~19,085 (approximate)
Remaining candidates: ~5,099 → ~5,072 (27 entries created)



---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
