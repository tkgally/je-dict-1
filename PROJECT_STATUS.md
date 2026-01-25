# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-25
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
- **Total entries**: 8,019
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 5,196 | Unassigned: 0 ✓
- **Candidate words**: ~438 words tracked in `candidate_words.json`
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

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 158)
Added 30 new dictionary entries from candidate_words.json, covering daily life vocabulary, Japanese communication patterns, work/shopping terms, health/sleep vocabulary, and ambiguity expressions:

- **Postponement/Progress (4)**: {先送|さきおく}り (postponement), {棚上|たなあ}げ (shelving), {足踏|あしぶ}み (marking time/stagnation), {行|い}き{詰|づ}まり (deadlock)
- **Sleep/Health (5)**: {寝違|ねちが}え (stiff neck from sleeping), ぎっくり{腰|ごし} (slipped disc), うたた{寝|ね} (dozing off), {寝相|ねぞう} (sleeping posture), {食|た}べごたえ (satisfying to eat)
- **Work/Satisfaction (2)**: {働|はたら}きがい (job satisfaction), {試飲|しいん} (drink tasting)
- **Phone/Technology (3)**: {着信音|ちゃくしんおん} (ringtone), {不在着信|ふざいちゃくしん} (missed call), {機内|きない}モード (airplane mode)
- **Garbage/Household (3)**: ゴミ{出|だ}し (taking out trash), {生|なま}ゴミ (food waste), {粗大|そだい}ゴミ (bulky garbage)
- **Shopping (3)**: まとめ{買|が}い (bulk buying), {買|か}いだめ (stocking up), {試飲|しいん} (drink tasting)
- **Ambiguity/Vagueness (3)**: うやむや (vague), あやふや (uncertain), {曖昧|あいまい} (ambiguous)
- **Communication (4)**: {八方美人|はっぽうびじん} (people-pleaser), {察|さっ}する (to sense/infer), {遠回|とおまわ}し (indirect), {打算的|ださんてき} (calculating)
- **Meaning/Visibility (3)**: {含|ふく}み (implication), {見|み}え{隠|かく}れ (appearing and disappearing), {押|お}し{問答|もんどう} (argument)
- **Other (1)**: つなぎ (connection/stopgap)

Notable entry features:
- Multi-sense entries: {足踏|あしぶ}み (marching in place vs. stagnation), {含|ふく}み (implication vs. unrealized gains), {見|み}え{隠|かく}れ (physical visibility vs. subtle hints), つなぎ (connection, stopgap, cooking binder)
- Related vocabulary clusters: うやむや/あやふや/{曖昧|あいまい} (vagueness terms), garbage types ({生|なま}ゴミ/{粗大|そだい}ゴミ), shopping patterns (まとめ{買|が}い/{買|か}いだめ)
- Japanese communication concepts: {察|さっ}する (reading implicit cues), {遠回|とおまわ}し (indirect communication), {八方美人|はっぽうびじん} (people-pleasing)
- Daily life in Japan: {機内|きない}モード, garbage sorting rules, bulk buying culture
- 1 new kanji added to kanji index: 曖

Total entries: 7,989 → 8,019
Remaining candidates: ~467 → ~438
New kanji: 2,060 → 2,061

### 2026-01-25 (Vocabulary Expansion - 30 New Entries, Session 157)
Added 30 new dictionary entries from candidate_words.json, covering science/chemistry terms, business operations, transformation nouns (-化), legal/document vocabulary, and everyday expressions:

- **Science/Chemistry (5)**: {風化|ふうか} (weathering), {凝縮|ぎょうしゅく} (condensation), {溶解|ようかい} (dissolution), {腐食|ふしょく} (corrosion), {還元|かんげん} (reduction)
- **Business operations (3)**: {操業|そうぎょう} (operation), {民営化|みんえいか} (privatization), {国有化|こくゆうか} (nationalization)
- **Transformation nouns -化 (6)**: {簡略化|かんりゃくか} (simplification), {規格化|きかくか} (standardization), {常態化|じょうたいか} (normalization), {空洞化|くうどうか} (hollowing out), {硬直化|こうちょくか} (rigidity), {陳腐化|ちんぷか} (obsolescence)
- **Legal/Documents (4)**: {誓約書|せいやくしょ} (written pledge), {捺印|なついん} (seal stamping), {言|い}い{逃|のが}れる (to make excuses), {差|さ}し{押|お}さえ (seizure)
- **Evidence/Scope (3)**: {喫煙|きつえん} (smoking), {網羅|もうら} (comprehensive coverage), {裏付|うらづ}け (backing/evidence)
- **Disappointment/Effort (4)**: {拍子抜|ひょうしぬ}け (anticlimax), {肩透|かたすか}かし (letdown), {二度手間|にどでま} (double work), {骨折|ほねお}り{損|ぞん} (wasted effort)
- **Nature (2)**: {潮風|しおかぜ} (sea breeze), {朝露|あさつゆ} (morning dew)
- **Activities (2)**: サイクリング (cycling), ランニング (running)
- **Daily life (1)**: {物干|ものほ}し{竿|ざお} (laundry pole)

Notable entry features:
- Cross-references: {民営化|みんえいか} ↔ {国有化|こくゆうか} (antonym pair), {拍子抜|ひょうしぬ}け ↔ {肩透|かたすか}かし (similar disappointment)
- Multi-sense entries: {風化|ふうか} (physical weathering vs. fading from memory), {凝縮|ぎょうしゅく} (physical vs. figurative condensation), {溶解|ようかい} (dissolving vs. melting), {還元|かんげん} (chemical reduction vs. returning benefits), {肩透|かたすか}かし (disappointment vs. sumo technique), ランニング (running vs. running costs)
- Six related -化 transformation nouns describing organizational/systemic changes
- {捺印|なついん} with cultural context on Japanese seal culture ({印鑑|いんかん})
- 1 new kanji added to kanji index: 捺

Total entries: 7,959 → 7,989
Remaining candidates: ~497 → ~467
New kanji: 2,059 → 2,060

### 2026-01-24 (Vocabulary Expansion - 30 New Entries, Session 156)
Added 30 new dictionary entries from candidate_words.json, covering formal/business vocabulary, legal terminology, financial/accounting terms, and excellence/criticism vocabulary:

- **Vision/perception (1)**: {翳|かす}む (to become misty/dim)
- **Social behavior (2)**: {迎合|げいごう} (ingratiation), {横槍|よこやり} (interference/meddling)
- **Control/deterrence (2)**: {抑止|よくし} (deterrence), {自制|じせい} (self-control)
- **Criticism/tyranny (4)**: {暴挙|ぼうきょ} (outrage), {横暴|おうぼう} (tyranny), {蛮行|ばんこう} (barbaric act), {専横|せんおう} (despotism)
- **Excellence terms (4)**: {着実|ちゃくじつ} (steady), {卓越|たくえつ} (excellence), {凌駕|りょうが} (surpassing), {傑出|けっしゅつ} (outstanding)
- **Financial/accounting (7)**: {換算|かんさん} (conversion), {充当|じゅうとう} (allocation), {計上|けいじょう} (recording), {弁済|べんさい} (repayment), {償還|しょうかん} (redemption), {資金繰|しきんぐ}り (cash flow), {台帳|だいちょう} (register/ledger)
- **Explanation/apology (3)**: {弁解|べんかい} (excuse), {弁明|べんめい} (explanation), {陳謝|ちんしゃ} (apology)
- **Legal terms (2)**: {告発|こくはつ} (accusation), {告訴|こくそ} (lawsuit/complaint)
- **Mining/excavation (3)**: {発掘|はっくつ} (excavation), {採掘|さいくつ} (mining), {掘削|くっさく} (drilling)
- **Change/deterioration (2)**: {腐敗|ふはい} (corruption/decay), {鈍化|どんか} (slowing down)

Notable entry features:
- {翳|かす}む with 3 senses: (1) physical mist/haze, (2) dimming vision, (3) being overshadowed
- {発掘|はっくつ} with 2 senses: (1) archaeological excavation, (2) discovering hidden talent
- {腐敗|ふはい} with 2 senses: (1) physical decay/rot, (2) political/moral corruption
- Business vocabulary chain: {計上|けいじょう} (record) → {弁済|べんさい} (repay) → {償還|しょうかん} (redeem)
- Criticism terms with cultural notes on workplace behavior and political discourse
- Legal terminology pair: {告発|こくはつ} (accusation) vs {告訴|こくそ} (formal complaint)
- 4 new kanji added to kanji index: 槍, 翳, 蛮, 駕

Total entries: 7,929 → 7,959
Remaining candidates: ~527 → ~497
New kanji: 2,055 → 2,059

### 2026-01-23 (Vocabulary Expansion - 30 New Entries, Session 155)
Added 30 new dictionary entries from candidate_words.json, covering business terms, cooking vocabulary, compound verbs, and formal/abstract nouns:

- **Business/commerce (7)**: {欠品|けっぴん} (out of stock), {売値|うりね} (selling price), {粗利|あらり} (gross profit), {退職金|たいしょくきん} (retirement allowance), {日給|にっきゅう} (daily wage), {帳簿|ちょうぼ} (ledger), {積立|つみたて} (savings)
- **Cooking/food (5)**: {水気|みずけ} (moisture), ひじき (hijiki seaweed), {干|ほ}し{椎茸|しいたけ} (dried shiitake), がんもどき (fried tofu fritter), さつま{揚|あ}げ (fried fish cake)
- **Compound verbs (4)**: {見慣|みな}れる (to get used to seeing), {読|よ}み{返|かえ}す (to reread), {聞|き}き{込|こ}む (to investigate), {降|ふ}り{注|そそ}ぐ (to pour down)
- **Documents/legal (2)**: {委任状|いにんじょう} (power of attorney), {覚書|おぼえがき} (memorandum)
- **Daily life/home (3)**: {荷解|にほど}き (unpacking), {節水|せっすい} (water conservation), {漏電|ろうでん} (electrical leak)
- **Formal/abstract nouns (6)**: {熟考|じゅっこう} (careful consideration), {誇示|こじ} (showing off), {歪曲|わいきょく} (distortion), {更迭|こうてつ} (reshuffle), {看過|かんか} (overlooking), {駆逐|くちく} (eradication)
- **Motivation (2)**: {奮起|ふんき} (rousing oneself), {発奮|はっぷん} (being inspired)
- **Photography (1)**: {一眼|いちがん}レフ (SLR camera)

Notable entry features:
- Business vocabulary covering the full transaction cycle: {粗利|あらり} (gross margin) → {欠品|けっぴん} (out of stock) → {売値|うりね} (selling price)
- Traditional Japanese foods: がんもどき etymology from "imitation goose", regional name variations
- Employment vocabulary: {退職金|たいしょくきん} with Japanese employment context, {日給|にっきゅう} vs {月給|げっきゅう}
- {覚書|おぼえがき} with two senses: (1) personal notes, (2) business MOU
- 2 new kanji added to kanji index: 簿, 迭

Total entries: 7,899 → 7,929
Remaining candidates: ~556 → ~527
New kanji: 2,053 → 2,055

### 2026-01-22 (Vocabulary Expansion - 30 New Entries, Session 154)
Added 30 new dictionary entries from candidate_words.json, covering formal expressions, business terms, physical verbs, and miscellaneous vocabulary:

- **Formal/honorific expressions (5)**: {恐|おそ}れ{入|い}ります (I'm sorry to trouble you), {僭越|せんえつ} (presumptuous), {謹|つつし}んで (respectfully), {仰|おお}せ (instruction - honorific), {御意|ぎょい} (as you wish - archaic)
- **Business/real estate (4)**: {歩合|ぶあい} (commission), {更地|さらち} (vacant lot), {築年数|ちくねんすう} (building age), {陳列|ちんれつ} (display)
- **Physical verbs (7)**: {敷|し}き{詰|つ}める (to spread all over), すり{潰|つぶ}す (to grind), {滑|すべ}らす (to slide), よじる (to twist), {摺|す}り{寄|よ}る (to sidle up)
- **Speech/mockery verbs (4)**: おだてる (to flatter), {嘲|あざけ}る (to mock), ほざく (to babble - vulgar), {嗾|けしか}ける (to incite)
- **Abstract nouns (5)**: {逐次|ちくじ} (sequentially), {当|あ}たり{障|さわ}り (offense), {粛清|しゅくせい} (purge), {改編|かいへん} (reorganization), {差|さ}し{支|つか}え (hindrance)
- **Environment/weather (1)**: {日射|にっしゃ} (sunshine/solar radiation)
- **Food (1)**: {黒酢|くろず} (black vinegar)
- **Modern/loanwords (3)**: コーデ (outfit coordination), プラットホーム (platform), アンプ (amplifier), シンセサイザー (synthesizer)

Notable entry features:
- {僭越|せんえつ} and {御意|ぎょい} with detailed notes on formal/historical contexts
- {嗾|けしか}ける with notes on instigating dogs to attack and figurative usage
- {摺|す}り{寄|よ}る with two senses: (1) physical sidling up, (2) opportunistic cozying up
- {憎|にく}まれ{口|ぐち} (sarcastic remarks) with cultural context about indirect criticism
- プラットホーム with notes distinguishing from プラットフォーム (computing/business platform)
- 6 new kanji added to kanji index: 僭, 嗾, 嘲, 摺, 謹, 陳

Total entries: 7,869 → 7,899
Remaining candidates: ~585 → ~556
New kanji: 2,047 → 2,053

### 2026-01-22 (Vocabulary Expansion - 30 New Entries, Session 153)
Added 30 new dictionary entries from candidate_words.json, covering sound verbs, compound verbs, adjectives, business/logistics terms, food vocabulary, and more:

- **Sound/crowd verbs (2)**: どよめく (to stir/be in uproar), ざわめく (to rustle/murmur)
- **Multi-sense verbs (1)**: {煽|あお}る with 3 senses: (1) to fan, (2) to incite/stir up, (3) to tailgate
- **Compound verbs (6)**: {持|も}て{余|あま}す (to have more than one can handle), {培|つちか}う (to cultivate), {聞|き}き{流|なが}す (to let pass), {乗|の}り{過|す}ごす (to ride past), {聞|き}き{逃|のが}す (to fail to hear), {傾|かし}げる (to tilt)
- **Adjectives (4)**: {艶|なまめ}かしい (alluring), おぞましい (disgusting), {巧妙|こうみょう} (clever/ingenious), {果敢|かかん} (bold/daring)
- **Leak/damage nouns (2)**: {雨漏|あまも}り (roof leak), {水漏|みずも}れ (water leak)
- **Business/logistics (6)**: {梱包|こんぽう} (packing), {荷造|にづく}り (packing for moving), {入荷|にゅうか} (arrival of goods), {棚卸|たなおろ}し (inventory), {問屋|とんや} (wholesaler), {着払|ちゃくばら}い (cash on delivery)
- **Formal/abstract nouns (5)**: {淘汰|とうた} (selection/weeding out), {改竄|かいざん} (falsification), {黙認|もくにん} (tacit approval), {惰性|だせい} (inertia), {抜擢|ばってき} (promotion/selection)
- **Food/kitchen (3)**: {湯葉|ゆば} (tofu skin), {高野豆腐|こうやどうふ} (freeze-dried tofu), {土鍋|どなべ} (earthenware pot)
- **Weather (1)**: {暴風|ぼうふう} (violent wind/gale)

Notable entry features:
- どよめく vs ざわめく comparison: どよめく is sudden collective reaction, ざわめく is continuous background noise
- {煽|あお}る covers physical fanning, social incitement, and modern driving term ({煽|あお}り{運転|うんてん})
- {改竄|かいざん} with notes on modern contexts (documents, data, DNA) and kanji/kana writing conventions
- Food vocabulary: {湯葉|ゆば} and {高野豆腐|こうやどうふ} with preparation and regional variation notes
- Business logistics chain: {入荷|にゅうか} (goods in) → {棚卸|たなおろ}し (inventory) → {問屋|とんや} (wholesale)
- 7 new kanji added to kanji index: 培, 惰, 擢, 梱, 淘, 煽, 竄

Total entries: 7,839 → 7,869
Remaining candidates: ~610 → ~585
New kanji: 2,040 → 2,047

### 2026-01-22 (Vocabulary Expansion - 30 New Entries, Session 152)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, adjectives, sports terms, culinary vocabulary, and daily life expressions:

- **Compound verbs (8)**: {立|た}ち{上|あ}げる (to launch), {染|し}み{込|こ}む (to soak in), {打|う}ち{解|と}ける (to open up), {盛|も}り{上|あ}げる (to liven up), {和|やわ}らぐ (to soften - intrans.), {和|やわ}らげる (to mitigate - trans.), {積|つ}み{上|あ}げる (to pile up), {成|な}り{立|た}つ (to consist of)
- **Adjectives (3)**: {儚|はかな}い (fleeting), {頼|たの}もしい (reliable), {清々|すがすが}しい (refreshing)
- **Sports competition terms (4)**: {奮闘|ふんとう} (hard struggle), {善戦|ぜんせん} (good fight), {圧勝|あっしょう} (overwhelming victory), {惜敗|せきはい} (narrow defeat)
- **Culinary/taste terms (3)**: {濃厚|のうこう} (rich/thick), {淡泊|たんぱく} (light/plain), {舌触|したざわ}り (texture/mouthfeel)
- **Safety/emergency (2)**: {防災|ぼうさい} (disaster prevention), {避難|ひなん} (evacuation)
- **Daily life/work (10)**: {雑用|ざつよう} (odd jobs), {身支度|みじたく} (getting ready), {後始末|あとしまつ} (cleaning up), {苛立|いらだ}つ (to be irritated), {爽快|そうかい} (refreshing), {滑稽|こっけい} (comical), {緻密|ちみつ} (meticulous), {仕掛|しか}け (mechanism), {仕分|しわ}け (sorting), {嵩張|かさば}る (to be bulky)

Notable entry features:
- Transitivity pair with cross-references: {和|やわ}らぐ (intransitive) ↔ {和|やわ}らげる (transitive)
- Antonym pair with cross-references: {濃厚|のうこう} (rich) ↔ {淡泊|たんぱく} (light)
- {濃厚|のうこう} with two senses: (1) rich taste/texture, (2) strong probability; includes COVID-19 term {濃厚接触者|のうこうせっしょくしゃ}
- {染|し}み{込|こ}む with cooking usage notes (common in recipes for flavors soaking in)
- {成|な}り{立|た}つ with two senses: (1) to consist of, (2) to be viable/sustainable
- {儚|はかな}い with literary and cultural notes about Japanese aesthetic concept of transience

Total entries: 7,809 → 7,839
Remaining candidates: ~640 → ~610

### 2026-01-21 (New Candidates - 100 Words Added)
Added 100 new candidate words to `candidate_words.json` using diverse search strategies across multiple domains:

**Business/Workplace (3)**: {部署|ぶしょ} (department), {主任|しゅにん} (supervisor), {係長|かかりちょう} (section chief)

**Medical/Health (8)**: {投薬|とうやく} (medication), {療養|りょうよう} (recuperation), {回診|かいしん} (doctor's rounds), {往診|おうしん} (house call), {肉離れ|にくばなれ} (muscle tear), {擦り傷|すりきず} (scrape), {渇き|かわき} (thirst), {寝汗|ねあせ} (night sweat)

**Emotions/Personality (12)**: {苛立|いらだ}つ (to be irritated), {爽快|そうかい} (refreshing), {痛快|つうかい} (thrilling), {奥床|おくゆか}しい (refined), {侘|わび}しい (desolate), {儚|はかな}い (fleeting), {頼|たの}もしい (reliable), {好|この}ましい (favorable), {疎|うと}ましい (disagreeable), {痛々|いたいた}しい (pitiful), {白々|しらじら}しい (unconvincing), {憎|にく}らしい (hateful)

**Culinary/Taste (9)**: {塩辛|しおから} (salted fish guts), {酢漬|すづ}け (vinegar pickle), {粕漬|かすづ}け (sake lees pickle), {濃厚|のうこう} (rich), {淡泊|たんぱく} (light), {芳醇|ほうじゅん} (mellow), {舌触|したざわ}り (texture)

**Compound Verbs (25+)**: {立|た}ち{上|あ}げる (to launch), {染|し}み{込|こ}む (to soak in), {擦|す}り{切|き}れる (to wear out), {書|か}き{換|か}える (to rewrite), {置|お}き{換|か}える (to replace), {入|い}れ{替|か}える (to swap), {持|も}ち{直|なお}す (to recover), {盛|も}り{返|かえ}す (to rally), {打|う}ち{解|と}ける (to open up), {開|ひら}き{直|なお}る (to become defiant), {居直|いなお}る (to become defiant), {成|な}り{立|た}つ (to consist of), {成|な}り{上|あ}がる (to rise in status), {成|な}り{下|さ}がる (to sink), {鍛|きた}え{上|あ}げる (to train thoroughly), {磨|みが}き{上|あ}げる (to polish up), {積|つ}み{上|あ}げる (to pile up), {盛|も}り{上|あ}げる (to liven up), {和|やわ}らぐ (to soften), {和|やわ}らげる (to mitigate), {紛|まぎ}らわす (to distract), {潤|うるお}う (to be moist), {潤|うるお}す (to moisten), {奮|ふる}い{立|た}つ (to be roused), {書|か}き{殴|なぐ}る (to scribble)

**Daily Life/Activities (15)**: {見掛|みか}け (appearance), {言|い}い{掛|が}かり (false accusation), {仕掛|しか}け (mechanism), {仕分|しわ}け (sorting), {振|ふ}り{分|わ}ける (to distribute), {嵩張|かさば}る (to be bulky), {滑稽|こっけい} (comical), {緻密|ちみつ} (meticulous), {怠惰|たいだ} (laziness), {草|くさ}むしり (weeding), {植|う}え{替|か}え (repotting), {追肥|ついひ} (fertilizing), {間引|まび}く (to thin out), {用足|ようた}し (errand), {買|か}い{出|だ}し (bulk buying)

**Safety/Emergency (4)**: {防犯|ぼうはん} (crime prevention), {防災|ぼうさい} (disaster prevention), {避難|ひなん} (evacuation), {応急|おうきゅう} (emergency)

**Work/Organization (8)**: {身支度|みじたく} (getting ready), {後始末|あとしまつ} (cleaning up), {整|ととの}え{直|なお}す (to readjust), {差配|さはい} (management), {指図|さしず} (instructions), {雑用|ざつよう} (odd jobs), {修練|しゅうれん} (training), {鍛錬|たんれん} (discipline)

**Sports/Competition (8)**: {奮闘|ふんとう} (hard struggle), {善戦|ぜんせん} (good fight), {大敗|たいはい} (crushing defeat), {惨敗|ざんぱい} (crushing defeat), {圧勝|あっしょう} (overwhelming victory), {快勝|かいしょう} (easy victory), {辛勝|しんしょう} (narrow victory), {惜敗|せきはい} (narrow defeat)

**Other (8)**: {凝|こ}らす (to concentrate), {凝|こ}る (to stiffen), {清々|すがすが}しい (refreshing), {空々|そらぞら}しい (feigned), {麗|うるわ}しい (beautiful), {慕|した}わしい (dear), {潤|うるお}い (moisture), {貪欲|どんよく} (greedy), {本選|ほんせん} (finals)

Notable features:
- Strong coverage of compound verbs (〜込む, 〜上げる, 〜直す patterns)
- Taste/culinary vocabulary for food descriptions
- Emotion adjectives with nuanced meanings (〜しい pattern)
- Sports terminology for competition results
- Practical daily life vocabulary

Candidate count: 540 → 640

### 2026-01-21 (Vocabulary Expansion - 30 New Entries, Session 151)
Added 30 new dictionary entries from candidate_words.json, covering practical vocabulary, formal expressions, organizational terms, and descriptive adjectives:

- **Practical/Technical (4)**: {配線|はいせん} (wiring), {物資|ぶっし} (supplies), {救援|きゅうえん} (relief), {配給|はいきゅう} (distribution)
- **Weather/Nature (2)**: {寒暖差|かんだんさ} (temperature difference), {朝靄|あさもや} (morning mist)
- **Adjectives (5)**: ものぐさ (lazy), あっけない (anticlimactic), か{弱|よわ}い (frail), {夥|おびただ}しい (numerous), ものものしい (imposing)
- **Verbs (6)**: {偏|かたよ}る (to be biased), {賄|まかな}う (to provide meals), {葬|ほうむ}る (to bury), めくれる (to turn up), {使|つか}い{込|こ}む (to embezzle/use extensively), {使|つか}い{慣|な}れる (to become used to using)
- **Places/Buildings (3)**: {作業場|さぎょうば} (workplace), {集会所|しゅうかいじょ} (meeting hall), {表口|おもてぐち} (front entrance)
- **Social/Business (4)**: シェア (share), {追従|ついしょう} (flattery), おべっか (flattery - colloquial), {憚|はばか}る (to hesitate)
- **Expressions/Concepts (3)**: {一枚上手|いちまいうわて} (a cut above), {天命|てんめい} (divine will), {抜本|ばっぽん} (drastic)
- **Formal/Political (3)**: {統廃合|とうはいごう} (consolidation), {糾弾|きゅうだん} (denunciation), {紛糾|ふんきゅう} (complication)

Notable entry features:
- {追従|ついしょう} ↔ おべっか cross-reference (formal vs. colloquial flattery)
- {使|つか}い{込|こ}む with 2 senses: (1) embezzlement, (2) developing skill through use
- ものものしい with 2 senses: (1) solemn/imposing, (2) heavy-handed (security)
- {偏|かたよ}る with 2 senses: (1) biased views, (2) physical leaning
- Confucian philosophical term {天命|てんめい} with famous saying from Analects
- Administrative vocabulary for school/hospital mergers ({統廃合|とうはいごう})

Total entries: 7,779 → 7,809
Remaining candidates: ~563 → ~540

### 2026-01-21 (Vocabulary Expansion - 30 New Entries, Session 150)
Added 30 new dictionary entries from candidate_words.json, covering expressive verbs, descriptive adjectives, traditional Japanese architectural terms, and useful everyday vocabulary:

- **Expressive verbs (10)**: {際立|きわだ}つ (to stand out), {安|やす}らぐ (to feel at ease), ひしめく (to crowd together), {項垂|うなだ}れる (to hang one's head), はにかむ (to be shy), {淀|よど}む (to stagnate), かすれる (to become hoarse), ふやける (to become soggy), ぼける (to become senile/blurred), {漲|みなぎ}る (to overflow with)
- **Descriptive adjectives (7)**: {疎|うと}い (unfamiliar with), {浅|あさ}ましい (shameful), {物悲|ものがな}しい (melancholy), {忌々|いまいま}しい (annoying), ぞんざい (careless/rude), けばい (gaudy), こすい (sly)
- **Traditional/architectural (5)**: {土間|どま} (dirt floor entry), {軒下|のきした} (under the eaves), {柱時計|はしらどけい} (pendulum clock), {傾|かたむ}き (tilt/slope), {諦観|ていかん} (resignation)
- **Everyday vocabulary (6)**: {身|み}の{回|まわ}り (one's surroundings), {小休止|しょうきゅうし} (short break), {山脈|さんみゃく} (mountain range), {具|ぐ} (ingredients), あて (prospect), {世話人|せわにん} (organizer)
- **Expressions (2)**: {思|おも}いのほか (more than expected), あのね (you know)

Notable entry features:
- ぼける with 3 senses: (1) becoming senile, (2) being blurred/out of focus (source of English "bokeh"), (3) playing dumb in comedy
- {淀|よど}む with 2 senses: (1) stagnant water, (2) hesitant speech
- {疎|うと}い with 2 senses: (1) unfamiliar with something, (2) estranged in relationships
- Traditional Japanese house vocabulary: {土間|どま}, {軒下|のきした} with cultural context
- {諦観|ていかん} with Buddhist philosophical undertones

Total entries: 7,749 → 7,779
Remaining candidates: ~584 → ~563

### 2026-01-21 (Vocabulary Expansion - 30 New Entries, Session 149)
Added 30 new dictionary entries from candidate_words.json, covering technology terms, business loanwords, scheduling vocabulary, and practical everyday expressions:

- **Technology/Communication (6)**: LINE (messaging app), プラグ (plug), レンズ (lens), IT (information technology), ID (identification), Bluetooth
- **Business/Startup terminology (6)**: ステークホルダー (stakeholder), ガバナンス (governance), レガシー (legacy), ローンチ (launch), スケール (scale), キャリアアップ (career advancement)
- **Scheduling/Work (5)**: {繰|く}り{上|あ}げ (moving up schedule), {繰|く}り{下|さ}げ (postponing), {日程調整|にっていちょうせい} (schedule coordination), {遅刻届|ちこくとどけ} (late arrival notice), {朝食付|ちょうしょくつ}き (with breakfast)
- **Music/Media (3)**: カバー (cover song), リミックス (remix), スパム (spam)
- **Lifestyle/Shopping (4)**: ガーデニング (gardening), ライフスタイル (lifestyle), {駐車料金|ちゅうしゃりょうきん} (parking fee), アイテム (item)
- **Daily life (6)**: イケてる (cool/stylish), {集合場所|しゅうごうばしょ} (meeting place), {物足|ものた}りなさ (wanting more), FAX (fax), バンパー (bumper), {太陽光発電|たいようこうはつでん} (solar power)

Notable entry features:
- Cross-references: {繰|く}り{上|あ}げ ↔ {繰|く}り{下|さ}げ (schedule antonym pair)
- カバー with 3 senses: (1) protective cover, (2) cover song, (3) compensating
- スケール with 3 senses: (1) business scale, (2) measuring scale, (3) musical scale
- レガシー with 2 senses: (1) positive heritage, (2) outdated system
- スパム with 2 senses: (1) email spam, (2) SPAM food (popular in Okinawa)
- LINE entry with cultural notes about Japan's messaging culture and {既読|きどく} feature
- FAX entry with cultural context about Japan's continued fax usage

Total entries: 7,719 → 7,749
Remaining candidates: ~613 → ~584

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
