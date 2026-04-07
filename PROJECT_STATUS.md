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

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 32)
Added 30 new dictionary entries (IDs 22670-22699) from candidate_words.json. A diverse mix of nouns, expressions, suru verbs, and a na-adjective covering personality, culture, law, business, perception, emotion, and more.

- **Expressions (8)**: {耳|みみ}を{澄|す}ます (to listen carefully), {気味|きみ}が{悪|わる}い (creepy), {暖簾|のれん}に{腕押|うでお}し (futile effort), {愛想|あいそ}が{悪|わる}い (unsociable), {無心|むしん}になる (to become absorbed), {手狭|てぜま}になる (to become cramped), ふと{思|おも}い{出|だ}す (to suddenly remember), {決定的瞬間|けっていてきしゅんかん} (decisive moment — as noun)
- **Suru verbs (2)**: {加入|かにゅう}する (to join), {深刻化|しんこくか}する (to become serious)
- **Na-adjective (1)**: {結果的|けっかてき} (resultant, eventual)
- **Nouns (19)**: {労力|ろうりょく} (labor/effort), {世間知|せけんし}らず (naive), {内密|ないみつ} (confidential), {秀作|しゅうさく} (excellent work), {家族|かぞく}{団|だん}らん (family togetherness), お{盆休|ぼんやす}み (Obon holiday), {半人前|はんにんまえ} (half-fledged), {青二才|あおにさい} (greenhorn), {日和見|ひよりみ} (opportunism), {児童文学|じどうぶんがく} (children's literature), {荷物検査|にもつけんさ} (baggage inspection), {国際協力|こくさいきょうりょく} (international cooperation), {営業利益|えいぎょうりえき} (operating profit), {旅日記|たびにっき} (travel diary), {精神的苦痛|せいしんてきくつう} (emotional distress), {有力候補|ゆうりょくこうほ} (leading candidate), {原子爆弾|げんしばくだん} (atomic bomb), {無期懲役|むきちょうえき} (life imprisonment), {寄稿者|きこうしゃ} (contributor)

### 2026-04-06 (Vocabulary Expansion - 25 New Entries, Session 31)
Added 25 new dictionary entries (IDs 22645-22669) from candidate_words.json. Removed 1 stale candidate (焦れったい, already existed as entry 22590). A diverse mix of nouns, suru verbs, and a na-adjective covering culture, music, medicine, literature, daily life, and more.

- **Nouns (16)**: {口笛|くちぶえ} (whistling), {警笛|けいてき} (warning whistle), {実用性|じつようせい} (practicality), {花札|はなふだ} (hanafuda cards), {本意|ほんい} (real intention), {社員証|しゃいんしょう} (employee ID), {暗黒街|あんこくがい} (underworld), {宿願|しゅくがん} (long-cherished wish), {便覧|べんらん} (handbook), {文壇|ぶんだん} (literary circles), {撮影所|さつえいじょ} (film studio), {縦笛|たてぶえ} (recorder), {旅行記|りょこうき} (travelogue), {紀行文|きこうぶん} (travel essay), {佳作|かさく} (honorable mention), あいこ (tie/draw)
- **Suru verbs (5)**: {流浪|るろう} (wandering), {接種|せっしゅ} (vaccination), {先導|せんどう} (leading), {敬畏|けいい} (awe/reverence), {企図|きと} (plan/scheme)
- **Na-adjective (1)**: {精細|せいさい} (detailed/fine)
- **Household (2)**: {鍋|なべ}つかみ (pot holder), {皇族|こうぞく} (imperial family)
- **Na-adjective (1)**: {演壇|えんだん} (podium)

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









