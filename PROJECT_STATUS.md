# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-18
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
| Total entries | ~11,900 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,101 (open) |
| Candidate words | ~270 |
| Cross-references | ~3,350 |
| Example sentences | ~43,400 |
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

### 2026-02-18 (Vocabulary Expansion - 30 New Entries, Session 269)
Added 30 new dictionary entries (IDs 11815-11844) from candidate_words.json:

- **Nouns/suru verbs - formal (7)**: {到達|とうたつ} (reaching), {制御|せいぎょ} (control), {勃発|ぼっぱつ} (outbreak), {喪失|そうしつ} (loss), {収集|しゅうしゅう} (collection), {募金|ぼきん} (fundraising), {回想|かいそう} (reminiscence)
- **Nouns - time/schedule (3)**: {前回|ぜんかい} (last time), {前倒|まえだお}し (moving up schedule), {即席|そくせき} (instant/impromptu)
- **Nouns - formal/abstract (4)**: {効力|こうりょく} (efficacy), {原点|げんてん} (origin), {協会|きょうかい} (association), {加齢|かれい} (aging)
- **Nouns - concrete/cultural (5)**: {剣|けん} (sword), {古民家|こみんか} (old traditional house), {商店|しょうてん} (shop), {品揃|しなぞろ}え (product lineup), {呪文|じゅもん} (spell/incantation)
- **Nouns - other (3)**: {原作|げんさく} (original work), {喜劇|きげき} (comedy), {品種|ひんしゅ} (variety/breed)
- **Na-adjective (1)**: {単調|たんちょう} (monotonous)
- **I-adjective (1)**: {危|あや}うい (dangerous/precarious)
- **Nouns (1)**: {器|うつわ} (vessel/caliber)
- **Verbs (5)**: {割|さ}く (to spare/devote), {励|はげ}む (to work hard at), {咲|さ}き{誇|ほこ}る (to be in full bloom), {営|いとな}む (to run a business), {吹|ふ}き{飛|と}ぶ (to be blown away)

Notable features:
- Multi-sense entries: {割|さ}く (spare/tear), {危|あや}うい (dangerous/narrowly), {営|いとな}む (run business/conduct ceremony), {器|うつわ} (vessel/caliber), {吹|ふ}き{飛|と}ぶ (blown away/vanish)
- Cultural context: {古民家|こみんか} (renovation trend), {器|うつわ} (food presentation aesthetics), {呪文|じゅもん} (Dragon Quest/RPG culture), {剣|けん} (martial arts)
- New kanji: 2,321 → 2,323 ({勃|ぼつ}, {呪|じゅ})

Total entries: 11,870 → 11,900
Remaining candidates: 300 → 270 (30 removed)

### 2026-02-18 (Vocabulary Expansion - 30 New Entries, Session 268)
Added 30 new dictionary entries (IDs 11785-11814) from candidate_words.json:

- **Nouns/suru verbs - formal (8)**: {判明|はんめい} (becoming clear), {削減|さくげん} (reduction), {創業|そうぎょう} (founding a business), {加工|かこう} (processing), {勝利|しょうり} (victory), {回避|かいひ} (avoidance), {制約|せいやく} (constraint), {収容|しゅうよう} (accommodation/internment)
- **Nouns - abstract/formal (6)**: {利点|りてん} (advantage), {前例|ぜんれい} (precedent), {効率|こうりつ} (efficiency), {危機|きき} (crisis), {勢力|せいりょく} (power/influence), {善意|ぜんい} (goodwill/good faith)
- **Nouns - time/arrival (2)**: {到来|とうらい} (advent), {史上|しじょう} (in history)
- **Nouns - concrete/cultural (5)**: {別荘|べっそう} (villa), {化石|かせき} (fossil), {匿名|とくめい} (anonymity), {口調|くちょう} (tone of voice), {古都|こと} (ancient capital)
- **Nouns - other (3)**: {前線|ぜんせん} (front line/weather front), {原則|げんそく} (principle), {原料|げんりょう} (raw materials)
- **Na-adjective (1)**: {台無|だいな}し (ruined)
- **Noun (1)**: {四季|しき} (four seasons)
- **Verbs (4)**: {占|し}める (to occupy/account for), {叶|かな}える (to fulfill), {告|つ}げる (to tell/herald), {嘆|なげ}く (to lament)

Notable features:
- Multi-sense entries: {占|し}める (occupy/account for), {告|つ}げる (tell/herald), {善意|ぜんい} (goodwill/good faith legal), {前線|ぜんせん} (front line/weather front), {収容|しゅうよう} (accommodation/internment), {原則|げんそく} (principle/as a rule)
- Homophone cross-references: {占|し}める ↔ {閉|し}める/{締|し}める, {勢力|せいりょく} ↔ {精力|せいりょく}
- Cultural context: {別荘|べっそう} (Karuizawa resort culture), {古都|こと} (Kyoto/Nara preservation), {四季|しき} (seasonal awareness), {匿名|とくめい} (anonymous internet culture)
- New kanji: 2,319 → 2,321 ({嘆|たん}, {荘|そう})

Total entries: 11,840 → 11,870
Remaining candidates: 330 → 300 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 267)
Added 30 new dictionary entries (IDs 11755-11784) from candidate_words.json:

- **Nouns - time/seasons (4)**: {冬季|とうき} (winter season), {冬至|とうじ} (winter solstice), {初雪|はつゆき} (first snow), {初回|しょかい} (first time/round)
- **Nouns/suru verbs - emergence/departure (6)**: {出現|しゅつげん} (appearance), {出土|しゅつど} (excavation), {出家|しゅっけ} (entering priesthood), {出港|しゅっこう} (departure from port), {出生|しゅっしょう} (birth), {処刑|しょけい} (execution)
- **Nouns - publishing/education (3)**: {出版社|しゅっぱんしゃ} (publisher), {全集|ぜんしゅう} (complete works), {初級|しょきゅう} (beginner level)
- **Nouns/suru verbs - division/separation (5)**: {分岐|ぶんき} (branching), {分担|ぶんたん} (sharing duties), {分断|ぶんだん} (division), {分離|ぶんり} (separation), {分子|ぶんし} (molecule)
- **Nouns - history/politics (3)**: {切腹|せっぷく} (seppuku), {列強|れっきょう} (great powers), {列挙|れっきょ} (enumeration)
- **Nouns - succession/salary (3)**: {初代|しょだい} (first generation), {初任給|しょにんきゅう} (starting salary), {再燃|さいねん} (recurrence)
- **Nouns - general (2)**: {出来|でき} (result/quality), {分刻|ふんきざ}み (minute by minute)
- **Verbs (4)**: {凍|こお}りつく (to freeze solid), {出揃|でそろ}う (to be all present), {分|わ}け{合|あ}う (to share), {切|き}り{分|わ}ける (to cut into pieces)

Notable features:
- Multi-sense entries: {凍|こお}りつく (freeze solid/freeze with fear), {分子|ぶんし} (molecule/numerator/group member)
- Cultural context: {冬至|とうじ} (yuzu bath tradition), {切腹|せっぷく} (samurai ritual), {出家|しゅっけ} (Buddhist vows), {初任給|しょにんきゅう} (gift tradition), {初雪|はつゆき} (seasonal news event)
- Semantic clusters: 出- compounds (7 entries), 分- compounds (6 entries), 初- compounds (5 entries)
- Distinction sets: {分担|ぶんたん} vs {分断|ぶんだん} vs {分離|ぶんり}

Total entries: 11,810 → 11,840
Remaining candidates: 360 → 330 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 266)
Added 30 new dictionary entries (IDs 11725-11754) from candidate_words.json:

- **Nouns - cold/food (2)**: {冷凍|れいとう} (freezing), {冷蔵|れいぞう} (refrigeration)
- **Nouns - entertainment (2)**: {出演|しゅつえん} (appearing on stage/TV), {出番|でばん} (one's turn)
- **Nouns - life events/health (2)**: {出産|しゅっさん} (childbirth), {出血|しゅっけつ} (bleeding)
- **Nouns - time/seasons (3)**: {初夏|しょか} (early summer), {初日|しょにち} (first day), {初期|しょき} (early period)
- **Nouns - formal/political (4)**: {冒頭|ぼうとう} (beginning/opening), {共同体|きょうどうたい} (community), {内乱|ないらん} (civil war), {列島|れっとう} (archipelago)
- **Nouns/suru verbs (6)**: {出品|しゅっぴん} (exhibiting/listing), {再建|さいけん} (reconstruction), {再考|さいこう} (reconsideration), {分割|ぶんかつ} (division), {分配|ぶんぱい} (distribution), {分裂|ぶんれつ} (split/fission)
- **Nouns - general (3)**: {刃物|はもの} (blade/cutlery), {分|わ}かれ{道|みち} (fork in the road), {凪|なぎ} (calm/lull)
- **Verbs (4)**: {冷|ひ}え{込|こ}む (to get very cold), {冷|ひ}やかす (to tease/window-shop), {出回|でまわ}る (to circulate), {兼|か}ね{備|そな}える (to possess both)
- **Adjectives (2)**: {冷|ひ}ややか (chilly/cold in attitude), {切実|せつじつ} (earnest/pressing)
- **Adverbs (2)**: {切|せつ}に (earnestly), {凛|りん}と (with dignity)

Notable features:
- Diverse POS mix: 22 nouns (incl. suru verbs), 4 verbs, 2 adjectives, 2 adverbs
- Multi-sense entries: {冷|ひ}え{込|こ}む (cold weather/economy), {冷|ひ}やかす (tease/window-shop), {出品|しゅっぴん} (exhibit/list for sale), {再建|さいけん} (rebuild/restructure), {分裂|ぶんれつ} (political split/cell division), {冷|ひ}ややか (physical chill/cold attitude)
- Distinction sets: {冷凍|れいとう} vs {冷蔵|れいぞう}, {分割|ぶんかつ} vs {分配|ぶんぱい} vs {分裂|ぶんれつ}
- Homophone cross-references: {冒頭|ぼうとう} ↔ {暴騰|ぼうとう}, {再建|さいけん} ↔ {債権|さいけん}, {再考|さいこう} ↔ {最高|さいこう}, {出血|しゅっけつ} ↔ {出欠|しゅっけつ}, {内乱|ないらん} ↔ {内覧|ないらん}
- Cultural context: {凪|なぎ} (kokuji, weather phenomenon), {堺|さかい} cutlery ({刃物|はもの}), {日本|にほん}{列島|れっとう}
- New kanji: 2,318 → 2,319 ({凪|なぎ} — kokuji)

Total entries: 11,780 → 11,810
Remaining candidates: 390 → 360 (30 removed)

### 2026-02-17 (Vocabulary Expansion - 30 New Entries, Session 265)
Added 30 new dictionary entries (IDs 11695-11724) from candidate_words.json:

- **Loanwords - nouns (10)**: チュートリアル (tutorial), ファンタジー (fantasy), フィットネス (fitness), フェスティバル (festival), プレート (plate), レーダー (radar), ロール (roll/role), パッケージ (package), リアリティ (reality), ピックアップ (pickup/selection)
- **Loanwords - na-adjective (1)**: ポピュラー (popular)
- **Loanwords - noun/suru verb (3)**: スカウト (scouting/recruiting), トライ (try/attempt), リベラル (liberal)
- **Japanese nouns - formal/historical (6)**: {主君|しゅくん} (feudal lord), {伯爵|はくしゃく} (count/earl), {俗称|ぞくしょう} (colloquial name), {亡骸|なきがら} (remains/corpse), {不死|ふし} (immortality), {下位|かい} (lower rank)
- **Japanese nouns - general (5)**: {今日|こんにち} (today/nowadays), {交友|こうゆう} (friendship), {人力|じんりき} (manpower), {人工衛星|じんこうえいせい} (artificial satellite), {付加価値|ふかかち} (added value)
- **Japanese nouns - counter (1)**: {件|けん} (matter/case; counter for cases)
- **Japanese nouns - cultural (1)**: {仲居|なかい} (ryokan attendant)
- **Nouns - warfare (1)**: {交戦|こうせん} (battle/engagement)
- **Verbs (2)**: {代|か}える (to substitute), {代|か}わる (to take the place of)

Notable features:
- Good mix of katakana loanwords (14) and native Japanese words (16)
- Multi-sense entries: トライ (attempt/rugby try), パッケージ (packaging/package deal), プレート (dish/metal plate), ファンタジー (genre/daydream), ロール (roll/role), リアリティ (realism/reality TV), ピックアップ (selection/pickup), {件|けん} (matter/counter), {今日|こんにち} (today/nowadays)
- Transitive/intransitive pair: {代|か}える ↔ {代|か}わる
- Homophone cross-references: {今日|こんにち} ↔ {今日|きょう}, {不死|ふし} ↔ {節|ふし}, {交戦|こうせん} ↔ {光線|こうせん}
- Cultural context: {仲居|なかい} (ryokan hospitality), {伯爵|はくしゃく} (Meiji peerage system)
- New kanji: 2,314 → 2,318 ({伯|はく}, {俗|ぞく}, {爵|しゃく}, {称|しょう})

Total entries: 11,750 → 11,780
Remaining candidates: 420 → 390 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
