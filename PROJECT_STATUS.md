# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-18
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
- **Total entries**: 6,961
- **Vocabulary tier assignment**: Basic: 1,113 | Core: 4,895 | General: 510 | Unassigned: 367
- **Candidate words**: ~767 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 600-800 fundamental words for basic communication
- **Core**: 1,600-2,000 words for adult-level communication
- **General**: All other vocabulary useful for learners

Most entries have provisional tier assignments. These values are subject to revision as the dictionary develops and tier assignment policies are refined.

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

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 113)
Added 30 new dictionary entries from candidate_words.json, focusing on idiomatic body part expressions and adverbs:

- **Body part idioms with {気|き}** (4): {気|き}が{利|き}く (attentive), {気|き}が{重|おも}い (reluctant), {気|き}が{短|みじか}い (short-tempered), {気|き}が{散|ち}る (distracted)
- **Body part idioms with {口|くち}** (2): {口|くち}が{軽|かる}い (loose-lipped), {口|くち}が{堅|かた}い (tight-lipped)
- **Body part idioms with other parts** (9): {腹|はら}が{立|た}つ (angry), {顔|かお}が{広|ひろ}い (well-connected), {足|あし}が{出|で}る (over budget), {手|て}が{離|はな}せない (too busy), {目|め}が{離|はな}せない (captivating), {肩身|かたみ}が{狭|せま}い (feel awkward), {耳|みみ}が{痛|いた}い (hard to hear), {頭|あたま}が{固|かた}い (stubborn), {腰|こし}が{低|ひく}い (humble)
- **Body action expressions** (12): {首|くび}を{振|ふ}る (shake head), {肩|かた}をすくめる (shrug), {眉|まゆ}をひそめる (frown), {足|あし}を{運|はこ}ぶ (visit), {顔|かお}を{出|だ}す (show up), {胸|むね}を{張|は}る (be proud), {腰|こし}を{据|す}える (settle down), {息|いき}を{呑|の}む (gasp), {耳|みみ}を{傾|かたむ}ける (listen carefully), {目|め}を{通|とお}す (skim), {手|て}を{抜|ぬ}く (cut corners), {足|あし}を{引|ひ}っ{張|ぱ}る (drag down)
- **Adverbs** (3): じろじろ (staring fixedly), とことん (thoroughly), ひょっとして (perhaps)

Notable entry features:
- Comprehensive coverage of Japanese body part idioms with {気|き}, {口|くち}, {手|て}, {足|あし}, {目|め}, {耳|みみ}, {頭|あたま}, {腹|はら}, {胸|むね}, {腰|こし}, {肩|かた}, {首|くび}, {眉|まゆ}, {息|いき}
- Antonym pairs: {口|くち}が{軽|かる}い ↔ {口|くち}が{堅|かた}い, {頭|あたま}が{固|かた}い ↔ {頭|あたま}が{柔|やわ}らかい
- Contrast pairs: {手|て}が{離|はな}せない (busy with hands) vs {目|め}が{離|はな}せない (can't stop watching)
- Cultural notes on Japanese body metaphors ({腹|はら} as seat of emotions)

Total entries: 6,931 → 6,961
Remaining candidates: ~797 → ~767

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 112)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, na-adjectives, and social/work vocabulary:

- **Compound verbs** (15): {読|よ}み{飛|と}ばす (skip reading), {書|か}き{足|た}す (add in writing), {放|ほう}り{込|こ}む (throw in), {焼|や}き{付|つ}ける (burn in/imprint), {弾|はじ}き{出|だ}す (calculate), {貼|は}り{付|つ}ける (paste), {吐|は}き{出|だ}す (spit out), {掘|ほ}り{起|お}こす (dig up), {浮|う}かび{上|あ}がる (emerge), {言|い}い{当|あ}てる (guess correctly), {見|み}せびらかす (show off), {練|ね}り{上|あ}げる (refine), {蹴飛|けと}ばす (kick away), {付|つ}け{足|た}す (add on), {取|と}り{繕|つくろ}う (keep up appearances)
- **Na-adjectives** (5): {気軽|きがる} (casual), {軽率|けいそつ} (rash), {大雑把|おおざっぱ} (rough), {几帳面|きちょうめん} (methodical), {窮屈|きゅうくつ} (cramped)
- **Work/Social nouns** (10): {世帯|せたい} (household), {手掛|てが}かり (clue), {見込|みこ}み (prospect), {取|と}り{柄|え} (merit), {言|い}い{分|ぶん} (one's say), {幹部|かんぶ} (executive), {中堅|ちゅうけん} (mid-level), {新米|しんまい} (newcomer), {常連|じょうれん} (regular customer), {運命|うんめい} (fate)

Notable entry features:
- Strong compound verb coverage: ～{飛|と}ばす (skip), ～{足|た}す (add), ～{込|こ}む (into), ～{付|つ}ける (attach), ～{出|だ}す (out), ～{起|お}こす (dig up), ～{上|あ}がる (emerge), ～{当|あ}てる (hit mark), ～{上|あ}げる (complete)
- Personality contrast pair: {大雑把|おおざっぱ} (rough) ↔ {几帳面|きちょうめん} (meticulous)
- Workplace hierarchy vocabulary: {幹部|かんぶ} → {中堅|ちゅうけん} → {新米|しんまい}
- Customer relationships: {常連|じょうれん} (regular) vs first-time customers

Total entries: 6,901 → 6,931
Remaining candidates: ~827 → ~797

### 2026-01-18 (New Candidates - 100 Words Added, Session 111)
Added 100 new candidate words to `candidate_words.json` with balanced coverage across multiple categories:

**Compound Verbs** (~20 words):
- {読|よ}み{飛|と}ばす (skip reading), {書|か}き{足|た}す (add in writing), {放|ほう}り{込|こ}む (throw in), {焼|や}き{付|つ}ける (burn in)
- {弾|はじ}き{出|だ}す (calculate), {貼|は}り{付|つ}ける (paste), {吐|は}き{出|だ}す (spit out), {掘|ほ}り{起|お}こす (dig up)
- {浮|う}かび{上|あ}がる (emerge), {言|い}い{当|あ}てる (guess correctly), {見|み}せびらかす (show off), {練|ね}り{上|あ}げる (refine)
- {蹴飛|けと}ばす (kick away), {付|つ}け{足|た}す (add on), {取|と}り{繕|つくろ}う (keep up appearances)

**Idiomatic Expressions with Body Parts** (~30 words):
- 気 expressions: {気|き}が{利|き}く (attentive), {気|き}が{重|おも}い (reluctant), {気|き}が{短|みじか}い (short-tempered), {気|き}が{散|ち}る (distracted)
- 口 expressions: {口|くち}が{軽|かる}い (loose-lipped), {口|くち}が{堅|かた}い (discreet)
- Body part idioms: {腹|はら}が{立|た}つ (angry), {顔|かお}が{広|ひろ}い (well-connected), {肩身|かたみ}が{狭|せま}い (awkward)
- Action expressions: {眉|まゆ}をひそめる (frown), {足|あし}を{運|はこ}ぶ (visit), {顔|かお}を{出|だ}す (show up), {胸|むね}を{張|は}る (be proud)
- Breath expressions: {息|いき}を{呑|の}む (gasp), {息|いき}を{潜|ひそ}める (hold breath)

**Adjectives and Personality Words** (~15 words):
- Adjectives: {奥深|おくぶか}い (profound), {生|なま}ぬるい (lukewarm), {差|さ}し{出|で}がましい (presumptuous)
- Personality: {気|き}まぐれ (capricious), {理不尽|りふじん} (unreasonable), {横柄|おうへい} (arrogant), {潔|いさぎよ}い (graceful)

**Nouns and Abstract Concepts** (~20 words):
- Social: {世帯|せたい} (household), {配偶者|はいぐうしゃ} (spouse), {世話人|せわにん} (organizer)
- Abstract: {見込|みこ}み (prospect), {手掛|てがか}かり (clue), {成|な}り{行|ゆ}き (outcome)
- Psychology: {先入観|せんにゅうかん} (preconception), {固定観念|こていかんねん} (fixed idea), {既成概念|きせいがいねん} (conventional notion)

**Adverbs and Onomatopoeia** (~15 words):
- Adverbs: とことん (thoroughly), ひょっとして (perhaps), まして (let alone), たいして (not very)
- Onomatopoeia: じろじろ (staring), ちらちら (flickering), めきめき (remarkably), むしゃむしゃ (munching)

Notable features:
- Strong focus on idiomatic body-part expressions (気・口・目・耳・手・足・腹・胸・腰・首・肩)
- Practical compound verbs for everyday actions
- Adjectives describing personality and social behavior
- Abstract nouns for thinking and social concepts

Candidate count: 727 → 827

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 110)
Added 30 new dictionary entries from candidate_words.json, covering adjectives, nouns, compound verbs, and onomatopoeia:

- **I-adjectives** (6): {渋|しぶ}い (astringent/refined), {青臭|あおくさ}い (grassy/immature), {生臭|なまぐさ}い (fishy), {焦|こ}げ{臭|くさ}い (burnt-smelling), {紛|まぎ}らわしい (confusing), {馴|な}れ{馴|な}れしい (overly familiar)
- **Na-adjectives (～的)** (5): {画期的|かっきてき} (groundbreaking), {徹底的|てっていてき} (thorough), {決定的|けっていてき} (decisive), {衝撃的|しょうげきてき} (shocking), {劇的|げきてき} (dramatic)
- **Business/Career nouns** (5): {左遷|させん} (demotion), {栄転|えいてん} (promotion with transfer), {手取|てど}り (take-home pay), {逆転|ぎゃくてん} (reversal), {敗退|はいたい} (defeat)
- **Writing/Editing nouns** (3): {下書|したが}き (draft), {添削|てんさく} (correction), {余白|よはく} (margin)
- **Social nouns** (2): {顔見知|かおみし}り (acquaintance), {仲間外|なかまはず}れ (exclusion from group)
- **Compound verbs** (4): {突|つ}き{出|だ}す (to thrust out), {叩|たた}き{落|お}とす (to knock down), {這|は}い{出|で}る (to crawl out), {切|き}り{崩|くず}す (to cut into/dip into savings)
- **Onomatopoeia** (3): ぬめぬめ (slimy), コリコリ (crunchy-chewy), プチプチ (popping/bubble wrap)
- **Loanwords** (2): メリット (advantage), デメリット (disadvantage)

Notable entry features:
- Smell-related adjective series: {青臭|あおくさ}い, {生臭|なまぐさ}い, {焦|こ}げ{臭|くさ}い (grassy, fishy, burnt)
- ～{的|てき} na-adjective group for formal/written Japanese: {画期的|かっきてき}, {徹底的|てっていてき}, etc.
- Career vocabulary pair: {左遷|させん} (demotion) ↔ {栄転|えいてん} (promotion)
- Compound verbs with clear auxiliary patterns: ～{出|だ}す (outward), ～{落|お}とす (down), ～{崩|くず}す (break down)
- Food texture onomatopoeia: コリコリ for cartilage-like crunch, プチプチ for popping fish roe

Total entries: 6,871 → 6,901
Remaining candidates: ~755 → ~727

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 109)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, formal grammar patterns, modern vocabulary, and everyday nouns:

- **Compound verbs** (9): {打|う}ち{出|だ}す (to launch), {引|ひ}き{付|つ}ける (to attract), {打|う}ち{消|け}す (to negate), {押|お}し{切|き}る (to overcome), {差|さ}し{入|い}れる (to insert/bring refreshments), {持|も}ちかける (to propose), {持|も}ち{堪|こた}える (to hold out), {取|と}り{付|つ}ける (to install), {押|お}し{進|すす}める (to push forward)
- **Formal grammar patterns** (6): において (in/at), に{対|たい}して (towards), によって (by/depending on), として (as), にとって (for someone), に{伴|ともな}い (accompanying)
- **Tech/Digital** (2): DM (direct message), プライバシー (privacy)
- **Everyday nouns** (8): {運休|うんきゅう} (service suspension), {発着|はっちゃく} (arrivals/departures), {下味|したあじ} (preliminary seasoning), {連|つ}れ{合|あ}い (spouse), {運用|うんよう} (operation), {居住|きょじゅう} (residence), {妄想|もうそう} (delusion), {宣告|せんこく} (verdict)
- **Verbs** (2): {痺|しび}れる (to become numb), かぶれる (to get a rash)
- **Slang** (1): ガチで (seriously)
- **Formal** (1): {遺憾|いかん} (regrettable)
- **Cooking** (1): {灰汁|あく}{抜|ぬ}き (removing bitterness)

Notable entry features:
- Comprehensive formal grammar patterns (において, に対して, etc.) essential for written Japanese
- Compound verb patterns: ～{切|き}る for completion, ～{出|だ}す for starting/launching
- Youth slang ガチで with etymology from sumo ガチンコ
- {差|さ}し{入|い}れる covering both literal insertion and bringing refreshments to people
- Cooking terminology {灰汁|あく}{抜|ぬ}き with common methods and ingredients

Total entries: 6,841 → 6,871
Remaining candidates: ~784 → ~755

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 108)
Added 30 new dictionary entries from candidate_words.json, covering verbs, loanwords, expressions, and nouns:

- **Verbs** (3): {押|お}し{入|い}る (to break in), {降|お}り{立|た}つ (to arrive/land), {萎縮|いしゅく}する (to shrink/be intimidated)
- **Business loanwords** (6): フィードバック (feedback), プロジェクト (project), タスク (task), デッドライン (deadline), キャンセル (cancel), マネジメント (management)
- **Food/Lifestyle loanwords** (4): カフェ (cafe), パスタ (pasta), ピザ (pizza), アイス (ice cream)
- **Housing** (2): ロフト (loft), バルコニー (balcony)
- **Sports abbreviations** (3): バスケ (basketball), バレー (volleyball), スノボ (snowboarding)
- **Expressions/Grammar** (4): にも{関|かか}わらず (in spite of), いずれにせよ (in any case), ともかく (anyway), っぽい (-ish suffix)
- **Nouns** (8): {一人前|いちにんまえ} (full portion/independent person), {一部|いちぶ} (part), {採択|さいたく} (adoption), {識別|しきべつ} (identification), {沿革|えんかく} (history/development), {斑点|はんてん} (spot), {末端|まったん} (end/tip), {悔|くや}しさ (frustration)

Notable entry features:
- Compound verbs: {押|お}し{入|い}る (criminal/forceful entry), {降|お}り{立|た}つ (literary/news context for arrivals)
- Business vocabulary common in Japanese workplaces (タスク, デッドライン, マネジメント)
- Youth-culture sports abbreviations (バスケ, バレー, スノボ) with parent word cross-references
- Productive suffix っぽい with semantic breakdown (resemblance, tendency, excess)
- {一人前|いちにんまえ} covering both food portions and personal maturity meanings

Total entries: 6,811 → 6,841
Remaining candidates: 804 → 784

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 107)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, adjectives, nouns, and onomatopoeia:

- **Compound verbs** (6): {書|か}き{留|と}める (to write down), {切|き}り{出|だ}す (to bring up), {打|う}ち{上|あ}げる (to launch/wrap-up party), {押|お}し{寄|よ}せる (to surge), {飛|と}び{降|お}りる (to jump down), {差|さ}し{掛|か}かる (to approach)
- **I-adjectives** (4): せわしない (restless), えげつない (nasty), おぼつかない (uncertain), いたわしい (pitiful)
- **Na-adjectives** (2): {特徴的|とくちょうてき} (characteristic), {防御的|ぼうぎょてき} (defensive)
- **Nouns - Business/Formal** (6): {告白|こくはく} (confession), {報告書|ほうこくしょ} (report), {成果|せいか} (result), {開発|かいはつ} (development), {概要|がいよう} (summary), {謝罪|しゃざい} (apology)
- **Nouns - Daily life** (4): {物件|ぶっけん} (property), {遅延|ちえん} (delay), {海藻|かいそう} (seaweed), {蚊取|かと}り{線香|せんこう} (mosquito coil)
- **Nouns - Abstract** (3): {錯覚|さっかく} (illusion), {幻想|げんそう} (fantasy), リスク (risk)
- **Onomatopoeia/Adverbs** (5): どっと (in a rush), むずむず (itching), うずうず (eager), くらくら (dizzy), しれっと (nonchalantly)

Notable entry features:
- Compound verb patterns: ～{留|と}める for securing/noting, ～{上|あ}げる for launching, ～{寄|よ}せる for gathering/surging
- Expressive i-adjectives including Kansai-origin えげつない and literary おぼつかない
- Business vocabulary ({報告書|ほうこくしょ}, {成果|せいか}, {開発|かいはつ}) common in corporate contexts
- Real estate vocabulary ({物件|ぶっけん}) and train terminology ({遅延|ちえん}{証明書|しょうめいしょ})
- Japanese summer icons: {蚊取|かと}り{線香|せんこう} with cultural notes on pig-shaped holders
- Onomatopoeia contrasting similar concepts: むずむず (physical itch) vs うずうず (eager anticipation)

Total entries: 6,781 → 6,811
Remaining candidates: 833 → 804

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 106)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, adjectives, adverbs, onomatopoeia, and modern vocabulary:

- **Compound verbs** (5): {受|う}け{継|つ}ぐ (to inherit), {差|さ}し{引|ひ}く (to deduct), {打|う}ち{切|き}る (to discontinue), {振|ふ}り{切|き}る (to shake off), {飛|と}び{付|つ}く (to jump at)
- **I-adjectives** (5): あどけない (innocent), いじらしい (touching), けたたましい (shrill), しおらしい (meek), ふてぶてしい (brazen)
- **Na-adjectives** (3): {閉鎖的|へいさてき} (exclusive), {包括的|ほうかつてき} (comprehensive), {暫定的|ざんていてき} (provisional)
- **Adverbs** (4): あくまで (to the end), おのずと (naturally), しみじみ (deeply), まんまと (completely fooled)
- **Onomatopoeia** (2): くねくね (winding), かりかり (crispy)
- **Verbs** (2): {呆|あき}れる (to be appalled), ばれる (to be found out)
- **Modern vocabulary** (4): スクショ (screenshot), ワンオペ (one-person operation), イクメン (hands-on father), {不動産|ふどうさん} (real estate)
- **Family terms** (2): {義母|ぎぼ} (mother-in-law), {義父|ぎふ} (father-in-law)
- **Abstract nouns** (3): {比率|ひりつ} (ratio), {切|せつ}なさ (heartache), {懐|なつ}かしさ (nostalgia)

Notable entry features:
- Compound verb patterns: ～{継|つ}ぐ for inheritance, ～{切|き}る for completion/severing
- Expressive i-adjectives for describing people's qualities and sounds
- ～{的|てき} na-adjectives common in formal/written Japanese
- Adverbs for emphasis and nuance in natural speech
- Modern slang: ワンオペ (from restaurant industry to parenting), イクメン (childcare-involved fathers)
- Emotion nouns formed from adjectives: {切|せつ}ない→{切|せつ}なさ, {懐|なつ}かしい→{懐|なつ}かしさ

Total entries: 6,751 → 6,781
Remaining candidates: 861 → 833

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 104)
Added 30 new dictionary entries from candidate_words.json, covering personality traits, emotions, cooking, cultural concepts, and modern business vocabulary:

- **Personality/Character traits** (8): {鈍感|どんかん} (insensitive), {敏感|びんかん} (sensitive), {不器用|ぶきよう} (clumsy), {頑固|がんこ} (stubborn), {無口|むくち} (taciturn), {口下手|くちべた} (inarticulate), せっかち (impatient), そそっかしい (careless)
- **Emotions/Mental states** (5): {悔|く}い (regret), {情|なさ}け (compassion), {悩|なや}み (worry), {思|おも}いやり (consideration), {億劫|おっくう} (bothersome)
- **Japanese cultural concepts** (3): やり{甲斐|がい} (sense of fulfillment), {生|い}き{甲斐|がい} (ikigai - purpose in life), {志|こころざし} (aspiration)
- **Cooking vocabulary** (4): {火加減|ひかげん} (heat level), {手際|てぎわ} (skill/efficiency), コツ (knack), {隠|かく}し{味|あじ} (secret ingredient)
- **I-adjective** (1): {香|こう}ばしい (fragrant/savory)
- **Adverbs** (5): {尚更|なおさら} (all the more), {一切|いっさい} (entirely), {最早|もはや} (no longer), {強|し}いて (if pressed), どうやら (apparently)
- **Business slang** (3): コスト (cost), リスケ (reschedule), アポ (appointment)
- **Weather** (1): {俄雨|にわかあめ} (sudden rain shower)

Notable entry features:
- Antonym pairs: {鈍感|どんかん}↔{敏感|びんかん}, やり{甲斐|がい}↔{生|い}き{甲斐|がい}
- Japanese cultural concept {生|い}き{甲斐|がい} (ikigai) with international popularity context
- Cooking vocabulary for temperature control and technique
- Business abbreviation slang (リスケ, アポ) with formal equivalents noted
- Adverbs for hedging and inference (どうやら, {強|し}いて{言|い}えば)

Total entries: 6,691 → 6,721
Remaining candidates: 918 → 891

### 2026-01-18 (Vocabulary Expansion - 20 New Entries, Session 103)
Added 20 new dictionary entries from candidate_words.json, focusing on interpersonal vocabulary and Japanese cultural concepts:

- **Cultural concepts** (2): {本音|ほんね} (true feelings), {建前|たてまえ} (public stance)
- **Emotions/Psychology** (5): {人見知|ひとみし}り (shy with strangers), {愚痴|ぐち} (complaint), {見栄|みえ} (vanity), {物足|ものた}りない (unsatisfying), {歯|は}がゆい (frustrating)
- **Verbs** (2): {甘|あま}える (to depend on), {甘|あま}やかす (to spoil)
- **Preparation/Signs** (4): {段取|だんど}り (preparation), {名残|なごり} (traces), {面影|おもかげ} (vestiges), {前触|まえぶ}れ (omen), {兆|きざ}し (sign)
- **Sensory/Comfort** (5): {居心地|いごこち} (comfort of place), {手応|てごた}え (response), {食感|しょっかん} (food texture), {肌触|はだざわ}り (skin feel)
- **Communication** (2): {陰口|かげぐち} (gossip), {雑談|ざつだん} (chitchat)

Notable entry features:
- {本音|ほんね}/{建前|たてまえ} pair with detailed cultural explanations of Japanese communication style
- {甘|あま}える/{甘|あま}やかす transitivity pair covering Japanese concept of {甘|あま}え (emotional dependence)
- Productive patterns: ～{心地|ごこち} (comfort of X), ～{応|ごた}え (worth doing X)
- Sensory vocabulary ({食感|しょっかん}, {肌触|はだざわ}り) with texture onomatopoeia examples
- Cross-references linking related vocabulary pairs

Total entries: 6,671 → 6,691
Remaining candidates: 937 → 918

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
   - Example: `entries/00000/00001_taberu.json`
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
python3 build/validate.py --id 00001_taberu

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
- Example: `entries/00000/00001_taberu.json`
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
