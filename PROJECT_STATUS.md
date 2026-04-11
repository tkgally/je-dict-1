# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-11
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

### 2026-04-11 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 23297-23326) from candidate_words.json. A mix of common everyday vocabulary, practical tech/web terms, health and medical terms, legal/tax vocabulary, and contemporary social keywords.

- **Nouns (18)**: ベジタリアン (vegetarian), {血液検査|けつえきけんさ} (blood test), {尿検査|にょうけんさ} (urine test), {料理教室|りょうりきょうしつ} (cooking class), {持久走|じきゅうそう} (endurance run), {反復横跳|はんぷくよことび}び (side-to-side jumping fitness test), {二次元|にじげん}コード (QR code), {即日|そくじつ}{配送|はいそう} (same-day delivery), {人間|にんげん}ドック (comprehensive medical checkup), ブラック{企業|きぎょう} (exploitative company), {働|はたら}き{方|かた}{改革|かいかく} (work-style reform), フレックス (flextime), {論文審査|ろんぶんしんさ} (thesis examination), {医療費|いりょうひ}{控除|こうじょ} (medical expense deduction), {扶養|ふよう}{控除|こうじょ} (dependent deduction), {間引|まび}き{運転|うんてん} (reduced service), {折返|おりかえ}し{運転|うんてん} (shuttle operation), {口頭試問|こうとうしもん} (oral examination), {寸志|すんし} (small token of gratitude)
- **Noun/suru verbs (5)**: ログインする (to log in), ログアウトする (to log out), {示談|じだん} (out-of-court settlement), {供述|きょうじゅつ} (testimony), {原状回復|げんじょうかいふく} (restoration to original condition), {盗用|とうよう} (plagiarism)
- **Adverbs (2)**: {正|ただ}しく (correctly), {元気|げんき}よく (energetically)
- **Expressions (3)**: {最初|さいしょ}から (from the start), {途中|とちゅう}で (halfway; on the way), {底知|そこし}れない (unfathomable)

### 2026-04-11 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 23277-23296) from candidate_words.json. All nouns — a mix of professional roles, institutional and social vocabulary, finance, military/politics, and everyday practical terms.

- **Nouns (20)**: {国語辞典|こくごじてん} (Japanese dictionary), {調理場|ちょうりば} (commercial kitchen), {研修会|けんしゅうかい} (training session), {相談会|そうだんかい} (consultation session), {担当医|たんとうい} (attending physician), {団体行動|だんたいこうどう} (group action), {発明者|はつめいしゃ} (inventor), {設計者|せっけいしゃ} (designer/architect), {産油国|さんゆこく} (oil-producing country), {開拓者|かいたくしゃ} (pioneer), {戦闘機|せんとうき} (fighter plane), {倹約家|けんやくか} (frugal person), {軍事力|ぐんじりょく} (military strength), {季節労働|きせつろうどう} (seasonal labor), {自己資金|じこしきん} (personal funds), {優待券|ゆうたいけん} (preferential voucher), {調理用具|ちょうりようぐ} (cooking utensils), {視力矯正|しりょくきょうせい} (vision correction), {人数制限|にんずうせいげん} (headcount limit), {防護壁|ぼうごへき} (protective wall)

### 2026-04-11 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23261-23276) from candidate_words.json. A mix of formal, technical, and everyday vocabulary covering food, international politics, security, business, linguistics, body/beauty, and materials science.

- **Nouns (13)**: {一口|ひとくち}サイズ (bite-sized), {核弾頭|かくだんとう} (nuclear warhead), {国交断絶|こっこうだんぜつ} (severance of diplomatic relations), {主力商品|しゅりょくしょうひん} (flagship product), {暗号鍵|あんごうかぎ} (encryption key), {不透明度|ふとうめいど} (opacity), {一重|ひとえ}まぶた (single eyelid), {二重|ふたえ}まぶた (double eyelid), {平和維持活動|へいわいじかつどう} (peacekeeping operations), {摩擦音|まさつおん} (fricative), {競争原理|きょうそうげんり} (principle of competition), {合成樹脂|ごうせいじゅし} (synthetic resin)
- **Noun/suru verbs (2)**: {非核化|ひかくか} (denuclearization), {水耕栽培|すいこうさいばい} (hydroponics)
- **Expressions (2)**: {関係者各位|かんけいしゃかくい} (to whom it may concern), {詳細不明|しょうさいふめい} (details unknown)
- Removed 1 stale candidate (多角形/たかっけい — variant reading duplicate of existing 05553 多角形/たかくけい)

### 2026-04-11 (Vocabulary Expansion - 18 New Entries)
Added 18 new dictionary entries (IDs 23243-23260) from candidate_words.json. A diverse mix of nouns, a godan verb, and two i-adjectives covering nature, academia, law, medicine, housing, exercise, and everyday language.

- **Nouns (11)**: {外来種|がいらいしゅ} (invasive species), {樹齢|じゅれい} (age of a tree), {承認欲求|しょうにんよっきゅう} (need for approval), {腕立|うでた}て{伏|ふ}せ (push-up), {学士|がくし} (bachelor's degree), {紀要|きよう} (academic bulletin), {内視鏡|ないしきょう} (endoscope), {更新料|こうしんりょう} (renewal fee), {公判|こうはん} (court hearing), {食|く}い{意地|いじ} (greed for food), {二重窓|にじゅうまど} (double window)
- **Noun/suru verbs (4)**: {鋳造|ちゅうぞう} (casting), {剽窃|ひょうせつ} (plagiarism), {再診|さいしん} (follow-up medical visit), {自首|じしゅ} (turning oneself in)
- **Godan verb (1)**: {思|おも}い{巡|めぐ}らす (to ponder)
- **I-adjectives (2)**: {聞|き}き{苦|ぐる}しい (hard to listen to), {罪深|つみぶか}い (sinful)
- Added 2 new kanji to index: 鋳 (cast), 剽 (plunder)

### 2026-04-11 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 23223-23242) from candidate_words.json. A mix of formal and technical vocabulary covering medicine, technology, politics, society, and daily life.

- **Nouns (17)**: {中枢神経|ちゅうすうしんけい} (central nervous system), {軍事行動|ぐんじこうどう} (military action), {自己同一性|じこどういつせい} (self-identity), {新興住宅地|しんこうじゅうたくち} (new housing development), {中性脂肪|ちゅうせいしぼう} (triglycerides), {悪性腫瘍|あくせいしゅよう} (malignant tumor), アレルギー{体質|たいしつ} (allergic constitution), {液晶|えきしょう}パネル (LCD panel), {皮下脂肪|ひかしぼう} (subcutaneous fat), {伝達手段|でんたつしゅだん} (means of communication), {電子商取引|でんししょうとりひき} (e-commerce), {通信速度|つうしんそくど} (connection speed), {核軍縮|かくぐんしゅく} (nuclear disarmament), {戦没者|せんぼつしゃ} (the war dead), {自覚症状|じかくしょうじょう} (subjective symptoms), {温暖前線|おんだんぜんせん} (warm front), {居住空間|きょじゅうくうかん} (living space), {身元保証人|みもとほしょうにん} (personal guarantor)
- **Expression/godan verbs (2)**: {意図|いと}を{汲|く}む (to grasp someone's intent), {権力|けんりょく}を{振|ふ}るう (to wield power)
- Added 1 new kanji to index: 瘍 (tumor)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








