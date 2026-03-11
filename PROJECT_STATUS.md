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
| Total entries | ~16,242 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,443 (open) |
| Candidate words | ~3,534 |
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

### 2026-03-10 (Vocabulary Expansion - 30 New Entries, Session 411)
Added 30 new dictionary entries (IDs 16101-16130) from candidate_words.json:

- **Nouns (12)**: {精進料理|しょうじんりょうり} (Buddhist vegetarian cuisine), {公衆電話|こうしゅうでんわ} (public telephone), {一時帰国|いちじきこく} (temporary return home), {休憩時間|きゅうけいじかん} (break time), {定期購読|ていきこうどく} (subscription), {清涼感|せいりょうかん} (refreshing feeling), {人道|じんどう} (humanitarianism), {零細|れいさい} (very small), {数式|すうしき} (equation), {寒流|かんりゅう} (cold current), {挙動|きょどう} (behavior), {箸箱|はしばこ} (chopstick case)
- **Nouns (compound) (2)**: {早期発見|そうきはっけん} (early detection), チンゲン{菜|さい} (bok choy)
- **Expressions (7)**: {間|ま}が{悪|わる}い (bad timing), {歯止|はど}めがかかる (to be brought under control), {返信不要|へんしんふよう} (no reply necessary), {目処|めど}が{立|た}つ (to take shape), お{世辞|せじ}{抜|ぬ}きで (without flattery), というか (or rather), {一挙一動|いっきょいちどう} (every single move)
- **Adverbs (4)**: {事前|じぜん}に (in advance), {直後|ちょくご}に (immediately after), {並行|へいこう}して (in parallel), {無臭|むしゅう} (odorless)
- **Nouns (other) (3)**: {見掛|みか}け{倒|だお}し (all show), {四方八方|しほうはっぽう} (in all directions), {乗|の}り{換|か}え (transfer)
- **Verb (1)**: {見|み}え{透|す}く (to be obvious)
- **Adjective (1)**: {手際|てぎわ}よい (efficient)

Notable features:
- Practical daily life: {公衆電話|こうしゅうでんわ}, {休憩時間|きゅうけいじかん}, {乗|の}り{換|か}え, {箸箱|はしばこ}, {定期購読|ていきこうどく}
- Communication: というか, {返信不要|へんしんふよう}, お{世辞|せじ}{抜|ぬ}きで
- Society/health: {人道|じんどう}, {早期発見|そうきはっけん}, {零細|れいさい}
- Multi-sense: {間|ま}が{悪|わる}い (2: bad timing + awkward), {乗|の}り{換|か}え (2: transfer + switching)

Total entries: ~16,152 → ~16,182 (approximate)
Remaining candidates: ~3,623 → ~3,594 (29 removed)

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 410)
Added 30 new dictionary entries (IDs 16071-16100) from candidate_words.json:

- **Nouns (22)**: デブ (fat person), {登場|とうじょう}{人物|じんぶつ} (character), {植民地|しょくみんち} (colony), {壁紙|かべがみ} (wallpaper), {帰路|きろ} (way home), {送別会|そうべつかい} (farewell party), {寒気|さむけ} (chill), {砂利|じゃり}{道|みち} (gravel road), {曇天|どんてん} (cloudy sky), {品詞|ひんし} (part of speech), {水鳥|みずとり} (waterfowl), {各所|かくしょ} (various places), {畜産|ちくさん} (livestock farming), {口座|こうざ}{番号|ばんごう} (account number), {脱力感|だつりょくかん} (exhaustion), {信頼|しんらい}{関係|かんけい} (trust relationship), {労働|ろうどう}{組合|くみあい} (labor union), {調理師|ちょうりし} (licensed cook)
- **Nouns/verb-suru (7)**: {解析|かいせき} (analysis), {飛散|ひさん} (scattering), {射撃|しゃげき} (shooting), {発案|はつあん} (proposal), {退会|たいかい} (withdrawal), {静養|せいよう} (recuperation), {感化|かんか} (influence), {加点|かてん} (adding points)
- **Na-adjective (1)**: {手狭|てぜま} (cramped)
- **I-adjective (1)**: {情|なさ}け{深|ぶか}い (compassionate)
- **Multi-sense (2)**: {壁紙|かべがみ} (2: wall + digital), {乳液|にゅうえき} (2: skincare + botanical), {解析|かいせき} (2: analysis + parsing)
- **Noun (other) (1)**: {交互|こうご} (alternation)

Notable features:
- Practical daily life: {壁紙|かべがみ}, {口座|こうざ}{番号|ばんごう}, {退会|たいかい}, {乳液|にゅうえき}, {送別会|そうべつかい}
- Health/body: {寒気|さむけ}, {脱力感|だつりょくかん}, {静養|せいよう}, {乳液|にゅうえき}
- Work/society: {労働|ろうどう}{組合|くみあい}, {信頼|しんらい}{関係|かんけい}, {発案|はつあん}, {調理師|ちょうりし}
- Academic: {品詞|ひんし}, {解析|かいせき}, {植民地|しょくみんち}

Total entries: ~16,122 → ~16,152 (approximate)
Remaining candidates: ~3,653 → ~3,623 (30 removed)

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 409)
Added 30 new dictionary entries (IDs 16040-16070) from candidate_words.json:

- **Na-adjectives (4)**: {不気味|ぶきみ} (eerie), {家庭的|かていてき} (homely), {情熱的|じょうねつてき} (passionate), {柔軟|じゅうなん} (flexible)
- **Nouns (15)**: {主体性|しゅたいせい} (initiative), {素足|すあし} (bare feet), そばかす (freckles), {深海|しんかい} (deep sea), {身寄|みよ}り (relative), {正装|せいそう} (formal dress), {客引|きゃくひ}き (tout), {校則|こうそく} (school rules), {良識|りょうしき} (good sense), {震源|しんげん} (epicenter), {公益|こうえき} (public interest), {常勤|じょうきん} (full-time work), {型落|かたお}ち (outdated model), {市町村|しちょうそん} (municipalities), {自意識|じいしき} (self-consciousness)
- **Nouns (multi-sense) (4)**: {幕開|まくあ}け (2: curtain rise + dawn of era), {往来|おうらい} (2: traffic + street), {着替|きが}え (2: changing + spare clothes), {物別|ものわか}れ (breakdown of talks)
- **I-adjectives (2)**: {泥臭|どろくさ}い (unrefined), きめ{細|こま}かい (fine-grained/detailed)
- **Verbs (3)**: {導入|どうにゅう}する (to introduce), {脈打|みゃくう}つ (to pulsate), {位置|いち}づける (to position)
- **Nouns (other) (1)**: {道|みち}なり (following the road), {新学期|しんがっき} (new school term)
- **Expression (1)**: {感銘|かんめい}を{受|う}ける (to be deeply impressed)

Notable features:
- Good variety: na-adjectives, i-adjectives, verbs, expressions, practical nouns
- Multi-sense: {幕開|まくあ}け, {往来|おうらい}, {着替|きが}え, {泥臭|どろくさ}い, {震源|しんげん}, {脈打|みゃくう}つ, きめ{細|こま}かい
- Practical daily life: {着替|きが}え, {素足|すあし}, {道|みち}なり, {新学期|しんがっき}, {型落|かたお}ち
- Social/cultural: {客引|きゃくひ}き, {校則|こうそく}, {正装|せいそう}, {自意識|じいしき}

Total entries: ~16,092 → ~16,122 (approximate)
Remaining candidates: ~3,683 → ~3,653 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
