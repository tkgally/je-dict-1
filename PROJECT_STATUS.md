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
| Total entries | ~12,230 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,431 (open) |
| Candidate words | ~487 |
| Cross-references | ~3,370 |
| Example sentences | ~43,700 |
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

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 280)
Added 30 new dictionary entries (IDs 12145-12174) from candidate_words.json:

- **Nouns - building/surface (2)**: {壁面|へきめん} (wall surface), {外観|がいかん} (outward appearance)
- **Nouns - communication (2)**: {声|こえ}かけ (calling out to someone), {声楽|せいがく} (vocal music)
- **Nouns - media/culture (3)**: {外伝|がいでん} (side story/spin-off), {夜桜|よざくら} (cherry blossoms at night), {大福|だいふく} (daifuku mochi)
- **Nouns - medical/body (2)**: {外傷|がいしょう} (external wound), {声帯|せいたい} (vocal cords)
- **Nouns - business/economics (4)**: {外貨|がいか} (foreign currency), {外注|がいちゅう} (outsourcing), {増産|ぞうさん} (increased production), {大手|おおて} (major company)
- **Nouns - general (6)**: {境界線|きょうかいせん} (boundary line), {売|う}り (selling point), {凡|ぼん}ミス (careless mistake), {団長|だんちょう} (group leader), {塩抜|しおぬ}き (desalting), {外面|がいめん} (outward appearance)
- **Nouns - time (3)**: {夜更|よふ}け (late at night), {夜通|よどお}し (all night long), {大砲|たいほう} (cannon)
- **Nouns/suru verbs (3)**: {変質|へんしつ} (change in quality), {増進|ぞうしん} (promotion/enhancement), {天使|てんし} (angel)
- **Na-adjectives (3)**: {壮麗|そうれい} (magnificent), {多彩|たさい} (colorful/diverse), {多忙|たぼう} (very busy)
- **Na-adjective/adverb (1)**: {大幅|おおはば} (significant/drastic)

Notable features:
- Multi-sense entries: {外伝|がいでん} (spin-off/supplementary biography), {売|う}り (selling point/selling), {外面|がいめん} (outer surface/public face), {大手|おおて} (major company/castle gate), {大砲|たいほう} (cannon/power hitter)
- Cultural context: {夜桜|よざくら} (nighttime cherry blossom viewing tradition), {大福|だいふく} (traditional Japanese sweet), {塩抜|しおぬ}き (Japanese cooking technique)
- Similar word comparisons: {壮麗|そうれい} vs {壮大|そうだい} vs {華麗|かれい}; {多忙|たぼう} vs {忙|いそが}しい vs {繁忙|はんぼう}; {多彩|たさい} vs {多様|たよう}

Total entries: 12,200 → 12,230
Remaining candidates: 517 → 487 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 279)
Added 30 new dictionary entries (IDs 12115-12144) from candidate_words.json:

- **Nouns/suru - change/transformation (4)**: {変容|へんよう} (transformation), {変異|へんい} (mutation), {変貌|へんぼう} (transfiguration), {増殖|ぞうしょく} (proliferation)
- **Nouns - politics/governance (4)**: {国政|こくせい} (national politics), {国益|こくえき} (national interest), {国賓|こくひん} (state guest), {圧政|あっせい} (tyranny)
- **Nouns - geography/earth (5)**: {地中|ちちゅう} (underground), {地価|ちか} (land price), {地殻|ちかく} (earth's crust), {土地柄|とちがら} (local character), {地|じ}べた (bare ground)
- **Nouns - employment/office (3)**: {在職|ざいしょく} (being in office), {在留|ざいりゅう} (residing abroad), {在位|ざいい} (reign)
- **Nouns - business/finance (3)**: {売却|ばいきゃく} (selling off assets), {取締役|とりしまりやく} (company director), {増額|ぞうがく} (increase in amount)
- **Nouns - food (2)**: {塩水|しおみず} (salt water), {塩焼|しおや}き (salt-grilling)
- **Nouns - naming/designation (2)**: {呼|よ}び{方|かた} (way of calling), {呼称|こしょう} (designation)
- **Nouns - general (5)**: {変|か}わり{目|め} (turning point), {境地|きょうち} (state of mind), {回忌|かいき} (death anniversary), {国民性|こくみんせい} (national character), {固形|こけい} (solid form)
- **Nouns - science/technical (2)**: {塩素|えんそ} (chlorine), {増幅|ぞうふく} (amplification)

Notable features:
- Multi-sense entry: {境地|きょうち} (state of mind / level of attainment)
- Related word groups: transformation trio ({変容|へんよう}/{変異|へんい}/{変貌|へんぼう}), 在- compounds ({在職|ざいしょく}/{在留|ざいりゅう}/{在位|ざいい}), naming pair ({呼|よ}び{方|かた}/{呼称|こしょう})
- Homophone cross-references: {地価|ちか} ↔ {地下|ちか}, {地殻|ちかく} ↔ {近|ちか}く
- New kanji: 2,334 → 2,336 ({貌|ぼう}, {賓|ひん})

Total entries: 12,170 → 12,200
Remaining candidates: 547 → 517 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 278)
Added 30 new dictionary entries (IDs 12085-12114) from candidate_words.json:

- **Verbs - ichidan (3)**: {取|と}り{換|か}える (to replace/exchange), {耐|た}える (to endure/withstand), {報|むく}いる (to reward/retaliate)
- **Verb - godan (1)**: {塞|ふさ}ぎ{込|こ}む (to become depressed/brood)
- **I-adjective (1)**: {固|かた}い (firm/solid/stiff)
- **Na-adjective/noun (1)**: {壮絶|そうぜつ} (fierce/intense)
- **Nouns/suru verbs (7)**: {変換|へんかん} (conversion), {増税|ぞうぜい} (tax increase), {壊滅|かいめつ} (devastation), {変装|へんそう} (disguise), {変身|へんしん} (transformation), {変革|へんかく} (reform), {団|だん}らん (family gathering)
- **Nouns - culture/place (3)**: {境内|けいだい} (temple/shrine grounds), {城下町|じょうかまち} (castle town), {声優|せいゆう} (voice actor)
- **Nouns - abstract/formal (5)**: {報酬|ほうしゅう} (remuneration), {境界|きょうかい} (boundary), {境遇|きょうぐう} (circumstances), {変人|へんじん} (eccentric), {外見|がいけん} (outward appearance)
- **Nouns - language/society (3)**: {外来語|がいらいご} (loanword), {報連相|ほうれんそう} (report-contact-consult), {売|う}れっ{子|こ} (popular person)
- **Nouns - nature/general (6)**: {夏季|かき} (summer season), {塩味|しおあじ} (salty taste), {塵|ちり} (dust), {地上|ちじょう} (above ground), {埋|う}め{立|た}て (land reclamation), {執事|しつじ} (butler)

Notable features:
- Multi-sense entries: {耐|た}える (endure/withstand), {報|むく}いる (reward/retaliate), {固|かた}い (firm/stiff)
- Cultural context: {報連相|ほうれんそう} (workplace communication norm), {声優|せいゆう} (voice acting industry), {城下町|じょうかまち} (feudal castle towns), {執事|しつじ} (butler cafes)
- Homophone cross-references: {変装|へんそう} ↔ {返送|へんそう}, {固|かた}い ↔ {硬|かた}い
- New kanji: 2,332 → 2,334 ({遇|ぐう}, {酬|しゅう})

Total entries: 12,140 → 12,170
Remaining candidates: 445 → 415 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
