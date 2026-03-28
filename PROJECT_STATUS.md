# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-27
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
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

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 532)
Added 30 new dictionary entries (IDs 20321-20350) from candidate_words.json. Diverse mix of practical vocabulary for intermediate learners.

- **Adjectives (7)**: ありきたり (commonplace), {凡庸|ぼんよう} (mediocre), {法外|ほうがい} (outrageous), {無鉄砲|むてっぽう} (reckless), {静粛|せいしゅく} (silent/solemn), {清廉|せいれん} (incorruptible), {底|そこ}なし (bottomless)
- **Verbs (5)**: {持|も}ち{寄|よ}る (to bring and share), {落胆|らくたん}する (to be discouraged), チンする (to microwave), {禿|は}げる (to go bald), {撫|な}で{回|まわ}す (to stroke all over)
- **Adverbs (2)**: さりげなく (casually), {一晩中|ひとばんじゅう} (all night long)
- **Nouns (16)**: {経験談|けいけんだん} (personal account), {耳鳴|みみな}り (tinnitus), {雨粒|あまつぶ} (raindrop), {過不足|かふそく} (excess or deficiency), {助|す}っ{人|と} (helper), {変態|へんたい} (pervert/metamorphosis), {若|わか}さ (youth), {細身|ほそみ} (slim build), {魔除|まよ}け (charm against evil), {台風一過|たいふういっか} (clear skies after typhoon), {水|みず}はけ (drainage), {船便|ふなびん} (sea mail), {所持品|しょじひん} (belongings), {万歩計|まんぽけい} (pedometer), {出場|しゅつじょう}する (to compete), {演奏|えんそう}する (to perform music)
- Added 1 new kanji to index: 禿
- Removed 30 candidates that now exist as entries

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 531)
Added 30 new dictionary entries (IDs 20291-20320) from candidate_words.json. Diverse vocabulary including verbs, adjectives, expressions, and nouns for intermediate learners.

- **Verbs (10)**: なりすます (to impersonate), {突|つ}き{刺|さ}さる (to pierce), ひったくる (to snatch), {吊|つ}り{下|さ}げる (to suspend), {兼用|けんよう}する (dual use), {使|つか}い{古|ふる}す (to wear out), {吸|す}い{上|あ}げる (to absorb), {巻|ま}き{上|あ}げる (to roll up/fleece), {含有|がんゆう}する (to contain), {内包|ないほう}する (to include/imply)
- **Adjectives (4)**: {忌|い}まわしい (abominable), {手|て}ぬるい (too lenient), {長細|ながぼそ}い (long and thin), {磯臭|いそくさ}い (smelling of the sea)
- **Expressions (8)**: {頼|たよ}りになる (reliable), {敷居|しきい}が{高|たか}い (intimidating), {忌憚|きたん}のない (frank), {手際|てぎわ}が{良|よ}い (efficient), {心|こころ}に{刺|さ}さる (to strike a chord), {頭|あたま}がいい (smart), {本気|ほんき}にする (to take seriously), {胸|むね}に{響|ひび}く (to resonate)
- **Nouns (3)**: すす (soot), かぼす (kabosu citrus), {干|ほ}しぶどう (raisins)
- **Other (5)**: {優秀|ゆうしゅう}な (excellent), {放|ほう}り{投|な}げる (to throw away), {日焼|ひや}けする (to sunburn/fade), だもん (because - casual), {運転|うんてん}する (to drive)
- Removed 30 candidates that now exist as entries

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 530)
Added 30 new dictionary entries (IDs 20261-20290) from candidate_words.json. Diverse vocabulary for intermediate learners covering daily life, culture, business, nature, and more.

- **Verbs (4)**: {呆|あき}れ{果|は}てる (to be utterly dumbfounded), {高鳴|たかな}る (to throb/beat fast), {食|た}べ{歩|ある}く (to eat one's way around), {取|と}り{立|た}てる (to collect forcibly/single out/promote)
- **Adjectives (3)**: {目新|めあたら}しい (novel), {型破|かたやぶ}り (unconventional), {小|こ}ぶり (smallish)
- **Nouns (23)**: {横並|よこなら}び (side by side/conformity), {無駄骨|むだぼね} (wasted effort), {密輸|みつゆ} (smuggling), {直営|ちょくえい} (direct management), {夜風|よかぜ} (night breeze), {質疑|しつぎ} (Q&A), {林業|りんぎょう} (forestry), {停泊|ていはく} (anchoring), {配達員|はいたついん} (delivery person), {最高級|さいこうきゅう} (highest grade), {母子|ぼし} (mother and child), {返礼品|へんれいひん} (return gift), {展覧|てんらん} (exhibition), {送|おく}り{状|じょう} (shipping label), {陣痛|じんつう} (labor pains), {火災保険|かさいほけん} (fire insurance), {登校日|とうこうび} (school attendance day), {眼球|がんきゅう} (eyeball), {贈答用|ぞうとうよう} (for gift-giving), {農道|のうどう} (farm road), {質問者|しつもんしゃ} (questioner), {天気図|てんきず} (weather map), {募集要項|ぼしゅうようこう} (application guidelines)
- Removed 8 stale candidates (duplicates of existing entries: 感動する, 密閉する, 考案する, 左右する, etc.)

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 529)
Added 30 new dictionary entries (IDs 20231-20260) from candidate_words.json. Mix of practical vocabulary for intermediate learners covering travel, daily life, food, business, and emotions.

- **Suru-verbs (5)**: {宿泊|しゅくはく}する (to stay overnight), {目撃|もくげき}する (to witness), {中座|ちゅうざ}する (to leave partway through), {見物|けんぶつ}する (to sightsee), {出火|しゅっか} (outbreak of fire)
- **Adjective (1)**: ずる{賢|がしこ}い (sly, cunning)
- **Adverb (1)**: {一向|いっこう} (not at all)
- **Nouns (23)**: {体調不良|たいちょうふりょう} (feeling unwell), {本降|ほんぶ}り (steady rain), {悪酔|わるよ}い (bad drunkenness), {破格|はかく} (exceptional/bargain), {美容室|びようしつ} (beauty salon), {余生|よせい} (remaining years), {水|みず}しぶき (splash), {先方|せんぽう} (other party), {応接室|おうせつしつ} (reception room), {防寒着|ぼうかんぎ} (winter clothing), ぜんざい (sweet red bean soup), {崖崩|がけくず}れ (landslide), {試運転|しうんてん} (test run), {専業主夫|せんぎょうしゅふ} (househusband), {画材|がざい} (art supplies), {看板商品|かんばんしょうひん} (signature product), {黒髪|くろかみ} (black hair), {小袋|こぶくろ} (small bag), {冬|ふゆ}ごもり (winter seclusion), むなしさ (emptiness), {優越|ゆうえつ} (superiority), {素肌|すはだ} (bare skin), {麻婆豆腐|まーぼーどうふ} (mapo tofu)
- Removed 1 stale candidate (連れ子 — already existed as entry with different reading)
- Removed 30 candidates that now exist as entries

### 2026-03-28 (Vocabulary Expansion - 30 New Entries, Session 528)
Added 30 new dictionary entries (IDs 20201-20230) from candidate_words.json. Mix of common suru-verbs, adjectives, and practical nouns for intermediate learners.

- **Suru-verbs (9)**: {努力|どりょく}する (to make effort), {連絡|れんらく}する (to contact), {案内|あんない}する (to guide), {反応|はんのう}する (to react), {刺激|しげき}する (to stimulate), {移転|いてん}する (to relocate), {点灯|てんとう}する (to turn on light), {奉仕|ほうし}する (to serve), {合致|がっち}する (to match)
- **Adjectives (4)**: {入念|にゅうねん} (thorough), {壊|こわ}れやすい (fragile), {物寂|ものさび}しい (lonely/desolate), {肥沃|ひよく} (fertile)
- **Nouns (15)**: {職員|しょくいん} (staff member), {緊張感|きんちょうかん} (sense of tension), {前列|ぜんれつ} (front row), {後列|こうれつ} (back row), {納屋|なや} (barn/shed), {親元|おやもと} (parents' home), {内幕|ないまく} (inside story), {火元|ひもと} (origin of fire), {家具付|かぐつ}き (furnished), {川辺|かわべ} (riverbank), {岸辺|きしべ} (shore), {役立|やくだ}たず (good-for-nothing), {片目|かため} (one eye), {離宮|りきゅう} (detached palace), {牙城|がじょう} (stronghold)
- **Verb (1)**: {看取|みと}る (to watch over a dying person)
- **Noun/Adjective (1)**: {耳障|みみざわ}り (grating to hear)
- Removed 30 candidates that now exist as entries

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
