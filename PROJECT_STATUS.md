# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-16
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
- **Total entries**: 6,108
- **Vocabulary tier assignment**: Pending (all entries have vocabulary_tier: null)
- **Candidate words**: ~869 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 600-800 fundamental words for basic communication
- **Core**: 1,600-2,000 words for adult-level communication
- **General**: All other vocabulary useful for learners

Tier assignment is pending. Once complete, entries will be categorized for progressive learning.

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

### 2026-01-16 (Vocabulary Expansion - 50 New Entries, Session 70)
Added 50 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (10): ざわざわ (rustling/uneasy), がさがさ (rustling/rough), どさどさ (with thuds), ぽっかり (gaping/floating), みっしり (tightly packed), ちろちろ (flickering), ぺちゃぺちゃ (chattering), ぱたぱた (flapping), ざぶざぶ (splashing), ぴよぴよ (chirping)
- Emotional/psychological terms (10): {孤独感|こどくかん} (loneliness), {優越感|ゆうえつかん} (superiority), {虚無感|きょむかん} (emptiness), {嫌悪|けんお} (disgust), {渇望|かつぼう} (craving), {郷愁|きょうしゅう} (nostalgia), {陶酔|とうすい} (intoxication), {恍惚|こうこつ} (ecstasy), {虚脱|きょだつ} (lethargy), {倦怠|けんたい} (weariness)
- Body/medical terms (10): {肩甲骨|けんこうこつ} (shoulder blade), {脊椎|せきつい} (spine), {靭帯|じんたい} (ligament), {毛細血管|もうさいけっかん} (capillary), リンパ (lymph), {骨髄|こつずい} (bone marrow), {呼吸器|こきゅうき} (respiratory system), {消化器|しょうかき} (digestive system), {循環器|じゅんかんき} (circulatory system), {喉仏|のどぼとけ} (Adam's apple)
- Cultural/memorial terms (5): {注連縄|しめなわ} (sacred rope), {初七日|しょなのか} (7th day memorial), {四十九日|しじゅうくにち} (49th day memorial), {一周忌|いっしゅうき} (first anniversary), {三回忌|さんかいき} (second anniversary)
- Four-character idioms (5): {二束三文|にそくさんもん} (dirt cheap), {三日坊主|みっかぼうず} (quitter), {本末転倒|ほんまつてんとう} (cart before horse), {一朝一夕|いっちょういっせき} (overnight), {青息吐息|あおいきといき} (gasping with distress)
- Concepts/abstract (6): {偏見|へんけん} (prejudice), {論理|ろんり} (logic), {理念|りねん} (principle), {民主|みんしゅ} (democracy), {進化|しんか} (evolution), {退化|たいか} (degeneration)
- Modern/other (4): ストリーミング (streaming), {拝借|はいしゃく}する (to borrow humble), {粛々|しゅくしゅく} (solemnly), ぶーぶー (honking/complaining)

Notable entry features:
- Comprehensive onomatopoeia covering sounds, textures, and psychological states
- Psychological vocabulary for nuanced emotional expression (感 compounds)
- Body systems vocabulary useful for medical/health contexts
- Buddhist memorial service terminology with cultural explanations
- Four-character idioms with etymological notes
- Cross-references linking antonyms ({進化|しんか}↔{退化|たいか}, {優越感|ゆうえつかん}↔{劣等感|れっとうかん})
- Organ system terms cross-referenced to each other

Total entries: 6,058 → 6,108
Remaining candidates: 918 → 869

### 2026-01-16 (Vocabulary Expansion - 50 New Entries, Session 69)
Added 50 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (10): にたにた (smirking), がつがつ (greedily), ぽりぽり (crunching), むしむし (muggy), じとじと (damp/sticky), どたばた (clumsily), ごそごそ (rustling), のそのそ (lumbering), しゃきしゃき (crisp), ころころ (rolling)
- Four-character idioms (5): {起承転結|きしょうてんけつ} (narrative structure), {弱肉強食|じゃくにくきょうしょく} (survival of the fittest), {喜怒哀楽|きどあいらく} (human emotions), {因果応報|いんがおうほう} (karma), {前代未聞|ぜんだいみもん} (unprecedented)
- Emotional/psychological terms (5): {執着|しゅうちゃく} (attachment), {罪悪感|ざいあくかん} (guilt), {達成感|たっせいかん} (sense of achievement), {充実感|じゅうじつかん} (sense of fulfillment), {劣等感|れっとうかん} (inferiority complex)
- Cultural/religious (5): お{守|まも}り (amulet), {鳥居|とりい} (torii gate), {絵馬|えま} (votive tablet), {賽銭|さいせん} (offering money), おみくじ (fortune slip)
- Body/medical terms (5): {膵臓|すいぞう} (pancreas), {脾臓|ひぞう} (spleen), {肋骨|ろっこつ} (rib), {骨盤|こつばん} (pelvis), {軟骨|なんこつ} (cartilage)
- Legal terms (5): {棄却|ききゃく} (dismissal), {控訴|こうそ} (appeal to high court), {上訴|じょうそ} (appeal), {革命|かくめい} (revolution), {独裁|どくさい} (dictatorship)
- Business/finance terms (5): {配当|はいとう} (dividend), {財務|ざいむ} (finances), {監査|かんさ} (audit), {決算|けっさん} (settlement), {担保|たんぽ} (collateral)
- Medical procedure terms (5): {通院|つういん} (outpatient visit), {処方|しょほう} (prescription), {感染|かんせん} (infection), {炎症|えんしょう} (inflammation), {健康診断|けんこうしんだん} (health checkup)
- Travel/aviation terms (3): {滑走路|かっそうろ} (runway), {離陸|りりく} (takeoff), {着陸|ちゃくりく} (landing)
- Modern/slang terms (2): マウント (one-upmanship), もやもや (feeling uneasy)

Notable entry features:
- Comprehensive onomatopoeia covering textures, sounds, movements, and atmospheric conditions
- Four-character idioms with detailed cultural/historical explanations
- Psychological vocabulary for expressing complex emotional states
- Shinto/temple cultural vocabulary essential for understanding Japanese religious practices
- Medical and anatomical terms for healthcare contexts
- Legal system vocabulary with explanations of Japanese court hierarchy
- Cross-references added linking related terms (離陸↔着陸, 控訴↔上訴)

Total entries: 6,008 → 6,058
Remaining candidates: 968 → 918

### 2026-01-16 (Vocabulary Expansion - 50 New Entries, Session 68)
Added 50 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (11): しとしと (drizzling), ざあざあ (pouring), さくさく (crispy), つやつや (glossy), ぱちぱち (crackling), こっそり (secretly), ぎっしり (packed), びっしり (densely), がっくり (dejected), るんるん (cheerfully), がりがり (crunching)
- ABAB adverbs (5): {堂々|どうどう} (dignified), {延々|えんえん} (endlessly), {淡々|たんたん} (calmly), {刻々|こっこく} (moment by moment), {代々|だいだい} (for generations)
- Modern/social media (6): リプライ (reply), ブロック (block), ミュート (mute), パワハラ (power harassment), セクハラ (sexual harassment)
- Legal/business terms (5): {判決|はんけつ} (verdict), {仲裁|ちゅうさい} (arbitration), {却下|きゃっか} (rejection), {認証|にんしょう} (authentication), {緊迫|きんぱく} (tension)
- Keigo verbs (5): {届|とど}け{出|で}る (to report), お{越|こ}しになる (to come, honorific), {存|ぞん}じる (to know, humble), {頂戴|ちょうだい}する (to receive, humble), {恐|おそ}れ{入|い}る (to be obliged)
- Adjectives (3): {甘酸|あまず}っぱい (bittersweet), {四角|しかく}い (square-shaped), {差|さ}し{支|つか}える (to hinder)
- Opposite/compound words (4): {功罪|こうざい} (merits and demerits), {需給|じゅきゅう} (supply and demand), {起伏|きふく} (ups and downs), {反面|はんめん} (on the other hand)
- Cultural/ceremonial (4): {初節句|はつぜっく} (baby's first festival), {告別式|こくべつしき} (funeral service), {法要|ほうよう} (memorial service), お{宮参|みやまい}り (shrine visit for newborn)
- Sports/music (4): シュート (shot), ドリブル (dribble), アンコール (encore), アドリブ (ad-lib)
- Nature/other (3): {五月雨|さみだれ} (early summer rain), {三昧|ざんまい} (absorption in), {万全|ばんぜん} (perfect), {稲刈|いねか}り (rice harvesting)

Notable entry features:
- Comprehensive onomatopoeia covering sounds, textures, and emotional states
- ABAB-pattern adverbs with kanji reduplication ({堂々|どうどう}, {延々|えんえん}, etc.)
- Modern harassment terminology (パワハラ, セクハラ) with workplace context
- Formal keigo verbs including humble ({謙譲語|けんじょうご}) and honorific ({尊敬語|そんけいご}) forms
- Japanese ceremonial vocabulary covering lifecycle events (birth, death, memorials)
- Cross-references added linking related terms (シュート↔ドリブル, パワハラ↔セクハラ)

Total entries: 5,958 → 6,008
Remaining candidates: 1,019 → 968

### 2026-01-16 (New Candidates - 100 Words Added, Session 67)
Added 100 new candidate words to `candidate_words.json` using balanced coverage strategy:

- **Modern loanwords** (32): Business terms (フィードバック, アジェンダ, キャンセル, リスケ, アポ, コスト, マネジメント, プロジェクト, タスク, デッドライン), places (カフェ, バー), food (パスタ, ピザ, アイス), sports (バスケ, バレー, スノボ), technology (オフライン, ストレージ, ペースト, スキャン, リンク, シェア, コメント, ハッシュタグ, タイムライン, プロフィール, DM), appliances (エアコン, ストーブ, 電子レンジ), travel (プラットホーム)
- **Compound words** (25): Verbs (持ち出す, 取り外す, 取り扱う, 取り締まる, 書き留める), housing (敷金, 物件), education (就学), work (報告書, 成果, 開発, 運用), weather (俄雨), formal expressions (告白, 宣告, 遺憾, 謝罪, 概要), abstract concepts (幻想, 妄想, 錯覚), travel (切符売り場), family (義母, 義父, 連れ合い)
- **～的 adjectives** (7): 実質的, 比較的, 定期的, 段階的, 保守的, 特徴的, plus four-character idioms (一直線, 一生懸命, 多事多難)
- **Emotional adjectives** (5): 切ない, 煩わしい, 鬱陶しい, 愛しい, 面倒くさい
- **Math/number terms** (2): 分数, 比率
- **Clothing** (2): 靴下, 手袋
- **Medical** (1): 湿疹
- **Conjunctions/connectors** (9): それなのに, 及び, 並びに, 若しくは, さもないと, 故に, 差し当たり, に伴い
- **Onomatopoeia/adverbs** (3): ぐんぐん, じゃんじゃん, ばんばん
- **Particles** (3): ぜ, ぞ, かしら
- **Verbs** (7): ばれる, いける, 怒る (いかる), 呆れる, 痺れる, かぶれる
- **Expressions** (3): うんざり, 今しがた, 度 (counter)

Candidate count: 919 → 1,019

### 2026-01-16 (Vocabulary Expansion - 50 New Entries, Session 66)
Added 50 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (10): しょんぼり (dejected), ぐったり (exhausted), ひんやり (cool), しっとり (moist), てくてく (plodding), とぼとぼ (trudging), すたすた (briskly), ゆったり (relaxed), きびきび (briskly), だらだら (sluggishly)
- ～{的|てき} adjectives (10): {継続的|けいぞくてき} (continuous), {一時的|いちじてき} (temporary), {永久的|えいきゅうてき} (permanent), {直感的|ちょっかんてき} (intuitive), {絶対的|ぜったいてき} (absolute), {相対的|そうたいてき} (relative), {精神的|せいしんてき} (mental), {身体的|しんたいてき} (physical), {圧倒的|あっとうてき} (overwhelming), {極端的|きょくたんてき} (extreme)
- Body/medical terms (5): {拳|こぶし} (fist), お{尻|しり} (buttocks), {動脈|どうみゃく} (artery), {静脈|じょうみゃく} (vein), {鎖骨|さこつ} (collarbone)
- Weather terms (5): {豪雨|ごうう} (heavy rain), {小雨|こさめ} (light rain), {夕立|ゆうだち} (afternoon shower), {肌寒|はだざむ}い (chilly), {薄曇|うすぐも}り (overcast)
- Modern/social media (6): いいね (like), フォロワー (follower), {炎上|えんじょう} (online backlash), ぼっち (loner), ホームページ (website), デジタル (digital)
- Compound verbs (5): {取|と}り{込|こ}む (to take in), {引|ひ}き{返|かえ}す (to turn back), {引|ひ}き{下|さ}がる (to withdraw), {押|お}し{入|い}れる (to force into), {泳|およ}ぎ{回|まわ}る (to swim around)
- Nouns (5): {墓場|はかば} (graveyard), メロディー (melody), ボーナス (bonus), {認可|にんか} (authorization), {根|ね}っこ (root)
- Food terms (4): {海鮮|かいせん} (seafood), {乳製品|にゅうせいひん} (dairy products), {炊|た}き{込|こ}みご{飯|はん} (mixed rice), {生鮮|せいせん} (fresh produce)

Notable entry features:
- Comprehensive onomatopoeia covering emotional and physical states
- ～的 adjective pairs including antonyms (絶対的↔相対的, 精神的↔身体的)
- Modern internet vocabulary reflecting contemporary Japanese usage
- Compound verb patterns with ～回る (movement around) and ～込む (action into)
- Cross-references added linking antonyms and related medical terms (動脈↔静脈)

Total entries: 5,907 → 5,958
Remaining candidates: 967 → 919

### 2026-01-16 (Code Quality Improvements - Debug Plan Complete)
Completed all 23 tasks from `main/debug_plan.md` across 8 debugging sessions, addressing recommendations from multi-LLM code reviews:

**Security & Build Stability:**
- Fixed XSS vulnerability in search results (HTML escaping in `search.js` and `build_flat.py`)
- Removed auto-install package pattern from `validate.py` (security risk)
- Fixed null candidate field crash in `build_flat.py`

**Data Integrity:**
- Fixed cross-reference migration losing distinct refs (composite key deduplication)
- Added duplicate ID check to build process
- Improved self-reference validation for entries without headword

**Robustness & Error Handling:**
- Added error handling to `cleanup_candidates.py` and `manage_candidates.py`
- Fixed hardcoded relative paths in `manage_candidates.py`
- Made build process atomic (builds to temp directory, then swaps)

**Performance:**
- Fixed double file read in `add_example_ids.py`
- Fixed O(n²) duplicate detection in search index (now uses sets)
- Reuse validator instance across entries

**Code Quality:**
- Moved inline imports to module top across 4 files
- Centralized furigana pattern `FURIGANA_PATTERN` in `japanese_utils.py`
- Refactored `validate_all_entries()` to return `ValidationResult` dataclass

**Schema & Validation:**
- Updated schema to allow legacy string cross-references (oneOf)
- Expanded reading pattern to include rare kana (ゝ, ゞ, etc.)
- Added 24-hour grace period for timestamp validation

**UX & Architecture:**
- Added furigana toggle script to `pending.html`
- Extended furigana scanning to all text fields (notes, examples, definitions, explanation)
- Centralized cross-reference types in `build/cross_ref_types.py`
- Moved `normalize_reading()` to `japanese_utils.py`

See `main/debug_plan.md` for full task details and progress log.

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 65)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Cultural vocabulary (8): {七夕|たなばた} (Tanabata), {法事|ほうじ} (memorial service), {披露宴|ひろうえん} (wedding reception), {盆踊|ぼんおど}り (Bon dance), お{葬式|そうしき} (funeral), お{見合|みあ}い (matchmaking), {鯉|こい}のぼり (carp streamers), {羽織|はおり} (haori jacket)
- Onomatopoeia (10): もふもふ (fluffy), ぎゅうぎゅう (crammed), ぽたぽた (dripping), ぶんぶん (buzzing), カチカチ (clicking), ばりばり (crunching), ぱくぱく (gobbling), じゃぶじゃぶ (splashing), ぼうぼう (overgrown), てきぱき (efficiently)
- Adverbs (11): あっさり (lightly), がっちり (firmly), ざっくり (roughly), すんなり (smoothly), ばっちり (perfectly), ばっさり (decisively), やたらに (excessively), {無闇|むやみ}に (recklessly), {碌|ろく}に (properly), ありのまま (as is), {却|かえ}って (on the contrary)
- ～的 adjectives (13): {革新的|かくしんてき} (innovative), {批判的|ひはんてき} (critical), {協力的|きょうりょくてき} (cooperative), {標準的|ひょうじゅんてき} (standard), {代表的|だいひょうてき} (representative), {全面的|ぜんめんてき} (overall), {部分的|ぶぶんてき} (partial), {中心的|ちゅうしんてき} (central), {内面的|ないめんてき} (internal), {外面的|がいめんてき} (external), {感覚的|かんかくてき} (sensory), {知性的|ちせいてき} (intellectual), {主体的|しゅたいてき} (autonomous)
- ～やか adjectives (2): {淑|しと}やか (graceful), {煌|きら}びやか (dazzling)
- Compound verbs (7): {受|う}け{付|つ}ける (to accept), {受|う}け{持|も}つ (to be in charge), {受|う}け{流|なが}す (to deflect), {引|ひ}き{上|あ}げる (to pull up), {立|た}て{込|こ}む (to be busy), {乗|の}りこなす (to master riding), {掛|か}け{合|あ}う (to negotiate)
- Four-character idioms (3): {一心不乱|いっしんふらん} (single-minded), {起死回生|きしかいせい} (revival), {七転八起|しちてんはっき} (perseverance)
- Number compounds (2): {五感|ごかん} (five senses), {九九|くく} (multiplication table)
- Abstract ～性 nouns (10): {独創性|どくそうせい} (originality), {柔軟性|じゅうなんせい} (flexibility), {適応性|てきおうせい} (adaptability), {正確性|せいかくせい} (accuracy), {緊急性|きんきゅうせい} (urgency), {整合性|せいごうせい} (consistency), {妥当性|だとうせい} (validity), {合理性|ごうりせい} (rationality), {論理性|ろんりせい} (logic), {探究心|たんきゅうしん} (curiosity)
- Society/politics (3): {都市化|としか} (urbanization), {安全保障|あんぜんほしょう} (security), {自衛隊|じえいたい} (Self-Defense Forces)
- Business/procedures (10): {登録|とうろく} (registration), {解除|かいじょ} (cancellation), {免除|めんじょ} (exemption), {早退|そうたい} (leaving early), {加盟|かめい} (joining), {脱退|だったい} (withdrawal), {提携|ていけい} (partnership), {処置|しょち} (treatment), {統括|とうかつ} (supervision), {勧告|かんこく} (recommendation)
- Other nouns (21): {臓器|ぞうき} (organ), {新旧|しんきゅう} (old and new), {合間|あいま} (interval), {羨望|せんぼう} (envy), {珍味|ちんみ} (delicacy), {盛|も}り{付|つ}け (plating), {財政|ざいせい} (finance), {紛争|ふんそう} (conflict), {作用|さよう} (effect), {偏|かたよ}り (bias), {局面|きょくめん} (phase), {側面|そくめん} (aspect), {風潮|ふうちょう} (trend), {風習|ふうしゅう} (custom), {無意識|むいしき} (unconscious), {不参加|ふさんか} (non-participation), {出発点|しゅっぱつてん} (starting point), {記述|きじゅつ} (description), {評論|ひょうろん} (criticism), {打診|だしん} (sounding out), それなら (if so)

Notable entry features:
- Japanese cultural vocabulary including ceremonies and traditional items
- Comprehensive ～的 adjective coverage for expressing qualities and states
- Abstract ～性 nouns useful for academic and business contexts
- Society and politics vocabulary including Self-Defense Forces with cultural notes
- Business procedure terms covering membership, exemptions, and organizational management

Total entries: 5,807 → 5,907
Remaining candidates: 1,067 → 967

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 64)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Suru verbs (10): {質問|しつもん}する (to ask), {説明|せつめい}する (to explain), {紹介|しょうかい}する (to introduce), {約束|やくそく}する (to promise), {報告|ほうこく}する (to report), {賛成|さんせい}する (to agree), {反対|はんたい}する (to oppose), {邪魔|じゃま}する (to disturb), {電話|でんわ}する (to call), お{願|ねが}いする (to request)
- Four-character idioms (7): {試行錯誤|しこうさくご} (trial and error), {自画自賛|じがじさん} (self-praise), {無我夢中|むがむちゅう} (being absorbed), {臨機応変|りんきおうへん} (flexibility), {五里霧中|ごりむちゅう} (bewilderment), {異口同音|いくどうおん} (unanimous), {油断大敵|ゆだんたいてき} (complacency warning)
- ～的 adjectives (15): {歴史的|れきしてき} (historical), {論理的|ろんりてき} (logical), {経済的|けいざいてき} (economical), {科学的|かがくてき} (scientific), {感情的|かんじょうてき} (emotional), {本格的|ほんかくてき} (full-scale), {技術的|ぎじゅつてき} (technical), {政治的|せいじてき} (political), {心理的|しんりてき} (psychological), {文化的|ぶんかてき} (cultural), {実践的|じっせんてき} (practical), {理論的|りろんてき} (theoretical), {創造的|そうぞうてき} (creative), {客観的|きゃっかんてき} (objective), {主観的|しゅかんてき} (subjective)
- ～やか adjectives (6): {爽|さわ}やか (refreshing), {鮮|あざ}やか (vivid), {和|なご}やか (harmonious), {健|すこ}やか (healthy), のどか (peaceful), {朗|ほが}らか (cheerful)
- Adverbs (12): もしかして (perhaps), いっそ (rather), {何|なに}しろ (after all), いかにも (indeed), かろうじて (barely), ひたすら (earnestly), もっぱら (exclusively), ひそかに (secretly), まれに (rarely), ひとまず (for now), おおむね (generally), あらかじめ (beforehand)
- Compound verbs (15): {引|ひ}き{込|こ}む (to draw in), {持|も}ち{歩|ある}く (to carry around), {生|い}き{返|かえ}る (to revive), {締|し}め{切|き}る (to close off), {切|き}り{開|ひら}く (to pioneer), {切|き}り{捨|す}てる (to cut off), {流|なが}れ{込|こ}む (to flow in), {落|お}ち{込|こ}む (to fall into), {巻|ま}き{込|こ}む (to involve), {受|う}け{入|い}れる (to accept), {受|う}け{止|と}める (to catch), {立|た}て{替|か}える (to pay for), {乗|の}り{出|だ}す (to set out), {切|き}り{離|はな}す (to separate), {押|お}し{出|だ}す (to push out)
- Onomatopoeia (10): にやにや (grinning), げらげら (guffawing), くすくす (giggling), めそめそ (sobbing), もぐもぐ (munching), ごくごく (gulping), ちびちび (sipping), ずるずる (slurping), すやすや (sleeping soundly), ぽかぽか (warmly)
- Cultural vocabulary (8): {床|とこ}の{間|ま} (alcove), {風呂敷|ふろしき} (wrapping cloth), {提灯|ちょうちん} (paper lantern), {暖簾|のれん} (shop curtain), {初詣|はつもうで} (first shrine visit), {還暦|かんれき} (60th birthday), {厄年|やくどし} (unlucky year), {大晦日|おおみそか} (New Year's Eve)
- Emotional nouns (5): {焦|あせ}り (impatience), {苛立|いらだ}ち (irritation), {戸惑|とまど}い (confusion), {安堵|あんど} (relief), {憂鬱|ゆううつ} (depression)
- Cooking vocabulary (5): {煮込|にこ}む (to simmer), {和|あ}える (to dress food), {惣菜|そうざい} (prepared food), {下|した}ごしらえ (food prep), {味付|あじつ}け (seasoning)
- Modern abbreviations (2): {就活|しゅうかつ} (job hunting), {婚活|こんかつ} (marriage hunting)
- Additional onomatopoeia (5): ぬくぬく (snugly warm), じめじめ (damp), からっと (dry/crispy), こそこそ (sneakily), さっさと (quickly)

Notable entry features:
- Common suru verbs essential for basic communication
- Four-character idioms with explanations of origins and usage
- Comprehensive ～的 adjective coverage for academic contexts
- Traditional Japanese cultural vocabulary with detailed notes
- Emotional noun entries useful for nuanced expression
- Cooking terms covering food preparation methods
- Cross-references added linking antonym pairs ({賛成|さんせい}↔{反対|はんたい}, {客観的|きゃっかんてき}↔{主観的|しゅかんてき})

Total entries: 5,707 → 5,807
Remaining candidates: 1,167 → 1,067

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 63)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Body postures/verbs (8): しゃがむ (to squat), {跪|ひざまず}く (to kneel), {屈|かが}む (to crouch), {反|そ}る (to bend backward), {捻|ひね}る (to twist), うつ{伏|ぶ}せ (face down), {仰向|あおむ}け (face up), {膝枕|ひざまくら} (lap pillow)
- Geometry (8): {立方体|りっぽうたい} (cube), {円錐|えんすい} (cone), {円柱|えんちゅう} (cylinder), {球|きゅう} (sphere), {多角形|たかっけい} (polygon), {対角線|たいかくせん} (diagonal), {弧|こ} (arc), {放物線|ほうぶつせん} (parabola)
- Opposite pairs (10): {内外|ないがい} (inside and outside), {大小|だいしょう} (large and small), {長短|ちょうたん} (long and short), {表裏|ひょうり} (front and back), {出入|でい}り (going in and out), {開閉|かいへい} (opening and closing), {高低|こうてい} (high and low), {軽重|けいちょう} (light and heavy), {善悪|ぜんあく} (good and evil), {正誤|せいご} (right and wrong)
- Abstract concepts (15): {信頼性|しんらいせい} (reliability), {効率性|こうりつせい} (efficiency), {透明性|とうめいせい} (transparency), {柔軟性|じゅうなんせい} (flexibility), {汎用性|はんようせい} (versatility), {利便性|りべんせい} (convenience), {耐久性|たいきゅうせい} (durability), {整合性|せいごうせい} (consistency), {持続性|じぞくせい} (sustainability), {即効性|そっこうせい} (quick effectiveness), {再現性|さいげんせい} (reproducibility), {公平性|こうへいせい} (fairness), {合理性|ごうりせい} (rationality), {独自性|どくじせい} (originality), {普遍性|ふへんせい} (universality)
- Events/Ceremonies (7): {卒業式|そつぎょうしき} (graduation ceremony), お{正月|しょうがつ} (New Year), お{盆|ぼん} (Obon festival), {七五三|しちごさん} (Shichi-Go-San), {節分|せつぶん} (Setsubun), {歓迎会|かんげいかい} (welcome party), {送別会|そうべつかい} (farewell party)
- Nature/Geography (6): {干潟|ひがた} (tidal flat), {荒野|こうや} (wilderness), {湿原|しつげん} (wetland), {水源|すいげん} (water source), {原野|げんや} (prairie), {河口|かこう} (river mouth)
- Tools (6): コンパス (compass), {分度器|ぶんどき} (protractor), {虫眼鏡|むしめがね} (magnifying glass), {巻|ま}き{尺|じゃく} (tape measure), {万力|まんりき} (vise), {梃子|てこ} (lever)
- Technology (8): SNS (social media), ウェブ (web), サイト (site), ブラウザ (browser), スクリーンショット (screenshot), {英和|えいわ} (English-Japanese), ハッシュタグ (hashtag), {画像|がぞう}{編集|へんしゅう} (image editing)
- Modern vocabulary (8): タピオカ (tapioca), ペットボトル (plastic bottle), フリーター (freeter), ニート (NEET), {非正規|ひせいき} (non-regular), {正社員|せいしゃいん} (full-time employee), {派遣|はけん} (temporary worker), {契約|けいやく}{社員|しゃいん} (contract employee)
- Business/formal (24): {委託|いたく} (consignment), {懸念|けねん} (concern), {顕著|けんちょ} (remarkable), {獲得|かくとく} (acquisition), {把握|はあく} (grasp), {暫定|ざんてい} (provisional), {妥当|だとう} (appropriate), {端末|たんまつ} (terminal), {拠点|きょてん} (base), {趣旨|しゅし} (gist), {指摘|してき} (pointing out), {是正|ぜせい} (correction), {促進|そくしん} (promotion), {抑制|よくせい} (suppression), {固有|こゆう} (inherent), {不十分|ふじゅうぶん} (insufficient), {革新|かくしん} (innovation), {保持|ほじ} (retention), {遂行|すいこう} (accomplishment), {簡潔|かんけつ} (concise)

Notable entry features:
- Comprehensive geometry vocabulary extending beyond basic shapes
- Abstract concept entries useful for academic and business discussions
- Opposite pair vocabulary commonly used in formal writing
- Employment status terms reflecting modern Japanese workforce categories
- Cross-reference added linking antonyms ({促進|そくしん}↔{抑制|よくせい})

Total entries: 5,607 → 5,707
Remaining candidates: 1,252 → 1,167

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 62)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Geometry (13): {三角形|さんかくけい} (triangle), {四角形|しかくけい} (quadrilateral), {正方形|せいほうけい} (square), {長方形|ちょうほうけい} (rectangle), {直線|ちょくせん} (straight line), {曲線|きょくせん} (curve), {円周|えんしゅう} (circumference), {直径|ちょっけい} (diameter), {直角|ちょっかく} (right angle), {平行|へいこう} (parallel), {垂直|すいちょく} (perpendicular), {傾斜|けいしゃ} (slope), {頂点|ちょうてん} (vertex)
- Position/Process (12): {内側|うちがわ} (inside), {外側|そとがわ} (outside), {由来|ゆらい} (origin), {手順|てじゅん} (procedure), {手続|てつづ}き (procedure), {方式|ほうしき} (method), {様式|ようしき} (style), パターン (pattern), {終点|しゅうてん} (terminal), {中間|ちゅうかん} (middle), {領域|りょういき} (domain), {順序|じゅんじょ} (order)
- Business/Finance (15): {配送|はいそう} (delivery), {返品|へんぴん} (return), {決済|けっさい} (settlement), {入金|にゅうきん} (deposit), {出金|しゅっきん} (withdrawal), {利息|りそく} (interest), {原価|げんか} (cost), {単価|たんか} (unit price), {総額|そうがく} (total amount), {数量|すうりょう} (quantity), {分量|ぶんりょう} (amount), {重量|じゅうりょう} (weight), {年収|ねんしゅう} (annual income), プレゼン (presentation), ミーティング (meeting)
- Tools (10): {金槌|かなづち} (hammer), {鋸|のこぎり} (saw), ドライバー (screwdriver), {懐中電灯|かいちゅうでんとう} (flashlight), {物差|ものさ}し (ruler), {電卓|でんたく} (calculator), {顕微鏡|けんびきょう} (microscope), {望遠鏡|ぼうえんきょう} (telescope), {体温計|たいおんけい} (thermometer), {体重計|たいじゅうけい} (scale)
- Plants/Nature (5): たんぽぽ (dandelion), チューリップ (tulip), サボテン (cactus), {苗|なえ} (seedling), {蝋燭|ろうそく} (candle)
- Ceremonies (3): {結婚式|けっこんしき} (wedding), {成人式|せいじんしき} (coming-of-age), {入学式|にゅうがくしき} (entrance ceremony)
- Geography (5): ジャングル (jungle), {高原|こうげん} (plateau), {海辺|うみべ} (seaside), {群島|ぐんとう} (archipelago), {本土|ほんど} (mainland)
- Occupations (3): {写真家|しゃしんか} (photographer), {秘書|ひしょ} (secretary), {駅員|えきいん} (station staff)
- Culture (2): {茶道|ちゃどう} (tea ceremony), バンド (band)
- Body/Sleep (2): いびき (snoring), {寝返|ねがえ}り (turning over in sleep)
- Office supplies (2): ホッチキス (stapler), クリップ (clip)
- Advice (3): {助言|じょげん} (advice), {忠告|ちゅうこく} (warning), {要請|ようせい} (request)
- Abstract (20): ブーム (boom), {名声|めいせい} (fame), {任務|にんむ} (duty), {役職|やくしょく} (position), {階級|かいきゅう} (class), {描写|びょうしゃ} (description), {苦悩|くのう} (anguish), {対処|たいしょ} (dealing with), {措置|そち} (measure), {処分|しょぶん} (disposal), {監視|かんし} (surveillance), {修行|しゅぎょう} (training), {慣習|かんしゅう} (custom), {中世|ちゅうせい} (medieval), {活力|かつりょく} (vitality), {精力|せいりょく} (energy), {見識|けんしき} (insight), {野望|やぼう} (ambition), {必然|ひつぜん} (inevitability), {象徴|しょうちょう} (symbol)
- Adverbs (5): {極|きわ}めて (extremely), {若干|じゃっかん} (some), {次第|しだい}に (gradually), {無論|むろん} (of course), {仲直|なかなお}り (reconciliation)

Notable entry features:
- Comprehensive geometry vocabulary for mathematical contexts
- Business/finance terms covering transactions and measurements
- Tool vocabulary useful for daily life and DIY contexts
- Abstract concepts covering emotions, social status, and philosophical terms

Total entries: 5,507 → 5,607
Remaining candidates: 1,351 → 1,252

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
4. Place file in correct directory based on reading and ID:
   - Directory: `entries/{kana}/{prefix}/` where:
     - `{kana}`: Based on first kana of reading (あ行 → `a/`, か行 → `ka/`, etc.)
     - `{prefix}`: First 2 characters of entry ID (e.g., `taberu_00001` → `ta/`)
   - Example: `entries/ta/ta/taberu_00001.json`
5. File naming: `{romaji}_{5-digit-id}.json`

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
python3 build/validate.py --id taberu_00001

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
- Format: `{romanized_reading}_{5-digit-id}.json`
- Romanization: Modified Hepburn with kana-faithful long vowels
- Directory: `entries/{kana}/{prefix}/` where:
  - `{kana}`: Based on first kana of reading (あ → `a/`, か → `ka/`, etc.)
  - `{prefix}`: First 2 characters of entry ID (e.g., `taberu` → `ta/`)
- Example: `entries/ta/ta/taberu_00001.json`
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
