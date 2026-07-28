# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-28
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

### 2026-07-28 (Routine v2: new-entries — 20 New Entries, IDs 30183–30202)
Created 20 general-tier entries. **All 8 "seen in entry" candidates were created**, draining that lane to zero again — every one of them was captured by yesterday's run from its own entries (30168–30182), so the §3 capture loop continues to close within a day. The seen-in eight: {未収金|みしゅうきん} (uncollected receivable), {販促費|はんそくひ} (sales promotion expenses), {上昇幅|じょうしょうはば} (extent of a rise), {入力端子|にゅうりょくたんし} (input terminal), {聴神経|ちょうしんけい} (auditory nerve), {死亡者数|しぼうしゃすう} (number of deaths), {一服|いっぷく}する (to take a short break; verb-suru, informal), {得|とく}をする (to come out ahead; expression). The other 12 are hand-picked standalone lexemes, since the non-seen candidate pool remains **heavily polluted** with corpus/OCR noise and transparent compounds — the top-of-list "oldest first" fallback is currently unusable, and a `[pattern]` observation was logged again this run: {打|う}つ{手|て} (move one can make / recourse), {国番号|くにばんごう} (country code), {試飲会|しいんかい} (drink tasting event), {来店客|らいてんきゃく} (store visitor), {柿|かき}の{種|たね} (kaki-no-tane rice cracker), {祝|いわ}い{膳|ぜん} (celebratory meal), {診療録|しんりょうろく} (medical record), {畜産物|ちくさんぶつ} (livestock products), {黒褐色|こっかっしょく} (dark brown), {電気工事士|でんきこうじし} (licensed electrician), {丸|まる}のこ (circular saw), {安全柵|あんぜんさく} (safety fence). Several entries close mirror pairs the dictionary already had: {未収金|みしゅうきん} ↔ {未払|みはら}い{金|きん} (30179), {入力端子|にゅうりょくたんし} ↔ {出力端子|しゅつりょくたんし} (30181), {上昇幅|じょうしょうはば} ↔ {下落幅|げらくはば} (30175), {聴神経|ちょうしんけい} ↔ {視神経|ししんけい} (30172), and {畜産物|ちくさんぶつ} joins {農産物|のうさんぶつ}/{水産物|すいさんぶつ}. Conjugation table added to the one suru-verb; **no new kanji**. 7 referenced-but-missing words added as candidates (C22580–C22586). §4 cross-model self-check on all 20 changed entries: **19 clean, 1 flagged — 0 applied, 1 rejected** (a `formality: formal` → `neutral` nit on {黒褐色|こっかっしょく}, rejected because the entry's own register description supports the written-register label and the parent {褐色|かっしょく} entry is tagged the same way). $0.0089.

- **Finance / business (5)**: {未収金|みしゅうきん}, {販促費|はんそくひ}, {上昇幅|じょうしょうはば}, {来店客|らいてんきゃく}, {得|とく}をする
- **Health / medical (3)**: {聴神経|ちょうしんけい}, {死亡者数|しぼうしゃすう}, {診療録|しんりょうろく}
- **Tools / technical (4)**: {入力端子|にゅうりょくたんし}, {電気工事士|でんきこうじし}, {丸|まる}のこ, {安全柵|あんぜんさく}
- **Food / culture (3)**: {柿|かき}の{種|たね}, {祝|いわ}い{膳|ぜん}, {試飲会|しいんかい}
- **Other (5)**: {一服|いっぷく}する, {打|う}つ{手|て}, {国番号|くにばんごう}, {畜産物|ちくさんぶつ}, {黒褐色|こっかっしょく}

### 2026-07-27 (Routine v2: new-entries — 18 New Entries, IDs 30165–30182)
Created 18 general-tier entries. **All 15 remaining "seen in entry" candidates were created**, draining that lane to zero again; 3 of the 18 came from that queue's own recent additions (C22557–C22567, cited from entries 30147–30163), so the §3 capture loop continues to close within a day. The seen-in fifteen: {成長率|せいちょうりつ} (growth rate), {最小値|さいしょうち} (minimum value), {平均値|へいきんち} (mean), {宣伝費|せんでんひ} (advertising expenses), {工作員|こうさくいん} (covert operative), {既存客|きぞんきゃく} (existing customer), {死者数|ししゃすう} (death toll), {視神経|ししんけい} (optic nerve), {南極大陸|なんきょくたいりく} (Antarctica), やり{切|き}る (to see through to the end; godan-ru), {下落幅|げらくはば} (extent of a decline), {偉|えら}そう (self-important; adjective-na), お{茶|ちゃ}する (to go for tea; verb-suru, informal), そこまで (that far / to that extent; two-sense expression), {未払|みはら}い{金|きん} (unpaid amount). The other 3 are hand-picked standalone lexemes, since the non-seen candidate pool remains **heavily polluted** with corpus/OCR noise: レントゲン{写真|しゃしん} (X-ray photograph), {出力端子|しゅつりょくたんし} (output terminal), {利益|りえき}を{得|え}る (to make a profit / to gain a benefit; two-sense expression). {最小値|さいしょうち}/{平均値|へいきんち} join the existing {最大値|さいだいち}, and {下落幅|げらくはば} extends the 率/幅 statistics family. Conjugation tables added to the godan verb and the suru-verb; **no new kanji**. 8 referenced-but-missing words added as candidates (C22572–C22579); 3 stale candidates removed (already entries). §4 self-check on all 18 changed entries: **accuracy pass clean — 0 flagged**; the furigana screener flagged 7, **all rejected** as one noise family — every source reading verified correct, and the flags trace to a prompt bug logged as a `[tooling]` observation (the screener's `followed by:` context is truncated mid-`{kanji|reading}` markup, and the model reads the truncation as an incomplete reading). $0.0101.

- **Statistics / finance (6)**: {成長率|せいちょうりつ}, {最小値|さいしょうち}, {平均値|へいきんち}, {死者数|ししゃすう}, {下落幅|げらくはば}, {未払|みはら}い{金|きん}
- **Business (3)**: {宣伝費|せんでんひ}, {既存客|きぞんきゃく}, {利益|りえき}を{得|え}る
- **Verbs / adjectives / expressions (4)**: やり{切|き}る, {偉|えら}そう, お{茶|ちゃ}する, そこまで
- **Other (5)**: {工作員|こうさくいん}, {視神経|ししんけい}, {南極大陸|なんきょくたいりく}, レントゲン{写真|しゃしん}, {出力端子|しゅつりょくたんし}

### 2026-07-27 (Routine v2: new-entries — 20 New Entries, IDs 30145–30164)
Created 20 general-tier entries. **All 13 "seen in entry" candidates were created**, draining that lane to zero — each one came from a previous run's own entries (30126–30144, plus 06646, 06648, 06654, 07441), so the §3 capture loop is still closing within a day or two. The seen-in thirteen: {私邸|してい} (private residence of an official), {手|て}さばき (deft handling), {下落率|げらくりつ} (rate of decline), {伸|の}び{率|りつ} (growth rate), {致死率|ちしりつ} (fatality rate), {捺印欄|なついんらん} (seal box on a form), {製品化|せいひんか} (commercialization; noun + verb-suru), {感染者数|かんせんしゃすう} (case count), {草|くさ}っ{原|ぱら} (grassy patch; informal), {急|せ}く (to feel rushed; godan-ku, the source of せっかち), {出|だ}し{切|き}る (to give everything one has; godan-ru), {迷走神経|めいそうしんけい} (vagus nerve), and the suffix 〜{後|ご} (after ~). The other 7 are hand-picked standalone lexemes, since the non-seen candidate pool remains **heavily polluted** — see the `[pattern]` observation logged this run: {最大値|さいだいち} (maximum value), {広告費|こうこくひ} (advertising expenses), {諜報員|ちょうほういん} (intelligence agent), {法人格|ほうじんかく} (legal personality), {南極圏|なんきょくけん} (Antarctic Circle), {新規客|しんききゃく} (new customer), {包装材|ほうそうざい} (packaging material). The three 率-compounds join yesterday's {上昇率|じょうしょうりつ} and {感染率|かんせんりつ}, and each cross-references the others, so that family is now internally connected. Conjugation tables added to the 2 godan verbs and the suru-verb noun; **no new kanji**. 11 referenced-but-missing words added as candidates (C22557–C22567). §4 cross-model self-check on all 20 changed entries: **clean — 20/20, 0 flagged, 0 applied, 0 rejected**. $0.0087.

- **Rates / statistics (5)**: {下落率|げらくりつ}, {伸|の}び{率|りつ}, {致死率|ちしりつ}, {感染者数|かんせんしゃすう}, {最大値|さいだいち}
- **Business / documents (5)**: {製品化|せいひんか}, {捺印欄|なついんらん}, {広告費|こうこくひ}, {法人格|ほうじんかく}, {新規客|しんききゃく}
- **Verbs / suffix (3)**: {急|せ}く (to feel rushed), {出|だ}し{切|き}る (to give one's all), 〜{後|ご} (after ~)
- **People / places / things (7)**: {私邸|してい}, {手|て}さばき, {草|くさ}っ{原|ぱら}, {迷走神経|めいそうしんけい}, {諜報員|ちょうほういん}, {南極圏|なんきょくけん}, {包装材|ほうそうざい}

### 2026-07-26 (Routine v2: new-entries — 20 New Entries, IDs 30125–30144)
Created 20 general-tier entries. **All 10 "seen in entry" candidates were created first**, draining that queue — and five of them ({商工会|しょうこうかい}, {公邸|こうてい}, {学習漢字|がくしゅうかんじ}, {生体認証|せいたいにんしょう}, {市松模様|いちまつもよう}) were captured by the previous day's new-entries run from its own entries, so the §3 capture loop is closing within a day. The seen-in ten: {商工会|しょうこうかい} (town/village society of commerce and industry), {公邸|こうてい} (official residence), {学習漢字|がくしゅうかんじ} (elementary-school kanji), {生体認証|せいたいにんしょう} (biometric authentication), {市松模様|いちまつもよう} (checkerboard pattern), {偲|しの}ぶ (to remember fondly; godan-bu, transitive), {兆|きざ}す (to show signs; godan-su, intransitive), {原|はら}っぱ (open field), {渡|わた}し{場|ば} (ferry landing), {手|て}つき (way one uses one's hands). The other 10 are hand-picked standalone lexemes, since the non-seen candidate pool stays **heavily polluted** (corpus/OCR noise and non-words such as 権使/些道/個尊/怒燥): {商品化|しょうひんか} (commercialization; noun + verb-suru), {不正直|ふしょうじき} (dishonest; adjective-na), {署名欄|しょめいらん} (signature field), {速達便|そくたつびん} (express mail), {無料券|むりょうけん} (free ticket), {集会場|しゅうかいじょう} (assembly hall), {梱包材|こんぽうざい} (packing material), {諸費用|しょひよう} (miscellaneous costs), {上昇率|じょうしょうりつ} (rate of increase), {感染率|かんせんりつ} (infection rate). Conjugation tables added to the 2 godan verbs and the suru-verb noun; **1 new kanji** assigned an ID — 偲 (02788_shi_shino_recollect). 9 referenced-but-missing words added as candidates ({私邸|してい}, {手|て}さばき, {下落率|げらくりつ}, {伸|の}び{率|りつ}, {致死率|ちしりつ}, {捺印欄|なついんらん}, {製品化|せいひんか}, {感染者数|かんせんしゃすう}, {草|くさ}っ{原|ぱら}). §4 cross-model self-check on all 20 changed entries: **19 clean, 1 flagged — 1 applied, 0 rejected** (removed the `business` semantic tag from {梱包材|こんぽうざい}, which denotes a material rather than a business concept). $0.0087.

- **Seen-in-entry (10)**: {商工会|しょうこうかい}, {公邸|こうてい}, {学習漢字|がくしゅうかんじ}, {生体認証|せいたいにんしょう}, {市松模様|いちまつもよう}, {偲|しの}ぶ, {兆|きざ}す, {原|はら}っぱ, {渡|わた}し{場|ば}, {手|て}つき
- **Business / documents (5)**: {商品化|しょうひんか}, {署名欄|しょめいらん}, {諸費用|しょひよう}, {梱包材|こんぽうざい}, {上昇率|じょうしょうりつ}
- **Daily life / other (5)**: {速達便|そくたつびん}, {無料券|むりょうけん}, {集会場|しゅうかいじょう}, {感染率|かんせんりつ}, {不正直|ふしょうじき}

### 2026-07-25 (Routine v2: new-entries — 20 New Entries, IDs 30105–30124)
Created 20 general-tier entries. Both **"seen in entry" candidates** were created first: {三毒|さんどく} (the three poisons, Buddhism; from entry 06623) and the suffix 〜{金|きん} (sum of money / fee / charge; from entry 06662, following the existing 〜{化|か} / 〜{感|かん} tilde-headword convention). The other 18 are hand-picked standalone lexemes, since the non-seen candidate pool remains **heavily polluted** — see the `[pattern]` observation logged this run. Clusters: institutions — {気象庁|きしょうちょう} (Japan Meteorological Agency), {商工会議所|しょうこうかいぎしょ} (chamber of commerce), {首相官邸|しゅしょうかんてい} (PM's office / the Kantei), {駆|か}け{込|こ}み{寺|でら} (place of last resort), {縁故|えんこ}{採用|さいよう} (hiring through connections); kanji-policy and grammar terms — {人名用漢字|じんめいようかんじ}, {教育漢字|きょういくかんじ}, {感動詞|かんどうし} (interjection); health — {脱水症状|だっすいしょうじょう} (dehydration), {出産予定日|しゅっさんよていび} (due date), {放射線科|ほうしゃせんか} (radiology dept.); business/tech — {異物混入|いぶつこんにゅう} (foreign-object contamination), {貸出|かしだし}{金利|きんり} (lending rate), {多要素認証|たようそにんしょう} (MFA), {浮動小数点|ふどうしょうすうてん} (floating point); maths and one textile term — {素因数|そいんすう} (prime factor), {立方根|りっぽうこん} (cube root), {格子縞|こうしじま} (check / plaid). No verbs or i-adjectives, so no conjugation tables; **no new kanji**. Two stale candidates removed as duplicates of existing entries (派出所 → 13284, 肘関節 → 29513); 5 referenced-but-missing words added as candidates ({商工会|しょうこうかい}, {公邸|こうてい}, {学習漢字|がくしゅうかんじ}, {生体認証|せいたいにんしょう}, {市松模様|いちまつもよう}). §4 cross-model self-check on all 20 changed entries: **18 clean, 2 flagged — 0 applied, 2 rejected** (an in-list `food` "too narrow" tag nit on {異物混入|いぶつこんにゅう}, rejected per the §A semantic-tag policy; and a prime-factor-multiplicity nit on a {素因数|そいんすう} example whose English faithfully mirrors the Japanese). $0.0087.

- **Institutions / society (5)**: {気象庁|きしょうちょう} (JMA), {商工会議所|しょうこうかいぎしょ} (chamber of commerce), {首相官邸|しゅしょうかんてい} (PM's office), {駆|か}け{込|こ}み{寺|でら} (place of refuge), {縁故|えんこ}{採用|さいよう} (nepotistic hiring)
- **Language / education (3)**: {人名用漢字|じんめいようかんじ} (name kanji), {教育漢字|きょういくかんじ} (elementary-school kanji), {感動詞|かんどうし} (interjection)
- **Health (3)**: {脱水症状|だっすいしょうじょう} (dehydration), {出産予定日|しゅっさんよていび} (due date), {放射線科|ほうしゃせんか} (radiology department)
- **Business / technology (4)**: {異物混入|いぶつこんにゅう} (foreign-object contamination), {貸出|かしだし}{金利|きんり} (lending rate), {多要素認証|たようそにんしょう} (MFA), {浮動小数点|ふどうしょうすうてん} (floating point)
- **Maths / other (5)**: {素因数|そいんすう} (prime factor), {立方根|りっぽうこん} (cube root), {格子縞|こうしじま} (check pattern), {三毒|さんどく} (the three poisons), 〜{金|きん} (fee; sum of money — suffix)
