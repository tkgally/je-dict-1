# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-13
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

### 2026-04-13 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23620-23635) from candidate_words.json. A mix of everyday nouns, commercial/retail vocabulary, medical terms, and formal/ceremonial language.

- **Nouns (11)**: {理容師|りようし} (barber), {売|う}り{手|て} (seller), {全品|ぜんぴん} (all items), {電気工事|でんきこうじ} (electrical work), {七夕祭|たなばたまつ}り (Tanabata festival), {下側|したがわ} (underside), {共和国|きょうわこく} (republic), {動脈硬化|どうみゃくこうか} (arteriosclerosis), {昼型|ひるがた} (day person), {外国製|がいこくせい} (foreign-made), {一般用|いっぱんよう} (for general use), ご{芳名|ほうめい} (your esteemed name — formal)
- **Noun/suru verbs (4)**: {誤飲|ごいん} (accidental swallowing), {転覆|てんぷく} (capsizing / overthrow), {入植|にゅうしょく} (settlement / colonization), {入庫|にゅうこ} (entering a warehouse or garage)
- Removed corresponding candidates from candidate_words.json after entry creation.

### 2026-04-12 (Vocabulary Expansion - 10 New Entries)
Added 10 new dictionary entries (IDs 23610-23619) from candidate_words.json. A mix of Japanese grammar/linguistic terms, disaster-reporting vocabulary, and formal medical/business/accounting terms.

- **Nouns (8)**: {未然形|みぜんけい} (irrealis form), {終止形|しゅうしけい} (terminal/dictionary form), {連体形|れんたいけい} (attributive form), {二人称|ににんしょう} (second person — grammatical), {臀部|でんぶ} (buttocks / gluteal region — formal), {被保険者|ひほけんしゃ} (the insured), {立替金|たてかえきん} (advance payment / reimbursable expense), {造影剤|ぞうえいざい} (contrast agent for medical imaging)
- **Noun/suru verbs (2)**: {床下浸水|ゆかしたしんすい} (below-floor flooding), {床上浸水|ゆかうえしんすい} (above-floor flooding)
- Added new kanji 臀 to kanji_list.json (ID 02678_den_shiri_buttocks)
- Removed 10 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23595-23609) from candidate_words.json. A mix of legal, medical, food, geographical, biological, business, and civics vocabulary of practical value to intermediate learners.

- **Nouns (13)**: {破産者|はさんしゃ} (bankrupt person), {皮膚炎|ひふえん} (dermatitis), {三温糖|さんおんとう} (Japanese light brown sugar), {入場者|にゅうじょうしゃ} (attendee / visitor), {峠道|とうげみち} (mountain pass road), {尾骨|びこつ} (coccyx / tailbone), {親権者|しんけんしゃ} (parent with legal custody), {正式名称|せいしきめいしょう} (official name), {発見者|はっけんしゃ} (discoverer / finder), {営業所|えいぎょうしょ} (sales / branch office), {受精卵|じゅせいらん} (fertilized egg), {閉店時間|へいてんじかん} (closing time), {市議会|しぎかい} (city council), {水力発電|すいりょくはつでん} (hydroelectric power generation)
- **Na-adjectives (1)**: {民族的|みんぞくてき} (ethnic / national)
- Removed 15 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23580-23594) from candidate_words.json. A mix of everyday loanwords, banking and transportation vocabulary, policy/business terms, and technical computing and science terms.

- **Nouns (11)**: メインディッシュ (main dish), {銃撃戦|じゅうげきせん} (shootout), {旅客列車|りょかくれっしゃ} (passenger train), {熱伝導|ねつでんどう} (heat conduction), {磁気|じき}テープ (magnetic tape), {発光|はっこう}ダイオード (light-emitting diode), {演算子|えんざんし} (operator — math/programming), {預金通帳|よきんつうちょう} (bankbook), {学園生活|がくえんせいかつ} (school/campus life), {地域振興|ちいきしんこう} (regional development), {球根|きゅうこん}{植物|しょくぶつ} (bulb plant)
- **Noun/suru verbs (4)**: サインイン (sign in), {均質化|きんしつか} (homogenization), {通帳記入|つうちょうきにゅう} (passbook update), {演算処理|えんざんしょり} (arithmetic processing)
- Removed 15 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 14 New Entries)
Added 14 new dictionary entries (IDs 23566-23579) from candidate_words.json. Focused on high-frequency set expressions, everyday collocations, and common spoken/business phrases that learners encounter early but often lack good dictionary coverage for.

- **Expressions (11)**: よろしくお{願|ねが}いします (please treat me well / I look forward to working with you), お{邪魔|じゃま}します (pardon my intrusion, said on entering), お{邪魔|じゃま}しました (thanks for having me, said on leaving), お{世話|せわ}になっております (thank you for your continued support, business greeting), つまらないものですが (it's just a small thing, said when giving a gift), {靴|くつ}を{脱|ぬ}ぐ (to take off one's shoes), {顔|かお}を{洗|あら}う (to wash one's face), {髪|かみ}を{乾|かわ}かす (to dry one's hair), {次|つぎ}の{駅|えき} (the next station), お{忙|いそが}しいところ (when you are busy, polite preface), {一列|いちれつ}に{並|なら}ぶ (to line up in a single file)
- **Expression/interjection (1)**: {助|たす}けて (help!; help me!)
- **Nouns (2)**: お{水|みず} (water, polite form), {起工式|きこうしき} (groundbreaking ceremony)
- Removed 14 candidates that now exist as entries

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








