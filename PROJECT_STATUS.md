# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-06
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
| Total entries | ~15,434 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,635 (open) |
| Candidate words | ~4,337 |
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

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 386)
Added 30 new dictionary entries (IDs 15349-15378) from candidate_words.json:

- **Noun/verb-suru (9)**: {判別|はんべつ} (distinction), {算出|さんしゅつ} (calculation), {服従|ふくじゅう} (obedience), {創立|そうりつ} (founding), {順延|じゅんえん} (postponement), {自死|じし} (suicide/euphemistic), {苦闘|くとう} (bitter struggle), {自害|じがい} (suicide/historical), {夕涼|ゆうすず}み (enjoying evening cool)
- **Nouns (13)**: {及第点|きゅうだいてん} (passing grade), {図案|ずあん} (design/pattern), {短歌|たんか} (tanka poetry), {白和|しらあ}え (tofu-dressed vegetables), {共著|きょうちょ} (co-authorship), {礼状|れいじょう} (thank-you letter), {家紋|かもん} (family crest), {工芸品|こうげいひん} (handicraft), {甲冑|かっちゅう} (armor), {錦絵|にしきえ} (color woodblock print), {画題|がだい} (painting subject), {遊郭|ゆうかく} (pleasure quarter), {蒸気機関車|じょうききかんしゃ} (steam locomotive)
- **Na-adjective (1)**: {明快|めいかい} (clear/lucid)
- **Noun/adjective-na (1)**: {無気力|むきりょく} (apathy/lethargy)
- **Person nouns (2)**: {道化師|どうけし} (clown), {老婆|ろうば} (old woman), {花魁|おいらん} (oiran)
- **Verbs (2)**: {究|きわ}める (to master/investigate), {仕|し}でかす (to make a blunder)
- **Intransitive verb (1)**: {野垂|のた}れ{死|じ}ぬ (to die in the gutter)

Notable features:
- Cultural: {家紋|かもん}, {錦絵|にしきえ}, {短歌|たんか}, {遊郭|ゆうかく}, {花魁|おいらん}, {甲冑|かっちゅう}, {夕涼|ゆうすず}み
- Academic/formal: {算出|さんしゅつ}, {創立|そうりつ}, {共著|きょうちょ}, {判別|はんべつ}, {明快|めいかい}
- Daily life: {礼状|れいじょう}, {白和|しらあ}え, {蒸気機関車|じょうききかんしゃ}, {工芸品|こうげいひん}
- New kanji: 2,507 → 2,510 ({冑|かぶと}, {婆|ばば}, {魁|さきがけ})

Total entries: 15,404 → 15,434 (approximate)
Remaining candidates: 4,367 → 4,337 (30 removed)

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 385)
Added 30 new dictionary entries (IDs 15319-15348) from candidate_words.json:

- **Nouns (15)**: {灰燼|かいじん} (ashes/destruction), {腰掛|こしか}け (seat/stepping stone), {不始末|ふしまつ} (mismanagement), {雨天|うてん} (rainy weather), {炭酸水|たんさんすい} (sparkling water), {消火器|しょうかき} (fire extinguisher), {果汁|かじゅう} (fruit juice), {水色|みずいろ} (light blue), {葬儀|そうぎ} (funeral), {歳末|さいまつ} (year-end), {張|は}り{紙|がみ} (posted notice), {弱|よわ}み (weakness), {菊|きく} (chrysanthemum), {貴重品|きちょうひん} (valuables), {貯金箱|ちょきんばこ} (piggy bank)
- **Noun/verb-suru (5)**: {健闘|けんとう} (good fight), {一目惚|ひとめぼ}れ (love at first sight), {夜遊|よあそ}び (nightlife), {命拾|いのちびろ}い (narrow escape), {対戦|たいせん} (match/competition)
- **Expressions (2)**: {弱音|よわね}を{吐|は}く (to whine), {見栄|みえ}を{張|は}る (to show off)
- **Na-adjective (1)**: {多種多様|たしゅたよう} (diverse)
- **Adverb (1)**: {期待通|きたいどお}り (as expected)
- **Pre-noun adjectival (1)**: {謎|なぞ}めいた (enigmatic)
- **Verb (1)**: {群|むら}がる (to swarm)
- **Other nouns (4)**: {空|あ}き{巣|す} (burglary), {普段着|ふだんぎ} (casual clothes), {丸太|まるた} (log), {波止場|はとば} (wharf)

Notable features:
- Multi-sense entries: {腰掛|こしか}け (2: bench + temporary job)
- Homophone cross-refs: {健闘|けんとう}/{検討|けんとう}/{見当|けんとう}, {消火器|しょうかき}/{消化器|しょうかき}, {対戦|たいせん}/{大戦|たいせん}
- Daily life: {炭酸水|たんさんすい}, {消火器|しょうかき}, {貴重品|きちょうひん}, {普段着|ふだんぎ}, {貯金箱|ちょきんばこ}, {張|は}り{紙|がみ}
- Culture: {菊|きく}, {葬儀|そうぎ}, {歳末|さいまつ}, {波止場|はとば}
- New kanji: 2,505 → 2,507 ({燼|じん}, {菊|きく})

Total entries: 15,374 → 15,404 (approximate)
Remaining candidates: 4,397 → 4,367 (30 removed)

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 384)
Added 30 new dictionary entries (IDs 15289-15318) from candidate_words.json:

- **Nouns (14)**: {王室|おうしつ} (royal family), {君主|くんしゅ} (monarch), {雨具|あまぐ} (rain gear), メンチカツ (minced meat cutlet), {監視|かんし}カメラ (surveillance camera), {男子校|だんしこう} (boys' school), {手編|てあ}み (hand-knit), {学籍番号|がくせきばんごう} (student ID number), お{墓参|はかまい}り (visiting a grave), お{供|そな}え{物|もの} (offering), {敬老|けいろう}の{日|ひ} (Respect for the Aged Day), {義兄弟|ぎきょうだい} (brothers-in-law), {但|ただ}し{書|が}き (proviso), {二流|にりゅう} (second-rate)
- **Noun/verb-suru (5)**: {同伴|どうはん} (accompanying), {履行|りこう} (fulfillment), {体調管理|たいちょうかんり} (health management), {環境保護|かんきょうほご} (environmental protection), {化膿|かのう} (suppuration)
- **Compound nouns (3)**: {森林破壊|しんりんはかい} (deforestation), {新社会人|しんしゃかいじん} (new workforce member), {不徳|ふとく} (lack of virtue)
- **Adverbs (3)**: {即座|そくざ}に (immediately), {予定通|よていどお}り (as scheduled), {終始|しゅうし} (throughout)
- **Na-adjectives (2)**: {真|まっ}っ{当|とう} (proper/honest), {色鮮|いろあざ}やか (colorful)
- **Expressions (2)**: {核心|かくしん}を{突|つ}く (to hit the nail on the head), {目|め}を{伏|ふ}せる (to look down)
- **Other (1)**: {爆睡|ばくすい} (sleeping deeply — colloquial)

Notable features:
- Multi-sense entries: {義兄弟|ぎきょうだい} (2: in-law/step + sworn), {但|ただ}し{書|が}き (2: legal proviso + receipt itemization)
- Culture: お{墓参|はかまい}り, {敬老|けいろう}の{日|ひ}, お{供|そな}え{物|もの}, {新社会人|しんしゃかいじん}
- Environment: {環境保護|かんきょうほご}, {森林破壊|しんりんはかい}
- Daily life: {体調管理|たいちょうかんり}, {雨具|あまぐ}, メンチカツ, {爆睡|ばくすい}
- Formal/business: {履行|りこう}, {但|ただ}し{書|が}き, {同伴|どうはん}, {不徳|ふとく}
- New kanji: 2,504 → 2,505 ({膿|のう})

Total entries: 15,344 → 15,374 (approximate)
Remaining candidates: 4,427 → 4,397 (30 removed)

### 2026-03-06 (Vocabulary Expansion - 30 New Entries, Session 383)
Added 30 new dictionary entries (IDs 15259-15288) from candidate_words.json:

- **Nouns (12)**: {強風|きょうふう} (strong wind), {空|あ}き{地|ち} (vacant lot), {農作物|のうさくぶつ} (crops), {株主|かぶぬし} (shareholder), {飲料水|いんりょうすい} (drinking water), {卒業生|そつぎょうせい} (graduate), {運転免許|うんてんめんきょ} (driver's license), {窃盗|せっとう} (theft), {飼|か}い{主|ぬし} (pet owner), {隔週|かくしゅう} (every other week), {門出|かどで} (departure/new start), {厚着|あつぎ} (dressing warmly)
- **Noun/verb-suru (9)**: {乱用|らんよう} (abuse/misuse), {的中|てきちゅう} (hitting the mark), {整列|せいれつ} (lining up), {服用|ふくよう} (taking medicine), {埋葬|まいそう} (burial), {抜粋|ばっすい} (excerpt), {重複|じゅうふく} (duplication), {布教|ふきょう} (proselytizing), {負傷|ふしょう} (injury), {決壊|けっかい} (breach/collapse)
- **Verbs (3)**: {緩|ゆる}める (to loosen), {引|ひ}き{締|し}める (to tighten), {似通|にかよ}う (to resemble closely)
- **Na-adjectives (2)**: {寛大|かんだい} (generous/tolerant), {速|すみ}やか (speedy/prompt)
- **Adverb (1)**: {絶|た}えず (constantly)
- **Expression (1)**: {一部始終|いちぶしじゅう} (the whole story)

Notable features:
- Multi-sense entries: {的中|てきちゅう} (2: hitting target + prediction coming true), {緩|ゆる}める (2: physical loosening + relaxing rules), {引|ひ}き{締|し}める (2: toning body + bracing discipline), {門出|かどで} (2: departure + new start), {布教|ふきょう} (2: religious + informal evangelizing)
- Antonym pair: {緩|ゆる}める ↔ {引|ひ}き{締|し}める
- Daily life: {厚着|あつぎ}, {飼|か}い{主|ぬし}, {運転免許|うんてんめんきょ}, {飲料水|いんりょうすい}, {隔週|かくしゅう}
- Formal/news: {窃盗|せっとう}, {負傷|ふしょう}, {決壊|けっかい}, {乱用|らんよう}, {整列|せいれつ}
- New kanji: 2,503 → 2,504 ({窃|せつ})

Total entries: 15,314 → 15,344 (approximate)
Remaining candidates: 4,457 → 4,427 (30 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 382)
Added 30 new dictionary entries (IDs 15229-15258) from candidate_words.json:

- **Expressions (1)**: {口|くち}を{挟|はさ}む (to butt in)
- **Nouns (12)**: {美食家|びしょくか} (gourmet), {墓地|ぼち} (cemetery), {肉屋|にくや} (butcher shop), お{惣菜|そうざい} (deli food), {難癖|なんくせ} (fault-finding), {幕切|まくぎ}れ (finale), {構成員|こうせいいん} (member), {筆順|ひつじゅん} (stroke order), {県民性|けんみんせい} (regional character), {自然界|しぜんかい} (natural world), たらこ (cod roe), {規則性|きそくせい} (regularity)
- **Noun/verb-suru (7)**: {転居|てんきょ} (moving), {弛緩|しかん} (relaxation), {激減|げきげん} (sharp decrease), {優先|ゆうせん} (priority), {後続|こうぞく} (following), {総計|そうけい} (sum total), {助力|じょりょく} (assistance)
- **Noun/verb-suru (more) (2)**: {戒告|かいこく} (admonition), {丸|まる}{呑|の}み (swallowing whole)
- **Adjective-i (1)**: {煙|けむ}たい (smoky; hard to be around)
- **Na-adjective (2)**: {難解|なんかい} (abstruse), {平穏無事|へいおんぶじ} (peaceful and uneventful)
- **Adjective-no/noun (3)**: {炊|た}き{立|た}て (freshly cooked), {不滅|ふめつ} (immortal), {極小|ごくしょう} (minuscule)
- **Adjective-no/noun (more) (1)**: {恒久|こうきゅう} (permanent)
- **Noun (other) (1)**: {不一致|ふいっち} (discrepancy)

Notable features:
- Multi-sense entries: {肉屋|にくや} (2: shop + person), {煙|けむ}たい (2: smoky + socially uncomfortable), {幕切|まくぎ}れ (2: theater + figurative), {丸|まる}{呑|の}み (2: literal + figurative)
- Food: お{惣菜|そうざい}, {炊|た}き{立|た}て, たらこ, {美食家|びしょくか}, {肉屋|にくや}
- Formal/written: {転居|てんきょ}, {戒告|かいこく}, {構成員|こうせいいん}, {総計|そうけい}, {助力|じょりょく}
- Culture: {県民性|けんみんせい}, {筆順|ひつじゅん}
- New kanji: 2,502 → 2,503 ({弛|し})

Total entries: 15,284 → 15,314 (approximate)
Remaining candidates: 4,487 → 4,457 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
