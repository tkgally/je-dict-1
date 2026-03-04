# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-04
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
| Total entries | ~15,074 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~12,275 (open) |
| Candidate words | ~4,696 |
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

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 371)
Added 30 new dictionary entries (IDs 14899-14928) from candidate_words.json:

- **Adverbs (2)**: {概|がい}して (generally), {続々|ぞくぞく}と (one after another)
- **Nouns (11)**: {最善|さいぜん} (the very best), {栄誉|えいよ} (honor), {右腕|みぎうで} (right arm/right-hand man), {毛筆|もうひつ} (writing brush), {車載|しゃさい} (on-board/vehicle-mounted), {準備運動|じゅんびうんどう} (warm-up exercise), {徹夜明|てつやあ}け (morning after all-nighter), {道具箱|どうぐばこ} (toolbox), {精神面|せいしんめん} (mental aspect), {韻|いん} (rhyme), ひび (crack)
- **Noun/suru verbs (5)**: {一掃|いっそう} (clean sweep), {退任|たいにん} (leaving office), {着任|ちゃくにん} (taking up a post), {再演|さいえん} (revival performance), {和解|わかい}する (to reconcile)
- **I-adjective (1)**: {絶|た}え{間|ま}ない (ceaseless)
- **Na-adjective (1)**: {個性的|こせいてき} (unique/distinctive)
- **Expressions (2)**: {腹|はら}を{括|くく}る (to brace oneself), ごまをする (to butter up)
- **Noun (time) (1)**: {一昼夜|いっちゅうや} (a whole day and night)
- **Noun (food/drink) (2)**: {晩酌|ばんしゃく} (evening drink), おつまみ (drinking snacks)
- **Other nouns (3)**: {弾力|だんりょく} (elasticity), {晴|は}れ{舞台|ぶたい} (grand occasion), {適性|てきせい} (aptitude)
- **Verb (1)**: ねじ{伏|ふ}せる (to pin down/force into submission)
- **Noun (school) (1)**: {日直|にっちょく} (day duty)

Notable features:
- Multi-sense entries: {右腕|みぎうで} (2: arm + right-hand man), ひび (2: crack + rift), {和解|わかい}する (2: reconcile + legal settlement), ねじ{伏|ふ}せる (2: physical + figurative), {弾力|だんりょく} (2: elasticity + flexibility)
- Diverse POS: adverbs, adjectives, verbs, nouns, expressions
- Daily life: {準備運動|じゅんびうんどう}, {徹夜明|てつやあ}け, {日直|にっちょく}, {道具箱|どうぐばこ}, {晩酌|ばんしゃく}, おつまみ
- Business/formal: {退任|たいにん}, {着任|ちゃくにん}, {適性|てきせい}, {和解|わかい}する, {概|がい}して
- Idiomatic: ごまをする, {腹|はら}を{括|くく}る

Total entries: 14,954 → 14,984 (approximate)
Remaining candidates: 4,816 → 4,786 (30 removed)

### 2026-03-04 (Vocabulary Expansion - 30 New Entries, Session 370)
Added 30 new dictionary entries (IDs 14869-14898) from candidate_words.json:

- **Godan verbs (4)**: {相次|あいつ}ぐ (to follow in succession), {嘲笑|あざわら}う (to sneer at), {塞|ふさ}がる (to be blocked), {寝|ね}そべる (to sprawl)
- **Nouns (13)**: {凹凸|おうとつ} (unevenness), {元旦|がんたん} (New Year's Day), {単身|たんしん} (alone), {麺類|めんるい} (noodles), {出稼|でかせ}ぎ (migrant work), {煩悩|ぼんのう} (worldly desires), {駄目元|だめもと} (nothing to lose), {乳幼児|にゅうようじ} (infants and toddlers), {離乳食|りにゅうしょく} (baby food), {遺族|いぞく} (bereaved family), {運動神経|うんどうしんけい} (athletic ability), {傷跡|きずあと} (scar), {睡魔|すいま} (drowsiness)
- **Noun/suru verbs (4)**: {朗読|ろうどく} (reading aloud), {仲違|なかたが}い (falling out), {紛失|ふんしつ} (loss), {決裂|けつれつ} (breakdown)
- **Na-adjectives (4)**: {不覚|ふかく} (blunder), {端正|たんせい} (handsome), {致命的|ちめいてき} (fatal), {念入|ねんい}り (thorough)
- **Nouns (other) (5)**: {自責|じせき} (self-blame), {門限|もんげん} (curfew), {発端|ほったん} (origin), {売|う}れ{行|ゆ}き (sales performance), {伸|の}びしろ (room for growth)

Notable features:
- Multi-sense entries: {塞|ふさ}がる (2: blocked + occupied)
- Daily life: {麺類|めんるい}, {門限|もんげん}, {元旦|がんたん}, {離乳食|りにゅうしょく}, {乳幼児|にゅうようじ}, {運動神経|うんどうしんけい}
- Emotions/psychology: {煩悩|ぼんのう}, {自責|じせき}, {不覚|ふかく}, {睡魔|すいま}
- Business/news: {相次|あいつ}ぐ, {決裂|けつれつ}, {紛失|ふんしつ}, {致命的|ちめいてき}, {売|う}れ{行|ゆ}き, {発端|ほったん}
- Colloquial: {駄目元|だめもと}, {寝|ね}そべる, {伸|の}びしろ

Total entries: 14,924 → 14,954 (approximate)
Remaining candidates: 4,846 → 4,816 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
