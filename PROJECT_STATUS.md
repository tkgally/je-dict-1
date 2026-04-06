# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-04
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
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
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

### 2026-04-06 (Vocabulary Expansion - 28 New Entries, Session 30)
Added 28 new dictionary entries (IDs 22617-22644) from candidate_words.json. A mix of verbs, nouns, and expressions covering daily life, medicine, law, emotion, social interaction, academic writing, music, biology, and more.

- **Suru verbs (7)**: {満足|まんぞく}する (to be satisfied), {突進|とっしん}する (to rush forward), {宣誓|せんせい}する (to swear an oath), タイプする (to type), {目隠|めかく}しする (to blindfold), {手術|しゅじゅつ}する (to perform surgery), {急浮上|きゅうふじょう}する (sudden emergence)
- **Ichidan verbs (8)**: {書|か}き{加|くわ}える (to add in writing), {招|まね}き{入|い}れる (to invite in), {巻|ま}き{付|つ}ける (to wrap around), {辱|はずかし}める (to humiliate), {取|と}り{揃|そろ}える (to stock/arrange), {定義|ていぎ}づける (to define), {関連|かんれん}づける (to relate), {痩|や}せこける (to become gaunt), {降|ふ}り{始|はじ}める (to begin to fall)
- **Expressions (4)**: {火|ひ}をつける (to light a fire), {弱|よわ}みに{付|つ}け{込|こ}む (to exploit weakness), {勘定|かんじょう}が{狂|くる}う (to miscalculate)
- **Nouns (9)**: {切|き}り{抜|ぬ}き (clipping/clip), {葉緑素|ようりょくそ} (chlorophyll), {譜面台|ふめんだい} (music stand), {精神衛生|せいしんえいせい} (mental health), {既得権益|きとくけんえき} (vested interests), {若白髪|わかしらが} (premature gray hair), {酒気帯|しゅきお}び (under influence of alcohol), {内服薬|ないふくやく} (oral medication), {介護福祉士|かいごふくしし} (certified care worker)

### 2026-04-06 (Vocabulary Expansion - 30 New Entries, Session 29)
Added 30 new dictionary entries (IDs 22587-22616) from candidate_words.json. A diverse mix of nouns, verbs, adjectives, adverbs, expressions, and a pronoun covering daily life, food, nature, emotion, language, law, and more.

- **I-adjectives (3)**: じれったい (frustrating), {薄気味悪|うすきみわる}い (creepy), {惜|お}しみない (unstinting)
- **Verbs (2)**: {飲|の}み{過|す}ぎる (to drink too much), {死|し}にかける (to nearly die)
- **Adverbs (2)**: はるかに (by far), {早急|そうきゅう}に (urgently)
- **Expressions (2)**: {喝采|かっさい}を{送|おく}る (to applaud), {気位|きぐらい}が{高|たか}い (proud/haughty)
- **Pronoun (1)**: どれか (one of them)
- **Nouns (20)**: {網|あみ} (net), {目|め}の{前|まえ} (right before one's eyes), {全長|ぜんちょう} (overall length), {漁船|ぎょせん} (fishing boat), {南向|みなみむ}き (south-facing), {外国籍|がいこくせき} (foreign nationality), {懐中|かいちゅう} (pocket), {短|みじか}さ (shortness), {盛|も}り{放題|ほうだい} (all-you-can-serve), {中食|なかしょく} (ready-made meals), こちら{側|がわ} (this side), {貯水|ちょすい} (water storage), {茹|ゆ}で{汁|じる} (cooking liquid), オノマトペ (onomatopoeia), {仮釈放|かりしゃくほう} (parole), {宿木|やどりぎ} (mistletoe), {条理|じょうり} (reason/logic), {最下|さいか} (lowest), {定量化|ていりょうか} (quantification), {水切|みずき}れ (drainage/stone skipping)

### 2026-04-06 (Vocabulary Expansion - 30 New Entries, Session 28)
Added 30 new dictionary entries (IDs 22557-22586) from candidate_words.json. Added new kanji 汐 to kanji index. A diverse mix of nouns, verbs, adjectives, and an adverb covering daily life, science, culture, emotions, and more.

- **Verbs (4)**: {押|お}し{留|とど}める (to restrain), {打|う}ち{壊|こわ}す (to smash), {習慣付|しゅうかんづ}ける (to habituate), {全力疾走|ぜんりょくしっそう}する (full-speed sprint)
- **Na-adjective (2)**: {苦労知|くろうし}らず (carefree/sheltered), {感情豊|かんじょうゆた}か (emotionally rich)
- **Adverb (1)**: {手厚|てあつ}く (generously/warmly)
- **Nouns (23)**: {触感|しょっかん} (tactile sensation), {建|た}て{直|なお}し (rebuilding), {昔風|むかしふう} (old-fashioned), {複合施設|ふくごうしせつ} (mixed-use complex), {氷枕|こおりまくら} (ice pillow), {地域性|ちいきせい} (regional characteristics), {含有量|がんゆうりょう} (content amount), {職務内容|しょくむないよう} (job duties), {年額|ねんがく} (annual fee), {異同|いどう} (differences), {通知設定|つうちせってい} (notification settings), {活動時間|かつどうじかん} (active hours), {不義|ふぎ} (immorality/infidelity), {興奮気味|こうふんぎみ} (somewhat excited), {心得違|こころえちが}い (misunderstanding), {潮汐|ちょうせき} (tide), {自然|しぜん}さ (naturalness), {連載中|れんさいちゅう} (currently serialized), {完読|かんどく} (reading through), {札入|さつい}れ (billfold), {絵付|えつ}け (ceramic painting), {持|も}ち{手|て} (handle/holder), {五分|ごぶ} (fifty-fifty)

### 2026-04-06 (Vocabulary Expansion - 30 New Entries, Session 27)
Added 30 new dictionary entries (IDs 22527-22556) from candidate_words.json. Removed 22 stale suru-verb candidates that already existed as noun entries. Added new kanji 帆 to kanji index. A diverse mix of nouns, expressions, a na-adjective, and suru verbs covering cooking, household, culture, language, society, nature, and more.

- **Nouns (21)**: {大|おお}さじ (tablespoon), {流|なが}し{台|だい} (kitchen sink), {土曜|どよう} (Saturday), {帆船|はんせん} (sailing ship), {繁忙|はんぼう} (busyness), {水浴|みずあ}び (bathing in water), {互恵|ごけい} (mutual benefit), {忠犬|ちゅうけん} (faithful dog), {門前町|もんぜんまち} (temple town), {擬音語|ぎおんご} (onomatopoeia), {報恩|ほうおん} (repaying kindness), {貝類|かいるい} (shellfish), {処世|しょせい} (worldly wisdom), {灯火|とうか} (lamplight), {弔意|ちょうい} (condolence), {浮腫|ふしゅ} (edema), {希代|きだい} (unprecedented), {鋭眼|えいがん} (keen eye), {取次|とりつぎ} (intermediary), {裏向|うらむ}き (face down), {甘|あま}やかし (spoiling)
- **Na-adjective (1)**: {尊大|そんだい} (haughty)
- **Nouns with verb-suru (4)**: {誘引|ゆういん} (inducement), {急襲|きゅうしゅう} (raid), {首謀|しゅぼう} (masterminding), スケッチ (sketch)
- **Expressions (2)**: {喉|のど}が{渇|かわ}く (to be thirsty), {油|あぶら}を{切|き}る (to drain oil)
- **Other (2)**: {愛人|あいじん} (lover), {先進|せんしん} (advanced)

### 2026-04-06 (Vocabulary Expansion - 23 New Entries, Session 26)
Added 23 new dictionary entries (IDs 22504-22526) from candidate_words.json. Focused on verbs (godan, ichidan, suru) and two nouns. Words cover a range of registers from formal/news vocabulary to everyday descriptive verbs.

- **Suru verbs (10)**: {値上|ねあ}げする (to raise prices), {飼育|しいく}する (to breed animals), {離陸|りりく}する (to take off), {破壊|はかい}する (to destroy), {懸念|けねん}する (to be concerned), {鎮火|ちんか}する (to extinguish fire), {伝播|でんぱ}する (to propagate), {否認|ひにん}する (to deny), {夢想|むそう}する (to fantasize), {憂慮|ゆうりょ}する (to be gravely concerned)
- **Ichidan verbs (5)**: {取|と}り{分|わ}ける (to serve out), {待|ま}ち{伏|ふ}せる (to ambush), {振|ふ}り{付|つ}ける (to choreograph), {古|ふる}ぼける (to look old/worn), しゃがれる (to become hoarse)
- **Godan verbs (6)**: {噴|ふ}き{上|あ}がる (to spout up), {生|お}い{茂|しげ}る (to grow thickly), {推|お}し{量|はか}る (to infer), {角張|かくば}る (to be angular), {食|く}いちぎる (to bite off), やせ{細|ほそ}る (to waste away)
- **Nouns (2)**: {旨|うま}さ (deliciousness/skill), {素直|すなお}さ (honesty/straightforwardness)








