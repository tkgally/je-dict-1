# Japanese-English Learner's Dictionary - Project Status Archive

This file contains the historical change log entries that have been moved from PROJECT_STATUS.md.
For current status, see [PROJECT_STATUS.md](PROJECT_STATUS.md).

---

## Archived Recent Changes

### 2026-01-18 (Katakana Reading Cleanup, Session 116)
Fixed inconsistency where some entries had katakana readings instead of hiragana, causing duplicate entries.

**Changes:**
- **Deleted 52 duplicate entries** where both katakana and hiragana reading versions existed (kept hiragana versions)
- **Converted 1 entry reading** to hiragana: 06805_diiemu (DM: ディーエム → でぃーえむ)
- **Fixed 93 candidate readings** in candidate_words.json
- **Removed 7 duplicate candidates** after hiragana normalization
- **Removed 51 candidates** that now exist in dictionary (index sync)

**Updated documentation and validation:**
- Added katakana reading validation to `validate.py` (now errors on katakana readings)
- Updated `entry-guidelines` skill with explicit "Reading Format" section
- Updated `find-candidates` skill with hiragana reading requirement
- Updated `manage_candidates.py` to auto-convert katakana readings to hiragana with warning
- Created `fix_katakana_readings.py` script for future cleanup needs

**Rationale:** Katakana readings like "スキー" vs hiragana "すきー" created duplicate entries for the same word. All readings are now normalized to hiragana (even for loanwords) to ensure consistent indexing, deduplication, and lookup. The long vowel mark ー is preserved since there's no hiragana equivalent.

Total entries: 7,021 → 6,969 (52 duplicates removed)
Remaining candidates: ~709 → ~651 (51 synced + 7 duplicates removed)

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 115)
Added 30 new dictionary entries from candidate_words.json, covering grammar patterns, four-character idioms, modern vocabulary, and everyday terms:

- **Grammar patterns** (5): に{関|かん}して (regarding), に{際|さい}して (on the occasion of), をもって (with/by means of), さもないと (otherwise), そうすると (in that case)
- **Casual expressions** (3): つーか (or rather - very casual), {知|し}らんけど (I dunno though - Kansai hedge), ぴえん (sad - internet slang)
- **Four-character idioms (yojijukugo)** (4): {一触即発|いっしょくそくはつ} (explosive situation), {全身全霊|ぜんしんぜんれい} (with all one's heart), {危機一髪|ききいっぱつ} (close call), {多事多難|たじたなん} (full of troubles)
- **Modern loanwords** (5): ストレージ (storage), デバイス (device), アジェンダ (agenda), クレジットカード (credit card), コメント (comment)
- **Music/Entertainment vocabulary** (3): {奏者|そうしゃ} (instrumentalist), {不協和音|ふきょうわおん} (dissonance), {自己|じこ}ベスト (personal best)
- **Everyday vocabulary** (6): バイト (part-time job), いける (to be doable), {湿疹|しっしん} (eczema), {分数|ぶんすう} (fraction), {残|のこ}らず (without exception), {一直線|いっちょくせん} (straight line/beeline)
- **Social/Family vocabulary** (2): ママ{友|とも} (mom friend), {就学|しゅうがく} (school attendance)
- **Formal expressions** (2): ご{容赦|ようしゃ} (pardon), {切符|きっぷ}{売|う}り{場|ば} (ticket booth)

Notable entry features:
- Formal grammar pattern coverage: に{関|かん}して vs について (formality contrast)
- Internet/youth slang: ぴえん with emoji context (🥺), {知|し}らんけど spreading from Kansai
- Comprehensive yojijukugo: {一触即発|いっしょくそくはつ} ↔ {危機一髪|ききいっぱつ} (cross-referenced)
- Tech vocabulary: ストレージ, デバイス for digital literacy
- Hybrid terms: {自己|じこ}ベスト (Japanese + English compound)

Total entries: 6,991 → 7,021
Remaining candidates: ~738 → ~709

### 2026-01-18 (Vocabulary Expansion - 30 New Entries, Session 114)
Added 30 new dictionary entries from candidate_words.json, focusing on conversational particles, formal conjunctions, adverbs, and onomatopoeia:

- **Conversational fillers/interjections** (8): えーと (um, let me see), あのー (um, excuse me), ほら (look, see), ねえ (hey, right?), よね (right?), やっぱ (as expected), ぜ (masculine emphasis), ぞ (emphasis particle)
- **Grammar/Quotative expressions** (4): なんて (such as, what a), っていう (called, that says), ていうか (or rather), かしら (I wonder - feminine)
- **Formal conjunctions** (6): {及|およ}び (and - formal), {並|なら}びに (and - very formal), {若|も}しくは (or - formal), {故|ゆえ}に (therefore), しかしながら (however), それなのに (even so)
- **Adverbs** (4): どのみち (anyway), {差|さ}し{当|あ}たり (for the time being), {今|いま}しがた (just now), ひいては (by extension)
- **Onomatopoeia** (4): おずおず (timidly), けろっと (nonchalantly), しゅんと (dejected), ぶくぶく (bubbling/getting fat)
- **Adjectives/Nouns** (4): うやうやしい (respectful), {敷居|しきい} (threshold), {疎外感|そがいかん} (alienation), ドヤ{顔|がお} (smug face)

Notable entry features:
- Comprehensive conversational particle coverage for natural Japanese speech
- Formal conjunction hierarchy: {及|およ}び (same level) vs {並|なら}びに (larger groups); {若|も}しくは (same level) vs または (larger groups)
- Register contrast: やっぱ (casual) vs やっぱり (neutral) vs やはり (formal)
- Gender-specific particles: かしら (feminine), ぜ/ぞ (masculine)
- Internet/modern vocabulary: ドヤ{顔|がお} (from Kansai dialect どや)
- Emotional onomatopoeia contrast pair: けろっと (unaffected) ↔ しゅんと (dejected)

Total entries: 6,961 → 6,991
Remaining candidates: ~767 → ~738

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

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 60)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Verbs (15): {映|ば}える (to look good), {手放|てばな}す (to let go), {垂|た}らす (to drip), {怒鳴|どな}る (to shout), {呟|つぶや}く (to mutter), {膨|ふく}らむ (to swell), {萎|しぼ}む (to wilt), {焦|こ}げる (to burn), {喚|わめ}く (to scream), {咎|とが}める (to blame), {寝|ね}ぼける (to be drowsy), {抓|つね}る (to pinch), しゃぶる (to suck), {欠伸|あくび}する (to yawn), くしゃみする (to sneeze)
- Onomatopoeia (25): くるくる (spinning), ばたばた (flapping), きゅっと (tightly), ぎゅっと (squeezing), ぱっと (suddenly), さっと (quickly), はっと (startled), ぎらぎら (glaring), てかてか (shiny), もこもこ (fluffy), ぼこぼこ (bumpy), すらすら (smoothly), ぶつぶつ (grumbling), ぴんぴん (lively), びしょびしょ (soaked), ふらふら (unsteady), よろよろ (tottering), おろおろ (flustered), いそいそ (eagerly), おどおど (timidly), ちくちく (prickly), しくしく (sobbing), ひやひや (anxious), めらめら (blazing), ぺたぺた (sticking)
- School terms (5): {部活|ぶかつ} (club activities), {生徒会|せいとかい} (student council), {職員室|しょくいんしつ} (staff room), {保健室|ほけんしつ} (nurse's office), {図書室|としょしつ} (library room)
- Health (5): {下痢|げり} (diarrhea), {便秘|べんぴ} (constipation), インフルエンザ (influenza), {包帯|ほうたい} (bandage), {絆創膏|ばんそうこう} (adhesive bandage)
- Nature (6): {紅葉|もみじ} (maple/autumn leaves), {葉|は}っぱ (leaf), {磯|いそ} (rocky shore), {珊瑚|さんご} (coral), {崖|がけ} (cliff), あられ (hail)
- Technology (8): ユーザー (user), フォルダ (folder), タップ (tap), サブスク (subscription), テレワーク (telework), ワイファイ (WiFi), {生配信|なまはいしん} (live streaming), エコ (eco)
- Media controls (3): {一時停止|いちじていし} (pause), {早送|はやおく}り (fast forward), {巻|ま}き{戻|もど}し (rewind)
- Emotions (4): {悲|かな}しみ (sadness), {恐|おそ}れ (fear), {嫉妬|しっと} (jealousy), {葛藤|かっとう} (conflict)
- Arts/crafts (4): {折|お}り{紙|がみ} (origami), {生|い}け{花|ばな} (ikebana), {舞踊|ぶよう} (dance), {刺繍|ししゅう} (embroidery)
- Political terms (4): {民主主義|みんしゅしゅぎ} (democracy), {資本主義|しほんしゅぎ} (capitalism), {社会主義|しゃかいしゅぎ} (socialism), {人権|じんけん} (human rights)
- Finance (6): {口座|こうざ} (bank account), {預金|よきん} (deposit), {振込|ふりこみ} (transfer), {残高|ざんだか} (balance), {手数料|てすうりょう} (handling fee), {値引|ねび}き (discount)
- Games (2): パズル (puzzle), オセロ (Othello)
- Live performance (1): ライブ (live concert)
- Misc (3): {真夜中|まよなか} (midnight), {染|し}み (stain), {麦|むぎ} (wheat/barley)
- Animal sounds (2): わんわん (bow-wow), にゃんにゃん (meow)
- Expressions (3): まあまあ (so-so), みたいな (like), じゃん (isn't it)
- Clothing (4): Tシャツ (T-shirt), ジャンパー (jacket), キャップ (cap), スニーカー (sneakers)

Notable entry features:
- Comprehensive onomatopoeia covering movement, texture, emotions, and states
- Japanese school-specific vocabulary (部活, 生徒会, etc.)
- Cross-references added linking antonyms (下痢↔便秘, 早送り↔巻き戻し)
- Political vocabulary useful for news and academic contexts
- Finance terms essential for daily life in Japan

Total entries: 5,407 → 5,507
Remaining candidates: 1,354 → 1,247

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 59)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (20): さらさら (smooth/rustling), ぺらぺら (fluent), とろとろ (thick/gooey), ねばねば (sticky), ぱりぱり (crispy), もちもち (chewy), がんがん (pounding), ずきずき (throbbing), ひりひり (stinging), じんじん (tingling), むかむか (nauseous), びくびく (nervous), そわそわ (restless), はらはら (anxious), ぼーっと (spaced out), うとうと (drowsy), うっとり (enchanted), ぞっと (shuddering), へとへと (exhausted), がたがた (rattling)
- Technology (7): クリック (click), ログイン (login), パスワード (password), オンライン (online), ネット (internet), ファイル (file), タブレット (tablet)
- Household items (10): エアコン (air conditioner), ヒーター (heater), リモコン (remote), ケトル (kettle), ポット (pot), {爪切|つめき}り (nail clippers), しゃもじ (rice paddle), ぬいぐるみ (stuffed toy), {印鑑|いんかん} (seal), レシート (receipt)
- Body parts (3): {眉毛|まゆげ} (eyebrow), こめかみ (temple), {手|て}のひら (palm)
- Transportation (5): バス{停|てい} (bus stop), {終電|しゅうでん} (last train), {車両|しゃりょう} (vehicle/train car), {乗車券|じょうしゃけん} (ticket), {運賃|うんちん} (fare)
- Rooms (2): {寝室|しんしつ} (bedroom), {浴室|よくしつ} (bathroom)
- Verbs (3): {憧|あこが}れる (to admire), {叶|かな}う (to come true), {励|はげ}ます (to encourage)
- Expressions (8): じゃあね (see ya), またね (see you later), だるい (sluggish), {面倒臭|めんどくさ}い (bothersome), なんか (like/somehow), ぶっちゃけ (to be honest), ぼちぼち (so-so), ほどほど (moderation)
- Abstract nouns (12): {難民|なんみん} (refugee), {移民|いみん} (immigrant), {世論|せろん} (public opinion), {真実|しんじつ} (truth), {意欲|いよく} (motivation), {体力|たいりょく} (stamina), {自覚|じかく} (self-awareness), {協定|きょうてい} (agreement), {同盟|どうめい} (alliance), {研修|けんしゅう} (training), {練習|れんしゅう} (practice), {古代|こだい} (ancient times)
- Measurements/Math (18): {産業|さんぎょう} (industry), {資源|しげん} (resources), {強力|きょうりょく} (powerful), {探査|たんさ} (exploration), {哲学|てつがく} (philosophy), {心理|しんり} (psychology), {楽|たの}しむ (to enjoy), {苦|くる}しむ (to suffer), {長|なが}さ (length), {高|たか}さ (height), {深|ふか}さ (depth), {厚|あつ}さ (thickness), {広|ひろ}さ (width), {面積|めんせき} (area), {体積|たいせき} (volume), {距離|きょり} (distance), {速度|そくど} (speed), {割合|わりあい} (ratio)
- Academic subjects (12): {平均|へいきん} (average), {合計|ごうけい} (total), {足|た}し{算|ざん} (addition), {引|ひ}き{算|ざん} (subtraction), {掛|か}け{算|ざん} (multiplication), {割|わ}り{算|ざん} (division), {数学|すうがく} (mathematics), {科学|かがく} (science), {化学|かがく} (chemistry), {物理|ぶつり} (physics), {生物|せいぶつ} (biology), {歴史|れきし} (history)

Notable entry features:
- Comprehensive onomatopoeia for textures, sensations, and emotional states
- Complete set of basic math operations (四則演算)
- Academic subjects useful for educational contexts
- Measurement vocabulary with related adjective notes
- Cross-references added linking homophones ({科学|かがく}↔{化学|かがく})

Total entries: 5,307 → 5,407
Remaining candidates: 1,441 → 1,354

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 58)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Onomatopoeia (26): ぴかぴか (sparkling), ふわふわ (fluffy), どきどき (heart pounding), わくわく (excited), きらきら (glittering), ぐるぐる (spinning), ぺこぺこ (hungry/bowing), のろのろ (slowly), すべすべ (smooth), ぼろぼろ (worn out), ばらばら (scattered), ぎりぎり (barely), ぶらぶら (wandering), うろうろ (loitering), くたくた (exhausted), ぐちゃぐちゃ (messy), べたべた (sticky), からから (parched), ぬるぬる (slimy), ざらざら (rough), つるつる (slippery), ごろごろ (rumbling), にこにこ (smiling), めちゃくちゃ (absurd), ぐっと (firmly), すっきり (refreshed)
- Food/Noodles (3): ラーメン (ramen), うどん (udon), チョコレート (chocolate)
- Vegetables (13): じゃがいも (potato), {人参|にんじん} (carrot), {大根|だいこん} (daikon), キャベツ (cabbage), {法蓮草|ほうれんそう} (spinach), {葱|ねぎ} (green onion), にんにく (garlic), {生姜|しょうが} (ginger), トマト (tomato), レタス (lettuce), メロン (melon), {胡瓜|きゅうり} (cucumber), {玉葱|たまねぎ} (onion)
- Animals (8): ライオン (lion), かもめ (seagull), カブトムシ (beetle), {蝉|せみ} (cicada), アヒル (duck), {鶏|にわとり} (chicken), {山羊|やぎ} (goat), {蜻蛉|とんぼ} (dragonfly)
- Daily expressions (5): おはよう (good morning), おやすみ (good night), どういたしまして (you're welcome), {お疲|おつか}れ{様|さま} (thank you for your work), とりあえず (for now)
- Adverbs (2): ちなみに (by the way), そもそも (in the first place)
- Abstract concepts (8): {忍耐|にんたい} (patience), {好奇心|こうきしん} (curiosity), {創造性|そうぞうせい} (creativity), {矛盾|むじゅん} (contradiction), {調和|ちょうわ} (harmony), {均衡|きんこう} (equilibrium), {中断|ちゅうだん} (interruption), {再開|さいかい} (resumption)
- Technology/Media (15): ブランド (brand), マーケティング (marketing), ウイルス (virus), {貼|は}り{付|つ}け (paste), {画素|がそ} (pixel), タッチパネル (touchscreen), {取材|しゅざい} (news gathering), {広報|こうほう} (PR), {吹|ふ}き{替|か}え (dubbing), スキャナー (scanner), テレビ{電話|でんわ} (video call), ドキュメンタリー (documentary), アダプター (adapter), ビッグデータ (big data), {和英|わえい} (Japanese-English)
- Music/Arts (5): {和歌|わか} (waka poetry), {和楽器|わがっき} (Japanese instruments), {独唱|どくしょう} (solo), {作詞|さくし} (lyrics writing), {編曲|へんきょく} (arrangement)
- Sports/Exercise (7): ボクシング (boxing), レスリング (wrestling), サーフィン (surfing), ダイビング (diving), ストレッチ (stretching), ウォーキング (walking)
- Science/Politics (8): {与党|よとう} (ruling party), {過疎化|かそか} (depopulation), {染色体|せんしょくたい} (chromosome), {小惑星|しょうわくせい} (asteroid), {成層圏|せいそうけん} (stratosphere), オゾン{層|そう} (ozone layer), {脈|みゃく} (pulse), {塵紙|ちりがみ} (tissue paper)

Notable entry features:
- Comprehensive onomatopoeia coverage for common sensory descriptions
- Vegetable vocabulary useful for cooking and shopping contexts
- Science vocabulary includes space and environmental terms
- Cross-references added linking antonym pairs ({中断|ちゅうだん}↔{再開|さいかい})

Total entries: 5,207 → 5,307
Remaining candidates: 1,548 → 1,441

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 57)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Occupations (15): {看護師|かんごし} (nurse), {警察官|けいさつかん} (police officer), {消防士|しょうぼうし} (firefighter), {銀行員|ぎんこういん} (bank employee), エンジニア (engineer), プログラマー (programmer), デザイナー (designer), シェフ (chef), コック (cook), ウェイター (waiter), ウェイトレス (waitress), ガイド (guide), {役者|やくしゃ} (actor), アイドル (idol), モデル (model)
- Natural disasters (4): {津波|つなみ} (tsunami), {洪水|こうずい} (flood), {雪崩|なだれ} (avalanche), {干|ひ}ばつ (drought)
- Colors (2): {金色|きんいろ} (gold), {銀色|ぎんいろ} (silver)
- Household items (6): {扇風機|せんぷうき} (electric fan), {炬燵|こたつ} (kotatsu), アイロン (iron), ベランダ (balcony), ガレージ (garage), ドライヤー (hair dryer)
- Health/Medical (2): ワクチン (vaccine), マスク (mask)
- Vehicles (5): {救急車|きゅうきゅうしゃ} (ambulance), {消防車|しょうぼうしゃ} (fire engine), パトカー (police car), バイク (motorcycle), ヘリコプター (helicopter)
- Business terms (10): {競合|きょうごう} (competition), {卸売|おろしうり} (wholesale), {小売|こうり} (retail), {発注|はっちゅう} (ordering), {受注|じゅちゅう} (receiving orders), {納品|のうひん} (delivery), {出荷|しゅっか} (shipping), {関税|かんぜい} (tariff), {物流|ぶつりゅう} (logistics), {流通|りゅうつう} (distribution)
- Abstract concepts (18): {願望|がんぼう} (desire), {欲望|よくぼう} (craving), {情熱|じょうねつ} (passion), {熱意|ねつい} (enthusiasm), やる{気|き} (motivation), {認識|にんしき} (recognition), {了解|りょうかい} (acknowledgment), {同意|どうい} (consent), {合意|ごうい} (agreement), {連携|れんけい} (cooperation), {規模|きぼ} (scale), {運営|うんえい} (management), {正義|せいぎ} (justice), {倫理|りんり} (ethics), {発言|はつげん} (statement), {討論|とうろん} (debate), {辛抱|しんぼう} (patience), {世代|せだい} (generation)
- Technology (6): アカウント (account), ブログ (blog), モニター (monitor), {充電器|じゅうでんき} (charger), {録音|ろくおん} (recording), アップデート (update)
- Math/Science (11): {百科事典|ひゃっかじてん} (encyclopedia), {代数|だいすう} (algebra), {幾何|きか} (geometry), {微分|びぶん} (differentiation), {積分|せきぶん} (integration), {定数|ていすう} (constant), {演算|えんざん} (operation), ハードウェア (hardware), ウェブサイト (website), {見積|みつも}もり (estimate), {株価|かぶか} (stock price)
- Education (4): {不合格|ふごうかく} (failure), {休学|きゅうがく} (leave of absence), {留年|りゅうねん} (repeating a year), {参考書|さんこうしょ} (reference book), {法則|ほうそく} (law/rule)
- Other vocabulary (17): カラオケ (karaoke), {舅|しゅうと} (father-in-law), {姑|しゅうとめ} (mother-in-law), ジーパン (jeans), {化粧品|けしょうひん} (cosmetics), {日焼|ひや}け{止|ど}め (sunscreen), {山葵|わさび} (wasabi), {皺|しわ} (wrinkle), {黒子|ほくろ} (mole), {齧|かじ}る (to gnaw), {啜|すす}る (to sip), むせる (to choke), {浮|う}き{浮|う}き (cheerful), しゃっくり (hiccup), クワガタ (stag beetle), ゴキブリ (cockroach)

Notable entry features:
- Business vocabulary covers supply chain and commerce terminology
- Math/Science entries include calculus and computer science vocabulary
- Abstract concept entries useful for academic and philosophical discussions
- Cross-references added linking related terms (発注↔受注, 物流↔流通)

Total entries: 5,107 → 5,207
Remaining candidates: 1,652 → 1,548

### 2026-01-16 (Candidate Words Expansion - 200 New Candidates)
Added 200 new candidates to `candidate_words.json` using the balanced coverage strategy:

- **Tier 1 - Core Vocabulary Gaps** (20 candidates): Basic vocabulary including 事 (こと), 黄 (yellow), 白 (white), 多分 (probably), counters (個, 枚, 冊, 台), verbs (点ける, 返す), adjectives (早い, 速い, 可愛い, 固い, 素敵, 綺麗), and conjunctions (ただし, そうすると).

- **Tier 2 - Semantic Domain Completion** (42 candidates): Food/cooking (麺, ラーメン, 煮込む, 和える, 漬ける, 揚げる, すりおろす, 泡立てる), body parts (腸, 肺, 腎臓), cultural terms (床の間, 風呂敷, 提灯, 暖簾, 初詣, 七五三, 盆踊り, 鳥居, お守り), family terms (従兄弟, 叔父, 叔母, 甥, 彼氏), music (曲, 楽器, ライブ), sports (バスケ, バレー, 練習), everyday items (カバン, メガネ, エアコン, バイク, 乗り換え, 終電), work (不合格, 部下, ボーナス), and places (消防署, 役所).

- **Tier 3 - Related Word Networks** (54 candidates): Emotional terms (焦り, 苛立ち, 戸惑い, 安堵, 憂鬱, 苦悩, 葛藤, 羨望, 嫉妬, 悲しみ, 恐れ), antonym pairs (内外, 表裏, 出入り, 開閉, 長短, 大小, 強弱, 高低, 軽重, 善悪, 正誤), communication verbs (説明する, 質問する, 励ます, 感謝する, 同意する, 反対する, 賛成する, 提案する, 議論する), cognition verbs (気づく, 理解する, 想像する, 考慮する, 判断する, 否定する, 予想する, 期待する, 心配する, 安心する), and compound verbs (切り離す, 押し入る, 取り込む, 追いかける, 追い払う, 巻き込む, 呼びかける, 見分ける, 聞き直す, 引き返す, 降り立つ).

- **Tier 4 - Productive Patterns** (56 candidates): ～的 adjectives (経済的, 歴史的, 文化的, 国際的, 科学的, 精神的, 物理的, 心理的, 論理的, 感情的), reduplication (段々, 堂々, 延々, 粛々, 淡々), four-character idioms (三日坊主, 七転八起, 四面楚歌, 一朝一夕, 起死回生, 弱肉強食, 臨機応変, 有名無実, 一心不乱, 我田引水, 異口同音, 因果応報, 暗中模索, 五里霧中), proverbs (猿も木から落ちる, 七転び八起き, 石の上にも三年, 早起きは三文の徳, 百聞は一見に如かず, 井の中の蛙, 蛙の子は蛙, 花より団子, 二兎を追う者は一兎をも得ず, 急がば回れ), number compounds (二重, 四季, 五感, 六法, 七夕, 八方, 九九, 百万, 千円, 万人, 一人前, 二度と), and onomatopoeia (ぴかぴか, ふわふわ, さらさら, ぼろぼろ, がたがた, ばらばら, きらきら, しとしと, ざあざあ, ぽたぽた, もぐもぐ, ぺらぺら, ぐるぐる, ばたばた, にこにこ).

- **Tier 5 - Modern & Informal Vocabulary** (28 candidates): Technology (アップデート, クリック, タップ, スワイプ, ログイン, パスワード, シェア, いいね, コメント, バグ, アカウント, プロフィール, オンライン, オフライン), lifestyle abbreviations (就活, 婚活, 終活, バイト), and social media (炎上, 既読).

Total candidates: 1,452 → 1,652

### 2026-01-16 (Vocabulary Expansion - 100 New Entries, Session 56)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Sports (12): {野球|やきゅう} (baseball), サッカー (soccer), バスケットボール (basketball), バレーボール (volleyball), ゴルフ (golf), マラソン (marathon), ジム (gym), ヨガ (yoga), ジョギング (jogging), スポーツ (sports), {決勝|けっしょう} (final), {予選|よせん} (preliminary)
- Music terms (5): リズム (rhythm), テンポ (tempo), {和音|わおん} (chord), {旋律|せんりつ} (melody), {音階|おんかい} (scale)
- Technology/Computing (15): サーバー (server), クラウド (cloud), ネットワーク (network), アップロード (upload), インストール (install), {更新|こうしん} (update), {設定|せってい} (settings), {入力|にゅうりょく} (input), {出力|しゅつりょく} (output), セキュリティ (security), {暗号|あんごう} (encryption), バックアップ (backup), ブラウザ (browser), アプリケーション (application), クライアント (client)
- AI/Computing (2): {人工知能|じんこうちのう} (AI), {機械学習|きかいがくしゅう} (machine learning)
- Business/Finance (15): {株式|かぶしき} (stock), {融資|ゆうし} (financing), {返済|へんさい} (repayment), {合併|がっぺい} (merger), {買収|ばいしゅう} (acquisition), {消費税|しょうひぜい} (consumption tax), {賃金|ちんぎん} (wages), {不況|ふきょう} (recession), {好況|こうきょう} (boom), インフレ (inflation), デフレ (deflation), {円高|えんだか} (strong yen), {円安|えんやす} (weak yen), {金利|きんり} (interest rate), {雇用|こよう} (employment)
- Education (5): {大学院|だいがくいん} (graduate school), {予備校|よびこう} (prep school), {専門学校|せんもんがっこう} (vocational school), {履修|りしゅう} (course registration), {工学|こうがく} (engineering)
- Science (4): {仮説|かせつ} (hypothesis), {定義|ていぎ} (definition), {分類|ぶんるい} (classification), {検証|けんしょう} (verification)
- Math (4): {方程式|ほうていしき} (equation), {関数|かんすう} (function), {変数|へんすう} (variable), グラフ (graph)
- Society/Politics (8): {内閣|ないかく} (cabinet), {介護|かいご} (nursing care), {少子化|しょうしか} (declining birthrate), {高齢化|こうれいか} (aging), {貧困|ひんこん} (poverty), {格差|かくさ} (disparity), {条約|じょうやく} (treaty), {社会保障|しゃかいほしょう} (social security)
- Sports results (6): {勝敗|しょうはい} (victory/defeat), {引|ひ}き{分|わ}け (draw), {得点|とくてん} (score), {準優勝|じゅんゆうしょう} (runner-up), {準決勝|じゅんけっしょう} (semifinal), {所得税|しょとくぜい} (income tax)
- Communication (4): {発信|はっしん} (transmission), {受信|じゅしん} (reception), {配信|はいしん} (streaming), {合唱|がっしょう} (chorus)
- Abstract concepts (13): {本質|ほんしつ} (essence), {反応|はんのう} (reaction), {改革|かいかく} (reform), {達成|たっせい} (achievement), {可能性|かのうせい} (possibility), {必要性|ひつようせい} (necessity), {重要性|じゅうようせい} (importance), {多様性|たようせい} (diversity), {最大|さいだい} (maximum), {最小|さいしょう} (minimum), {最新|さいしん} (latest), {標準|ひょうじゅん} (standard), ボランティア (volunteer)
- Tech hardware (7): コピー (copy), {圧縮|あっしゅく} (compression), {容量|ようりょう} (capacity), {解像度|かいぞうど} (resolution), ディスプレイ (display), メモリ (memory), {筋|きん}トレ (strength training)

Notable entry features:
- Computing entries include both Japanese and English terminology used in tech contexts
- Business/Finance terms cover modern economic vocabulary
- Cross-references added linking related terms (発信↔受信, 合唱↔独唱)
- Sports vocabulary includes competition terminology

Total entries: 5,007 → 5,107
Remaining candidates: 1,552 → 1,452

### 2026-01-15 (Candidate Words Expansion - 200 New Candidates)
Added 200 new candidates to `candidate_words.json` using the balanced coverage strategy outlined in `newcandidates.md`:

- **Tier 1 - Core Vocabulary Gaps** (70 candidates): Essential verbs missing from the dictionary including 行く, 来る, 見る, 聞く, 言う, 思う, 知る, 分かる, 食べる, 飲む, 書く, 読む, plus transitive/intransitive pairs like 開ける/開く, 閉める/閉じる, 始まる/始める, 終わる/終える. Also added missing basic adjectives (早い, 熱い), adverbs (本当に, 多分, 確かに), and nouns (事).

- **Tier 2 - Semantic Domain Completion** (70 candidates): Action verbs (走る, 歩く, 泳ぐ, 飛ぶ), emotion verbs (怒る, 笑う, 泣く, 喜ぶ, 驚く, 困る), change-of-state verbs (壊れる/壊す, 変わる/変える, 増える, 減る), plus missing colors (白, ピンク), animals (豚, 羊), family terms (叔父, 叔母).

- **Tier 3 & 4 - Related Word Networks & Productive Patterns** (35 candidates): Reduplication words (日々, 国々, 山々, 木々), ～的 adjectives (消極的, 具体的, 抽象的, 一般的, 基本的, 個人的, 社会的, 効果的, 現実的, 理想的, 魅力的, 典型的, 伝統的), compound verbs (追い出す, 取り出す, 持ち上げる, 引き受ける, 飛び出す, 思い出す, 呼び出す), and four-character idioms (一石二鳥, 以心伝心, 一期一会, 十人十色, 四苦八苦, 一長一短, 自業自得).

- **Tier 5 - Modern & Informal Vocabulary** (25 candidates): Technology terms (スマホ, アプリ, ダウンロード, 検索), social media vocabulary (フォロー, 投稿, バズる, 推し), lifestyle terms (コスパ, タイパ, リモート), and colloquial expressions (マジ, やばい, めっちゃ, ウザい, ダサい, キモい, エモい, ガチ, イケメン, 草, 神, ネタバレ).

Total candidates: 1,631 → 1,831

### 2026-01-15 (Vocabulary Expansion - 100 New Entries, Session 55)
Added 100 new dictionary entries from candidate_words.json, covering diverse vocabulary categories:

- Core vocabulary (5): {豚|ぶた} (pig), {羊|ひつじ} (sheep), {本当|ほんとう}に (really), {確|たし}かに (certainly), ピンク (pink)
- Modern/Slang vocabulary (21): スマホ, アプリ, ダウンロード, {検索|けんさく}, フォロー, {投稿|とうこう}, バズる, {推|お}し, コスパ, タイパ, リモート, マジ, やばい, めっちゃ, ウザい, ダサい, キモい, エモい, ガチ, イケメン, ネタバレ
- 四字熟語 (7): {一石二鳥|いっせきにちょう}, {以心伝心|いしんでんしん}, {一期一会|いちごいちえ}, {十人十色|じゅうにんといろ}, {四苦八苦|しくはっく}, {一長一短|いっちょういったん}, {自業自得|じごうじとく}
- ～的 adjectives (13): {消極的|しょうきょくてき}, {具体的|ぐたいてき}, {抽象的|ちゅうしょうてき}, {一般的|いっぱんてき}, {基本的|きほんてき}, {個人的|こじんてき}, {社会的|しゃかいてき}, {効果的|こうかてき}, {現実的|げんじつてき}, {理想的|りそうてき}, {魅力的|みりょくてき}, {典型的|てんけいてき}, {伝統的|でんとうてき}
- Reduplication (4): {日々|ひび}, {国々|くにぐに}, {山々|やまやま}, {木々|きぎ}
- Compound verb (1): {呼|よ}び{出|だ}す (to call out)
- Onomatopoeia (12): ひらひら, ゆらゆら, すれすれ, がらがら, へらへら, むすっと, ぷりぷり, うんざり, げんなり, しんみり, ぱさぱさ, ほかほか
- Emotional vocabulary (15): {哀愁|あいしゅう}, {羞恥|しゅうち}, {孤独|こどく}, {充実|じゅうじつ}, {虚無|きょむ}, {軽蔑|けいべつ}, {惨|みじ}め, {屈辱|くつじょく}, {焦燥|しょうそう}, {切望|せつぼう}, {愛着|あいちゃく}, {落胆|らくたん}, {絶望|ぜつぼう}, {憎悪|ぞうお}, {未練|みれん}
- Business terms (11): {戦略|せんりゃく}, {方針|ほうしん}, {業績|ぎょうせき}, {損失|そんしつ}, {商談|しょうだん}, {企画|きかく}, {手当|てあて}, {福利厚生|ふくりこうせい}, {確定申告|かくていしんこく}, {源泉徴収|げんせんちょうしゅう}, {見積|みつも}り
- Household/Environment (11): インターホン, {表札|ひょうさつ}, {郵便受|ゆうびんう}け, ブラインド, ブレスレット, ブローチ, {世界遺産|せかいいさん}, {天然記念物|てんねんきねんぶつ}, {保護区|ほごく}, {給湯器|きゅうとうき}, {電化製品|でんかせいひん}

Notable entry features:
- Modern slang includes internet/social media terms popular with younger generations
- 四字熟語 entries include origin, literal meaning, and modern usage contexts
- ～的 adjectives cover common academic and formal vocabulary
- Emotional vocabulary useful for literature and nuanced expression
- Business terms cover tax, HR, and corporate planning terminology

Total entries: 4,907 → 5,007
Remaining candidates: 1,831 → 1,552

### 2026-01-15 (Vocabulary Expansion - 50 New Entries, Session 54)
Added 50 new dictionary entries from candidate_words.json, focusing on verbs, kitchen appliances, household items, accessories, work/business vocabulary, education, and technology:

- Verbs (4): {砕|くだ}ける (to break into pieces), {挟|はさ}まる (to be caught between), {照|て}らす (to illuminate), {落|お}ち{着|つ}く (to calm down)
- Kitchen Appliances (6): バター (butter), {乾燥機|かんそうき} (dryer), {食器洗|しょっきあら}い{機|き} (dishwasher), オーブン (oven), トースター (toaster), ミキサー (blender)
- Household Items (3): コンロ (stove), {換気扇|かんきせん} (ventilation fan), シンク (sink)
- Clothing/Accessories (8): {衣類|いるい} (clothing), ベスト (vest), ストッキング (stockings), タイツ (tights), イヤリング (clip-on earrings), ピアス (pierced earrings), {日傘|ひがさ} (parasol)
- Work/Business (14): {昇給|しょうきゅう} (salary increase), {降格|こうかく} (demotion), リストラ (restructuring), {求人|きゅうじん} (job offer), {履歴書|りれきしょ} (resume), {月給|げっきゅう} (monthly salary), {時給|じきゅう} (hourly wage), {賞与|しょうよ} (bonus), {年金|ねんきん} (pension), {経費|けいひ} (expenses), {領収書|りょうしゅうしょ} (receipt), {請求書|せいきゅうしょ} (invoice), {見積|みつも}り (estimate), {取引|とりひき} (transaction), {在庫|ざいこ} (inventory)
- Education (5): {塾|じゅく} (cram school), {幼稚園|ようちえん} (kindergarten), {保育園|ほいくえん} (nursery school), {入試|にゅうし} (entrance exam), {学費|がくひ} (tuition)
- Science/Technology (10): {辞書|じしょ} (dictionary), {理論|りろん} (theory), {概念|がいねん} (concept), {投資|とうし} (investment), {赤字|あかじ} (deficit), {黒字|くろじ} (surplus), アルゴリズム (algorithm), ソフトウェア (software), データベース (database), インターネット (internet)

Notable entry features:
- Verb entries include transitivity pairs and aspect notes
- Business vocabulary covers employment cycle, financial documents, and inventory management
- Education entries explain Japanese education system distinctions (幼稚園 vs 保育園, 塾 vs 予備校)
- Technology entries include modern IT terminology with Japanese usage notes

Total entries: 4,857 → 4,907
Remaining candidates: 1,680 → 1,631

### 2026-01-14 (Candidate Words Expansion - 201 New Candidates)
Added 201 new candidates to `candidate_words.json` using systematic semantic gap analysis across multiple domains:

- **Emotions/psychological terms** (21): 哀愁, 羞恥, 孤独, 充実, 虚無, 軽蔑, 惨め, 屈辱, 焦燥, 切望, 愛着, 落胆, 絶望, 憎悪, 未練, 恥辱, 怨念, 悔恨, 狂喜, 憤慨
- **Compound verbs** (24): 閉め出す, 売り出す, 送り出す, 抜け出す, 逃げ出す, 流れ出す, 染み出す, 溢れ出す, 浮き上がる, 舞い上がる, 呼び込む, 誘い込む, 突き刺す, 突き飛ばす, 投げ捨てる, 殴り倒す, 蹴り飛ばす, 踏みつける, 抱きしめる, 引きずる, 引き寄せる, 押し倒す, 張り付く, 絞り込む
- **Onomatopoeia** (11): ひらひら, ゆらゆら, すれすれ, がらがら, へらへら, むすっと, ぷりぷり, うんざり, げんなり, しんみり, ぱさぱさ, ほかほか
- **Modern/technology terms** (32): プログラミング, コーディング, デバッグ, バグ, プロフィール, プッシュ通知, リモートワーク, 在宅勤務, オンライン会議, ウェブ会議, ビデオ通話, 画面共有, コンテンツ, インフルエンサー, ユーチューバー, 投げ銭, スタートアップ, イノベーション, ソリューション, サステナブル, SDGs, カーボンニュートラル, 脱炭素, 電動, 蓄電, ドローン, 自動運転, ロボット, IoT, 仮想通貨, ブロックチェーン, QRコード
- **Traditional Japanese items & ceremonies** (18): 掛け軸, 屏風, 座布団, ちゃぶ台, 火鉢, 紋付, 手拭い, 番傘, 蛇の目傘, 硯, 香炉, お中元, お歳暮, 祝儀, 不祝儀, 香典, 年賀状, 喪中
- **四字熟語 & proverbs** (27): 我田引水, 森羅万象, 言語道断, 四面楚歌, 針小棒大, 馬耳東風, 青天霹靂, 晴耕雨読, 竜頭蛇尾, 呉越同舟, 画竜点睛, 二律背反, 天変地異, 自暴自棄, 有言実行, 能ある鷹は爪を隠す, 虻蜂取らず, 井の中の蛙, 鬼に金棒, 花より団子, 七転び八起き, 灯台下暗し, 良薬口に苦し, 情けは人の為ならず, 豚に真珠, 猫の手も借りたい, 馬の耳に念仏
- **Body/medical terms** (15): 骨格, 横隔膜, 粘膜, 皮下, 表皮, 発熱, 筋肉痛, 動悸, 息切れ, 痙攣
- **～的 adjectives** (9): 直接的, 間接的, 自発的, 強制的, 悲観的, 楽観的, 建設的, 破壊的, 支配的
- **Food/cooking terms** (14): すりおろす, 汁物, 具材, 冷凍食品, 加工食品, 生鮮食品, 保存料, 添加物, 賞味期限, 消費期限, カロリー, 栄養素, 炭水化物
- **Business/commerce terms** (30): 認定, 取消, 施行, 遵守, 保活, 朝活, ノマド, キャッシュレス, ペーパーレス, コワーキング, フリーランス, ベンチャー, 電子決済, キャッシュバック, ポイント還元, クーポン, 送料, 年会費, 入会金, 解約, 延長, 有効期限, 返金, 不具合, 問い合わせ, 納品書, 明細, 契約書, 同意書

Total candidates: 1,479 → 1,680

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 53)
Added 50 new dictionary entries from candidate_words.json, focusing on household items, clothing, accessories, and work vocabulary:

- Kitchen Utensils (10): ざる (colander), おたま (ladle), へら (spatula), {菜箸|さいばし} (cooking chopsticks), {汁椀|しるわん} (soup bowl), {小皿|こざら} (small plate), {大皿|おおざら} (large plate), {湯呑|ゆの}み (teacup), {箸置|はしお}き (chopstick rest), ボウル (mixing bowl)
- Home/Living Items (10): ソファ (sofa), テーブル (table), {本棚|ほんだな} (bookshelf), クローゼット (closet), {扉|とびら} (door), {縁側|えんがわ} (veranda), {絨毯|じゅうたん} (carpet), シーツ (sheets), ベッド (bed), シャワー (shower)
- Bathroom Items (5): スポンジ (sponge), シャンプー (shampoo), {歯|は}ブラシ (toothbrush), バスタオル (bath towel), {便器|べんき} (toilet bowl)
- Clothing (10): パジャマ (pajamas), ブラウス (blouse), カーディガン (cardigan), ジャケット (jacket), パーカー (hoodie), ワンピース (dress), スニーカー (sneakers), ブーツ (boots), スリッパ (slippers), マフラー (scarf)
- Accessories (5): サングラス (sunglasses), {腕時計|うでどけい} (wristwatch), ネックレス (necklace), リュック (backpack), {団扇|うちわ} (round fan)
- Work Vocabulary (10): {勤務|きんむ} (work), {出勤|しゅっきん} (going to work), {退勤|たいきん} (leaving work), {有給|ゆうきゅう} (paid leave), {昇進|しょうしん} (promotion), {転勤|てんきん} (job transfer), {転職|てんしょく} (job change), {退職|たいしょく} (resignation), {解雇|かいこ} (dismissal), {採用|さいよう} (hiring)

Notable entry features:
- Comprehensive household vocabulary useful for daily life in Japan
- Clothing entries include both loanwords and the casual/formal distinctions in Japanese
- Work vocabulary covers the full employment lifecycle with cultural notes on Japanese workplace culture
- All entries include common expressions and related vocabulary

Total entries: 4,807 → 4,857
Remaining candidates: 1,529 → 1,479

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 52)
Added 50 new dictionary entries from candidate_words.json, focusing on technology/electronics, media/broadcasting, and traditional Japanese arts:

- Technology/Electronics (15): {画面|がめん} (screen), キーボード (keyboard), マウス (mouse), プリンター (printer), カメラ (camera), スピーカー (speaker), イヤホン (earphones), ヘッドホン (headphones), バッテリー (battery), {充電|じゅうでん} (charging), {電源|でんげん} (power supply), コンセント (outlet), ケーブル (cable), {携帯電話|けいたいでんわ} (mobile phone), スマートフォン (smartphone)
- Media/Communication (12): メール (email), チャット (chat), ニュース (news), {報道|ほうどう} (news coverage), {編集|へんしゅう} (editing), {見出|みだ}し (headline), {録画|ろくが} (recording), {再生|さいせい} (playback), {動画|どうが} (video), {映像|えいぞう} (footage), {音声|おんせい} (audio), {字幕|じまく} (subtitles)
- Fine Arts (3): {美術|びじゅつ} (fine arts), {彫刻|ちょうこく} (sculpture), {陶芸|とうげい} (pottery)
- Traditional Japanese Arts (5): {華道|かどう} (flower arrangement), {茶道|さどう} (tea ceremony), {剣道|けんどう} (kendo), {弓道|きゅうどう} (archery), {空手|からて} (karate)
- Performing Arts (7): {歌舞伎|かぶき} (kabuki), {狂言|きょうげん} (kyogen), {落語|らくご} (rakugo), {漫才|まんざい} (manzai), {脚本|きゃくほん} (script), {演出|えんしゅつ} (direction), {視聴|しちょう} (viewing)
- Musical Instruments (5): ギター (guitar), フルート (flute), ドラム (drums), {三味線|しゃみせん} (shamisen), {尺八|しゃくはち} (shakuhachi)
- Other (3): オーケストラ (orchestra), {購読|こうどく} (subscription), チャンネル (channel)

Notable entry features:
- Comprehensive technology vocabulary for modern life and digital communication
- Traditional Japanese arts entries include major schools, equipment, and cultural context
- Performing arts entries cover traditional comedy, theater, and modern media
- Musical instrument entries include both Western and Japanese traditional instruments

Total entries: 4,757 → 4,807
Remaining candidates: 1,579 → 1,529

### 2026-01-14 (Candidate Words Expansion - 202 New Candidates)
Added 202 new candidates to `candidate_words.json` using systematic semantic gap analysis:

- **Medical/anatomical terms** (15): 肩甲骨, 肋骨, 骨盤, 脊椎, 靭帯, 軟骨, 毛細血管, リンパ, 通院, 処方, 感染, 炎症, 切り傷, 応急処置, 健康診断
- **Four-character idioms & proverbs** (9): 二束三文, 三日坊主, 青息吐息, 本末転倒, 猿も木から落ちる, 石の上にも三年, 塵も積もれば山となる, 棚から牡丹餅, 一朝一夕
- **Emotional/psychological terms** (8): 倦怠, 嫌悪, 渇望, 郷愁, 陶酔, 恍惚, 虚脱, 緊迫
- **Traditional culture** (6): 褌, 朱肉, 御神籤, お宮参り, 告別式, 初七日, 四十九日, 一周忌, 三回忌, 法要
- **Honorific vocabulary** (9): お越しになる, 存じる, 頂戴する, 拝借する, お供する, 恐れ入る, 差し支える, お手数, ご容赦
- **Sports & music terms** (14): ドリブル, シュート, オフサイド, ファウル, ゴールキーパー, フォワード, ミッドフィルダー, ディフェンダー, スタメン, アレンジ, リフ, ビート, アドリブ, アンコール
- **Business & finance** (10): 配当, 財務, 経理, 監査, 決算, 収益, 抵当, 担保, 手形, 小切手
- **Transportation** (9): 滑走路, 離陸, 着陸, 搭乗, 乗車, 優先席, 車内, 車掌, 運転士
- **Construction & architecture** (13): 施工, 骨組み, 外壁, 内装, 断熱, 防水, 耐震, 解体, 改築, 増築, 修繕, 塗装, 足場
- **Agriculture** (12): 耕作, 播種, 灌漑, 肥料, 害虫, 苗床, 果樹園, 酪農, 牧場, 飼育, 家畜, 堆肥
- **Modern vocabulary** (6): マウント, チルい, パワハラ, モラハラ, セクハラ, マタハラ
- **Social media slang** (6): リツイート, ハッシュタグ, ネタ, 空気を読む, KY, ガチ勢
- **Environment & energy** (8): 省エネ, ゴミ分別, 埋立地, 太陽光, 風力, 原子力, 水力, 炭素
- **Other categories** (77): Various nouns, verbs, adjectives, and number compounds

Total candidates: 1,377 → 1,579

### 2026-01-14 (Duplicate Entry Cleanup)
Removed 112 duplicate entries (63 duplicate sets) using the new resolve-duplicates and delete-entry skills. Entry count reduced from 4,819 to 4,707.

Added two new Claude Code skills:
- `resolve-duplicates`: Guidelines for identifying, comparing, and safely removing duplicate entries
- `delete-entry`: Step-by-step process for safely deleting entries while updating indexes and cross-references

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 51)
Added 50 new dictionary entries from candidate_words.json, focusing on animal classification, exotic animals, tree types, Japanese cooking methods, and household vocabulary:

- Loanwords (2): ルール (rule), レベル (level)
- Animal classification (6): {哺乳類|ほにゅうるい} (mammal), {爬虫類|はちゅうるい} (reptile), {両生類|りょうせいるい} (amphibian), {魚類|ぎょるい} (fish class), {鳥類|ちょうるい} (bird class), {甲虫|こうちゅう} (beetle)
- Insects/creatures (3): {蚯蚓|みみず} (earthworm), {毛虫|けむし} (caterpillar), {穴熊|あなぐま} (badger)
- Birds (4): {孔雀|くじゃく} (peacock), {白鳥|はくちょう} (swan), {鷺|さぎ} (heron), {鸚鵡|おうむ} (parrot)
- Exotic animals (5): {獅子|しし} (lion), {河馬|かば} (hippopotamus), {麒麟|きりん} (giraffe), {縞馬|しまうま} (zebra), {駱駝|らくだ} (camel)
- Tree classification (5): {樹木|じゅもく} (tree), {広葉樹|こうようじゅ} (broadleaf), {針葉樹|しんようじゅ} (conifer), {落葉樹|らくようじゅ} (deciduous), {常緑樹|じょうりょくじゅ} (evergreen)
- Plants (2): {菖蒲|あやめ} (iris), {蔦|つた} (ivy)
- Japanese cooking methods (7): {佃煮|つくだに} (tsukudani), {煮物|にもの} (simmered dish), {焼|や}き{物|もの} (grilled dish), {揚|あ}げ{物|もの} (fried food), {蒸|む}し{物|もの} (steamed dish), {和|あ}え{物|もの} (dressed dish), {酢|す}の{物|もの} (vinegared dish)
- Japanese dishes/food (7): {焼肉|やきにく} (yakiniku), {雑炊|ぞうすい} (rice porridge), {茶漬|ちゃづ}け (ochazuke), {吸|す}い{物|もの} (clear soup), {饅頭|まんじゅう} (manju), {羊羹|ようかん} (yokan), {洋菓子|ようがし} (Western sweets)
- Meal structure (3): {前菜|ぜんさい} (appetizer), {副菜|ふくさい} (side dish), {主菜|しゅさい} (main dish)
- Household/architecture (6): {玄関|げんかん} (entrance), {廊下|ろうか} (hallway), {天井|てんじょう} (ceiling), {柱|はしら} (pillar), {箪笥|たんす} (chest of drawers), {洋服|ようふく} (Western clothes)

Notable entry features:
- Complete animal classification system with related terms cross-referenced
- Comprehensive Japanese cooking method vocabulary with examples
- Tree classification entries cover both botanical and practical information
- All entries include cultural notes where relevant

Total entries: 4,707 → 4,757
Remaining candidates: 1,840 → 1,783

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 50)
Added 50 new dictionary entries from candidate_words.json, focusing on Japanese food, cooking ingredients, kitchen items, and nature vocabulary:

- Food ingredients (15): {出汁|だし} (soup stock), {味醂|みりん} (mirin), {胡麻油|ごまあぶら} (sesame oil), {小麦粉|こむぎこ} (wheat flour), {片栗粉|かたくりこ} (potato starch), パン{粉|こ} (breadcrumbs), {豆腐|とうふ} (tofu), {納豆|なっとう} (natto), こんにゃく (konjac), {昆布|こんぶ} (kelp), {鰹節|かつおぶし} (dried bonito), {漬物|つけもの} (pickles), {食材|しょくざい} (ingredient), {調味料|ちょうみりょう} (seasoning), {香辛料|こうしんりょう} (spice)
- Japanese dishes (10): {寿司|すし} (sushi), {天|てん}ぷら (tempura), {唐揚|からあ}げ (fried chicken), {焼|や}き{鳥|とり} (yakitori), {味噌汁|みそしる} (miso soup), おにぎり (rice ball), {煎餅|せんべい} (rice cracker), {団子|だんご} (dumpling), {和菓子|わがし} (Japanese sweets), {薬味|やくみ} (condiment)
- Kitchen & household (12): {家電|かでん} (appliances), {掃除機|そうじき} (vacuum), {洗濯機|せんたくき} (washing machine), {炊飯器|すいはんき} (rice cooker), {電子|でんし}レンジ (microwave), {包丁|ほうちょう} (kitchen knife), まな{板|いた} (cutting board), {急須|きゅうす} (teapot), {石鹸|せっけん} (soap), {歯磨|はみが}き{粉|こ} (toothpaste), {浴槽|よくそう} (bathtub), {洗面台|せんめんだい} (washstand)
- Nature & plants (8): {稲妻|いなずま} (lightning), {苔|こけ} (moss), {茸|きのこ} (mushroom), {雑草|ざっそう} (weed), {紫陽花|あじさい} (hydrangea), {向日葵|ひまわり} (sunflower), {朝顔|あさがお} (morning glory)
- Birds & insects (5): {鴉|からす} (crow), {雀|すずめ} (sparrow), {鳩|はと} (pigeon), {昆虫|こんちゅう} (insect), {蛾|が} (moth), {蠅|はえ} (fly)

Notable entry features:
- Extensive coverage of Japanese food culture with cooking terminology
- Kitchen appliance entries include Japanese-specific features and brands
- All food entries include types, preparation methods, and cultural context
- Nature entries feature seasonal significance and traditional associations

Total entries: 4,769 → 4,819
Remaining candidates: 1,904 → 1,840

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 49)
Added 50 new dictionary entries from candidate_words.json, focusing on verbs, environmental/scientific terms, medical vocabulary, and useful suffixes:

- Verbs (27): {透|す}ける (to be transparent), {滲|にじ}む (to blur), {滴|したた}る (to drip), {舞|ま}う (to dance/flutter), {暴|あば}れる (to act violently), {荒|あ}れる (to be rough), {静|しず}まる (to become quiet), {老|お}いる (to grow old), {衰|おとろ}える (to decline), {早|はや}まる (to quicken), {早|はや}める (to hasten), {枯|か}れる (to wither), {萎|しお}れる (to wilt), {芽生|めば}える (to sprout), {蒸|む}れる (to be stuffy), {揺|ゆ}する (to shake), {括|くく}る (to bundle), {絡|から}める (to entwine), {着替|きが}える (to change clothes), {漁|あさ}る (to rummage), {暴|あば}く (to expose), {晒|さら}す (to expose), {逃|のが}す (to let escape), {拒|こば}む (to refuse), {跳|は}ね{上|あ}がる (to jump up), {吹|ふ}き{飛|と}ばす (to blow away), {焦|あせ}る (to be impatient)
- Environmental terms (11): {温暖化|おんだんか} (global warming), リサイクル (recycling), {生態系|せいたいけい} (ecosystem), {気候変動|きこうへんどう} (climate change), {二酸化炭素|にさんかたんそ} (carbon dioxide), {排出|はいしゅつ} (emission), {廃棄物|はいきぶつ} (waste), {再生可能|さいせいかのう} (renewable), {持続可能|じぞくかのう} (sustainable), {生物多様性|せいぶつたようせい} (biodiversity), {絶滅危惧種|ぜつめつきぐしゅ} (endangered species)
- Medical/Health terms (5): {体調|たいちょう} (physical condition), アレルギー (allergy), {脳卒中|のうそっちゅう} (stroke), {鬱病|うつびょう} (depression), {関節痛|かんせつつう} (joint pain)
- Nature/Time terms (3): {言|い}い{訳|わけ} (excuse), {朝焼|あさや}け (morning glow), {日没|にちぼつ} (sunset)
- Suffixes (4): 〜{社|しゃ} (company), 〜{者|しゃ} (person), 〜{団|だん} (group), 〜{長|ちょう} (head/leader)

Notable entry features:
- Comprehensive verb entries with transitivity pairs and ている aspect behavior
- Environmental vocabulary highly relevant for current events discussions
- Medical terms cover common conditions and health-related expressions
- All suffixes include extensive compound word lists

Total entries: 4,719 → 4,769
Remaining candidates: 1,950 → 1,904

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 48)
Added 50 new dictionary entries from candidate_words.json, focusing on animals, plants/trees, and medical/health terms:

- Insects (5): {蝶|ちょう} (butterfly), {蟻|あり} (ant), {蚊|か} (mosquito), {蝸牛|かたつむり} (snail), {蛙|かえる} (frog)
- Reptiles/Sea creatures (8): {蜥蜴|とかげ} (lizard), {鰐|わに} (crocodile), {鯨|くじら} (whale), {海豚|いるか} (dolphin), {鮫|さめ} (shark), {烏賊|いか} (squid), {蛸|たこ} (octopus), {蟹|かに} (crab)
- Birds (4): {鷲|わし} (eagle), {梟|ふくろう} (owl), {鶴|つる} (crane), {燕|つばめ} (swallow)
- Mammals (8): {狼|おおかみ} (wolf), {狐|きつね} (fox), {狸|たぬき} (raccoon dog), {熊|くま} (bear), {鹿|しか} (deer), {猪|いのしし} (wild boar), {栗鼠|りす} (squirrel), {蝙蝠|こうもり} (bat)
- Plants/Trees (15): {幹|みき} (trunk), {蕾|つぼみ} (bud), {花弁|かべん} (petal), {花粉|かふん} (pollen), {楓|かえで} (maple), {銀杏|いちょう} (ginkgo), {桃|もも} (peach), {柿|かき} (persimmon), {栗|くり} (chestnut), {薔薇|ばら} (rose), {百合|ゆり} (lily), {藤|ふじ} (wisteria), {椿|つばき} (camellia), {檜|ひのき} (Japanese cypress), {笹|ささ} (bamboo grass)
- Medical/Health (10): {花粉症|かふんしょう} (hay fever), {糖尿病|とうにょうびょう} (diabetes), {高血圧|こうけつあつ} (high blood pressure), {心臓病|しんぞうびょう} (heart disease), {認知症|にんちしょう} (dementia), {嗅覚|きゅうかく} (sense of smell), {味覚|みかく} (sense of taste), {触覚|しょっかく} (sense of touch), くしゃみ (sneeze), {鼻水|はなみず} (runny nose)

Notable entry features:
- Animal entries include counters, cultural notes, and figurative expressions (e.g., {狐|きつね}と{狸|たぬき}の{化|ば}かし{合|あ}い)
- Plant entries feature seasonal significance and traditional uses (e.g., {笹|ささ} for Tanabata)
- Medical terms cover common conditions relevant to aging society (diabetes, dementia, hypertension)
- All entries include common collocations, proverbs where relevant, and cross-references

Total entries: 4,669 → 4,719
Remaining candidates: 2,000 → 1,950

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 47)
Added 50 new dictionary entries from candidate_words.json, focusing on health/medical vocabulary, nature/geography terms, and astronomy:

- Katakana loanwords (10): ユーモア, ヨット, ヨーロッパ, ライター, ラケット, ラベル, ロケット, パイプ, ノー, タイプライター
- Health/medical terms (10): {副作用|ふくさよう}, {捻挫|ねんざ}, {打撲|だぼく}, {凍傷|とうしょう}, {腹痛|ふくつう}, {腰痛|ようつう}, {吐|は}き{気|け}, {眩暈|めまい}, {倦怠感|けんたいかん}, {不眠症|ふみんしょう}
- Body parts & biology (10): {歯茎|はぐき}, {太腿|ふともも}, {脹脛|ふくらはぎ}, {内臓|ないぞう}, {肝臓|かんぞう}, {細胞|さいぼう}, {遺伝子|いでんし}, {免疫|めんえき}, {視力|しりょく}, {聴力|ちょうりょく}
- Nature/geography (10): {草原|そうげん}, {湿地|しっち}, {峡谷|きょうこく}, {洞窟|どうくつ}, {断崖|だんがい}, {入|い}り{江|え}, {浜|はま}, {霞|かすみ}, {木陰|こかげ}, {日向|ひなた}
- Astronomy/sky (10): {夕焼|ゆうや}け, {黄昏|たそがれ}, {月明|つきあ}かり, {星空|ほしぞら}, {流|なが}れ{星|ぼし}, {天|あま}の{川|がわ}, {銀河|ぎんが}, {惑星|わくせい}, {彗星|すいせい}, {隕石|いんせき}

Notable entry features:
- Medical terms include symptoms, conditions, and body parts useful for healthcare situations
- Nature terms cover diverse landscapes and weather phenomena
- Astronomy entries include cultural references (Tanabata, seasonal observations)
- All entries include common expressions, collocations, and related vocabulary

Total entries: 4,619 → 4,669
Remaining candidates: 2,043 → 2,000

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 46)
Added 50 new dictionary entries from candidate_words.json, focusing on common katakana loanwords:

- Core loanwords: チェックする, アイスクリーム, アルバム, アンケート, イメージ, インタビュー, ウイスキー, エネルギー, エンジン, オフィス
- Commerce/daily life: カード, キャンプ, クラシック, クリスマス, グループ, ゲーム, コンテスト, コーチ, ゴール, サイン
- Emotions/communication: ショック, スイッチ, スケジュール, ストレス, スピーチ, スープ, セット, センター, タイトル, ダンス
- Activities/objects: チャンス, チーム, テント, デザイン, データ, トンネル, ドライブ, ハイキング, バランス, パスポート
- Technology/sports: ブレーキ, プラスチック, プロ, ベンチ, ホーム, ボール, マスコミ, メッセージ, メモ, メンバー

Notable entry features:
- All entries include common patterns and collocations
- Multiple meanings documented where applicable (e.g., ホーム: platform/home, ボール: ball/bowl)
- Japanese-specific usage explained (e.g., ホーム for train platform)
- Related vocabulary and synonyms cross-referenced
- Loanword origins noted (e.g., アンケート from French 'enquête')

Total entries: 4,569 → 4,619
Remaining candidates: 2,043 (sync pending due to reading format mismatch)

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 45)
Added 50 new dictionary entries from candidate_words.json, focusing on compound verbs and transitive/intransitive pairs:

- Compound verbs with 取り～ (take): {取|と}り{出|だ}す, {取|と}り{入|い}れる, {取|と}り{除|のぞ}く, {取|と}り{戻|もど}す, {取|と}り{消|け}す, {取|と}り{組|く}む
- Compound verbs with 持ち～ (hold): {持|も}ち{込|こ}む, {持|も}ち{帰|かえ}る
- Compound verbs with 打ち～ (strike): {打|う}ち{合|あ}わせる, {打|う}ち{込|こ}む, {打|う}ち{明|あ}ける
- Compound verbs with 振り～ (swing): {振|ふ}り{返|かえ}る, {振|ふ}り{向|む}く, {振|ふ}る{舞|ま}う
- Compound verbs with 差し～/押し～/切り～: {差|さ}し{出|だ}す, {差|さ}し{込|こ}む, {押|お}し{付|つ}ける, {押|お}し{込|こ}む, {切|き}り{取|と}る, {切|き}り{替|か}える
- Other compound verbs: {見送|みおく}る, {握|にぎ}りしめる, {詰|つ}め{込|こ}む, {仕掛|しか}ける, {仕込|しこ}む, {縮|ちぢ}める
- Physical state verbs: {歪|ゆが}む, {弾|はず}む, {崩|くず}れる, {潰|つぶ}れる, {溢|あふ}れる
- Transitive/intransitive pairs: {零|こぼ}す/{零|こぼ}れる, {染|そ}める/{染|そ}まる, {嵌|は}める/{嵌|は}まる, {纏|まと}める/{纏|まと}まる
- Cleaning/action verbs: {整|ととの}える, {掃|は}く, {拭|ふ}く, {擦|こす}る, {濯|すす}ぐ, {漕|こ}ぐ
- Body parts: {踵|かかと}, {顎|あご}, {眉|まゆ}, {睫毛|まつげ}, {瞼|まぶた}

Notable entry features:
- All verb entries include transitivity (自動詞/他動詞) markings
- ている aspect behavior documented for each verb
- Transitive/intransitive pairs cross-referenced
- Common collocations and patterns included
- Body part entries include related expressions and idioms

Total entries: 4,519 → 4,569
Remaining candidates: 2,105 → 2,043

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 44)
Added 50 new compound verb entries (複合動詞) from candidate_words.json:

- Compound verbs with 見/聞/思/言 (vision/hearing/thinking/speaking): {見上|みあ}げる, {見下|みおろ}す, {見|み}つめる, {見守|みまも}る, {見逃|みのが}す, {見落|みおと}す, {見直|みなお}す, {見習|みなら}う, {聞|き}き{取|と}る, {聞|き}き{入|い}れる, {思|おも}い{込|こ}む, {思|おも}い{切|き}る, {考|かんが}え{直|なお}す, {言|い}い{出|だ}す, {言|い}い{換|か}える
- Compound verbs with 書/読 (writing/reading): {書|か}き{直|なお}す, {書|か}き{込|こ}む, {読|よ}み{取|と}る, {読|よ}み{上|あ}げる
- Motion compound verbs with ～回る/～込む/～越える (around/into/over): {歩|ある}き{回|まわ}る, {走|はし}り{回|まわ}る, {飛|と}び{回|まわ}る, {動|うご}き{回|まわ}る, {飛|と}び{込|こ}む, {飛|と}び{越|こ}える, {乗|の}り{込|こ}む, {乗|の}り{越|こ}える, {乗|の}り{遅|おく}れる
- Compound verbs with 追/入/出/立 (chase/enter/exit/stand): {追|お}い{越|こ}す, {追|お}い{出|だ}す, {追|お}い{掛|か}ける, {入|はい}り{込|こ}む, {出|で}くわす, {出迎|でむか}える, {立|た}ち{止|ど}まる, {立|た}ち{寄|よ}る, {立|た}ち{去|さ}る
- Body position compound verbs: {座|すわ}り{込|こ}む, {寝転|ねころ}ぶ, {寝付|ねつ}く, {起|お}き{上|あ}がる, {目覚|めざ}める
- Reciprocal compound verbs with ～合う: {向|む}き{合|あ}う, {助|たす}け{合|あ}う, {競|きそ}い{合|あ}う, {支|ささ}え{合|あ}う
- Assembly compound verbs: {組|く}み{合|あ}わせる, {組|く}み{立|た}てる, {仕上|しあ}げる, {仕切|しき}る

Notable entry features:
- All entries follow v2 quality standards with transitivity (自動詞/他動詞) marked
- ている aspect behavior documented for each verb
- Common patterns and collocations included
- Cross-references linking related compound verbs (antonym pairs, similar patterns)
- Compound structure breakdown (e.g., 見る + 上げる → 見上げる)

Total entries: 4,469 → 4,519
Remaining candidates: 2,161 → 2,105

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 43)
Added 50 new dictionary entries from candidate_words.json, focusing on katakana loanwords:

- Nouns (50): アウト (out), アップ (up), インク (ink), カー (car), キャプテン (captain), クリーム (cream), グラス (glass), グランド (ground), ケース (case), コード (code/cord), ジェット{機|き} (jet plane), ジーンズ (jeans), スキー (ski), スケート (skate), スタイル (style), スタンド (stand), スター (star), チャイム (chime), チーズ (cheese), デザート (dessert), デート (date), トップ (top), トラック (truck/track), トランプ (playing cards), トレーニング (training), トン (ton), ダイヤ (diamond/schedule), ダウン (down), ドラマ (drama), ドレス (dress), ノック (knock), ハンサム (handsome), バイオリン (violin), バッグ (bag), パイロット (pilot), パス (pass), ピクニック (picnic), ピン (pin), プラス (plus), プラン (plan), ペンキ (paint), ボーイ (boy/porter), ボート (boat), マイク (microphone), マイナス (minus), マスター (master), マッサージ (massage), マーケット (market), ミス (miss/mistake), ミルク (milk)

Notable entry features:
- All entries are katakana loanwords from English, German, or Dutch
- Words with multiple meanings documented (e.g., グラス: glass/grass, コード: code/cord/chord)
- Common compounds and collocations for each word
- Japanese-specific usage explained (e.g., トランプ for playing cards, not trump)
- Distinctions from native Japanese alternatives noted

Total entries: 4,419 → 4,469
Remaining candidates: 2,249 → 2,161

### 2026-01-14 (Candidate Word Expansion - Session 2)
Added 200 new candidate words across 10 semantic domains:
- **Body parts/medical** (20): 拳, 膵臓, 動脈, 静脈, 免疫, 瞳, 額, 鎖骨, etc.
- **Food/cooking** (25): 捏ねる, 出汁, 薬味, 惣菜, 煮物, 揚げ物, 漬物, 味噌汁, etc.
- **Weather/nature** (20): 霧, 霜, 露, 雹, 吹雪, 稲妻, 豪雨, 虹, 気温, etc.
- **Compound verbs** (25): 追い出す, 追いかける, 切り替える, 取り出す, 持ち上げる, 引き受ける, etc.
- **Onomatopoeia** (20): ざわざわ, しんしん, ぼんやり, じっと, すっきり, しっとり, etc.
- **～的 adjectives** (15): 積極的, 消極的, 具体的, 抽象的, 歴史的, 圧倒的, etc.
- **Four-character idioms** (15): 一石二鳥, 以心伝心, 一期一会, 試行錯誤, 臨機応変, etc.
- **Modern/tech vocabulary** (20): スマホ, アプリ, 推し, バズる, コスパ, タイパ, サブスク, etc.
- **Emotional/psychological** (20): 焦り, 苛立ち, 憂鬱, 葛藤, 嫉妬, 達成感, 虚無感, etc.
- **Traditional/cultural** (20): 畳, 障子, 風呂敷, 初詣, 七五三, 鳥居, 絵馬, etc.

Total candidates: 2,049 → 2,249

### 2026-01-14 (Candidate Word Expansion - 200 New Candidates)
Added 200 new candidate words to candidate_words.json, covering:
- **Reduplication words**: 国々, 山々, 木々, 日々
- **〜的 adjectives**: 具体的, 革新的, 批判的, 本格的, 伝統的, 継続的, etc. (25+ terms)
- **〜やか adjectives**: 煌びやか, 朗らか, 健やか, 爽やか, 鮮やか, 和やか, etc.
- **Compound verbs**: 押し出す, 引き込む, 落ち込む, 受け入れる, 乗り出す, etc.
- **Adverbs**: かろうじて, ひたすら, やたらに, ひとまず, あらかじめ, etc.
- **Onomatopoeia**: 50+ terms covering emotions, texture, movement, eating sounds
- **Modern/Internet vocabulary**: バズる, エモい, ガチ, コスパ, タイパ, SNS terms
- **Tech loanwords**: サブスク, クラウド, アプリ, スマホ, テレワーク, etc.

Total candidates: 1,849 → 2,049

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 42)
Added 50 new dictionary entries from candidate_words.json, including a mix of verbs and nouns:

- Verbs (19): {漂|ただよ}う (to drift), {散|ち}らかる (to be messy), {散|ち}らかす (to scatter), {剥|は}がれる (to come off), {絡|から}む (to get tangled), {解|と}ける (to come undone), {織|お}る (to weave), {研|と}ぐ (to sharpen), {跳|は}ねる (to jump), {潜|ひそ}む (to lurk), {瞬|またた}く (to blink), {鳴|な}く (to cry - animals), {唸|うな}る (to groan), {吸|す}う (to inhale), {吐|は}く (to exhale), {舐|な}める (to lick), {飲|の}み{込|こ}む (to swallow), {味|あじ}わう (to taste), {撫|な}でる (to stroke)
- Na-adjective (1): {卑怯|ひきょう} (cowardly)
- Nouns (30): {統計|とうけい} (statistics), {等分|とうぶん} (division), {特定|とくてい} (specific), {特売|とくばい} (special sale), {内線|ないせん} (phone extension), {中指|なかゆび} (middle finger), {謎々|なぞなぞ} (riddle), {南米|なんべい} (South America), {南北|なんぼく} (north and south), {日程|にってい} (schedule), {農村|のうそん} (farming village), {農薬|のうやく} (pesticide), {能率|のうりつ} (efficiency), {乗換|のりかえ} (transfer), {灰色|はいいろ} (gray), {歯車|はぐるま} (gear), {発想|はっそう} (idea), {発電|はつでん} (power generation), {発売|はつばい} (sale/release), {花嫁|はなよめ} (bride), {早口|はやくち} (fast-talking), {針金|はりがね} (wire), {反映|はんえい} (reflection), {半径|はんけい} (radius), {半島|はんとう} (peninsula), {売買|ばいばい} (trade), {万歳|ばんざい} (banzai), {引算|ひきざん} (subtraction), {筆者|ひっしゃ} (writer), {表紙|ひょうし} (cover)

Notable entry features:
- Comprehensive verb entries with transitivity pairs and aspect notes
- Physical action verbs: {吸|す}う/{吐|は}く (inhale/exhale pair), {舐|な}める, {撫|な}でる
- Sound verbs: {鳴|な}く (animal sounds), {唸|うな}る (groaning)
- Messy/tidy pair: {散|ち}らかる (intransitive) / {散|ち}らかす (transitive)
- Geographic terms: {南米|なんべい}, {南北|なんぼく}, {半島|はんとう}
- Business/technical terms: {統計|とうけい}, {発電|はつでん}, {能率|のうりつ}

Total entries: 4,369 → 4,419
Remaining candidates: 1,902 → 1,849

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 41)
Added 50 new dictionary entries from candidate_words.json, including a mix of verbs, nouns, adjectives, and adverbs:

- Verbs (5): {浮|う}かぶ (to float), {吊|つ}るす (to hang), {捩|ね}じる (to twist), {剥|は}がす (to peel off), {養|やしな}う (to support/nourish)
- Na-adjectives (4): {逆様|さかさま} (upside down), {的確|てきかく} (precise), {透明|とうめい} (transparent), {特殊|とくしゅ} (special)
- Adverb (1): {大層|たいそう} (very much)
- Nouns (40): {温帯|おんたい} (temperate zone), {造船|ぞうせん} (shipbuilding), {増大|ぞうだい} (increase), {体系|たいけい} (system), {体制|たいせい} (structure), {体積|たいせき} (volume), {体操|たいそう} (gymnastics), {大木|たいぼく} (large tree), {対立|たいりつ} (confrontation), {溜息|ためいき} (sigh), {炭鉱|たんこう} (coal mine), {短所|たんしょ} (weak point), {淡水|たんすい} (fresh water), {単数|たんすう} (singular), {短編|たんぺん} (short story), {脱線|だっせん} (derailment), {段階|だんかい} (stage), {断水|だんすい} (water outage), {断定|だんてい} (conclusion), {中途|ちゅうと} (halfway), {超過|ちょうか} (excess), {直後|ちょくご} (immediately after), {貯蔵|ちょぞう} (storage), {通用|つうよう} (circulation), {定員|ていいん} (capacity), {停車|ていしゃ} (stopping), {手帳|てちょう} (notebook), {鉄砲|てっぽう} (gun), {展開|てんかい} (development), {点数|てんすう} (score), {天皇|てんのう} (Emperor), {凸凹|でこぼこ} (unevenness), {伝染|でんせん} (contagion), {統一|とういつ} (unity), {東西|とうざい} (east and west), {投書|とうしょ} (letter to editor), {当日|とうじつ} (that day), {灯台|とうだい} (lighthouse), {盗難|とうなん} (theft), {当番|とうばん} (duty)

Notable entry features:
- Diverse vocabulary: verbs with transitivity info, technical nouns, cultural terms
- Japanese-specific concepts: {天皇|てんのう}, {体操|たいそう}, {障子|しょうじ}-related vocab
- Common expressions and collocations documented in notes
- Proverbs included: {灯台|とうだい}{下|もと}{暗|くら}し (lighthouse proverb)

Total entries: 4,319 → 4,369
Remaining candidates: 1,949 → 1,902

### 2026-01-14 (Vocabulary Expansion - 50 New Entries, Session 40)
Added 50 new dictionary entries from candidate_words.json, focusing on katakana loanwords:
- Nouns (50): アイスクリーム (ice cream), アルバム (album), アンケート (questionnaire), イメージ (image), インタビュー (interview), ウイスキー (whiskey), エネルギー (energy), エンジン (engine), オフィス (office), カード (card), キャンプ (camp), クラシック (classical), クリスマス (Christmas), グループ (group), ゲーム (game), コンテスト (contest), コーチ (coach), ゴール (goal), サイン (sign/autograph), ショック (shock), スイッチ (switch), スケジュール (schedule), ストレス (stress), スピーチ (speech), スープ (soup), セット (set), センター (center), タイトル (title), ダンス (dance), チャンス (chance), チーム (team), テント (tent), デザイン (design), データ (data), トンネル (tunnel), ドライブ (drive), ドラマ (drama), ハイキング (hiking), バランス (balance), ブレーキ (brake), プラスチック (plastic), プロ (professional), ベンチ (bench), ホーム (platform/home), マスコミ (mass media), メッセージ (message), メモ (memo), メンバー (member), ルール (rule), レベル (level)

Notable entry features:
- All entries are katakana loanwords from English, German, or French
- Common everyday vocabulary for learners
- Includes cultural notes where Japanese usage differs from English (e.g., クリスマス, ホーム)
- Multiple meanings documented for polysemous words (e.g., サイン, ホーム, ゴール)

Total entries: 4,269 → 4,319
Remaining candidates: 1,949 → 1,899

### 2026-01-13 (Vocabulary Expansion - 50 New Entries, Session 39)
Added 50 new dictionary entries from candidate_words.json, including:
- Nouns (48): {素人|しろうと} (amateur), {受験|じゅけん} (taking an exam), {述語|じゅつご} (predicate), {巡査|じゅんさ} (policeman), {蒸気|じょうき} (steam), {定規|じょうぎ} (ruler), {上下|じょうげ} (up and down), {人造|じんぞう} (man-made), {人命|じんめい} (human life), {水産|すいさん} (fisheries), {推定|すいてい} (estimation), {水滴|すいてき} (water drop), {水筒|すいとう} (water bottle), {水分|すいぶん} (moisture), {水平|すいへい} (horizontal), {水面|すいめん} (water surface), {寸法|すんぽう} (measurement), {随筆|ずいひつ} (essay), {図表|ずひょう} (chart), {制作|せいさく} (production), {製作|せいさく} (manufacture), {清書|せいしょ} (clean copy), {整数|せいすう} (integer), {清掃|せいそう} (cleaning), {生存|せいぞん} (survival), {政党|せいとう} (political party), {性能|せいのう} (performance), {成分|せいぶん} (ingredient), {性別|せいべつ} (gender), {正門|せいもん} (main gate), {成立|せいりつ} (establishment), {西暦|せいれき} (Western calendar), {赤道|せきどう} (equator), {接近|せっきん} (approach), {接続|せつぞく} (connection), {先端|せんたん} (tip/cutting edge), {先頭|せんとう} (lead), {洗面|せんめん} (washing face), {税関|ぜいかん} (customs), {全般|ぜんぱん} (whole), {創作|そうさく} (creation), {葬式|そうしき} (funeral), {送別|そうべつ} (farewell), {速達|そくたつ} (express mail), {測定|そくてい} (measurement), {算盤|そろばん} (abacus), {損得|そんとく} (profit and loss), {雑巾|ぞうきん} (cleaning rag), {増減|ぞうげん} (fluctuation)
- Adverb (1): {折角|せっかく} (with effort, long-awaited)

Notable entry features:
- Grammar/academic terms: {述語|じゅつご}, {整数|せいすう}, {随筆|ずいひつ}
- Measurement/technical: {水平|すいへい}, {寸法|すんぽう}, {測定|そくてい}
- Homophone pairs: {制作|せいさく} vs {製作|せいさく}
- Traditional Japanese: {算盤|そろばん}, {雑巾|ぞうきん}
- Daily life: {水筒|すいとう}, {洗面|せんめん}, {税関|ぜいかん}

Total entries: 4,219 → 4,269
Remaining candidates: 2,000 → 1,949

### 2026-01-13 (Vocabulary Expansion - 50 New Entries, Session 38)
Added 50 new dictionary entries from candidate_words.json, including:
- Nouns (45): {締|し}め{切|き}り (deadline), {職場|しょくば} (workplace), {資料|しりょう} (materials), {算数|さんすう} (arithmetic), {将棋|しょうぎ} (shogi), {真空|しんくう} (vacuum), {習字|しゅうじ} (penmanship), {書道|しょどう} (calligraphy), {激増|げきぞう} (surge), {原産|げんさん} (origin), {工員|こういん} (factory worker), {工芸|こうげい} (crafts), {口実|こうじつ} (excuse), {高等|こうとう} (higher), {合同|ごうどう} (joint), {作成|さくせい} (creation), {作製|さくせい} (manufacture), {山林|さんりん} (mountain forest), {在学|ざいがく} (enrollment), {材木|ざいもく} (lumber), {雑音|ざつおん} (noise), {下町|したまち} (downtown), {執筆|しっぴつ} (writing), {失恋|しつれん} (heartbreak), {写生|しゃせい} (sketching), {社説|しゃせつ} (editorial), {車輪|しゃりん} (wheel), {主役|しゅやく} (leading role), {消化|しょうか} (digestion), {障子|しょうじ} (shoji), {正味|しょうみ} (net), {書籍|しょせき} (books), {食器|しょっき} (tableware), {書店|しょてん} (bookstore), {心身|しんしん} (mind and body), {申請|しんせい} (application), {寝台|しんだい} (bed), {診断|しんだん} (diagnosis), {親類|しんるい} (relatives), {磁石|じしゃく} (magnet), {自習|じしゅう} (self-study), {実感|じっかん} (realization), {実績|じっせき} (achievements), {実物|じつぶつ} (real thing), {実用|じつよう} (practical use), {実例|じつれい} (example), {蛇口|じゃぐち} (faucet), {熟語|じゅくご} (compound word)
- Na-adjective (1): {公式|こうしき} (official/formula)
- Adverb (1): {始終|しじゅう} (constantly)

Notable entry features:
- Academic terms: {算数|さんすう}, {習字|しゅうじ}, {書道|しょどう}, {熟語|じゅくご}
- Traditional Japanese: {将棋|しょうぎ}, {障子|しょうじ}, {下町|したまち}
- Business/work terms: {職場|しょくば}, {締|し}め{切|き}り, {申請|しんせい}, {実績|じっせき}
- Homophone pairs: {作成|さくせい} vs {作製|さくせい}

Total entries: 4,169 → 4,219
Remaining candidates: 2,051 → 2,000

### 2026-01-13 (Vocabulary Expansion - 43 New Entries, Session 37)
Added 43 new dictionary entries from candidate_words.json, including:
- Adverbs: 恐らく, 徐々に, 再三, 先程, 早速
- Nouns: 陽射し, 夜間, 液体, 応用, 屋外, 書取り, 紙屑, 学会, 規準, 系統, 謙遜, 功績, 光線, 高層, 交替, 校庭, 肯定, 鉱物, 項目, 紅葉, 国王, 国立, 混合, 献立, 祭日, 催促, 採点, 災難, 裁縫, 索引, 作者, 削除, 撮影, 三角
- Na-adjective: 強引

Total entries: 4,136 → 4,169
Remaining candidates: 2,090 → 2,051

### 2026-01-13 (Session 37 initial - superseded)
- Added 10 new dictionary entries from candidate_words.json (4,126 → 4,136 total)
- Each entry written individually following entry-guidelines skill
- New entries include:
  - Adverbs (3): いつのまにか (before one knows), {少|すく}なくとも (at least), {例|たと}え (even if)
  - Nouns (7): いとこ (cousin), {知|し}り{合|あ}い (acquaintance), {釣|つ}り (fishing), {出会|であ}い (encounter), {年寄|としよ}り (elderly person), {他|ほか} (other), {堀|ほり} (moat)
- Note: Many initially targeted candidates (katakana loanwords) were found to already exist in the dictionary
- Removed 3 candidates from candidate_words.json (2,093 → 2,090)

### 2026-01-13 (Vocabulary Expansion - 50 New Entries, Session 36)
- Added 50 new dictionary entries from candidate_words.json (4,076 → 4,126 total)
- Each entry written individually following entry-guidelines skill
- New entries include a diverse mix of vocabulary:
  - Nouns (38): {火傷|やけど} (burn), {夜行|やこう} (night train), {家主|やぬし} (landlord), {夕日|ゆうひ} (setting sun), {浴衣|ゆかた} (yukata), {行方|ゆくえ} (whereabouts), {輸血|ゆけつ} (blood transfusion), {輸送|ゆそう} (transport), {用語|ようご} (terminology), {要旨|ようし} (gist), {用途|ようと} (use), {利害|りがい} (interests), {煉瓦|れんが} (brick), {和服|わふく} (Japanese clothes), {足跡|あしあと} (footprint), {足元|あしもと} (at one's feet), {粗筋|あらすじ} (synopsis), {受取|うけとり} (receipt), {裏口|うらぐち} (back door), {売上|うりあげ} (sales), {英文|えいぶん} (English text), {宴会|えんかい} (party), {園芸|えんげい} (gardening), {演劇|えんげき} (drama), {遠足|えんそく} (excursion), {王女|おうじょ} (princess), {応接|おうせつ} (reception), {応対|おうたい} (handling), {往復|おうふく} (round trip), {欧米|おうべい} (Europe and America), {親指|おやゆび} (thumb), {恩恵|おんけい} (blessing), {温室|おんしつ} (greenhouse), {温泉|おんせん} (hot spring), {会館|かいかん} (meeting hall), {改札|かいさつ} (ticket gate), {開通|かいつう} (opening), {寒帯|かんたい} (frigid zone)
  - Na-adjectives (3): {幼稚|ようち} (childish), {余計|よけい} (unnecessary), {過剰|かじょう} (excessive)
  - Adverbs (3): {油断|ゆだん} (negligence), {幾分|いくぶん} (somewhat), {大凡|おおよそ} (approximately)
  - Suru-verbs (4): {開会|かいかい} (opening), {解散|かいさん} (dissolution), {一旦|いったん} (once/temporarily), {観念|かんねん} (concept/resignation)
  - Academic (2): {概論|がいろん} (introduction), {臨時|りんじ} (temporary)
- Notable entry features:
  - Japanese culture: {浴衣|ゆかた}, {温泉|おんせん}, {宴会|えんかい}
  - Transportation: {夜行|やこう}, {改札|かいさつ}, {往復|おうふく}, {開通|かいつう}
  - Business terms: {売上|うりあげ}, {応接|おうせつ}, {応対|おうたい}
  - Geography: {欧米|おうべい}, {寒帯|かんたい}
  - Body parts: {親指|おやゆび}, {足元|あしもと}
- Removed 51 candidates from candidate_words.json (2,144 → 2,093)

### 2026-01-13 and earlier sessions

See the full archive of earlier sessions in the commit history.

Note: This archive was created on 2026-01-14 when PROJECT_STATUS.md was reorganized to keep only the 10 most recent change entries.
