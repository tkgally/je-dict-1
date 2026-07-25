# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-25
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

### 2026-07-25 (Routine v2: new-entries — 20 New Entries, IDs 30105–30124)
Created 20 general-tier entries. Both **"seen in entry" candidates** were created first: {三毒|さんどく} (the three poisons, Buddhism; from entry 06623) and the suffix 〜{金|きん} (sum of money / fee / charge; from entry 06662, following the existing 〜{化|か} / 〜{感|かん} tilde-headword convention). The other 18 are hand-picked standalone lexemes, since the non-seen candidate pool remains **heavily polluted** — see the `[pattern]` observation logged this run. Clusters: institutions — {気象庁|きしょうちょう} (Japan Meteorological Agency), {商工会議所|しょうこうかいぎしょ} (chamber of commerce), {首相官邸|しゅしょうかんてい} (PM's office / the Kantei), {駆|か}け{込|こ}み{寺|でら} (place of last resort), {縁故|えんこ}{採用|さいよう} (hiring through connections); kanji-policy and grammar terms — {人名用漢字|じんめいようかんじ}, {教育漢字|きょういくかんじ}, {感動詞|かんどうし} (interjection); health — {脱水症状|だっすいしょうじょう} (dehydration), {出産予定日|しゅっさんよていび} (due date), {放射線科|ほうしゃせんか} (radiology dept.); business/tech — {異物混入|いぶつこんにゅう} (foreign-object contamination), {貸出|かしだし}{金利|きんり} (lending rate), {多要素認証|たようそにんしょう} (MFA), {浮動小数点|ふどうしょうすうてん} (floating point); maths and one textile term — {素因数|そいんすう} (prime factor), {立方根|りっぽうこん} (cube root), {格子縞|こうしじま} (check / plaid). No verbs or i-adjectives, so no conjugation tables; **no new kanji**. Two stale candidates removed as duplicates of existing entries (派出所 → 13284, 肘関節 → 29513); 5 referenced-but-missing words added as candidates ({商工会|しょうこうかい}, {公邸|こうてい}, {学習漢字|がくしゅうかんじ}, {生体認証|せいたいにんしょう}, {市松模様|いちまつもよう}). §4 cross-model self-check on all 20 changed entries: **18 clean, 2 flagged — 0 applied, 2 rejected** (an in-list `food` "too narrow" tag nit on {異物混入|いぶつこんにゅう}, rejected per the §A semantic-tag policy; and a prime-factor-multiplicity nit on a {素因数|そいんすう} example whose English faithfully mirrors the Japanese). $0.0087.

- **Institutions / society (5)**: {気象庁|きしょうちょう} (JMA), {商工会議所|しょうこうかいぎしょ} (chamber of commerce), {首相官邸|しゅしょうかんてい} (PM's office), {駆|か}け{込|こ}み{寺|でら} (place of refuge), {縁故|えんこ}{採用|さいよう} (nepotistic hiring)
- **Language / education (3)**: {人名用漢字|じんめいようかんじ} (name kanji), {教育漢字|きょういくかんじ} (elementary-school kanji), {感動詞|かんどうし} (interjection)
- **Health (3)**: {脱水症状|だっすいしょうじょう} (dehydration), {出産予定日|しゅっさんよていび} (due date), {放射線科|ほうしゃせんか} (radiology department)
- **Business / technology (4)**: {異物混入|いぶつこんにゅう} (foreign-object contamination), {貸出|かしだし}{金利|きんり} (lending rate), {多要素認証|たようそにんしょう} (MFA), {浮動小数点|ふどうしょうすうてん} (floating point)
- **Maths / other (5)**: {素因数|そいんすう} (prime factor), {立方根|りっぽうこん} (cube root), {格子縞|こうしじま} (check pattern), {三毒|さんどく} (the three poisons), 〜{金|きん} (fee; sum of money — suffix)

### 2026-07-25 (Routine v2: new-entries — 15 New Entries, IDs 30090–30104)
Created 15 general-tier entries. The **3 "seen in entry" candidates** were adjudicated first: {引|ひ}き{渡|わた}し (handover / delivery / extradition; from entry 06618) was created, while the other two were **variant-reading near-duplicates** and were dropped with their candidates removed — 雪ぐ/すすぐ duplicates the existing 30089 雪ぐ/そそぐ (source 06614 actually uses そそぐ), and 裏面/うらめん duplicates 18245 裏面/りめん. The remaining 12 are hand-picked standalone lexemes, since the non-seen candidate pool stays **heavily polluted** (corpus/OCR noise, number/counter phrases, transparent compounds). The batch: かけ{離|はな}れる (to differ greatly; verb-ichidan), {薬用|やくよう} (medicinal), {養豚|ようとん} (pig farming), {堕胎|だたい} (abortion; verb-suru), {甘柿|あまがき} (sweet persimmon), {柿色|かきいろ} (persimmon color), {音圧|おんあつ} (sound pressure), {広縁|ひろえん} (wide veranda), {局番|きょくばん} (telephone exchange number), {路側|ろそく} (roadside), {骨材|こつざい} (aggregate), {受贈|じゅぞう} (receiving a donation; verb-suru), {斜角|しゃかく} (oblique angle), {情欲|じょうよく} (carnal desire). Conjugation tables added to the 1 ichidan + 2 suru verbs; **1 new kanji** assigned an ID — 胎 (02787_tai_none_womb). §4 cross-model self-check on all 15 changed entries: **clean — 15/15, 0 flagged, 0 applied, 0 rejected**. $0.0065.

- **Nature / food (2)**: {甘柿|あまがき} (sweet persimmon), {柿色|かきいろ} (persimmon color)
- **Construction / physics (4)**: {音圧|おんあつ} (sound pressure), {骨材|こつざい} (aggregate), {斜角|しゃかく} (oblique angle), {広縁|ひろえん} (wide veranda)
- **Verbs (3)**: かけ{離|はな}れる (to differ greatly), {堕胎|だたい} (abortion; verb-suru), {受贈|じゅぞう} (receiving a donation; verb-suru)
- **Other (6)**: {引|ひ}き{渡|わた}し (handover), {薬用|やくよう} (medicinal), {養豚|ようとん} (pig farming), {局番|きょくばん} (exchange number), {路側|ろそく} (roadside), {情欲|じょうよく} (carnal desire)

### 2026-07-24 (Routine v2: new-entries — 13 New Entries, IDs 30077–30089)
Created 13 general-tier entries, **all 13 from the "seen in entry" priority queue** (candidates C22516–C22528, cited from entries 06608, 06609, 06612–06614, 06616) — internal-completeness gaps the dictionary already referenced. This **cleared the seen-in-entry queue**. Clusters: places/loanwords — カナダ (Canada), ニュージーランド (New Zealand), ワーキングホリデー (working holiday; full form of ワーホリ), カードキー (key card), コンバイン (combine harvester); compass directions — {北西|ほくせい} (northwest), {南東|なんとう} (southeast), completing the intercardinal set alongside existing {北東|ほくとう}/{南西|なんせい}; law — {法体系|ほうたいけい} (legal system), {六法全書|ろっぽうぜんしょ} (compendium of laws), {商法|しょうほう} (commercial code), {訴訟法|そしょうほう} (procedural law), {判例|はんれい} (judicial precedent); plus one literary verb — {雪|そそ}ぐ (to wipe out a disgrace / avenge; verb-godan, godan-gu). Conjugation table added to the new godan verb; no new kanji. §4 cross-model self-check on all 13 changed entries: **12 clean, 1 flagged — 1 applied, 0 rejected** — added a `business` semantic tag to {商法|しょうほう} to cover its 悪徳商法 "way of doing business" sense, which the entry documents. $0.0056. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Places / loanwords (5)**: カナダ (Canada), ニュージーランド (New Zealand), ワーキングホリデー (working holiday), カードキー (key card), コンバイン (combine harvester)
- **Compass directions (2)**: {北西|ほくせい} (northwest), {南東|なんとう} (southeast)
- **Law (5)**: {法体系|ほうたいけい} (legal system), {六法全書|ろっぽうぜんしょ} (compendium of laws), {商法|しょうほう} (commercial code), {訴訟法|そしょうほう} (procedural law), {判例|はんれい} (judicial precedent)
- **Verb (1)**: {雪|そそ}ぐ (to wipe out a disgrace; to avenge; verb)

### 2026-07-23 (Routine v2: new-entries — 13 New Entries, IDs 30064–30076)
Created 13 general-tier entries, **all 13 from the "seen in entry" priority queue** (candidates C22502–C22514, cited from entries 06590, 06599–06604, 30055, 30062) — internal-completeness gaps the dictionary already referenced. This **cleared the seen-in-entry queue**. Clusters: computing/AI — {自然|しぜん}{言語|げんご}{処理|しょり} (NLP), {畳|たた}み{込|こ}み (convolution), ニューラルネットワーク (neural network), クラウドストレージ (cloud storage), {内蔵|ないぞう} (built-in; verb-suru), {置|お}き{換|か}わる (to be replaced; verb-godan, paired with {置|お}き{換|か}える); energy/electronics — リチウムイオン{電池|でんち} (lithium-ion battery), {配電|はいでん} (power distribution; verb-suru), スマートグリッド (smart grid); music — {拍|はく} (beat; counter), グルーブ (groove); science/folklore — {状態変化|じょうたいへんか} (change of state; verb-suru), {浮遊霊|ふゆうれい} (wandering spirit). Conjugation tables added to the 3 new suru-verbs and 1 godan verb; no new kanji. The C22505 グルーヴ candidate was created under the equally-standard グルーブ spelling (the ゔ form is not romanizable by the ID toolchain) and C22515 部 was dropped as already covered by the 〜部 suffix entry (00440_bu). §4 cross-model self-check on all 13 changed entries: **clean — 13/13, 0 flagged, 0 applied, 0 rejected**. $0.0056. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Computing / AI (6)**: {自然|しぜん}{言語|げんご}{処理|しょり} (NLP), {畳|たた}み{込|こ}み (convolution), ニューラルネットワーク (neural network), クラウドストレージ (cloud storage), {内蔵|ないぞう} (built-in; verb), {置|お}き{換|か}わる (to be replaced; verb)
- **Energy / electronics (3)**: リチウムイオン{電池|でんち} (lithium-ion battery), {配電|はいでん} (power distribution; verb), スマートグリッド (smart grid)
- **Music (2)**: {拍|はく} (beat; counter), グルーブ (groove)
- **Science / folklore (2)**: {状態変化|じょうたいへんか} (change of state; verb), {浮遊霊|ふゆうれい} (wandering spirit)

### 2026-07-23 (Routine v2: new-entries — 15 New Entries, IDs 30049–30063)
Created 15 general-tier entries. The **13 "seen in entry" candidates** (C22489–C22501, cited from entries 30031–30048 and 06583–06591) were created first — internal-completeness gaps the dictionary already referenced; this **cleared the seen-in-entry queue**. The 5 business/finance words were the ones flagged as referenced-but-missing by the 2026-07-22 run: {入金|にゅうきん}{済|ず}み (payment received), {比較表|ひかくひょう} (comparison table), {借入額|かりいれがく} (amount borrowed), {社用車|しゃようしゃ} (company car), plus {通電|つうでん} (energizing; verb-suru). A soccer-position set filled the 06587–06589 gaps: サブ (sub/backup), センターバック (center back), サイドバック (fullback), ボランチ (defensive midfielder), サイドハーフ (side midfielder). Plus {遺恨|いこん} (grudge), {地縛霊|じばくれい} (earthbound spirit; folklore), {炭化水素|たんかすいそ} (hydrocarbon). The 2 remaining are hand-picked standalone lexemes, since the non-seen candidate pool stays **heavily polluted** (transparent compounds, corpus fragments, wrong readings): {相変化|そうへんか} (phase change; verb-suru), {索引語|さくいんご} (index term). Conjugation tables added to the 2 new suru-verbs ({通電|つうでん}, {相変化|そうへんか}); no new kanji. §4 cross-model self-check on all 15 changed entries: **14 clean, 1 flagged — 1 applied (2 issues), 0 rejected** — dropped "principal" from {借入額|かりいれがく}'s gloss (借入額 is the amount borrowed, not 元金 principal proper). $0.0065. Added {浮遊霊|ふゆうれい} (wandering spirit) and {状態変化|じょうたいへんか} (change of state) as referenced-but-missing candidates. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Business / finance (5)**: {入金|にゅうきん}{済|ず}み (payment received), {比較表|ひかくひょう} (comparison table), {借入額|かりいれがく} (amount borrowed), {社用車|しゃようしゃ} (company car), {通電|つうでん} (energizing; verb)
- **Soccer positions (5)**: サブ (sub/backup), センターバック (center back), サイドバック (fullback), ボランチ (defensive midfielder), サイドハーフ (side midfielder)
- **Other (5)**: {遺恨|いこん} (grudge), {地縛霊|じばくれい} (earthbound spirit), {炭化水素|たんかすいそ} (hydrocarbon), {相変化|そうへんか} (phase change; verb), {索引語|さくいんご} (index term)
