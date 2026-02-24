# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-24
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
| Total entries | ~13,454 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,655 (open) |
| Candidate words | ~547 |
| Cross-references | ~3,400 |
| Example sentences | ~46,500 |
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

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 320)
Added 30 new dictionary entries (IDs 13369-13398) from candidate_words.json:

- **Nouns (14)**: {炭|すみ} (charcoal), {炭酸|たんさん} (carbonation), {炊飯|すいはん} (rice cooking), {火花|ひばな} (spark), {灯|あか}り (lamplight), {海産物|かいさんぶつ} (marine products), {湾岸|わんがん} (bay area), {漢方|かんぽう} (kampo medicine), {漢文|かんぶん} (classical Chinese writing), {無罪|むざい} (not guilty), {無言|むごん} (silence), {無効|むこう} (invalid), {無職|むしょく} (unemployed), {無人|むじん} (unmanned)
- **Noun/suru verbs (7)**: {激動|げきどう} (upheaval), {激化|げきか} (intensification), {濃縮|のうしゅく} (concentration), {火葬|かそう} (cremation), {潜入|せんにゅう} (infiltration), {潜在|せんざい} (latent), {点在|てんざい} (scattered), {流用|りゅうよう} (diversion)
- **Verbs (3)**: {澄|す}む (to become clear, godan intransitive), {灯|とも}る (to be lit, godan intransitive), {火照|ほて}る (to flush, godan intransitive)
- **Na-adjective/noun (3)**: {激安|げきやす} (dirt cheap), {無茶|むちゃ} (unreasonable)
- **I-adjective (1)**: {温|あたた}かい (warm)
- **Adverb/noun (1)**: {無断|むだん} (without permission)

Notable features:
- 無- cluster: {無断|むだん}, {無罪|むざい}, {無言|むごん}, {無効|むこう}, {無職|むしょく}, {無茶|むちゃ}, {無人|むじん}
- 激- cluster: {激動|げきどう}, {激化|げきか}, {激安|げきやす}
- Fire/light cluster: {火花|ひばな}, {火葬|かそう}, {火照|ほて}る, {灯|あか}り, {灯|とも}る, {炭|すみ}, {炭酸|たんさん}
- 潜- pair: {潜入|せんにゅう} (infiltration) ↔ {潜在|せんざい} (latent)
- Multi-sense entries: {潮|しお} (2), {澄|す}む (2), {炭酸|たんさん} (2), {火花|ひばな} (2), {無人|むじん} (2), {流用|りゅうよう} (2), {温|あたた}かい (2)
- Kanji contrast: {温|あたた}かい vs {暖|あたた}かい (food/feelings vs weather/climate)
- Cultural: {漢方|かんぽう} (traditional medicine), {漢文|かんぶん} (classical Chinese study), {火葬|かそう} (cremation customs), {炭|すみ} (charcoal in tea ceremony)
- New kanji: 2,400 → 2,401 ({澄|すむ})

Total entries: 13,424 → 13,454 (approximate)
Remaining candidates: 577 → 547 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 319)
Added 30 new dictionary entries (IDs 13339-13368) from candidate_words.json:

- **Verbs (8)**: {浸る|ひたる} (to be immersed, godan intransitive), {清める|きよめる} (to purify, ichidan transitive), {泣きじゃくる|なきじゃくる} (to sob, godan intransitive), {泣き崩れる|なきくずれる} (to break down in tears, ichidan intransitive), {決め込む|きめこむ} (to assume/pretend, godan transitive), {添う|そう} (to accompany/marry, godan intransitive), {減じる|げんじる} (to reduce, ichidan), {換える|かえる} (to exchange, ichidan transitive)
- **Nouns (15)**: {深入り|ふかいり} (overinvolvement), {渦中|かちゅう} (in the midst of), {渾身|こんしん} (with all one's might), {浴場|よくじょう} (bathhouse), {消失|しょうしつ} (disappearance), {混在|こんざい} (intermingling), {添加|てんか} (addition of substances), {清酒|せいしゅ} (refined sake), {減量|げんりょう} (weight reduction), {渡来|とらい} (arrival from abroad), {満了|まんりょう} (expiration), {満天|まんてん} (whole sky), {源流|げんりゅう} (headwaters/origin), {漏れ|もれ} (leak/omission), {流儀|りゅうぎ} (style/manner)
- **Noun/suru verbs (5)**: {滅亡|めつぼう} (downfall), {演習|えんしゅう} (exercise/drill), {混浴|こんよく} (mixed bathing), {深入り|ふかいり}, {消失|しょうしつ}
- **Other (2)**: {滅多|めった} (rarely/reckless, adverb/na-adj), {法被|はっぴ} (happi coat), {流派|りゅうは} (school/style), {海女|あま} (ama diver)

Notable features:
- Crying cluster: {泣きじゃくる|なきじゃくる} (to sob) ↔ {泣き崩れる|なきくずれる} (to break down in tears)
- 流- cluster: {流儀|りゅうぎ} (personal style) ↔ {流派|りゅうは} (school/tradition)
- 減- cluster: {減じる|げんじる} (to reduce), {減量|げんりょう} (weight loss)
- Water/bathing: {浴場|よくじょう}, {混浴|こんよく}, {清酒|せいしゅ}, {浸る|ひたる}
- Multi-sense entries: {浸る|ひたる} (2), {清める|きよめる} (2), {決め込む|きめこむ} (2), {添う|そう} (2), {源流|げんりゅう} (2), {滅多|めった} (2), {漏れ|もれ} (2), {演習|えんしゅう} (2), {換える|かえる} (1, with kanji distinction notes)
- Cultural: {法被|はっぴ} (festival coat), {海女|あま} (pearl diving), {混浴|こんよく} (bathing customs), {清める|きよめる} (Shinto purification), {清酒|せいしゅ} (sake)
- New kanji: 2,399 → 2,400 ({渾|こん})

Total entries: 13,394 → 13,424 (approximate)
Remaining candidates: 607 → 577 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 318)
Added 30 new dictionary entries (IDs 13309-13338) from candidate_words.json:

- **Nouns (13)**: {水中|すいちゅう} (underwater), {水平線|すいへいせん} (horizon), {清流|せいりゅう} (clear stream), {溶岩|ようがん} (lava), {漆器|しっき} (lacquerware), {深み|ふかみ} (depth), {海水|かいすい} (seawater), {湯船|ゆぶね} (bathtub), {気づき|きづき} (awareness)
- **Na-adjectives (2)**: {浅はか|あさはか} (shallow/thoughtless), {清らか|きよらか} (pure)
- **Noun/suru verbs (10)**: {減税|げんぜい} (tax cut), {満載|まんさい} (fully loaded), {派生|はせい} (derivation), {流入|りゅうにゅう} (influx), {流出|りゅうしゅつ} (outflow), {消滅|しょうめつ} (extinction), {混迷|こんめい} (turmoil), {減速|げんそく} (deceleration), {源泉|げんせん} (source), {漂流|ひょうりゅう} (drifting)
- **Verbs (5)**: {渋る|しぶる} (to hesitate, godan), {浮かべる|うかべる} (to float/show expression, ichidan transitive), {添える|そえる} (to add/garnish, ichidan transitive), {演じる|えんじる} (to perform, ichidan transitive), {滅ぼす|ほろぼす} (to destroy, godan transitive)
- **Other (2)**: {満開|まんかい} (full bloom), {湧く|わく} (to well up, godan intransitive), {湿る|しめる} (to get damp, godan intransitive), {渦巻く|うずまく} (to swirl, godan intransitive)

Notable features:
- Water/nature theme: {水中|すいちゅう}, {水平線|すいへいせん}, {清流|せいりゅう}, {海水|かいすい}, {溶岩|ようがん}, {湧く|わく}, {漂流|ひょうりゅう}
- 流- cluster: {流入|りゅうにゅう}↔{流出|りゅうしゅつ} (antonym pair with cross-refs)
- 減- cluster: {減税|げんぜい}, {減速|げんそく}
- Multi-sense entries: {浮かべる|うかべる} (2), {湧く|わく} (2), {深み|ふかみ} (2), {渦巻く|うずまく} (2), {源泉|げんせん} (2)
- Cultural: {漆器|しっき} (traditional lacquerware), {湯船|ゆぶね} (Japanese bathing), {満開|まんかい} (cherry blossom season)
- Transitive/intransitive pairs: {浮かべる|うかべる}↔{浮かぶ|うかぶ}, {滅ぼす|ほろぼす}↔{滅びる|ほろびる}

Total entries: 13,364 → 13,394 (approximate)
Remaining candidates: 637 → 607 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 317)
Added 30 new dictionary entries (IDs 13279-13308) from candidate_words.json:

- **Nouns (16)**: {沿岸|えんがん} (coast), {派出所|はしゅつしょ} (police box), {浮世絵|うきよえ} (ukiyo-e), {海底|かいてい} (seabed), {海賊|かいぞく} (pirate), {海軍|かいぐん} (navy), {消火|しょうか} (firefighting), {深呼吸|しんこきゅう} (deep breath), {法人|ほうじん} (corporation), {法令|ほうれい} (law/ordinance), {沢庵|たくあん} (pickled daikon), {浮き彫り|うきぼり} (relief/highlighting), {深読み|ふかよみ} (overinterpretation), {流行語|りゅうこうご} (buzzword), {浅漬け|あさづけ} (quick pickles), {洋風|ようふう} (Western-style)
- **Na-adjective (1)**: {法的|ほうてき} (legal)
- **I-adjective (1)**: {淡い|あわい} (faint, pale)
- **Noun/suru verbs (7)**: {洗濯|せんたく} (laundry), {消耗|しょうもう} (consumption), {混同|こんどう} (confusion), {治癒|ちゆ} (healing), {泣き寝入り|なきねいり} (giving up without recourse), {浮気|うわき} (infidelity), {浪人|ろうにん} (ronin/exam retaker)
- **Verbs (5)**: {沿う|そう} (to follow along, godan intransitive), {泊める|とめる} (to let stay, ichidan transitive), {浸かる|つかる} (to soak, godan intransitive), {淹れる|いれる} (to brew, ichidan transitive), {混沌|こんとん} (chaos, taru-adj)

Notable features:
- Water/liquid cluster: {沿岸|えんがん}, {海底|かいてい}, {海賊|かいぞく}, {海軍|かいぐん}, {浸かる|つかる}, {淹れる|いれる}
- Law cluster: {法人|ほうじん}, {法令|ほうれい}, {法的|ほうてき}
- Food cluster: {沢庵|たくあん}, {浅漬け|あさづけ}, {洋風|ようふう} (with cross-references)
- Multi-sense entries: {沿う|そう} (2), {浮気|うわき} (2), {淡い|あわい} (2), {浸かる|つかる} (2), {浮き彫り|うきぼり} (2), {浪人|ろうにん} (2)
- Cultural: {浮世絵|うきよえ} (Edo art), {派出所|はしゅつしょ} (police system), {浪人|ろうにん} (exam culture), {沢庵|たくあん} (Zen cuisine)
- New kanji: 2,396 → 2,399 ({庵|あん}, {沌|とん}, {癒|ゆ})

Total entries: 13,334 → 13,364 (approximate)
Remaining candidates: 667 → 637 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 316)
Added 30 new dictionary entries (IDs 13249-13278) from candidate_words.json:

- **Nouns (18)**: {決着|けっちゃく} (settlement), {決|き}め{手|て} (deciding factor), {気品|きひん} (elegance), {気質|きしつ} (temperament), {民衆|みんしゅう} (the masses), {水害|すいがい} (flood damage), {水田|すいでん} (rice paddy), {水蒸気|すいじょうき} (steam), {水路|すいろ} (waterway), {汚名|おめい} (disgrace), {氷柱|つらら} (icicle), {沿道|えんどう} (roadside), {波乱|はらん} (turbulence), {没後|ぼつご} (after death), {河川|かせん} (river), {戦乱|せんらん} (turmoil of war), {洋食|ようしょく} (Western food), {民間|みんかん} (private sector)
- **Na-adjective (1)**: {活発|かっぱつ} (active, lively)
- **Noun/na-adjective (1)**: {気|き}がかり (worry, concern)
- **Noun/suru verbs (6)**: {沈黙|ちんもく} (silence), {決断|けつだん} (decision), {決戦|けっせん} (decisive battle), {気兼|きが}ね (reserve), {派遣|はけん} (dispatch/temp staffing), {抹殺|まっさつ} (obliteration)
- **Verbs (2)**: {決|き}めつける (to jump to conclusions, ichidan), {気遣|きづか}う (to worry about, godan)
- **Multi-sense entries (2)**: {民間|みんかん} (2 senses), {派遣|はけん} (2 senses)

Notable features:
- 決- cluster: {決断|けつだん}, {決着|けっちゃく}, {決|き}め{手|て}, {決戦|けっせん}, {決|き}めつける
- 気- cluster: {気合|きあ}い, {気品|きひん}, {気質|きしつ}, {気|き}がかり, {気兼|きが}ね, {気遣|きづか}う
- 水- cluster: {水害|すいがい}, {水田|すいでん}, {水蒸気|すいじょうき}, {水路|すいろ}
- 民- pair: {民衆|みんしゅう}, {民間|みんかん}
- Cultural: {洋食|ようしょく} (Meiji-era Western food), {気兼|きが}ね (Japanese social restraint), {水田|すいでん} (rice cultivation)

Total entries: 13,304 → 13,334 (approximate)
Remaining candidates: 697 → 667 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
