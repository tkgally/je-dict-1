# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-21
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
- **Total entries**: 7,809
- **Vocabulary tier assignment**: Basic: 795 | Core: 1,998 | General: 5,016 | Unassigned: 0 ✓
- **Candidate words**: ~640 words tracked in `candidate_words.json`
- **Priority candidates**: 0 words remaining in `candidate_words_priority.json` (all 94 completed)
- **Cross-references**: 567 total (555 resolved, 97% resolution rate)
- **Audio files**: 1,028 MP3 files covering example sentences

### Vocabulary Tier System
The dictionary uses a three-tier vocabulary classification system (see vocabulary-tiers skill):
- **Basic**: 795 entries (target: 600-800) - fundamental words for basic communication
- **Core**: 1,998 entries (target: 1,600-2,000) - words for adult-level communication
- **General**: 4,866+ entries (no limit) - all other vocabulary useful for learners

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

### 2026-01-21 (Vocabulary Expansion - 30 New Entries, Session 148)
Added 30 new dictionary entries from candidate_words.json, covering practical everyday vocabulary, expressions, and useful Japanese words:

- **Help/Support terms (5)**: {納期|のうき} (delivery date), サポート (support), {助|たす}け (help), {支援|しえん} (support/aid), お{手伝|てつだ}い (help/housemaid)
- **Rest/Break expressions (3)**: {一息|ひといき} (a breather), ひと{休|やす}み (short rest), {行楽|こうらく} (outing/excursion)
- **Shopping terms (2)**: {安売|やすう}り (bargain sale), セール (sale)
- **Direction words (3)**: {真|ま}っ{先|さき} (first of all), {真上|まうえ} (directly above), {真下|ました} (directly below)
- **Emotion verbs (2)**: {恥|は}ずかしがる (to be shy), {寂|さび}しがる (to feel lonely)
- **Usage patterns (2)**: {使|つか}い{方|かた} (how to use), {使|つか}い{道|みち} (use/purpose)
- **Personality/Character (3)**: {心配性|しんぱいしょう} (worrywart), {気前|きまえ} (generosity), {粗相|そそう} (blunder)
- **Adjectives (2)**: ばかばかしい (ridiculous), ちっぽけ (tiny)
- **Other useful vocabulary (8)**: {悟|さと}り (enlightenment), {除菌|じょきん} (disinfection), {千切|ちぎ}る (to tear), {落第|らくだい} (failing), {嫌々|いやいや} (reluctantly), {手加減|てかげん} (holding back), {根幹|こんかん} (root/basis), {堅牢|けんろう} (robust)

Notable entry features:
- Cross-references between {真上|まうえ} ↔ {真下|ました} (directional antonyms)
- Cross-reference: {使|つか}い{方|かた} ↔ {使|つか}い{道|みち} (how to use vs. what to use for)
- がる verb pair: {恥|は}ずかしがる and {寂|さび}しがる showing third-person emotion expression
- お{手伝|てつだ}い with two senses: (1) help/assistance, (2) housemaid (dated)
- {粗相|そそう} with two senses: (1) blunder, (2) toileting accident (euphemism)
- {一息|ひといき} with two senses: (1) a breather, (2) in one breath/without stopping

Total entries: 7,689 → 7,719
Remaining candidates: ~643 → ~613

### 2026-01-21 (Vocabulary Expansion - 30 New Entries, Session 147)
Added 30 new dictionary entries from candidate_words.json, focusing on romaji abbreviations used in Japanese media, technology, daily life, and practical Japanese vocabulary:

- **Youth/Student abbreviations (4)**: JK ({女子高生|じょしこうせい} - high school girl), JC ({女子中学生|じょしちゅうがくせい} - middle school girl), DK ({男子高生|だんしこうせい} - high school boy), JD ({女子大生|じょしだいせい} - female college student)
- **Media/Entertainment (8)**: SP (special program/security personnel), VTR (video clip), MC (master of ceremonies), PR (public relations), PV (promotional video), MV (music video), BL (boys' love), GL (girls' love)
- **Anime/Manga (3)**: OP (opening theme), ED (ending theme), OVA (original video animation)
- **Lifestyle (3)**: LDK (living-dining-kitchen), TPO (time, place, occasion), EV (electric vehicle)
- **Automotive (2)**: AT (automatic transmission), MT (manual transmission)
- **Technology/Gaming (5)**: NPC (non-player character), RPG (role-playing game), AI (artificial intelligence), VR (virtual reality), AR (augmented reality)
- **Japanese vocabulary (5)**: {既成概念|きせいがいねん} (preconceived notion), {概略|がいりゃく} (outline), {采配|さいはい} (command/leadership), お{粗末|そまつ} (poor quality), {不振|ふしん} (slump)

Notable entry features:
- Cross-references: JK ↔ JC ↔ DK, BL ↔ GL, OP ↔ ED, AT ↔ MT, VR ↔ AR, PV ↔ MV
- SP with two senses: (1) TV special program, (2) security personnel
- NPC with internet slang meaning (someone without independent thought)
- LDK with explanation of Japanese real estate notation (1LDK, 2LDK, etc.)
- TPO as essential Japanese etiquette concept
- {采配|さいはい} with etymology from commander's baton
- お{粗末|そまつ} with humble expression usage after serving meals

Total entries: 7,659 → 7,689
Remaining candidates: ~673 → ~643

### 2026-01-21 (Vocabulary Expansion - 30 New Entries, Session 146)
Added 30 new dictionary entries from candidate_words.json, covering romaji abbreviations commonly used in Japan and practical Japanese vocabulary:

- **Romaji abbreviations (10)**: CM (TV commercial), NG (blooper), BGM (background music), OB (male alumnus), OG (female alumna), OL (female office worker), PC (personal computer), DIY (do-it-yourself), GW (Golden Week), OK (okay)
- **Difficult situations (5)**: {躊躇|ちゅうちょ} (hesitation), {板挟|いたばさ}み (caught between), {空回|からまわ}り (spinning wheels), とばっちり (collateral damage), {八方塞|はっぽうふさ}がり (blocked in all directions)
- **Work/business (5)**: {手抜|てぬ}き (cutting corners), {根回|ねまわ}し (groundwork), {勤怠|きんたい} (attendance), {欠勤|けっきん} (absence from work), {未読|みどく} (unread)
- **Social/lifestyle (6)**: {噂話|うわさばなし} (gossip), {立|た}ち{話|ばなし} (standing chat), {世渡|よわた}り (getting through life), {処世術|しょせいじゅつ} (wisdom for living), {裏表|うらおもて} (two-faced), {腹黒|はらぐろ}い (scheming)
- **Shopping/food (4)**: {見切|みき}り{品|ひん} (clearance item), お{得|とく} (good deal), {偏食|へんしょく} (picky eating), {間食|かんしょく} (snacking)

Notable entry features:
- Romaji abbreviations covering media (CM, NG, BGM), alumni (OB, OG), work (OL, PC), and lifestyle (DIY, GW, OK)
- Cross-references between OB ↔ OG (gender equivalents) and OK ↔ NG (opposites)
- {根回|ねまわ}し with cultural notes about Japanese business consensus-building
- {世渡|よわた}り ↔ {処世術|しょせいじゅつ} cross-references for related social navigation concepts
- {腹黒|はらぐろ}い with cultural explanation of the "belly" as seat of true intentions in Japanese
- {八方塞|はっぽうふさ}がり with etymology from {陰陽道|おんみょうどう} (onmyodo)

Total entries: 7,629 → 7,659
Remaining candidates: ~703 → ~673

### 2026-01-21 (New Candidates - 102 Romaji Abbreviations Added, Session 145)
Added 102 new candidate words to `candidate_words.json` focusing on romaji abbreviations used in Japanese. These include Japanese-origin abbreviations (from Japanese words), 和製英語 abbreviations (unique Japanese usage of English terms), and specialized domain abbreviations commonly used in Japan:

**Japanese-Origin Abbreviations** (~8 words):
- Student/age categories: JK (女子高生 - high school girl), JC (女子中学生 - middle school girl), JD (女子大生 - female college student), DK (男子高生 - high school boy)
- Food: TKG (卵かけご飯 - egg over rice)
- Alumni: OB (old boy - male alumnus), OG (old girl - female alumna)
- Work: OL (office lady - female office worker)

**Media/Entertainment Abbreviations** (~15 words):
- TV/film: CM (commercial message), NG (no good - blooper), SP (special), VTR (video tape recording), PV (promotional video), MV (music video)
- Anime/manga: CV (character voice), BL (boys' love), GL (girls' love), OP (opening theme), ED (ending theme), OVA (original video animation), SE (sound effect)
- General: MC (master of ceremonies), BGM (background music), CG (computer graphics)

**Technology/Computing** (~15 words):
- Hardware: PC (personal computer), USB, CD, DVD, LED, LCD
- Internet: HP (homepage), URL, PDF
- Mobile: AI, IT (already existed), ID (already existed)
- Gaming: NPC, RPG, FPS, MMO, RTA (real-time attack)

**Automotive/Transportation** (~7 words):
- Transmission: AT (automatic), MT (manual)
- Vehicle types: EV (electric vehicle)
- Interchange: IC
- Appliances: IH (induction heating), AC (air conditioning)

**Sports Abbreviations** (~8 words):
- Soccer positions: FW (forward), GK (goalkeeper), DF (defender), MF (midfielder)
- Soccer terms: PA (penalty area), PK (penalty kick)
- Awards: MVP (most valuable player)
- Organizations: NBA, MLB

**Medical/Science** (~10 words):
- Medical: CT, MRI, PTSD, ADHD, AED, CPR, OTC
- Science: DNA, CO2, IQ, EQ

**Business/Organizations** (~10 words):
- Organizations: NHK, UN, EU, NPO (already existed), NGO, PTA
- Business: CEO, PR, OJT, FAQ
- Lifestyle: DIY, VR, AR, LCC, EC

**Lifestyle/Modern Terms** (~15 words):
- Housing: LDK (living/dining/kitchen)
- Social: TPO (time, place, occasion), NEET, DINKS
- Media: TV, FM, AM, GPS, DJ
- Communication: OK, SOS, VIP, LGBT, SDGs (already existed)
- Technology: iOS, OS, SS (screenshot)

Notable features:
- Comprehensive coverage of romaji abbreviations used daily in Japan
- Includes Japanese-coined terms (JK, TKG, KY already in dictionary) that reflect uniquely Japanese concepts
- Media/entertainment abbreviations essential for understanding anime, TV, and internet culture
- Practical technology and business abbreviations learners encounter in daily life
- Sports abbreviations commonly used in Japanese sports broadcasting

Candidate count: 601 → 703

### 2026-01-20 (Vocabulary Expansion - 30 New Entries, Session 144)
Added 30 new dictionary entries from candidate_words.json, covering nature/weather vocabulary, phone/technology terms, health/sleep vocabulary, work-related terms, communication patterns, and household activities:

- **Nature/weather (3)**: {夕暮|ゆうぐ}れ (twilight), {木漏|こも}れ{日|び} (dappled sunlight), {霧雨|きりさめ} (drizzle)
- **Phone/technology (7)**: {着信|ちゃくしん} (incoming call), {留守電|るすでん} (voicemail), マナーモード (silent mode), {電池切|でんちぎ}れ (dead battery), {圏外|けんがい} (out of range), {試着|しちゃく} (trying on clothes), {衝動買|しょうどうが}い (impulse buying)
- **Health/sleep (4)**: {寝不足|ねぶそく} (lack of sleep), {夜更|よふ}かし (staying up late), {二度寝|にどね} (going back to sleep), {肩凝|かたこ}り (stiff shoulders)
- **Work terms (6)**: {在宅|ざいたく} (remote work), {定時|ていじ} (regular hours), {直行|ちょっこう} (going directly), {直帰|ちょっき} (going straight home), {配慮|はいりょ} (consideration), {踏|ふ}まえる (to be based on)
- **Communication (6)**: やり{取|と}り (exchange), {駆|か}け{引|ひ}き (bargaining), {前置|まえお}き (preamble), {忖度|そんたく} (surmising wishes), {婉曲|えんきょく} (euphemistic), {暗示|あんじ} (hint)
- **Household (4)**: {分別|ぶんべつ} (sorting garbage), {詰|つ}め{替|か}え (refill), {模様替|もようが}え (room rearrangement), {衣替|ころもが}え (seasonal clothing change)

Notable entry features:
- {木漏|こも}れ{日|び} with cultural notes about this untranslatable Japanese aesthetic concept
- Modern phone/technology vocabulary essential for daily life in Japan
- マナーモード with cultural context about phone etiquette on public transport
- {忖度|そんたく} with notes about its prominence in 2017 political scandals
- Cross-references between {直行|ちょっこう} ↔ {直帰|ちょっき} work terms
- {衣替|ころもが}え with explanation of Japan's traditional June 1st/October 1st clothing change dates

Total entries: 7,599 → 7,629
Remaining candidates: ~631 → ~601

### 2026-01-20 (New Candidates - 102 Words Added, Session 143)
Added 102 new candidate words to `candidate_words.json` with balanced coverage across multiple categories:

**High-Frequency Business/Academic Terms** (~10 words):
- Business vocabulary: {踏|ふ}まえる (to be based on), やり{取|と}り (exchange), {配慮|はいりょ} (consideration), {網羅|もうら} (comprehensive coverage), {裏付|うらづ}け (backing)
- Process terms: {先送|さきおく}り (postponement), {棚上|たなあ}げ (shelving), {足踏|あしぶ}み (marking time), {行|い}き{詰|づ}まり (deadlock)

**Idiomatic Compound Expressions** (~15 words):
- Disappointment: {拍子抜|ひょうしぬ}け (anticlimax), {肩透|かたすか}かし (letdown), {骨折|ほねお}り{損|ぞん} (wasted effort), {空回|からまわ}り (futile effort), {二度手間|にどでま} (doing something twice)
- Social situations: とばっちり (getting caught up in), {板挟|いたばさ}み (caught between), {八方塞|はっぽうふさ}がり (blocked in all directions)
- Effort/work: {手抜|てぬ}き (cutting corners)

**Nature/Weather Terms** (~6 words):
- Time of day: {夕暮|ゆうぐ}れ (twilight)
- Weather phenomena: {木漏|こも}れ{日|び} (sunlight through leaves), {潮風|しおかぜ} (sea breeze), {朝露|あさつゆ} (morning dew), {霧雨|きりさめ} (drizzle)
- Emotions: {躊躇|ちゅうちょ} (hesitation)

**Daily Life/Household** (~20 words):
- Sleep-related: {夜更|よふ}かし (staying up late), うたた{寝|ね} (dozing off), {二度寝|にどね} (going back to sleep), {寝相|ねぞう} (sleeping posture), {寝不足|ねぶそく} (lack of sleep), ぎっくり{腰|ごし} (strained back), {寝違|ねちが}え (stiff neck)
- Health: {肩凝|かたこ}り (stiff shoulders)
- Work: {定時|ていじ} (regular hours), {勤怠|きんたい} (attendance), {欠勤|けっきん} (absence), {直行|ちょっこう} (going directly), {直帰|ちょっき} (going straight home), {在宅|ざいたく} (remote work)
- Household: {布団干|ふとんほ}し (airing bedding), {衣替|ころもが}え (seasonal clothing change), {模様替|もようが}え (room rearrangement), {水回|みずまわ}り (water areas), {詰|つ}め{替|か}え (refill), ゴミ{出|だ}し (taking out trash)

**Garbage/Recycling Terms** (~4 words):
- Waste: {生|なま}ゴミ (food waste), {粗大|そだい}ゴミ (bulky garbage), {分別|ぶんべつ} (sorting)

**Shopping/Consumer Terms** (~10 words):
- Buying patterns: まとめ{買|が}い (bulk buying), {買|か}いだめ (stocking up), {衝動買|しょうどうが}い (impulse buying), ついで{買|が}い (buying on the way), {試着|しちゃく} (trying on clothes), {試飲|しいん} (drink tasting)
- Sales: お{得|とく} (bargain), {目玉商品|めだましょうひん} (featured item), タイムセール (time-limited sale), {見切|みき}り{品|ひん} (clearance item)

**Technology/Digital Terms** (~10 words):
- Phone: {着信|ちゃくしん} (incoming call), {不在着信|ふざいちゃくしん} (missed call), {留守電|るすでん} (voicemail), {着信音|ちゃくしんおん} (ringtone), マナーモード (silent mode), {機内|きない}モード (airplane mode)
- Device states: {電池切|でんちぎ}れ (battery dead), {圏外|けんがい} (out of range), {未読|みどく} (unread)

**Productive Patterns** (~15 words):
- ～ごたえ (satisfying to ~): {食|た}べごたえ, {飲|の}みごたえ, {作|つく}りごたえ, {読|よ}みがい, {働|はたら}きがい
- Communication: {立|た}ち{話|ばなし} (standing chat), {噂話|うわさばなし} (gossip)
- Discussion terms: {見|み}え{隠|かく}れ (appearing/disappearing), {押|お}し{問答|もんどう} (argument), {駆|か}け{引|ひ}き (bargaining), {前置|まえお}き (preamble), つなぎ (stopgap)

**Social/Interpersonal Terms** (~15 words):
- Personality: {腹黒|はらぐろ}い (scheming), {打算的|ださんてき} (calculating), {裏表|うらおもて} (two-faced), {八方美人|はっぽうびじん} (people-pleaser)
- Life skills: {世渡|よわた}り (getting through life), {処世術|しょせいじゅつ} (wisdom for living), {根回|ねまわ}し (groundwork), {忖度|そんたく} (surmising someone's wishes)
- Communication: {察|さっ}する (to sense), {行間|ぎょうかん}を{読|よ}む (read between lines), {含|ふく}み (implication), {暗示|あんじ} (hint), {遠回|とおまわ}し (indirect), {婉曲|えんきょく} (euphemism)
- Vagueness: うやむや (vague), あやふや (uncertain), {曖昧|あいまい} (ambiguous), {不明瞭|ふめいりょう} (unclear)

Notable features:
- Strong coverage of daily life vocabulary (household, shopping, technology)
- Productive morphological patterns (～ごたえ, ～がい compounds)
- Social/interpersonal vocabulary useful for understanding Japanese communication styles
- Modern technology terms (phone, digital device states)
- Practical shopping and consumer vocabulary
- Garbage sorting terms (important for daily life in Japan)

Candidate count: 529 → 631

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
