# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-05
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
| Total entries | ~15,134 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,335 (open) |
| Candidate words | ~4,636 |
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

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 376)
Added 30 new dictionary entries (IDs 15049-15078) from candidate_words.json:

- **Nouns (14)**: {綴|つづ}り (spelling), {用件|ようけん} (business/matter), {鉢植|はちう}え (potted plant), {下地|したじ} (groundwork/base coat), {幹線|かんせん} (main line), {爆音|ばくおん} (roar/blast), {原色|げんしょく} (primary color), {来歴|らいれき} (history/provenance), {振替休日|ふりかえきゅうじつ} (substitute holiday), {救急|きゅうきゅう} (emergency), {首飾|くびかざ}り (necklace), {腕輪|うでわ} (bracelet), {倍率|ばいりつ} (magnification/competitive ratio), {個展|こてん} (solo exhibition)
- **Noun/verb-suru (7)**: {没入|ぼつにゅう} (immersion), {燃焼|ねんしょう} (combustion), {補修|ほしゅう} (repair), {近代化|きんだいか} (modernization), {読解|どっかい} (reading comprehension), {聴解|ちょうかい} (listening comprehension), {粘着|ねんちゃく} (adhesion)
- **Na-adjectives (3)**: {綿密|めんみつ} (meticulous), {不遜|ふそん} (arrogant), {具|ぐ}だくさん (full of ingredients)
- **No-adjective (1)**: {泥|どろ}だらけ (covered in mud)
- **Noun/verb-suru (art) (1)**: {彩色|さいしき} (coloring/painting)
- **Godan verbs (3)**: {立|た}ち{直|なお}る (to recover), {響|ひび}き{渡|わた}る (to echo), {摘|つ}み{取|と}る (to pluck)
- **Ichidan verb (1)**: {追|お}い{上|あ}げる (to gain on)

Notable features:
- Multi-sense entries: {綴|つづ}り (2: spelling + bound pages), {燃焼|ねんしょう} (2: combustion + energy burning), {下地|したじ} (2: groundwork + base coat), {原色|げんしょく} (2: primary color + vivid color), {粘着|ねんちゃく} (2: adhesion + obsessive clinging), {倍率|ばいりつ} (2: magnification + competitive ratio), {摘|つ}み{取|と}る (2: pluck + nip in the bud)
- Education pair: {読解|どっかい}/{聴解|ちょうかい} (reading/listening comprehension)
- Accessories: {首飾|くびかざ}り, {腕輪|うでわ}
- Daily life: {鉢植|はちう}え, {具|ぐ}だくさん, {泥|どろ}だらけ, {救急|きゅうきゅう}, {振替休日|ふりかえきゅうじつ}
- Compound verbs: {立|た}ち{直|なお}る, {響|ひび}き{渡|わた}る, {追|お}い{上|あ}げる, {摘|つ}み{取|と}る

Total entries: 15,104 → 15,134 (approximate)
Remaining candidates: 4,666 → 4,636 (30 removed)

### 2026-03-05 (Vocabulary Expansion - 30 New Entries, Session 375)
Added 30 new dictionary entries (IDs 15019-15048) from candidate_words.json:

- **Nouns (16)**: {雑学|ざつがく} (trivia), {目頭|めがしら} (inner corner of eye), {発作|ほっさ} (attack/fit), {堪忍袋|かんにんぶくろ} (patience), {反動|はんどう} (recoil/backlash), {上流|じょうりゅう} (upstream/upper class), {下流|かりゅう} (downstream/lower class), {段位|だんい} (dan rank), {裏方|うらかた} (behind-the-scenes), {口数|くちかず} (talkativeness), {帳消|ちょうけ}し (cancellation), {沿線|えんせん} (along a railway line), {容疑者|ようぎしゃ} (suspect), {裏声|うらごえ} (falsetto), {直射日光|ちょくしゃにっこう} (direct sunlight), まつ{毛|げ} (eyelash)
- **Noun/verb-suru (5)**: {激励|げきれい} (encouragement), {合法|ごうほう} (legal), {独|ひと}り{占|じ}め (monopolizing), {殺到|さっとう} (rush/flood), {噴射|ふんしゃ} (jet/spray)
- **Noun/na-adj (1)**: {無礼|ぶれい} (rude)
- **Godan verbs (3)**: {呻|うめ}く (to groan), {着飾|きかざ}る (to dress up), {断|た}ち{切|き}る (to sever)
- **Adverbs (2)**: {当分|とうぶん} (for the time being), {一挙|いっきょ}に (all at once)
- **Noun (linguistics) (2)**: {送|おく}り{仮名|がな} (okurigana), {号泣|ごうきゅう} (wailing)
- **Noun (water) (1)**: {給水|きゅうすい} (water supply)

Notable features:
- Multi-sense entries: {呻|うめ}く (2: pain + frustration), {発作|ほっさ} (2: medical + emotional), {上流|じょうりゅう} (2: river + social class), {下流|かりゅう} (2: river + social class), {反動|はんどう} (2: rebound + political), {断|た}ち{切|き}る (2: physical + figurative)
- Paired entries: {上流|じょうりゅう}/{下流|かりゅう} (upstream/downstream, upper/lower class)
- Body/emotion: {目頭|めがしら}, まつ{毛|げ}, {号泣|ごうきゅう}, {堪忍袋|かんにんぶくろ}
- Daily life: {裏方|うらかた}, {沿線|えんせん}, {直射日光|ちょくしゃにっこう}, {給水|きゅうすい}
- Legal/news: {容疑者|ようぎしゃ}, {合法|ごうほう}, {殺到|さっとう}
- Culture: {段位|だんい}, {送|おく}り{仮名|がな}
- New kanji: 2,499 → 2,500 ({呻|うめ}く)

Total entries: 15,074 → 15,104 (approximate)
Remaining candidates: 4,696 → 4,666 (30 removed)

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 374)
Added 30 new dictionary entries (IDs 14989-15018) from candidate_words.json:

- **Nouns (21)**: {淡雪|あわゆき} (light snow), {掃除当番|そうじとうばん} (cleaning duty), {調理器具|ちょうりきぐ} (cooking utensils), {湯切|ゆぎ}り (draining hot water), {賀正|がしょう} (New Year's greeting), {迎春|げいしゅん} (welcoming New Year), {糸|いと}こんにゃく (konjac noodles), {追跡番号|ついせきばんごう} (tracking number), {美品|びひん} (item in good condition), {放射線|ほうしゃせん} (radiation), {自分|じぶん}らしさ (individuality), {赤外線|せきがいせん} (infrared), {国庫|こっこ} (national treasury), {愛好家|あいこうか} (enthusiast), {凝|こ}り{性|しょう} (perfectionist streak), {一口大|ひとくちだい} (bite-sized), {梯子酒|はしござけ} (bar hopping), {無礼講|ぶれいこう} (dropping formalities), {特盛|とくも}り (extra-large serving), {並盛|なみも}り (regular serving), {山菜採|さんさいと}り (foraging)
- **Noun/verb-suru (2)**: {電子化|でんしか} (digitization), {職務質問|しょくむしつもん} (police questioning)
- **Adverb (1)**: {点々|てんてん}と (here and there)
- **Nouns (other) (3)**: {外線|がいせん} (outside phone line), {義手|ぎしゅ} (prosthetic hand), {商用車|しょうようしゃ} (commercial vehicle)
- **Ichidan verb (1)**: {組|く}み{伏|ふ}せる (to pin down)
- **Godan verb (1)**: {痛|いた}み{入|い}る (to be deeply grateful)
- **Loanword (1)**: ルーチン (routine)

Notable features:
- Diverse themes: food/cooking ({糸|いと}こんにゃく, {湯切|ゆぎ}り, {一口大|ひとくちだい}, {特盛|とくも}り, {並盛|なみも}り), seasonal ({淡雪|あわゆき}, {賀正|がしょう}, {迎春|げいしゅん}, {山菜採|さんさいと}り), daily life ({追跡番号|ついせきばんごう}, {美品|びひん}, {掃除当番|そうじとうばん})
- Science/tech: {放射線|ほうしゃせん}, {赤外線|せきがいせん}, {電子化|でんしか}
- Culture: {無礼講|ぶれいこう}, {梯子酒|はしござけ}, {掃除当番|そうじとうばん}
- Keigo: {痛|いた}み{入|い}る (humble formal expression)
- First entries in 15000 directory range

Total entries: 15,044 → 15,074 (approximate)
Remaining candidates: 4,726 → 4,696 (30 removed)

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 373)
Added 30 new dictionary entries (IDs 14959-14988) from candidate_words.json:

- **Nouns (15)**: {芸能人|げいのうじん} (celebrity), {雇|やと}い{主|ぬし} (employer), {日雇|ひやと}い (day labor), {学生証|がくせいしょう} (student ID), {授業料|じゅぎょうりょう} (tuition fee), {親睦会|しんぼくかい} (social gathering), {独身者|どくしんしゃ} (single person), {粒子|りゅうし} (particle), {適応力|てきおうりょく} (adaptability), {潜在能力|せんざいのうりょく} (latent ability), {税収|ぜいしゅう} (tax revenue), {不審物|ふしんぶつ} (suspicious object), {保存食|ほぞんしょく} (preserved food), {初耳|はつみみ} (news to me), {不祥事|ふしょうじ} (scandal)
- **Noun/na-adj (2)**: {不釣|ふつ}り{合|あ}い (mismatched), {未定|みてい} (undecided)
- **Noun/verb-suru (3)**: {拍手喝采|はくしゅかっさい} (applause and cheers), {舌打|したう}ち (clicking tongue), {表裏|ひょうり} (two sides)
- **Godan verbs (4)**: {追|お}い{抜|ぬ}く (to pass), {搾|しぼ}り{取|と}る (to squeeze out), {送|おく}り{返|かえ}す (to send back), {使|つか}い{勝手|がって} (ease of use)
- **Ichidan verb (1)**: {寄|よ}せ{集|あつ}める (to gather together)
- **Nouns (other) (5)**: {芸術家|げいじゅつか} (artist), {佳境|かきょう} (climax), {遠距離|えんきょり} (long distance), {前世|ぜんせ} (previous life), {来世|らいせ} (next life)

Notable features:
- Multi-sense entries: {追|お}い{抜|ぬ}く (2: overtake + surpass), {搾|しぼ}り{取|と}る (2: squeeze + exploit), {授業料|じゅぎょうりょう} (2: tuition + lesson learned), {日雇|ひやと}い (2: day labor + day laborer), {表裏|ひょうり} (3: front/back + duality + duplicity)
- Daily life: {学生証|がくせいしょう}, {初耳|はつみみ}, {使|つか}い{勝手|がって}, {保存食|ほぞんしょく}
- Work/society: {雇|やと}い{主|ぬし}, {日雇|ひやと}い, {親睦会|しんぼくかい}, {税収|ぜいしゅう}, {不祥事|ふしょうじ}
- Science/abstract: {粒子|りゅうし}, {適応力|てきおうりょく}, {潜在能力|せんざいのうりょく}
- Culture/religion: {前世|ぜんせ}, {来世|らいせ}
- New kanji: 2,498 → 2,499 ({佳|か})

Total entries: 15,014 → 15,044 (approximate)
Remaining candidates: 4,756 → 4,726 (30 removed)

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 372)
Added 30 new dictionary entries (IDs 14929-14958) from candidate_words.json:

- **Nouns (14)**: {雨宿|あまやど}り (taking shelter from rain), {群衆|ぐんしゅう} (crowd), {履物|はきもの} (footwear), {酒豪|しゅごう} (heavy drinker), {黒帯|くろおび} (black belt), {牡丹雪|ぼたんゆき} (large snowflakes), {宿場|しゅくば} (post town), {砂利|じゃり} (gravel), {目玉焼|めだまや}き (fried egg), {母校|ぼこう} (alma mater), しきたり (custom), {負債|ふさい} (debt), {公害|こうがい} (pollution), {奥義|おうぎ} (secret teachings)
- **Noun/suru verbs (7)**: {浄化|じょうか} (purification), {授乳|じゅにゅう} (breastfeeding), {執務|しつむ} (office work), {交代|こうたい} (replacement), {浸水|しんすい} (flooding), {順応|じゅんのう} (adaptation), {擁護|ようご} (advocacy)
- **Noun/suru verbs (political) (2)**: {出馬|しゅつば} (running for office), {伝授|でんじゅ} (passing down knowledge)
- **Na-adjectives (2)**: {高飛車|たかびしゃ} (high-handed), {明白|めいはく} (obvious)
- **Noun (no-adj) (2)**: {未婚|みこん} (unmarried), {月例|げつれい} (monthly)
- **Godan verb (1)**: {涙|なみだ}ぐむ (to be moved to tears)
- **Noun (cultural) (2)**: {横綱|よこづな} (sumo grand champion), {段落|だんらく} (paragraph)

Notable features:
- Multi-sense entries: {段落|だんらく} (2: paragraph + end of phase), {浄化|じょうか} (2: physical + figurative), {出馬|しゅつば} (2: candidacy + stepping in), {横綱|よこづな} (2: sumo rank + the very best)
- Daily life: {雨宿|あまやど}り, {履物|はきもの}, {目玉焼|めだまや}き, {授乳|じゅにゅう}, しきたり
- Culture/sports: {横綱|よこづな}, {黒帯|くろおび}, {宿場|しゅくば}, {奥義|おうぎ}, {砂利|じゃり}
- Business/formal: {執務|しつむ}, {負債|ふさい}, {月例|げつれい}, {明白|めいはく}, {擁護|ようご}
- Environment/weather: {牡丹雪|ぼたんゆき}, {公害|こうがい}, {浸水|しんすい}, {浄化|じょうか}
- Politics/social: {出馬|しゅつば}, {未婚|みこん}, {交代|こうたい}

Total entries: 14,984 → 15,014 (approximate)
Remaining candidates: 4,786 → 4,756 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
