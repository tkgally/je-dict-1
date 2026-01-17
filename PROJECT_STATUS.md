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
- **Total entries**: 6,283
- **Vocabulary tier assignment**: Pending (all entries have vocabulary_tier: null)
- **Candidate words**: ~756 words tracked in `candidate_words.json`
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

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 74)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **{駆|か}け～ compound verbs** (5): {駆|か}け{上|あ}がる (to run up), {駆|か}け{下|お}りる (to run down), {駆|か}け{込|こ}む (to rush in), {駆|か}け{回|まわ}る (to run around), {駆|か}け{抜|ぬ}ける (to run through)
- **Four-character idioms** (5): {青天霹靂|せいてんへきれき} (bolt from the blue), {画竜点睛|がりょうてんせい} (finishing touch), {四面楚歌|しめんそか} (surrounded by enemies), {馬耳東風|ばじとうふう} (in one ear and out the other), {竜頭蛇尾|りゅうとうだび} (anticlimax)
- **Traditional Japanese culture** (5): {座布団|ざぶとん} (floor cushion), {火鉢|ひばち} (charcoal brazier), {掛|か}け{軸|じく} (hanging scroll), {手拭|てぬぐ}い (tenugui towel), {硯|すずり} (inkstone)
- **Gift-giving/ceremony** (3): お{中元|ちゅうげん} (mid-year gift), お{歳暮|せいぼ} (year-end gift), {香典|こうでん} (funeral offering)
- **Business/consumer terms** (4): {送料|そうりょう} (shipping fee), {解約|かいやく} (cancellation), {返金|へんきん} (refund), {問|と}い{合|あ}わせ (inquiry)
- **～{的|てき} adjectives** (3): {自発的|じはつてき} (spontaneous), {強制的|きょうせいてき} (compulsory), {破壊的|はかいてき} (destructive)

Notable entry features:
- Complete {駆|か}け～ compound verb series with running/rushing movement patterns
- Classical four-character idioms with historical/cultural origins
- Traditional Japanese items used in tea ceremony and calligraphy
- Japanese gift-giving customs with cultural etiquette notes
- Antonym pairs ({自発的|じはつてき}↔{強制的|きょうせいてき})

Total entries: 6,183 → 6,208
Remaining candidates: 853 → 828

### 2026-01-17 (Vocabulary Expansion - 25 New Entries, Session 73)
Added 25 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Compound verbs** (5): {送|おく}り{出|だ}す (to send off), {流|なが}れ{出|だ}す (to flow out), {呼|よ}び{込|こ}む (to call in), {突|つ}き{刺|さ}す (to stab), {踏|ふ}みつける (to trample)
- **～{的|てき} adjectives** (5): {楽観的|らっかんてき} (optimistic), {悲観的|ひかんてき} (pessimistic), {建設的|けんせつてき} (constructive), {直接的|ちょくせつてき} (direct), {間接的|かんせつてき} (indirect)
- **Modern loanwords** (5): リモートワーク (remote work), キャッシュレス (cashless), ドローン (drone), バグ (bug), プログラミング (programming)
- **Food/agriculture terms** (5): {玄米|げんまい} (brown rice), {白米|はくまい} (white rice), {肥料|ひりょう} (fertilizer), {牧場|ぼくじょう} (ranch), {酪農|らくのう} (dairy farming)
- **Fish/legal terms** (5): {鰻|うなぎ} (eel), {鰹|かつお} (bonito), {遵守|じゅんしゅ} (compliance), {認定|にんてい} (certification), カロリー (calorie)

Notable entry features:
- Compound verbs with ～{出|だ}す (outward) and ～{込|こ}む (inward) patterns
- ～{的|てき} adjective antonym pairs ({楽観的|らっかんてき}↔{悲観的|ひかんてき}, {直接的|ちょくせつてき}↔{間接的|かんせつてき})
- Modern technology vocabulary (リモートワーク, キャッシュレス, プログラミング)
- Japanese food culture ({鰻|うなぎ} with {土用|どよう}の{丑|うし}の{日|ひ} tradition, {鰹|かつお} with regional cuisine notes)
- Agriculture vocabulary relevant for discussing Japanese food production

Total entries: 6,158 → 6,183
Remaining candidates: 878 → 853

### 2026-01-17 (Vocabulary Expansion - 50 New Entries, Session 72)
Added 50 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Basic verbs** (3): ためらう (to hesitate), {戸惑|とまど}う (to be confused), {怯|おび}える (to be frightened)
- **Compound verbs** (17): {締|し}め{出|だ}す (to lock out), {売|う}り{出|だ}す (to launch), {抜|ぬ}け{出|だ}す (to slip out), {逃|に}げ{出|だ}す (to run away), {浮|う}き{上|あ}がる (to float up), {舞|ま}い{上|あ}がる (to soar), {抱|だ}き{締|し}める (to embrace), {引|ひ}きずる (to drag), {引|ひ}き{寄|よ}せる (to draw near), {押|お}し{倒|たお}す (to push down), {張|は}り{付|つ}く (to stick to), {絞|しぼ}り{込|こ}む (to narrow down), {取|と}り{返|かえ}す (to take back), {振|ふ}り{回|まわ}す (to swing around), {叩|たた}き{込|こ}む (to hammer in), {見過|みす}ごす (to overlook), {切|き}り{抜|ぬ}く (to cut out)
- **Suru verbs** (13): {感謝|かんしゃ}する (to be grateful), {同意|どうい}する (to agree), {提案|ていあん}する (to propose), {議論|ぎろん}する (to discuss), {理解|りかい}する (to understand), {想像|そうぞう}する (to imagine), {考慮|こうりょ}する (to consider), {判断|はんだん}する (to judge), {否定|ひてい}する (to deny), {予想|よそう}する (to predict), {期待|きたい}する (to expect), {心配|しんぱい}する (to worry), {安心|あんしん}する (to feel relieved)
- **Na-adjectives** (5): {滑|なめ}らか (smooth), {脆|もろ}い (fragile), {華|はな}やか (gorgeous), {素朴|そぼく} (simple), {野暮|やぼ} (unsophisticated)
- **Adverbs** (2): わざわざ (deliberately), あえて (dare to)
- **Housing/rental terms** (5): {敷金|しききん} (security deposit), {礼金|れいきん} (key money), {賃貸|ちんたい} (rental), {間取|まど}り (floor plan), {冷凍食品|れいとうしょくひん} (frozen food)
- **Food terms** (2): {賞味期限|しょうみきげん} (best-before date), {消費期限|しょうひきげん} (use-by date)
- **Profession terms** (3): {建築家|けんちくか} (architect), {会計士|かいけいし} (accountant), サラリーマン (salaryman)

Notable entry features:
- Comprehensive compound verb coverage with ～出す (escape/start) patterns, ～上がる (upward) patterns, and ～込む (into) patterns
- Essential suru verbs for communication and reasoning ({理解|りかい}する, {議論|ぎろん}する, {考慮|こうりょ}する)
- Japanese rental system vocabulary ({敷金|しききん}/{礼金|れいきん}) with cultural notes
- Food expiration terms with explanation of legal distinctions
- Cross-references linking related terms ({敷金|しききん}↔{礼金|れいきん}, {賞味期限|しょうみきげん}↔{消費期限|しょうひきげん})

Total entries: 6,108 → 6,158
Remaining candidates: 928 → 878

### 2026-01-17 (New Candidates - 59 Words Added, Session 71)
Added 59 new candidate words to `candidate_words.json` using balanced coverage strategy:

- **Compound verbs** (28): Transportation verbs ({切|き}り{出|だ}す, {打|う}ち{出|だ}す, {突|つ}き{出|だ}す, {取|と}り{付|つ}ける), emotional/action verbs ({引|ひ}き{取|と}る, {引|ひ}き{起|お}こす, {引|ひ}き{止|と}める, {引|ひ}き{付|つ}ける), launching verbs ({打|う}ち{上|あ}げる, {打|う}ち{切|き}る, {打|う}ち{消|け}す), movement verbs ({押|お}し{切|き}る, {押|お}し{進|すす}める, {押|お}し{寄|よ}せる, {受|う}け{継|つ}ぐ), courtesy ({差|さ}し{入|い}れる, {差|さ}し{掛|か}かる, {差|さ}し{引|ひ}く), persistence ({持|も}ちかける, {持|も}ち{堪|こた}える, {振|ふ}り{切|き}る), jumping ({飛|と}び{付|つ}く, {飛|と}び{降|お}りる), running ({駆|か}け{上|あ}がる, {駆|か}け{下|お}りる, {駆|か}け{込|こ}む, {駆|か}け{回|まわ}る, {駆|か}け{抜|ぬ}ける)
- **Fashion/music/food loanwords** (9): コーデ, トレンド, アイテム, フェス, サビ, アレンジ, カバー, テイクアウト, デリバリー
- **Modern lifestyle terms** (7): ワンオペ, モラハラ, イクメン, ママ{友|とも}, リスク, メリット, デメリット, トラブル
- **IT/tech loanwords** (4): スワイプ, スクロール, プライバシー, メールアドレス
- **Transportation** (3): {遅延|ちえん}, {運休|うんきゅう}, {発着|はっちゃく}
- **Cooking** (2): {下味|したあじ}, {灰汁抜|あくぬ}き
- **Housing** (2): {不動産|ふどうさん}, {居住|きょじゅう}
- **Four-character idioms** (2): {一触即発|いっしょくそくはつ}, {危機一髪|ききいっぱつ}
- **～的 adjective** (1): {総合的|そうごうてき}
- **Other** (1): モチベーション

Candidate count: 869 → 928

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
