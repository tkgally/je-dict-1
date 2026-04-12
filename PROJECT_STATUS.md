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

### 2026-04-12 (Vocabulary Expansion - 22 New Entries)
Added 22 new dictionary entries (IDs 23459-23482) from candidate_words.json. A diverse mix of vocabulary across cooking, language/phonetics, business, military/history, culture, health, nature, and modern slang.

- **Nouns (18)**: {論争点|ろんそうてん} (point of contention), {縦列|じゅうれつ} (column/vertical row), {御神体|ごしんたい} (sacred shrine object), {拗音|ようおん} (contracted sounds), {撥音|はつおん} (nasal n sound), {左党|さとう} (sake lover), {自著|じちょ} (one's own book), {設定温度|せっていおんど} (set temperature), {多目的室|たもくてきしつ} (multi-purpose room), {能力給|のうりょくきゅう} (merit pay), {営業収益|えいぎょうしゅうえき} (operating revenue), {多忙期|たぼうき} (busy period), {情趣|じょうしゅ} (charm/refined atmosphere), {陣形|じんけい} (battle formation), {本営|ほんえい} (headquarters), {商売仇|しょうばいがたき} (business rival), {空一面|そらいちめん} (entire sky), {脂性|あぶらしょう} (oily skin), {果菜|かさい} (fruit vegetable), {慢性病|まんせいびょう} (chronic illness), しんどさ (tiredness/hardship)
- **Noun/suru verbs (2)**: {調味|ちょうみ}する (to season food), {裏漉|うらご}し (straining/sieving)
- **Expression (1)**: マウントを{取|と}る (to one-up/assert dominance)
- Removed 2 stale candidates (base forms already existed)

### 2026-04-12 (Vocabulary Expansion - 24 New Entries)
Added 24 new dictionary entries (IDs 23435-23458) from candidate_words.json. A diverse mix of food/cooking, language/phonetics, formal/business, nature, technology, and cultural vocabulary.

- **Nouns (21)**: {魚介類|ぎょかいるい} (seafood), {諸般|しょはん} (various/sundry), {天候不良|てんこうふりょう} (inclement weather), {屋台村|やたいむら} (food stall village), {枝垂|しだ}れ (weeping tree), {麻婆茄子|まーぼーなす} (mapo eggplant), {電源|でんげん}コード (power cord), {鶏|とり}ひき{肉|にく} (ground chicken), {豚|ぶた}ひき{肉|にく} (ground pork), {肉|にく}だね (meat filling), {炒|い}りごま (toasted sesame), {茶殻|ちゃがら} (used tea leaves), {指示書|しじしょ} (instruction document), {昇降機|しょうこうき} (elevator/lift), お{餅|もち} (rice cake), スキューバ (scuba), {半濁音|はんだくおん} (semi-voiced sound), {白|しろ}ごま (white sesame), {黒|くろ}ごま (black sesame), くず{粉|こ} (arrowroot starch), {清音|せいおん} (voiceless sound)
- **Noun/suru verbs (3)**: {拝受|はいじゅ} (humble receipt), {警護|けいご} (bodyguarding), {作付|さくづ}け (crop planting)
- 1 new kanji added to index: 茄 (eggplant)

### 2026-04-12 (Vocabulary Expansion - 30 New Entries)
Added 30 new dictionary entries (IDs 23405-23434) from candidate_words.json. A diverse mix of everyday and learner-useful vocabulary: loanwords, body parts, clothing, food/kitchen, beauty, music, geography, law, art, ethics, and communication.

- **Nouns (20)**: デスク (desk / desk editor), チラシ (flyer), {目元|めもと} (around the eyes), {耳栓|みみせん} (earplugs), {休憩室|きゅうけいしつ} (break room), ブーケ (bouquet), オーブントースター (toaster oven), グルテンフリー (gluten-free), {北極圏|ほっきょくけん} (Arctic Circle), {倫理観|りんりかん} (sense of ethics), {下唇|したくちびる} (lower lip), {夏服|なつふく} (summer clothes), {短縮形|たんしゅくけい} (shortened form), サッシ (window sash), コーヒーカップ (coffee cup / teacup ride), ブラスバンド (brass band), ダイレクトメッセージ (direct message), {解熱|げねつ} (lowering a fever), {予熱|よねつ} (preheating), {肖像画|しょうぞうが} (portrait painting)
- **Verb-suru (5)**: デッサン, {投函|とうかん}, カール, デコレーション (also nouns)
- **Verbs (2)**: {言|い}いくるめる (to talk into — ichidan), ぬぐい{去|さ}る (to wipe away — godan)
- **Na-adjective (1)**: {可憐|かれん}な (sweet and delicate)
- **Other (2)**: ええと (filler word — interjection), ブルゾン (blouson jacket), {誘導尋問|ゆうどうじんもん} (leading question)
- 2 new kanji added to index: 函, 肖

### 2026-04-12 (Vocabulary Expansion - 16 New Entries)
Added 16 new dictionary entries (IDs 23389-23404) from candidate_words.json. A broad mix of everyday and specialized vocabulary across nouns, a suru verb, and two na-adjectives — covering marine biology, geology, mathematics, education, technology, military, cuisine, and abstract concepts.

- **Nouns (13)**: {駆逐艦|くちくかん} (destroyer), {渡航費|とこうひ} (overseas travel expenses), {携帯端末|けいたいたんまつ} (mobile device / handheld terminal), {中等教育|ちゅうとうきょういく} (secondary education), {水菜|みずな} (mizuna / Japanese mustard greens), {二枚貝|にまいがい} (bivalve), {巻|ま}き{貝|がい} (univalve / spiral-shelled mollusk), {石灰岩|せっかいがん} (limestone), {自然数|しぜんすう} (natural number), {先史|せんし} (prehistory), {教育機関|きょういくきかん} (educational institution), {記憶媒体|きおくばいたい} (storage medium), {実数|じっすう} (real number / actual count — multi-sense)
- **Verb-suru (1)**: {画一化|かくいつか}する (to standardize / homogenize)
- **Na-adjectives (2)**: {規則的|きそくてき} (regular / systematic), {野性的|やせいてき} (wild / primal / rugged)

### 2026-04-11 (Vocabulary Expansion - 14 New Entries)
Added 14 new dictionary entries (IDs 23375-23388) from candidate_words.json. A mix of everyday nouns, sports, science and math vocabulary, a business term, and several idiomatic expressions.

- **Nouns (11)**: {光線銃|こうせんじゅう} (ray gun), {女子中学生|じょしちゅうがくせい} (junior high school girl), {副|ふく}キャプテン (vice-captain), {三段跳|さんだんと}び (triple jump), {副団長|ふくだんちょう} (deputy leader of a troupe), {事前交渉|じぜんこうしょう} (prior negotiation), {人工皮革|じんこうひかく} (synthetic leather), {平行四辺形|へいこうしへんけい} (parallelogram), {最優秀選手|さいゆうしゅうせんしゅ} (MVP), {過飽和|かほうわ} (supersaturation), {群体|ぐんたい} (colonial organism)
- **Expressions (3)**: {看板|かんばん}を{掲|かか}げる (to hang out a sign / to publicly proclaim), {歴史|れきし}を{紐解|ひもと}く (to delve into history), {脇道|わきみち}にそれる (to go off on a tangent)

### 2026-04-11 (Vocabulary Expansion - 20 New Entries)
Added 20 new dictionary entries (IDs 23355-23374) from candidate_words.json. A diverse mix of everyday vocabulary, tech and business terms, a medical word, and formal written-register vocabulary.

- **Nouns (16)**: {翌年|よくねん} (the following year), {血行|けっこう} (blood circulation), {自己|じこ} (the self), お{嬢様|じょうさま} (young lady), {英和辞典|えいわじてん} (English-Japanese dictionary), {電源|でんげん}ボタン (power button), コンシーラー (concealer), {牛|ぎゅう}ひき{肉|にく} (ground beef), {腫瘍|しゅよう} (tumor), {初期値|しょきち} (initial/default value), {交渉力|こうしょうりょく} (negotiating skill / bargaining power), {天性|てんせい} (innate nature), {数百|すうひゃく} (several hundred), {実利|じつり} (practical benefit), {追加|ついか}{予算|よさん} (additional budget), {悲運|ひうん} (tragic fate), {賛同者|さんどうしゃ} (supporter)
- **Noun/suru verb (1)**: {結晶化|けっしょうか} (crystallization; figurative taking form)
- **Expressions (2)**: {唯一|ゆいいつ}の (the only; the sole), {多|おお}くの (many of; a lot of — attributive)



_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_








