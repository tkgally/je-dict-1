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
| Total entries | ~12,290 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~9,491 (open) |
| Candidate words | ~551 |
| Cross-references | ~3,380 |
| Example sentences | ~43,930 |
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

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 282)
Added 30 new dictionary entries (IDs 12205-12234) from candidate_words.json:

- **Nouns - preferences/food (3)**: {好|す}き{嫌|きら}い (likes and dislikes), {好物|こうぶつ} (favorite food), {好意|こうい} (goodwill/romantic interest)
- **Nouns - people/family (4)**: {女将|おかみ} (proprietress), {女神|めがみ} (goddess), {女房|にょうぼう} (wife - informal), {姫|ひめ} (princess)
- **Nouns - politics/society (4)**: {大国|たいこく} (major power), {大多数|だいたすう} (vast majority), {外資系|がいしけい} (foreign-affiliated), {委員会|いいんかい} (committee)
- **Nouns - nature/science (2)**: {大麦|おおむぎ} (barley), {太陽系|たいようけい} (solar system)
- **Nouns - culture (1)**: {妖怪|ようかい} (yokai)
- **Nouns - social issues (2)**: {嫌|いや}がらせ (harassment), {子育|こそだ}て (child-rearing)
- **Nouns/suru verbs (5)**: {奨励|しょうれい} (encouragement), {奪取|だっしゅ} (seizure), {妊娠|にんしん} (pregnancy), {孤立|こりつ} (isolation), {始末|しまつ} (management/outcome)
- **Na-adjectives (3)**: {大人気|だいにんき} (very popular), {好調|こうちょう} (going well), {大|おお}がかり (large-scale)
- **Na-adj/adverb (2)**: {存分|ぞんぶん} (to one's heart's content), {如実|にょじつ} (vividly)
- **Verbs (3)**: {妨|さまた}げる (to hinder - ichidan), {威張|いば}る (to swagger - godan), {嫁|とつ}ぐ (to marry into - godan)

Notable features:
- Multi-sense entries: {好意|こうい} (goodwill/romantic interest), {始末|しまつ} (management/sorry outcome), {姫|ひめ} (princess/small prefix)
- Cultural context: {女将|おかみ} (ryokan hospitality), {妖怪|ようかい} (Japanese folklore), {嫁|とつ}ぐ (patrilocal marriage), {子育|こそだ}て (declining birth rate policy)
- Similar word comparisons: {好調|こうちょう} vs {順調|じゅんちょう}; {好意|こうい} vs {親切|しんせつ}; {好機|こうき} vs {機会|きかい}; {妨|さまた}げる vs {邪魔|じゃま}する
- New kanji: 2,339 → 2,343 ({妊|にん}, {妖|よう}, {姫|ひめ}, {娠|しん})

Total entries: 12,260 → 12,290
Remaining candidates: 581 → 551 (30 removed)

### 2026-02-20 (Vocabulary Expansion - 30 New Entries, Session 281)
Added 30 new dictionary entries (IDs 12175-12204) from candidate_words.json:

- **Verbs - ichidan (3)**: {失|う}せる (to vanish/get lost), {奏|かな}でる (to play music), {大人|おとな}びる (to look mature)
- **Na-adjectives (4)**: {大嫌|だいきら}い (to detest), {大々的|だいだいてき} (large-scale), {多様|たよう} (diverse), {多大|ただい} (enormous)
- **Adverbs (3)**: {夜|よ}な{夜|よ}な (night after night), {大概|たいがい} (generally/enough already), {大方|おおかた} (mostly/probably)
- **Nouns - scale/size (3)**: {大規模|だいきぼ} (large-scale), {大都市|だいとし} (major city), {大金|たいきん} (large sum of money)
- **Nouns - time/history (3)**: {大昔|おおむかし} (ancient times), {天下|てんか} (the realm/supremacy), {大河|たいが} (great river)
- **Nouns - language/society (3)**: {失言|しつげん} (verbal gaffe), {失踪|しっそう} (disappearance), {失格|しっかく} (disqualification)
- **Nouns - events/scale (4)**: {大賞|たいしょう} (grand prize), {大作|たいさく} (major work), {大病|たいびょう} (serious illness), {大惨事|だいさんじ} (catastrophe)
- **Nouns - culture/abstract (4)**: {奉納|ほうのう} (shrine offering), {奈落|ならく} (abyss/theater trap), {奥底|おくそこ} (innermost depths), {多岐|たき} (wide-ranging)
- **Nouns - groups (3)**: {多数派|たすうは} (majority faction), {大地|だいち} (earth/ground)

Notable features:
- Multi-sense entries: {失|う}せる (vanish/rude imperative), {大概|たいがい} (generally/moderation), {大方|おおかた} (mostly/probably), {奈落|ならく} (abyss/theater trap), {天下|てんか} (realm/supremacy), {失格|しっかく} (disqualification/unfit)
- Cultural context: {奈落|ならく} (kabuki stage trap), {天下|てんか} (Sengoku period conquest), {奉納|ほうのう} (shrine offerings), {失格|しっかく} ({人間|にんげん}{失格|しっかく} novel)
- Similar word comparisons: {大々的|だいだいてき} vs {大規模|だいきぼ}; {大概|たいがい} vs だいたい vs {大抵|たいてい}; {大作|たいさく} vs {名作|めいさく} vs {傑作|けっさく}
- New kanji: 2,336 → 2,339 ({奈|な}, {奉|ほう}, {踪|そう})

Total entries: 12,230 → 12,260
Remaining candidates: 487 → 457 (30 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
