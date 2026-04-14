# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-14
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

### 2026-04-14 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 23668-23697) from candidate_words.json. A mix of technology, architecture, business, ecology, grammar, accounting, and general vocabulary for intermediate learners.

- **Nouns (20)**: {高画質|こうがしつ} (high image quality), {低画質|ていがしつ} (low image quality), {平面図|へいめんず} (floor plan), {立面図|りつめんず} (elevation drawing), {原始林|げんしりん} (primeval forest), {自然林|しぜんりん} (natural forest), {地元紙|じもとし} (local newspaper), {歴史学|れきしがく} (history as a discipline), {奇術|きじゅつ} (stage magic), {出世欲|しゅっせよく} (desire for career advancement), {提出書類|ていしゅつしょるい} (required submission documents), {金管楽器|きんかんがっき} (brass instrument), {低品質|ていひんしつ} (low quality), {上級者向|じょうきゅうしゃむ}け (for advanced users), {初級者向|しょきゅうしゃむ}け (for beginners), つなぎ{役|やく} (intermediary / bridging role), {提携先|ていけいさき} (business partner), {会議費|かいぎひ} (meeting expenses, accounting), {給水塔|きゅうすいとう} (water tower), {受|う}け{止|と}め{方|かた} (way of taking/interpreting), {成語|せいご} (set phrase/idiom)
- **Noun+suru verbs (5)**: {自給|じきゅう} (self-sufficiency in supply), {自足|じそく} (self-sufficiency), {事故死|じこし} (accidental death), {送風|そうふう} (ventilation/fan), {正比例|せいひれい} (direct proportion), {区別化|くべつか} (differentiation)
- **Expressions (3)**: どのように (how, in what way), {仕事|しごと}のやりがい (fulfillment at work), {対価|たいか}を{払|はら}う (to pay a price)
- Added conjugation tables to 6 new suru verbs automatically
- Removed 30 candidates that now exist as entries

### 2026-04-13 (Vocabulary Expansion - 15 New Entries)
Added 15 new dictionary entries (IDs 23653-23667) from candidate_words.json. A mix of historical, biological, medical, geographical, business, geometric, and everyday vocabulary.

- **Nouns (15)**: {引|ひ}き{揚|あ}げ{者|しゃ} (postwar repatriate), {誕生祭|たんじょうさい} (birthday celebration, esp. for an idol/character), {二十日鼠|はつかねずみ} (house mouse), {齧歯類|げっしるい} (rodents), {死後硬直|しごこうちょく} (rigor mortis), {家庭用|かていよう}ゲーム{機|き} (home game console), {耳鼻咽喉科|じびいんこうか} (ENT department), {輸液|ゆえき} (IV infusion), {首長竜|くびながりゅう} (plesiosaur), {返信|へんしん}はがき (reply postcard), {同族企業|どうぞくきぎょう} (family business), {正三角形|せいさんかくけい} (equilateral triangle), {二十三区|にじゅうさんく} (Tokyo's 23 wards), {顎紐|あごひも} (chin strap), {脱脂粉乳|だっしふんにゅう} (skim milk powder)
- Removed 15 candidates that now exist as entries

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








