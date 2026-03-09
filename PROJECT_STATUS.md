# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-09
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
| Total entries | ~16,122 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,323 (open) |
| Candidate words | ~3,653 |
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

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 406)
Added 30 new dictionary entries (IDs 15950-15979) from candidate_words.json:

- **Nouns (14)**: ジャスミン (jasmine), {盲人|もうじん} (blind person), {厳秘|げんぴ} (strict secrecy), {環境破壊|かんきょうはかい} (environmental destruction), {食欲不振|しょくよくふしん} (loss of appetite), {自習室|じしゅうしつ} (study room), {音声認識|おんせいにんしき} (voice recognition), {筆記用具|ひっきようぐ} (writing utensils), {海鳥|うみどり} (seabird), {窮乏|きゅうぼう} (destitution), {逆方向|ぎゃくほうこう} (opposite direction), {低速|ていそく} (low speed), {目詰|めづ}まり (clogging), {進行方向|しんこうほうこう} (direction of travel)
- **Noun/verb-suru (3)**: {群雄割拠|ぐんゆうかっきょ} (rivalry of warlords), {防戦|ぼうせん} (defensive fight), {歩留|ぶどま}り (yield rate)
- **Noun/na-adjective (2)**: {鉄面皮|てつめんぴ} (brazen), {読|よ}み{上|あ}げ (reading aloud / text-to-speech)
- **Four-character compounds (2)**: {群雄割拠|ぐんゆうかっきょ}, {文明開化|ぶんめいかいか} (Meiji Westernization)
- **Adverbs (3)**: {悠々|ゆうゆう}と (leisurely), {容赦|ようしゃ}なく (relentlessly), {全般的|ぜんぱんてき}に (overall)
- **Expressions (4)**: どういうわけか (for some reason), {勇気|ゆうき}を{振|ふ}り{絞|しぼ}る (to summon courage), {会話|かいわ}が{弾|はず}む (lively conversation), ピントを{合|あ}わせる (to focus a lens)
- **Other (2)**: ならば (if so - conjunction), {路上|ろじょう}ライブ (street performance)

Notable features:
- Technology: {音声認識|おんせいにんしき}, {低速|ていそく}, {目詰|めづ}まり, {読|よ}み{上|あ}げ
- Culture/history: {文明開化|ぶんめいかいか}, {群雄割拠|ぐんゆうかっきょ}, {路上|ろじょう}ライブ, {彫|ほ}り{師|し}
- Multi-sense entries: {彫|ほ}り{師|し} (2: tattoo artist + engraver), {読|よ}み{上|あ}げ (2: reading aloud + text-to-speech)

Total entries: ~16,002 → ~16,032 (approximate)
Remaining candidates: ~3,772 → ~3,743 (29 removed)

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 405)
Added 30 new dictionary entries (IDs 15920-15949) from candidate_words.json:

- **Nouns (14)**: {突風|とっぷう} (gust of wind), {雷雨|らいう} (thunderstorm), {目印|めじるし} (landmark), {専門店|せんもんてん} (specialty store), {札束|さつたば} (wad of bills), {王冠|おうかん} (crown), {日報|にっぽう} (daily report), {特産|とくさん} (local specialty), {本堂|ほんどう} (main hall), {分母|ぶんぼ} (denominator), {類義語|るいぎご} (synonym), {唾液|だえき} (saliva), {目星|めぼし} (lead/estimate), {卸値|おろしね} (wholesale price)
- **Noun/verb-suru (4)**: {面会|めんかい} (visit), {大笑|おおわら}い (big laugh), {躍動|やくどう} (lively motion), {受講|じゅこう} (taking a course)
- **Noun/na-adjective (3)**: {欲張|よくば}り (greedy), {無尽蔵|むじんぞう} (inexhaustible), {無欲|むよく} (selfless)
- **Noun (multi-sense) (2)**: {王冠|おうかん} (2: crown + bottle cap), {大当|おおあ}たり (2: jackpot + big hit)
- **Verb-godan (2)**: {強|つよ}がる (to act tough), {居座|いすわ}る (to stay put)
- **Verb-ichidan (1)**: わきまえる (to discern/know one's place)
- **Nouns (other) (4)**: {振|ふ}り{出|だ}し (starting point), {振替|ふりかえ} (transfer/substitution), {高潮|たかしお} (storm surge), {口封|くちふう}じ (silencing someone), {北方|ほっぽう} (the north)

Notable features:
- Weather cluster: {突風|とっぷう}, {雷雨|らいう}, {高潮|たかしお}
- Commerce/work: {専門店|せんもんてん}, {卸値|おろしね}, {日報|にっぽう}, {受講|じゅこう}
- Cultural: わきまえる (knowing one's place), {本堂|ほんどう} (temple hall), {特産|とくさん} (regional specialties)
- Language: {類義語|るいぎご} (synonym), {分母|ぶんぼ} (denominator)
- New kanji: 2,523 → 2,524 ({唾|だ})

Total entries: ~15,972 → ~16,002 (approximate)
Remaining candidates: ~3,802 → ~3,772 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
