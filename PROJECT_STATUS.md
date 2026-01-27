# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-27
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
- **Total entries**: 8,469
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 5,616 | Unassigned: 0 ✓
- **Candidate words**: ~500 words tracked in `candidate_words.json`
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

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 173)
Added 30 new dictionary entries from candidate_words.json, covering expressions/emotions vocabulary, personality types, communication skills, transportation vocabulary, and work culture:

- **Smile/Laugh Expressions (7)**: {薄笑|うすわら}い (smirk), {高笑|たかわら}い (loud laugh), {照|て}れ{笑|わら}い (embarrassed smile), {泣|な}き{笑|わら}い (laughing through tears), {思|おも}い{出|だ}し{笑|わら}い (laughing at memory), {嘘泣|うそな}き (fake crying), {作|つく}り{笑|わら}い (fake smile)
- **Personality Types (6)**: {社交的|しゃこうてき} (sociable), {内向的|ないこうてき} (introverted), {外向的|がいこうてき} (extroverted), {無神経|むしんけい} (insensitive), {多弁|たべん} (talkative), {二面性|にめんせい} (two-faced nature)
- **Communication Skills (4)**: {話|はな}し{上手|じょうず} (good speaker), {聞|き}き{上手|じょうず} (good listener), {告|つ}げ{口|ぐち} (tattling), {揚|あ}げ{足取|あしと}り (nitpicking)
- **Social/Dining (4)**: {会費|かいひ} (membership fee), {別会計|べつかいけい} (separate checks), {持|も}ち{寄|よ}り (potluck), もらい{泣|な}き (sympathetic crying)
- **Transportation (4)**: {落|お}とし{物|もの} (lost property), {回数券|かいすうけん} (book of tickets), {人身事故|じんしんじこ} (rail accident), {遅延証明|ちえんしょうめい} (delay certificate)
- **Work Culture (3)**: サービス{残業|ざんぎょう} (unpaid overtime), {飲|の}みニケーション (drinking-based networking), {副業|ふくぎょう} (side job)
- **Conflict/Quarrel (1)**: {口喧嘩|くちげんか} (verbal argument)
- **Gift/Culture (1)**: お{年玉|としだま} (New Year's money gift)

Notable entry features:
- Facial expression vocabulary cluster: {薄笑|うすわら}い/{高笑|たかわら}い/{照|て}れ{笑|わら}い/{作|つく}り{笑|わら}い (types of smiles)
- Emotion vocabulary: {泣|な}き{笑|わら}い (complex emotion), もらい{泣|な}き (empathetic crying)
- Personality psychology terms: {内向的|ないこうてき}/{外向的|がいこうてき} (introversion/extroversion)
- ~{上手|じょうず} pattern: {話|はな}し{上手|じょうず}/{聞|き}き{上手|じょうず} (communication skills)
- Japanese work culture: サービス{残業|ざんぎょう}/{飲|の}みニケーション (workplace practices)
- Train culture: {人身事故|じんしんじこ}/{遅延証明|ちえんしょうめい} (commuter vocabulary)
- Japanese customs: お{年玉|としだま} (New Year's money gift tradition)

Total entries: 8,439 → 8,469
Remaining candidates: ~530 → ~500

### 2026-01-27 (Vocabulary Expansion - 30 New Entries, Session 172)
Added 30 new dictionary entries from candidate_words.json, covering health/medical terms, onomatopoeia, katakana loanwords, environmental vocabulary, personality types, compound verbs, and traditional Japanese vocabulary:

- **Health/Medical (6)**: {肌荒|はだあ}れ (rough skin), {食|しょく}あたり (food poisoning), {肺炎|はいえん} (pneumonia), {喘息|ぜんそく} (asthma), {関節炎|かんせつえん} (arthritis), {嘔吐|おうと} (vomiting)
- **Onomatopoeia (3)**: がちがち (rigid/stiff), じりじり (scorching/gradually), ごつごつ (rugged/bony)
- **Katakana Loanwords (5)**: コミュニケーション (communication), コミュニティ (community), ワンルーム (studio apartment), システム (system), エラー (error)
- **Environment (3)**: {伐採|ばっさい} (logging), {植林|しょくりん} (afforestation), {食物連鎖|しょくもつれんさ} (food chain)
- **Personality Types (3)**: {食|く}わず{嫌|ぎら}い (disliking without trying), {恥|は}ずかしがり{屋|や} (shy person), {寂|さび}しがり{屋|や} (lonely person)
- **Compound Verbs (2)**: {撒|ま}き{散|ち}らす (to scatter), {掻|か}き{消|け}す (to drown out)
- **Weather/Seasons (2)**: {花冷|はなび}え (late spring cold), {寝違|ねちが}える (stiff neck from sleep)
- **Household (1)**: {整理整頓|せいりせいとん} (organizing/tidying up)
- **Traditional (1)**: {弓|ゆみ} (bow)
- **Expression (1)**: もしかしたら (perhaps/maybe)
- **Miscellaneous (3)**: {方角|ほうがく} (direction), {試乗|しじょう} (test drive), {鉄筋|てっきん} (rebar/reinforced concrete)

Notable entry features:
- Medical vocabulary cluster: disease names ending in {炎|えん} ({肺炎|はいえん}/{関節炎|かんせつえん})
- Onomatopoeia with texture/sensation meanings: がちがち/じりじり/ごつごつ (mimetic words)
- Environmental vocabulary: {伐採|ばっさい}/{植林|しょくりん} (forestry), {食物連鎖|しょくもつれんさ} (ecology)
- Personality type patterns with {屋|や}: {恥|は}ずかしがり{屋|や}/{寂|さび}しがり{屋|や}
- Traditional Japanese culture: {弓|ゆみ} with notes on {弓道|きゅうどう} (kyudo)
- Wasei-eigo terms: ワンルーム (studio apartment), with housing terminology notes
- 5 new kanji added to kanji index: 伐 (02089), 喘 (02090), 嘔 (02091), 撒 (02092), 肺 (02093)

Total entries: 8,409 → 8,439
Remaining candidates: ~560 → ~530
New kanji: 2,088 → 2,093

### 2026-01-26 (Vocabulary Expansion - 30 New Entries, Session 171)
Added 30 new dictionary entries from candidate_words.json, covering counter questions, time/celestial vocabulary, weather terms, compound verbs, financial vocabulary, memory-related words, travel expressions, cognitive abilities, housing rooms, and Japanese food:

- **Counter Questions (3)**: {何度|なんど} (how many times), {何人|なんにん} (how many people), {何歳|なんさい} (how old)
- **Time/Celestial (5)**: {明|あ}け{方|がた} (dawn), {日|ひ}の{出|で} (sunrise), {三日月|みかづき} (crescent moon), {満月|まんげつ} (full moon), {新月|しんげつ} (new moon)
- **Weather (2)**: {通|とお}り{雨|あめ} (passing shower), {底冷|そこび}え (bone-chilling cold)
- **Compound Verbs (4)**: {聞|き}き{慣|な}れる (become used to hearing), {迷|まよ}い{込|こ}む (wander into), {引|ひ}き{抜|ぬ}く (pull out/headhunt), {投|な}げ{込|こ}む (throw into)
- **Financial (3)**: {利子|りし} (interest), {分割払|ぶんかつばら}い (installment payment), {一括払|いっかつばら}い (lump-sum payment)
- **Memory/Error (3)**: {勘違|かんちが}い (misunderstanding), {物忘|ものわす}れ (forgetfulness), {ど忘|わす}れ (memory lapse)
- **Travel (2)**: {日帰|ひがえ}り (day trip), {外泊|がいはく} (staying out overnight)
- **Cognitive Abilities (4)**: {集中力|しゅうちゅうりょく} (concentration), {想像力|そうぞうりょく} (imagination), {記憶力|きおくりょく} (memory), {判断力|はんだんりょく} (judgment)
- **Housing (2)**: {洗面所|せんめんじょ} (washroom), {脱衣所|だついじょ} (changing room)
- **Japanese Food (2)**: {肉|にく}じゃが (nikujaga), {親子丼|おやこどん} (oyakodon)

Notable entry features:
- Moon phase vocabulary cluster: {新月|しんげつ}/{三日月|みかづき}/{満月|まんげつ} with astronomical notes
- Cognitive ability cluster: {集中力|しゅうちゅうりょく}/{想像力|そうぞうりょく}/{記憶力|きおくりょく}/{判断力|はんだんりょく} (～{力|りょく} compounds)
- Payment vocabulary contrast: {分割払|ぶんかつばら}い vs {一括払|いっかつばら}い
- Memory-related words: {物忘|ものわす}れ (chronic) vs {ど忘|わす}れ (momentary) vs {勘違|かんちが}い (misinterpretation)
- Japanese bath culture: {洗面所|せんめんじょ}/{脱衣所|だついじょ} with house layout notes
- Home cooking classics: {肉|にく}じゃが/{親子丼|おやこどん} with recipe and cultural notes
- Multi-sense entry: {引|ひ}き{抜|ぬ}く (physical pulling vs. headhunting)

Total entries: 8,379 → 8,409
Remaining candidates: ~590 → ~560

### 2026-01-26 (New Candidates - 100 Words Added)
Added 100 new candidate words to `candidate_words.json` across diverse domains:

**Common Adverbs/Expressions (3)**: {改|あらた}めて (anew), {思|おも}い{切|き}り (with all one's might), やむを{得|え}ず (unavoidably)

**Housing/Architecture (6)**: {書棚|しょだな} (bookshelf), {洗面所|せんめんじょ} (washroom), {脱衣所|だついじょ} (changing room), {応接間|おうせつま} (reception room), {踊|おど}り{場|ば} (landing of stairs)

**Household Chores (5)**: {芝刈|しばか}り (lawn mowing), {草取|くさと}り (weeding), {水撒|みずま}き (watering), {雑巾|ぞうきん}がけ (mopping), {窓拭|まどふ}き (window cleaning)

**Cooking/Food (9)**: {圧力鍋|あつりょくなべ} (pressure cooker), {蒸|む}し{器|き} (steamer), {炒|いた}め{物|もの} (stir-fry), {出汁巻|だしま}き{卵|たまご} (rolled omelet), きんぴら (kinpira), {筑前煮|ちくぜんに} (chicken stew), {肉|にく}じゃが (nikujaga), {親子丼|おやこどん} (oyakodon), カツ{丼|どん} (katsudon), {牛丼|ぎゅうどん} (gyudon)

**Sports (9)**: {審判員|しんぱんいん} (referee), {線審|せんしん} (line judge), {逆転勝|ぎゃくてんが}ち (comeback victory), {先制点|せんせいてん} (opening goal), {同点|どうてん} (tie score), {空振|からぶ}り (swing and miss), {三振|さんしん} (strikeout), ノーヒット (no-hitter), {打点|だてん} (RBI)

**Technology/Social Media (9)**: SNS{映|ば}え (Instagram-worthy), リポスト (repost), エンゲージメント (engagement), {音声入力|おんせいにゅうりょく} (voice input), {顔認証|かおにんしょう} (facial recognition), {指紋認証|しもんにんしょう} (fingerprint auth), {二段階認証|にだんかいにんしょう} (2FA), クラウドサービス (cloud service), サブスクリプション (subscription)

**Work/Employment (9)**: オンライン{診療|しんりょう} (telemedicine), ハイブリッド{勤務|きんむ} (hybrid work), ワーケーション (workcation), {時差出勤|じさしゅっきん} (staggered hours), フレックス{制|せい} (flextime), {兼業|けんぎょう} (side business), {雇用形態|こようけいたい} (employment type)

**Health/Medical (11)**: メンタルヘルス (mental health), {燃|も}え{尽|つ}き{症候群|しょうこうぐん} (burnout syndrome), {適応障害|てきおうしょうがい} (adjustment disorder), {自律神経|じりつしんけい} (autonomic nervous system), {更年期|こうねんき} (menopause), {免疫力|めんえきりょく} (immunity), {後遺症|こういしょう} (aftereffect), {既往症|きおうしょう} (medical history), {生活習慣病|せいかつしゅうかんびょう} (lifestyle disease), {内臓脂肪|ないぞうしぼう} (visceral fat), {過労|かろう} (overwork)

**Family/Society (7)**: {栄養不足|えいようぶそく} (nutritional deficiency), {運動不足|うんどうぶそく} (lack of exercise), {体力低下|たいりょくていか} (physical decline), {共働|ともばたら}き (dual-income), {待機児童|たいきじどう} (daycare waitlist), {育休|いくきゅう} (childcare leave), {介護休暇|かいごきゅうか} (nursing care leave)

**Education (9)**: {遠隔授業|えんかくじゅぎょう} (remote classes), {学力|がくりょく} (academic ability), {終業式|しゅうぎょうしき} (closing ceremony), {始業式|しぎょうしき} (opening ceremony), クラス{替|が}え (class reshuffling), {通知表|つうちひょう} (report card), {時間割|じかんわり} (timetable), {内申点|ないしんてん} (internal assessment), {偏差値|へんさち} (deviation score), {課外活動|かがいかつどう} (extracurricular), {卒論|そつろん} (graduation thesis)

**Weather/Seasons (6)**: {厳冬|げんとう} (severe winter), {五月晴|さつきば}れ (May weather), {木枯|こが}らし (wintry wind), {雪解|ゆきど}け (thaw), {霜柱|しもばしら} (frost pillars), {残暑|ざんしょ} (lingering heat), {晩秋|ばんしゅう} (late autumn), {初冬|しょとう} (early winter)

**Body/Physical (9)**: {眉間|みけん} (between eyebrows), うなじ (nape of neck), みぞおち (solar plexus), {土踏|つちふ}まず (arch of foot), {青筋|あおすじ} (blue vein), {鳥肌|とりはだ} (goosebumps), {吹|ふ}き{出物|でもの} (pimple), あばた (pockmarks), {歯|は}ぎしり (teeth grinding)

**Sleep-related (6)**: {寝違|ねちが}い (stiff neck from sleep), {寝|ね}つき (sleep onset), {寝覚|ねざ}め (awakening), {目覚|めざ}まし (alarm clock)

**Transportation (2)**: {通勤電車|つうきんでんしゃ} (commuter train), {始発電車|しはつでんしゃ} (first train)

Notable patterns:
- Japanese food culture: Popular donburi dishes and home cooking terminology
- Modern work vocabulary: Remote/hybrid work, work-life balance terms
- Health awareness: Mental health, lifestyle diseases, medical terminology
- Daily life vocabulary: Sleep, body parts, household chores
- Sports terminology: Baseball and competition vocabulary

Candidate count: 490 → 590

### 2026-01-26 (New Candidates - 102 Words Added)
Added 102 new candidate words to `candidate_words.json` across diverse domains:

**Counter Questions (7)**: {何度|なんど} (how many times), {何回|なんかい} (how many times), {何人|なんにん} (how many people), {何枚|なんまい} (how many flat objects), {何冊|なんさつ} (how many books), {何杯|なんばい} (how many cups), {何歳|なんさい} (how old)

**Function Words/Demonstratives (12)**: どちらも (both), {誰|だれ}でも (anyone), そのため (therefore), {その後|そのご} (after that), {その前|そのまえ} (before that), {その間|そのあいだ} (meanwhile), {向|む}こう{側|がわ} (other side), それとなく (indirectly), それなりに (in its own way), それにしても (nevertheless), {何|なん}となく (somehow), {何|なに}かと (one way or another)

**Time Expressions (7)**: {明|あ}け{方|がた} (dawn), {日|ひ}の{出|で} (sunrise), {朝帰|あさがえ}り (coming home in the morning), {日帰|ひがえ}り (day trip), {泊|とま}りがけ (overnight stay), {外泊|がいはく} (staying out overnight), オールナイト (all-night)

**Celestial Bodies (4)**: {三日月|みかづき} (crescent moon), {満月|まんげつ} (full moon), {新月|しんげつ} (new moon), {半月|はんげつ} (half moon)

**Weather (3)**: {通|とお}り{雨|あめ} (passing shower), {底冷|そこび}え (bone-chilling cold), {上弦|じょうげん} (first quarter moon)

**Cooking Terms (12)**: ぶつ{切|ぎ}り (rough chopping), {半切|はんぎ}り (cutting in half), {細切|ほそぎ}り (thin strips), {湯通|ゆどお}し (blanching), {水切|みずき}り (draining water), {油切|あぶらき}り (draining oil), {塩加減|しおかげん} (saltiness), {焦|こ}げ{目|め} (char marks), とろ{火|び} (low heat)

**Compound Verbs (10)**: {聞|き}き{慣|な}れる (become used to hearing), {食|た}べ{慣|な}れる (become used to eating), {住|す}み{慣|な}れる (become accustomed to living), {引|ひ}き{抜|ぬ}く (to pull out), {投|な}げ{込|こ}む (to throw into), {迷|まよ}い{込|こ}む (to wander into)

**Financial Terms (4)**: {利子|りし} (interest), {分割払|ぶんかつばら}い (installment payment), {一括払|いっかつばら}い (lump-sum payment), {副業|ふくぎょう} (side job)

**Mistake/Error Terms (6)**: {聞|き}き{間違|まちが}い (mishearing), {言|い}い{間違|まちが}い (slip of tongue), {書|か}き{間違|まちが}い (writing mistake), {読|よ}み{間違|まちが}い (misreading), {見間違|みまちが}い (mistake in seeing), {勘違|かんちが}い (misunderstanding)

**Personality/Traits (10)**: {恥|は}ずかしがり (shy person), {世話好|せわず}き (likes to help), {物忘|ものわす}れ (forgetfulness), ど{忘|わす}れ (memory lapse), うっかり{忘|わす}れ (careless forgetfulness), {気分転換|きぶんてんかん} (change of pace), {気分屋|きぶんや} (moody person), {記憶違|きおくちが}い (faulty memory), {思|おも}い{違|ちが}い (misconception)

**Ability/力 Compounds (16)**: {気力|きりょく} (willpower), {脚力|きゃくりょく} (leg strength), {腕力|わんりょく} (arm strength), {握力|あくりょく} (grip strength), {持久力|じきゅうりょく} (endurance), {瞬発力|しゅんぱつりょく} (explosive power), {集中力|しゅうちゅうりょく} (concentration), {記憶力|きおくりょく} (memory), {判断力|はんだんりょく} (judgment), {決断力|けつだんりょく} (decisiveness), {行動力|こうどうりょく} (action ability), {実行力|じっこうりょく} (execution ability), {想像力|そうぞうりょく} (imagination), {洞察力|どうさつりょく} (insight), {観察力|かんさつりょく} (observation), {分析力|ぶんせきりょく} (analysis), {理解力|りかいりょく} (comprehension), {説得力|せっとくりょく} (persuasiveness)

**Transportation (5)**: {運転見合|うんてんみあ}わせ (service suspension), {運転再開|うんてんさいかい} (resumption of service), {車両点検|しゃりょうてんけん} (train inspection), {信号故障|しんごうこしょう} (signal malfunction), {睡眠不足|すいみんぶそく} (sleep deprivation)

**Other (6)**: {同期|どうき}する (to synchronize), ワイヤレス (wireless), じんわり (gradually), いくら{何|なん}でも (no matter what), {自力|じりき} (one's own power), {他力|たりき} (help from others)

Notable patterns:
- Counter question words: Complete {何|なん}+counter pattern
- Ability vocabulary: Comprehensive 〜{力|りょく} compounds covering physical, mental, and cognitive abilities
- Mistake vocabulary: Systematic 〜{間違|まちが}い patterns for different senses
- Transportation announcements: Common train delay/suspension vocabulary

Candidate count: 388 → 490

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
