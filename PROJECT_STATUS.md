# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-25
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
| Total entries | ~13,604 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,805 (open) |
| Candidate words | ~6,165 |
| Cross-references | ~3,400 |
| Example sentences | ~46,900 |
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

### 2026-02-25 (Vocabulary Expansion - 30 New Entries, Session 325)
Added 30 new dictionary entries (IDs 13519-13548) from candidate_words.json:

- **Food noun (1)**: {甘酒|あまざけ} (amazake)
- **I-adjective (1)**: {甚|はなは}だしい (extreme, excessive)
- **Godan verbs (2)**: {生|い}き{残|のこ}る (to survive), {生|う}まれ{変|か}わる (to be reborn)
- **生- cluster (4)**: {生業|なりわい} (livelihood), {生計|せいけい} (living), {生息|せいそく} (inhabiting), {生態|せいたい} (ecology)
- **Na-adjectives (2)**: {無作法|ぶさほう} (ill-mannered), {無様|ぶざま} (unsightly)
- **王- cluster (3)**: {王宮|おうきゅう} (royal palace), {王者|おうじゃ} (king/champion), {王家|おうけ} (royal family)
- **特- cluster (2)**: {特製|とくせい} (specially made), {特質|とくしつ} (characteristic)
- **Noun/suru verbs (3)**: {献上|けんじょう} (offering), {現存|げんそん} (extant), {混濁|こんだく} (turbidity)
- **Other nouns (12)**: {甥|おい} (nephew), {用品|ようひん} (supplies), {田畑|たはた} (farmland), {深紅|しんく} (crimson), {火消|ひけ}し (firefighter/damage control), {物欲|ぶつよく} (materialism), {狭義|きょうぎ} (narrow sense), {産声|うぶごえ} (first cry), {産物|さんぶつ} (product), {用心棒|ようじんぼう} (bodyguard), {用法|ようほう} (usage), {瓢箪|ひょうたん} (gourd)

Notable features:
- 生- cluster: 4 entries covering livelihood, living, inhabiting, and ecology
- 王- cluster: 3 entries covering palaces, champions, and royal families
- Multi-sense entries: {生|い}き{残|のこ}る (2: physical + competitive survival), {生|う}まれ{変|か}わる (2: reincarnation + transformation), {火消|ひけ}し (2: historical firefighter + damage control), {産声|うぶごえ} (2: literal first cry + figurative founding), {産物|さんぶつ} (2: physical product + result of circumstances), {王者|おうじゃ} (2: king + champion), {用心棒|ようじんぼう} (2: bodyguard + door bar), {混濁|こんだく} (2: turbidity + confusion)
- Cultural: {甘酒|あまざけ} (New Year's shrine drink), {瓢箪|ひょうたん} (Hideyoshi's emblem, proverb), {火消|ひけ}し (Edo firefighters), {献上|けんじょう} (imperial offerings), {用心棒|ようじんぼう} (Kurosawa film)
- New kanji: 2,410 → 2,411 ({甥|せい})

Total entries: 13,574 → 13,604 (approximate)
Remaining candidates: 6,195 → 6,165 (30 removed)

### 2026-02-25 (Vocabulary Expansion - 30 New Entries, Session 324)
Added 30 new dictionary entries (IDs 13489-13518) from candidate_words.json:

- **Food noun (1)**: {焼売|しゅうまい} (shumai)
- **Na-adjectives (4)**: {猛烈|もうれつ} (fierce), {率直|そっちょく} (frank), {無造作|むぞうさ} (casual/careless), {無差別|むさべつ} (indiscriminate)
- **I-adjective (1)**: {狭苦|せまくる}しい (cramped)
- **特- cluster (4)**: {特権|とっけん} (privilege), {特例|とくれい} (special case), {特筆|とくひつ} (special mention), {特性|とくせい} (characteristic)
- **現- cluster (3)**: {現地|げんち} (local/on-site), {現行|げんこう} (current/in force), {現職|げんしょく} (incumbent)
- **王- cluster (2)**: {王道|おうどう} (classic approach/royal road), {王朝|おうちょう} (dynasty)
- **Noun/suru verbs (6)**: {独占|どくせん} (monopoly), {猶予|ゆうよ} (postponement), {献金|けんきん} (donation), {牽引|けんいん} (towing/leading), {狩猟|しゅりょう} (hunting), {爆破|ばくは} (blasting)
- **Verb (1)**: {燃|も}え{上|あ}がる (to flare up, godan intransitive)
- **Other nouns (8)**: {狭間|はざま} (gap/between), {片腕|かたうで} (one arm/right-hand man), {灯火|ともしび} (lamplight), {減益|げんえき} (profit decline), {漉|こ}す (to strain), {熊手|くまで} (rake/lucky charm), {獅子舞|ししまい} (lion dance), {物体|ぶったい} (object)

Notable features:
- 特- cluster: 4 entries covering rights, exceptions, noteworthy mentions, and properties
- 現- cluster: 3 entries covering location, laws, and positions
- 王- cluster: 2 entries covering mainstream/classic and dynasty
- Multi-sense entries: {独占|どくせん} (2: monopoly + exclusive possession), {牽引|けんいん} (2: towing + leading), {片腕|かたうで} (2: one arm + right-hand man), {王道|おうどう} (2: classic + royal road), {燃|も}え{上|あ}がる (2: flare up + passion), {現職|げんしょく} (2: incumbent + current position), {熊手|くまで} (2: rake + lucky charm)
- Cultural: {獅子舞|ししまい} (lion dance traditions), {熊手|くまで} (Tori-no-Ichi festival), {王朝|おうちょう} (Heian court culture)
- Legal/business: {猶予|ゆうよ} (suspended sentence), {献金|けんきん} (political donations), {特権|とっけん} (diplomatic immunity), {減益|げんえき} (earnings reports)
- New kanji: 2,405 → 2,410 ({漉|ろく}, {烈|れつ}, {牽|けん}, {猟|りょう}, {猶|ゆう})

Total entries: 13,544 → 13,574 (approximate)
Remaining candidates: 6,225 → 6,195 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
