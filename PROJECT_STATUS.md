# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-08
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
| Total entries | ~10,581 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~7,782 (open) |
| Candidate words | ~208 |
| Cross-references | ~3,320 |
| Example sentences | ~41,000 |
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

### 2026-02-08 (Vocabulary Expansion - 30 New Entries, Session 227)
Added 30 new dictionary entries (IDs 10575-10604) from candidate_words.json:

- **Nouns (18)**: {証拠|しょうこ} (evidence), {起訴|きそ} (indictment), {和解|わかい} (reconciliation/settlement), {弁護|べんご} (defense), {点滴|てんてき} (IV drip), {麻酔|ますい} (anesthesia), {版画|はんが} (printmaking), {織物|おりもの} (textile), {秩序|ちつじょ} (order), {逆説|ぎゃくせつ} (paradox), {心境|しんきょう} (state of mind), {胸騒|むなさわ}ぎ (foreboding), {仕返|しかえ}し (retaliation), {出来心|できごころ} (sudden impulse), {修羅場|しゅらば} (carnage/confrontation), {権限|けんげん} (authority), お{裾分|すそわ}け (sharing gifts), {機転|きてん} (quick wit), {所作|しょさ} (demeanor)
- **Verbs (6)**: {付|つ}き{添|そ}う (to accompany), {噛|か}み{合|あ}う (to mesh), {寄|よ}り{添|そ}う (to stay close), {入|い}り{浸|びた}る (to frequent), {投|な}げ{出|だ}す (to give up), そそのかす (to instigate)
- **I-adjectives (3)**: {何気|なにげ}ない (casual), {初々|ういうい}しい (fresh/innocent), {目|め}まぐるしい (dizzying)
- **Noun + suru verbs (1)**: {赴任|ふにん} (taking up a new post)
- **Noun (cultural)**: {漆|うるし} (lacquer/lacquerware)

Notable features:
- Multi-sense entries: {和解|わかい} (reconciliation/legal settlement), {漆|うるし} (lacquer/lacquerware), {噛|か}み{合|あ}う (mesh/in sync), {投|な}げ{出|だ}す (stretch out/give up), {修羅場|しゅらば} (battle/confrontation), {寄|よ}り{添|そ}う (physical/emotional)
- Legal vocabulary cluster: {証拠|しょうこ}, {起訴|きそ}, {和解|わかい}, {弁護|べんご}
- Medical vocabulary: {点滴|てんてき}, {麻酔|ますい}
- Cultural context: {漆|うるし} (lacquerware tradition), お{裾分|すそわ}け (sharing custom), {修羅場|しゅらば} (Buddhist origin), {所作|しょさ} (tea ceremony)
- Cross-references: {起訴|きそ}↔{弁護|べんご}, {付|つ}き{添|そ}う↔{寄|よ}り{添|そ}う

Total entries: 10,551 → 10,581
Remaining candidates: 238 → 208
New kanji: 2,267 → 2,270 ({漆|しつ}, {秩|ちつ}, {赴|ふ})

### 2026-02-08 (Vocabulary Expansion - 31 New Entries, Session 226)
Added 31 new dictionary entries (IDs 10544-10574) from candidate_words.json:

- **Verbs (7)**: ひっくり{返|かえ}る (to topple over), もたらす (to bring about), {真似|まね}る (to imitate), {免|まぬが}れる (to escape), {纏|まつ}わる (to be associated with), {纏|まと}う (to be clad in)
- **Nouns (20)**: {屋台|やたい} (food stall), {猫舌|ねこじた} (can't handle hot food), {朝飯前|あさめしまえ} (a piece of cake), {正座|せいざ} (formal sitting), {波紋|はもん} (ripple), {瀬戸際|せとぎわ} (brink), {土壇場|どたんば} (last moment), {先手|せんて} (initiative), {後手|ごて} (reactive position), {転売|てんばい} (resale), {内訳|うちわけ} (breakdown), {余韻|よいん} (afterglow), {感銘|かんめい} (deep impression), {手柄|てがら} (feat), {手本|てほん} (model), {手探|てさぐ}り (trial and error), {見通|みとお}し (outlook), {実態|じったい} (actual conditions), {名誉|めいよ} (honor), {奥行|おくゆ}き (depth), {貫禄|かんろく} (gravitas), {掛|か}け{声|ごえ} (rallying cry), {抹茶|まっちゃ} (matcha)
- **Adverb (1)**: {丸|まる}ごと (whole, entirely)
- **Na-adjective (1)**: {場違|ばちが}い (out of place)

Notable features:
- Multi-sense entries: ひっくり{返|かえ}る (physical/figurative), {屋台|やたい} (food stall/festival float), {波紋|はもん} (ripple/repercussions), {先手|せんて}/{後手|ごて} (strategy/board games), {手探|てさぐ}り (physical/figurative), {見通|みとお}し (forecast/visibility), {余韻|よいん} (sound/impression), {纏|まつ}わる (associated/cling)
- Cross-references: {先手|せんて}↔{後手|ごて} (antonym pair), {土壇場|どたんば}→{瀬戸際|せとぎわ}, {纏|まと}う→{纏|まつ}わる
- Cultural vocabulary: {屋台|やたい} (Fukuoka food stalls), {猫舌|ねこじた}, {正座|せいざ}, {抹茶|まっちゃ} (tea ceremony)
- Strategy/business: {先手|せんて}, {後手|ごて}, {転売|てんばい}, {内訳|うちわけ}, {見通|みとお}し, {実態|じったい}

Total entries: 10,520 → 10,551
Remaining candidates: 269 → 238
New kanji: 2,263 → 2,267 ({瀬|せ}, {禄|ろく}, {誉|よ}, {韻|いん})

### 2026-02-08 (New Candidate Words - 90 Words Added)
Added 90 new candidate words to candidate_words.json across 15+ domains, using diverse search strategies:

- **Legal/Justice (4)**: {証拠|しょうこ}, {起訴|きそ}, {和解|わかい}, {弁護|べんご}
- **Medical (2)**: {点滴|てんてき}, {麻酔|ますい}
- **Arts/Crafts (3)**: {版画|はんが}, {織物|おりもの}, {漆|うるし}
- **Compound Verbs (6)**: {付|つ}き{添|そ}う, {噛|か}み{合|あ}う, {寄|よ}り{添|そ}う, {入|い}り{浸|びた}る, {投|な}げ{出|だ}す, そそのかす
- **Abstract/Academic (5)**: {実態|じったい}, {見通|みとお}し, {秩序|ちつじょ}, {逆説|ぎゃくせつ}, {偏差|へんさ}
- **Emotional/Aesthetic (4)**: {余韻|よいん}, {心境|しんきょう}, {感銘|かんめい}, {胸騒|むなさわ}ぎ
- **Adjectives (7)**: {何気|なにげ}ない, {初々|ういうい}しい, {目|め}まぐるしい, {晴|は}れ{晴|ば}れしい, {神々|こうごう}しい, おっかない, {気味悪|きみわる}い
- **Dramatic/Critical (3)**: {瀬戸際|せとぎわ}, {土壇場|どたんば}, {修羅場|しゅらば}
- **Social/Interpersonal (10)**: {場違|ばちが}い, {仕返|しかえ}し, {出来心|できごころ}, {素振|そぶ}り, {嫌気|いやけ}, {暇潰|ひまつぶ}し, {顔合|かおあ}わせ, {水際|みずぎわ}, {境目|さかいめ}, {口添|くちぞ}え
- **Strategy (2)**: {先手|せんて}, {後手|ごて}
- **Business/Admin (6)**: {転売|てんばい}, {権限|けんげん}, {内訳|うちわけ}, {赴任|ふにん}, {名義|めいぎ}, {便宜|べんぎ}
- **Cultural/Traditional (8)**: お{裾分|すそわ}け, {引|ひ}き{出物|でもの}, {正座|せいざ}, {屋台|やたい}, {紙芝居|かみしばい}, {縁日|えんにち}, {肝試|きもだめ}し, {茶|ちゃ}の{間|ま}
- **Religion/Spiritual (3)**: {参拝|さんぱい}, {巡礼|じゅんれい}, {墓参|はかまい}り
- **Character/Dignity (3)**: {威厳|いげん}, {貫禄|かんろく}, {名誉|めいよ}
- **Expressions/Idioms (3)**: {朝飯前|あさめしまえ}, {猫舌|ねこじた}, {取|と}り{越|こ}し{苦労|くろう}
- **Other useful (11)**: {機転|きてん}, {所作|しょさ}, {手筈|てはず}, {脱力|だつりょく}, {波紋|はもん}, {掛|か}け{声|ごえ}, {手柄|てがら}, {手本|てほん}, {名乗|なの}り, {折|お}り{返|かえ}し, {手探|てさぐ}り
- **Body/Daily (5)**: {読|よ}み{聞|き}かせ, {飛|と}び{火|ひ}, {寝癖|ねぐせ}, {足取|あしど}り, {腕組|うでぐ}み
- **Remaining (5)**: {奥行|おくゆ}き, {利便性|りべんせい}, {一任|いちにん}, {触媒|しょくばい}, {幻覚|げんかく}

Search strategies used: Legal/medical gap analysis, arts/crafts domain exploration, compound verb pattern completion, academic/abstract cross-referencing, emotional vocabulary expansion, social custom vocabulary, religious/spiritual coverage, dramatic expression mining, business register coverage, adjective gap filling

Candidate words: 179 → 269

### 2026-02-07 (Vocabulary Expansion - 30 New Entries, Session 225)
Added 30 new dictionary entries (IDs 10499-10528) from candidate_words.json:

- **Verbs (10)**: ほぐれる (to come loose), ほどく (to untie), なぞる (to trace), {攫|さら}う (to kidnap), したためる (to compose), ひっくり{返|かえ}す (to overturn), {紐解|ひもと}く (to unravel), {翻|ひるがえ}す (to wave/reverse), ぶちまける (to dump out/confess), ぶれる (to blur/waver), {目指|めざ}す (to aim for)
- **Nouns (8)**: {侍|さむらい} (samurai), タレ (sauce), ひよこ (chick), まとめ (summary), {簾|すだれ} (bamboo blind), {溜|た}まり{場|ば} (hangout), ちらし{寿司|ずし} (scattered sushi), ひき{逃|に}げ (hit-and-run), ひな{祭|まつ}り (Girls' Day), {振|ふ}る{舞|ま}い (behavior), {恵|めぐ}み (blessing)
- **Adjectives (5)**: {分厚|ぶあつ}い (very thick), {密|ひそ}か (secret), まちまち (varied), まっさら (brand new), まばら (sparse), まとも (proper)
- **Adverbs (2)**: まだまだ (still far from enough), {無理|むり}やり (forcibly)

Notable features:
- Multi-sense entries: ひよこ (chick/novice), ほぐれる (loosen/relax), なぞる (trace/retrace), {攫|さら}う (kidnap/sweep away), ひっくり{返|かえ}す (flip/reverse), {翻|ひるがえ}す (flutter/retract), ぶちまける (dump/confess), ぶれる (blur/waver), まとも (proper/direct), まっさら (new/blank), まだまだ (not enough/more to come), {振|ふ}る{舞|ま}い (behavior/hospitality), {目指|めざ}す (aspire/head for)
- Cultural context: ひな{祭|まつ}り (March 3 traditions), ちらし{寿司|ずし} (festive food), {簾|すだれ} (Heian-era usage), {侍|さむらい} (warrior class)
- Food vocabulary: タレ (dipping sauce), ちらし{寿司|ずし}

Total entries: 10,475 → 10,505
Remaining candidates: 208 → 179
New kanji: 2,261 → 2,263 ({侍|さむらい}, {攫|さら})

### 2026-02-07 (Vocabulary Expansion - 30 New Entries, Session 224)
Added 30 new dictionary entries from candidate_words.json, covering a diverse mix of vocabulary types:

- **Nouns (10)**: {付|つ}き{物|もの} (inseparable part), {一口|ひとくち} (one bite/in a word), {褒美|ほうび} (reward), しゃぶしゃぶ (shabu-shabu), すすき (pampas grass), つけ{麺|めん} (tsukemen), {外|はず}れ (miss/outskirts), {贔屓|ひいき} (favoritism), {引|ひ}きこもり (social withdrawal), ひととき (a moment), {拍子|ひょうし} (rhythm/moment)
- **Verbs (3)**: {馳|は}せる (to rush/send thoughts), ばら{撒|ま}く (to scatter), ほぐす (to loosen/relieve)
- **Adjectives (5)**: {相応|ふさわ}しい (suitable), どんくさい (clumsy), ほろ{苦|にが}い (bittersweet), ひたむき (earnest), ふかふか (fluffy)
- **Adverbs/Onomatopoeia (8)**: ひっそり (quietly), ふんわり (softly), しんなり (wilted), ずたずた (in tatters), ちまちま (in small amounts), {甚|はなは}だ (exceedingly), {一際|ひときわ} (conspicuously), ほのぼの (heartwarming)
- **Expressions (2)**: せい (fault/blame), できる{限|かぎ}り (as much as possible), とっておき (prized)

Notable entry features:
- Multi-sense entries: {一口|ひとくち} (bite/in a word), {馳|は}せる (rush/send thoughts), ばら{撒|ま}く (scatter/distribute), {外|はず}れ (miss/outskirts), {拍子|ひょうし} (rhythm/moment), ほろ{苦|にが}い (bitter taste/bittersweet), ほぐす (loosen/relieve)
- Transitivity pair cross-ref: ほぐす/ほぐれる
- Cultural context: {引|ひ}きこもり (8050 problem), すすき ({月見|つきみ} tradition)
- Food vocabulary: しゃぶしゃぶ, つけ{麺|めん}, しんなり (cooking term)

Total entries: 10,445 → 10,475
Remaining candidates: 238 → 208
New kanji: 2,258 → 2,261 ({贔|ひ}, {屓|き}, {麺|めん})

### 2026-02-07 (Vocabulary Expansion - 30 New Entries, Session 223)
Added 30 new dictionary entries from candidate_words.json, covering a diverse mix of verbs, adverbs, nouns, and adjectives:

- **Verbs (12)**: {伴|ともな}う (to accompany), {育|はぐく}む (to nurture), {倣|ならう}う (to follow an example), {灯|とも}す (to light), {囚|とら}われる (to be captured/bound by), {出来上|できあ}がる (to be completed), なじる (to reproach), {綴|つづ}る (to spell/compose), {務|つと}まる (to be fit for), はぐらかす (to dodge), {留|とど}まる (to stay/remain), {留|とど}める (to keep/retain)
- **Adverbs (8)**: とりわけ (especially), {遥々|はるばる} (from far away), {伸|の}び{伸|の}び (freely), とびきり (exceptionally), とっとと (quickly), {時折|ときおり} (occasionally), つべこべ (quibbling), たやすい
- **Nouns (6)**: {海苔|のり} (nori), {温|ぬく}もり (warmth), どら{焼|や}き (dorayaki), とうもろこし (corn), {取|と}り{組|く}み (effort/initiative), {咄嗟|とっさ} (instant)
- **Adverb/Adjective (3)**: {結構|けっこう} (quite/fine), {遥|はる}か (far/by far), {道理|どうり} (reason/no wonder)
- **Adjective (1)**: {色|いろ}とりどり (colorful)

Notable entry features:
- Multi-sense entries: {結構|けっこう} (quite/fine/no thank you, 3 senses), {囚|とら}われる (captured/bound by, 2 senses), {綴|つづ}る (spell/compose, 2 senses), {留|とど}まる (stay/limited to, 2 senses), {留|とど}める (keep/limit, 2 senses), {道理|どうり} (reason/no wonder, 2 senses), {取|と}り{組|く}み (initiative/sumo bout, 2 senses)
- Transitivity pair: {留|とど}まる/{留|とど}める
- Cross-references: {遥|はる}か↔{遥々|はるばる}
- Food vocabulary: {海苔|のり}, どら{焼|や}き, とうもろこし

Total entries: 10,363 → 10,393
Remaining candidates: 194 → 164
New kanji: 2,250 → 2,256 ({倣|ほう}, {咄|とつ}, {嗟|さ}, {囚|しゅう}, {綴|てつ}, {遥|よう})

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
