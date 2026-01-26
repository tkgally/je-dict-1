# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-26
**Current phase**: Phase 4 - Vocabulary Expansion & Interface Enhancement

**Live site**: https://tkgally.github.io/je-dict-1/

## Current State

### Phase
**Phase 4: Vocabulary Expansion & Interface Enhancement** - Adding vocabulary while maintaining v2 quality standards, plus new web interface features. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Infrastructure Status
- [x] Directory structure created (prefix-based subdirectories for scalability)
- [x] JSON schema defined (`build/schema.json`)
- [x] Validation script working (`build/validate.py`)
- [x] Build script working (`build/build_flat.py`)
- [x] Furigana system with toggle
- [x] Claude Code skills for entry guidelines
- [x] Quality specification v2 from multi-model evaluation
- [x] Vocabulary-notes skill for formatting guidelines
- [x] Notes field supports paragraph breaks and bullet points
- [x] Multiple interface modes (Search, Browse, Recent, Random)
- [x] Sticky header with interface toggle
- [x] Last updated date in footer
- [x] Cross-reference linking system with UI navigation (567 refs, 97% resolved)
- [x] Audio pronunciation for example sentences (1,028 audio files)
- [x] Prefix-based subdirectory structure for entries and audio (scalable to 10,000+ entries)
- [x] Shared utility modules (`path_utils.py`, `japanese_utils.py`)
- [x] Audio integrity validation in `validate.py`
- [x] Deterministic build output (clean before build)
- [x] Atomic build process (temp directory swap prevents broken states)
- [x] Centralized cross-reference type definitions (`build/cross_ref_types.py`)
- [x] Centralized furigana pattern and utilities (`build/japanese_utils.py`)
- [x] Enhanced validation with structured return types
- [x] Improved security (XSS prevention, no auto-install)

### Content Status
- **Total entries**: 8,379
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 5,556 | Unassigned: 0 ✓
- **Candidate words**: ~388 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 795 entries (target: 600-800) - fundamental words for basic communication
- **Core**: 1,998 entries (target: 1,600-2,000) - words for adult-level communication
- **General**: 5,046+ entries (no limit) - all other vocabulary useful for learners

**Tier realignment completed 2026-01-19.** All entries have tier assignments meeting target ranges. The basic and core tiers are curated to ensure semantic group integrity.

**Policy for new entries:** All new entries must be assigned to the **general** tier. The basic and core tiers are considered stable and should not be modified unless explicitly requested.

### Entry Breakdown by Type
| Type | Count | Notes |
|------|-------|-------|
| Verbs | ~1,200 | Includes transitivity and aspect info |
| Nouns | ~2,500 | Includes katakana loanwords |
| Adjectives | ~400 | I-adjectives and na-adjectives |
| Adverbs | ~200 | Time, manner, degree adverbs |
| Particles | 10 | Core particles with predicate lists |
| Counters | ~50 | Common counting patterns |
| Keigo verbs | 12 | Honorific and humble forms |
| Other | ~1,100 | Expressions, onomatopoeia, suffixes, etc. |

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

## Claude Code Skills

Available in `.claude/skills/` (automatically loaded when relevant):

| Skill | Use When |
|-------|----------|
| `entry-guidelines` | Creating any entry |
| `verb-entry` | Creating/revising verb entries |
| `adjective-entry` | Creating/revising adjective entries |
| `particle-entry` | Creating/revising particle entries |
| `other-entries` | Creating nouns, counters, adverbs, expressions |
| `revise-entries` | Revising existing entries to v2 standards |
| `vocabulary-notes` | Formatting notes field content |
| `cross-reference-entry` | Adding cross-references between entries |
| `find-candidates` | Finding new candidate words for the dictionary |
| `resolve-duplicates` | Identifying and resolving duplicate entries |
| `delete-entry` | Safely deleting entries with proper cleanup |

## Recent Changes

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 170)
Added 30 new dictionary entries from candidate_words.json, covering science/physics terminology, legal/government vocabulary, sports competition terms, infrastructure/location words, academic/publishing terms, and technology vocabulary:

- **Science/Physics (5)**: {反射|はんしゃ} (reflection/reflex), {共鳴|きょうめい} (resonance/sympathy), {屈折|くっせつ} (refraction), {融解|ゆうかい} (melting), {光合成|こうごうせい} (photosynthesis)
- **Legal/Government (7)**: {冤罪|えんざい} (false accusation), {黙秘|もくひ} (silence/refusing to answer), {公布|こうふ} (promulgation), {採決|さいけつ} (vote), {否決|ひけつ} (rejection), {訴状|そじょう} (complaint), {陳述|ちんじゅつ} (statement)
- **Sports/Competition (4)**: トーナメント (tournament), リーグ{戦|せん} (league match), {不戦勝|ふせんしょう} (win by default), {大差|たいさ} (big difference)
- **Infrastructure/Location (5)**: {舗装|ほそう} (paving), {石畳|いしだたみ} (cobblestone), {突|つ}き{当|あ}たり (dead end), {縁石|えんせき} (curb), {軒先|のきさき} (eaves/shopfront)
- **Academic/Publishing (3)**: {査読|さどく} (peer review), {凡例|はんれい} (legend/explanatory notes), {抄録|しょうろく} (abstract)
- **Technology (4)**: {暗号化|あんごうか} (encryption), {復号|ふくごう} (decryption), {並列|へいれつ} (parallel), {直列|ちょくれつ} (serial)
- **Household/Other (2)**: {窓際|まどぎわ} (by the window/sidelined), {追|お}い{焚|だ}き (reheating bath)

Notable entry features:
- Physics vocabulary cluster: {反射|はんしゃ}/{屈折|くっせつ} (reflection vs refraction), {融解|ゆうかい}/{光合成|こうごうせい}
- Legal process vocabulary: {訴状|そじょう}/{陳述|ちんじゅつ}/{黙秘|もくひ} (courtroom terms)
- Legislative process: {採決|さいけつ}/{否決|ひけつ}/{公布|こうふ} (voting and promulgation)
- Competition formats: トーナメント vs リーグ{戦|せん} (knockout vs round-robin)
- Circuit terminology: {並列|へいれつ} vs {直列|ちょくれつ} (parallel vs series)
- Multi-sense entries: {反射|はんしゃ} (light reflection vs physiological reflex), {共鳴|きょうめい} (physics vs sympathy), {屈折|くっせつ} (physics vs psychological), {窓際|まどぎわ} (location vs sidelined employee)
- 3 new kanji added to kanji index: 冤 (02086), 抄 (02087), 舗 (02088)

Total entries: 8,349 → 8,379
Remaining candidates: ~418 → ~388
New kanji: 2,085 → 2,088

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 169)
Added 30 new dictionary entries from candidate_words.json, covering workplace/business vocabulary, relationship conflicts, entertainment/media terminology, and technology terms:

- **Workplace/Career (8)**: {値切|ねぎ}る (to haggle), {勤務先|きんむさき} (workplace), {昇格|しょうかく} (promotion), {引|ひ}き{継|つ}ぎ (handover), {申|もう}し{送|おく}り (handover briefing), {半休|はんきゅう} (half-day off), {繁忙期|はんぼうき} (busy season), {閑散期|かんさんき} (slow season)
- **Relationship Conflicts (7)**: {揉|も}め{事|ごと} (trouble/dispute), {八|や}つ{当|あ}たり (taking out anger), {逆恨|さかうら}み (misplaced resentment), {口論|こうろん} (argument), {疎遠|そえん} (estranged), {破局|はきょく} (breakup), {絶縁|ぜつえん} (severing ties)
- **Entertainment/Media (8)**: {楽屋|がくや} (dressing room), {舞台裏|ぶたいうら} (backstage), {収録|しゅうろく} (recording), {予告|よこく} (preview/trailer), {上映|じょうえい} (screening), {視聴率|しちょうりつ} (viewer ratings), {観覧|かんらん} (viewing), {喝采|かっさい} (applause)
- **Business/Academic (4)**: {保留|ほりゅう} (pending/on hold), {審査|しんさ} (examination), {補足|ほそく} (supplement), {校閲|こうえつ} (proofreading)
- **Technology/Other (3)**: {課金|かきん} (billing/in-app purchase), {分解|ぶんかい} (disassembly), {抜|ぬ}け{道|みち} (shortcut/loophole)

Notable entry features:
- Workplace transition vocabulary: {引|ひ}き{継|つ}ぎ (handover tasks) vs {申|もう}し{送|おく}り (handover briefing)
- Seasonal business terms: {繁忙期|はんぼうき} vs {閑散期|かんさんき} (busy vs slow season)
- Relationship deterioration scale: {疎遠|そえん} → {破局|はきょく} → {絶縁|ぜつえん}
- Entertainment industry vocabulary: {楽屋|がくや}/{舞台裏|ぶたいうら} (behind the scenes)
- Multi-sense entries: {絶縁|ぜつえん} (severing ties vs electrical insulation), {分解|ぶんかい} (disassembly vs decomposition), {抜|ぬ}け{道|みち} (shortcut vs loophole)
- 4 new kanji added to kanji index: 喝 (02082), 繁 (02083), 閑 (02084), 閲 (02085)

Total entries: 8,319 → 8,349
Remaining candidates: ~448 → ~418
New kanji: 2,081 → 2,085

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 168)
Added 30 new dictionary entries from candidate_words.json, covering health/body vocabulary, weather/seasons, personality types, food/cooking, lifestyle/home, transportation, social customs/gifts, and emotions:

- **Health/Body (5)**: {熱中症|ねっちゅうしょう} (heatstroke), {二日酔|ふつかよ}い (hangover), {五月病|ごがつびょう} (May blues), {仮眠|かみん} (nap), {寝落|ねお}ち (falling asleep unintentionally)
- **Weather/Seasons (4)**: {秋晴|あきば}れ (clear autumn weather), {小春日和|こはるびより} (Indian summer), {梅雨入|つゆい}り (start of rainy season), {梅雨明|つゆあ}け (end of rainy season)
- **Personality/Eating Types (4)**: {甘党|あまとう} (sweet tooth), {辛党|からとう} (spice/alcohol lover), {大食|おおぐ}い (big eater), {怖|こわ}がり (scaredy-cat)
- **Food/Cooking (4)**: {出来立|できた}て (freshly made), {焼|や}き{立|た}て (freshly baked), {作|つく}り{置|お}き (meal prep), こだわり (commitment/obsession)
- **Lifestyle/Home (3)**: {大掃除|おおそうじ} (major cleaning), {断捨離|だんしゃり} (decluttering), {住|す}み{心地|ごこち} (livability)
- **Transportation (3)**: {満員電車|まんいんでんしゃ} (packed train), {吊|つ}り{革|かわ} (train strap), {振替輸送|ふりかえゆそう} (alternative transport)
- **Social/Gifts (4)**: {手土産|てみやげ} (visiting gift), お{返|かえ}し (return gift), {二次会|にじかい} (after-party), ご{祝儀|しゅうぎ} (congratulatory money)
- **Emotions/Expressions (2)**: {苦笑|にがわら}い (bitter smile), {愛想笑|あいそうわら}い (forced smile)
- **Work/Career (1)**: {出世|しゅっせ} (career advancement)

Notable entry features:
- Japanese health vocabulary: {熱中症|ねっちゅうしょう} (summer danger), {二日酔|ふつかよ}い (hangover remedies), {五月病|ごがつびょう} (adjustment disorder)
- Seasonal weather cluster: {秋晴|あきば}れ/{小春日和|こはるびより} (autumn), {梅雨入|つゆい}り/{梅雨明|つゆあ}け (rainy season)
- Eating preference types: {甘党|あまとう} vs {辛党|からとう} (sweets vs alcohol historically)
- ～{立|た}て pattern: {出来立|できた}て/{焼|や}き{立|た}て (freshness suffix)
- Commuting vocabulary: {満員電車|まんいんでんしゃ}/{吊|つ}り{革|かわ}/{振替輸送|ふりかえゆそう}
- Japanese gift culture: {手土産|てみやげ}/お{返|かえ}し/ご{祝儀|しゅうぎ}
- Multi-sense entries: {辛党|からとう} (alcohol lover vs spicy food lover), {大食|おおぐ}い (big eater vs eating contest), こだわり (positive dedication vs negative fixation)

Total entries: 8,289 → 8,319
Remaining candidates: ~478 → ~448

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 167)
Added 30 new dictionary entries from candidate_words.json, covering products/shopping vocabulary, food/dining terms, weather vocabulary, business/finance expressions, and compound verbs:

- **Products/Shopping (8)**: {手作|てづく}り (handmade), {手書|てが}き (handwriting), {中古品|ちゅうこひん} (used item), {新品|しんぴん} (brand new), {既製品|きせいひん} (ready-made), {在庫切|ざいこぎ}れ (out of stock), {取|と}り{置|お}き (holding item), {取|と}り{寄|よ}せ (ordering in)
- **Food/Dining (5)**: {飲|の}み{放題|ほうだい} (all-you-can-drink), {替|か}え{玉|だま} (extra noodles), おまかせ (chef's choice), {腹八分目|はらはちぶんめ} (eating in moderation), {落|お}とし{蓋|ぶた} (drop lid)
- **Weather (3)**: {猛暑|もうしょ} (intense heat), {酷暑|こくしょ} (extreme heat), {渇水|かっすい} (water shortage)
- **Business/Finance (5)**: {概算|がいさん} (rough estimate), {収支|しゅうし} (income and expenses), たたき{台|だい} (draft proposal), {試算|しさん} (trial calculation), {累計|るいけい} (cumulative total)
- **Compound verbs (4)**: {見込|みこ}む (to expect), {吹|ふ}き{荒|あ}れる (to rage), {駆|か}け{巡|めぐ}る (to rush around), {張|は}り{巡|めぐ}らす (to stretch around)
- **Shopping/Services (3)**: ラッピング (gift wrapping), {景品|けいひん} (prize), {先着|せんちゃく} (first-come)
- **Housing (2)**: {木造|もくぞう} (wooden construction), {駅近|えきちか} (close to station)

Notable entry features:
- Product condition vocabulary: {新品|しんぴん} vs {中古品|ちゅうこひん} vs {既製品|きせいひん} vs {手作|てづく}り
- Ramen culture: {替|か}え{玉|だま} (extra noodles at no/low cost), {飲|の}み{放題|ほうだい} (all-you-can-drink)
- Japanese proverb: {腹八分目|はらはちぶんめ} (eating in moderation for health)
- Weather extremes: {猛暑|もうしょ} vs {酷暑|こくしょ} (intensity distinction)
- Business planning vocabulary: たたき{台|だい}/{概算|がいさん}/{試算|しさん}/{累計|るいけい}
- Multi-sense entries: {見込|みこ}む (expect/anticipate vs. see potential in), {吹|ふ}き{荒|あ}れる (weather vs. figurative), {駆|か}け{巡|めぐ}る (physical vs. mental)
- 3 new kanji added to kanji index: 猛 (02079), 累 (02080), 酷 (02081)

Total entries: 8,259 → 8,289
Remaining candidates: ~508 → ~478
New kanji: 2,078 → 2,081

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 166)
Added 30 new dictionary entries from candidate_words.json, covering daily life vocabulary, travel/tourism terms, dining expressions, household items, and media/entertainment terminology:

- **Personality/Character (5)**: おっとり (calm), {生意気|なまいき} (impudent), {嘘|うそ}つき (liar), {不真面目|ふまじめ} (insincere)
- **Food/Dining (4)**: おかず (side dish), {立|た}ち{食|ぐ}い (stand-up eating), {食|た}べ{放題|ほうだい} (all-you-can-eat)
- **Household/Gardening (6)**: ハンガー (hanger), ジッパー (zipper), プランター (planter), じょうろ (watering can), スコップ (scoop), {鍬|くわ} (hoe)
- **Travel/Tourism (5)**: チェックイン (check-in), チェックアウト (check-out), ビザ (visa), {旅券|りょけん} (passport), ツアー (tour)
- **Tickets/Events (4)**: {立|た}ち{見|み} (standing room only), {当日券|とうじつけん} (same-day ticket), {整理券|せいりけん} (numbered ticket), {前売|まえう}り (advance sale)
- **Services/Rules (3)**: {貸|か}し{切|き}り (reserved), {持|も}ち{込|こ}み (bringing in), {差|さ}し{入|い}れ (gift/treat)
- **Media/Publishing (3)**: {打|う}ち{切|き}り (cancellation), {見逃|みのが}し (overlooking/catch-up viewing), {読|よ}み{切|き}り (one-shot story)
- **Time/Competition (2)**: {駆|か}け{込|こ}み (last-minute rush), {出遅|でおく}れ (late start)

Notable entry features:
- Japanese food culture: おかず (side dishes with rice), {立|た}ち{食|ぐ}い (stand-up eateries), {食|た}べ{放題|ほうだい} (all-you-can-eat)
- Travel vocabulary cluster: チェックイン/チェックアウト (hotel), {旅券|りょけん}/ビザ (documents), ツアー
- Ticket types: {当日券|とうじつけん} vs {前売|まえう}り (pricing differences)
- Japanese services: {整理券|せいりけん} (bus/restaurant queue system), {差|さ}し{入|い}れ (workplace gift culture)
- Media terminology: {打|う}ち{切|き}り (series cancellation), {読|よ}み{切|き}り (manga one-shots)
- Multi-sense entries: {駆|か}け{込|こ}み (last-minute rush vs. emergency shelter), {見逃|みのが}し (overlooking vs. catch-up streaming)
- 1 new kanji added to kanji index: 鍬 (02078)

Total entries: 8,229 → 8,259
Remaining candidates: ~538 → ~508
New kanji: 2,077 → 2,078

### 2026-01-25 (New Candidates - 100 Words Added)
Added 100 new candidate words to `candidate_words.json` across diverse domains:

**Health/Body (8)**: {寝違|ねちが}える (stiff neck), {肌荒|はだあ}れ (skin irritation), {五月病|ごがつびょう} (May blues), {熱中症|ねっちゅうしょう} (heatstroke), {食|しょく}あたり (food poisoning), {二日酔|ふつかよ}い (hangover), {湯冷|ゆざ}め (catching cold after bath), {仮眠|かみん} (nap), {寝落|ねお}ち (falling asleep unintentionally)

**Weather/Seasons (5)**: {花冷|はなび}え (late spring cold snap), {秋晴|あきば}れ (clear autumn weather), {小春日和|こはるびより} (Indian summer), {梅雨入|つゆい}り (start of rainy season), {梅雨明|つゆあ}け (end of rainy season)

**Household/Lifestyle (6)**: {大掃除|おおそうじ} (major cleaning), {整理整頓|せいりせいとん} (organizing), {断捨離|だんしゃり} (decluttering), {食|く}わず{嫌|ぎら}い (disliking without trying), {住|す}み{心地|ごこち} (livability), {書|か}き{心地|ごこち} (writing feel)

**Personality Types (8)**: {恥|は}ずかしがり{屋|や} (shy person), {寂|さび}しがり{屋|や} (lonely person), {怖|こわ}がり (scaredy-cat), {甘党|あまとう} (sweet tooth), {辛党|からとう} (spice lover), {大食|おおぐ}い (big eater), {少食|しょうしょく} (light eater), {早食|はやぐ}い (fast eater)

**Food/Cooking (8)**: {作|つく}り{置|お}き (meal prep), {出来立|できた}て (freshly made), {焼|や}き{立|た}て (freshly baked), {揚|あ}げ{立|た}て (freshly fried), {茹|ゆ}でたて (freshly boiled), {採|と}れたて (freshly harvested), こだわり (commitment/obsession)

**Transportation (12)**: {通勤|つうきん}ラッシュ (commuter rush), {満員電車|まんいんでんしゃ} (packed train), {帰宅|きたく}ラッシュ (evening rush), {駆|か}け{込|こ}み{乗車|じょうしゃ} (rushing onto train), {立|た}ち{乗|の}り (standing on train), {座席争|ざせきあらそ}い (seat competition), {吊|つ}り{革|かわ} (train strap), {車内放送|しゃないほうそう} (train announcement), {運行状況|うんこうじょうきょう} (service status), {振替輸送|ふりかえゆそう} (alternative transport), {落|お}とし{物|もの} (lost property), {回数券|かいすうけん} (book of tickets)

**Train/Transport Types (5)**: グリーン{車|しゃ} (first-class car), {女性専用車両|じょせいせんようしゃりょう} (women-only car), ホームドア (platform screen door), {人身事故|じんしんじこ} (injury accident), {遅延証明|ちえんしょうめい} (delay certificate)

**Work/Business (8)**: {飛|と}び{込|こ}み{営業|えいぎょう} (cold calling), サービス{残業|ざんぎょう} (unpaid overtime), {配置転換|はいちてんかん} (job transfer), {出世|しゅっせ} (career advancement), {窓際族|まどぎわぞく} (sidelined employees), {社内恋愛|しゃないれんあい} (office romance), {飲|の}みニケーション (drinking-based networking), {二次会|にじかい} (after-party)

**Social/Gifts (15)**: {会費|かいひ} (membership fee), {別会計|べつかいけい} (separate checks), {持|も}ち{寄|よ}り (potluck), {手土産|てみやげ} (visiting gift), お{返|かえ}し (return gift), ご{祝儀|しゅうぎ} (congratulatory money), のし{袋|ぶくろ} (money gift envelope), お{年玉|としだま} (New Year's money), {引|ひ}っ{越|こ}し{祝|いわ}い (housewarming gift), {出産祝|しゅっさんいわ}い (baby gift), {入学祝|にゅうがくいわ}い (school entrance gift), {卒業祝|そつぎょういわ}い (graduation gift), {就職祝|しゅうしょくいわ}い (job celebration gift), {快気祝|かいきいわ}い (recovery gift)

**Expressions/Smiles (13)**: {無神経|むしんけい} (insensitive), {顔色|かおいろ}をうかがう (watching expression), {愛想笑|あいそうわら}い (forced smile), {作|つく}り{笑|わら}い (fake smile), {笑|わら}いすぎ (laughing too much), {苦笑|にがわら}い (bitter smile), {照|て}れ{笑|わら}い (embarrassed smile), {泣|な}き{笑|わら}い (laughing through tears), {薄笑|うすわら}い (smirk), {高笑|たかわら}い (loud laugh), {思|おも}い{出|だ}し{笑|わら}い (laughing at memory), {嘘泣|うそな}き (fake crying), もらい{泣|な}き (sympathetic crying)

**Communication/Personality (12)**: {揚|あ}げ{足取|あしと}り (nitpicking), {告|つ}げ{口|ぐち} (tattling), {口喧嘩|くちげんか} (verbal argument), {多弁|たべん} (talkative), {話|はな}し{上手|じょうず} (good speaker), {聞|き}き{上手|じょうず} (good listener), {甘|あま}え{上手|じょうず} (good at being spoiled), {世渡|よわた}り{上手|じょうず} (socially adept), {場見知|ばみし}り (shy in new places), {社交的|しゃこうてき} (sociable), {内向的|ないこうてき} (introverted), {外向的|がいこうてき} (extroverted), {二面性|にめんせい} (two-faced nature)

Notable patterns:
- Japanese social customs: gift-giving occasions, celebration types
- Workplace culture: commuter experience, office dynamics
- Personality vocabulary: types and traits
- Expressions of laughter/crying: nuanced emotional vocabulary
- "Freshly made" patterns: ~{立|た}て compound words
- "-{上手|じょうず}" skill patterns: communication abilities

Candidate count: 438 → 538

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 165)
Added 30 new dictionary entries from candidate_words.json, covering abstract nouns, compound verbs, daily life vocabulary, pronouns, and cooking terms:

- **Abstract nouns (5)**: {前提|ぜんてい} (premise), {実践|じっせん} (practice), {拒否|きょひ} (refusal), {条例|じょうれい} (ordinance), {差配|さはい} (management)
- **Body/Health (2)**: {体質|たいしつ} (constitution), {渇|かわ}き (thirst)
- **Household/Daily life (4)**: {光熱費|こうねつひ} (utility costs), {付箋|ふせん} (sticky note), {筆箱|ふでばこ} (pencil case), {用足|ようた}し (errand)
- **Training/Skills (3)**: {修練|しゅうれん} (training), {鍛|きた}え{上|あ}げる (to train thoroughly), {磨|みが}き{上|あ}げる (to polish up)
- **Moisture/Benefit (3)**: {潤|うるお}す (to moisten), {潤|うるお}い (moisture), {渇|かわ}き (thirst)
- **Compound verbs (5)**: {奮|ふる}い{立|た}つ (to be roused), {書|か}き{殴|なぐ}る (to scribble), {言|い}い{直|なお}す (to rephrase), {整|ととの}え{直|なお}す (to readjust), {燻|いぶ}す (to smoke food)
- **Entertainment (1)**: {主演|しゅえん} (starring role)
- **Shopping (1)**: バーゲン (bargain sale)
- **Food/Cooking (2)**: {付|つ}け{合|あ}わせ (side dish), {溶|と}かす (to melt)
- **Communication (2)**: お{詫|わ}び (apology), {逆|ぎゃく}に (conversely)
- **Pronouns (2)**: あいつ (that guy), こいつ (this guy)
- **Emotion (1)**: {寂|さび}しさ (loneliness)

Notable entry features:
- Multi-sense entries: {体質|たいしつ} (physical constitution vs. organizational culture), {用足|ようた}し (errand vs. bathroom euphemism), {燻|いぶ}す (smoking food vs. fumigation)
- Compound verb patterns with {直|なお}す: {言|い}い{直|なお}す, {整|ととの}え{直|なお}す (redo/correct nuance)
- Compound verb patterns with {上|あ}げる: {鍛|きた}え{上|あ}げる, {磨|みが}き{上|あ}げる (completion/perfection nuance)
- Related vocabulary cluster: {潤|うるお}す/{潤|うるお}い/{渇|かわ}き (moisture/thirst contrast)
- Ko-so-a-do pronouns: あいつ/こいつ (informal person pronouns)
- Japanese daily life: {光熱費|こうねつひ} (utility costs), {付箋|ふせん} (sticky notes)
- 1 new kanji added to kanji index: 詫 (02077)

Total entries: 8,199 → 8,229
Remaining candidates: ~468 → ~438
New kanji: 2,076 → 2,077

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 164)
Added 30 new dictionary entries from candidate_words.json, covering workplace positions, i-adjectives, verbs, food preservation, gardening vocabulary, and sports/competition terms:

- **Workplace positions (2)**: {主任|しゅにん} (supervisor), {係長|かかりちょう} (section chief)
- **Institutions (1)**: {公立|こうりつ} (public institution)
- **Medical (1)**: {投薬|とうやく} (medication)
- **Appearance/Communication (2)**: {見掛|みか}け (appearance), {言|い}い{掛|が}かり (false accusation)
- **Verbs (9)**: {擦|す}り{切|き}れる (to wear out), {縮|ちぢ}こまる (to huddle up), {振|ふ}り{分|わ}ける (to distribute), {凝|こ}らす (to concentrate), {書|か}き{換|か}える (to rewrite), {置|お}き{換|か}える (to replace), {入|い}れ{替|か}える (to swap), {居直|いなお}る (to become defiant), {成|な}り{下|さ}がる (to sink to), {間引|まび}く (to thin out)
- **I-adjectives (5)**: {奥|おく}ゆかしい (refined), {疎|うと}ましい (disagreeable), {痛々|いたいた}しい (pitiful), {空々|そらぞら}しい (feigned), {慕|した}わしい (dear/beloved)
- **Japanese preserved foods (3)**: {塩辛|しおから} (salted seafood), {酢漬|すづ}け (vinegar pickle), {粕漬|かすづ}け (sake lees pickle)
- **Gardening (3)**: {植|う}え{替|か}え (repotting), {追肥|ついひ} (additional fertilizer), {間引|まび}く (to thin out plants)
- **Sports results (4)**: {惨敗|ざんぱい} (crushing defeat), {快勝|かいしょう} (easy victory), {辛勝|しんしょう} (narrow victory), {本選|ほんせん} (finals)

Notable entry features:
- Japanese corporate hierarchy vocabulary: {主任|しゅにん} → {係長|かかりちょう} → {課長|かちょう} → {部長|ぶちょう}
- Multi-sense entries: {縮|ちぢ}こまる (cold vs. fear), {書|か}き{換|か}える (rewrite vs. renew), {凝|こ}らす (focus vs. elaborate), {居直|いなお}る (defiant vs. sit up), {間引|まび}く (plants vs. services)
- Traditional Japanese foods cluster: {塩辛|しおから} (fermented seafood), {酢漬|すづ}け}/{粕漬|かすづ}け (pickle types)
- Victory/defeat scale: {惨敗|ざんぱい} → {大敗|たいはい} → {敗北|はいぼく} and {圧勝|あっしょう} → {快勝|かいしょう} → {辛勝|しんしょう}
- Japanese aesthetic concept: {奥|おく}ゆかしい (understated elegance)
- 2 new kanji added to kanji index: 慕 (02075), 粕 (02076)

Total entries: 8,169 → 8,199
Remaining candidates: ~497 → ~468
New kanji: 2,074 → 2,076

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 163)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, i-adjectives, na-adjectives, health/medical terms, workplace vocabulary, and sports terms:

- **Compound verbs (7)**: {凝|こ}る (to be absorbed in; to stiffen), {潤|うるお}う (to be moist; to profit), {盛|も}り{返|かえ}す (to rally), {持|も}ち{直|なお}す (to recover), {開|ひら}き{直|なお}る (to become defiant), {成|な}り{上|あ}がる (to rise in status), {紛|まぎ}らわす (to distract)
- **I-adjectives (5)**: {白々|しらじら}しい (feigned), {侘|わび}しい (lonely/desolate), {麗|うるわ}しい (beautiful), {憎|にく}らしい (hateful), {好|この}ましい (favorable)
- **Na-adjectives (4)**: {怠惰|たいだ} (lazy), {痛快|つうかい} (thrilling), {貪欲|どんよく} (greedy; eager), {芳醇|ほうじゅん} (mellow)
- **Workplace (2)**: {部署|ぶしょ} (department), {指図|さしず} (orders/instructions)
- **Shopping (1)**: {買|か}い{出|だ}し (shopping for supplies)
- **Health/Medical (5)**: {寝汗|ねあせ} (night sweat), {肉離|にくばな}れ (muscle tear), {擦|す}り{傷|きず} (scrape), {療養|りょうよう} (recuperation), {回診|かいしん} (doctor's rounds), {往診|おうしん} (house call)
- **Training (1)**: {鍛錬|たんれん} (training/discipline)
- **Safety (2)**: {防犯|ぼうはん} (crime prevention), {応急|おうきゅう} (emergency/first-aid)
- **Gardening (1)**: {草|くさ}むしり (weeding)
- **Sports (1)**: {大敗|たいはい} (crushing defeat)

Notable entry features:
- Multi-sense entries: {凝|こ}る (absorbed in vs. stiff muscles), {潤|うるお}う (moisture vs. profit), {貪欲|どんよく} (negative greed vs. positive eagerness)
- Defiant attitude vocabulary: {開|ひら}き{直|なお}る (becoming unapologetically defiant when confronted)
- Social mobility: {成|な}り{上|あ}がる with notes on negative nuance (parvenu/nouveau riche)
- Medical visit types: {回診|かいしん} (hospital rounds) vs {往診|おうしん} (house calls)
- Japanese aesthetic concept: {侘|わび}しい with connection to {侘|わ}び{寂|さ}び aesthetic
- 6 new kanji added to kanji index: 侘 (02069), 貪 (02070), 醇 (02071), 錬 (02072), 鍛 (02073), 麗 (02074)

Total entries: 8,139 → 8,169
Remaining candidates: ~527 → ~497
New kanji: 2,068 → 2,074

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 162)
Added 30 new dictionary entries from candidate_words.json, covering verbs, adjectives, food/dining vocabulary, shopping terms, travel/places, cooking heat levels, media/entertainment, and science terms:

- **Verbs (4)**: {咲|さ}く (to bloom), {飼|か}う (to keep/raise animals), {照|て}れる (to be shy), おごる (to treat someone)
- **Adjectives (2)**: {乏|とぼ}しい (scarce), {険|けわ}しい (steep)
- **Food/Dining (7)**: {出前|でまえ} (food delivery), {割|わ}り{勘|かん} (splitting bill), {味見|あじみ} (tasting), {持|も}ち{帰|かえ}り (takeout), {大盛|おおも}り (large serving)
- **Shopping/Retail (2)**: {福袋|ふくぶくろ} (lucky bag), おまけ (bonus/freebie)
- **Cooking heat levels (3)**: {弱火|よわび} (low heat), {中火|ちゅうび} (medium heat), {強火|つよび} (high heat)
- **Household (1)**: {洗|あら}い{物|もの} (dishes to wash)
- **Travel/Places (4)**: {名所|めいしょ} (famous place), {民宿|みんしゅく} (guesthouse), {坂道|さかみち} (slope), {行|い}き{止|ど}まり (dead end)
- **Entertainment/Media (4)**: {生放送|なまほうそう} (live broadcast), {再放送|さいほうそう} (rerun), {開幕|かいまく} (opening), {閉幕|へいまく} (closing)
- **Sports (1)**: {接戦|せっせん} (close game)
- **Work/Business (1)**: {面談|めんだん} (interview/meeting)
- **Science/Physics (2)**: {拡散|かくさん} (diffusion/spread), {振動|しんどう} (vibration)
- **Personality (1)**: {人柄|ひとがら} (personality/character)

Notable entry features:
- Cooking heat level cluster: {弱火|よわび}/{中火|ちゅうび}/{強火|つよび} with cross-references between all three
- Food/dining vocabulary chain covering the full experience: {味見|あじみ} → {大盛|おおも}り → {持|も}ち{帰|かえ}り/{出前|でまえ} → {割|わ}り{勘|かん}/おごる
- Cultural notes on {福袋|ふくぶくろ} (New Year lucky bags) and {民宿|みんしゅく} (Japanese guesthouse tradition)
- Multi-sense entries: {拡散|かくさん} (physical diffusion vs. information spread), おまけ (bonus item vs. on top of that)
- {出前|でまえ} with notes on traditional delivery culture vs. modern delivery apps
- 2 new kanji added to kanji index: 乏 (02067), 咲 (02068)

Total entries: 8,109 → 8,139
Remaining candidates: ~557 → ~527
New kanji: 2,066 → 2,068

### 2026-01-25 (New Candidates - 106 Words Added)
Added 106 new candidate words to `candidate_words.json` across diverse domains:

**Weather/Climate (3)**: {猛暑|もうしょ} (intense heat), {酷暑|こくしょ} (extreme heat), {渇水|かっすい} (water shortage)

**Health/Medical (4)**: {嘔吐|おうと} (vomiting), {肺炎|はいえん} (pneumonia), {喘息|ぜんそく} (asthma), {関節炎|かんせつえん} (arthritis)

**Finance/Business (9)**: {歳入|さいにゅう} (annual revenue), {歳出|さいしゅつ} (annual expenditure), {収支|しゅうし} (income and expenses), {累計|るいけい} (cumulative total), {試算|しさん} (trial calculation), {概算|がいさん} (rough estimate), {債権|さいけん} (credit/bond), たたき{台|だい} (draft proposal), {審査|しんさ} (examination/review)

**Government/Legal (6)**: {訴状|そじょう} (complaint), {陳述|ちんじゅつ} (statement), {冤罪|えんざい} (false accusation), {黙秘|もくひ} (silence), {採決|さいけつ} (vote), {否決|ひけつ} (rejection), {公布|こうふ} (promulgation)

**Onomatopoeia (3)**: じりじり (scorching), ごつごつ (rugged), がちがち (rigid)

**Compound Verbs (7)**: {見込|みこ}む (to expect), {駆|か}け{巡|めぐ}る (to rush around), {張|は}り{巡|めぐ}らす (to stretch around), {撒|ま}き{散|ち}らす (to scatter), {掻|か}き{消|け}す (to vanish), {吹|ふ}き{荒|あ}れる (to rage)

**Cooking (5)**: {弱火|よわび} (low heat), {強火|つよび} (high heat), {中火|ちゅうび} (medium heat), {落|お}とし{蓋|ぶた} (drop lid), {追|お}い{焚|だ}き (reheating bath)

**Household/Places (9)**: {洗|あら}い{物|もの} (dishes to wash), {窓際|まどぎわ} (by the window), {軒先|のきさき} (shopfront), {突|つ}き{当|あ}たり (dead end), {坂道|さかみち} (slope), {抜|ぬ}け{道|みち} (shortcut), {行|い}き{止|ど}まり (dead end), {舗装|ほそう} (pavement), {石畳|いしだたみ} (cobblestone), {縁石|えんせき} (curb)

**Science/Physics (8)**: {光合成|こうごうせい} (photosynthesis), {融解|ゆうかい} (melting), {分解|ぶんかい} (decomposition), {反射|はんしゃ} (reflection), {屈折|くっせつ} (refraction), {振動|しんどう} (vibration), {共鳴|きょうめい} (resonance), {拡散|かくさん} (diffusion)

**Entertainment/Media (12)**: {楽屋|がくや} (dressing room), {舞台裏|ぶたいうら} (backstage), {観覧|かんらん} (viewing), {喝采|かっさい} (acclaim), {開幕|かいまく} (opening), {閉幕|へいまく} (closing), {上映|じょうえい} (screening), {視聴率|しちょうりつ} (ratings), {収録|しゅうろく} (recording), {生放送|なまほうそう} (live broadcast), {再放送|さいほうそう} (rerun), {予告|よこく} (preview)

**Sports (5)**: リーグ{戦|せん} (league match), トーナメント (tournament), {不戦勝|ふせんしょう} (win by default), {大差|たいさ} (wide margin), {接戦|せっせん} (close game)

**Work Culture (11)**: {昇格|しょうかく} (promotion), {勤務先|きんむさき} (workplace), {面談|めんだん} (interview), {申|もう}し{送|おく}り (handover), {引|ひ}き{継|つ}ぎ (succession), {半休|はんきゅう} (half-day off), {繁忙期|はんぼうき} (busy season), {閑散期|かんさんき} (slow season), {検討中|けんとうちゅう} (under consideration), {保留|ほりゅう} (on hold)

**Relationships (6)**: {破局|はきょく} (breakup), {疎遠|そえん} (estranged), {絶縁|ぜつえん} (breaking ties), {揉|も}め{事|ごと} (trouble), {口論|こうろん} (argument), {逆恨|さかうら}み (grudge), {八|や}つ{当|あ}たり (taking out anger)

**Academic/Publishing (6)**: {査読|さどく} (peer review), {校閲|こうえつ} (proofreading), {補足|ほそく} (supplement), {抄録|しょうろく} (abstract), {凡例|はんれい} (explanatory notes)

**Technology (9)**: {課金|かきん} (billing), {非同期|ひどうき} (asynchronous), {暗号化|あんごうか} (encryption), {復号|ふくごう} (decryption), {並列|へいれつ} (parallel), {直列|ちょくれつ} (serial), {帯域|たいいき} (bandwidth), スループット (throughput), {可用性|かようせい} (availability)

**Environment (3)**: {伐採|ばっさい} (logging), {植林|しょくりん} (afforestation), {食物連鎖|しょくもつれんさ} (food chain)

Candidate count: 451 → 557

---

**Archive Note**: Only the 10 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).


## Workflow: Adding Entries from Candidates

Follow this step-by-step process when adding new dictionary entries from `candidate_words.json`:

### Step 1: Select Candidates
1. Review `candidate_words.json` to choose words to add
2. Prioritize by JLPT level (N5 → N4 → N3) or thematic groups
3. Check that the candidate hasn't already been added to the dictionary

### Step 2: Create Entry Files
1. Create the JSON entry file following the schema (`build/schema.json`)
2. Use the appropriate Claude skill based on entry type:
   - Verbs: `verb-entry` skill
   - Adjectives: `adjective-entry` skill
   - Particles: `particle-entry` skill
   - Others: `other-entries` skill
3. Follow `vocabulary-notes` skill for notes formatting
4. Place file in correct directory based on numeric ID range:
   - Directory: `entries/{range}/` where `{range}` is based on the 5-digit ID:
     - IDs 00001-00499 → `entries/00000/`
     - IDs 00500-00999 → `entries/00500/`
     - IDs 01000-01499 → `entries/01000/`
     - etc. (500 entries per directory)
   - Example: `entries/00000/00396_taberu.json`
5. File naming: `{5-digit-id}_{romaji}.json`

### Step 3: Validate Entry
```bash
python3 build/validate.py --id {entry_id}
# Or validate all:
python3 build/validate.py
```

### Step 4: Update Indexes
**IMPORTANT: Run this after adding ANY entries:**
```bash
python3 build/update_indexes.py
```
This will:
- Update `entries_index.json` with the new entry
- Remove added words from `candidate_words.json` (sync)

### Step 5: Rebuild Website
**IMPORTANT: Run this to update the GitHub Pages site:**
```bash
python3 build/build_flat.py
```
This regenerates all HTML files in `docs/` which GitHub Pages serves. Without this step, new entries won't appear on the live site.

### Step 6: Add Cross-References
1. Use the `cross-reference-entry` skill for guidelines
2. Add structured references for:
   - Transitivity pairs (for verbs)
   - Keigo equivalents
   - Antonyms/opposites
   - Related vocabulary mentioned in notes
3. References can point to entries that don't exist yet

### Step 7: Commit Changes
Commit all changes including:
- New entry JSON files in `entries/`
- Updated `entries_index.json` and `candidate_words.json`
- Rebuilt `docs/` folder (required for GitHub Pages to update)

## Workflow: Adding Cross-References to Entries

### Cross-Reference Format
```json
"cross_references": [
  {
    "type": "pair",
    "reading": "しまる",
    "headword": "{閉|し}まる",
    "label": "intransitive"
  }
]
```

### Reference Types
| Type | Use For | Example |
|------|---------|---------|
| `pair` | Transitivity pairs | 閉める → 閉まる |
| `antonym` | Opposites | 大きい → 小さい |
| `keigo` | Honorific/humble | 食べる → 召し上がる |
| `synonym` | Similar meaning | 分かる → 理解する |
| `contrast` | Easily confused | は → が |
| `related` | Semantically connected | 食べる → 食べ物 |
| `see_also` | General reference | - |

## Technical Notes

### Build Commands
```bash
# Validate entries (includes schema, cross-refs, audio integrity)
python3 build/validate.py

# Validate a single entry
python3 build/validate.py --id 00396_taberu

# Merge new audio files (from audio-to-add/)
python3 build/merge_audio.py

# Build dictionary
python3 build/build_flat.py

# Update index files (after adding/removing entries)
python3 build/update_indexes.py

# Manage candidate words
python3 build/manage_candidates.py stats    # Show statistics
python3 build/manage_candidates.py add "漢字" "かんじ" "notes"  # Add candidate

# Cross-reference resolution report
python3 build/resolve_links.py

# View locally
open docs/index.html
```

### File Naming Convention
- Format: `{5-digit-id}_{romanized_reading}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: `entries/{range}/` where `{range}` is based on the numeric ID:
  - IDs 00001-00499 → `entries/00000/`
  - IDs 00500-00999 → `entries/00500/`
  - IDs 01000-01499 → `entries/01000/`
  - etc. (500 entries per directory)
- Example: `entries/00000/00396_taberu.json`
- Katakana loanwords: Use hiragana reading (e.g., アルバイト → あるばいと)

### Entry and Candidate Tracking
- **entries_index.json**: Auto-generated index of all dictionary entries
- **candidate_words.json**: Words to potentially add (each has unique ID like C00001)
- Run `python build/update_indexes.py` after modifying entries to keep indexes in sync

## Notes for AI Assistants

### Before Starting Work
1. Read this file to understand current state
2. Relevant skills will be auto-loaded based on task type (see Claude Code Skills table above)
3. Use the `entry-guidelines` skill for general quality standards

### Entry Requirements
- All kanji must have furigana: `{漢字|かんじ}`
- 2-3 example sentences minimum
- Examples progress from simple to complex
- Include at least one collocation or fixed phrase
- Katakana loanwords use hiragana in reading field
- **sense_numbers required**: All examples must have `sense_numbers` field populated
  - Single-sense entries: use `[1]` for all examples
  - Multi-sense entries: each example must specify which sense(s) it illustrates

### Quality Standards
See the `entry-guidelines` skill for comprehensive guidelines. Key points:
- **Verbs**: Transitivity type, pair verb, aspect/ている behavior, collocations
- **Particles**: Predicates requiring particle, contrast with similar particles
- **Adjectives**: Forms (adverbial, noun), similar word distinctions
- **All entries**: Consistent depth with similar entries

### After Each Session
Update the "Recent Changes" section in this file with:
- Entries added/revised
- Any issues encountered

**Note**: Keep only the 10 most recent change entries. When adding a new entry, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
