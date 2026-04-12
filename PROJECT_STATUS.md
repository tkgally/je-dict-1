# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-12
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

### 2026-04-12 (Vocabulary Expansion - 21 New Entries)
Added 21 new dictionary entries (IDs 23545-23565) from candidate_words.json. A mix of everyday, academic, business, and formal vocabulary: time expressions, adverbs, nouns for daily life and technology, mathematical and philosophical terms, and formal compounds used in business and administrative contexts.

- **Nouns (13)**: {食事|しょくじ}{会|かい} (meal gathering), コピー{機|き} (copier), ニックネーム (nickname), {自家用車|じかようしゃ} (private car), {有理数|ゆうりすう} (rational number), {倫理学|りんりがく} (ethics / moral philosophy), {大工|だいく}{道具|どうぐ} (carpentry tools), {音響|おんきょう}{設備|せつび} (sound equipment), {法医学|ほういがく} (forensic medicine), {付|つ}け{替|か}え (replacement / swap), {公約数|こうやくすう} (common divisor — multi-sense), {教育|きょういく}{課程|かてい} (curriculum), {添付|てんぷ}{書類|しょるい} (attached documents), {番号|ばんごう}{順|じゅん} (numerical order)
- **Noun/suru verbs (4)**: {安全|あんぜん}{管理|かんり} (safety management), {自己|じこ}{認識|にんしき} (self-awareness), {弔問|ちょうもん} (condolence visit), {機密|きみつ}{保持|ほじ} (confidentiality / NDA)
- **Noun/na-adjective (1)**: {非合理|ひごうり} (irrationality / irrational)
- **Expression (1)**: {昔|むかし}から (from a long time ago)
- **Adverb (1)**: {極端|きょくたん}に (extremely)
- Removed 21 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 30 New Practical Entries)
Added 30 new dictionary entries (IDs 23515-23544) from candidate_words.json. Focused on practical, daily-life vocabulary useful for foreign residents and travelers in Japan: housing, finance, transportation, technology, entertainment, and business communication.

- **Nouns (30)**: お{寺|てら} (Buddhist temple), トレー (tray), メーター (meter/gauge), キャラクター (fictional/mascot character), アトラクション (amusement park attraction), {普通|ふつう}{預金|よきん} (savings account), {国際|こくさい}{郵便|ゆうびん} (international mail), コンビニ{払|ばら}い (convenience store payment), {日本語|にほんご}{学校|がっこう} (Japanese language school), {為替|かわせ}レート (exchange rate), {燃|も}えないゴミ (non-burnable trash), {在留|ざいりゅう}カード (residence card), ICカード (IC transit card), ペット{可|か} (pets allowed), {音声|おんせい}ガイド (audio guide), {保険|ほけん}{会社|がいしゃ} (insurance company), {管理|かんり}{会社|がいしゃ} (management company), {相談|そうだん}{窓口|まどぐち} (consultation counter), {引|ひ}っ{越|こ}し{業者|ぎょうしゃ} (moving company), {国民|こくみん}{年金|ねんきん} (national pension), ジェットコースター (roller coaster), SIMカード (SIM card), {訳|やく} (translation), ご{挨拶|あいさつ} (formal greeting), タイム (time/time-out), メールアドレス (email address), {共用|きょうよう}{部分|ぶぶん} (shared area), {実行|じっこう}{委員|いいん} (organizing committee member), {横|よこ}{一列|いちれつ} (horizontal line), ご{確認|かくにん} (confirmation, formal)
- Removed 30 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 23495-23514) from candidate_words.json. A diverse mix of practical, everyday vocabulary useful for intermediate learners: food/drink, health, daily life, travel, entertainment, culture, and nature.

- **Nouns (17)**: {朝日|あさひ} (morning sun), {生|なま}ビール (draft beer), {痛|いた}み{止|ど}め (painkiller), {還付|かんぷ} (refund), {端数|はすう} (fraction/odd amount), {暑中見舞|しょちゅうみま}い (summer greeting card), {親知|おやし}らず (wisdom tooth), {番号札|ばんごうふだ} (numbered ticket), {送|おく}り{先|さき} (destination address), ドリンク (drink/beverage), ナビ (navigation), {防災|ぼうさい}グッズ (disaster supplies), {取|と}り{付|つ}け (installation), {便名|びんめい} (flight number), {日誌|にっし} (daily log), {怪我人|けがにん} (injured person), ポップコーン (popcorn)
- **Noun/suru verbs (2)**: {還付|かんぷ} (refund), {開演|かいえん} (start of performance) — both also function as nouns
- **Noun/suffix (1)**: {抜|ぬ}き (without/excluding)
- **Expression (1)**: {目|め}が{覚|さ}める (to wake up; to come to one's senses)
- Removed 20 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 12 New Entries)
Added 12 new dictionary entries (IDs 23483-23494) from candidate_words.json. A mix of food, nature, time, culture, science, occupational, diplomatic, and art vocabulary.

- **Nouns (11)**: {菜|な}っ{葉|ぱ} (leafy greens), {遊歩道|ゆうほどう} (promenade/walkway), {年数|ねんすう} (number of years), {墓参|ぼさん} (visiting a grave), {組成|そせい} (composition/makeup), {門下|もんか} (disciples/pupils), {行員|こういん} (bank employee), {特使|とくし} (special envoy), {散歩道|さんぽみち} (walking path), {水夫|すいふ} (sailor), {画壇|がだん} (art world)
- **Noun/suru verb (1)**: {去勢|きょせい} (castration/neutering)
- Removed 12 candidates that now exist as entries

### 2026-04-12 (Vocabulary Expansion - 22 New Entries)
Added 22 new dictionary entries (IDs 23459-23482) from candidate_words.json. A diverse mix of vocabulary across cooking, language/phonetics, business, military/history, culture, health, nature, and modern slang.

- **Nouns (18)**: {論争点|ろんそうてん} (point of contention), {縦列|じゅうれつ} (column/vertical row), {御神体|ごしんたい} (sacred shrine object), {拗音|ようおん} (contracted sounds), {撥音|はつおん} (nasal n sound), {左党|さとう} (sake lover), {自著|じちょ} (one's own book), {設定温度|せっていおんど} (set temperature), {多目的室|たもくてきしつ} (multi-purpose room), {能力給|のうりょくきゅう} (merit pay), {営業収益|えいぎょうしゅうえき} (operating revenue), {多忙期|たぼうき} (busy period), {情趣|じょうしゅ} (charm/refined atmosphere), {陣形|じんけい} (battle formation), {本営|ほんえい} (headquarters), {商売仇|しょうばいがたき} (business rival), {空一面|そらいちめん} (entire sky), {脂性|あぶらしょう} (oily skin), {果菜|かさい} (fruit vegetable), {慢性病|まんせいびょう} (chronic illness), しんどさ (tiredness/hardship)
- **Noun/suru verbs (2)**: {調味|ちょうみ}する (to season food), {裏漉|うらご}し (straining/sieving)
- **Expression (1)**: マウントを{取|と}る (to one-up/assert dominance)
- Removed 2 stale candidates (base forms already existed)





_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








