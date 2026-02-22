# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-22
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
| Total entries | ~12,815 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,016 (open) |
| Candidate words | ~417 |
| Cross-references | ~3,380 |
| Example sentences | ~45,150 |
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

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 299)
Added 30 new dictionary entries (IDs 12739-12768) from candidate_words.json:

- **Godan verbs (2)**: {手渡|てわた}す (to hand over), {打|う}ち{勝|か}つ (to overcome)
- **Ichidan verb (1)**: {手|て}がける (to handle/work on)
- **I-adjective (1)**: {憎|にく}い (hateful/admirable)
- **Na-adjective (1)**: {意外|いがい} (unexpected/surprising)
- **Nouns - emotion/thought (3)**: {情感|じょうかん} (emotion/pathos), {念|ねん} (thought/caution), {感触|かんしょく} (feel/touch/impression)
- **Nouns - hand/manual (8)**: {手|て}すり (handrail), {手|て}ぶら (empty-handed), {手口|てぐち} (modus operandi), {手触|てざわ}り (texture), {手引|てび}き (guidance/handbook), {手料理|てりょうり} (home cooking), {手洗|てあら}い (handwashing/washroom), {手作業|てさぎょう} (manual work)
- **Nouns - ownership/affiliation (3)**: {所属|しょぞく} (affiliation), {所持|しょじ} (possession), {所有|しょゆう} (ownership)
- **Nouns - war/military (3)**: {戦場|せんじょう} (battlefield), {戦士|せんし} (warrior), {戦術|せんじゅつ} (tactics)
- **Nouns - other (8)**: {情勢|じょうせい} (situation), {意思|いし} (intention/will), {成|な}り{立|た}ち (formation/origin), {手法|しゅほう} (technique), {徳用|とくよう} (economy size), {心霊|しんれい} (supernatural), {当主|とうしゅ} (head of household), {所在|しょざい} (whereabouts)

Notable features:
- Multi-sense entries: {憎|にく}い (hateful/ironic praise), {感触|かんしょく} (physical/figurative), {手引|てび}き (guidance/handbook), {手洗|てあら}い (handwashing/restroom), {念|ねん} (thought/caution), {成|な}り{立|た}ち (origin/structure), {手|て}がける (work on/raise)
- Cross-references: {意外|いがい}↔{以外|いがい}, {意思|いし}↔{意志|いし}, {憎|にく}い↔〜にくい, {当主|とうしゅ}↔{投手|とうしゅ}, {念|ねん}↔{年|ねん}
- Strong 手-compound cluster: 8 entries built around {手|て}
- Good mix of everyday ({手|て}ぶら, {手洗|てあら}い) and formal vocabulary ({所有|しょゆう}, {情勢|じょうせい})

Total entries: 12,785 → 12,815 (approximate)
Remaining candidates: 447 → 417 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 298)
Added 30 new dictionary entries (IDs 12700-12729) from candidate_words.json:

- **Godan verbs (4)**: {操|あやつ}る (to manipulate/operate), {挑|いど}む (to challenge), {撒|ま}く (to scatter/sprinkle), {散|ち}らばる (to be scattered)
- **Ichidan verbs (2)**: {損|そこ}ねる (to harm/fail to do), {敗|やぶ}れる (to be defeated)
- **I-adjective (1)**: {拙|つたな}い (unskillful/clumsy)
- **Na-adjective (1)**: {性急|せいきゅう} (hasty/impatient)
- **Adverbs (2)**: {断固|だんこ} (firmly/resolutely), {断然|だんぜん} (definitely/by far)
- **Nouns - emotion/abstract (3)**: {心情|しんじょう} (feelings/sentiments), {快感|かいかん} (pleasant sensation), {挙句|あげく} (in the end)
- **Nouns - time/season (3)**: {旬|しゅん} (in season/peak), {放課後|ほうかご} (after school), {新緑|しんりょく} (fresh green foliage)
- **Nouns - culture/language (4)**: {昔話|むかしばなし} (folktale), {教訓|きょうくん} (lesson/moral), {文脈|ぶんみゃく} (context), {数々|かずかず} (many/numerous)
- **Nouns - body/object (3)**: {指先|ゆびさき} (fingertip), {指紋|しもん} (fingerprint), {斧|おの} (axe)
- **Nouns - food (1)**: {明太子|めんたいこ} (spicy pollock roe)
- **Nouns - person (1)**: {旅人|たびびと} (traveler)
- **Nouns - other (5)**: {御託|ごたく} (tedious excuses), {往生|おうじょう} (passing away/being stuck), {掟|おきて} (rule/code), {早|はや}とちり (jumping to conclusions), {時代遅|じだいおく}れ (outdated)

Notable features:
- Multi-sense entries: {操|あやつ}る (skillful handling/manipulation), {往生|おうじょう} (death/being stuck), {損|そこ}ねる (harm/fail to do), {撒|ま}く (scatter/shake off), {断然|だんぜん} (by far/resolutely), {旬|しゅん} (food season/peak popularity), {昔話|むかしばなし} (folktale/reminiscence)
- Diverse word types: godan verbs, ichidan verbs, adjectives (i/na), adverbs, nouns, suru verbs
- Cultural depth: {旬|しゅん} (seasonal food culture), {昔話|むかしばなし} (oral tradition), {明太子|めんたいこ} (Hakata specialty), {掟|おきて} (traditional codes)
- New kanji: 2,371 → 2,373 ({掟|てい}, {斧|ふ})

Total entries: 12,755 → 12,785
Remaining candidates: 375 → 345 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 297)
Added 30 new dictionary entries (IDs 12670-12699) from candidate_words.json:

- **Ichidan verbs (2)**: {忍|しの}ばせる (to hide/conceal), {戯|たわむ}れる (to play/frolic/flirt)
- **Godan verb (1)**: {惚|ほ}れ{込|こ}む (to fall deeply in love with)
- **I-adjective (1)**: {愛|あい}らしい (lovely/charming)
- **Na-adjective (1)**: {微細|びさい} (minute/fine/microscopic)
- **Taru-adjective/adverb (1)**: {意気揚々|いきようよう} (in high spirits/triumphant)
- **Noun/suru verbs (7)**: {急増|きゅうぞう} (rapid increase), {悪用|あくよう} (misuse), {応答|おうとう} (response), {懇願|こんがん} (entreaty), {成就|じょうじゅ} (fulfillment), {急変|きゅうへん} (sudden change), {愛用|あいよう} (regular use)
- **Nouns - emotion/personality (3)**: {憂|うれ}い (sorrow/grief), {感受性|かんじゅせい} (sensitivity), {愛想|あいそ} (friendliness)
- **Nouns - reputation/naming (2)**: {悪名|あくめい} (infamy), {愛称|あいしょう} (pet name/nickname)
- **Nouns - society/law (3)**: {慣例|かんれい} (custom/convention), {戸籍|こせき} (family register), {必然性|ひつぜんせい} (necessity/inevitability)
- **Nouns - scene/spectacle (2)**: {情景|じょうけい} (scene/spectacle), {惨状|さんじょう} (disastrous scene)
- **Nouns - person/role (2)**: {悪党|あくとう} (villain/scoundrel), {悪役|あくやく} (villain role)
- **Nouns - other (5)**: {悪寒|おかん} (chills), {悪口|わるぐち} (insult/bad-mouthing), {怪物|かいぶつ} (monster), {意匠|いしょう} (design/artistic conception), {心持|こころも}ち (feeling/slightly)

Notable features:
- Multi-sense entries: {怪物|かいぶつ} (monster/extraordinary person), {憂|うれ}い (sorrow/worry), {戯|たわむ}れる (frolic/flirt), {愛想|あいそ} (friendliness/patience), {心持|こころも}ち (feeling/slightly)
- Diverse word types: ichidan verbs, godan verb, adjectives (i/na/taru), suru verbs, nouns, adverb
- Cultural context: {戸籍|こせき} (Japanese family register system), {成就|じょうじゅ} (shrine prayers), {意匠|いしょう} (design law)
- New kanji: 2,370 → 2,371 ({懇|こん})

Total entries: 12,725 → 12,755
Remaining candidates: 405 → 375 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 296)
Added 30 new dictionary entries (IDs 12640-12669) from candidate_words.json:

- **Pre-noun adjectival (1)**: {幾多|いくた} (many/numerous - literary)
- **Noun/suru verbs (2)**: {女装|じょそう} (cross-dressing), {志願|しがん} (volunteering/application)
- **Noun/adjective-no (1)**: {多国籍|たこくせき} (multinational)
- **Nouns - technical/academic (4)**: {座標|ざひょう} (coordinates), {微生物|びせいぶつ} (microorganism), {心理学|しんりがく} (psychology), {建材|けんざい} (building materials)
- **Nouns - history/culture (10)**: {平安|へいあん} (Heian era/peace), {宰相|さいしょう} (prime minister - literary), {宮中|きゅうちゅう} (imperial court), {宮司|ぐうじ} (Shinto chief priest), {家臣|かしん} (retainer), {家老|かろう} (chief retainer), {奉行|ぶぎょう} (magistrate), {公家|くげ} (court noble), {士族|しぞく} (former samurai class), {人間国宝|にんげんこくほう} (Living National Treasure)
- **Nouns - society/geography (5)**: {外需|がいじゅ} (external demand), {官民|かんみん} (public-private), {山地|さんち} (mountainous area), {女中|じょちゅう} (maid - archaic), {大佐|たいさ} (colonel)
- **Nouns - general (5)**: {寺社|じしゃ} (temples and shrines), {宙|ちゅう} (midair/space), {女形|おんながた} (onnagata actor), {大関|おおぜき} (ōzeki sumo rank), {思春期|ししゅんき} (puberty/adolescence)
- **Nouns - abstract (2)**: {悪循環|あくじゅんかん} (vicious cycle), {多神教|たしんきょう} (polytheism)

Notable features:
- Multi-sense entries: {平安|へいあん} (peace/Heian era), {宙|ちゅう} (midair/space)
- Strong Japanese history/culture cluster: {公家|くげ}, {家臣|かしん}, {家老|かろう}, {奉行|ぶぎょう}, {宰相|さいしょう}, {士族|しぞく}, {宮中|きゅうちゅう}, {宮司|ぐうじ}
- Cultural depth: {女形|おんながた} (kabuki tradition), {大関|おおぜき} (sumo ranking), {人間国宝|にんげんこくほう} (cultural preservation)
- New kanji: 2,368 → 2,370 ({佐|さ}, {宰|さい})

Total entries: 12,695 → 12,725
Remaining candidates: 435 → 405 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 295)
Added 30 new dictionary entries (IDs 12610-12639) from candidate_words.json:

- **Godan verbs (2)**: {悼|いた}む (to mourn/grieve), {憤|いきどおる} (to be indignant)
- **Ichidan verbs (3)**: {恵|めぐ}まれる (to be blessed with), {愛|め}でる (to admire beauty), {成|な}し{遂|と}げる (to accomplish)
- **Godan verb (1)**: {慈|いつく}しむ (to cherish tenderly)
- **I-adjective (1)**: {愛|いと}おしい (dear/lovable/precious)
- **Na-adjective (1)**: {悲惨|ひさん} (miserable/tragic)
- **Adverb (1)**: {幾度|いくど} (many times - literary)
- **Pronoun (1)**: {当方|とうほう} (we/our side - formal)
- **Nouns - emotion/abstract (5)**: {憧|あこが}れ (longing/yearning), {感性|かんせい} (sensibility), {恋愛|れんあい} (romantic love), {恥|はじ} (shame), {悪夢|あくむ} (nightmare)
- **Nouns - communication (3)**: {悲鳴|ひめい} (scream), {応酬|おうしゅう} (exchange of arguments), {後援|こうえん} (sponsorship)
- **Nouns - cognitive (3)**: {想定|そうてい} (assumption), {意向|いこう} (intention), {意図|いと} (aim/purpose)
- **Nouns - cultural (4)**: {彼岸|ひがん} (equinox/the other shore), {山門|さんもん} (temple gate), {懐石|かいせき} (kaiseki cuisine), {心中|しんじゅう} (double suicide)
- **Nouns - other (5)**: {役人|やくにん} (government official), {引|ひ}き{換|か}え (exchange), {懐|ふところ} (bosom/purse), {成熟|せいじゅく} (maturity), {戦闘|せんとう} (combat)

Notable features:
- Multi-sense entries: {引|ひ}き{換|か}え (exchange/in return for), {彼岸|ひがん} (equinox/Buddhist concept), {懐|ふところ} (bosom/finances)
- Cultural depth: {彼岸|ひがん} (equinox customs, Buddhist philosophy), {懐石|かいせき} (tea ceremony origins), {心中|しんじゅう} (Chikamatsu plays), {恥|はじ} (shame culture), {山門|さんもん} (Buddhist architecture)
- Strong emotion/psychology cluster: {愛|いと}おしい, {慈|いつく}しむ, {愛|め}でる, {憧|あこが}れ, {憤|いきどお}る, {悼|いた}む
- New kanji: 2,367 → 2,368 ({悼|とう})

Total entries: 12,665 → 12,695
Remaining candidates: 465 → 435 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
