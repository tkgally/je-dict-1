# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-07-17
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

### 2026-07-18 (Routine v2: new-entries — 12 New Entries, IDs 29924–29935)
Created 12 general-tier noun entries. The **3 remaining "seen in entry" candidates** (C22399–C22401, cited from entry 06526 平泳ぎ) were created first — a swimming set: メドレー (medley), {蛙足|かえるあし} (frog kick), プル (swimming arm pull). This **cleared the seen-in-entry queue**. The other 9 are hand-picked standalone lexemes, because the general candidate pool is now **heavily polluted with corpus-harvesting noise** — a ~600-candidate sample across the full added-date range was mostly bare numbers/counters, compositional phrases, mis-glossed place names, coined compounds, and wrong-kanji/wrong-gloss items. The 9 salvaged: {曳航|えいこう}{船|せん} (tugboat); a baseball cluster — {中堅|ちゅうけん}{手|しゅ} (center fielder), {右翼|うよく}{手|しゅ} (right fielder), {左翼|さよく}{手|しゅ} (left fielder), {出塁|しゅつるい}{率|りつ} (on-base percentage), {打点|だてん}{王|おう} (RBI leader); plus {章末|しょうまつ} (end of a chapter), {手|て}{牌|はい} (mahjong hand tiles), {持|じ}{碁|ご} (drawn game in go). All plain nouns — no new verbs, i-adjectives, or kanji. No duplicates created. Removed 1 stale candidate (C18953 剥れる/はぐれる — wrong kanji+gloss for the existing entry 28244 はぐれる). §4 cross-model self-check on all 12 changed entries: **clean — 12/12, 0 flagged, 0 applied, 0 rejected**. $0.0052. Logged a `[tooling]` observation recommending a curator prune of the corpus-harvested junk and a restock of useful mid-frequency vocabulary — the pool can no longer feed a full 20-entry run at quality.

- **Swimming — seen-in-entry (3)**: メドレー (medley), {蛙足|かえるあし} (frog kick), プル (arm pull)
- **Baseball (5)**: {中堅|ちゅうけん}{手|しゅ} (center fielder), {右翼|うよく}{手|しゅ} (right fielder), {左翼|さよく}{手|しゅ} (left fielder), {出塁|しゅつるい}{率|りつ} (on-base percentage), {打点|だてん}{王|おう} (RBI leader)
- **Other (4)**: {曳航|えいこう}{船|せん} (tugboat), {章末|しょうまつ} (end of a chapter), {手|て}{牌|はい} (mahjong hand tiles), {持|じ}{碁|ご} (drawn game in go)

### 2026-07-17 (Routine v2: new-entries — 18 New Entries, IDs 29906–29923)
Created 18 general-tier noun entries, **all 18 from the "seen in entry" priority queue** (candidates C22381–C22398, cited from entries 06517–06525, 29891, 29905) — internal-completeness gaps the dictionary already referenced. This **cleared the seen-in-entry queue**. Three thematic clusters plus a tail: a road-safety set (from 06517/06518) — {中央分離帯|ちゅうおうぶんりたい} (median strip), ガードパイプ (pipe guardrail), ガードケーブル (cable barrier), {単管|たんかん} (steel scaffolding pipe); a first-aid set (from 06519) — {心肺蘇生|しんぱいそせい} (CPR), {救命講習|きゅうめいこうしゅう} (lifesaving course), {応急手当|おうきゅうてあて} (emergency first aid); a rock-paper-scissors set (from 06520) — グー (rock), チョキ (scissors), パー (paper), {後出|あとだ}し (showing one's hand late); plus religion ({山伏|やまぶし} yamabushi, {修験道|しゅげんどう} Shugendo, from 06522), and singletons {保護色|ほごしょく} (protective coloration), {口直|くちなお}し (palate cleanser), {水|みず}かき (webbing), {世界一周|せかいいっしゅう} (round-the-world trip), {研|と}ぎ{師|し} (blade sharpener). All plain nouns — no new verbs, i-adjectives, or kanji. No duplicates. §4 cross-model self-check on all 18 changed entries: **clean — 18/18, 0 flagged, 0 applied, 0 rejected**. $0.0078. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Road safety (4)**: {中央分離帯|ちゅうおうぶんりたい} (median strip), ガードパイプ (pipe guardrail), ガードケーブル (cable barrier), {単管|たんかん} (steel scaffolding pipe)
- **First aid (3)**: {心肺蘇生|しんぱいそせい} (CPR), {救命講習|きゅうめいこうしゅう} (lifesaving course), {応急手当|おうきゅうてあて} (emergency first aid)
- **Rock-paper-scissors (4)**: グー (rock), チョキ (scissors), パー (paper), {後出|あとだ}し (showing one's hand late)
- **Religion / nature / everyday (7)**: {山伏|やまぶし} (yamabushi), {修験道|しゅげんどう} (Shugendo), {保護色|ほごしょく} (protective coloration), {口直|くちなお}し (palate cleanser), {水|みず}かき (webbing), {世界一周|せかいいっしゅう} (round-the-world trip), {研|と}ぎ{師|し} (blade sharpener)

### 2026-07-16 (Routine v2: new-entries — 18 New Entries, IDs 29888–29905)
Created 18 general-tier entries, **all 18 from the "seen in entry" priority queue** (candidates C22361/C22363–C22372/C22374–C22380, cited from entries 29878/29881/29883 and the 06505–06516 nature block) — internal-completeness gaps the dictionary already referenced. Of the 20 seen-in-entry candidates, **2 were duplicates removed rather than created**: テントウムシ (= existing てんとう{虫|むし} at 06497) and アシナガバチ (= existing {足長蜂|あしながばち} at 28005). This **cleared the seen-in-entry queue**. The bulk is a nature/insect cluster drawn from the 06513–06516 entries — {擬態|ぎたい} (mimicry; noun/suru), {女王蜂|じょおうばち} (queen bee), {働|はたら}き{蜂|ばち} (worker bee), クマバチ (carpenter bee), キリギリス (katydid), コオロギ (cricket), トノサマバッタ (migratory locust), オランウータン (orangutan), シルバーバック (silverback), {前足|まえあし} (foreleg), {草|くさ}むら (grassy thicket) — plus a handful of science/medical/weather/food/time singletons. Conjugation tables added to the 1 new suru-verb ({擬態|ぎたい}) and 1 new i-adjective (わざとらしい); 1 new kanji ({珪|けい} → 02785_kei_none_silica, from {珪素|けいそ}). §4 cross-model self-check on all 18 changed entries: **12 clean, 6 flagged — 0 applied, 6 rejected** — all in-list semantic-tag breadth nits (health→okubi, +nature/animal-general→擬態), a gloss-broadening nit (working-bee figurative sense, already in the definition), a narrower-species gloss (Oriental migratory locust vs migratory locust), a translation "contradiction" already explained in the notes (アリとキリギリス = The Ant and the Grasshopper), and one null flag (suggestion equalled the current gloss); rejected per the in-list-narrowness policy. $0.0078. Removed 2 stale duplicate candidates (C22362, C22373); added {保護色|ほごしょく} (protective coloration) and {口直|くちなお}し (palate cleanser) as referenced-but-missing candidates. The seen-in-entry queue is empty again and awaits curator/polish restock.

- **Nature / insects & animals (11)**: {擬態|ぎたい} (mimicry; suru), {女王蜂|じょおうばち} (queen bee), {働|はたら}き{蜂|ばち} (worker bee), クマバチ (carpenter bee), キリギリス (katydid), コオロギ (cricket), トノサマバッタ (migratory locust), オランウータン (orangutan), シルバーバック (silverback), {前足|まえあし} (foreleg), {草|くさ}むら (grassy thicket)
- **Science / medical / weather (4)**: {医薬分業|いやくぶんぎょう} (separation of prescribing and dispensing), {珪素|けいそ} (silicon), {黄砂|こうさ} (yellow dust), おくび (belch)
- **Everyday / food / time / manner (3)**: シャーベット (sherbet), {飛|と}び{石|いし}{連休|れんきゅう} (scattered holidays), わざとらしい (affected; adj-i)

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
