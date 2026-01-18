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
- **Total entries**: 6,781
- **Vocabulary tier assignment**: Basic: 1,113 | Core: 4,840 | General: 475 | Unassigned: 337
- **Candidate words**: ~833 words tracked in `candidate_words.json`
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

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 105)
Added 30 new dictionary entries from candidate_words.json, covering adjectives, verbs, adverbs, onomatopoeia, and everyday vocabulary:

- **I-adjectives** (5): {細長|ほそなが}い (long and thin), {平|ひら}たい (flat), {瑞々|みずみず}しい (fresh/juicy), {図太|ずぶと}い (thick-skinned), {甲斐甲斐|かいがい}しい (devoted)
- **Na-adjectives** (2): {生真面目|きまじめ} (overly serious), {愚|おろ}か (foolish)
- **Verbs** (4): {焦|こ}がす (to burn/scorch), {笑|わら}い{出|だ}す (to start laughing), {走|はし}り{出|だ}す (to start running), {履|は}き{替|か}える (to change shoes)
- **Onomatopoeia/Adverbs** (7): こってり (rich/heavy), じわじわ (gradually), ぽつぽつ (bit by bit), そこそこ (so-so), {到底|とうてい} (not possibly), {否応|いやおう}なく (inevitably), なんだかんだ (one way or another)
- **Nouns - Memory/Attitude** (3): {物覚|ものおぼ}え (memory ability), {気配|きくば}り (attentiveness), {心掛|こころが}け (mindset)
- **Nouns - Exams** (3): {期末試験|きまつしけん} (final exam), {中間試験|ちゅうかんしけん} (midterm exam), {追試験|ついしけん} (makeup exam)
- **Nouns - Modern life** (6): {退去|たいきょ} (moving out), {電子|でんし}マネー (electronic money), {小川|おがわ} (stream), トレンド (trend), フェス (music festival), ドリンクバー (drink bar)

Notable entry features:
- Compound adjectives: {細長|ほそなが}い from {細|ほそ}い + {長|なが}い, {生真面目|きまじめ} with intensifying {生|き} prefix
- Compound verbs with ～{出|だ}す pattern for "beginning to" ({笑|わら}い{出|だ}す, {走|はし}り{出|だ}す)
- Transitivity pair: {焦|こ}がす (trans.) ↔ {焦|こ}げる (intrans.)
- Japanese school exam terminology set with cross-references
- {和製英語|わせいえいご} entries: ドリンクバー (self-service drinks), フェス (festival)
- Onomatopoeia for texture/gradual change: こってり↔あっさり antonym pair, じわじわ for slow persistent change

Total entries: 6,721 → 6,751
Remaining candidates: 891 → 861

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

### 2026-01-18 (New Candidates - 117 Words Added, Session 102)
Added 117 new candidate words to `candidate_words.json` with balanced coverage across interpersonal and social vocabulary:

**Personality & Character Traits** (~15 words):
- {気軽|きがる} (casual), {軽率|けいそつ} (rash), {大雑把|おおざっぱ} (rough), {几帳面|きちょうめん} (methodical), {窮屈|きゅうくつ} (cramped)
- {無愛想|ぶあいそう} (curt), {愛想|あいそう} (amiability), {愛嬌|あいきょう} (charm)
- {不可欠|ふかけつ} (indispensable), {不可解|ふかかい} (mysterious), {不可思議|ふかしぎ} (inexplicable), {不用意|ふようい} (careless)

**Communication & Speech** (~20 words):
- Verbal habits: {口癖|くちぐせ} (verbal habit), {愚痴|ぐち} (complaint), {陰口|かげぐち} (gossip)
- Social concepts: {本音|ほんね} (true feelings), {建前|たてまえ} (public stance), {人見知り|ひとみしり} (shy with strangers)
- Types of talk: {世間話|せけんばなし} (small talk), {雑談|ざつだん} (chitchat), {井戸端会議|いどばたかいぎ} (gossip session), {独り言|ひとりごと} (monologue)
- Speech types: {寝言|ねごと} (sleep-talking), たわ{言|ごと} (nonsense), {繰|く}り{言|ごと} (repetitive complaints), {憎|にく}まれ{口|ぐち} (sarcasm), {減|へ}らず{口|ぐち} (backtalk)
- Flattery: お{世辞|せじ} (flattery), {追従|ついしょう} (sycophancy), おべっか (brown-nosing), {嫌味|いやみ} (snide remark)

**Emotions & Psychology** (~15 words):
- {甘|あま}える (depend on), {甘|あま}やかす (spoil), {見栄|みえ} (vanity), {虚栄心|きょえいしん} (conceit)
- {自己嫌悪|じこけんお} (self-loathing), {自己満足|じこまんぞく} (self-satisfaction), {物足|ものた}りない (unsatisfying), {歯|は}がゆい (frustrating)
- {強|つよ}がり (bravado), {負|ま}け{惜|お}しみ (sour grapes), {勝|か}ち{気|き} (competitive), {負|ま}けず{嫌|ぎら}い (hate to lose)

**Consideration & Care** (~10 words):
- お{節介|せっかい} (meddlesome), {心配|こころくば}り (thoughtfulness), {目配|めくば}り (watchfulness)
- {気遣|きづか}い (concern), {心遣|こころづか}い (consideration), {心得|こころえ} (knowledge), {心構|こころがま}え (mental preparedness)

**Sensory & Physical Experience** (~20 words):
- ～{応|ごた}え pattern: {手応|てごた}え (response), {歯応|はごた}え (chewiness), {読|よ}み{応|ごた}え (worth reading), {見応|みごた}え (worth seeing), {聞|き}き{応|ごた}え (worth listening)
- ～{心地|ごこち} pattern: {居心地|いごこち} (comfort), {寝心地|ねごこち} (sleeping comfort), {乗|の}り{心地|ごこち} (ride comfort), {着心地|きごこち} (wearing comfort), {使|つか}い{心地|ごこち} (ease of use)
- Textures: {触感|しょっかん} (tactile feel), {食感|しょくかん} (mouthfeel), {肌触|はだざわ}り (skin texture)
- Health: {凝|こ}り (stiffness), {痺|しび}れ (numbness), むくみ (swelling), かゆみ (itchiness), {持病|じびょう} (chronic illness)

**Work & Social Status** (~20 words):
- Ability: {段取|だんど}り (preparation), {采配|さいはい} (leadership), {裁量|さいりょう} (discretion), {腕前|うでまえ} (skill), {手腕|しゅわん} (capability), {敏腕|びんわん} (capable), {凄腕|すごうで} (highly skilled)
- Hierarchy: {幹部|かんぶ} (executive), {中堅|ちゅうけん} (mid-level), {格上|かくうえ} (superior), {格下|かくした} (inferior), {年上|としうえ} (older), {年下|としした} (younger)
- Status: {新米|しんまい} (newcomer), {古株|ふるかぶ} (veteran), {新顔|しんがお} (new face), {常連|じょうれん} (regular), {一見|いちげん} (first-timer)

**Relationships & Fate** (~15 words):
- People: {馴染|なじ}み (acquaintance), {顔馴染|かおなじ}み (familiar face), {赤|あか}の{他人|たにん} (complete stranger), {見|み}ず{知|し}らず (total stranger), {初対面|しょたいめん} (first meeting)
- Destiny: {因縁|いんねん} (karma), {運命|うんめい} (destiny), {宿命|しゅくめい} (fate), {天命|てんめい} (divine will), {定|さだ}め (destiny)
- Other: {巡|めぐ}り{合|あ}わせ (chance), {別|わか}れ{際|ぎわ} (moment of parting), {名残|なごり} (traces), {面影|おもかげ} (vestiges)

**Idioms & Expressions** (~5 words):
- {日常茶飯事|にちじょうさはんじ} (everyday occurrence), {紆余曲折|うよきょくせつ} (twists and turns), {大同小異|だいどうしょうい} (essentially the same)
- {二枚目|にまいめ} (handsome man), {三枚目|さんまいめ} (comedian), {一枚上手|いちまいうわて} (a cut above)

Notable features:
- Productive patterns: ～{応|ごた}え (worth doing X), ～{心地|ごこち} (comfort of X)
- Japanese cultural concepts: {本音|ほんね}/{建前|たてまえ}, {人見知り|ひとみしり}, {甘|あま}え
- Social hierarchy vocabulary reflecting Japanese workplace and relationships
- Interpersonal speech vocabulary for natural conversation

Candidate count: 820 → 937

### 2026-01-18 (New Candidates - 122 Words Added, Session 101)
Added 122 new candidate words to `candidate_words.json` with balanced coverage across specialized areas:

**Specialized Hobbies** (~24 words):
- Crafts/arts: {盆栽|ぼんさい} (bonsai), {水彩画|すいさいが} (watercolor), {油絵|あぶらえ} (oil painting), {型紙|かたがみ} (pattern), コスプレ (cosplay)
- Outdoor activities: {釣り竿|つりざお} (fishing rod), {寝袋|ねぶくろ} (sleeping bag), {焚き火|たきび} (campfire), {登山靴|とざんぐつ} (hiking boots)
- Photography: {一眼|いちがん}レフ (SLR camera), {三脚|さんきゃく} (tripod), {露出|ろしゅつ} (exposure)
- Games/collecting: {麻雀|マージャン} (mahjong), {双六|すごろく} (sugoroku), {骨董品|こっとうひん} (antique), コレクション (collection)
- Astronomy/gardening: {天体観測|てんたいかんそく} (stargazing), {家庭菜園|かていさいえん} (home garden), バードウォッチング
- Modern hobbies: {模型|もけい} (model), プラモデル (plastic model), ラジコン (RC), {同人誌|どうじんし} (doujinshi), オタク, フィギュア
- Entertainment: パチンコ, スロット, クラフトビール, {利き酒|ききざけ} (sake tasting), ゲーセン (arcade)

**Music Terminology** (~30 words):
- Notation: {楽譜|がくふ} (sheet music), {音符|おんぷ} (musical note), {休符|きゅうふ} (rest), {音色|ねいろ} (timbre)
- Performance: {独奏|どくそう} (solo), {即興|そっきょう} (improvisation), {吹奏楽|すいそうがく} (wind band), リハーサル (rehearsal)
- Orchestral instruments: チェロ, コントラバス, クラリネット, トランペット, トロンボーン, サックス
- Equipment: {指揮棒|しきぼう} (baton), シンセサイザー (synthesizer), アンプ (amplifier), {弓|ゆみ} (bow), ピック (pick)
- Categories: {打楽器|だがっき} (percussion), {管楽器|かんがっき} (wind), {弦楽器|げんがっき} (string)
- Genres: ロック, ジャズ, ヒップホップ, {民謡|みんよう} (folk song), {演歌|えんか} (enka)
- Production: レコーディング, ミキシング, {調律|ちょうりつ} (tuning), {転調|てんちょう} (modulation)

**Regional Dialect Vocabulary** (~28 words):
- General: {方言|ほうげん} (dialect), {訛|なま}り (accent), {標準語|ひょうじゅんご} (standard language)
- Kansai: おおきに (thank you), あかん (no good), ほんま (really), なんでやねん, しんどい, せや, わや, うっとこ
- Kyoto: おいでやす (welcome), おおけに (thank you)
- Nagoya: でら (very)
- Hiroshima: じゃけん (therefore)
- Kyushu/Hakata: ばってん (but), よか (good), ちかっぱ (very)
- Hokkaido: なまら (very), したっけ (bye/well then)
- Tohoku: いずい (uncomfortable), おばんです (good evening), だべ (right?)
- Edo: べらぼう (ridiculously)
- Shizuoka: ズラ, だら (sentence-enders)
- Dialect forms: どないやねん, ええやん, さぶい

**Compound Verbs** (~28 words):
- ～込む: {踏み込|ふみこ}む (step into), {割り込|わりこ}む (cut in), {溶け込|とけこ}む (blend in), {組み込|くみこ}む (incorporate), {吸い込|すいこ}む (inhale)
- ～出す/取る: {聞き出|ききだ}す (get info), {呼び戻|よびもど}す (call back)
- ～上げる/下げる: {書き上|かきあ}げる (finish writing), {切り上|きりあ}げる (finish up), {切り下|きりさ}げる (lower), {繰り上|くりあ}げる (move up), {繰り下|くりさ}げる (postpone)
- ～渡る/広げる: {行き渡|いきわた}る (spread throughout), {繰り広|くりひろ}げる (unfold)
- ～切る/向かう: {言い切|いいき}る (say definitively), {立ち向|たちむ}かう (confront)
- ～起こる/返す: {巻き起|まきお}こる (arise), {巻き返|まきかえ}す (comeback)
- ～浮かべる/伸べる: {思い浮|おもいう}かべる (imagine), {差し伸|さしの}べる (extend)
- ～落とす/進む: {突き落|つきお}とす (push down), {突き進|つきすす}む (push forward), {突き当|つきあ}たる (run into)
- ～戻す/抜く: {差し戻|さしもど}す (send back), {見抜|みぬ}く (see through)
- ～渡す/上がる: {言い渡|いいわた}す (hand down), {沸き上|わきあ}がる (well up), {湧き出|わきで}る (gush out)

Notable features:
- Specialized hobbies covering traditional Japanese arts (盆栽) and modern otaku culture (同人誌, フィギュア)
- Complete music terminology set from notation to production
- Regional dialects spanning all major Japanese dialect regions
- Compound verbs systematically organized by auxiliary verb patterns

Candidate count: 698 → 820

### 2026-01-18 (New Candidates - 101 Words Added, Session 100)
Added 101 new candidate words to `candidate_words.json` with balanced coverage across diverse categories:

**Professions & Occupations** (8):
- {薬剤師|やくざいし} (pharmacist), {獣医|じゅうい} (veterinarian), {司書|ししょ} (librarian), {配管工|はいかんこう} (plumber), {電気技師|でんきぎし} (electrician), {彫刻家|ちょうこくか} (sculptor), {映画監督|えいがかんとく} (film director), {探偵|たんてい} (detective)

**Household & Daily Life** (26):
- Tools/kitchen: {栓抜|せんぬ}き (bottle opener), {缶切|かんき}り (can opener), おろし{金|がね} (grater), {蛍光|けいこう}ペン (highlighter), {軍手|ぐんて} (work gloves), {巻尺|まきじゃく} (tape measure)
- Household items: {電源|でんげん}タップ (power strip), {延長|えんちょう}コード (extension cord), {柔軟剤|じゅうなんざい} (fabric softener), {漂白剤|ひょうはくざい} (bleach), {消臭剤|しょうしゅうざい} (deodorizer), {殺虫剤|さっちゅうざい} (insecticide), {芳香剤|ほうこうざい} (air freshener), {接着剤|せっちゃくざい} (adhesive), {潤滑油|じゅんかつゆ} (lubricant)
- Laundry: {洗濯籠|せんたくかご} (laundry basket), ゴミ{箱|ばこ} (trash can), {靴棚|くつだな} (shoe rack), {傘立|かさた}て (umbrella stand), {鍵掛|かぎか}け (key hook)
- Bedding: {掛|か}け{布団|ぶとん} (comforter), {敷布団|しきぶとん} (mattress futon)
- Tech: {携帯充電器|けいたいじゅうでんき} (phone charger), モバイルバッテリー (portable battery), ワイヤレス{充電|じゅうでん} (wireless charging), {液晶画面|えきしょうがめん} (LCD screen)

**Building & Architecture** (9):
- {天窓|てんまど} (skylight), {網戸|あみど} (screen door), {出窓|でまど} (bay window), {吹|ふ}き{抜|ぬ}け (atrium), {物干|ものほ}し (drying rack), {排水溝|はいすいこう} (drain)

**Environment & Energy** (7):
- {節電|せつでん} (power saving), {再生可能|さいせいかのう}エネルギー (renewable energy), {太陽光発電|たいようこうはつでん} (solar power), {風力発電|ふうりょくはつでん} (wind power), {断熱材|だんねつざい} (insulation), {気密性|きみつせい} (airtightness), カビ (mold)

**Taste Vocabulary** (4):
- {酸味|さんみ} (sourness), {甘味|あまみ} (sweetness), {塩気|しおけ} (saltiness), {旨味|うまみ} (umami), {渋|しぶ}み (astringency)

**Medical & Health** (7):
- {鬱血|うっけつ} (congestion), {脱臼|だっきゅう} (dislocation), {貧血|ひんけつ} (anemia), {不整脈|ふせいみゃく} (arrhythmia), {低血圧|ていけつあつ} (low blood pressure), {食中毒|しょくちゅうどく} (food poisoning)

**Action Verbs** (6):
- よろめく (to stagger), つまずく (to stumble), {撫|な}で{下|お}ろす (to smooth down), {突|つ}っ{込|こ}む (to thrust), {飛|と}び{跳|は}ねる (to hop), {引|ひ}っ{掻|か}く (to scratch)

**Public Facilities & Travel** (22):
- Facilities: {観客席|かんきゃくせき} (spectator seating), {控|ひか}え{室|しつ} (waiting room), {更衣室|こういしつ} (changing room), {喫煙所|きつえんじょ} (smoking area), {授乳室|じゅにゅうしつ} (nursing room), {多目的|たもくてき}トイレ (accessible restroom), {指定席|していせき} (reserved seat), {自由席|じゆうせき} (unreserved seat), {喫茶室|きっさしつ} (tea lounge), {休憩所|きゅうけいじょ} (rest area), {集合場所|しゅうごうばしょ} (meeting place)
- Safety: {非常口|ひじょうぐち} (emergency exit), {避難経路|ひなんけいろ} (evacuation route), {防犯|ぼうはん}カメラ (security camera)
- Fees: {入場料|にゅうじょうりょう} (admission fee), {入館料|にゅうかんりょう} (museum fee), {拝観料|はいかんりょう} (temple fee), {駐車料金|ちゅうしゃりょうきん} (parking fee), {宿泊料|しゅくはくりょう} (accommodation fee)

**Accommodation & Business** (12):
- {送迎|そうげい} (shuttle service), {朝食付|ちょうしょくつ}き (with breakfast), {素泊|すどま}り (room only), {連泊|れんぱく} (consecutive stay), {予約制|よやくせい} (by reservation), {先着順|せんちゃくじゅん} (first-come-first-served), {抽選|ちゅうせん} (lottery), {当選|とうせん} (winning), {落選|らくせん} (losing), {繰|く}り{上|あ}げ (moving up schedule), {繰|く}り{下|さ}げ (pushing back), {日程調整|にっていちょうせい} (scheduling)

**Work & Leave** (5):
- {遅刻届|ちこくとどけ} (late notice), {欠席届|けっせきとどけ} (absence notice), {有給休暇|ゆうきゅうきゅうか} (paid vacation), {育児休暇|いくじきゅうか} (parental leave), {産休|さんきゅう} (maternity leave)

Notable features:
- Practical daily life vocabulary covering household items, cleaning supplies, and modern technology
- Comprehensive public facility vocabulary useful for travelers
- Complete accommodation/booking vocabulary set
- Work-related leave terminology reflecting Japanese corporate culture
- Taste vocabulary completing the five basic tastes (umami as the fifth taste, discovered in Japan)
- Environment/sustainability terms reflecting Japan's carbon neutrality goals

Candidate count: 597 → 698

### 2026-01-18 (Vocabulary Expansion - 20 New Entries, Session 99)
Added 20 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- **Technology/Computing** (4): {深層|しんそう}{学習|がくしゅう} (deep learning), {検索|けんさく}エンジン (search engine), USBメモリ (USB flash drive), ハードディスク (hard disk)
- **Communication/Remote work** (3): オンライン{会議|かいぎ} (online meeting), ビデオ{通話|つうわ} (video call), ワーホリ (working holiday)
- **Sports** (1): {陸上|りくじょう}{競技|きょうぎ} (track and field)
- **Food** (1): {加工|かこう}{食品|しょくひん} (processed food)
- **Compound concepts** (4): {出入|でい}り (going in and out), {開閉|かいへい} (opening and closing), {表裏|おもてうら} (front and back), {八方|はっぽう} (all directions)
- **Legal** (1): {六法|ろっぽう} (the Six Codes)
- **Emotions** (1): {恥辱|ちじょく} (disgrace)
- **Agriculture** (3): {精米|せいまい} (rice polishing), {脱穀|だっこく} (threshing), {耕作|こうさく} (cultivation)
- **Construction** (1): {施工|せこう} (construction work)
- **Nature** (1): {熱帯林|ねったいりん} (tropical forest)

Notable entry features:
- AI/computing vocabulary ({深層|しんそう}{学習|がくしゅう}, {検索|けんさく}エンジン) for modern technology discussions
- Remote work terminology (オンライン{会議|かいぎ}, ビデオ{通話|つうわ}) reflecting post-pandemic work culture
- Rice production vocabulary ({精米|せいまい}, {脱穀|だっこく}, {耕作|こうさく}) with agricultural process context
- Compound words pairing opposites ({出入|でい}り, {開閉|かいへい}, {表裏|おもてうら})
- Japanese legal terminology ({六法|ろっぽう}) with the six fundamental codes explained

Total entries: 6,651 → 6,671
Remaining candidates: 683 → 663

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
