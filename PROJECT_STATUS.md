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
| Total entries | ~18,428 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,629 (open) |
| Candidate words | ~5,736 |
| Cross-references | ~3,400 |
| Example sentences | ~52,600 |
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

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 474)
Added 35 new dictionary entries (IDs 18472-18508) from candidate_words.json.

- **Nouns (17)**: {抱負|ほうふ} (aspiration), {台車|だいしゃ} (hand cart), {健康保険|けんこうほけん} (health insurance), {営業時間|えいぎょうじかん} (business hours), お{猪口|ちょこ} (sake cup), {暖炉|だんろ} (fireplace), {財宝|ざいほう} (treasure), {予防策|よぼうさく} (preventive measure), {取|と}り{換|か}え (replacement), {飼|か}い{猫|ねこ} (pet cat), {商社|しょうしゃ} (trading company), {首都圏|しゅとけん} (Tokyo metro area), {潮干狩|しおひが}り (clamming), {出張所|しゅっちょうじょ} (branch office), {代理人|だいりにん} (agent/proxy), {中辛|ちゅうから} (medium-spicy), {水揚|みずあ}げ (fish landing/sales)
- **Nouns/Suru verbs (7)**: {着席|ちゃくせき} (taking a seat), {飲酒運転|いんしゅうんてん} (drunk driving), {命中|めいちゅう} (direct hit), {即決|そっけつ} (snap decision), {模造|もぞう} (imitation), {放流|ほうりゅう} (release/discharge), {二転三転|にてんさんてん} (changing repeatedly)
- **Na-adjectives (3)**: {悲痛|ひつう} (grief-stricken), {必然的|ひつぜんてき} (inevitable), {誇|ほこ}らしげ (proud-looking)
- **Verbs (2)**: まぶす (to coat), {群|む}れる (to flock)
- **Adjective (1)**: {得難|えがた}い (hard to come by)
- **Expression (1)**: {気|き}が{進|すす}まない (reluctant)
- **Noun/Adj (2)**: {最良|さいりょう} (the best), {失策|しっさく} (blunder/error)
- **Four-character idiom (2)**: {一攫千金|いっかくせんきん} (striking it rich), {他力本願|たりきほんがん} (relying on others)
- **Noun/Suru verb (1)**: {推奨|すいしょう} (recommendation)

Notable features:
- Daily life: {営業時間|えいぎょうじかん}, {健康保険|けんこうほけん}, {台車|だいしゃ}, {暖炉|だんろ}, {飼|か}い{猫|ねこ}, {中辛|ちゅうから}
- Culture: お{猪口|ちょこ}, {潮干狩|しおひが}り, {他力本願|たりきほんがん}
- Business: {商社|しょうしゃ}, {代理人|だいりにん}, {出張所|しゅっちょうじょ}
- Four-character idioms: {一攫千金|いっかくせんきん}, {他力本願|たりきほんがん}, {二転三転|にてんさんてん}
- Removed 2 duplicate candidates ({推奨|すいしょう}, {雑|ざつ} — already existed as entries)

Total entries: ~18,283 → ~18,318 (approximate)
Remaining candidates: ~5,883 → ~5,848 (35 removed)

### 2026-03-22 (Vocabulary Expansion - 35 New Entries, Session 473)
Added 35 new dictionary entries (IDs 18437-18471) from candidate_words.json.

- **Nouns (24)**: {文庫|ぶんこ} (paperback), {異世界|いせかい} (another world), {三|み}つ{編|あ}み (braid), {礼服|れいふく} (formal wear), {精神疾患|せいしんしっかん} (mental illness), {論評|ろんぴょう} (criticism), {役|やく}どころ (role), {引|ひ}き{立|た}て{役|やく} (foil), {長期保存|ちょうきほぞん} (long-term storage), {念珠|ねんじゅ} (prayer beads), {司令部|しれいぶ} (headquarters), {歳時記|さいじき} (saijiki), {万雷|ばんらい} (thunderous), {類人猿|るいじんえん} (great ape), {霊長類|れいちょうるい} (primates), {若造|わかぞう} (youngster), {水洗|すいせん}トイレ (flush toilet), {車夫|しゃふ} (rickshaw puller), {股下|またした} (inseam), {言|い}い{付|つ}け (order/tattling), {取|と}り{消|け}し{線|せん} (strikethrough), {鍵盤楽器|けんばんがっき} (keyboard instrument), {円座|えんざ} (round cushion), {英才教育|えいさいきょういく} (gifted education)
- **Nouns/Other (5)**: {未開|みかい} (undeveloped), {不実|ふじつ} (faithlessness), {目出|めだ}し{帽|ぼう} (balaclava), {喚声|かんせい} (shout), {頓服|とんぷく} (as-needed medicine)
- **Adverb (1)**: {判然|はんぜん} (clearly)
- **Pronoun (1)**: {貴様|きさま} (you, rude)
- **Interjection (1)**: ちくしょう (damn it)
- **Expression (1)**: {熱|ねつ}を{帯|お}びる (to get heated)
- **Traditional month name (1)**: {文月|ふづき} (July)
- **Suru verb (1)**: {妥結|だけつ} (settlement)

Notable features:
- Culture: {歳時記|さいじき}, {文月|ふづき}, {念珠|ねんじゅ}, {車夫|しゃふ}, {円座|えんざ}
- Modern culture: {異世界|いせかい}, {文庫|ぶんこ}
- Medical: {精神疾患|せいしんしっかん}, {頓服|とんぷく}
- Biology: {類人猿|るいじんえん}, {霊長類|れいちょうるい}
- Expressive vocabulary: ちくしょう, {貴様|きさま}, {若造|わかぞう}
- Removed 1 stale candidate ({蛞蝓|なめくじ} — kanji variant of existing なめくじ entry)

Total entries: ~18,248 → ~18,283 (approximate)
Remaining candidates: ~5,919 → ~5,883 (35 removed as entries + 1 stale removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
