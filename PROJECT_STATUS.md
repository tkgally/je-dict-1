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
- **Total entries**: 6,651
- **Vocabulary tier assignment**: Basic: 1,113 | Core: 4,762 | General: 449 | Unassigned: 307
- **Candidate words**: ~683 words tracked in `candidate_words.json`
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

### 2026-01-18 (Vocabulary Expansion - 20 New Entries, Session 98)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Soccer positions** (5): ゴールキーパー (goalkeeper), フォワード (forward), ミッドフィルダー (midfielder), ディフェンダー (defender), スタメン (starting lineup)
- **Sports** (2): ファウル (foul), オフサイド (offside)
- **Modern/Youth culture** (1): {推|お}し{活|かつ} (fan activity supporting idols)
- **Music** (1): ビート (beat/rhythm)
- **Emotions** (2): {怨念|おんねん} (grudge/vengeful spirit), {悔恨|かいこん} (remorse)
- **Construction/Building** (2): {塗装|とそう} (painting/coating), {骨組|ほねぐ}み (framework/skeleton)
- **Legal/Business** (3): {施行|しこう} (enforcement), {納品書|のうひんしょ} (delivery slip), {保存料|ほぞんりょう} (preservative)
- **Science/Environment** (2): {炭素|たんそ} (carbon), {蓄電|ちくでん} (power storage)
- **Technology/Digital** (2): オンデマンド (on-demand), ペーパーレス (paperless)

Notable entry features:
- Complete soccer position set (GK, DF, MF, FW) with abbreviations and cross-references
- {推|お}し{活|かつ} covering modern Japanese fan culture with ～{活|かつ} word pattern
- Environmental vocabulary ({炭素|たんそ}, {蓄電|ちくでん}) for sustainability discussions
- Business document vocabulary ({納品書|のうひんしょ}) with document flow context
- Supernatural/emotional vocabulary ({怨念|おんねん}, {悔恨|かいこん}) with cultural context

Total entries: 6,631 → 6,651
Remaining candidates: 702 → 683

### 2026-01-18 (Vocabulary Expansion - 20 New Entries, Session 97)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Animals** (2): チンパンジー (chimpanzee), アザラシ (seal)
- **Insects** (1): クワガタムシ (stag beetle)
- **Baseball** (2): {投手|とうしゅ} (pitcher), {打者|だしゃ} (batter)
- **Music** (3): {指揮者|しきしゃ} (conductor), {伴奏|ばんそう} (accompaniment), コーラス (chorus)
- **Construction** (3): {新築|しんちく} (newly built), {増築|ぞうちく} (extension), {修繕|しゅうぜん} (repair)
- **Plants** (1): コスモス (cosmos flower)
- **Professions** (2): {税理士|ぜいりし} (tax accountant), {不動産屋|ふどうさんや} (real estate agent)
- **Sports** (1): {連覇|れんぱ} (consecutive championship)
- **Real estate** (3): {管理費|かんりひ} (management fee), {共益費|きょうえきひ} (common expense fee), {分譲|ぶんじょう} (for-sale housing)
- **Finance** (2): {債務|さいむ} (debt), ローン (loan)

Notable entry features:
- Animal vocabulary including zoo favorites (チンパンジー, アザラシ) and popular summer insects (クワガタムシ with hobby/collection context)
- Baseball pair: {投手|とうしゅ} (pitcher) ↔ {打者|だしゃ} (batter) with detailed statistics terminology
- Music terminology covering orchestral ({指揮者|しきしゃ}, {伴奏|ばんそう}) and pop music (コーラス) contexts
- Construction vocabulary for home building and renovation ({新築|しんちく} ↔ {中古|ちゅうこ})
- Real estate terms commonly seen in apartment hunting ({管理費|かんりひ}, {共益費|きょうえきひ}, {分譲|ぶんじょう})
- Finance vocabulary with legal context ({債務|さいむ}, ローン)

Total entries: 6,611 → 6,631
Remaining candidates: 722 → 702

### 2026-01-18 (Vocabulary Expansion - 20 New Entries, Session 96)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Sports/Baseball** (4): {延長戦|えんちょうせん} (overtime), {反則|はんそく} (foul), {打席|だせき} (at-bat), {完封|かんぷう} (shutout)
- **Swimming strokes** (2): バタフライ (butterfly stroke), クロール (front crawl)
- **Carpentry/Tools** (4): のみ (chisel), たがね (cold chisel), {万力|まんりき} (vise), かんな (plane)
- **Vehicle parts** (4): ウィンカー (turn signal), ダッシュボード (dashboard), サイドミラー (side mirror), クラッチ (clutch)
- **Traditional games** (4): あみだくじ (ladder lottery), くじ{引|び}き (lottery drawing), お{手玉|てだま} (beanbag juggling), {竹馬|たけうま} (stilts)
- **Japanese mythology** (1): {座敷童|ざしきわらし} (zashiki-warashi)
- **Natural phenomena** (1): {蜃気楼|しんきろう} (mirage)

Notable entry features:
- Baseball terminology with detailed rules ({延長戦|えんちょうせん}'s extra innings, {完封|かんぷう} statistics)
- Swimming strokes completing the 4{泳法|えいほう} set with cross-references
- Traditional Japanese carpentry tools with technique notes (かんな's pull-type motion)
- Vehicle parts with {和製英語|わせいえいご} notes (ウィンカー from "winker")
- Traditional games with cultural/mathematical explanations (あみだくじ's permutation property)
- Japanese folklore creature {座敷童|ざしきわらし} with detailed mythology
- {蜃気楼|しんきろう} with kanji etymology (giant clam legend)

Total entries: 6,591 → 6,611
Remaining candidates: 742 → 722

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 95)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Traditional games** (4): じゃんけん (rock-paper-scissors), けん{玉|だま} (kendama), サイコロ (dice)
- **Japanese mythology** (2): {河童|かっぱ} (kappa), {天狗|てんぐ} (tengu)
- **Swimming strokes** (2): {平泳|ひらおよ}ぎ (breaststroke), {背泳|せおよ}ぎ (backstroke)
- **Sports terms** (2): {連勝|れんしょう} (winning streak), {連敗|れんぱい} (losing streak)
- **Natural phenomena** (2): {満潮|まんちょう} (high tide), {干潮|かんちょう} (low tide)
- **Physical states** (3): {空腹|くうふく} (hunger), {満腹|まんぷく} (full stomach), {眠気|ねむけ} (sleepiness)
- **Adjectives** (3): {図々|ずうずう}しい (shameless), {気|き}まずい (awkward), もどかしい (frustrating)
- **Cultural items** (2): {招|まね}き{猫|ねこ} (beckoning cat), だるま (daruma doll)
- **Tools** (1): {砥石|といし} (whetstone)

Notable entry features:
- Traditional Japanese games and toys with cultural background (じゃんけん rules, けん{玉|だま} tricks)
- Japanese mythology creatures with folklore details ({河童|かっぱ}'s dish, {天狗|てんぐ}'s characteristics)
- Swimming vocabulary with competitive context
- Antonym pairs: {連勝|れんしょう}↔{連敗|れんぱい}, {満潮|まんちょう}↔{干潮|かんちょう}, {空腹|くうふく}↔{満腹|まんぷく}
- Good luck charms ({招|まね}き{猫|ねこ}, だるま) with symbolic meanings

Total entries: 6,571 → 6,591
Remaining candidates: 762 → 742

### 2026-01-17 (New Candidates - 102 Words Added, Session 94)
Added 102 new candidate words to `candidate_words.json` with balanced coverage:

**Novel categories NOT mentioned in prompt/skill (~52 words):**
- **Gardening** (4): {接|つ}ぎ{木|き} (grafting), {挿|さ}し{木|き} (plant cutting), {雨樋|あまどい} (rain gutter), {土台|どだい} (foundation)
- **Sports** (14): {延長戦|えんちょうせん} (overtime), {反則|はんそく} (foul), {打席|だせき} (at-bat), {打率|だりつ} (batting average), {防御率|ぼうぎょりつ} (ERA), {完封|かんぷう} (shutout), {逆転|ぎゃくてん} (comeback), {敗退|はいたい} (defeat), {連勝|れんしょう} (winning streak), {連敗|れんぱい} (losing streak), {平泳|ひらおよ}ぎ (breaststroke), {背泳|せおよ}ぎ (backstroke), バタフライ (butterfly), クロール (front crawl)
- **Tools/Carpentry** (6): のみ (chisel), たがね (cold chisel), {万力|まんりき} (vise), {糸鋸|いとのこ} (coping saw), かんな (plane), {砥石|といし} (whetstone)
- **Vehicle parts** (6): ウィンカー (turn signal), ダッシュボード (dashboard), サイドミラー (side mirror), バックミラー (rearview mirror), クラッチ (clutch), ワイパー (wiper)
- **Traditional games** (9): {駒|こま} (game piece), サイコロ (dice), じゃんけん (rock-paper-scissors), あみだくじ (ladder lottery), くじ{引|び}き (lottery), お{手玉|てだま} (juggling beanbags), けん{玉|だま} (kendama), {竹馬|たけうま} (stilts), {凧揚|たこあ}げ (kite flying)
- **Mythology** (3): {河童|かっぱ} (kappa), {天狗|てんぐ} (tengu), {座敷童|ざしきわらし} (zashiki-warashi)
- **Natural phenomena** (4): {干潮|かんちょう} (low tide), {満潮|まんちょう} (high tide), {引|ひ}き{潮|しお} (ebb tide), {蜃気楼|しんきろう} (mirage)
- **Other novel categories** (6): {裏地|うらじ} (lining), {縫|ぬ}い{目|め} (seam), {飛|と}び{込|こ}み (diving), ゴーグル (goggles), {羽根|はね}つき (Japanese badminton), {福笑|ふくわら}い (pin-the-face game)

**Standard categories from prompt/skill (~50 words):**
- **～{的|てき} adjectives** (5): {画期的|かっきてき} (groundbreaking), {徹底的|てっていてき} (thorough), {決定的|けっていてき} (decisive), {衝撃的|しょうげきてき} (shocking), {劇的|げきてき} (dramatic)
- **Employment/finance** (5): {左遷|させん} (demotion), {栄転|えいてん} (promotion transfer), {出向|しゅっこう} (temporary transfer), {手取|てど}り (take-home pay), {額面|がくめん} (face value)
- **Academic subjects** (3): {地学|ちがく} (earth science), {生物学|せいぶつがく} (biology), {天文学|てんもんがく} (astronomy)
- **Crafts/hobbies** (3): {木彫|きぼ}り (wood carving), {手芸|しゅげい} (handicraft), {斜線|しゃせん} (diagonal)
- **Physical states/textures** (9): {空腹|くうふく} (hunger), {満腹|まんぷく} (full stomach), {眠気|ねむけ} (sleepiness), ぬめぬめ (slimy), コリコリ (crunchy), プチプチ (popping), {渋|しぶ}い (astringent), {青臭|あおくさ}い (grassy smell), {生臭|なまぐさ}い (fishy smell)
- **Social/emotion terms** (9): {顔見知|かおみし}り (acquaintance), {仲間入|なかまい}り (joining), {仲間外|なかまはず}れ (exclusion), {馴|な}れ{馴|な}れしい (overly familiar), {図々|ずうずう}しい (shameless), {気|き}まずい (awkward), てれくさい (embarrassed), {気恥|きは}ずかしい (bashful), もどかしい (frustrating)
- **Writing/publishing** (6): {行間|ぎょうかん} (line spacing), {余白|よはく} (margin), {下書|したが}き (draft), {添削|てんさく} (correction), {手回|てまわ}し (preparation), {紛|まぎ}らわしい (confusing)
- **Cultural items** (4): だるま (daruma doll), {招|まね}き{猫|ねこ} (beckoning cat), {狛犬|こまいぬ} (shrine guardian), {焦|こ}げ{臭|くさ}い (burnt smell)
- **Music/geometry** (5): {元本|がんぽん} (principal), {対角線|たいかくせん} (diagonal), {音程|おんてい} (pitch/interval)

Notable features:
- Novel categories (~50%) explore areas not mentioned in prompt: sports statistics, traditional Japanese games, carpentry tools, vehicle parts, mythology
- Swimming strokes complete the aquatic sports vocabulary
- Traditional games (じゃんけん, あみだくじ, けん{玉|だま}) cover Japanese childhood culture
- Vehicle interior parts complement existing driving vocabulary
- Mythology ({河童|かっぱ}, {天狗|てんぐ}) adds folklore vocabulary

Candidate count: 660 → 762

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 93)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Animals** (4): ペンギン (penguin), ゴリラ (gorilla), {蜜蜂|みつばち} (honeybee), バッタ (grasshopper)
- **Insects** (1): カマキリ (praying mantis)
- **Weather** (2): {霙|みぞれ} (sleet), {靄|もや} (haze/mist)
- **Infrastructure/Roads** (3): {横断歩道|おうだんほどう} (crosswalk), {路地|ろじ} (alley), ガードレール (guardrail)
- **Kitchen/Household** (4): お{椀|わん} (soup bowl), {鍋敷|なべし}き (trivet), マグカップ (mug), {空気清浄機|くうきせいじょうき} (air purifier)
- **Tools** (1): ねじ{回|まわ}し (screwdriver)
- **Construction** (1): {足場|あしば} (scaffolding)
- **Body Functions** (2): げっぷ (burp), {咳払|せきばら}い (clearing throat)
- **Arts** (1): バレエ (ballet)
- **Medical** (1): {応急処置|おうきゅうしょち} (first aid)

Notable entry features:
- Animal vocabulary including zoo favorites (ペンギン, ゴリラ) and common insects (バッタ, カマキリ, {蜜蜂|みつばち})
- Weather terms {霙|みぞれ} and {靄|もや} with meteorological distinctions
- Infrastructure vocabulary ({横断歩道|おうだんほどう}, ガードレール) for road safety
- Kitchen items with traditional Japanese context (お{椀|わん} for soup, {鍋敷|なべし}き)
- {空気清浄機|くうきせいじょうき} with notes on Japanese allergy season ({花粉|かふん}{症|しょう})
- Body function terms (げっぷ, {咳払|せきばら}い) with cultural etiquette notes
- {応急処置|おうきゅうしょち} with Japanese first aid training context

Total entries: 6,551 → 6,571
Remaining candidates: 680 → 660

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 92)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Compound verbs** (2): {呼|よ}びかける (to call out/appeal), {聞|き}き{直|なお}す (to ask again/re-listen)
- **Adverb** (1): {二度|にど}と (never again)
- **Modern/Digital** (1): {既読|きどく} (read message status)
- **Body/Physical** (3): {欠伸|あくび} (yawn), {瞬|まばた}き (blink), {踝|くるぶし} (ankle)
- **Clothing** (4): {襟|えり} (collar), {裾|すそ} (hem), チャック (zipper), {下駄箱|げたばこ} (shoe cabinet)
- **Home Appliances** (2): {加湿器|かしつき} (humidifier), {除湿機|じょしつき} (dehumidifier)
- **Infrastructure** (3): {踏切|ふみきり} (railroad crossing), {歩道橋|ほどうきょう} (pedestrian overpass), {地下道|ちかどう} (underground passage)
- **Medical** (1): {処方箋|しょほうせん} (prescription)
- **Nature** (1): てんとう{虫|むし} (ladybug)
- **Adjectives** (2): しつこい (persistent/heavy taste), {健気|けなげ} (brave/admirable)

Notable entry features:
- {既読|きどく} covering LINE messaging culture and {既読|きどく}スルー phenomenon
- Antonym pair {加湿器|かしつき}↔{除湿機|じょしつき} for seasonal Japanese climate needs
- Infrastructure vocabulary ({踏切|ふみきり}, {歩道橋|ほどうきょう}, {地下道|ちかどう}) common in urban Japan
- {処方箋|しょほうせん} with Japanese healthcare system context (out-of-hospital dispensing)
- Body function vocabulary ({欠伸|あくび}, {瞬|まばた}き) and clothing terminology ({襟|えり}, {裾|すそ})
- チャック as wasei-eigo (Japanese-made English word)

Total entries: 6,531 → 6,551
Remaining candidates: 700 → 680

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 91)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Modern Slang/Internet** (6): リア{充|じゅう} (person with fulfilling life), コミュ{障|しょう} (socially awkward), KY (can't read the room), ガチ{勢|ぜい} (hardcore fan), アンチ (hater), チルい (chill/relaxed)
- **Tech/Digital** (5): ガジェット (gadget), プロフィール (profile), ユーチューバー (YouTuber), {画面共有|がめんきょうゆう} (screen sharing), プッシュ{通知|つうち} (push notification)
- **Business/Consumer** (2): {入会金|にゅうかいきん} (membership fee), {添加物|てんかぶつ} (additive)
- **Beauty/Appearance** (2): {一重|ひとえ} (single eyelid), {二重|ふたえ} (double eyelid)
- **Polite/Formal** (2): お{手数|てすう} (trouble - polite), {洗練|せんれん} (refinement)
- **Workplace** (1): モラハラ (moral harassment)
- **Agriculture** (2): {堆肥|たいひ} (compost), {果樹園|かじゅえん} (orchard)

Notable entry features:
- Modern youth slang with リア{充|じゅう}, コミュ{障|しょう}, KY reflecting Japanese internet culture
- Gaming/fan community vocabulary (ガチ{勢|ぜい} vs エンジョイ{勢|ぜい})
- Digital communication terms ({画面共有|がめんきょうゆう}, プッシュ{通知|つうち}) for remote work/meetings
- Beauty vocabulary ({一重|ひとえ}↔{二重|ふたえ}) with cultural context
- チルい as example of English loanword becoming Japanese i-adjective
- Workplace harassment terminology (モラハラ) alongside other ハラ words

Total entries: 6,511 → 6,531
Remaining candidates: 716 → 700

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 90)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Social Media/Modern** (4): タイムライン (timeline/feed), {陰|いん}キャ (introvert slang), {陽|よう}キャ (extrovert slang), {投|な}げ{銭|せん} (online tipping)
- **Technology** (2): アナログ (analog/old-fashioned), {自動運転|じどううんてん} (autonomous driving)
- **Business/Consumer** (6): クーポン (coupon), {延長|えんちょう} (extension), {明細|めいさい} (itemization/statement), {同意書|どういしょ} (consent form), {部下|ぶか} (subordinate), {彼氏|かれし} (boyfriend)
- **Public Services** (2): {消防署|しょうぼうしょ} (fire station), {役所|やくしょ} (government office)
- **Traditional Japanese** (2): {不祝儀|ぶしゅうぎ} (condolence money), {蛇|じゃ}の{目傘|めがさ} (traditional umbrella)
- **Modern Lifestyle** (1): {朝活|あさかつ} (morning activity)
- **Four-character idioms** (2): {暗中模索|あんちゅうもさく} (groping in dark), {有名無実|ゆうめいむじつ} (nominal)
- **Adjective** (1): {国際的|こくさいてき} (international)

Notable entry features:
- Social media vocabulary with {陰|いん}キャ/{陽|よう}キャ as antonym pair (youth slang)
- {投|な}げ{銭|せん} covering both traditional (street performers) and modern (streaming tips) usage
- Traditional Japanese culture terms ({不祝儀|ぶしゅうぎ} with envelope etiquette, {蛇|じゃ}の{目傘|めがさ} with craft traditions)
- {朝活|あさかつ} as part of the ～{活|かつ} word pattern trend
- Government/public service vocabulary ({消防署|しょうぼうしょ}, {役所|やくしょ}) with emergency numbers and procedures
- Four-character idioms with etymology and context

Total entries: 6,513 → 6,533
Remaining candidates: 732 → 716

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 89)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Social Media** (2): ハッシュタグ (hashtag), インフルエンサー (influencer)
- **Construction/Building** (4): {内装|ないそう} (interior), {外壁|がいへき} (exterior wall), {断熱|だんねつ} (insulation), {防水|ぼうすい} (waterproofing)
- **Agriculture/Farming** (3): {灌漑|かんがい} (irrigation), {害虫|がいちゅう} (pest), {家畜|かちく} (livestock)
- **Energy/Power** (3): {風力|ふうりょく} (wind power), {原子力|げんしりょく} (nuclear power), {水力|すいりょく} (hydropower)
- **Academic/Publishing** (3): {脚注|きゃくちゅう} (footnote), {出典|しゅってん} (source/reference), {飼育|しいく} (breeding/raising)
- **Emotions** (2): {狂喜|きょうき} (wild joy/ecstasy), {憤慨|ふんがい} (indignation)
- **Body Parts** (2): {二|に}の{腕|うで} (upper arm), {手|て}の{甲|こう} (back of hand)
- **Business** (1): {経理|けいり} (accounting)

Notable entry features:
- Social media vocabulary for modern digital communication
- Construction terms with building industry context and related terminology
- Energy sources vocabulary ({風力|ふうりょく}, {水力|すいりょく}, {原子力|げんしりょく}) as a set
- Agriculture vocabulary including {灌漑|かんがい} with historical notes on Japanese rice cultivation
- Body part terms with beauty/fitness context ({二|に}の{腕|うで} discussion of {振|ふ}り{袖|そで} slang)
- Academic writing terms ({脚注|きゃくちゅう}, {出典|しゅってん}) with cross-references

Total entries: 6,493 → 6,513
Remaining candidates: 752 → 732

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 88)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Tech/Finance** (5): {仮想通貨|かそうつうか} (cryptocurrency), ブロックチェーン (blockchain), {電子決済|でんしけっさい} (electronic payment), QRコード (QR code), ロボット (robot)
- **Modern Business** (5): ノマド (digital nomad), コワーキング (coworking), イノベーション (innovation), ベンチャー (venture/startup), ソリューション (solution)
- **Environmental** (3): {脱炭素|だつたんそ} (decarbonization), カーボンニュートラル (carbon neutral), {電動|でんどう} (electric-powered)
- **Business/Consumer** (4): {不具合|ふぐあい} (defect/malfunction), {年会費|ねんかいひ} (annual fee), {有効期限|ゆうこうきげん} (expiration date), {契約書|けいやくしょ} (contract)
- **Modern Japanese** (2): テンション (mood/energy level), {保活|ほかつ} (daycare hunting)
- **Cooking verb** (1): {泡立|あわだ}てる (to whip/froth)

Notable entry features:
- Cryptocurrency and blockchain terminology with related terms and Japanese legal terminology ({暗号資産|あんごうしさん})
- QRコード noting its Japanese origin (Denso Wave, 1994)
- Modern work vocabulary (ノマド, コワーキング) reflecting post-pandemic work trends
- Environmental terms for Japan's 2050 carbon neutrality goals
- テンション as {和製英語|わせいえいご} (different meaning from English "tension")
- {保活|ほかつ} as part of ～{活|かつ} word pattern ({就活|しゅうかつ}, {婚活|こんかつ}, etc.)
- {泡立|あわだ}てる with transitivity pair and cooking terminology

Total entries: 6,473 → 6,493
Remaining candidates: 772 → 752

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 87)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Photography** (1): シャッター (shutter)
- **Humble expression** (1): {拝借|はいしゃく} (borrowing humble)
- **Compound verbs** (5): {押|お}し{流|なが}す (to wash away), {踏|ふ}み{倒|たお}す (to default on), {食|く}い{止|と}める (to hold back), {嵌|は}め{込|こ}む (to fit into), {飛|と}び{移|うつ}る (to jump across)
- **～{的|てき} adjectives** (3): {挑発的|ちょうはつてき} (provocative), {排他的|はいたてき} (exclusive), {壊滅的|かいめつてき} (devastating)
- **Four-character idioms** (5): {抱腹絶倒|ほうふくぜっとう} (hilarious), {傍若無人|ぼうじゃくぶじん} (arrogant), {意気投合|いきとうごう} (hit it off), {厚顔無恥|こうがんむち} (shameless), {朝令暮改|ちょうれいぼかい} (inconsistent)
- **Modern business loanwords** (5): クラウドファンディング (crowdfunding), ブレインストーミング (brainstorming), シェアハウス (share house), マインドセット (mindset), ワークショップ (workshop)

Notable entry features:
- Compound verbs with ～{流|なが}す (wash away), ～{倒|たお}す (knock down/default), ～{止|と}める (stop), ～{込|こ}む (into), ～{移|うつ}る (transfer) patterns
- Four-character idioms covering emotions ({抱腹絶倒|ほうふくぜっとう}, {意気投合|いきとうごう}) and character traits ({傍若無人|ぼうじゃくぶじん}, {厚顔無恥|こうがんむち})
- Modern business loanwords used in Japanese corporate culture
- Humble expression {拝借|はいしゃく} with {拝|はい} prefix for formal contexts
- {排他的|はいたてき}{経済|けいざい}{水域|すいいき} (EEZ) terminology

Total entries: 6,453 → 6,473
Remaining candidates: 792 → 772

### 2026-01-17 (Vocabulary Expansion - 20 New Entries, Session 86)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Astronomy/space** (2): {軌道|きどう} (orbit/trajectory), {天体|てんたい} (celestial body)
- **Photography** (2): {現像|げんぞう} (photo developing), ピント (focus)
- **Textiles** (2): {編|あ}み{物|もの} (knitting), ミシン (sewing machine)
- **Geology** (2): {地層|ちそう} (stratum), {断層|だんそう} (fault)
- **Publishing** (1): {印税|いんぜい} (royalty)
- **Eye care** (2): {老眼|ろうがん} (presbyopia), {乱視|らんし} (astigmatism)
- **Compound verbs** (2): {追|お}い{込|こ}む (to corner), {引|ひ}き{伸|の}ばす (to stretch)
- **～{的|てき} adjectives** (2): {威圧的|いあつてき} (intimidating), {革命的|かくめいてき} (revolutionary)
- **Four-character idioms** (4): {大器晩成|たいきばんせい} (great talents mature late), {疑心暗鬼|ぎしんあんき} (suspicion breeds monsters), {一目瞭然|いちもくりょうぜん} (obvious at a glance), {波乱万丈|はらんばんじょう} (eventful/turbulent)
- **Modern business loanword** (1): コンプライアンス (compliance)

Notable entry features:
- Science vocabulary covering astronomy ({軌道|きどう}, {天体|てんたい}) and geology ({地層|ちそう}, {断層|だんそう})
- Photography terminology from film era ({現像|げんぞう}, ピント) with modern digital context
- Textile crafts vocabulary ({編|あ}み{物|もの}↔ミシン)
- Eye care conditions with medical terminology
- Compound verbs with ～{込|こ}む (into) and ～{伸|の}ばす (extend) patterns
- Four-character idioms with etymology and cultural context
- Modern business Japanese (コンプライアンス) with corporate culture notes

Total entries: 6,433 → 6,453
Remaining candidates: 812 → 792

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 85)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Japanese proverbs** (3): {早起|はやお}きは{三文|さんもん}の{徳|とく} (the early bird catches the worm), {百聞|ひゃくぶん}は{一見|いっけん}に{如|し}かず (seeing is believing), {急|いそ}がば{回|まわ}れ (more haste, less speed)
- **Four-character idioms** (4): {心機一転|しんきいってん} (turning over a new leaf), {絶体絶命|ぜったいぜつめい} (desperate situation), {創意工夫|そういくふう} (originality and ingenuity), {取捨選択|しゅしゃせんたく} (careful selection)
- **Compound verbs** (7): {吹|ふ}き{出|だ}す (to burst out laughing/gush), {泣|な}き{出|だ}す (to burst into tears), {盛|も}り{上|あ}がる (to get excited), {飛|と}び{上|あ}がる (to jump up), {出直|でなお}す (to start over), {追|お}い{払|はら}う (to chase away), {見分|みわ}ける (to distinguish)
- **～{的|てき} adjectives** (4): {公的|こうてき} (public/official), {私的|してき} (private/personal), {内的|ないてき} (internal/inner), {外的|がいてき} (external/outer)
- **Adverbs** (4): いよいよ (finally/more and more), きっぱり (decisively), どうせ (anyway/after all), さすがに (as expected)
- **Slang verbs** (2): ムカつく (to be pissed off), ググる (to google)
- **Weather noun** (1): {竜巻|たつまき} (tornado)

Notable entry features:
- Classic Japanese proverbs with origins, English equivalents, and usage notes
- Four-character idioms with etymology and contextual examples
- Compound verbs with ～{出|だ}す (sudden action) and ～{上|あ}がる (completion/rising) patterns
- ～{的|てき} adjective antonym pairs ({公的|こうてき}↔{私的|してき}, {内的|ないてき}↔{外的|がいてき})
- Modern internet slang (ググる) and youth slang (ムカつく) with register notes
- Adverbs with nuanced emotional/situational meanings

Total entries: 6,408 → 6,433
Remaining candidates: 837 → 812

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 84)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Astronomy/space** (4): {流星|りゅうせい} (meteor), {日食|にっしょく} (solar eclipse), {月食|げっしょく} (lunar eclipse), {星座|せいざ} (constellation)
- **Tools/hardware** (2): ペンチ (pliers), {脚立|きゃたつ} (stepladder)
- **Postal/mail** (2): {差出人|さしだしにん} (sender), {消印|けしいん} (postmark)
- **Grooming/hair** (3): {散髪|さんぱつ} (haircut), {美容院|びよういん} (beauty salon), {理髪店|りはつてん} (barbershop)
- **Games/playground** (6): {鬼|おに}ごっこ (tag), かくれんぼ (hide-and-seek), {縄跳|なわと}び (jump rope), ぶらんこ (swing), {滑|すべ}り{台|だい} (slide), {砂場|すなば} (sandbox)
- **Gardening** (3): {剪定|せんてい} (pruning), {水|みず}やり (watering), {植木鉢|うえきばち} (flower pot)
- **Vehicle parts** (3): タイヤ (tire), ハンドル (steering wheel), アクセル (accelerator)
- **～{的|てき} adjectives** (2): {肯定的|こうていてき} (affirmative), {否定的|ひていてき} (negative)

Notable entry features:
- Astronomy vocabulary with eclipse types ({皆既日食|かいきにっしょく}, {部分日食|ぶぶんにっしょく})
- Complete playground equipment vocabulary with cross-references
- Grooming/hair vocabulary contrasting {美容院|びよういん}↔{理髪店|りはつてん}
- Vehicle parts for driving contexts with safety notes
- ～{的|てき} adjective antonym pair ({肯定的|こうていてき}↔{否定的|ひていてき})

Total entries: 6,383 → 6,408
Remaining candidates: 862 → 837

### 2026-01-17 (New Candidates - 101 Words Added, Session 83)
Added 101 new candidate words to `candidate_words.json` using balanced coverage strategy:

**Novel categories NOT mentioned in prompt/skill (~51 words):**
- **Astronomy/space** (6): {流星|りゅうせい} (meteor), {日食|にっしょく} (solar eclipse), {月食|げっしょく} (lunar eclipse), {星座|せいざ} (constellation), {軌道|きどう} (orbit), {天体|てんたい} (celestial body)
- **Tools/hardware** (2): ペンチ (pliers), {脚立|きゃたつ} (stepladder)
- **Postal/mail** (2): {差出人|さしだしにん} (sender), {消印|けしいん} (postmark)
- **Grooming/hair** (3): {散髪|さんぱつ} (haircut), {美容院|びよういん} (beauty salon), {理髪店|りはつてん} (barbershop)
- **Photography** (3): {現像|げんぞう} (developing), ピント (focus), シャッター (shutter)
- **Games/playground** (6): {鬼|おに}ごっこ (tag), かくれんぼ (hide-and-seek), {縄跳|なわと}び (jump rope), ぶらんこ (swing), {滑|すべ}り{台|だい} (slide), {砂場|すなば} (sandbox)
- **Textiles** (2): {編|あ}み{物|もの} (knitting), ミシン (sewing machine)
- **Gardening** (4): {剪定|せんてい} (pruning), {水|みず}やり (watering), {植木鉢|うえきばち} (flower pot), {種|たね}まき (sowing)
- **Geology** (2): {地層|ちそう} (stratum), {断層|だんそう} (fault)
- **Publishing** (1): {印税|いんぜい} (royalty)
- **Eyecare** (3): {乱視|らんし} (astigmatism), {遠視|えんし} (farsightedness), {老眼|ろうがん} (presbyopia)
- **Furniture** (2): {食器棚|しょっきだな} (dish cabinet), マットレス (mattress)
- **Marine** (1): {海藻|かいそう} (seaweed)
- **Vehicle parts** (4): タイヤ (tire), ハンドル (steering wheel), バンパー (bumper), アクセル (accelerator)
- **Religious items** (3): {数珠|じゅず} (prayer beads), {仏壇|ぶつだん} (Buddhist altar), {位牌|いはい} (memorial tablet)
- **Traditional items** (1): {熨斗|のし} (gift ornament)
- **Architecture** (2): {敷居|しきい} (threshold), {鴨居|かもい} (lintel)
- **Household items** (5): {柱時計|はしらどけい} (pendulum clock), {湯|ゆ}たんぽ (hot water bottle), {蚊取|かと}り{線香|せんこう} (mosquito coil), {物干|ものほ}し{竿|ざお} (laundry pole), {洗濯|せんたく}ばさみ (clothespin)

**Standard categories mentioned in prompt/skill (~50 words):**
- **Compound verbs** (4): {追|お}い{込|こ}む (to corner), {引|ひ}き{伸|の}ばす (to stretch), {飛|と}び{移|うつ}る (to jump to), ちょこちょこ (in small steps)
- **～{的|てき} adjectives** (8): {威圧的|いあつてき} (intimidating), {革命的|かくめいてき} (revolutionary), {挑発的|ちょうはつてき} (provocative), {排他的|はいたてき} (exclusive), {否定的|ひていてき} (negative), {肯定的|こうていてき} (affirmative), {壊滅的|かいめつてき} (devastating), {支離滅裂|しりめつれつ} (incoherent)
- **Four-character idioms** (18): {大器晩成|たいきばんせい} (great talents mature late), {抱腹絶倒|ほうふくぜっとう} (hilarious), {傍若無人|ぼうじゃくぶじん} (arrogant), {粉骨砕身|ふんこつさいしん} (working hard), {疑心暗鬼|ぎしんあんき} (suspicion), {意気投合|いきとうごう} (hit it off), {一喜一憂|いっきいちゆう} (swinging between hope and fear), {厚顔無恥|こうがんむち} (shameless), {朝令暮改|ちょうれいぼかい} (inconsistent), {一目瞭然|いちもくりょうぜん} (obvious at a glance), {公明正大|こうめいせいだい} (fair and square), {前途多難|ぜんとたなん} (grim future), {満身創痍|まんしんそうい} (covered in wounds), {付和雷同|ふわらいどう} (following blindly), {栄枯盛衰|えいこせいすい} (ups and downs), {明鏡止水|めいきょうしすい} (serene mind), {波乱万丈|はらんばんじょう} (eventful)
- **Modern business/tech loanwords** (20): クラウドファンディング, ブレインストーミング, シェアハウス, マインドセット, ワークショップ, ファシリテーター, キャリアアップ, ライフスタイル, ウェルビーイング, ダイバーシティ, インクルーシブ, ワークライフバランス, デジタルネイティブ, レガシー, ローンチ, ピボット, スケール, コンプライアンス, ガバナンス, ステークホルダー

Candidate count: 761 → 862

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 82)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Modern slang/expressions** (5): ワンチャン (maybe/possibly), エモ (emotional), {界隈|かいわい} (community/scene), {古参|こさん} (longtime fan), {新規|しんき} (new fan)
- **Japanese proverbs** (4): {能|のう}ある{鷹|たか}は{爪|つめ}を{隠|かく}す (still waters run deep), {情|なさ}けは{人|ひと}の{為|ため}ならず (kindness comes back to you), {馬|うま}の{耳|みみ}に{念仏|ねんぶつ} (preaching to deaf ears), {虻|あぶ}{蜂|はち}{取|と}らず (grasp all, lose all)
- **Traditional Japanese items** (3): {紋付|もんつき} (formal kimono), {番傘|ばんがさ} (traditional umbrella), {香炉|こうろ} (incense burner)
- **Medical terms** (5): {発熱|はつねつ} (fever), {筋肉痛|きんにくつう} (muscle pain), {動悸|どうき} (palpitation), {息切|いきぎ}れ (shortness of breath), {痙攣|けいれん} (spasm)
- **Business/financial terms** (4): {収益|しゅうえき} (earnings), {抵当|ていとう} (mortgage), {手形|てがた} (promissory note), {小切手|こぎって} (check)
- **Social/cultural** (3): {空気|くうき}を{読|よ}む (read the room), {仲直|なかなお}りする (to reconcile), {省|しょう}エネ (energy saving)
- **Other** (1): ネタ (material/topic)

Notable entry features:
- Modern youth slang for online communities (ワンチャン, エモ, {界隈|かいわい}, {古参|こさん}↔{新規|しんき})
- Classic Japanese proverbs with cultural explanations and English equivalents
- Traditional Japanese items for formal occasions and ceremonies
- Medical terminology for common symptoms
- Business/financial vocabulary for formal contexts
- Cultural expression {空気|くうき}を{読|よ}む central to Japanese social dynamics

Total entries: 6,358 → 6,383
Remaining candidates: 786 → 761

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 81)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **～{的|てき} adjectives** (6): {本能的|ほんのうてき} (instinctive), {刺激的|しげきてき} (stimulating), {意欲的|いよくてき} (ambitious), {献身的|けんしんてき} (devoted), {象徴的|しょうちょうてき} (symbolic), {恒久的|こうきゅうてき} (permanent)
- **Compound verbs** (5): {蹴|け}り{倒|たお}す (to kick down), {突|つ}き{詰|つ}める (to investigate thoroughly), {切|き}り{詰|つ}める (to economize), {這|は}い{上|あ}がる (to crawl up), {塗|ぬ}り{替|か}える (to repaint)
- **Onomatopoeia/adverbs** (7): ちょろちょろ (trickling), がやがや (noisy chatter), ひそひそ (whispering), もじもじ (fidgeting), ほんのり (slightly), ほっこり (heartwarming), ちゃっかり (shrewdly)
- **Four-character idioms** (2): {軽挙妄動|けいきょもうどう} (rash action), {温厚篤実|おんこうとくじつ} (gentle and sincere)
- **Humble expressions** (2): {拝読|はいどく} (reading humble), {拝聴|はいちょう} (listening humble)
- **Conjunctions** (2): とはいえ (although), とはいうものの (having said that)
- **Modern casual** (1): てか (or rather)

Notable entry features:
- ～{的|てき} adjectives with antonym pairs ({恒久的|こうきゅうてき}↔{暫定的|ざんていてき}, {意欲的|いよくてき}↔{消極的|しょうきょくてき})
- Compound verbs with ～{倒|たお}す (knock down), ～{詰|つ}める (exhaustive), ～{上|あ}がる (upward) patterns
- Onomatopoeia covering sounds (がやがや, ひそひそ), emotions (もじもじ, ほっこり), and textures (ちょろちょろ)
- Humble expressions with {拝|はい} prefix for formal business/academic contexts
- Modern youth slang (てか) alongside formal conjunctions

Total entries: 6,333 → 6,358
Remaining candidates: 811 → 786

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
