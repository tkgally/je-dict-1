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

### 2026-04-13 (Vocabulary Expansion - 18 New Entries)
Added 18 new dictionary entries (IDs 23635-23652) from candidate_words.json. A mix of diplomatic, legal, bureaucratic, meteorological, culinary, grammatical, and everyday vocabulary, including some slang and tech-era terms.

- **Nouns (16)**: {特命全権大使|とくめいぜんけんたいし} (ambassador extraordinary and plenipotentiary), {所定事項|しょていじこう} (required items on a form), {不該当|ふがいとう} (not applicable), {計算手法|けいさんしゅほう} (calculation method), {既遂|きすい} (consummated crime), {正犯|せいはん} (principal offender), {略奪愛|りゃくだつあい} (stealing someone's partner), {暖波|だんぱ} (warm spell / heat wave), {被修飾語|ひしゅうしょくご} (modified word — grammar), {指図役|さしずやく} (person giving orders), {内皮|ないひ} (endothelium / inner skin), {先日付|さきづけ} (post-dating), {逆|ぎゃく}ナン (woman picking up a man — slang), {投|な}げ{銭|せん}{機能|きのう} (tipping feature), {焼|や}き{麩|ふ} (toasted wheat gluten), {生麩|なまふ} (fresh wheat gluten), {八歳|はっさい} (eight years old)
- **Na-adjectives (1)**: {自衛的|じえいてき} (self-defensive)
- Removed 18 candidates that now exist as entries

### 2026-04-13 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23620-23634) from candidate_words.json. A mix of technical, educational, and everyday vocabulary including medical, household, kanji-radical, industrial, mathematical, and number/age terms.

- **Nouns (13)**: {抗炎症|こうえんしょう} (anti-inflammatory), {体脂肪計|たいしぼうけい} (body fat scale), {身長計|しんちょうけい} (stadiometer), ハンマー{投|な}げ (hammer throw), にんべん (person radical 亻), きへん (tree radical 木), {旁|つくり} (right-hand kanji component), スタンプ{台|だい} (ink pad for rubber stamps), {溶鉱炉|ようこうろ} (blast furnace), {四角錐|しかくすい} (square pyramid), {処理装置|しょりそうち} (processing unit), {骨格標本|こっかくひょうほん} (skeletal specimen), {十九歳|じゅうきゅうさい} (nineteen years old), {大量殺人|たいりょうさつじん} (mass murder)
- **Number (1)**: {二万|にまん} (twenty thousand)
- Added new kanji 旁 to kanji_list.json (ID 02679_hou_tsukuri_right-component)
- Removed 15 candidates that now exist as entries

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








