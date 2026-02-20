# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-20
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
| Total entries | ~12,140 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,341 (open) |
| Candidate words | ~445 |
| Cross-references | ~3,360 |
| Example sentences | ~43,500 |
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

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 277)
Added 30 new dictionary entries (IDs 12055-12084) from candidate_words.json:

- **Nouns - international/geography (3)**: {各国|かっこく} (each country), {全土|ぜんど} (entire territory), {地形|ちけい} (terrain)
- **Nouns - formal/policy (5)**: {同等|どうとう} (equality), {喫緊|きっきん} (urgent), {名目|めいもく} (nominal/pretext), {参画|さんかく} (participation in planning), {基調|きちょう} (keynote/trend)
- **Nouns - academic/language (3)**: {古語|こご} (archaic word), {和語|わご} (native Japanese word), {受動|じゅどう} (passive)
- **Nouns - social/general (4)**: {同類|どうるい} (same kind), {呼|よ}び{名|な} (designation), {出所|でどころ} (source), {土日|どにち} (weekend)
- **Nouns - specialized (4)**: {合併症|がっぺいしょう} (medical complication), {名勝|めいしょう} (scenic spot), {嗜好|しこう} (taste/preference), {右翼|うよく} (right wing)
- **Nouns/suru verbs (5)**: {入隊|にゅうたい} (enlisting), {合体|がったい} (fusion), {同化|どうか} (assimilation), {同席|どうせき} (being present together), {回帰|かいき} (return/regression)
- **Noun/suru/na-adj (1)**: {堪能|たんのう} (to enjoy fully / proficient)
- **Nouns - historical (1)**: {合戦|かっせん} (battle)
- **Nouns - grammar/formal (2)**: {否|いな} (whether or not / nay), {原形|げんけい} (original form / base form)
- **Verbs - godan (2)**: {取|と}り{去|さ}る (to remove), {取|と}り{払|はら}う (to clear away)

Notable features:
- Multi-sense entries: {合戦|かっせん} (battle/contest), {同類|どうるい} (same type/birds of a feather), {回帰|かいき} (return/regression), {受動|じゅどう} (passivity/passive voice), {右翼|うよく} (politics/sports), {名目|めいもく} (pretext/nominal), {原形|げんけい} (original shape/base form), {否|いな} (whether or not/nay), {堪能|たんのう} (enjoy/proficient), {基調|きちょう} (keynote/trend)
- Similar word comparisons: {同等|どうとう} vs {平等|びょうどう} vs {対等|たいとう}; {名勝|めいしょう} vs {名所|めいしょ}; {参画|さんかく} vs {参加|さんか}; {喫緊|きっきん} vs {緊急|きんきゅう}
- Economics vocabulary: {名目|めいもく}GDP, {名目|めいもく}{賃金|ちんぎん}, {回帰|かいき}{分析|ぶんせき}, {基調|きちょう}

Total entries: 12,110 → 12,140
Remaining candidates: 419 → 445 (30 removed; net count changed due to other additions)

### 2026-02-19 (Vocabulary Expansion - 30 New Entries, Session 276)
Added 30 new dictionary entries (IDs 12025-12054) from candidate_words.json:

- **Verbs - ichidan (2)**: {埋|うも}れる (to be buried/hidden), {入|い}り{乱|みだ}れる (to be jumbled together)
- **Nouns/suru (9)**: {入所|にゅうしょ} (admission to facility), {合成|ごうせい} (synthesis), {同行|どうこう} (accompanying), {同期|どうき} (same cohort/synchronization), {命名|めいめい} (naming), {受理|じゅり} (acceptance of documents), {圧倒|あっとう} (overwhelming), {出店|しゅってん} (opening a shop), {在住|ざいじゅう} (residing in)
- **Nouns - geography/land (5)**: {全域|ぜんいき} (entire area), {国土|こくど} (national territory), {土壌|どじょう} (soil), {土手|どて} (embankment), {地下室|ちかしつ} (basement)
- **Nouns - culture/society (5)**: {和風|わふう} (Japanese-style), {土足|どそく} (with shoes on), {地主|じぬし} (landowner), {地獄|じごく} (hell), {各位|かくい} (formal address: everyone)
- **Nouns - language/academic (3)**: {名称|めいしょう} (name/designation), {口語|こうご} (spoken language), {史実|しじつ} (historical fact)
- **Nouns - general (4)**: {国連|こくれん} (United Nations), {回路|かいろ} (circuit), {囲|かこ}い (enclosure), {命取|いのちと}り (fatal mistake)
- **Noun/na-adjective (1)**: {均一|きんいつ} (uniform/flat-rate)
- **Noun/suffix (1)**: {向|む}き (direction/suited for)

Notable features:
- Multi-sense entries: {同期|どうき} (cohort/synchronization), {土壌|どじょう} (soil/breeding ground), {向|む}き (direction/suitability), {出店|しゅってん} (opening store/setting up stall), {均一|きんいつ} (uniform/flat-rate), {地獄|じごく} (Buddhist hell/terrible situation), {埋|うも}れる (buried/hidden)
- Cultural context: {土足|どそく} (shoe etiquette), {和風|わふう} (Japanese vs Western style), {地獄|じごく} (Buddhist cosmology, idioms), {各位|かくい} (business etiquette), {地主|じぬし} (land reform history), {命名|めいめい} (baby naming ceremony)
- New kanji: 2,331 → 2,332 ({獄|ごく})

Total entries: 12,080 → 12,110
Remaining candidates: 448 → 419 (29 removed)

### 2026-02-19 (Vocabulary Expansion - 30 New Entries, Session 275)
Added 30 new dictionary entries (IDs 11995-12024) from candidate_words.json:

- **Verbs - godan (7)**: {哀|あわ}れむ (to pity), {取|と}り{交|か}わす (to exchange documents), {取|と}り{合|あ}う (to compete for), {吸|す}い{取|と}る (to absorb), {合|あ}わさる (to come together), {囲|かこ}う (to enclose), {図|はか}る (to plan/aim for)
- **Verbs - ichidan (3)**: {噛|か}みしめる (to chew/savor), {名付|なづ}ける (to name), {問|と}いかける (to pose a question)
- **Verbs - suru (1)**: {呈|てい}する (to present/exhibit)
- **I-adjective (1)**: {喜|よろこ}ばしい (delightful)
- **Nouns - body/health (1)**: {咳|せき} (cough)
- **Nouns - culture/traditional (3)**: {囲炉裏|いろり} (sunken hearth), {土俵|どひょう} (sumo ring), {嗜|たしな}み (refinement)
- **Nouns - politics/economics (5)**: {圧力|あつりょく} (pressure), {国交|こっこう} (diplomatic relations), {国債|こくさい} (government bond), {国産|こくさん} (domestic production), {困窮|こんきゅう} (poverty)
- **Nouns - evaluation/abstract (4)**: {圧巻|あっかん} (highlight), {圧迫|あっぱく} (pressure/oppression), {合致|がっち} (agreement), {固執|こしつ} (obstinacy)
- **Nouns - general (4)**: {吸血鬼|きゅうけつき} (vampire), {商標|しょうひょう} (trademark), {回顧|かいこ} (retrospection), {図面|ずめん} (blueprint)
- **Nature (1)**: {団栗|どんぐり} (acorn)

Notable features:
- Multi-sense entries: {噛|か}みしめる (chew/savor), {取|と}り{合|あ}う (compete/pay attention), {吸|す}い{取|と}る (absorb/exploit), {囲|かこ}う (enclose/keep), {図|はか}る (plan/aim for), {呈|てい}する (present/exhibit), {圧迫|あっぱく} (physical/figurative), {圧力|あつりょく} (physical/political), {土俵|どひょう} (sumo ring/arena), {嗜|たしな}み (refinement/propriety)
- Cultural context: {囲炉裏|いろり} (traditional hearth), {土俵|どひょう} (sumo culture), {嗜|たしな}み (cultural accomplishments), {団栗|どんぐり} (どんぐりの{背比|せくら}べ idiom)
- Homophone cross-references: {図|はか}る ↔ {測|はか}る, {国債|こくさい} ↔ {国際|こくさい}, {回顧|かいこ} ↔ {解雇|かいこ}
- New kanji: 2,329 → 2,331 ({俵|ひょう}, {嗜|し})

Total entries: 12,050 → 12,080
Remaining candidates: 478 → 448 (30 removed)

### 2026-02-19 (Vocabulary Expansion - 30 New Entries, Session 274)
Added 30 new dictionary entries (IDs 11965-11994) from candidate_words.json:

- **Verbs - godan (3)**: {厭|いと}う (to dislike/shun), {反|そ}る (to bend backward/warp), {取|と}り{憑|つ}く (to possess/haunt)
- **Verbs - ichidan (1)**: {取|と}りやめる (to cancel)
- **Verbs - suru (4)**: {反|はん}する (to contradict/violate), {博|はく}する (to win/gain), {即|そく}する (to conform to), {口|くち}ごたえする (to talk back)
- **Nouns/suru - formal (5)**: {入団|にゅうだん} (joining a team), {即死|そくし} (instant death), {即位|そくい} (enthronement), {参戦|さんせん} (entering a war), {出展|しゅってん} (exhibiting)
- **Nouns - food (2)**: {卵白|らんぱく} (egg white), {卵黄|らんおう} (egg yolk)
- **Nouns - geography/direction (2)**: {原野|げんや} (wilderness), {南方|なんぽう} (the south)
- **Nouns - abstract/formal (3)**: {原型|げんけい} (prototype), {原案|げんあん} (draft proposal), {利上|りあ}げ (interest rate hike)
- **Nouns - culture (4)**: {参道|さんどう} (approach to shrine), {反旗|はんき} (flag of rebellion), {厄|やく} (misfortune/unlucky age), {八百万|やおよろず} (myriad gods)
- **Nouns - general (4)**: {双眼鏡|そうがんきょう} (binoculars), {出禁|できん} (banned from entry), {単品|たんぴん} (single item/a la carte), {公|おおやけ} (public/official)
- **Noun/adjective (1)**: {単一|たんいつ} (single/uniform)
- **Expression (1)**: {右往左往|うおうさおう} (running about in confusion)

Notable features:
- Multi-sense entries: {反|はん}する (contradict/violate), {反|そ}る (arch back/warp), {取|と}り{憑|つ}く (possess/obsessed), {厄|やく} (misfortune/unlucky age), {原案|げんあん} (draft/original concept), {参戦|さんせん} (war/competition)
- Cultural context: {厄|やく} ({厄年|やくどし} ages), {八百万|やおよろず} (Shinto animism), {参道|さんどう} ({表参道|おもてさんどう}), {即位|そくい} (Emperor's enthronement ceremony)
- Homophone cross-references: {反|そ}る ↔ {剃|そ}る, {出展|しゅってん} ↔ {出典|しゅってん}
- New kanji: 2,328 → 2,329 ({厭|えん})

Total entries: 12,020 → 12,050
Remaining candidates: 508 → 478 (30 removed)

### 2026-02-19 (Vocabulary Expansion - 30 New Entries, Session 273)
Added 30 new dictionary entries (IDs 11935-11964) from candidate_words.json:

- **Nouns - food/cooking (2)**: {半熟|はんじゅく} (soft-boiled), {厨房|ちゅうぼう} (professional kitchen)
- **Nouns - geography/history (2)**: {南極|なんきょく} (South Pole), {史跡|しせき} (historic site)
- **Nouns - nuclear/military (3)**: {原爆|げんばく} (atomic bomb), {原発|げんぱつ} (nuclear power plant), {反撃|はんげき} (counterattack)
- **Nouns/suru - formal/abstract (7)**: {即答|そくとう} (immediate reply), {反転|はんてん} (reversal), {取得|しゅとく} (acquisition), {受容|じゅよう} (acceptance), {召集|しょうしゅう} (convocation), {否認|ひにん} (denial), {君臨|くんりん} (reigning)
- **Nouns - culture/language (5)**: {単行本|たんこうぼん} (standalone book/tankoubon), {博打|ばくち} (gambling), {合言葉|あいことば} (password/motto), {名門|めいもん} (prestigious institution), {号令|ごうれい} (command/signal)
- **Nouns - general (2)**: {同情|どうじょう} (sympathy), {各種|かくしゅ} (various kinds)
- **I-adjectives (2)**: {口寂|くちさび}しい (wanting to snack), {名高|なだか}い (renowned)
- **Verbs - godan (4)**: {取|と}り{仕切|しき}る (to manage), {司|つかさど}る (to govern), {吹|ふ}き{込|こ}む (to blow into/instill), {叩|たた}き{出|だ}す (to drive out/produce a result)
- **Verbs - ichidan (3)**: {千切|ちぎ}れる (to be torn apart), {古|ふる}びる (to become old), {呼|よ}び{寄|よ}せる (to summon)

Notable features:
- Multi-sense entries: {半熟|はんじゅく} (cooking/ripeness), {博打|ばくち} (gambling/risky venture), {合言葉|あいことば} (password/motto), {名門|めいもん} (family/institution), {吹|ふ}き{込|こ}む (blow in/instill/record), {叩|たた}き{出|だ}す (expel/achieve)
- Cultural context: {口寂|くちさび}しい (uniquely Japanese concept), {号令|ごうれい} (Japanese classroom routine), {単行本|たんこうぼん} (manga culture), {博打|ばくち} (Edo-period gambling)
- Homophone note: {受容|じゅよう} vs {需要|じゅよう}, {反転|はんてん} vs {斑点|はんてん}
- New kanji: 2,327 → 2,328 ({厨|ちゅう})

Total entries: 11,990 → 12,020
Remaining candidates: 538 → 508 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
