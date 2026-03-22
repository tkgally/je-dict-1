# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-22
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
| Total entries | ~18,498 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,699 (open) |
| Candidate words | ~5,666 |
| Cross-references | ~3,400 |
| Example sentences | ~53,000 |
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

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 479)
Added 35 new dictionary entries (IDs 18654-18688) from candidate_words.json.

- **Nouns (19)**: お{酢|す} (vinegar), インコ (parakeet), {査証|さしょう} (visa), {中高生|ちゅうこうせい} (jr/sr high school students), {体脂肪|たいしぼう} (body fat), {利回|りまわ}り (yield), {聖堂|せいどう} (cathedral), {経験者|けいけんしゃ} (experienced person), {賭|か}け{事|ごと} (gambling), {埴輪|はにわ} (haniwa clay figure), {夏野菜|なつやさい} (summer vegetables), {煮浸|にびた}し (simmered dish), {混血|こんけつ} (mixed heritage), {白金|はっきん} (platinum), {水深|すいしん} (water depth), {坑道|こうどう} (mine tunnel), {胴元|どうもと} (bookmaker), {日勤|にっきん} (day shift), {拡大鏡|かくだいきょう} (magnifying glass)
- **Nouns/Suru verbs (4)**: {希釈|きしゃく} (dilution), {差別化|さべつか} (differentiation), {続伸|ぞくしん} (continued rise), {共和|きょうわ} (republic)
- **Na-adjectives/Nouns (4)**: {安楽|あんらく} (comfortable), {利発|りはつ} (clever), {姑息|こそく} (stopgap/cowardly), {耽美|たんび} (aestheticism)
- **Adjective-no/Noun (1)**: {多機能|たきのう} (multi-function)
- **Nouns (business pair) (2)**: {上期|かみき} (first half of fiscal year), {下期|しもき} (second half of fiscal year)
- **Noun (2 senses) (3)**: {外装|がいそう} (exterior/packaging), {原画|げんが} (original art/key animation), {煙管|きせる} (kiseru pipe/fare evasion)
- **Noun (2 senses) (2)**: {舎弟|しゃてい} (younger brother/underling), {姑息|こそく} (stopgap/cowardly)

Notable features:
- Multi-sense entries: {外装|がいそう} (2), {原画|げんが} (2), {煙管|きせる} (2), {姑息|こそく} (2), {舎弟|しゃてい} (2)
- Business/Finance: {利回|りまわ}り, {上期|かみき}, {下期|しもき}, {差別化|さべつか}, {続伸|ぞくしん}
- Food/Cooking: お{酢|す}, {夏野菜|なつやさい}, {煮浸|にびた}し
- Culture/History: {埴輪|はにわ}, {煙管|きせる}, {睦月|むつき}, {耽美|たんび}
- New kanji added: 埴 (ID 02583), 耽 (ID 02584)

Total entries: ~18,463 → ~18,498 (approximate)
Remaining candidates: ~5,701 → ~5,666 (35 removed as entries)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 478)
Added 35 new dictionary entries (IDs 18619-18653) from candidate_words.json.

- **Nouns (22)**: {洋楽|ようがく} (Western music), {新製品|しんせいひん} (new product), {付属品|ふぞくひん} (accessories), {別売|べつう}り (sold separately), {買|か}い{値|ね} (purchase price), {理事会|りじかい} (board of directors), {生命|せいめい}{保険|ほけん} (life insurance), {産業|さんぎょう}{革命|かくめい} (Industrial Revolution), {百貨店|ひゃっかてん} (department store), {裏門|うらもん} (back gate), {小心者|しょうしんもの} (coward), {正真正銘|しょうしんしょうめい} (genuine), お{化|ば}け{屋敷|やしき} (haunted house), {受験生|じゅけんせい} (exam student), くちばし (beak), {人事|じんじ}{異動|いどう} (personnel reshuffle), {撮|と}り{直|なお}し (retake), {予断|よだん} (prejudgment), {患部|かんぶ} (affected area), {微塵|みじん} (tiny particle / not at all), {序列|じょれつ} (hierarchy), {再利用|さいりよう} (reuse)
- **Nouns/Suru verbs (7)**: {激変|げきへん} (drastic change), {分散|ぶんさん} (dispersion), {気疲|きづか}れ (mental fatigue), {介助|かいじょ} (caregiving), {切|き}り{盛|も}り (managing), {熱望|ねつぼう} (ardent desire), {除草|じょそう} (weeding)
- **Nouns/Na-adjectives (4)**: {無知|むち} (ignorance), {軽|かる}はずみ (rashness), {気弱|きよわ} (timid), {半透明|はんとうめい} (translucent)
- **Na-adjective (1)**: {体系的|たいけいてき} (systematic)
- **Noun (1)**: {単身|たんしん}{赴任|ふにん} (living away from family for work)

Notable features:
- Multi-sense entries: {分散|ぶんさん} (2 senses), {微塵|みじん} (2 senses)
- Cultural: {単身|たんしん}{赴任|ふにん}, {受験生|じゅけんせい}, {百貨店|ひゃっかてん}, お{化|ば}け{屋敷|やしき}
- Business/Finance: {生命|せいめい}{保険|ほけん}, {買|か}い{値|ね}, {理事会|りじかい}, {人事|じんじ}{異動|いどう}, {序列|じょれつ}
- Medical/Health: {患部|かんぶ}, {介助|かいじょ}
- Homophone cross-references added for: {無知|むち}/{無恥|むち}, {予断|よだん}/{余談|よだん}, {除草|じょそう}/{助走|じょそう}/{女装|じょそう}, {患部|かんぶ}/{幹部|かんぶ}

Total entries: ~18,428 → ~18,463 (approximate)
Remaining candidates: ~5,736 → ~5,701 (35 removed as entries)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 477)
Added 35 new dictionary entries (IDs 18584-18618) from candidate_words.json.

- **Expressions (13)**: に{違|ちが}いない (must be), {面目|めんぼく}ない (ashamed), {運|うん}が{良|い}い (lucky), {場|ば}を{盛|も}り{上|あ}げる (liven up), {喉|のど}を{鳴|な}らす (to purr), {本音|ほんね}を{吐|は}く (speak one's mind), {腰|こし}がある (chewy/firm), {変化|へんか}に{富|と}む (varied), {付|つ}き{合|あ}いがいい (sociable), {熱|ねつ}を{冷|さ}ます (cool down), {危険|きけん}を{孕|はら}む (fraught with danger), ページを{繰|く}る (leaf through pages), {発給|はっきゅう}する (to issue)
- **Verbs (9)**: {書|か}き{損|そん}じる (writing mistake), {曲|ま}がりくねる (twist and turn), {叩|たた}きのめす (thrash), {立|た}ち{回|まわ}る (maneuver), {走|はし}り{去|さ}る (run away), {動|うご}き{出|だ}す (start moving), {滑|すべ}り{出|だ}す (get underway), めくり{上|あ}げる (roll up), そぎ{落|お}とす (strip away), {教|おし}え{導|みちび}く (mentor)
- **Adjectives (5)**: {格好|かっこう}いい (cool), {小汚|こぎたな}い (scruffy), くすぐったい (ticklish), {疑|うたが}い{深|ぶか}い (distrustful), {理屈|りくつ}っぽい (argumentative)
- **Nouns (3)**: {斜|なな}め{向|む}かい (diagonally opposite), {目利|めき}き (connoisseur), {身|み}の{上|うえ} (one's circumstances)
- **Pronouns (2)**: {誰|だれ}も (nobody/everyone), どいつ (which one - rude)
- **Adverb (1)**: {静|しず}かに (quietly)
- **Noun/Suru verb (1)**: {更生|こうせい}する (rehabilitate)

Notable features:
- Multi-sense entries: くすぐったい (2), {立|た}ち{回|まわ}る (2), {滑|すべ}り{出|だ}す (2), {喉|のど}を{鳴|な}らす (2), {静|しず}かに (2), {誰|だれ}も (2), {熱|ねつ}を{冷|さ}ます (2)
- Grammar/Patterns: に{違|ちが}いない, {誰|だれ}も, {静|しず}かに
- Social/Cultural: {付|つ}き{合|あ}いがいい, {場|ば}を{盛|も}り{上|あ}げる, {本音|ほんね}を{吐|は}く, {腰|こし}がある
- Compound verbs: {曲|ま}がりくねる, {叩|たた}きのめす, {走|はし}り{去|さ}る, {動|うご}き{出|だ}す, {滑|すべ}り{出|だ}す
- Removed 4 stale candidates (duplicates: {挑戦|ちょうせん}, ～だらけ, ～だけでなく, ～がち)

Total entries: ~18,393 → ~18,428 (approximate)
Remaining candidates: ~5,773 → ~5,736 (33 removed as entries + 4 stale removed)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 476)
Added 35 new dictionary entries (IDs 18549-18583) from candidate_words.json.

- **Nouns (20)**: {宝|たから}くじ (lottery), {夕刊|ゆうかん} (evening newspaper), {表通|おもてどお}り (main street), {得点王|とくてんおう} (top scorer), {新人王|しんじんおう} (rookie of the year), {寄合|よりあい} (gathering), {故事成語|こじせいご} (historical idiom), {列国|れっこく} (the nations), {蚊柱|かばしら} (gnat swarm), {多人数|たにんずう} (large group), {東洋学|とうようがく} (East Asian studies), {糊口|ここう} (livelihood), {有閑|ゆうかん} (leisure), {聖霊|せいれい} (Holy Spirit), {誰々|だれだれ} (so-and-so), {二回|ふたまわ}り (two rounds/sizes), {分譲地|ぶんじょうち} (subdivided land), {広告塔|こうこくとう} (advertising tower/figurehead), {使|つか}い{走|ばし}り (errand boy), {代書|だいしょ} (scrivener's work)
- **Nouns/Suru verbs (7)**: {給油|きゅうゆ} (refueling), {訓読|くんどく} (kun reading), {反比例|はんぴれい} (inverse proportion), {注油|ちゅうゆ} (oiling), {類焼|るいしょう} (fire spread), {自決|じけつ} (self-determination), {代書|だいしょ} (writing for another)
- **Na-adjectives (3)**: {乱雑|らんざつ} (messy), {不景気|ふけいき} (recession/gloomy), {土|つち}まみれ (covered in dirt)
- **Adverbs (2)**: {多|おお}くとも (at most), {裏|うら}で (behind the scenes)
- **Other (3)**: {因|よ}って (therefore — conjunction), {如|ごと}き (like — suffix), {盤|ばん} (board — noun/suffix)

Notable features:
- Multi-sense entries: {不景気|ふけいき} (2 senses), {広告塔|こうこくとう} (2 senses), {自決|じけつ} (2 senses), {両性|りょうせい} (2 senses), {使|つか}い{走|ばし}り (2 senses), {二回|ふたまわ}り (2 senses), {盤|ばん} (2 senses), {如|ごと}き (2 senses)
- Sports: {得点王|とくてんおう}, {新人王|しんじんおう}
- Academic/Literary: {訓読|くんどく}, {故事成語|こじせいご}, {東洋学|とうようがく}, {因|よ}って, {如|ごと}き, {糊口|ここう}
- Removed 1 stale candidate ({片寄|かたよ}る — variant of existing {偏|かたよ}る)

Total entries: ~18,358 → ~18,393 (approximate)
Remaining candidates: ~5,808 → ~5,773 (34 removed as entries + 1 stale removed)

### 2026-03-22 (Vocabulary Expansion - 40 New Entries, Session 475)
Added 40 new dictionary entries (IDs 18509-18548) from candidate_words.json.

- **Nouns (14)**: {密室|みっしつ} (locked room), {車検|しゃけん} (vehicle inspection), {担架|たんか} (stretcher), {本州|ほんしゅう} (Honshu), {照|て}れ{屋|や} (shy person), {月初|げっしょ} (beginning of month), {見張|みは}り (lookout), {静電気|せいでんき} (static electricity), {固定電話|こていでんわ} (landline), {長期戦|ちょうきせん} (long haul), {横線|よこせん} (horizontal line), {末娘|すえむすめ} (youngest daughter), {羊飼|ひつじか}い (shepherd), {滴|しずく} (droplet)
- **Nouns/Suru verbs (6)**: {折半|せっぱん} (splitting in half), {没収|ぼっしゅう} (confiscation), {目配|めくば}せ (eye signal), {知覚|ちかく} (perception), {欠場|けつじょう} (absence from contest), {補正|ほせい} (correction)
- **Na-adjectives/Nouns (5)**: {早急|さっきゅう} (urgent), {桁外|けたはず}れ (extraordinary), {朦朧|もうろう} (hazy/dazed), {混|ま}ぜこぜ (jumbled), {豊穣|ほうじょう} (bountiful)
- **Suru verbs (2)**: {感服|かんぷく}する (to be impressed), {覚醒|かくせい}する (to awaken)
- **Other verbs (1)**: {口|くち}ずさむ (to hum)
- **Nouns with two senses (3)**: {大黒柱|だいこくばしら} (central pillar / breadwinner), {密室|みっしつ} (locked room / behind closed doors), {埋没|まいぼつ} (burial / obscurity)
- **Adverb/Onomatopoeia (1)**: ぐつぐつ (simmering)
- **Expression (1)**: {遅|おそ}かれ{早|はや}かれ (sooner or later)
- **Four-character idiom (1)**: {一刀両断|いっとうりょうだん} (decisive action)
- **Noun (1)**: {施策|しさく} (policy/measure)
- **Noun (1)**: {若返|わかがえ}り (rejuvenation)
- **Noun/Suru verb (1)**: {充血|じゅうけつ} (bloodshot)
- **Noun/Suru verb (1)**: {競売|きょうばい} (auction)
- **Noun (1)**: {夢心地|ゆめごこち} (dreamlike state)
- **Noun (1)**: {嫌疑|けんぎ} (suspicion)
- **Noun/Suru verb (1)**: {一握|ひとにぎ}り (a handful)

Notable features:
- Daily life: {車検|しゃけん}, {固定電話|こていでんわ}, {静電気|せいでんき}, {月初|げっしょ}, ぐつぐつ
- Geography: {本州|ほんしゅう}
- Legal/Formal: {嫌疑|けんぎ}, {競売|きょうばい}, {没収|ぼっしゅう}, {施策|しさく}
- Four-character idiom: {一刀両断|いっとうりょうだん}
- Multi-sense entries: {大黒柱|だいこくばしら}, {密室|みっしつ}, {埋没|まいぼつ}, {朦朧|もうろう}, {覚醒|かくせい}する, {一握|ひとにぎ}り
- New kanji added: 朦 (ID 02580), 穣 (ID 02581), 醒 (ID 02582)

Total entries: ~18,318 → ~18,358 (approximate)
Remaining candidates: ~5,848 → ~5,808 (40 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
