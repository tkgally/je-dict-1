# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-22
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
| Total entries | ~12,695 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,896 (open) |
| Candidate words | ~435 |
| Cross-references | ~3,380 |
| Example sentences | ~45,150 |
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

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 295)
Added 30 new dictionary entries (IDs 12610-12639) from candidate_words.json:

- **Godan verbs (2)**: {悼|いた}む (to mourn/grieve), {憤|いきどおる} (to be indignant)
- **Ichidan verbs (3)**: {恵|めぐ}まれる (to be blessed with), {愛|め}でる (to admire beauty), {成|な}し{遂|と}げる (to accomplish)
- **Godan verb (1)**: {慈|いつく}しむ (to cherish tenderly)
- **I-adjective (1)**: {愛|いと}おしい (dear/lovable/precious)
- **Na-adjective (1)**: {悲惨|ひさん} (miserable/tragic)
- **Adverb (1)**: {幾度|いくど} (many times - literary)
- **Pronoun (1)**: {当方|とうほう} (we/our side - formal)
- **Nouns - emotion/abstract (5)**: {憧|あこが}れ (longing/yearning), {感性|かんせい} (sensibility), {恋愛|れんあい} (romantic love), {恥|はじ} (shame), {悪夢|あくむ} (nightmare)
- **Nouns - communication (3)**: {悲鳴|ひめい} (scream), {応酬|おうしゅう} (exchange of arguments), {後援|こうえん} (sponsorship)
- **Nouns - cognitive (3)**: {想定|そうてい} (assumption), {意向|いこう} (intention), {意図|いと} (aim/purpose)
- **Nouns - cultural (4)**: {彼岸|ひがん} (equinox/the other shore), {山門|さんもん} (temple gate), {懐石|かいせき} (kaiseki cuisine), {心中|しんじゅう} (double suicide)
- **Nouns - other (5)**: {役人|やくにん} (government official), {引|ひ}き{換|か}え (exchange), {懐|ふところ} (bosom/purse), {成熟|せいじゅく} (maturity), {戦闘|せんとう} (combat)

Notable features:
- Multi-sense entries: {引|ひ}き{換|か}え (exchange/in return for), {彼岸|ひがん} (equinox/Buddhist concept), {懐|ふところ} (bosom/finances)
- Cultural depth: {彼岸|ひがん} (equinox customs, Buddhist philosophy), {懐石|かいせき} (tea ceremony origins), {心中|しんじゅう} (Chikamatsu plays), {恥|はじ} (shame culture), {山門|さんもん} (Buddhist architecture)
- Strong emotion/psychology cluster: {愛|いと}おしい, {慈|いつく}しむ, {愛|め}でる, {憧|あこが}れ, {憤|いきどお}る, {悼|いた}む
- New kanji: 2,367 → 2,368 ({悼|とう})

Total entries: 12,665 → 12,695
Remaining candidates: 465 → 435 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 294)
Added 30 new dictionary entries (IDs 12580-12609) from candidate_words.json:

- **Godan verbs (7)**: {張|は}る (to stretch/spread/insist), {引|ひ}き{離|はな}す (to pull apart/leave behind), {悟|さと}る (to realize/attain enlightenment), {悩|なや}ます (to trouble/torment), {急|せ}かす (to rush someone), {怒鳴|どな}り{込|こ}む (to barge in yelling), {思|おも}い{立|た}つ (to resolve on impulse)
- **Ichidan verbs (2)**: {引|ひ}き{立|た}てる (to set off/promote), {惚|ほ}れる (to fall in love/be captivated)
- **I-adjective (1)**: {息苦|いきぐる}しい (suffocating/oppressive)
- **Na-adjective (1)**: {形式的|けいしきてき} (formal/perfunctory)
- **Adverbs (2)**: {往々|おうおう} (often/not uncommonly), {恐|おそ}る{恐|おそ}る (timidly/gingerly)
- **Nouns - workplace/social (5)**: {後任|こうにん} (successor), {後継者|こうけいしゃ} (heir/successor), {恩師|おんし} (former teacher/mentor), {後期|こうき} (latter period), {恒例|こうれい} (regular event)
- **Nouns - abstract (5)**: {後戻|あともど}り (turning back/regression), {底上|そこあ}げ (raising the level), {後付|あとづ}け (after-the-fact), {広義|こうぎ} (broad sense), {忠誠|ちゅうせい} (loyalty)
- **Nouns - culture (2)**: {忍|しの}び (stealth/ninja), {怪談|かいだん} (ghost story)
- **Nouns - other (3)**: {強者|つわもの} (formidable person), {山間|さんかん} (mountain area), {微量|びりょう} (trace amount)
- **Noun/suru verbs (2)**: {志向|しこう} (inclination/orientation), {心待|こころま}ち (eager anticipation)

Notable features:
- Multi-sense entries: {張|は}る (3 senses: stretch/tense/stubborn), {引|ひ}き{離|はな}す (pull apart/leave behind), {引|ひ}き{立|た}てる (enhance/promote), {形式的|けいしきてき} (procedural/perfunctory), {悟|さと}る (perceive/enlightenment), {惚|ほ}れる (romantic/non-romantic), {息苦|いきぐる}しい (physical/figurative), {後戻|あともど}り (physical/figurative), {忍|しの}び (stealth/ninja), {強者|つわもの} (competitor/warrior)
- Diverse word types: godan verbs, ichidan verbs, adjectives, adverbs, nouns, suru verbs
- Cross-references added: {後任|こうにん}↔{後継者|こうけいしゃ}, {広義|こうぎ}↔{狭義|きょうぎ}, {形式的|けいしきてき}↔{実質的|じっしつてき}, {張|は}る↔{貼|は}る, {後期|こうき}↔{前期|ぜんき}

Total entries: 12,635 → 12,665
Remaining candidates: 495 → 465 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 293)
Added 30 new dictionary entries (IDs 12550-12579) from candidate_words.json:

- **Ichidan verbs (3)**: {役立|やくだ}てる (to put to use), {従|したが}える (to be accompanied by), {徹|てっ}する (to devote oneself to)
- **Godan verbs (3)**: {志|こころざ}す (to aspire to), {思|おも}い{描|えが}く (to envision), {忍|しの}び{込|こ}む (to sneak in)
- **I-adjective (1)**: {快|こころよ}い (pleasant/willing)
- **Na-adjective (1)**: {忠実|ちゅうじつ} (faithful/loyal)
- **Adverb (1)**: {急遽|きゅうきょ} (suddenly/on short notice)
- **Nouns - abstract/descriptive (7)**: {当|あ}たり{外|はず}れ (hit or miss), {形態|けいたい} (form/configuration), {得体|えたい} (true nature), {念頭|ねんとう} (mind/keeping in mind), {思惑|おもわく} (speculation/ulterior motive), {心地|ここち} (feeling/sensation), {快挙|かいきょ} (remarkable feat)
- **Nouns - economics/society (4)**: {引|ひ}き{上|あ}げ (raise/withdrawal), {引|ひ}き{下|さ}げ (reduction/cut), {後半|こうはん} (second half), {後釜|あとがま} (successor)
- **Nouns - time (1)**: {後々|のちのち} (later on)
- **Nouns - role (1)**: {役|やく} (role/duty)
- **Noun/suru verbs (5)**: {後退|こうたい} (retreat/decline), {強行|きょうこう} (forcing through), {従事|じゅうじ} (engaging in), {復帰|ふっき} (return/comeback), {復活|ふっかつ} (revival/resurrection)
- **Noun/na-adjective (1)**: {得|とく} (profit/economical)
- **Noun (1)**: {底|そこ} (bottom/depths)
- **Noun (1)**: {微笑|ほほえ}み (smile)

Notable features:
- Multi-sense entries: {引|ひ}き{上|あ}げ (increase/repatriation), {後退|こうたい} (physical retreat/figurative decline), {復活|ふっかつ} (revival/resurrection), {快|こころよ}い (pleasant/willing), {忠実|ちゅうじつ} (loyal/accurate), {徹|てっ}する (devote oneself/last through), {得|とく} (profit/bargain), {底|そこ} (physical bottom/figurative depths), {思惑|おもわく} (expectation/ulterior motive), {役|やく} (acting role/duty)
- Diverse word types: ichidan verbs, godan verbs, suru verbs, adjectives, adverbs, nouns
- New kanji: 2,366 → 2,367 ({遽|きょ})

Total entries: 12,605 → 12,635
Remaining candidates: 525 → 495 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 292)
Added 30 new dictionary entries (IDs 12520-12549) from candidate_words.json:

- **Na-adjectives (2)**: {強固|きょうこ} (firm/solid), {強硬|きょうこう} (hardline/unyielding)
- **I-adjective (1)**: {後|うし}ろめたい (feeling guilty/uneasy)
- **Godan verbs (2)**: {彩|いろど}る (to color/decorate), {建|た}つ (to be built)
- **Nouns - geography/nature (3)**: {山岳|さんがく} (mountains), {山村|さんそん} (mountain village), {山地|さんち} (mountainous area — replaced with {広域|こういき})
- **Nouns - history/culture (4)**: {幕末|ばくまつ} (end of Edo period), {家元|いえもと} (grand master of traditional art), {宮廷|きゅうてい} (imperial court), {屋号|やごう} (trade name/kabuki stage name)
- **Nouns - society/governance (4)**: {弱者|じゃくしゃ} (the weak), {当局|とうきょく} (the authorities), {年功序列|ねんこうじょれつ} (seniority system), {廃校|はいこう} (school closure)
- **Nouns - food/nature (2)**: {小松菜|こまつな} (komatsuna), {山賊|さんぞく} (mountain bandit)
- **Nouns - abstract/descriptive (5)**: {巨体|きょたい} (huge physique), {序章|じょしょう} (prologue), {彷彿|ほうふつ} (reminiscent), {当|あ}て{字|じ} (ateji), {座談会|ざだんかい} (round-table discussion)
- **Nouns - arts/theater (1)**: {小道具|こどうぐ} (props)
- **Noun/suru verbs (6)**: {大量生産|たいりょうせいさん} (mass production), {定住|ていじゅう} (permanent residence), {強要|きょうよう} (coercion), {形成|けいせい} (formation), {待望|たいぼう} (long-awaited), {征服|せいふく} (conquest)

Notable features:
- Multi-sense entries: {小道具|こどうぐ} (theater props/small tools), {屋号|やごう} (shop name/kabuki stage name), {彩|いろど}る (color/embellish), {征服|せいふく} (military conquest/figurative mastery)
- Cultural context: {家元|いえもと} (iemoto system), {幕末|ばくまつ} (Bakumatsu era), {屋号|やごう} (kabuki calling names), {年功序列|ねんこうじょれつ} (Japanese employment), {山賊|さんぞく} (sanzoku-yaki dish), {廃校|はいこう} (rural repurposing trend)
- Diverse word types: adjectives (na/i), godan verbs, suru verbs, formal nouns, cultural terms
- New kanji: 2,361 → 2,366 ({岳|がく}, {廷|てい}, {彷|ほう}, {彿|ふつ}, {征|せい})

Total entries: 12,575 → 12,605
Remaining candidates: 555 → 525 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 291)
Added 30 new dictionary entries (IDs 12490-12519) from candidate_words.json:

- **Adverbs (3)**: {引|ひ}き{続|つづ}き (continuously/subsequently), {当初|とうしょ} (initially), {後日|ごじつ} (another day)
- **Na-adjectives (3)**: {小規模|しょうきぼ} (small-scale), {必須|ひっす} (essential/mandatory), {強欲|ごうよく} (greedy/avaricious)
- **I-adjective (1)**: {心地|ここち}よい (comfortable/pleasant)
- **Godan verbs (1)**: {微睡|まどろ}む (to doze/slumber)
- **Ichidan verb (1)**: {張|は}りつめる (to be taut/tense)
- **Nouns - occupation (2)**: {庭師|にわし} (gardener), {家政婦|かせいふ} (housekeeper)
- **Nouns - social/political (2)**: {少数派|しょうすうは} (minority group), {当事者|とうじしゃ} (person concerned)
- **Nouns - abstract/formal (6)**: {弱点|じゃくてん} (weak point), {強み|つよみ} (strength/forte), {形見|かたみ} (keepsake/memento), {彩|いろど}り (coloring/variety), {従来|じゅうらい} (conventional), {待遇|たいぐう} (treatment/conditions)
- **Nouns - time/period (2)**: {幼少|ようしょう} (childhood), {後味|あとあじ} (aftertaste)
- **Nouns - other (2)**: {幕|まく} (curtain/act), {弾丸|だんがん} (bullet)
- **Noun/suru verbs (7)**: {強制|きょうせい} (compulsion), {強奪|ごうだつ} (robbery), {後押|あとお}し (support/backing), {復讐|ふくしゅう} (revenge), {寵愛|ちょうあい} (favor/doting), {延焼|えんしょう} (fire spread), {待遇|たいぐう} (treatment)

Notable features:
- Multi-sense entries: {張|は}りつめる (taut/tense), {彩|いろど}り (coloring/variety), {後味|あとあじ} (literal/figurative aftertaste), {幕|まく} (curtain/act), {待遇|たいぐう} (treatment/compensation), {引|ひ}き{続|つづ}き (continuously/subsequently), {従来|じゅうらい} (conventional/up to now)
- Cultural context: {庭師|にわし} (traditional Japanese garden craft), {幕|まく} (kabuki theater/Edo period compounds), {形見|かたみ} ({形見|かたみ}{分|わ}け custom), {家政婦|かせいふ} (agency-based services)
- Diverse word types: adjectives, verbs, adverbs, suru verbs, formal nouns
- New kanji: 2,359 → 2,361 ({寵|ちょう}, {讐|しゅう})

Total entries: 12,545 → 12,575
Remaining candidates: 585 → 555 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
