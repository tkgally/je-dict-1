# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-11
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
| Total entries | ~16,332 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,533 (open) |
| Candidate words | ~3,445 |
| Cross-references | ~3,400 |
| Example sentences | ~49,200 |
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

### 2026-03-11 (Vocabulary Expansion - 30 New Entries, Session 416)
Added 30 new dictionary entries (IDs 16253-16282) from candidate_words.json:

- **Nouns (14)**: {備品|びひん} (equipment), {起点|きてん} (starting point), {月刊|げっかん} (monthly publication), {交通渋滞|こうつうじゅうたい} (traffic jam), {自動改札機|じどうかいさつき} (automatic ticket gate), {地産地消|ちさんちしょう} (local production/consumption), {自給自足|じきゅうじそく} (self-sufficiency), {拳銃|けんじゅう} (handgun), {生野菜|なまやさい} (raw vegetables), {通話料|つうわりょう} (call charges), {労働力|ろうどうりょく} (labor force), {幸福感|こうふくかん} (sense of happiness), {冷食|れいしょく} (frozen food), {二泊三日|にはくみっか} (3 days 2 nights)
- **Nouns/suru verbs (3)**: {全快|ぜんかい} (complete recovery), {改行|かいぎょう} (line break), {口座開設|こうざかいせつ} (opening a bank account)
- **Nouns/adjective-no (3)**: {生乾|なまがわ}き (half-dried), {中規模|ちゅうきぼ} (medium-scale), {高性能|こうせいのう} (high performance)
- **Expressions (4)**: {嫌気|いやけ}が{差|さ}す (to be fed up), {席|せき}を{譲|ゆず}る (to give up one's seat), お{暇|いとま}する (to take one's leave), {手際|てぎわ}のいい (efficient)
- **Nouns (other) (3)**: {仕切|しき}り{直|なお}し (fresh start), {運任|うんまか}せ (trusting to luck), {三十日|みそか} (last day of month)
- **Verb (1)**: {盛|も}り{立|た}てる (to liven up)
- **Proper noun (1)**: {東南|とうなん}アジア (Southeast Asia)
- **Onomatopoeia (1)**: けらけら (cackling laughter)

Notable features:
- Daily life: {生乾|なまがわ}き, {冷食|れいしょく}, {生野菜|なまやさい}, {交通渋滞|こうつうじゅうたい}
- Travel: {二泊三日|にはくみっか}, {自動改札機|じどうかいさつき}, {東南|とうなん}アジア
- Business/economy: {備品|びひん}, {口座開設|こうざかいせつ}, {労働力|ろうどうりょく}
- Society: {地産地消|ちさんちしょう}, {自給自足|じきゅうじそく}, {幸福感|こうふくかん}
- Multi-sense: {席|せき}を{譲|ゆず}る (2: literal seat + figurative position), {盛|も}り{立|た}てる (2: enliven + support)

Total entries: ~16,302 → ~16,332 (approximate)
Remaining candidates: ~3,475 → ~3,445 (30 removed)

### 2026-03-11 (Vocabulary Expansion - 30 New Entries, Session 415)
Added 30 new dictionary entries (IDs 16223-16252) from candidate_words.json:

- **Nouns (15)**: {願書|がんしょ} (application form), {鼻詰|はなづ}まり (stuffy nose), {遮断機|しゃだんき} (crossing gate), {書庫|しょこ} (archive/stacks), {講義室|こうぎしつ} (lecture room), {投資家|とうしか} (investor), {守秘義務|しゅひぎむ} (duty of confidentiality), {十代|じゅうだい} (teens), {一戦|いっせん} (a match/battle), {排水口|はいすいこう} (drain), {警報機|けいほうき} (alarm device), {開放感|かいほうかん} (sense of openness), {実技|じつぎ} (practical skill), {自己啓発|じこけいはつ} (self-development), {生唾|なまつば} (saliva from anticipation)
- **Nouns/verb-suru (6)**: {適任|てきにん} (well-qualified), {返礼|へんれい} (return gift), {切磋琢磨|せっさたくま} (friendly rivalry), {過信|かしん} (overconfidence), {弱体化|じゃくたいか} (weakening), {封入|ふうにゅう} (enclosure), {列席|れっせき} (formal attendance)
- **Verbs (3)**: {張|は}り{合|あ}う (to compete), {預|あず}け{入|い}れる (to deposit), ガタつく (to rattle/become unstable)
- **Adverbs (2)**: {一貫|いっかん}して (consistently), {絶|た}え{間|ま}なく (incessantly)
- **Pre-noun adjectival (1)**: {並外|なみはず}れた (extraordinary)
- **Historical (2)**: {仇討|あだう}ち (vengeance), {倒幕|とうばく} (overthrowing shogunate)

Notable features:
- Multi-sense: ガタつく (2: rattle + become unstable), {預|あず}け{入|い}れる (2: deposit money + check luggage)
- Business/legal: {守秘義務|しゅひぎむ}, {投資家|とうしか}, {自己啓発|じこけいはつ}
- Daily life: {鼻詰|はなづ}まり, {排水口|はいすいこう}, {遮断機|しゃだんき}, {警報機|けいほうき}
- Culture/history: {仇討|あだう}ち, {倒幕|とうばく}, {返礼|へんれい}, {切磋琢磨|せっさたくま}
- New kanji: 2,527 → 2,529 (琢, 磋)

Total entries: ~16,272 → ~16,302 (approximate)
Remaining candidates: ~3,505 → ~3,475 (30 removed)

### 2026-03-11 (Vocabulary Expansion - 30 New Entries, Session 414)
Added 30 new dictionary entries (IDs 16193-16222) from candidate_words.json:

- **Nouns (14)**: {城跡|しろあと} (castle ruins), {太巻|ふとま}き (thick sushi roll), {洞穴|ほらあな} (cave), {体格|たいかく} (physique), {力作|りきさく} (painstaking work), ぬかるみ (muddy ground), {怒号|どごう} (angry roar), {人影|ひとかげ} (figure/sign of people), {仕事納|しごとおさ}め (last working day), {投|な}げ{売|う}り (fire sale), {夜行性|やこうせい} (nocturnal), {粘|ねば}り{気|け} (stickiness/tenacity), {三|さん}が{日|にち} (first three days of year), {昼下|ひるさ}がり (early afternoon)
- **Nouns/verb-suru (6)**: {起業|きぎょう} (entrepreneurship), {配合|はいごう} (blending), {閉口|へいこう} (being stumped), {目隠|めかく}し (blindfold), やりくり (making do), {癒着|ゆちゃく} (adhesion/collusion)
- **Na-adjectives (2)**: {貧弱|ひんじゃく} (poor/meager), {物騒|ぶっそう} (dangerous/unsafe)
- **I-adjective (1)**: {卑|いや}しい (lowly/vulgar/greedy)
- **Verbs (3)**: おどける (to joke around), うろつく (to loiter), ハッとする (to be startled)
- **Noun/verb-suru (2)**: {棄権|きけん} (abstention/withdrawal), {独|ひと}り{立|だ}ち (becoming independent)
- **Mimetic (1)**: ぐらぐら (wobbly/boiling vigorously)

Notable features:
- Good POS variety: nouns, verbs, adjectives, mimetic words
- Multi-sense: {棄権|きけん} (2: voting + sports), {卑|いや}しい (2: lowly + greedy), {物騒|ぶっそう} (2: dangerous + alarming), {目隠|めかく}し (2: blindfold + screen), {粘|ねば}り{気|け} (2: sticky + tenacious), {癒着|ゆちゃく} (2: medical + political), ハッとする (2: startled + realization), ぐらぐら (2: wobbly + boiling), {人影|ひとかげ} (2: figure + sign of people)
- Cultural: {三|さん}が{日|にち} (New Year), {仕事納|しごとおさ}め (year-end), {太巻|ふとま}き (sushi culture)
- Daily life: やりくり, ぐらぐら, {昼下|ひるさ}がり, うろつく
- Business/politics: {起業|きぎょう}, {投|な}げ{売|う}り, {癒着|ゆちゃく}

Total entries: ~16,242 → ~16,272 (approximate)
Remaining candidates: ~3,534 → ~3,505 (29 removed)

### 2026-03-11 (Vocabulary Expansion - 30 New Entries, Session 413)
Added 30 new dictionary entries (IDs 16161-16192) from candidate_words.json:

- **Nouns (17)**: {献血|けんけつ} (blood donation), {難関|なんかん} (barrier), {感嘆|かんたん} (admiration), {変形|へんけい} (transformation), {着手|ちゃくしゅ} (commencing), {免税店|めんぜいてん} (duty-free shop), {照会|しょうかい} (inquiry), {参観|さんかん} (observation visit), {形相|ぎょうそう} (grimace), {遠浅|とおあさ} (shallow shore), {下校|げこう} (leaving school), {聖火|せいか} (Olympic flame), {食|く}いしん{坊|ぼう} (glutton), {肩車|かたぐるま} (shoulder ride), {額縁|がくぶち} (picture frame), {悪天候|あくてんこう} (bad weather), {球団|きゅうだん} (baseball team)
- **Na-adjective (1)**: {冷淡|れいたん} (cold, indifferent)
- **Nouns (multi-sense) (2)**: {水玉|みずたま} (2: polka dots + water droplet), {目|め}を{細|ほそ}める (2: squint + look fondly)
- **Verbs (3)**: {着|き}こなす (to wear well), {放|ほう}り{出|だ}す (to throw out/abandon), {作|つく}り{替|か}える (to remake)
- **Noun (other) (3)**: {経営者|けいえいしゃ} (business owner), {限定品|げんていひん} (limited edition), {主将|しゅしょう} (team captain)
- **Expressions (2)**: {挙句|あげく}の{果|は}て (in the end), {目|め}を{細|ほそ}める (to squint/look fondly)
- **Verb (2-sense) (2)**: {放|ほう}り{出|だ}す (2: throw out + abandon), {建|た}て{直|なお}す (2: rebuild + reorganize)
- **Noun (cultural) (1)**: {一見|いちげん}さん (first-time customer)

Notable features:
- Good POS variety: nouns, verbs, na-adjective, expressions
- Cultural: {一見|いちげん}さん (Kyoto customer culture), {聖火|せいか} (Olympics), {食|く}いしん{坊|ぼう} (food culture)
- Sports: {球団|きゅうだん}, {主将|しゅしょう}
- Education: {下校|げこう}, {参観|さんかん}
- Business: {着手|ちゃくしゅ}, {経営者|けいえいしゃ}, {照会|しょうかい}
- Shopping/travel: {免税店|めんぜいてん}, {限定品|げんていひん}

Total entries: ~16,212 → ~16,242 (approximate)
Remaining candidates: ~3,564 → ~3,534 (30 removed)

### 2026-03-10 (Vocabulary Expansion - 30 New Entries, Session 412)
Added 30 new dictionary entries (IDs 16131-16160) from candidate_words.json:

- **Nouns (20)**: {誤字|ごじ} (typo), {自我|じが} (self/ego), {不和|ふわ} (discord), {締|し}め (closing/final dish), デマ (false rumor), {競|せ}り (auction), {揺|ゆ}れ (shaking), {毛穴|けあな} (pore), つまみ (drinking snack/knob), {背丈|せたけ} (stature), {熱気|ねっき} (heat/fervor), {総務|そうむ} (general affairs), {世論|よろん} (public opinion), {顧問|こもん} (advisor), {小言|こごと} (nagging), {余震|よしん} (aftershock), {可否|かひ} (approval), {老舗|しにせ} (long-established shop), {画質|がしつ} (image quality), {安否|あんぴ} (safety), {産毛|うぶげ} (downy hair), {公募|こうぼ} (open recruitment), {既婚|きこん} (married), {師走|しわす} (December), {牙|きば} (fang), {音痴|おんち} (tone-deaf)
- **Verbs (3)**: {見入|みい}る (to gaze at), {蒸|む}らす (to steam/let rest), {背負|せお}う (to carry on back)
- **Adverb (1)**: {随時|ずいじ} (at any time)

Notable features:
- Good POS variety: nouns, verbs, adverb, with multiple senses on つまみ, {締|し}め, {熱気|ねっき}, {音痴|おんち}, {背負|せお}う
- Cultural: {老舗|しにせ}, {師走|しわす}, {競|せ}り (fish market auctions), {締|し}め (final dish), つまみ (izakaya culture)
- Disaster vocabulary: {余震|よしん}, {揺|ゆ}れ, {安否|あんぴ}
- Modern/digital: {画質|がしつ}, デマ, {公募|こうぼ}
- New kanji: 2,526 → 2,527 ({牙|きば})

Total entries: ~16,182 → ~16,212 (approximate)
Remaining candidates: ~3,594 → ~3,564 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
