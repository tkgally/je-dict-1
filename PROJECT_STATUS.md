# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-10
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
| Total entries | ~16,182 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,383 (open) |
| Candidate words | ~3,594 |
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

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 408)
Added 30 new dictionary entries (IDs 16010-16039) from candidate_words.json:

- **Nouns (16)**: {極意|ごくい} (innermost secrets), {貨幣|かへい} (currency), {皆無|かいむ} (nothing at all), {忍|しの}び{足|あし} (stealthy steps), {葉桜|はざくら} (cherry tree in leaf), {積|つ}み{木|き} (building blocks), {異臭|いしゅう} (strange smell), {手鏡|てかがみ} (hand mirror), {地毛|じげ} (natural hair), {給湯室|きゅうとうしつ} (office kitchenette), {水割|みずわ}り (whisky and water), {通夜|つや} (wake/vigil), {補欠|ほけつ} (substitute), {鼻血|はなぢ} (nosebleed), {謝礼|しゃれい} (honorarium), {内祝|うちいわ}い (return gift)
- **Na-adjectives (2)**: {熾烈|しれつ} (fierce), {非情|ひじょう} (heartless)
- **Noun/na-adjective (3)**: {別格|べっかく} (exceptional), {弱気|よわき} (timid/bearish), {任意|にんい} (optional)
- **Noun/verb-suru (2)**: {鑑定|かんてい} (appraisal), {抱擁|ほうよう} (embrace)
- **Nouns (other) (3)**: {動機|どうき} (motive), {格式|かくしき} (formality/prestige), {好敵手|こうてきしゅ} (worthy rival)
- **Verb-godan (1)**: {勝|か}ち{取|と}る (to win through effort)
- **I-adjective (1)**: {口|くち}うるさい (nagging)
- **Adverb (1)**: {一斉|いっせい}に (all at once)
- **Noun (building/place) (1)**: {銭湯|せんとう} (public bathhouse)

Notable features:
- Multi-sense: {弱気|よわき} (2: timid + bearish), {任意|にんい} (2: optional + arbitrary)
- Cultural: {通夜|つや} (funeral wake), {銭湯|せんとう} (public bath), {内祝|うちいわ}い (gift customs), {葉桜|はざくら} (seasonal)
- Homophone notes: {非情|ひじょう} vs {非常|ひじょう}, {動機|どうき} vs {動悸|どうき}/{同期|どうき}
- New kanji: 2,525 → 2,526 ({熾|し})

Total entries: ~16,062 → ~16,092 (approximate)
Remaining candidates: ~3,713 → ~3,683 (30 removed)

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 407)
Added 30 new dictionary entries (IDs 15980-16009) from candidate_words.json:

- **Nouns (11)**: {愛読|あいどく} (devoted reading), {多読|たどく} (extensive reading), {精読|せいどく} (intensive reading), {喪失感|そうしつかん} (sense of loss), {満足感|まんぞくかん} (feeling of satisfaction), {照合|しょうごう} (verification), {媒介|ばいかい} (intermediary/vector), {発電所|はつでんしょ} (power plant), {各界|かっかい} (various fields), {虚脱感|きょだつかん} (emptiness/lethargy), {自己肯定感|じここうていかん} (self-esteem)
- **Na-adjectives (3)**: {粗末|そまつ}な (poor quality/humble), {貴重|きちょう}な (precious/valuable), {雑多|ざった}な (miscellaneous/jumbled)
- **Nouns (geographical/cultural) (4)**: {諸国|しょこく} (various countries), {手巻|てま}き{寿司|ずし} (hand-rolled sushi), {稲荷寿司|いなりずし} (inari sushi), ペンション (Western-style guesthouse)
- **Nouns (specialized) (4)**: {空車|くうしゃ} (vacant taxi), {蒸留酒|じょうりゅうしゅ} (distilled spirits), {庇|ひさし} (eaves/visor), {吸入|きゅうにゅう} (inhalation), {通信網|つうしんもう} (communication network)
- **Verb-suru (1)**: {相反|あいはん}する (to conflict with)
- **Conjunction (1)**: {乃至|ないし} (from...to, or even)
- **Expressions (4)**: {胸|むね}をなでおろす (to feel relieved), {一線|いっせん}を{画|かく}す (to draw a clear line), {一刻|いっこく}も{早|はや}く (ASAP), {良心|りょうしん}が{咎|とが}める (to feel guilty)

Notable features:
- Reading cluster: {愛読|あいどく}, {多読|たどく}, {精読|せいどく}
- Emotion cluster: {喪失感|そうしつかん}, {満足感|まんぞくかん}, {虚脱感|きょだつかん}, {自己肯定感|じここうていかん}
- Food: {手巻|てま}き{寿司|ずし}, {稲荷寿司|いなりずし}, {蒸留酒|じょうりゅうしゅ}
- Idiomatic expressions: {胸|むね}をなでおろす, {一線|いっせん}を{画|かく}す, {良心|りょうしん}が{咎|とが}める
- New kanji: 2,524 → 2,525 ({乃|ない})

Total entries: ~16,032 → ~16,062 (approximate)
Remaining candidates: ~3,743 → ~3,713 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
