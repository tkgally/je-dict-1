# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-19
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
- **Total entries**: 7,269
- **Vocabulary tier assignment**: Basic: 1,118 | Core: 5,061 | General: 571 | Unassigned: 489
- **Candidate words**: ~547 words tracked in `candidate_words.json`
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

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 128)
Added 30 new dictionary entries from candidate_words.json, covering practical everyday vocabulary, cultural/hobby terms, transportation, and business expressions:

- **Keigo/honorific** (1): お{越|こ}し (coming - honorific)
- **Social/group** (1): {仲間入|なかまい}り (joining a group)
- **Reading/communication** (1): {行間|ぎょうかん} (line spacing; between the lines)
- **Hobbies/entertainment** (7): パチンコ (pachinko), {同人誌|どうじんし} (doujinshi), コレクション (collection), プラモデル (plastic model), ゲーセン (game center), {天体観測|てんたいかんそく} (astronomical observation), {利|き}き{酒|ざけ} (sake tasting)
- **Outdoor/sports** (2): {釣|つ}り{竿|ざお} (fishing rod), {登山靴|とざんぐつ} (hiking boots)
- **Car parts** (2): バックミラー (rearview mirror), ワイパー (windshield wiper)
- **Household** (2): {排水溝|はいすいこう} (drain), {靴棚|くつだな} (shoe rack)
- **Adverbs** (3): ともあれ (anyway), ひょっと (possibly), {明|あき}らかに (clearly)
- **Occupations** (1): {運転士|うんてんし} (train driver)
- **Medical** (1): {切|き}り{傷|きず} (cut wound)
- **Technology** (2): リンク (link/URL), スキャン (scan)
- **Business/shipping** (4): {払戻|はらいもど}し (refund), {返送|へんそう} (return shipping), {送付|そうふ} (sending), {取消|とりけし} (cancellation)
- **Crafts/games** (3): {型紙|かたがみ} (pattern/template), {双六|すごろく} (sugoroku), ラジコン (radio-controlled)

Notable entry features:
- Japanese cultural vocabulary: パチンコ with gambling context, {同人誌|どうじんし} with otaku culture notes, {双六|すごろく} as traditional New Year game
- Hobby vocabulary group: コレクション, プラモデル, ゲーセン, {天体観測|てんたいかんそく}, ラジコン
- Business correspondence: {送付|そうふ}/{返送|へんそう} contrast pair, {払戻|はらいもど}し, {取消|とりけし}
- Practical everyday vocabulary: car parts, household items, medical terms
- Adverbs with common patterns: ともあれ, ひょっと (with ひょっとしたら/ひょっとして)

Total entries: 7,239 → 7,269
Remaining candidates: ~577 → ~547

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 127)
Added 30 new dictionary entries from candidate_words.json, focusing on personality traits, social relationships, consideration/care vocabulary, and useful adjectives:

- **Friendliness/charm** (3): {愛想|あいそう} (amiability), {愛嬌|あいきょう} (charm), {無愛想|ぶあいそう} (unfriendly)
- **Care/consideration** (4): {気遣|きづか}い (concern), {心遣|こころづか}い (thoughtfulness), {心配|こころくば}り (attentive care), {目配|めくば}り (watchfulness)
- **Skill vocabulary** (3): {腕前|うでまえ} (skill), {凄腕|すごうで} (expert), {敏腕|びんわん} (capable)
- **Age/status** (2): {年上|としうえ} (older), {年下|としした} (younger)
- **Familiarity** (3): {馴染|なじ}み (familiarity), {顔馴染|かおなじ}み (familiar face), {初対面|しょたいめん} (first meeting)
- **Attitude/behavior** (4): {強|つよ}がり (bravado), {負|ま}け{惜|お}しみ (sour grapes), お{節介|せっかい} (meddlesome), {気|き}まぐれ (capricious)
- **Abstract nouns** (3): {無駄遣|むだづか}い (waste), {成|な}り{行|ゆ}き (course of events), {先入観|せんにゅうかん} (preconception)
- **I-adjectives** (5): {奥深|おくぶか}い (profound), {生|なま}ぬるい (lukewarm), {潔|いさぎよ}い (graceful in defeat), {程|ほど}よい (moderate), {差|さ}し{出|で}がましい (presumptuous)
- **Na-adjectives** (2): {理不尽|りふじん} (unreasonable), {横柄|おうへい} (arrogant)
- **Expression** (1): やむを{得|え}ない (unavoidable)

Notable entry features:
- Complete care/consideration vocabulary group with cross-references: {気遣|きづか}い, {心遣|こころづか}い, {心配|こころくば}り, {目配|めくば}り
- Skill words: {腕前|うでまえ} → {凄腕|すごうで} → {敏腕|びんわん} with nuance distinctions
- Friendliness/unfriendliness: {愛想|あいそう}/{愛嬌|あいきょう}/{無愛想|ぶあいそう} as antonym pairs
- Useful adjectives for describing personalities and situations
- Expressions for social situations: {初対面|しょたいめん}, お{節介|せっかい}, {差|さ}し{出|で}がましい

Total entries: 7,209 → 7,239
Remaining candidates: ~607 → ~577

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 126)
Added 30 new dictionary entries from candidate_words.json, focusing on compound verbs, comfort/worth expressions, physical sensations, and useful vocabulary:

- **Compound verbs** (6): {繰|く}り{下|さ}げる (to postpone), {沸|わ}き{上|あ}がる (to well up), {突|つ}き{当|あ}たる (to run into), {差|さ}し{伸|の}べる (to extend), {突|つ}き{進|すす}む (to push forward), {切|き}り{下|さ}げる (to cut down)
- **～{心地|ごこち} comfort words** (4): {乗|の}り{心地|ごこち} (ride comfort), {着心地|きごこち} (wearing comfort), {寝心地|ねごこち} (sleeping comfort), {使|つか}い{心地|ごこち} (ease of use)
- **～{応|ごた}え worth expressions** (4): {歯応|はごた}え (chewiness), {読|よ}み{応|ごた}え (worth reading), {見応|みごた}え (worth seeing), {聞|き}き{応|ごた}え (worth listening)
- **Physical sensations** (5): {痺|しび}れ (numbness), むくみ (swelling), かゆみ (itchiness), {凝|こ}り (stiffness), {持病|じびょう} (chronic illness)
- **Everyday vocabulary** (4): {口癖|くちぐせ} (verbal habit), {励|はげ}み (encouragement), {張|は}り{合|あ}い (motivation), {日頃|ひごろ} (usually)
- **Abstract/business** (3): {裁量|さいりょう} (discretion), {目処|めど} (prospect), {大筋|おおすじ} (outline)
- **Yojijukugo** (3): {日常茶飯事|にちじょうさはんじ} (everyday occurrence), {紆余曲折|うよきょくせつ} (twists and turns), {自己満足|じこまんぞく} (self-satisfaction)
- **Noun** (1): {虚栄心|きょえいしん} (vanity)

Notable entry features:
- Complete ～{心地|ごこち} pattern: 4 related words showing how this suffix creates comfort expressions
- Complete ～{応|ごた}え pattern: 4 expressions describing worth/satisfaction across different senses
- Physical sensation vocabulary: common body-related words for describing discomfort
- Compound verbs with {繰|く}り～, {突|つ}き～, {切|き}り～ patterns
- Three yojijukugo with character breakdown and usage notes

Total entries: 7,179 → 7,209
Remaining candidates: ~637 → ~607

### 2026-01-19 (Vocabulary Expansion - 30 New Entries, Session 125)
Added 30 new dictionary entries from candidate_words.json, covering adverbs, adjectives, compound verbs, and practical vocabulary:

- **Adverbs** (5): {互|たが}いに (mutually), {意外|いがい}と (unexpectedly), {思|おも}いがけず (unexpectedly), {仕方|しかた}なく (reluctantly), {思|おも}い{切|き}って (resolutely)
- **Na-adjectives** (5): {巧|たく}み (skillful), {気|き}さく (friendly), {気楽|きらく} (carefree), {些細|ささい} (trivial), {手軽|てがる} (easy)
- **I-adjectives** (3): {気持|きも}ち{悪|わる}い (creepy), {我慢強|がまんづよ}い (patient), {粘|ねば}り{強|づよ}い (tenacious)
- **Nouns** (10): {打|う}ち{合|あ}わせ (meeting), {調理|ちょうり} (cooking), レシピ (recipe), {落|お}ち{着|つ}き (composure), プレッシャー (pressure), {諦|あきら}め (resignation), {決意|けつい} (determination), {仕組|しく}み (mechanism), {手遅|ておく}れ (too late), {手入|てい}れ (maintenance)
- **Compound verbs** (7): {見渡|みわた}す (to survey), {見届|みとど}ける (to see through), {見極|みきわ}める (to discern), {思|おも}い{知|し}る (to learn from experience), {思|おも}い{直|なお}す (to reconsider), {手間取|てまど}る (to take time), {使|つか}いこなす (to master)

Notable entry features:
- Strong adverb coverage: manner expressions ({互|たが}いに, {仕方|しかた}なく) and unexpectedness ({意外|いがい}と, {思|おも}いがけず)
- Personality/character adjectives: {気|き}さく, {気楽|きらく}, {我慢強|がまんづよ}い, {粘|ねば}り{強|づよ}い with nuance distinctions
- {見|み}る compound verbs: {見渡|みわた}す, {見届|みとど}ける, {見極|みきわ}める showing visual perception patterns
- {思|おも}う compound verbs: {思|おも}い{切|き}って, {思|おも}い{知|し}る, {思|おも}い{直|なお}す showing mental processes
- {手|て} compounds: {手遅|ておく}れ, {手入|てい}れ, {手軽|てがる}, {手間取|てまど}る with practical meanings
- Business/work vocabulary: {打|う}ち{合|あ}わせ, プレッシャー, {調理|ちょうり}, レシピ

Total entries: 7,149 → 7,179
Remaining candidates: ~667 → ~637

### 2026-01-19 (New Candidates - 100 Words Added, Session 124)
Added 100 new candidate words to `candidate_words.json` with balanced coverage across multiple categories:

**Adverbs & Manner Expressions** (~20 words):
- Togetherness/separation: {互|たが}いに (mutually), {一緒|いっしょ}に (together), {別々|べつべつ}に (separately)
- Unexpectedness: {意外|いがい}と (unexpectedly), {思|おも}いがけず (by chance), {思|おも}いのほか (more than expected)
- Time/occasion: {当面|とうめん} (for now), {事前|じぜん} (beforehand), {事後|じご} (after the fact)
- Manner: {仕方|しかた}なく (reluctantly), {嫌々|いやいや} (unwillingly), ちょくちょく (often), {思|おも}い{切|き}って (resolutely)

**Personality & Emotional States** (~15 words):
- Personality traits: {心配性|しんぱいしょう} (worrywart), {神経質|しんけいしつ} (nervous), {繊細|せんさい} (delicate), {臆病|おくびょう} (timid), {大胆|だいたん} (bold)
- Resilience: {我慢強|がまんづよ}い (patient), {粘|ねば}り{強|づよ}い (tenacious), {諦|あきら}め (resignation), {悟|さと}り (enlightenment), {決意|けつい} (determination)
- Mental states: {落|お}ち{着|つ}き (composure), プレッシャー (pressure), {気楽|きらく} (carefree), {気|き}さく (friendly)

**Compound Verbs - 見る/思う/使う patterns** (~20 words):
- {見|み}る compounds: {見渡|みわた}す (survey), {見届|みとど}ける (see through), {見極|みきわ}める (discern)
- {思|おも}う compounds: {思|おも}い{知|し}る (learn from experience), {思|おも}い{直|なお}す (reconsider), {思|おも}い{浮|う}かぶ (come to mind)
- {使|つか}う compounds: {使|つか}い{方|かた} (how to use), {使|つか}い{道|みち} (purpose), {使|つか}い{捨|す}て (disposable), {使|つか}い{分|わ}ける (use differently), {使|つか}いこなす (master), {使|つか}い{果|は}たす (use up)

**手 Compounds** (~8 words):
- {手間取|てまど}る (take time), {手軽|てがる} (easy), {手配|てはい} (arrangement), {手遅|ておく}れ (too late), {手元|てもと} (at hand), {手加減|てかげん} (holding back), {手入|てい}れ (maintenance)

**Commerce & Pricing** (~8 words):
- {値上|ねあ}げ (price increase), {値下|ねさ}げ (price reduction), {安売|やすう}り (bargain sale), セール (sale), {相場|そうば} (market price)
- {満員|まんいん} (full), {満席|まんせき} (fully booked), {空席|くうせき} (vacancy), {余地|よち} (room/margin)

**Color & Position Intensifiers** (~8 words):
- {真|ま}っ{白|しろ} (pure white), {真|ま}っ{黒|くろ} (pitch black), {真|ま}っ{青|さお} (deep blue), {真|ま}っ{暗|くら} (pitch dark), {真|ま}っ{先|さき} (first of all), {真上|まうえ} (directly above), {真下|ました} (directly below)

**Time Off & Rest** (~6 words):
- {連休|れんきゅう} (consecutive holidays), {祝日|しゅくじつ} (national holiday), {小休止|しょうきゅうし} (short break), {一息|ひといき} (breather), ひと{休|やす}み (short rest)

**がる Verbs & Physical Actions** (~8 words):
- Emotional expression: {欲|ほ}しがる (want), {怖|こわ}がる (fear), {恥|は}ずかしがる (be shy), {寂|さび}しがる (feel lonely)
- Spatial verbs: {狭|せば}まる (narrow), {狭|せば}める (contract)

**Miscellaneous** (~7 words):
- {打|う}ち{合|あ}わせ (meeting), {調理|ちょうり} (cooking), {具|ぐ} (ingredients), レシピ (recipe), ハード (hardware)
- {山脈|さんみゃく} (mountain range), {落第|らくだい} (failing grade)
- {散策|さんさく} (stroll), {行楽|こうらく} (outing), {整頓|せいとん} (tidying), {消毒|しょうどく} (disinfection), {除菌|じょきん} (sanitizing)

Notable features:
- Strong coverage of compound verb patterns (~使う, ~見る, ~思う)
- Comprehensive 手 compound vocabulary for everyday expressions
- Personality and emotional vocabulary for describing people
- Practical commerce and pricing vocabulary
- Color/position intensifiers with 真っ～ pattern
- Balance of native Japanese and loanwords

Candidate count: 567 → 667

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 123)
Added 30 new dictionary entries from candidate_words.json, covering yojijukugo, mimetics, cultural/religious items, modern vocabulary, and everyday terms:

- **Yojijukugo** (4): {満身創痍|まんしんそうい} (covered in wounds), {付和雷同|ふわらいどう} (following blindly), {栄枯盛衰|えいこせいすい} (rise and fall), {明鏡止水|めいきょうしすい} (serene mind)
- **Mimetics/Adverbs** (4): ちょこちょこ (in small steps), きりきり (sharp pain), ひょこひょこ (bobbing), ひょいと (quickly)
- **Traditional New Year games** (3): {凧揚|たこあ}げ (kite flying), {羽根|はね}つき (Japanese badminton), {福笑|ふくわら}い (pin-the-face game)
- **Religious/Cultural items** (3): {数珠|じゅず} (prayer beads), {位牌|いはい} (memorial tablet), {熨斗|のし} (gift ornament)
- **Adjectives** (2): てれくさい (embarrassing), {気恥|きは}ずかしい (bashful)
- **Modern/Safety vocabulary** (4): {節電|せつでん} (power saving), {防犯|ぼうはん}カメラ (security camera), {避難経路|ひなんけいろ} (evacuation route), {観客席|かんきゃくせき} (spectator seating)
- **Facilities/Fees** (3): {多目的|たもくてき}トイレ (accessible toilet), {入館料|にゅうかんりょう} (admission fee), {宿泊料|しゅくはくりょう} (accommodation fee)
- **Work/Life** (1): {育児休暇|いくじきゅうか} (parental leave)
- **Tools/Architecture** (4): やすり (file), {雨樋|あまどい} (rain gutter), {土台|どだい} (foundation), {糸鋸|いとのこ} (coping saw)
- **Nature/Taste** (2): {引|ひ}き{潮|しお} (ebb tide), {渋|しぶ}み (astringency)

Notable entry features:
- Four yojijukugo with character breakdowns and etymology
- Traditional New Year games group with cross-references and cultural context
- Buddhist/religious vocabulary: {数珠|じゅず}, {位牌|いはい} linked with {仏壇|ぶつだん}
- Modern safety terminology common in public facilities
- Japanese aesthetic concept: {渋|しぶ}み (astringency and refined elegance)
- Mimetics describing manner of movement and sensation

Total entries: 7,119 → 7,149
Remaining candidates: ~597 → ~567

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 122)
Added 30 new dictionary entries from candidate_words.json, covering occupations, household items, medical terms, academic subjects, business vocabulary, and cultural terms:

- **Occupations** (4): {配管工|はいかんこう} (plumber), {電気技師|でんきぎし} (electrician), {彫刻家|ちょうこくか} (sculptor), {映画監督|えいがかんとく} (film director)
- **Household items** (5): {物干|ものほ}し (drying rack), {洗濯籠|せんたくかご} (laundry basket), {吹|ふ}き{抜|ぬ}け (atrium), {食器棚|しょっきだな} (dish cabinet), マットレス (mattress)
- **Sewing/Clothing** (3): ファスナー (zipper), {裏地|うらじ} (lining), {縫|ぬ}い{目|め} (seam)
- **Medical terms** (3): {低血圧|ていけつあつ} (low blood pressure), {不整脈|ふせいみゃく} (arrhythmia), {遠視|えんし} (farsightedness)
- **Academic subjects** (3): {地学|ちがく} (earth science), {生物学|せいぶつがく} (biology), {天文学|てんもんがく} (astronomy)
- **Music** (1): {音程|おんてい} (pitch/interval)
- **Business/Work** (3): {出向|しゅっこう} (secondment), ワークライフバランス (work-life balance), ダイバーシティ (diversity)
- **Sports** (2): {打率|だりつ} (batting average), {飛|と}び{込|こ}み (diving)
- **Cultural/Religious** (2): {狛犬|こまいぬ} (guardian lion-dog), {仏壇|ぶつだん} (Buddhist altar)
- **Yojijukugo** (2): {粉骨砕身|ふんこつさいしん} (working oneself to the bone), {前途多難|ぜんとたなん} (many difficulties ahead)
- **Games** (1): {駒|こま} (game piece)
- **Compound verb** (1): {撫|な}で{下|お}ろす (to smooth down/feel relieved)

Notable entry features:
- Trade/professional occupations with qualification contexts
- Household vocabulary for daily life: laundry, furniture, architecture
- Medical terms with antonym pairs: {低血圧|ていけつあつ} ↔ {高血圧|こうけつあつ}, {遠視|えんし} ↔ {近視|きんし}
- Academic subjects as a group with cross-references
- Modern business loanwords: ワークライフバランス, ダイバーシティ
- Japanese cultural items: {狛犬|こまいぬ} with 阿吽 symbolism, {仏壇|ぶつだん} with component vocabulary
- Two yojijukugo with character breakdowns and similar expressions

Total entries: 7,089 → 7,119
Remaining candidates: ~627 → ~597

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 121)
Added 30 new dictionary entries from candidate_words.json, covering practical everyday vocabulary across multiple categories:

- **Establishments/Facilities** (3): バー (bar), {控|ひか}え{室|しつ} (waiting room), {授乳室|じゅにゅうしつ} (nursing room)
- **Architecture/Windows** (2): {天窓|てんまど} (skylight), {出窓|でまど} (bay window)
- **Tools/Equipment** (4): {蛍光|けいこう}ペン (highlighter), {軍手|ぐんて} (work gloves), {紙|かみ}やすり (sandpaper), ゴーグル (goggles)
- **Household products** (3): {延長|えんちょう}コード (extension cord), {消臭剤|しょうしゅうざい} (deodorizer), {接着剤|せっちゃくざい} (adhesive)
- **Crafts/Hobbies** (6): {手芸|しゅげい} (handicraft), {木彫|きぼ}り (wood carving), {日曜大工|にちようだいく} (DIY), {模型|もけい} (model), コスプレ (cosplay), フィギュア (figure)
- **Art** (2): {油絵|あぶらえ} (oil painting), {水彩画|すいさいが} (watercolor painting)
- **Music genres** (3): {演歌|えんか} (enka), {民謡|みんよう} (folk song), ジャズ (jazz)
- **Finance** (2): {元本|がんぽん} (principal), {額面|がくめん} (face value)
- **Elections/Lotteries** (2): {当選|とうせん} (winning), {落選|らくせん} (losing)
- **Medical** (1): {脱臼|だっきゅう} (dislocation)
- **Gardening** (1): {家庭菜園|かていさいえん} (home vegetable garden)
- **Other** (1): トラブル (trouble)

Notable entry features:
- Hobby/culture vocabulary: コスプレ, フィギュア, {日曜大工|にちようだいく} with etymology and cultural context
- Art vocabulary contrast pairs: {油絵|あぶらえ} ↔ {水彩画|すいさいが}
- Music genres with cultural notes: {演歌|えんか} (famous singers), {民謡|みんよう} (regional songs)
- Election vocabulary antonym pair: {当選|とうせん} ↔ {落選|らくせん}
- Financial terms with context: {元本|がんぽん}, {額面|がくめん} (including figurative usage)

Total entries: 7,059 → 7,089
Remaining candidates: ~657 → ~627

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 120)
Added 30 new dictionary entries from candidate_words.json, covering occupations, household products, facilities, travel/accommodation terms, and four-character idioms:

- **Occupations** (4): {薬剤師|やくざいし} (pharmacist), {獣医|じゅうい} (veterinarian), {司書|ししょ} (librarian), {探偵|たんてい} (detective)
- **Household products** (4): {柔軟剤|じゅうなんざい} (fabric softener), {漂白剤|ひょうはくざい} (bleach), {殺虫剤|さっちゅうざい} (insecticide), {芳香剤|ほうこうざい} (air freshener)
- **Household items** (4): おろし{金|がね} (grater), {巻尺|まきじゃく} (tape measure), {湯|ゆ}たんぽ (hot water bottle), {洗濯|せんたく}ばさみ (clothespin)
- **Facilities/Places** (4): {更衣室|こういしつ} (changing room), {喫煙所|きつえんじょ} (smoking area), {休憩所|きゅうけいじょ} (rest area), {非常口|ひじょうぐち} (emergency exit)
- **Travel/Accommodation** (5): {指定席|していせき} (reserved seat), {自由席|じゆうせき} (unreserved seat), {素泊|すど}まり (room only), {連泊|れんぱく} (consecutive nights), {送迎|そうげい} (shuttle service)
- **Yojijukugo (4-character idioms)** (3): {支離滅裂|しりめつれつ} (incoherent), {公明正大|こうめいせいだい} (fair and square), {一喜一憂|いっきいちゆう} (emotional ups and downs)
- **Booking/Fee systems** (5): {抽選|ちゅうせん} (lottery), {先着順|せんちゃくじゅん} (first-come-first-served), {予約制|よやくせい} (by reservation), {入場料|にゅうじょうりょう} (admission fee), {拝観料|はいかんりょう} (temple viewing fee)
- **Other** (1): カビ (mold)

Notable entry features:
- Occupation vocabulary with workplace contexts and related professions
- Household chemical products (～{剤|ざい} suffix pattern): cleaning, laundry, pest control
- Travel and accommodation terminology with contrast pairs: {指定席|していせき} ↔ {自由席|じゆうせき}, {抽選|ちゅうせん} ↔ {先着順|せんちゃくじゅん}
- Public facility vocabulary with usage contexts
- Three yojijukugo with formation analysis and grammar patterns

Total entries: 7,029 → 7,059
Remaining candidates: ~687 → ~657

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 119)
Added 30 new dictionary entries from candidate_words.json, covering compound verbs, household items, taste vocabulary, medical terms, and social expressions:

- **Compound verbs** (10): {突|つ}っ{込|こ}む (to thrust/retort), {引|ひ}っ{掻|か}く (to scratch), {言|い}い{渡|わた}す (to hand down), {行|い}き{渡|わた}る (to spread throughout), {呼|よ}び{戻|もど}す (to call back), {巻|ま}き{起|お}こる (to arise), {巻|ま}き{返|かえ}す (to make a comeback), {繰|く}り{上|あ}げる (to move up schedule), {折|お}り{曲|ま}げる (to fold), {跳|は}ね{返|かえ}る (to bounce back)
- **Household items** (6): {栓|せん}{抜|ぬ}き (bottle opener), {缶切|かんき}り (can opener), {電源|でんげん}タップ (power strip), {傘立|かさた}て (umbrella stand), {掛|か}け{布団|ぶとん} (comforter), {敷|し}き{布団|ぶとん} (mattress futon)
- **Taste vocabulary** (3): {酸味|さんみ} (sourness), {甘味|あまみ} (sweetness), {塩気|しおけ} (saltiness)
- **Medical terms** (2): {貧血|ひんけつ} (anemia), {食中毒|しょくちゅうどく} (food poisoning)
- **Social/communication** (5): {世間話|せけんばなし} (small talk), {独|ひと}り{言|ごと} (talking to oneself), お{世辞|せじ} (flattery), {嫌味|いやみ} (sarcasm), {負|ま}けず{嫌|ぎら}い (competitive)
- **Abstract concepts** (2): {心構|こころがま}え (mental preparedness), {不可欠|ふかけつ} (indispensable)
- **Adverbs** (2): {次々|つぎつぎ}と (one after another), {仮|かり}に (supposing)

Notable entry features:
- Strong compound verb coverage: ～{込|こ}む (into), ～{渡|わた}す (convey), ～{渡|わた}る (spread), ～{戻|もど}す (return), ～{起|お}こる (arise), ～{返|かえ}す (reverse), ～{上|あ}げる (advance), ～{返|かえ}る (rebound)
- Practical household vocabulary: kitchen tools, bedding, and home items
- Five basic taste words group: {酸味|さんみ}, {甘味|あまみ}, {塩気|しおけ} linked with cross-references
- Social communication: small talk, flattery, sarcasm with nuance explanations
- Comedy culture: {突|つ}っ{込|こ}む with manzai (tsukkomi/boke) context

Total entries: 6,999 → 7,029
Remaining candidates: ~716 → ~687

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
