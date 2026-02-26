# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-26
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
| Total entries | ~13,694 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,895 (open) |
| Candidate words | ~6,075 |
| Cross-references | ~3,400 |
| Example sentences | ~47,200 |
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

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 328)
Added 30 new dictionary entries (IDs 13609-13638) from candidate_words.json:

- **Health/illness cluster (7)**: {疫病|えきびょう} (epidemic), {病|やまい} (illness), {病|や}む (to be ill), {病弱|びょうじゃく} (sickly), {痛|いた}める (to hurt), {痛感|つうかん} (keenly feeling), {療法|りょうほう} (therapy)
- **Healing (1)**: {癒|いや}す (to heal)
- **四字熟語 (1)**: {疲労困憊|ひろうこんぱい} (total exhaustion)
- **Cognition/language (3)**: {目撃|もくげき} (witnessing), {直訳|ちょくやく} (literal translation), {疑似|ぎじ} (pseudo/simulated)
- **Descriptive (2)**: {目覚|めざま}ましい (remarkable), {盛大|せいだい} → replaced by {発祥|はっしょう} (origin/birthplace)
- **Food (2)**: {田楽|でんがく} (dengaku), ラード (lard)
- **People (3)**: {猛者|もさ} (tough guy), {痴漢|ちかん} (groper), {王妃|おうひ} (queen consort)
- **General nouns (4)**: {物販|ぶっぱん} (merchandise sales), {法|ほう} (law/method), {渡|わた}り (crossing), {白紙|はくし} (blank paper/clean slate)
- **Scene/stage (1)**: {登場|とうじょう} (appearance/entrance)
- **Loanwords (5)**: ライト (light), リストアップ (listing), レーベル (music label), リニア (maglev), ファクス (fax)
- **Person (1)**: レディ (lady)

Notable features:
- Health/illness cluster: 7 related entries covering epidemic, illness, constitution, pain, therapy
- Multi-sense entries: {病|やまい} (2: illness + bad habit), {病|や}む (2: physical + mental), {痛|いた}める (2: physical + emotional), {癒|いや}す (2: heal + soothe), ライト (2: light device + casual), {白紙|はくし} (2: blank paper + clean slate), {法|ほう} (2: law + method), {渡|わた}り (2: crossing + opportunity), レーベル (2: music label + product label), リニア (2: maglev + linear)
- Cultural: {痴漢|ちかん} (women-only train cars), ファクス (Japan's fax culture), {田楽|でんがく} (traditional cuisine), ラード (ramen culture)
- Wasei-eigo: リストアップ (list up — not standard English)
- Modern slang: {病|や}んでる (mentally unwell, youth language)
- New kanji: 2,413 → 2,416 ({妃|ひ}, {憊|はい}, {祥|しょう})

Total entries: 13,664 → 13,694 (approximate)
Remaining candidates: 6,105 → 6,075 (30 removed)

### 2026-02-26 (Vocabulary Expansion - 30 New Entries, Session 327)
Added 30 new dictionary entries (IDs 13579-13608) from candidate_words.json:

- **Government/town cluster (3)**: {町役場|まちやくば} (town hall), {町長|ちょうちょう} (town mayor), {町人|ちょうにん} (townsperson)
- **Royalty cluster (3)**: {王位|おうい} (throne), {王族|おうぞく} (royalty), {王立|おうりつ} (royal)
- **画- cluster (3)**: {画数|かくすう} (stroke count), {画一的|かくいつてき} (uniform/standardized), {画策|かくさく} (scheming)
- **疑- cluster (2)**: {疑わしい|うたがわしい} (suspicious/doubtful), {疑惑|ぎわく} (suspicion)
- **Tea/food cluster (4)**: {玉露|ぎょくろ} (gyokuro tea), {烏龍|うーろん} (oolong), {白菜|はくさい} (Chinese cabbage), {発酵|はっこう} (fermentation)
- **Health/body (2)**: {疲労|ひろう} (fatigue), {癒し|いやし} (healing/comfort)
- **History/military (2)**: {爆撃|ばくげき} (bombing), {疎開|そかい} (wartime evacuation)
- **Other nouns (8)**: {無所属|むしょぞく} (independent/unaffiliated), {男爵|だんしゃく} (baron), {異名|いみょう} (epithet), {男気|おとこぎ} (chivalry), {瓜|うり} (melon/gourd), {炉|ろ} (furnace/hearth), {牢|ろう} (prison), {皇居|こうきょ} (Imperial Palace)
- **Loanword (1)**: リカバリー (recovery)
- **Na-adjective (1)**: {無惨|むざん} (cruel/tragic)
- **Godan verb (1)**: {盛り込む|もりこむ} (to incorporate)

Notable features:
- Multi-sense entries: {疑わしい|うたがわしい} (2: doubtful + suspicious), {男爵|だんしゃく} (2: baron + potato), {無惨|むざん} (2: cruel + tragic/pitiful), {盛り込む|もりこむ} (2: incorporate + heap into)
- Government cluster: {町役場|まちやくば}/{町長|ちょうちょう}/{町人|ちょうにん} with context on Japan's municipal hierarchy
- Tea culture: {玉露|ぎょくろ} (brewing temperature), {烏龍|うーろん} (izakaya culture)
- Cultural: {皇居|こうきょ} (Imperial Palace jogging/visits), {男気|おとこぎ}じゃんけん, {画数|かくすう} (name fortune-telling)
- Historical: {町人|ちょうにん} (Edo merchant class), {疎開|そかい} (wartime evacuation), {男爵|だんしゃく} (Meiji peerage)
- New kanji: 2,411 → 2,413 ({酵|こう}, {龍|りゅう})

Total entries: 13,634 → 13,664 (approximate)
Remaining candidates: 6,135 → 6,105 (30 removed)

### 2026-02-25 (Vocabulary Expansion - 30 New Entries, Session 326)
Added 30 new dictionary entries (IDs 13549-13578) from candidate_words.json:

- **異- cluster (8)**: {異様|いよう} (bizarre), {異論|いろん} (dissenting opinion), {異議|いぎ} (objection), {異例|いれい} (exceptional), {異性|いせい} (opposite sex), {異質|いしつ} (heterogeneous), {異端|いたん} (heresy)
- **略- cluster (3)**: {略称|りゃくしょう} (abbreviation), {略歴|りゃくれき} (brief bio), {略奪|りゃくだつ} (plunder)
- **特- cluster (2)**: {特異|とくい} (peculiar), {特段|とくだん} (particularly)
- **現- cluster (2)**: {現時点|げんじてん} (at this point), {現物|げんぶつ} (the real thing)
- **町- cluster (2)**: {町内|ちょうない} (neighborhood), {町|まち}おこし (town revitalization)
- **I-adjective (1)**: {甲高|かんだか}い (shrill)
- **Na-adjective/noun (1)**: {男前|おとこまえ} (handsome/cool)
- **Noun/suru verbs (4)**: {疎外|そがい} (alienation), {産卵|さんらん} (egg-laying), {生還|せいかん} (survival), {畏怖|いふ} (awe)
- **Other nouns (7)**: {画像|がぞう} (image), {理事|りじ} (director), {申|もう}し{出|で} (offer), {甘味|かんみ} (sweetness/dessert), {無形|むけい} (intangible), {生協|せいきょう} (co-op), {用例|ようれい} (usage example)

Notable features:
- 異- cluster: 7 entries covering deviation, dissent, formality, gender, nature, and doctrine
- Multi-sense entries: {現物|げんぶつ} (2: real thing + spot goods), {生還|せいかん} (2: survival + baseball scoring), {甘味|かんみ} (2: sweetness + dessert), {男前|おとこまえ} (2: handsome + admirably bold)
- Formal register: {異議|いぎ} (courtroom), {異論|いろん} (meetings), {現時点|げんじてん} (news/business), {特段|とくだん} (official), {略歴|りゃくれき} (professional), {理事|りじ} (governance)
- Cultural: {町|まち}おこし (regional revitalization movement), {甘味|かんみ}{処|どころ} (traditional sweets shops), {生協|せいきょう} (university co-ops), {無形|むけい}{文化|ぶんか}{財|ざい} (UNESCO heritage)
- Homophone cross-refs: {異議|いぎ}↔{意義|いぎ}, {特異|とくい}↔{得意|とくい}, {異性|いせい}↔{威勢|いせい}

Total entries: 13,604 → 13,634 (approximate)
Remaining candidates: 6,165 → 6,135 (30 removed)

### 2026-02-25 (Vocabulary Expansion - 30 New Entries, Session 325)
Added 30 new dictionary entries (IDs 13519-13548) from candidate_words.json:

- **Food noun (1)**: {甘酒|あまざけ} (amazake)
- **I-adjective (1)**: {甚|はなは}だしい (extreme, excessive)
- **Godan verbs (2)**: {生|い}き{残|のこ}る (to survive), {生|う}まれ{変|か}わる (to be reborn)
- **生- cluster (4)**: {生業|なりわい} (livelihood), {生計|せいけい} (living), {生息|せいそく} (inhabiting), {生態|せいたい} (ecology)
- **Na-adjectives (2)**: {無作法|ぶさほう} (ill-mannered), {無様|ぶざま} (unsightly)
- **王- cluster (3)**: {王宮|おうきゅう} (royal palace), {王者|おうじゃ} (king/champion), {王家|おうけ} (royal family)
- **特- cluster (2)**: {特製|とくせい} (specially made), {特質|とくしつ} (characteristic)
- **Noun/suru verbs (3)**: {献上|けんじょう} (offering), {現存|げんそん} (extant), {混濁|こんだく} (turbidity)
- **Other nouns (12)**: {甥|おい} (nephew), {用品|ようひん} (supplies), {田畑|たはた} (farmland), {深紅|しんく} (crimson), {火消|ひけ}し (firefighter/damage control), {物欲|ぶつよく} (materialism), {狭義|きょうぎ} (narrow sense), {産声|うぶごえ} (first cry), {産物|さんぶつ} (product), {用心棒|ようじんぼう} (bodyguard), {用法|ようほう} (usage), {瓢箪|ひょうたん} (gourd)

Notable features:
- 生- cluster: 4 entries covering livelihood, living, inhabiting, and ecology
- 王- cluster: 3 entries covering palaces, champions, and royal families
- Multi-sense entries: {生|い}き{残|のこ}る (2: physical + competitive survival), {生|う}まれ{変|か}わる (2: reincarnation + transformation), {火消|ひけ}し (2: historical firefighter + damage control), {産声|うぶごえ} (2: literal first cry + figurative founding), {産物|さんぶつ} (2: physical product + result of circumstances), {王者|おうじゃ} (2: king + champion), {用心棒|ようじんぼう} (2: bodyguard + door bar), {混濁|こんだく} (2: turbidity + confusion)
- Cultural: {甘酒|あまざけ} (New Year's shrine drink), {瓢箪|ひょうたん} (Hideyoshi's emblem, proverb), {火消|ひけ}し (Edo firefighters), {献上|けんじょう} (imperial offerings), {用心棒|ようじんぼう} (Kurosawa film)
- New kanji: 2,410 → 2,411 ({甥|せい})

Total entries: 13,574 → 13,604 (approximate)
Remaining candidates: 6,195 → 6,165 (30 removed)

### 2026-02-25 (Vocabulary Expansion - 30 New Entries, Session 324)
Added 30 new dictionary entries (IDs 13489-13518) from candidate_words.json:

- **Food noun (1)**: {焼売|しゅうまい} (shumai)
- **Na-adjectives (4)**: {猛烈|もうれつ} (fierce), {率直|そっちょく} (frank), {無造作|むぞうさ} (casual/careless), {無差別|むさべつ} (indiscriminate)
- **I-adjective (1)**: {狭苦|せまくる}しい (cramped)
- **特- cluster (4)**: {特権|とっけん} (privilege), {特例|とくれい} (special case), {特筆|とくひつ} (special mention), {特性|とくせい} (characteristic)
- **現- cluster (3)**: {現地|げんち} (local/on-site), {現行|げんこう} (current/in force), {現職|げんしょく} (incumbent)
- **王- cluster (2)**: {王道|おうどう} (classic approach/royal road), {王朝|おうちょう} (dynasty)
- **Noun/suru verbs (6)**: {独占|どくせん} (monopoly), {猶予|ゆうよ} (postponement), {献金|けんきん} (donation), {牽引|けんいん} (towing/leading), {狩猟|しゅりょう} (hunting), {爆破|ばくは} (blasting)
- **Verb (1)**: {燃|も}え{上|あ}がる (to flare up, godan intransitive)
- **Other nouns (8)**: {狭間|はざま} (gap/between), {片腕|かたうで} (one arm/right-hand man), {灯火|ともしび} (lamplight), {減益|げんえき} (profit decline), {漉|こ}す (to strain), {熊手|くまで} (rake/lucky charm), {獅子舞|ししまい} (lion dance), {物体|ぶったい} (object)

Notable features:
- 特- cluster: 4 entries covering rights, exceptions, noteworthy mentions, and properties
- 現- cluster: 3 entries covering location, laws, and positions
- 王- cluster: 2 entries covering mainstream/classic and dynasty
- Multi-sense entries: {独占|どくせん} (2: monopoly + exclusive possession), {牽引|けんいん} (2: towing + leading), {片腕|かたうで} (2: one arm + right-hand man), {王道|おうどう} (2: classic + royal road), {燃|も}え{上|あ}がる (2: flare up + passion), {現職|げんしょく} (2: incumbent + current position), {熊手|くまで} (2: rake + lucky charm)
- Cultural: {獅子舞|ししまい} (lion dance traditions), {熊手|くまで} (Tori-no-Ichi festival), {王朝|おうちょう} (Heian court culture)
- Legal/business: {猶予|ゆうよ} (suspended sentence), {献金|けんきん} (political donations), {特権|とっけん} (diplomatic immunity), {減益|げんえき} (earnings reports)
- New kanji: 2,405 → 2,410 ({漉|ろく}, {烈|れつ}, {牽|けん}, {猟|りょう}, {猶|ゆう})

Total entries: 13,544 → 13,574 (approximate)
Remaining candidates: 6,225 → 6,195 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
