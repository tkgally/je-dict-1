# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-20
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
- **Total entries**: 7,599
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 4,806 | Unassigned: 0 ✓
- **Candidate words**: ~529 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 795 entries (target: 600-800) - fundamental words for basic communication
- **Core**: 1,998 entries (target: 1,600-2,000) - words for adult-level communication
- **General**: 4,776+ entries (no limit) - all other vocabulary useful for learners

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

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 142)
Added 30 new dictionary entries from candidate_words.json, covering a variety of vocabulary types including verbs, adjectives, adverbs, and nouns:

- **Verbs (11)**: ほっとする (to feel relieved), {掻|か}き{立|た}てる (to stir up), {賜|たまわ}る (to receive - honorific), {綻|ほころ}びる (to come apart), {蔓延|はびこ}る (to spread/be rampant), {使|つか}い{分|わ}ける (to use selectively), {使|つか}い{果|は}たす (to use up), さまよう (to wander), たくらむ (to scheme), きらめく (to sparkle), {訪|おとず}れる (to visit)
- **I-adjectives (4)**: そっけない (curt), みすぼらしい (shabby), たどたどしい (halting), すさまじい (tremendous)
- **Na-adjectives (2)**: {冗長|じょうちょう} (redundant), {大|おお}まか (rough/approximate)
- **Adverbs (2)**: {別々|べつべつ}に (separately), ちょくちょく (often)
- **Nouns (11)**: {汎用|はんよう} (general-purpose), {互換性|ごかんせい} (compatibility), {再編|さいへん} (restructuring), {瓦解|がかい} (collapse), {使|つか}い{捨|す}て (disposable), {相場|そうば} (market price), {氷点下|ひょうてんか} (below freezing), {暴風雨|ぼうふうう} (storm), {検診|けんしん} (medical checkup), {土砂降|どしゃぶ}り (downpour), {暗証番号|あんしょうばんごう} (PIN number)

Notable entry features:
- Honorific verb {賜|たまわ}る with formal/humble usage notes
- Negative-connotation verbs: {蔓延|はびこ}る (for spreading of undesirable things), たくらむ (scheming)
- Technical computing terms: {汎用|はんよう}, {互換性|ごかんせい}, {冗長|じょうちょう} (with redundancy in IT context)
- Weather vocabulary: {氷点下|ひょうてんか}, {暴風雨|ぼうふうう}, {土砂降|どしゃぶ}り
- つかい~ compound verbs: {使|つか}い{捨|す}て, {使|つか}い{分|わ}ける, {使|つか}い{果|は}たす
- Adjectives describing manner/appearance: そっけない, みすぼらしい, たどたどしい, すさまじい

Total entries: 7,569 → 7,599
Remaining candidates: ~558 → ~529

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 141)
Added 30 new dictionary entries from candidate_words.json, covering psychological/emotional vocabulary, information/revelation terms, social actions, character traits, legal/business terminology, -化 transformation words, and comparison verbs:

- **Psychological/emotional (5)**: {衝動|しょうどう} (impulse), {本能|ほんのう} (instinct), {直感|ちょっかん} (intuition), {没頭|ぼっとう} (immersion), {憧憬|しょうけい} (longing)
- **Information/revelation (4)**: {隠蔽|いんぺい} (concealment), {捏造|ねつぞう} (fabrication), {発覚|はっかく} (coming to light), {暴露|ばくろ} (exposure)
- **Social/political actions (4)**: {排除|はいじょ} (exclusion), {妨害|ぼうがい} (obstruction), {阻止|そし} (prevention), {便乗|びんじょう} (taking advantage)
- **Character traits (5)**: {傲慢|ごうまん} (arrogance), {卑屈|ひくつ} (servile), {勇敢|ゆうかん} (brave), {堅実|けんじつ} (steady), {狡猾|こうかつ} (cunning)
- **Legal/business (4)**: {釈明|しゃくめい} (clarification), {賠償|ばいしょう} (compensation), {訴訟|そしょう} (lawsuit), {出資|しゅっし} (investment)
- **-化 transformation words (4)**: {可視化|かしか} (visualization), {形骸化|けいがいか} (becoming nominal), {老朽化|ろうきゅうか} (deterioration), {劣化|れっか} (degradation)
- **Comparison verbs (2)**: {上回|うわまわ}る (to exceed), {下回|したまわ}る (to fall below)
- **Other (2)**: {自粛|じしゅく} (self-restraint), {蒸発|じょうはつ} (evaporation)

Notable entry features:
- Antonym verb pair with cross-references: {上回|うわまわ}る ↔ {下回|したまわ}る
- -化 transformation words covering positive ({可視化|かしか}) and negative ({形骸化|けいがいか}, {老朽化|ろうきゅうか}, {劣化|れっか}) changes
- {自粛|じしゅく} with cultural context about COVID-19 pandemic usage and Japanese social values
- Information vocabulary useful for news comprehension: {隠蔽|いんぺい}, {捏造|ねつぞう}, {発覚|はっかく}, {暴露|ばくろ}
- Character trait vocabulary with nuanced distinctions between similar concepts
- Legal terminology for formal/news contexts: {賠償|ばいしょう}, {訴訟|そしょう}

Total entries: 7,539 → 7,569
Remaining candidates: ~588 → ~558

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 140)
Added 30 new dictionary entries from candidate_words.json, covering social/business suru-verbs, personality adjectives, verb pairs, and practical everyday vocabulary:

- **Social/business suru-verbs** (5): {普及|ふきゅう} (spread/diffusion), {浸透|しんとう} (permeation), {定着|ていちゃく} (establishment), {台頭|たいとう} (rise/emergence), {手配|てはい} (arrangement)
- **Formal expressions** (4): {恐縮|きょうしゅく} (grateful/apologetic), {不躾|ぶしつけ} (rude/blunt), {不手際|ふてぎわ} (mishandling), {不備|ふび} (deficiency)
- **Verb pairs** (4): {揺|ゆ}さぶる/{揺|ゆ}らぐ (shake/sway), {狭|せば}まる/{狭|せば}める (narrow intrans./trans.)
- **Personality adjectives** (4): {神経質|しんけいしつ} (nervous), {繊細|せんさい} (delicate), {臆病|おくびょう} (timid), {大胆|だいたん} (bold)
- **真っ〜 intensifiers** (4): {真|ま}っ{白|しろ} (pure white), {真|ま}っ{黒|くろ} (pitch black), {真|ま}っ{青|さお} (deep blue/pale), {真|ま}っ{暗|くら} (pitch dark)
- **Compound verbs** (2): {嵩|かさ}む (to mount up), {思|おも}い{浮|う}かぶ (to come to mind)
- **Other vocabulary** (7): {手元|てもと} (at hand), {余地|よち} (room/margin), {整頓|せいとん} (tidying up), {散策|さんさく} (stroll), ねだる (to beg for), くすぐる (to tickle), {拭|ぬぐ}う (to wipe)

Notable entry features:
- Personality adjective pairs with antonym cross-references: {臆病|おくびょう} ↔ {大胆|だいたん}
- Verb transitivity pairs with cross-references: {揺|ゆ}さぶる ↔ {揺|ゆ}らぐ, {狭|せば}める ↔ {狭|せば}まる
- Complete 真っ〜 color intensifier group with cross-references
- Business/formal expressions useful for professional contexts
- Social dynamics vocabulary: {普及|ふきゅう}, {浸透|しんとう}, {定着|ていちゃく}, {台頭|たいとう}

Total entries: 7,509 → 7,539
Remaining candidates: ~616 → ~588

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 139)
Added 30 new dictionary entries from candidate_words.json, plus one user-requested entry, covering transformation vocabulary, verbs, adjectives, time expressions, price/capacity terms, and practical nouns:

- **User-requested** (1): {卵|たまご}かけご{飯|はん} (TKG - raw egg on rice) with note about TKG abbreviation
- **-化 transformation words** (5): {活性化|かっせいか} (activation), {多様化|たようか} (diversification), {効率化|こうりつか} (streamlining), {自動化|じどうか} (automation), {最適化|さいてきか} (optimization)
- **Verbs** (5): {覆|くつがえ}す (to overturn), {懲|こ}りる (to learn one's lesson), {醸|かも}す (to brew/create atmosphere), {萎|な}える (to wilt/lose motivation), {紛|まぎ}れる (to be lost in/blend into)
- **-がる verbs** (2): {欲|ほ}しがる (to want - third person), {怖|こわ}がる (to be scared - third person)
- **Adjectives** (3): さりげない (casual/nonchalant), よそよそしい (distant/aloof), せこい (stingy/petty)
- **Time expressions** (4): {案|あん}の{定|じょう} (as expected), {当面|とうめん} (for the time being), {事前|じぜん} (beforehand), {事後|じご} (after the fact)
- **Price terms** (2): {値上|ねあ}げ (price increase), {値下|ねさ}げ (price decrease) - antonym pair with cross-references
- **Capacity terms** (3): {満員|まんいん} (full capacity), {満席|まんせき} (full/no seats), {空席|くうせき} (empty seat) - with cross-references
- **Holiday terms** (2): {連休|れんきゅう} (consecutive holidays), {祝日|しゅくじつ} (national holiday)
- **Practical nouns** (3): {備蓄|びちく} (stockpiling), {復興|ふっこう} (reconstruction), {消毒|しょうどく} (disinfection)

Notable entry features:
- TKG entry with cultural notes about this iconic Japanese breakfast and its social media abbreviation
- Complete -化 transformation pattern: 5 productive suru-verbs for describing process changes
- -がる verb pair explaining third-person emotion/desire expression in Japanese
- Antonym pairs with cross-references: {事前|じぜん} ↔ {事後|じご}, {値上|ねあ}げ ↔ {値下|ねさ}げ, {満席|まんせき} ↔ {空席|くうせき}
- Expressive verbs: {醸|かも}す (with sake-brewing etymology), {懲|こ}りる (learning from mistakes)
- Emergency/disaster vocabulary: {備蓄|びちく}, {復興|ふっこう}, {消毒|しょうどく}

Total entries: 7,479 → 7,509
Remaining candidates: ~645 → ~616

### 2026-01-20 (New Candidates - 100 Words Added, Session 138)
Added 100 new candidate words to `candidate_words.json` with balanced coverage across multiple categories:

**Psychological/Emotional States** (~15 words):
- Motivation/arousal: {奮起|ふんき} (stirring to action), {発奮|はっぷん} (being roused), {衝動|しょうどう} (impulse), {憧憬|しょうけい} (longing)
- Mental states: {惰性|だせい} (inertia), {本能|ほんのう} (instinct), {直感|ちょっかん} (intuition), {没頭|ぼっとう} (immersion)

**Information/Actions Vocabulary** (~20 words):
- Concealment: {隠蔽|いんぺい} (cover-up), {捏造|ねつぞう} (fabrication), {歪曲|わいきょく} (distortion), {改竄|かいざん} (falsification)
- Consideration/perception: {熟考|じゅっこう} (careful consideration), {黙認|もくにん} (tacit approval), {誇示|こじ} (showing off), {看過|かんか} (overlooking)
- Revelation: {発覚|はっかく} (coming to light), {告発|こくはつ} (disclosure), {暴露|ばくろ} (exposure), {発掘|はっくつ} (excavation)

**Social/Political Actions** (~15 words):
- Elimination/change: {排除|はいじょ} (exclusion), {淘汰|とうた} (selection), {駆逐|くちく} (expulsion), {更迭|こうてつ} (replacement), {抜擢|ばってき} (promotion)
- Obstruction: {阻止|そし} (prevention), {抑止|よくし} (deterrence), {妨害|ぼうがい} (obstruction), {横槍|よこやり} (interference)
- Social dynamics: {迎合|げいごう} (pandering), {便乗|びんじょう} (taking advantage)

**Character/Personality Traits** (~15 words):
- Negative: {傲慢|ごうまん} (arrogance), {横暴|おうぼう} (tyranny), {専横|せんおう} (despotism), {卑屈|ひくつ} (servile), {狡猾|こうかつ} (cunning)
- Positive: {勇敢|ゆうかん} (brave), {果敢|かかん} (resolute), {堅実|けんじつ} (steady), {着実|ちゃくじつ} (reliable)
- Excellence: {卓越|たくえつ} (excellence), {傑出|けっしゅつ} (outstanding), {巧妙|こうみょう} (ingenious), {凌駕|りょうが} (surpassing)

**Explanation/Apology** (~10 words):
- Speech acts: {弁解|べんかい} (explanation), {弁明|べんめい} (vindication), {釈明|しゃくめい} (clarification), {陳謝|ちんしゃ} (formal apology)
- Financial resolution: {賠償|ばいしょう} (compensation), {償還|しょうかん} (repayment), {弁済|べんさい} (reimbursement)

**Business/Finance** (~10 words):
- Investment: {出資|しゅっし} (investment), {資金繰|しきんぐ}り (cash flow management)
- Calculation: {充当|じゅうとう} (allocation), {計上|けいじょう} (recording), {換算|かんさん} (conversion)
- Legal: {差|さ}し{押|お}さえ (seizure), {訴訟|そしょう} (lawsuit), {告訴|こくそ} (accusation)

**Transformation/Change (-化 words)** (~25 words):
- Process improvements: {活性化|かっせいか} (activation), {効率化|こうりつか} (streamlining), {自動化|じどうか} (automation), {最適化|さいてきか} (optimization), {可視化|かしか} (visualization), {簡略化|かんりゃくか} (simplification)
- Social changes: {多様化|たようか} (diversification), {民営化|みんえいか} (privatization), {国有化|こくゆうか} (nationalization), {商業化|しょうぎょうか} (commercialization), {大衆化|たいしゅうか} (popularization)
- Negative changes: {形骸化|けいがいか} (becoming nominal), {空洞化|くうどうか} (hollowing out), {硬直化|こうちょくか} (rigidity), {陳腐化|ちんぷか} (obsolescence), {老朽化|ろうきゅうか} (deterioration)
- Physical/chemical: {劣化|れっか} (degradation), {腐敗|ふはい} (decay), {腐食|ふしょく} (corrosion), {風化|ふうか} (weathering), {還元|かんげん} (reduction), {蒸発|じょうはつ} (evaporation), {凝縮|ぎょうしゅく} (condensation), {溶解|ようかい} (dissolution)

**Other** (~10 words):
- Verbs: {上回|うわまわ}る (to exceed), {下回|したまわ}る (to fall below), {聞|き}き{逃|のが}す (to mishear), {言|い}い{逃|のが}れる (to make excuses)
- Industrial: {採掘|さいくつ} (mining), {掘削|くっさく} (drilling), {操業|そうぎょう} (operation)
- Control: {自制|じせい} (self-control), {自粛|じしゅく} (self-restraint)
- Actions: {暴挙|ぼうきょ} (outrage), {蛮行|ばんこう} (barbaric act)

Notable features:
- Strong coverage of transformation vocabulary (-化 words) useful for discussing social/economic changes
- Business/legal terminology for professional contexts
- Character trait vocabulary for describing personalities
- Information-related vocabulary (concealment, revelation, consideration)
- Self-control and restraint vocabulary relevant to Japanese cultural values

Candidate count: 544 → 645

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 137)
Added 30 new dictionary entries from candidate_words.json, covering musical instruments/terminology, regional dialects from multiple areas, and practical everyday vocabulary:

- **Musical instruments (3)**: {打楽器|だがっき} (percussion instrument), {管楽器|かんがっき} (wind instrument), {弦楽器|げんがっき} (string instrument)
- **Music terminology (7)**: {吹奏楽|すいそうがく} (wind band music), {調律|ちょうりつ} (tuning), {転調|てんちょう} (modulation), {休符|きゅうふ} (rest), {独奏|どくそう} (solo), サックス (saxophone), トランペット (trumpet)
- **Kansai dialect (5)**: せや (that's right), わや (mess), ええやん (it's good), どないやねん (what's up with that)
- **Kyushu dialect (2)**: ばってん (but), よか (good)
- **Hokkaido dialect (2)**: なまら (very), したっけ (bye/well then)
- **Tohoku dialect (1)**: いずい (uncomfortable)
- **Edo origin (1)**: べらぼう (ridiculously)
- **Technology/modern (2)**: オフライン (offline), モバイルバッテリー (portable battery)
- **Business/documents (5)**: {資質|ししつ} (qualities), {届出|とどけで} (notification), {引落|ひきおと}し (automatic deduction), {借入|かりいれ} (borrowing), {届|とど}け (report)
- **Other (2)**: リハーサル (rehearsal), クラフトビール (craft beer), {潤滑油|じゅんかつゆ} (lubricant)

Notable entry features:
- Complete musical instrument classification group: {打楽器|だがっき} ↔ {管楽器|かんがっき} ↔ {弦楽器|げんがっき} with cross-references
- Comprehensive regional dialect coverage: Kansai (せや, わや, ええやん, どないやねん), Kyushu (ばってん, よか), Hokkaido (なまら, したっけ), Tohoku (いずい)
- べらぼう with Edo period etymology and cultural notes about {時代劇|じだいげき}
- いずい with explanation of this "untranslatable" Tohoku dialect word describing subtle discomfort
- {吹奏楽|すいそうがく} with cultural context about popularity in Japanese schools
- Financial/administrative vocabulary: {届出|とどけで}, {引落|ひきおと}し, {借入|かりいれ}

Total entries: 7,449 → 7,479
Remaining candidates: ~574 → ~544

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 136)
Added 30 new dictionary entries from candidate_words.json, covering cooking vocabulary, adverbs/mimetics, business/IT terms, abstract nouns, and Kansai dialect expressions:

- **Cooking/food items (4)**: {卵焼|たまごや}きご{飯|はん} (rice with tamagoyaki), {塩梅|あんばい} (seasoning/condition), {擂|す}り{鉢|ばち} (mortar), {吟味|ぎんみ} (scrutiny)
- **Cooking verbs (4)**: {浸|ひた}す (to soak), {拵|こしら}える (to prepare), {裏返|うらがえ}す (to flip), {削|そ}ぐ (to slice thin)
- **Adverbs/mimetics (8)**: ずばり (directly), てっきり (surely/mistakenly), しぶしぶ (reluctantly), やたら (excessively), きょろきょろ (looking around), もたもた (sluggishly), そそくさ (hurriedly), {逐一|ちくいち} (one by one), まごまご (bewildered)
- **Business/IT terms (6)**: {査定|さてい} (assessment), {精査|せいさ} (close examination), {刷新|さっしん} (reform), {復旧|ふっきゅう} (recovery), {切|き}り{替|か}え (switching), {脆弱|ぜいじゃく} (vulnerability)
- **Abstract nouns (3)**: {疲弊|ひへい} (exhaustion), {逸脱|いつだつ} (deviation), {萎縮|いしゅく} (atrophy)
- **Kansai dialect (4)**: ほんま (really), なんでやねん (what the heck), おおきに (thank you), あかん (no good)

Notable entry features:
- Traditional Japanese cooking vocabulary including {擂|す}り{鉢|ばち} (mortar) with cultural context
- Complete Kansai dialect coverage: ほんま, なんでやねん, おおきに, あかん with manzai comedy context for なんでやねん
- Useful mimetic expressions for describing behaviors and states
- Business/IT terminology including {脆弱|ぜいじゃく} with security context
- {塩梅|あんばい} with etymology note about salt and plum vinegar

Total entries: 7,419 → 7,449
Remaining candidates: ~603 → ~574

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 135)
Added 30 new dictionary entries from candidate_words.json, focusing on cooking vocabulary, business documents, seal terminology, office supplies, infrastructure/housing, and employment terms:

- **Cooking cuts (6)**: みじん{切|ぎ}り (finely chopped), {千切|せんぎ}り (julienne), {輪切|わぎ}り (round slices), {薄切|うすぎ}り (thin slices), {厚切|あつぎ}り (thick slices), {下処理|したしょり} (preliminary preparation)
- **Food items (4)**: {油揚|あぶらあ}げ (deep-fried tofu), {厚揚|あつあ}げ (thick fried tofu), ちくわ (tube-shaped fish cake), しらたき (konjac noodles)
- **Business documents (6)**: {議事録|ぎじろく} (meeting minutes), {稟議|りんぎ} (approval request), {見積書|みつもりしょ} (quotation), {仕様書|しようしょ} (specification document), {申請書|しんせいしょ} (application form), {伝票|でんぴょう} (slip/voucher)
- **Seal terminology (4)**: {押印|おういん} (affixing seal), {認印|みとめいん} (personal seal), {実印|じついん} (registered seal), {印鑑登録|いんかんとうろく} (seal registration)
- **Office supplies (3)**: シュレッダー (shredder), トナー (toner), {紙詰|かみづ}まり (paper jam)
- **Infrastructure/housing (4)**: {配管|はいかん} (plumbing), ブレーカー (circuit breaker), {収納|しゅうのう} (storage), {日当|ひあ}たり (sun exposure)
- **Employment (3)**: {内定|ないてい} (unofficial job offer), {定年|ていねん} (retirement age), {控除|こうじょ} (deduction)

Notable entry features:
- Complete Japanese seal system vocabulary: {押印|おういん} → {認印|みとめいん} → {実印|じついん} → {印鑑登録|いんかんとうろく} with detailed registration process and requirements
- Comprehensive cooking cut terms covering all common Japanese cutting styles
- Traditional Japanese food items (tofu products, konjac)
- Japanese employment system vocabulary: {内定|ないてい} with explanation of Japan's unique job offer system
- Infrastructure vocabulary useful for housing: {配管|はいかん}, ブレーカー, {収納|しゅうのう}, {日当|ひあ}たり
- Business document types essential for office work in Japan

Total entries: 7,389 → 7,419
Remaining candidates: ~633 → ~603

### 2026-01-20 (New Candidates - 100 Words Added, Session 134)
Added 100 new candidate words to `candidate_words.json` with balanced coverage across multiple categories:

**Business Documents & Seals** (~20 words):
- Seal terminology: {押印|おういん} (seal impression), {捺印|なついん} (seal impression), {認印|みとめいん} (personal seal), {実印|じついん} (registered seal), {印鑑登録|いんかんとうろく} (seal registration)
- Document types: {議事録|ぎじろく} (meeting minutes), {稟議|りんぎ} (approval request), {委任状|いにんじょう} (power of attorney), {誓約書|せいやくしょ} (written pledge), {覚書|おぼえがき} (memorandum), {見積書|みつもりしょ} (quotation), {発注書|はっちゅうしょ} (purchase order), {注文書|ちゅうもんしょ} (order form), {仕様書|しようしょ} (specification document), {申請書|しんせいしょ} (application form), {伝票|でんぴょう} (voucher)

**Office & Business Terms** (~15 words):
- Office supplies: シュレッダー (shredder), {穴|あな}あけパンチ (hole punch), カートリッジ (cartridge), トナー (toner), コピー{用紙|ようし} (copy paper), {裏紙|うらがみ} (scratch paper), {両面印刷|りょうめんいんさつ} (double-sided printing), {紙詰|かみづ}まり (paper jam)
- Business records: {帳簿|ちょうぼ} (account book), {台帳|だいちょう} (register)
- Retail terms: {陳列|ちんれつ} (display), {棚卸|たなおろ}し (inventory), {問屋|とんや} (wholesaler), {粗利|あらり} (gross profit)

**Housing & Infrastructure** (~12 words):
- Housing: {築年数|ちくねんすう} (building age), {更地|さらち} (vacant lot), {日当|ひあ}たり (sun exposure), {収納|しゅうのう} (storage)
- Infrastructure: {水道管|すいどうかん} (water pipe), {配管|はいかん} (plumbing), ブレーカー (circuit breaker), {漏電|ろうでん} (electrical leak), {節水|せっすい} (water conservation), {雨漏|あまも}り (roof leak), {水漏|みずも}れ (water leak)

**Employment & Salary** (~12 words):
- Career: {内定|ないてい} (unofficial job offer), {定年|ていねん} (retirement age), {早期退職|そうきたいしょく} (early retirement), {退職金|たいしょくきん} (retirement allowance)
- Compensation: {日給|にっきゅう} (daily wage), {歩合|ぶあい} (commission), {歩合制|ぶあいせい} (commission-based), {積立|つみたて} (savings), {控除|こうじょ} (deduction)

**Cooking Cuts & Food Items** (~20 words):
- Cutting terms: みじん{切|ぎ}り (finely chopped), {千切|せんぎ}り (julienne), {乱切|らんぎ}り (irregular cut), {薄切|うすぎ}り (thin sliced), {厚切|あつぎ}り (thick sliced), {輪切|わぎ}り (round slices), {短冊切|たんざくぎ}り (rectangle cut), {角切|かくぎ}り (diced), いちょう{切|ぎ}り (quarter rounds), {半月切|はんげつぎ}り (half-moon slices), {斜|なな}め{切|ぎ}り (diagonal cut)
- Kitchen items: {泡立|あわだ}て{器|き} (whisk), すくい{網|あみ} (strainer), {灰汁|あく}とり (skimming)
- Food items: {油揚|あぶらあ}げ (deep-fried tofu), {厚揚|あつあ}げ (thick fried tofu), がんもどき (fried tofu fritter), ちくわ (tube fish cake), さつま{揚|あ}げ (fried fish cake), しらたき (konjac noodles), {高野豆腐|こうやどうふ} (freeze-dried tofu), {車麩|くるまふ} (ring-shaped wheat gluten), お{麩|ふ} (wheat gluten), {湯葉|ゆば} (tofu skin), {切|き}り{干|ぼ}し{大根|だいこん} (dried radish strips), ひじき (hijiki seaweed), とろろ{昆布|こんぶ} (shredded kelp), {干|ほ}し{椎茸|しいたけ} (dried shiitake)

**Compound Verbs & Weather** (~10 words):
- Compound verbs: {聞|き}き{流|なが}す (to let pass), {聞|き}き{込|こ}む (to investigate), {読|よ}み{返|かえ}す (to reread), {見慣|みな}れる (to get used to seeing), {乗|の}り{過|す}ごす (to ride past), {降|ふ}り{注|そそ}ぐ (to pour down)
- Weather: {土砂降|どしゃぶ}り (downpour)
- Processing: {下処理|したしょり} (preliminary preparation), {水気|みずけ} (moisture)

**Other** (~11 words):
- Storage battery: {蓄電池|ちくでんち} (storage battery)
- Medical: {検診|けんしん} (medical checkup)
- Logistics: {売値|うりね} (selling price), {欠品|けっぴん} (out of stock), {入荷|にゅうか} (arrival of goods), {梱包|こんぽう} (packing), {荷造|にづく}り (packing for shipping), {荷解|にほど}き (unpacking), {着払|ちゃくばら}い (cash on delivery)
- Kitchenware: {寿司桶|すしおけ} (sushi tub), おひつ (rice container), {土鍋|どなべ} (earthenware pot)

Notable features:
- Comprehensive Japanese document vocabulary with seal terminology (essential for business/legal contexts)
- Cooking vocabulary covering all common cutting terms and traditional food items
- Housing and infrastructure terms for daily life in Japan
- Employment/salary terminology for workplace contexts
- Strong practical vocabulary useful for intermediate-advanced learners

Candidate count: 533 → 633

### 2026-01-19 (Vocabulary Tier Realignment Complete - Phase 4 & 5)
Completed the vocabulary tier realignment project (Phases 4 and 5):

**Phase 4: Assigned 200 unassigned entries**
- All previously unassigned entries have been assigned to the general tier
- Categories included: four-character idioms (yojijukugo), proverbs, traditional Japanese items, modern tech/business terms, medical terms, work terms, -teki adjectives, onomatopoeia, and compound verbs

**Phase 5: Validation and finalization**
- Verified final tier counts meet targets:
  - Basic: 795 (target: 600-800) ✓
  - Core: 1,998 (target: 1,600-2,000) ✓
  - General: 4,566 (no limit) ✓
  - Unassigned: 0 (target: 0) ✓
- Ran full validation (7,357/7,359 entries valid)
- Updated indexes and rebuilt flat HTML
- Updated PROJECT_STATUS.md

The tier realignment project is now complete. All 7,359 dictionary entries have vocabulary tier assignments that meet the target ranges specified in the vocabulary-tiers skill guidelines.

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
