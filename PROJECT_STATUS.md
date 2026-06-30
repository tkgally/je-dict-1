# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-06-16
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

### 2026-06-30 (Routine v2: new-entries — 12 New Entries, IDs 29581–29592)
Created 12 general-tier entries, all from the high-priority "seen in entry" pool — internal-completeness gaps referenced by existing entries 06329–06337 (a gardening/flowerpot cluster, a driving/tire cluster, and three encyclopedic terms cited from proverb entries). All were `noentry` or near-`noentry` inline-link targets, so each closes a self-reference. The non-seen candidate tail remains heavy corpus-harvest/OCR noise (些道, 個尊, 怒燥, 権使, アンパッサン misglossed "ice cream sundae"; potential/negated verb forms; bare counters), so no padding from the oldest queue — logged a `[pattern]` observation requesting a curator cleanup pass. Two new kanji assigned IDs (琵, 琶 from {琵琶湖|びわこ}); all 12 are single-sense nouns, no new verbs. §4 cross-model self-check on all 12 changed entries: **11 fully clean; 0 applied, 1 rejected** (29585 {空気圧|くうきあつ} flagged semantic `transportation`→`science`/`general`, an in-list narrowness nit rejected per the semantic-tag policy — the entry's explanation and all three examples are framed on tire pressure). $0.0052.

- **Gardening cluster (4)**: {鉢|はち} (bowl/pot/basin), {鉢皿|はちざら} (pot saucer), {培養土|ばいようど} (potting soil), {鉢底石|はちぞこいし} (drainage stones)
- **Driving cluster (4)**: {空気圧|くうきあつ} (air/tire pressure), スタッドレスタイヤ (studless winter tire), {踏|ふ}み{間違|まちが}え (pedal misapplication), {全開|ぜんかい} (fully open; full throttle)
- **Other (4)**: ハンドルネーム (online handle), {文|もん} (mon, old currency unit), {漢書|かんじょ} (Book of Han), {琵琶湖|びわこ} (Lake Biwa)

### 2026-06-29 (Routine v2: new-entries — 12 New Entries, IDs 29569–29580)
Created 12 general-tier entries: all 8 remaining "seen in entry" priority candidates (a children's-outdoor-play and gardening cluster referenced from existing entries 06323–06327) plus 4 hand-vetted standalone words. The non-seen candidate tail remains heavy corpus-harvest noise (misglosses and transparent compounds — e.g. 権使, 些道, 怒燥, 三千代 "three thousand yen note?"), so the 4 supplements were chosen individually for genuine dictionary-worthiness, not padded from the oldest queue. Conjugation table added to the one verb ({滑|すべ}り{降|お}りる); no new kanji. §4 cross-model self-check on all 12 changed entries: **12 CLEAN, 0 flagged**. $0.0052.

- **Seen-in-entry (8)**: {二重|にじゅう}{跳|と}び (double under, jump rope), {大|おお}{縄|なわ}{跳|と}び (group long-rope jumping), {滑|すべ}り{降|お}りる (to slide down; verb-ichidan), {泥|どろ}{団子|だんご} (mud ball), {剪定|せんてい}ばさみ (pruning shears), {植木|うえき}{屋|や} (gardener), シーソー (seesaw), ジャングルジム (jungle gym)
- **Standalone (4)**: スーパーボールすくい (superball scooping, festival game), バラ{科|か} (rose family / Rosaceae), ユリ{科|か} (lily family / Liliaceae), {足|そく}{関節|かんせつ} (ankle joint; medical, distinguished from 足首)

### 2026-06-29 (Routine v2: new-entries — 17 New Entries, IDs 29552–29568)
Created 17 general-tier entries entirely from the high-priority "seen in entry" pool (internal-completeness gaps referenced by existing entries 06311–06321). Dominated by the 12-sign Western zodiac set referenced from 06313 ({星座|せいざ}), plus an eclipse term and a barbershop/grooming/childhood-game cluster. Two homophone candidates dropped as duplicates of existing entries (髭 → 01332 ひげ; 髭そり → 22892 {髭剃|ひげそ}り). Two new kanji assigned IDs ({蝕|しょく}, {蠍|さそり}); no new verbs. §4 cross-model self-check on all 17 changed entries: **13 fully clean; 0 applied, 4 rejected** (3 zodiac signs flagged semantic `culture`→`science`/astronomy — model conflated the astrological sign with the constellation, and the horoscope-framed entries are correctly `culture`; 29567 {理容店|りようてん} flagged formality `formal`→`neutral`, but the entry's own register note confirms `formal`). $0.0074.

- **Zodiac signs (12)**: {牡羊座|おひつじざ} (Aries), {牡牛座|おうしざ} (Taurus), {双子座|ふたござ} (Gemini), {蟹座|かにざ} (Cancer), {獅子座|ししざ} (Leo), {乙女座|おとめざ} (Virgo), {天秤座|てんびんざ} (Libra), {蠍座|さそりざ} (Scorpio), {射手座|いてざ} (Sagittarius), {山羊座|やぎざ} (Capricorn), {水瓶座|みずがめざ} (Aquarius), {魚座|うおざ} (Pisces)
- **Other (5)**: {蝕|しょく} (eclipse; literary), トリートメント (hair treatment), {顔|かお}そり (face shaving), {理容店|りようてん} (barbershop; formal), {缶|かん}{蹴|け}り (kick the can)

### 2026-06-28 (Routine v2: new-entries — 20 New Entries, IDs 29532–29551)
Created 20 general-tier entries from the high-priority "seen in entry" pool (internal-completeness gaps referenced by existing entries 06304–06314). Four themed clusters — solar/lunar eclipses, night-sky objects, hand tools, and a business/energy set. §4 cross-model self-check on all 20 changed entries: **20 CLEAN, 0 flagged**. $0.0087. Conjugation table added to the one verb ({割|わ}り{引|び}く); no new kanji.

- **Eclipses (5)**: {皆既日食|かいきにっしょく} (total solar eclipse), {部分日食|ぶぶんにっしょく} (partial solar eclipse), {金環日食|きんかんにっしょく} (annular solar eclipse), {部分月食|ぶぶんげっしょく} (partial lunar eclipse), {半影月食|はんえいげっしょく} (penumbral lunar eclipse)
- **Sky objects (3)**: ブラッドムーン (blood moon), {北斗七星|ほくとしちせい} (Big Dipper), {南十字星|みなみじゅうじせい} (Southern Cross)
- **Tools (4)**: {工具箱|こうぐばこ} (toolbox), ニッパー (nippers), ラジオペンチ (needle-nose pliers), プライヤー (pliers)
- **Business / energy / other (8)**: {不渡|ふわた}り (dishonored check), {割|わ}り{引|び}く (to discount; verb-godan), {当座|とうざ} (the time being; current account), マネー (money), {省|しょう}エネルギー (energy conservation), クールビズ (Cool Biz), ウォームビズ (Warm Biz), {早見表|はやみひょう} (quick-reference chart)

### 2026-06-27 (Routine v2: new-entries — 15 New Entries, IDs 29517–29531)
Created 15 general-tier entries, all from the high-priority "seen in entry" pool (internal-completeness gaps referenced by existing entries 06294–06302, 29514). §4 cross-model self-check: **15 CLEAN, 0 flagged**. $0.0065.

- **Seen-in-entry (15)**: {巻積雲|けんせきうん} (cirrocumulus), {要注意|ようちゅうい} (requiring caution), {貸衣装|かしいしょう} (rental costume), {黒留袖|くろとめそで} (black formal kimono), {油紙|あぶらがみ} (oilpaper), {香道|こうどう} (way of incense), {仏事|ぶつじ} (Buddhist service), {仏前|ぶつぜん} (before the altar), {聞香|もんこう} (appreciating incense), てんかん (epilepsy), こむら{返|がえ}り (calf cramp), {電解質|でんかいしつ} (electrolyte), {胸痛|きょうつう} (chest pain), {今期|こんき} (this term), {生|う}む (to produce/generate; verb-godan, cross-ref {産|う}む)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
