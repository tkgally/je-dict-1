# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-01-17
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
- **Total entries**: 6,473
- **Vocabulary tier assignment**: Basic: 1,112 | Core: 4,713 | General: 423 | Unassigned: 225
- **Candidate words**: ~772 words tracked in `candidate_words.json`
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

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 80)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Compound verbs** (5): {積|つ}み{重|かさ}ねる (to pile up), {食|く}い{込|こ}む (to bite into), {踏|ふ}み{切|き}る (to take the plunge), {掻|か}き{集|あつ}める (to scrape together), {振|ふ}り{払|はら}う (to shake off)
- **～{的|てき} adjectives** (5): {効率的|こうりつてき} (efficient), {衝動的|しょうどうてき} (impulsive), {独創的|どくそうてき} (original), {攻撃的|こうげきてき} (aggressive), {開放的|かいほうてき} (open)
- **Four-character idioms** (4): {千差万別|せんさばんべつ} (great variety), {単刀直入|たんとうちょくにゅう} (straight to the point), {日進月歩|にっしんげっぽ} (rapid progress), {誠心誠意|せいしんせいい} (in all sincerity)
- **Emotional nouns** (3): {違和感|いわかん} (sense of discomfort), {一体感|いったいかん} (sense of unity), {臨場感|りんじょうかん} (sense of presence)
- **Adverbs** (3): じっくり (slowly and carefully), つくづく (deeply), ふわっと (softly)
- **Adjectives** (4): たくましい (sturdy), おおらか (broad-minded), にこやか (smiling), あざとい (cunning)
- **Modern term** (1): ゲーマー (gamer)

Notable entry features:
- Compound verbs with ～{込|こ}む (into), ～{切|き}る (decisively), ～{払|はら}う (away) patterns
- ～{的|てき} adjectives with antonym pairs ({攻撃的|こうげきてき}↔{防御的|ぼうぎょてき}, {開放的|かいほうてき}↔{閉鎖的|へいさてき})
- Four-character idioms with etymological context
- Emotional ～{感|かん} compound nouns for expressing nuanced feelings
- Modern youth/gaming vocabulary (あざとい's semantic shift, ゲーマー)

Total entries: 6,308 → 6,333
Remaining candidates: 836 → 811

### 2026-01-17 (New Candidates - 104 Words Added, Session 79)
Added 104 new candidate words to `candidate_words.json` using balanced coverage strategy:

- **Compound verbs** (16): {振|ふ}り{払|はら}う (to shake off), {蹴|け}り{倒|たお}す (to kick down), {突|つ}き{詰|つ}める (to investigate thoroughly), {押|お}し{流|なが}す (to wash away), {切|き}り{詰|つ}める (to economize), {掻|か}き{集|あつ}める (to scrape together), {叩|たた}き{落|お}とす (to knock down), {踏|ふ}み{切|き}る (to take the plunge), {踏|ふ}み{倒|たお}す (to default on), {食|く}い{込|こ}む (to bite into), {食|く}い{止|と}める (to hold back), {這|は}い{上|あ}がる (to crawl up), {這|は}い{出|で}る (to crawl out), {嵌|は}め{込|こ}む (to fit in), {塗|ぬ}り{替|か}える (to repaint), {積|つ}み{重|かさ}ねる (to pile up)
- **～{的|てき} adjectives** (14): {効率的|こうりつてき} (efficient), {衝動的|しょうどうてき} (impulsive), {本能的|ほんのうてき} (instinctive), {刺激的|しげきてき} (stimulating), {意欲的|いよくてき} (ambitious), {献身的|けんしんてき} (devoted), {独創的|どくそうてき} (original), {攻撃的|こうげきてき} (aggressive), {防御的|ぼうぎょてき} (defensive), {開放的|かいほうてき} (open), {閉鎖的|へいさてき} (exclusive), {象徴的|しょうちょうてき} (symbolic), {包括的|ほうかつてき} (comprehensive), {暫定的|ざんていてき} (provisional)
- **Four-character idioms** (7): {誠心誠意|せいしんせいい} (in all sincerity), {軽挙妄動|けいきょもうどう} (rash action), {温厚篤実|おんこうとくじつ} (gentle and sincere), {千差万別|せんさばんべつ} (great diversity), {単刀直入|たんとうちょくにゅう} (straight to the point), {日進月歩|にっしんげっぽ} (rapid progress), {恒久的|こうきゅうてき} (permanent)
- **Humble/formal expressions** (7): {拝借|はいしゃく} (borrowing humble), {拝読|はいどく} (reading humble), {拝聴|はいちょう} (listening humble), お{越|こ}し (coming honorific), とはいえ (although), とはいうものの (having said that), てか (or rather casual)
- **Emotional/psychological** (7): {切|せつ}なさ (heartache), {懐|なつか}しさ (nostalgia), {物足|ものた}りなさ (dissatisfaction), {違和感|いわかん} (discomfort), {疎外感|そがいかん} (alienation), {一体感|いったいかん} (unity), {臨場感|りんじょうかん} (sense of presence)
- **Onomatopoeia/adverbs** (32): ちょろちょろ (trickling), がやがや (noisy chatter), ひそひそ (whispering), ぶくぶく (bubbling), くねくね (winding), ふわっと (softly), かりかり (crispy), どっと (all at once), ひょっと (possibly), ひょいと (quickly), ひょこひょこ (bobbing), もじもじ (fidgeting), おいおい (bawling), きりきり (sharp pain), くらくら (dizzy), ほんのり (slightly), ほっこり (heartwarming), ちゃっかり (shrewdly), しれっと (nonchalantly), けろっと (casually), しゅんと (dejected), あくまで (to the end), おのずと (naturally), ひいては (by extension), ともあれ (anyway), つくづく (deeply), しみじみ (keenly), まんまと (successfully), じっくり (thoroughly), むずむず (itching), うずうず (restless), おずおず (timidly)
- **Adjectives** (13): にこやか (smiling), あどけない (innocent), いじらしい (touching), いたわしい (pitiful), うやうやしい (respectful), おぼつかない (uncertain), けたたましい (piercing), しおらしい (demure), たくましい (sturdy), ふてぶてしい (brazen), おおらか (broad-minded), あざとい (cunning), えげつない (nasty)
- **Modern terms** (8): ドヤ{顔|がお} (smug face), リミックス (remix), ゲーマー (gamer), スクショ (screenshot), スパム (spam), {水加減|みずかげん} (water level), {切|き}り{崩|くず}す (to encroach on), せわしない (restless)

Candidate count: 732 → 836

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 78)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Compound verbs** (3): すり{下|お}ろす (to grate), {誘|さそ}い{込|こ}む (to lure into), {殴|なぐ}り{倒|たお}す (to knock down)
- **Japanese proverbs** (4): {花|はな}より{団子|だんご} (substance over style), {豚|ぶた}に{真珠|しんじゅ} (pearls before swine), {猫|ねこ}の{手|て}も{借|か}りたい (desperately busy), {良薬|りょうやく}{口|くち}に{苦|にが}し (good medicine tastes bitter)
- **Four-character idioms** (5): {針小棒大|しんしょうぼうだい} (making a mountain out of a molehill), {晴耕雨読|せいこううどく} (farm when sunny, read when rainy), {呉越同舟|ごえつどうしゅう} (enemies in same boat), {我田引水|がでんいんすい} (self-serving), {二律背反|にりつはいはん} (antinomy)
- **Construction terms** (3): {耐震|たいしん} (earthquake-resistant), {解体|かいたい} (demolition), {改築|かいちく} (renovation)
- **Japanese customs** (3): {祝儀|しゅうぎ} (congratulatory money), {喪中|もちゅう} (mourning period), {年賀状|ねんがじょう} (New Year's card)
- **Traditional Japanese items** (2): {屏風|びょうぶ} (folding screen), ちゃぶ{台|だい} (low dining table)
- **Food terms** (3): {具材|ぐざい} (ingredients), {汁物|しるもの} (soup dish), {生鮮食品|せいせんしょくひん} (fresh produce)
- **Other** (2): {骨格|こっかく} (skeleton/framework), コンテンツ (content)

Notable entry features:
- Classic Japanese proverbs with origins and English equivalents
- Four-character idioms ({四字熟語|よじじゅくご}) with historical context
- Construction vocabulary related to Japan's earthquake preparedness
- Japanese gift-giving customs ({祝儀|しゅうぎ}↔{不祝儀|ぶしゅうぎ})
- New Year traditions with cultural etiquette ({年賀状|ねんがじょう}, {喪中|もちゅう})
- Traditional home items from Showa era (ちゃぶ{台|だい})

Total entries: 6,283 → 6,308
Remaining candidates: 756 → 732

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 77)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Japanese proverbs** (3): {石|いし}の{上|うえ}にも{三年|さんねん} (perseverance pays off), {塵|ちり}も{積|つ}もれば{山|やま}となる (many a little makes a mickle), {棚|たな}から{牡丹餅|ぼたもち} (unexpected good fortune)
- **～{的|てき} adjectives** (3): {物理的|ぶつりてき} (physical), {肉体的|にくたいてき} (bodily), {合理的|ごうりてき} (rational)
- **Transportation terms** (5): {搭乗|とうじょう} (boarding aircraft), {乗車|じょうしゃ} (boarding train), {優先席|ゆうせんせき} (priority seat), {車内|しゃない} (inside train), {車掌|しゃしょう} (conductor)
- **Weather/nature terms** (3): {雷鳴|らいめい} (thunder), {日照|ひで}り (drought), {太陽光|たいようこう} (solar energy)
- **Traditional Japanese items** (3): お{札|ふだ} (paper charm), {乾物|かんぶつ} (dried food), {朱肉|しゅにく} (red ink pad)
- **Food/nutrition** (2): {栄養素|えいようそ} (nutrient), {炭水化物|たんすいかぶつ} (carbohydrate)
- **Book structure** (2): {序文|じょぶん} (preface), {付録|ふろく} (appendix)
- **Cultural** (2): {七五三|しちごさん} (Shichi-Go-San festival), ずぶ{濡|ぬ}れ (soaking wet)
- **Verbs** (2): {捏|こ}ねる (to knead), {引|ひ}き{下|さ}げる (to lower)

Notable entry features:
- Three classic Japanese proverbs with English equivalents and usage notes
- ～{的|てき} adjectives with contrast pairs ({物理的|ぶつりてき}↔{肉体的|にくたいてき})
- Complete transportation vocabulary set with cross-references ({搭乗|とうじょう}↔{乗車|じょうしゃ})
- Cultural items for shrine visits and traditional practices
- Nutrition terminology with {三大|さんだい}{栄養素|えいようそ} (three major nutrients) context

Total entries: 6,258 → 6,283
Remaining candidates: 780 → 756

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 76)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Compound verbs** (7): {持|も}ち{出|だ}す (to take out, to bring up), {取|と}り{外|はず}す (to remove), {取|と}り{扱|あつか}う (to handle), {取|と}り{締|し}まる (to regulate), {引|ひ}き{取|と}る (to take back), {引|ひ}き{起|お}こす (to cause), {引|ひ}き{止|と}める (to hold back)
- **Emotional adjectives** (4): {切|せつ}ない (bittersweet), {煩|わずら}わしい (troublesome), {鬱陶|うっとう}しい (gloomy/annoying), {愛|いと}しい (beloved)
- **～{的|てき} adjectives** (6): {実質的|じっしつてき} (substantial), {比較的|ひかくてき} (relatively), {定期的|ていきてき} (regular), {段階的|だんかいてき} (gradual), {総合的|そうごうてき} (comprehensive), {保守的|ほしゅてき} (conservative)
- **Onomatopoeia/adverbs** (3): ぐんぐん (steadily), じゃんじゃん (one after another), ばんばん (vigorously)
- **Modern loanwords** (5): テイクアウト (takeout), デリバリー (delivery), スワイプ (swipe), スクロール (scroll), モチベーション (motivation)

Notable entry features:
- {取|と}り～ and {引|ひ}き～ compound verb patterns with business/everyday usage
- Emotional i-adjectives expressing complex feelings ({切|せつ}ない for bittersweet longing)
- ～{的|てき} adjectives for formal/academic contexts ({比較的|ひかくてき} as adverb)
- Tech/smartphone vocabulary (スワイプ, スクロール) reflecting modern usage
- Food delivery terms (テイクアウト↔デリバリー) with COVID-era context

Total entries: 6,233 → 6,258
Remaining candidates: 803 → 780

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 75)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Compound verbs** (5): {突|つ}き{飛|と}ばす (to shove away), {投|な}げ{捨|す}てる (to throw away), {蹴|け}り{飛|と}ばす (to kick away), {染|し}み{出|だ}す (to ooze out), {溢|あふ}れ{出|だ}す (to overflow)
- **Japanese proverbs** (5): {猿|さる}も{木|き}から{落|お}ちる (even monkeys fall from trees), {七転|ななころ}び{八起|やお}き (fall seven times, get up eight), {灯台|とうだい}{下|もと}{暗|くら}し (darkest under the lamppost), {鬼|おに}に{金棒|かなぼう} (making strong stronger), {井|い}の{中|なか}の{蛙|かわず} (frog in a well)
- **Four-character idioms** (5): {言語道断|ごんごどうだん} (outrageous), {天変地異|てんぺんちい} (natural disaster), {自暴自棄|じぼうじき} (self-destructive despair), {有言実行|ゆうげんじっこう} (practice what you preach), {森羅万象|しんらばんしょう} (all things in the universe)
- **Modern/tech terms** (5): コーディング (coding), デバッグ (debugging), フリーランス (freelance), スタートアップ (startup), サステナブル (sustainable)
- **Work-related terms** (5): {出社|しゅっしゃ} (going to work), {退社|たいしゃ} (leaving work), {辞職|じしょく} (resignation), {在宅勤務|ざいたくきんむ} (work from home), {配属|はいぞく} (assignment)

Notable entry features:
- Compound verbs with ～{飛|と}ばす (send flying) and ～{出|だ}す (come out) patterns
- Classic Japanese proverbs with cultural explanations and English equivalents
- Four-character idioms with etymology and usage contexts
- Modern tech/work vocabulary reflecting contemporary Japanese usage
- Cross-references linking related terms ({出社|しゅっしゃ}↔{退社|たいしゃ})

Total entries: 6,208 → 6,233
Remaining candidates: 828 → 803

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
