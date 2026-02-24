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
| Total entries | ~13,544 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,745 (open) |
| Candidate words | ~457 |
| Cross-references | ~3,400 |
| Example sentences | ~46,600 |
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

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 323)
Added 30 new dictionary entries (IDs 13459-13488) from candidate_words.json:

- **Time/day noun (1)**: {火曜|かよう} (Tuesday)
- **Food/cooking nouns (4)**: {熱湯|ねっとう} (boiling water), {燻製|くんせい} (smoked food), {牛蒡|ごぼう} (burdock root), {牡丹|ぼたん} (peony)
- **片- cluster (3)**: {片手|かたて} (one hand), {片言|かたこと} (broken speech), {片隅|かたすみ} (corner/nook)
- **特- cluster (9)**: {特訓|とっくん} (special training), {特許|とっきょ} (patent), {特集|とくしゅう} (special feature), {特典|とくてん} (bonus/perk), {特化|とっか} (specialization), {特有|とくゆう} (peculiar to), {特産品|とくさんひん} (local specialty), {特色|とくしょく} (distinctive feature), {特注|とくちゅう} (custom order)
- **無- cluster (5)**: {無視|むし} (ignoring), {無責任|むせきにん} (irresponsible), {無条件|むじょうけん} (unconditional), {無能|むのう} (incompetent), {無縁|むえん} (unrelated)
- **Noun/suru verbs (5)**: {物|もの}まね (mimicry), {特訓|とっくん}, {特集|とくしゅう}, {特化|とっか}, {熱狂|ねっきょう} (frenzy)
- **Other nouns (6)**: {燃料|ねんりょう} (fuel), {犯行|はんこう} (criminal act), {焼失|しょうしつ} (destruction by fire), {深層|しんそう} (deep layer), {熱弁|ねつべん} (passionate speech), {物言|ものい}い (way of speaking/objection)

Notable features:
- 特- cluster: 9 entries covering training, patents, media, commerce, and culture
- 無- cluster: 5 entries covering social behavior, morality, and philosophy
- 片- cluster: 3 entries covering body, language, and space
- Multi-sense entries: {物言|ものい}い (2: speech manner + objection/sumo term)
- Cultural: {牡丹|ぼたん} (flower symbolism, botan-nabe), {牛蒡|ごぼう} (burdock in Japanese cooking), {物|もの}まね (impersonation comedy), {特産品|とくさんひん} (regional products/omiyage culture)
- Homophone cross-refs: {犯行|はんこう}↔{反抗|はんこう}, {焼失|しょうしつ}↔{消失|しょうしつ}
- New kanji: 2,404 → 2,405 ({蒡|ぼう})

Total entries: 13,514 → 13,544 (approximate)
Remaining candidates: 487 → 457 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 322)
Added 30 new dictionary entries (IDs 13429-13458) from candidate_words.json:

- **Nouns (20)**: {瀕死|ひんし} (near death), {火|ひ}の{粉|こ} (sparks), {濁|にご}り (cloudiness), {激流|げきりゅう} (torrent), {深淵|しんえん} (abyss), {潮目|しおめ} (tidal front/turning point), {演者|えんじゃ} (performer), {演芸|えんげい} (performing arts), {漢詩|かんし} (Chinese poetry), {漢語|かんご} (Sino-Japanese word), {最低賃金|さいていちんぎん} (minimum wage), {最安値|さいやすね} (lowest price), {氷河期|ひょうがき} (ice age), {浄土|じょうど} (Pure Land), {旗本|はたもと} (hatamoto), {怨霊|おんりょう} (vengeful spirit), {淵|ふち} (deep pool/abyss), {灰汁|あく} (scum/lye), {無傷|むきず} (unscathed), {新進気鋭|しんしんきえい} (up-and-coming)
- **Noun/suru verbs (4)**: {激闘|げきとう} (fierce battle), {撃破|げきは} (crushing defeat), {擁立|ようりつ} (to install a leader), {憑依|ひょうい} (spirit possession)
- **Noun/suru verb (work) (1)**: {本採用|ほんさいよう} (permanent hire)
- **Noun/suffix (1)**: {気味|きみ} (sensation/touch of)
- **Formal nouns (2)**: {我|わ}が{国|くに} (our country), {所存|しょぞん} (intention, humble)
- **Noun with two senses (2)**: {沙汰|さた} (notice/affair), {手打|てう}ち (handmade/settlement)

Notable features:
- Multi-sense entries: {潮目|しおめ} (2), {気味|きみ} (2), {沙汰|さた} (2), {手打|てう}ち (2), {淵|ふち} (2), {灰汁|あく} (3), {無傷|むきず} (2)
- Supernatural cluster: {怨霊|おんりょう}, {憑依|ひょうい} (with cross-cultural notes)
- Historical: {旗本|はたもと} (Edo-period), {浄土|じょうど} (Buddhist Pure Land)
- 激- cluster: {激流|げきりゅう}, {激闘|げきとう}, {撃破|げきは}
- Cultural: {灰汁|あく} (cooking technique), {演芸|えんげい} (variety entertainment), {漢詩|かんし}/{漢語|かんご} (language/literature)
- Formal register: {所存|しょぞん} (humble), {我|わ}が{国|くに} (official)
- New kanji: 2,402 → 2,404 ({擁|よう}, {淵|えん})

Total entries: 13,484 → 13,514 (approximate)
Remaining candidates: 517 → 487 (30 removed)

### 2026-02-24 (Vocabulary Expansion - 30 New Entries, Session 321)
Added 30 new dictionary entries (IDs 13399-13428) from candidate_words.json:

- **Verbs (6)**: {替|か}える (to replace, ichidan transitive), {有|ゆう}する (to possess, suru formal), {瀕|ひん}する (to be on the verge of, suru), {炒|い}る (to roast, godan transitive), {点|た}てる (to make tea, ichidan transitive), {煮立|にた}つ (to come to a boil, godan intransitive)
- **Food nouns (5)**: {焼|や}きそば (fried noodles), {焼|や}き{魚|ざかな} (grilled fish), {煎茶|せんちゃ} (sencha green tea), {煮干|にぼ}し (dried sardines for broth), {点心|てんしん} (dim sum)
- **Light/fire nouns (4)**: {灯籠|とうろう} (lantern), {灯|ともしび} (light/lamp), {火種|ひだね} (ember/source of conflict), {火星|かせい} (Mars)
- **General nouns (4)**: {焦点|しょうてん} (focus/focal point), {熟成|じゅくせい} (aging/maturation), {激戦|げきせん} (fierce battle), {激突|げきとつ} (clash/collision)
- **Na-adjectives/nouns (7)**: {濃密|のうみつ} (dense/intense), {無力|むりょく} (powerless), {無名|むめい} (unknown), {無垢|むく} (pure/innocent), {無謀|むぼう} (reckless), {無関心|むかんしん} (indifferent), {無常|むじょう} (impermanence)
- **Other (4)**: {漫然|まんぜん} (aimlessly, adverb), {潮流|ちょうりゅう} (tidal current/trend), {煙幕|えんまく} (smokescreen), {演目|えんもく} (program item)

Notable features:
- 無- cluster: {無力|むりょく}, {無名|むめい}, {無垢|むく}, {無常|むじょう}, {無謀|むぼう}, {無関心|むかんしん}
- Food/cooking cluster: {焼|や}きそば, {焼|や}き{魚|ざかな}, {煎茶|せんちゃ}, {煮干|にぼ}し, {点心|てんしん}, {炒|い}る, {煮立|にた}つ, {点|た}てる, {熟成|じゅくせい}
- Fire/light cluster: {灯籠|とうろう}, {灯|ともしび}, {火種|ひだね}, {火星|かせい}
- Multi-sense entries: {灯|ともしび} (2), {火種|ひだね} (2), {焦点|しょうてん} (2), {激戦|げきせん} (2), {激突|げきとつ} (2), {潮流|ちょうりゅう} (2), {濃密|のうみつ} (2), {無名|むめい} (2), {無垢|むく} (2), {煙幕|えんまく} (2)
- Cultural: {無常|むじょう} (Buddhist impermanence), {点|た}てる (tea ceremony), {灯籠|とうろう} (Obon lanterns), {煎茶|せんちゃ} (tea varieties)
- Kanji contrast: {替|か}える vs {変|か}える vs {代|か}える (replace vs change vs substitute)
- New kanji: 2,401 → 2,402 ({瀕|ひん})

Total entries: 13,454 → 13,484 (approximate)
Remaining candidates: 547 → 517 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
