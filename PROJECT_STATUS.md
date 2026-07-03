# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-02
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

### 2026-07-03 (Routine v2: new-entries — 13 New Entries, IDs 29642–29654)
Created 13 general-tier noun entries. The one remaining "seen in entry" candidate was created first ({規則遵守|きそくじゅんしゅ}, rule compliance, cited from 06379); the rest are genuinely real, useful vocabulary hand-picked from the noisy candidate tail — the oldest/non-seen candidates are dominated by corpus-harvest garbage (fabricated words, compositional compounds, wrong glosses), so only ~13 defensible entries could be responsibly sourced rather than padding to 20. Picks skew to loanwords and news vocabulary: business franchise pair (フランチャイザー/フランチャイジー), a missile-range set ({誘導|ゆうどう}/{短距離|たんきょり}/{長距離|ちょうきょり}ミサイル), and everyday loanwords (アクションゲーム, フルカラー, コンペティション, マイナーリーグ, ハンドセット, ディップソース, プレイメーカー). §4 cross-model self-check on all 13: **12 clean; 0 applied, 1 rejected** — rejected a tag flag on コンペティション (`leisure`→`action`; in-list narrowness nit and "action" is a worse fit for a contest noun). Logged a `[pattern]` observation requesting a curator restock/cleanup of the polluted candidate list. $0.0056.

- **Business (3)**: {規則遵守|きそくじゅんしゅ} (rule compliance), フランチャイザー (franchisor), フランチャイジー (franchisee)
- **Military/news (3)**: {誘導|ゆうどう}ミサイル (guided missile), {短距離|たんきょり}ミサイル (short-range missile), {長距離|ちょうきょり}ミサイル (long-range missile)
- **Everyday loanwords (7)**: アクションゲーム (action game), フルカラー (full color), コンペティション (competition; contest), マイナーリーグ (minor league), ハンドセット (handset), ディップソース (dipping sauce; dip), プレイメーカー (playmaker)

### 2026-07-02 (Routine v2: new-entries — 12 New Entries, IDs 29630–29641)
Created 12 general-tier entries, all from the high-priority "seen in entry" pool — internal-completeness gaps referenced by existing entries (a photography cluster from 06362, geology terms, an optometry/vision-surgery cluster from 06370/06366, and single terms cited from the {正史|せいし}, {威圧的|いあつてき}, and {大器晩成|たいきばんせい} entries). This **cleared the entire remaining seen-in-entry queue** (12 candidates). The non-seen candidate tail remains heavy corpus-harvest noise ({小鼻|こばな}を{挟|はさ}む, 権使, がまま, 些道, 個尊, 怒燥, compositional phrases, bare counters), so no padding from the oldest queue. Conjugation tables added to the 3 new suru-verbs ({堆積|たいせき}, {褶曲|しゅうきょく}, {検眼|けんがん}); one new kanji assigned an ID ({褶|しゅう} from 褶曲 → 02780). §4 cross-model self-check on all 12 changed entries: **10 fully clean; 2 applied, 0 rejected** — applied 29634 ネガティブ semantic `technology` removed (core sense is attitude; kept `evaluation`) and 29640 {強圧的|きょうあつてき} semantic `personality`→`descriptive` (matches near-synonym {威圧的|いあつてき} and the -teki adjective convention; the model's `action` suggestion was not used). $0.0052.

- **Photography (2)**: {現像液|げんぞうえき} (developer / developing solution), ネガティブ (negative — attitude; photographic negative)
- **Geology (2)**: {堆積|たいせき} (deposition; sedimentation; suru), {褶曲|しゅうきょく} (geological fold; suru)
- **Vision (2)**: {検眼|けんがん} (eye examination; suru), {屈折矯正手術|くっせつきょうせいしゅじゅつ} (refractive surgery)
- **Other (6)**: {肌感覚|はだかんかく} (gut feeling; intuitive sense), {野史|やし} (unofficial history), {使用料|しようりょう} (usage fee), ロイヤリティ (royalty; licensing fee), {強圧的|きょうあつてき} (coercive; high-handed), {大器|たいき} (person of great talent)

### 2026-07-01 (Routine v2: new-entries — 17 New Entries, IDs 29613–29629)
Created 17 general-tier entries: all 7 remaining "seen in entry" priority candidates plus 10 hand-vetted standalone words. The non-seen candidate tail remains heavy corpus-harvest noise (compositional phrases, bare counters/numbers/dates, typos, dialect fragments), so the 10 supplements were each chosen for genuine dictionary-worthiness rather than padded from the oldest queue. Conjugation table added to the one new verb ({イラつく}); no new kanji. §4 cross-model self-check on all 17 changed entries: **14 fully clean; 1 applied, 2 rejected** — applied 29625 {皮膚感覚|ひふかんかく} `body-part`→removed (a sensation/faculty, not anatomy; kept `cognition`); rejected 29616 {楕円形|だえんけい} `general`→`size` (no "shape" tag exists; `size` is wrong, `general` is the correct fallback) and 29622 {神曲|しんきょく} formality `informal`→`slang` (`slang` is not a valid formality enum value). $0.0073. Captured 3 referenced-but-missing words as candidates ({肌感覚|はだかんかく}, {堆積|たいせき}, {野史|やし}).

- **Seen-in-entry (7)**: {年少|ねんしょう} (young; junior in age; antonym of 年長), {正史|せいし} (official dynastic history), {イラつく} (to get irritated; verb-godan, slang), {楕円形|だえんけい} (ellipse; oval shape), {円軌道|えんきどう} (circular orbit), {楕円軌道|だえんきどう} (elliptical orbit), {静止軌道|せいしきどう} (geostationary orbit)
- **Standalone (10)**: ナンパ{師|し} (pick-up artist), {非|ひ}リア{充|じゅう} (person without a fulfilling offline life), {神曲|しんきょく} (masterpiece song; slang), コードリール (cord reel), カニ{缶|かん} (canned crab), {皮膚感覚|ひふかんかく} (cutaneous sensation; intuitive feel), {侵食作用|しんしょくさよう} (erosion), {風化作用|ふうかさよう} (weathering), トナーカートリッジ (toner cartridge), ピアス{穴|あな} (piercing hole)

### 2026-07-01 (Routine v2: new-entries — 20 New Entries, IDs 29593–29612)
Created 20 general-tier entries: all 8 remaining "seen in entry" priority candidates plus 12 hand-vetted standalone words. The non-seen candidate tail remains heavy corpus-harvest noise (compositional phrases, bare counters/numbers, typos, dialect fragments), so the 12 supplements were each chosen for genuine dictionary-worthiness rather than padded from the oldest queue — logged a `[pattern]` observation. Also added the reciprocal antonym cross-ref to the pre-existing {全開|ぜんかい} (29588) so the 全開↔全閉 pair is symmetric. Conjugation tables added to the 2 new verbs and 3 suru-nouns; no new kanji. §4 cross-model self-check on all 21 changed entries: **20 fully clean; 0 applied, 1 rejected** (29593 {腐葉土|ふようど} flagged semantic `daily-life`→`plant-general`, an in-list narrowness nit rejected — leaf mold is a soil product, not a plant, and `daily-life` mirrors sibling {培養土|ばいようど}). $0.0091. Captured 2 referenced-but-missing words as candidates ({年少|ねんしょう}, {正史|せいし}).

- **Seen-in-entry (8)**: {腐葉土|ふようど} (leaf mold), {軽石|かるいし} (pumice), {全閉|ぜんぺい} (fully closed; antonym of 全開), {史記|しき} (Records of the Grand Historian), {間欠泉|かんけつせん} (geyser), {怒|おこ}り{出|だ}す (to flare up; verb-godan), {邪気|じゃき} (malice; evil spirit), {聞|き}き{分|わ}ける (to distinguish by ear; verb-ichidan)
- **Standalone (12)**: {年長|ねんちょう} (senior in age), {湿度計|しつどけい} (hygrometer), {非通知|ひつうち} (withheld number), {切削|せっさく} (cutting/machining; suru), {旋削|せんさく} (lathe turning; suru), {絹布|けんぷ} (silk cloth), {尾根筋|おねすじ} (ridge line), {遊女屋|ゆうじょや} (brothel; historical), {係助詞|かかりじょし} (binding particle), {炭化物|たんかぶつ} (carbide), {情報提供|じょうほうていきょう} (provision of information; suru), {黄緑色|きみどりいろ} (yellow-green)

### 2026-06-30 (Routine v2: new-entries — 12 New Entries, IDs 29581–29592)
Created 12 general-tier entries, all from the high-priority "seen in entry" pool — internal-completeness gaps referenced by existing entries 06329–06337 (a gardening/flowerpot cluster, a driving/tire cluster, and three encyclopedic terms cited from proverb entries). All were `noentry` or near-`noentry` inline-link targets, so each closes a self-reference. The non-seen candidate tail remains heavy corpus-harvest/OCR noise (些道, 個尊, 怒燥, 権使, アンパッサン misglossed "ice cream sundae"; potential/negated verb forms; bare counters), so no padding from the oldest queue — logged a `[pattern]` observation requesting a curator cleanup pass. Two new kanji assigned IDs (琵, 琶 from {琵琶湖|びわこ}); all 12 are single-sense nouns, no new verbs. §4 cross-model self-check on all 12 changed entries: **11 fully clean; 0 applied, 1 rejected** (29585 {空気圧|くうきあつ} flagged semantic `transportation`→`science`/`general`, an in-list narrowness nit rejected per the semantic-tag policy — the entry's explanation and all three examples are framed on tire pressure). $0.0052.

- **Gardening cluster (4)**: {鉢|はち} (bowl/pot/basin), {鉢皿|はちざら} (pot saucer), {培養土|ばいようど} (potting soil), {鉢底石|はちぞこいし} (drainage stones)
- **Driving cluster (4)**: {空気圧|くうきあつ} (air/tire pressure), スタッドレスタイヤ (studless winter tire), {踏|ふ}み{間違|まちが}え (pedal misapplication), {全開|ぜんかい} (fully open; full throttle)
- **Other (4)**: ハンドルネーム (online handle), {文|もん} (mon, old currency unit), {漢書|かんじょ} (Book of Han), {琵琶湖|びわこ} (Lake Biwa)

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
