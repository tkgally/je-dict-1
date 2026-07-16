# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-14
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

### 2026-07-16 (Routine v2: new-entries — 12 New Entries, IDs 29876–29887)
Created 12 general-tier entries, **all 12 from the "seen in entry" priority queue** (candidates C22348, C22350–C22360, cited from entries 05432, 06496–06508) — internal-completeness gaps the dictionary already referenced. This **cleared the seen-in-entry queue**. A medical-dispensing cluster (from 06496) — {調剤|ちょうざい}{薬局|やっきょく} (dispensing pharmacy), {院内|いんない}{処方|しょほう} (in-hospital dispensing), {院外|いんがい}{処方|しょほう} (out-of-hospital dispensing); a Japanese-garden cluster (from 06501) — {飛|と}び{石|いし} (stepping stone), {石|いし}{灯籠|どうろう} (stone lantern); household/material loanwords (from 06508) — シリコン (silicone), {籐|とう} (rattan), コースター (coaster), ナチュラル (natural style; na-adj); plus ナナホシテントウ (seven-spot ladybird, from 06497), {涙|なみだ}ぐましい (touching, tear-inducing; adj-i, from 06499), and じゃんか (casual emphatic sentence-ending expression, from 05432 — the marginal candidate deferred by the 07-15 run, now given a concise expression entry). Conjugation table added to the 1 new i-adjective; 1 new kanji ({籐|とう} → 02784_tou_none_rattan). §4 cross-model self-check on all 12 changed entries: **9 clean, 3 flagged — 0 applied, 4 rejected** — all in-list semantic-tag breadth nits (tool/science suggested over general on 飛び石/シリコン/コースター) plus a gloss over-broadening on シリコン (silicone → "silicon; silicone"), rejected per the in-list-narrowness policy and the standard シリコン=silicone / {珪素|けいそ}=silicon mapping (the entry notes already document the loose usage). $0.0052. Added {医薬分業|いやくぶんぎょう}, テントウムシ, {珪素|けいそ}, {飛|と}び{石|いし}{連休|れんきゅう} as referenced-but-missing candidates. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Medical dispensing (3)**: {調剤|ちょうざい}{薬局|やっきょく} (dispensing pharmacy), {院内|いんない}{処方|しょほう} (in-hospital dispensing), {院外|いんがい}{処方|しょほう} (out-of-hospital dispensing)
- **Japanese garden (2)**: {飛|と}び{石|いし} (stepping stone), {石|いし}{灯籠|どうろう} (stone lantern)
- **Household / material loanwords (4)**: シリコン (silicone), {籐|とう} (rattan), コースター (coaster), ナチュラル (natural style; na-adj)
- **Nature / feeling / speech (3)**: ナナホシテントウ (seven-spot ladybird), {涙|なみだ}ぐましい (touching; adj-i), じゃんか (casual emphatic ending)

### 2026-07-15 (Routine v2: new-entries — 20 New Entries, IDs 29856–29875)
Created 20 general-tier entries. The **4 real "seen in entry" candidates** (C22345/C22346/C22347/C22349, cited from entries 29855/29847/29845/06492) were created first — internal-completeness gaps the dictionary already referenced: {邪教|じゃきょう} (evil cult; heretical religion), {番兵|ばんぺい} (sentry), {低迷期|ていめいき} (slump period), {部屋干|へやぼ}し (drying laundry indoors). Three of these had been logged as candidates by the 07-14 run. The 5th seen-in-entry candidate (じゃんか, a dialectal sentence-ending particle) was left for the curator as too marginal for a clean entry. The 部屋干し candidate reading was corrected from へやほし to the standard rendaku'd へやぼし. The remaining 16 are hand-picked standalone lexemes from the general pool (still heavily contaminated with compositional/OCR junk): {障害児|しょうがいじ} (child with a disability), {採用試験|さいようしけん} (hiring exam), {静止衛星|せいしえいせい} (geostationary satellite), {使用者|しようしゃ} (user / employer — 2 senses, legal), {学長|がくちょう} (university president), {射撃場|しゃげきじょう} (shooting range), {転居先|てんきょさき} (new address), {督促状|とくそくじょう} (demand notice), {低評価|ていひょうか} (low rating), {限定販売|げんていはんばい} (limited sale; suru), {調達先|ちょうたつさき} (supplier), {昇降口|しょうこうぐち} (school entrance), {奉公人|ほうこうにん} (live-in servant; historical), {再構成|さいこうせい} (restructuring; suru), {受賞歴|じゅしょうれき} (award history), {傷病者|しょうびょうしゃ} (injured/sick person). Conjugation tables added to the 2 new suru-verbs; no i-adjectives, no new kanji. One duplicate skipped at batch-check ({派出所|はしゅつじょ}, which already exists as a reading variant at 13284). §4 cross-model self-check on all 20 changed entries: **19 clean, 1 flagged — 2 applied, 0 rejected** — the model correctly caught that {昇降口|しょうこうぐち}'s gloss "entrance; entryway" was too broad; narrowed to "entrance; entryway (esp. of a school)" in both the top-level and sense gloss. $0.0087. The seen-in-entry queue is empty again (bar the deferred じゃんか) and awaits curator/polish restock.

- **Seen-in-entry priority (4)**: {邪教|じゃきょう} (evil cult), {番兵|ばんぺい} (sentry), {低迷期|ていめいき} (slump period), {部屋干|へやぼ}し (drying laundry indoors)
- **People / social (5)**: {障害児|しょうがいじ} (child with a disability), {使用者|しようしゃ} (user; employer), {学長|がくちょう} (university president), {奉公人|ほうこうにん} (live-in servant; historical), {傷病者|しょうびょうしゃ} (injured/sick person)
- **Places / objects (3)**: {静止衛星|せいしえいせい} (geostationary satellite), {射撃場|しゃげきじょう} (shooting range), {昇降口|しょうこうぐち} (school entrance)
- **Business / abstract (8)**: {採用試験|さいようしけん} (hiring exam), {転居先|てんきょさき} (new address), {督促状|とくそくじょう} (demand notice), {低評価|ていひょうか} (low rating), {限定販売|げんていはんばい} (limited sale; suru), {調達先|ちょうたつさき} (supplier), {再構成|さいこうせい} (restructuring; suru), {受賞歴|じゅしょうれき} (award history)

### 2026-07-14 (Routine v2: new-entries — 17 New Entries, IDs 29839–29855)
Created 17 general-tier entries. The **5 "seen in entry" candidates** (C22324/C22335/C22342–C22344, cited from entries 06471/06477/06481/06486) were created first — internal-completeness gaps the dictionary already referenced: ソックス (socks), {読|よ}み{直|なお}す (to reread; godan), {丈|たけ} (length; hem length), コンポスター (composter), オン (on; switched-on state). This **cleared the seen-in-entry queue**. The other 12 are hand-picked standalone lexemes from the general pool, which remains heavily contaminated with compositional/OCR junk: {異教徒|いきょうと} (pagan) and {異教|いきょう} (paganism), {偏愛|へんあい} (favoritism; suru), {困憊|こんぱい} (utter exhaustion; suru), {衛兵|えいへい} (sentry), {消防隊|しょうぼうたい} (fire brigade), {統率者|とうそつしゃ} (leader/commander), {停滞期|ていたいき} (period of stagnation), {自然観|しぜんかん}/{宇宙観|うちゅうかん} (view of nature / of the universe; the ～観 pattern), {他郷|たきょう} (place away from home; literary), {無価値|むかち} (worthless; na-adjective). Conjugation tables added to the 1 new godan verb and 2 new suru-verbs; no i-adjectives, no new kanji. Three duplicates skipped at batch-check ({潔|いさぎよ}い, {偏見|へんけん}, and {派出所|はしゅつじょ} which already exists as a reading variant); the stale phrase candidate {潔|いさぎよ}い{態度|たいど} was removed. §4 cross-model self-check on all 17 changed entries: **16 clean, 1 flagged — 0 applied, 1 rejected** — an in-list semantic-tag narrowness nit (health→action on {困憊|こんぱい}), rejected per the in-list-narrowness policy (health is consistent with {過労|かろう} at 08563). $0.0074. Added {邪教|じゃきょう}, {番兵|ばんぺい}, {低迷期|ていめいき} as referenced-but-missing candidates. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Seen-in-entry priority (5)**: ソックス (socks), {読|よ}み{直|なお}す (to reread; godan), {丈|たけ} (length; hem length), コンポスター (composter), オン (on; switched-on state)
- **Religion / people (4)**: {異教徒|いきょうと} (pagan), {異教|いきょう} (paganism), {衛兵|えいへい} (sentry), {統率者|とうそつしゃ} (leader/commander)
- **State / abstract nouns (5)**: {偏愛|へんあい} (favoritism; suru), {困憊|こんぱい} (utter exhaustion; suru), {停滞期|ていたいき} (period of stagnation), {自然観|しぜんかん} (view of nature), {宇宙観|うちゅうかん} (view of the universe)
- **Other (3)**: {消防隊|しょうぼうたい} (fire brigade), {他郷|たきょう} (place away from home; literary), {無価値|むかち} (worthless; na-adjective)

### 2026-07-14 (Routine v2: new-entries — 20 New Entries, IDs 29819–29838)
Created 20 general-tier entries, **all 20 from the "seen in entry" priority queue** (candidates C22320–C22341, cited from entries 06471–06479, 29808/29811/29815) — internal-completeness gaps the dictionary already referenced. This **cleared the seen-in-entry queue**. One stale candidate (きたならしい, the kana form of the existing {汚|きたな}らしい at 29808) was removed rather than created. Two thematic clusters plus a tail: a composting/gardening set (mostly from 06471) and a packaged-food-label set (from 06479); plus streaming/app terms and a handful of everyday words including one i-adjective (むさ{苦|くる}しい). Conjugation tables added to the 2 new suru-verbs and 1 new i-adjective; no new kanji. §4 cross-model self-check on all 20 changed entries: **18 clean, 2 flagged — 0 applied, 2 rejected** — both were in-list semantic-tag narrowness nits (daily-life on {不使用|ふしよう}, food on {酸化防止剤|さんかぼうしざい}), rejected per the in-list-narrowness policy. $0.0086. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Composting/gardening (4)**: コンポスト (compost, compost bin), {刈|か}り{草|くさ} (grass clippings), {枯|か}れ{枝|えだ} (dead branch), {堆肥化|たいひか} (composting; suru)
- **Food-label terms (4)**: {不使用|ふしよう} (X-free; non-use), {乳化剤|にゅうかざい} (emulsifier), {酸化防止剤|さんかぼうしざい} (antioxidant), {原材料名|げんざいりょうめい} (ingredients list)
- **Streaming/app terms (7)**: プロフ (profile; casual), {実況者|じっきょうしゃ} (streamer, commentator), Vチューバー (VTuber), プッシュ (push, notify; suru), リマインダー (reminder), {通知音|つうちおん} (notification sound), {微課金|びかきん} (light in-app spending; slang)
- **Everyday & other (5)**: {数回|すうかい} (several times), むさ{苦|くる}しい (squalid, shabby; adj-i), {果物|くだもの}{狩|が}り (fruit picking), {登録料|とうろくりょう} (registration fee), スポーツジム (fitness gym)

### 2026-07-13 (Routine v2: new-entries — 15 New Entries, IDs 29804–29818)
Created 15 general-tier entries. The **8 "seen in entry" candidates** (C22312–C22319, cited from entries 00788, 06463–06465, 06470, 29796) were created first — internal-completeness gaps the dictionary already referenced: {抄本|しょうほん} (abstract copy of a register; legal, counterpart of {謄本|とうほん}), {八重|やえ} (multi-petaled/multi-layered) and {八重桜|やえざくら} (double cherry blossom), {奥二重|おくぶたえ} (inner double eyelid; the 一重/二重 eyelid cluster), {汚|きたな}らしい (filthy, grimy; intensified 汚い, previously a `noentry` inline-link target in 00788), and three gaming/youth-slang terms — チルする (to chill; suru), エンジョイ{勢|ぜい} (casual player; counterpart of ガチ勢), {重課金勢|じゅうかきんぜい} (heavy spender/"whale"). This **cleared the seen-in-entry queue**. The other 7 are hand-picked genuine standalone lexemes: {三桁|さんけた} (three-digit number), {融雪|ゆうせつ} (snowmelt/thaw), {写|うつ}り{具合|ぐあい} (how a photo comes out), {数台|すうだい} (several vehicles/machines; the 数〜 pattern), シャッター{通|どお}り (shuttered shopping street), {洗浄剤|せんじょうざい} (cleaning agent), {資料室|しりょうしつ} (reference/archive room). Conjugation tables added to the 1 new suru-verb and 1 new i-adjective; no new kanji. §4 cross-model self-check on all 15 changed entries: **fully clean — 0 flagged, 0 applied, 0 rejected**. $0.0065. Added {微課金|びかきん}, {数回|すうかい}, むさ{苦|くる}しい as referenced-but-missing candidates. The old corpus-harvested candidate block remains heavily polluted with OCR/hallucination non-words; logged a `[pattern]` observation recommending a cleanup pass.

- **Seen-in-entry priority (8)**: {抄本|しょうほん} (abstract copy; legal), {八重|やえ} (multi-petaled), {八重桜|やえざくら} (double cherry blossom), {奥二重|おくぶたえ} (inner double eyelid), {汚|きたな}らしい (filthy; adj-i), チルする (to chill; slang suru), エンジョイ{勢|ぜい} (casual player; slang), {重課金勢|じゅうかきんぜい} (heavy spender; slang)
- **Standalone lexemes (7)**: {三桁|さんけた} (three digits), {融雪|ゆうせつ} (snowmelt), {写|うつ}り{具合|ぐあい} (photographic result), {数台|すうだい} (several machines), シャッター{通|どお}り (shuttered street), {洗浄剤|せんじょうざい} (cleaning agent), {資料室|しりょうしつ} (reference room)

