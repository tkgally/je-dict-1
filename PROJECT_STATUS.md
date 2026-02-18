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
| Total entries | ~11,960 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,161 (open) |
| Candidate words | ~210 |
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

### 2026-02-18 (Vocabulary Expansion - 30 New Entries, Session 271)
Added 30 new dictionary entries (IDs 11875-11904) from candidate_words.json:

- **Nouns - time (3)**: {前半|ぜんはん} (first half), {前夜|ぜんや} (the night before), {初頭|しょとう} (beginning of a period)
- **Nouns - 別 compounds (4)**: {別人|べつじん} (different person), {別名|べつめい} (alias), {別物|べつもの} (different thing entirely), {別途|べっと} (separately)
- **Nouns - 厳 compounds/na-adj (4)**: {厳守|げんしゅ} (strict observance), {厳密|げんみつ} (precise), {厳格|げんかく} (strict/stern), {厳重|げんじゅう} (tight/stringent)
- **Nouns - ceremony/customs (3)**: {参列|さんれつ} (ceremony attendance), {喪服|もふく} (mourning clothes), {吉日|きちじつ} (auspicious day)
- **Nouns - body/speech (2)**: {口元|くちもと} (area around the mouth), {口頭|こうとう} (oral/verbal)
- **Nouns/suru - formal (4)**: {制裁|せいさい} (sanction), {収縮|しゅうしゅく} (contraction), {受診|じゅしん} (seeing a doctor), {別居|べっきょ} (living apart)
- **Nouns - relationships/culture (4)**: {同棲|どうせい} (cohabitation), {回転寿司|かいてんずし} (conveyor belt sushi), {合宿|がっしゅく} (training camp), {合流|ごうりゅう} (merging/joining up)
- **Nouns - general (6)**: {召使|めしつか}い (servant), {吐露|とろ} (disclosure), {向上心|こうじょうしん} (ambition), {味|あじ}わい (flavor/charm), {古風|こふう} (old-fashioned), {営|いとな}み (activity/pursuit)

Notable features:
- Multi-sense entries: {味|あじ}わい (flavor/charm), {合流|ごうりゅう} (rivers-roads/people)
- Semantic clusters: 別- compounds (4), 厳- compounds (4)
- Distinction set: {厳密|げんみつ} vs {厳格|げんかく} vs {厳重|げんじゅう}
- Cultural context: {吉日|きちじつ} (六曜 calendar), {回転寿司|かいてんずし} (dining culture), {喪服|もふく} (funeral etiquette), {合宿|がっしゅく} (club culture)

Total entries: 11,930 → 11,960
Remaining candidates: 240 → 210 (30 removed)

### 2026-02-18 (Vocabulary Expansion - 30 New Entries, Session 270)
Added 30 new dictionary entries (IDs 11845-11874) from candidate_words.json:

- **Verbs - godan (6)**: {利|き}く (to be effective), {勝|まさ}る (to surpass), {区切|くぎ}る (to divide/mark off), {口説|くど}く (to persuade/hit on), {呪|のろ}う (to curse), {名乗|なの}る (to call oneself)
- **Verbs - ichidan (4)**: {努|つと}める (to strive), {化|ば}ける (to transform), {収|おさ}まる (to fit into/settle down), {割|わ}り{当|あ}てる (to assign/allocate)
- **I-adjective (1)**: {勇|いさ}ましい (brave, valiant)
- **Na-adjective (1)**: {厳|おごそ}か (solemn, majestic)
- **Nouns - abstract/formal (6)**: {双方|そうほう} (both sides), {即座|そくざ} (immediately), {危惧|きぐ} (apprehension), {参照|さんしょう} (reference), {因果|いんが} (cause and effect/karma), {厳選|げんせん} (careful selection)
- **Nouns - military/historical (2)**: {反乱|はんらん} (rebellion), {占領|せんりょう} (occupation)
- **Nouns - cultural (2)**: {古墳|こふん} (ancient burial mound), {唐辛子|とうがらし} (chili pepper)
- **Nouns - general (4)**: {呼|よ}びかけ (call/appeal), {命懸|いのちが}け (risking one's life), {咆哮|ほうこう} (roar/howl), {医師|いし} (doctor/physician)
- **Nouns - arts/records (4)**: {台本|だいほん} (script/screenplay), {名作|めいさく} (masterpiece), {名簿|めいぼ} (register/roster), {受賞|じゅしょう} (winning a prize)

Notable features:
- Multi-sense entries: {利|き}く (effective/possible), {化|ば}ける (supernatural/figurative), {区切|くぎ}る (segment/conclude), {口説|くど}く (persuade/romance), {収|おさ}まる (fit/settle), {因果|いんが} (causation/karma), {名乗|なの}る (identify/claim)
- Homophone cross-references: {利|き}く ↔ {効|き}く/{聞|き}く, {努|つと}める ↔ {務|つと}める/{勤|つと}める, {医師|いし} ↔ {意志|いし}/{石|いし}
- Cultural context: {古墳|こふん} (Kofun period/UNESCO), {唐辛子|とうがらし} (shichimi/ichimi), {化|ば}ける (fox/tanuki folklore)
- New kanji: 2,323 → 2,326 ({咆|ほう}, {哮|こう}, {墳|ふん})

Total entries: 11,900 → 11,930
Remaining candidates: 270 → 240 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
