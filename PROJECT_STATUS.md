# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-21
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
| Total entries | ~12,605 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,806 (open) |
| Candidate words | ~525 |
| Cross-references | ~3,380 |
| Example sentences | ~44,800 |
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

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 292)
Added 30 new dictionary entries (IDs 12520-12549) from candidate_words.json:

- **Na-adjectives (2)**: {強固|きょうこ} (firm/solid), {強硬|きょうこう} (hardline/unyielding)
- **I-adjective (1)**: {後|うし}ろめたい (feeling guilty/uneasy)
- **Godan verbs (2)**: {彩|いろど}る (to color/decorate), {建|た}つ (to be built)
- **Nouns - geography/nature (3)**: {山岳|さんがく} (mountains), {山村|さんそん} (mountain village), {山地|さんち} (mountainous area — replaced with {広域|こういき})
- **Nouns - history/culture (4)**: {幕末|ばくまつ} (end of Edo period), {家元|いえもと} (grand master of traditional art), {宮廷|きゅうてい} (imperial court), {屋号|やごう} (trade name/kabuki stage name)
- **Nouns - society/governance (4)**: {弱者|じゃくしゃ} (the weak), {当局|とうきょく} (the authorities), {年功序列|ねんこうじょれつ} (seniority system), {廃校|はいこう} (school closure)
- **Nouns - food/nature (2)**: {小松菜|こまつな} (komatsuna), {山賊|さんぞく} (mountain bandit)
- **Nouns - abstract/descriptive (5)**: {巨体|きょたい} (huge physique), {序章|じょしょう} (prologue), {彷彿|ほうふつ} (reminiscent), {当|あ}て{字|じ} (ateji), {座談会|ざだんかい} (round-table discussion)
- **Nouns - arts/theater (1)**: {小道具|こどうぐ} (props)
- **Noun/suru verbs (6)**: {大量生産|たいりょうせいさん} (mass production), {定住|ていじゅう} (permanent residence), {強要|きょうよう} (coercion), {形成|けいせい} (formation), {待望|たいぼう} (long-awaited), {征服|せいふく} (conquest)

Notable features:
- Multi-sense entries: {小道具|こどうぐ} (theater props/small tools), {屋号|やごう} (shop name/kabuki stage name), {彩|いろど}る (color/embellish), {征服|せいふく} (military conquest/figurative mastery)
- Cultural context: {家元|いえもと} (iemoto system), {幕末|ばくまつ} (Bakumatsu era), {屋号|やごう} (kabuki calling names), {年功序列|ねんこうじょれつ} (Japanese employment), {山賊|さんぞく} (sanzoku-yaki dish), {廃校|はいこう} (rural repurposing trend)
- Diverse word types: adjectives (na/i), godan verbs, suru verbs, formal nouns, cultural terms
- New kanji: 2,361 → 2,366 ({岳|がく}, {廷|てい}, {彷|ほう}, {彿|ふつ}, {征|せい})

Total entries: 12,575 → 12,605
Remaining candidates: 555 → 525 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 291)
Added 30 new dictionary entries (IDs 12490-12519) from candidate_words.json:

- **Adverbs (3)**: {引|ひ}き{続|つづ}き (continuously/subsequently), {当初|とうしょ} (initially), {後日|ごじつ} (another day)
- **Na-adjectives (3)**: {小規模|しょうきぼ} (small-scale), {必須|ひっす} (essential/mandatory), {強欲|ごうよく} (greedy/avaricious)
- **I-adjective (1)**: {心地|ここち}よい (comfortable/pleasant)
- **Godan verbs (1)**: {微睡|まどろ}む (to doze/slumber)
- **Ichidan verb (1)**: {張|は}りつめる (to be taut/tense)
- **Nouns - occupation (2)**: {庭師|にわし} (gardener), {家政婦|かせいふ} (housekeeper)
- **Nouns - social/political (2)**: {少数派|しょうすうは} (minority group), {当事者|とうじしゃ} (person concerned)
- **Nouns - abstract/formal (6)**: {弱点|じゃくてん} (weak point), {強み|つよみ} (strength/forte), {形見|かたみ} (keepsake/memento), {彩|いろど}り (coloring/variety), {従来|じゅうらい} (conventional), {待遇|たいぐう} (treatment/conditions)
- **Nouns - time/period (2)**: {幼少|ようしょう} (childhood), {後味|あとあじ} (aftertaste)
- **Nouns - other (2)**: {幕|まく} (curtain/act), {弾丸|だんがん} (bullet)
- **Noun/suru verbs (7)**: {強制|きょうせい} (compulsion), {強奪|ごうだつ} (robbery), {後押|あとお}し (support/backing), {復讐|ふくしゅう} (revenge), {寵愛|ちょうあい} (favor/doting), {延焼|えんしょう} (fire spread), {待遇|たいぐう} (treatment)

Notable features:
- Multi-sense entries: {張|は}りつめる (taut/tense), {彩|いろど}り (coloring/variety), {後味|あとあじ} (literal/figurative aftertaste), {幕|まく} (curtain/act), {待遇|たいぐう} (treatment/compensation), {引|ひ}き{続|つづ}き (continuously/subsequently), {従来|じゅうらい} (conventional/up to now)
- Cultural context: {庭師|にわし} (traditional Japanese garden craft), {幕|まく} (kabuki theater/Edo period compounds), {形見|かたみ} ({形見|かたみ}{分|わ}け custom), {家政婦|かせいふ} (agency-based services)
- Diverse word types: adjectives, verbs, adverbs, suru verbs, formal nouns
- New kanji: 2,359 → 2,361 ({寵|ちょう}, {讐|しゅう})

Total entries: 12,545 → 12,575
Remaining candidates: 585 → 555 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 290)
Added 30 new dictionary entries (IDs 12460-12489) from candidate_words.json:

- **Na-adjectives (3)**: {希薄|きはく} (thin/tenuous), {平坦|へいたん} (flat/uneventful), {広範|こうはん} (wide-ranging)
- **Na-adjective/noun (1)**: {廉価|れんか} (low-priced/inexpensive)
- **Godan verbs (2)**: {弄|もてあそ}ぶ (to toy with/fiddle with), {引|ひ}き{渡|わた}す (to hand over/extradite)
- **Nouns - government/politics (3)**: {安保|あんぽ} (security treaty), {官庁|かんちょう} (government office), {市長|しちょう} (mayor)
- **Nouns - geography/place (3)**: {山麓|さんろく} (foot of mountain), {市街|しがい} (city streets), {店頭|てんとう} (storefront)
- **Nouns - food/culture (2)**: {寒天|かんてん} (agar), {巻物|まきもの} (scroll/rolled sushi)
- **Nouns - business (2)**: {店舗|てんぽ} (shop - formal), {廃棄|はいき} (disposal)
- **Nouns - abstract/formal (5)**: {定説|ていせつ} (established theory), {実体|じったい} (substance/true form), {席巻|せっけん} (sweeping over), {庇護|ひご} (protection/asylum), {廃止|はいし} (abolition)
- **Nouns - time (2)**: {年明|としあ}け (beginning of new year), {年越|としこ}し (New Year's Eve)
- **Nouns - people/education (3)**: {幼児|ようじ} (infant/toddler), {少人数|しょうにんずう} (small group), {底辺|ていへん} (base/bottom of society)
- **Nouns - other (3)**: {小型|こがた} (small-sized), {小文字|こもじ} (lowercase/small kana), {差|さ}し{金|がね} (instigation)
- **Noun/suru verb (1)**: {延命|えんめい} (life extension)

Notable features:
- Multi-sense entries: {希薄|きはく} (diluted/weak), {平坦|へいたん} (flat terrain/smooth path), {小文字|こもじ} (lowercase/small kana), {巻物|まきもの} (scroll/rolled sushi), {弄|もてあそ}ぶ (toy with emotions/fiddle with), {引|ひ}き{渡|わた}す (deliver property/extradite), {底辺|ていへん} (triangle base/bottom of society)
- Cultural context: {安保|あんぽ} (Anpo protests of 1960), {年越|としこ}し (toshikoshi soba tradition), {寒天|かんてん} (wagashi ingredient), {山麓|さんろく} (literary/travel writing)
- Diverse word types: na-adjectives, godan verbs, suru verbs, formal nouns, cultural terms
- New kanji: 2,356 → 2,359 ({坦|たん}, {庁|ちょう}, {廉|れん})

Total entries: 12,515 → 12,545
Remaining candidates: 615 → 585 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 289)
Added 30 new dictionary entries (IDs 12430-12459) from candidate_words.json:

- **I-adjective (1)**: {小難|こむずか}しい (somewhat difficult/nitpicky)
- **Na-adjectives (2)**: {希少|きしょう} (rare/scarce), {平穏|へいおん} (peaceful/tranquil)
- **Godan verbs (3)**: {引|ひ}っかかる (to get caught/be tricked/bother), {引|ひ}き{継|つ}ぐ (to take over/inherit), {引|ひ}き{裂|さ}く (to tear apart/separate)
- **Nouns - measurement/quantity (3)**: {小|こ}さじ (teaspoon), {少量|しょうりょう} (small amount), {度合|どあ}い (degree/extent)
- **Nouns - geography/place (3)**: {山奥|やまおく} (deep in mountains), {家並|いえな}み (row of houses), {庭園|ていえん} (formal garden)
- **Nouns - history/culture (3)**: {幕府|ばくふ} (shogunate), {干支|えと} (Chinese zodiac), {年末年始|ねんまつねんし} (year-end/New Year period)
- **Nouns - business/society (4)**: {属性|ぞくせい} (attribute/property), {対価|たいか} (compensation), {店主|てんしゅ} (shop owner), {干渉|かんしょう} (interference)
- **Nouns - abstract/descriptive (5)**: {巨人|きょじん} (giant/great figure), {寒気|かんき} (cold air), {廃墟|はいきょ} (ruins), {引|ひ}き{金|がね} (trigger), {序盤|じょばん} (opening phase)
- **Noun/suru verbs (4)**: {工作|こうさく} (crafting/scheming), {巣|す}ごもり (staying home), {小出|こだ}し (doling out), {尻込|しりご}み (flinching)
- **Noun/suffix (1)**: {層|そう} (layer/demographic segment)

Notable features:
- Multi-sense entries: {小難|こむずか}しい (complicated/fussy), {巨人|きょじん} (giant/titan), {工作|こうさく} (crafts/scheming), {引|ひ}き{金|がね} (gun trigger/catalyst), {引|ひ}っかかる (3 senses: caught/tricked/bother), {引|ひ}き{裂|さ}く (tear/separate), {層|そう} (layer/demographic)
- Cultural context: {幕府|ばくふ} (three shogunates), {干支|えと} (twelve zodiac animals), {年末年始|ねんまつねんし} (holiday customs), {巣|す}ごもり (COVID-era buzzword), {庭園|ていえん} (Japanese garden types)
- Diverse word types: verbs, adjectives, nouns, suru verbs, suffix
- New kanji: 2,355 → 2,356 ({墟|きょ})

Total entries: 12,485 → 12,515
Remaining candidates: 483 → 453 (30 removed)

### 2026-02-21 (Vocabulary Expansion - 30 New Entries, Session 288)
Added 30 new dictionary entries (IDs 12400-12429) from candidate_words.json:

- **Nouns - abstract/formal (4)**: {差異|さい} (difference/discrepancy), {山積|さんせき} (accumulation of problems), {対比|たいひ} (contrast/comparison), {巨額|きょがく} (enormous sum)
- **Nouns - culture/religion (4)**: {山車|だし} (festival float), {巫女|みこ} (shrine maiden), {師匠|ししょう} (master/teacher), {帝国|ていこく} (empire)
- **Nouns - food (3)**: {山菜|さんさい} (wild mountain vegetables), {山椒|さんしょう} (Japanese pepper), {干物|ひもの} (dried fish)
- **Nouns - geography/places (2)**: {山道|やまみち} (mountain path), {工房|こうぼう} (workshop/studio)
- **Nouns - daily life/society (5)**: {巷|ちまた} (the streets/the public), {巻|ま}き{寿司|ずし} (sushi roll), {工程|こうてい} (process/procedure), {庶民|しょみん} (common people), {市販|しはん} (commercially available)
- **Nouns - travel/lifestyle (2)**: {帰省|きせい} (returning to hometown), {幼馴染|おさななじみ} (childhood friend)
- **Nouns - other (3)**: {対話|たいわ} (dialogue), {展示|てんじ} (exhibition), {巡回|じゅんかい} (patrol/tour)
- **Na-adjective (1)**: {平凡|へいぼん} (ordinary/commonplace)
- **I-adjective (1)**: {小高|こだか}い (slightly elevated)
- **Ichidan verbs (2)**: {廃|すた}れる (to fall into disuse), {帯|お}びる (to wear/be tinged with)
- **Godan verb (1)**: {巡|めぐ}らす (to encircle/to ponder)
- **Suru verb (1)**: {属|ぞく}する (to belong to)
- **Noun/suru verbs (1)**: {幻|まぼろし} (illusion/phantom/legendary)

Notable features:
- Multi-sense entries: {巡|めぐ}らす (encircle/ponder), {帯|お}びる (wear/be tinged with), {幻|まぼろし} (illusion/legendary rarity)
- Cultural context: {山車|だし} (festival floats at Gion and Takayama), {巫女|みこ} (shrine maiden traditions), {帰省|きせい} (homecoming rush), {山椒|さんしょう} (proverb about small but pungent)
- Similar word comparisons: {差異|さい} vs {違|ちが}い; {対比|たいひ} vs {比較|ひかく}; {巷|ちまた} journalistic usage; {工房|こうぼう} vs {工場|こうじょう}
- New kanji: 2,350 → 2,355 ({匠|しょう}, {巫|ふ}, {巷|こう}, {帝|てい}, {庶|しょ})

Total entries: 12,455 → 12,485
Remaining candidates: 513 → 483 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
