# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-07
**Current phase**: Phase 6 - Continued Expansion & Polish

**Live site**: https://www.tkgje.jp/

> **Full history**: Older change logs are archived in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
> **Quick reference**: See [PROJECT_CONTEXT_BRIEF.md](PROJECT_CONTEXT_BRIEF.md) for a concise session-start overview.
> **Project setup**: See [CLAUDE.md](CLAUDE.md) for commands, file placement, and skills.

## Current State

**Phase 6: Continued Expansion & Polish** — Adding vocabulary while maintaining v2 quality standards, with an automated pipeline for batch maintenance tasks. The dictionary uses an original three-tier vocabulary classification (basic, core, general) instead of JLPT levels.

### Content Status

These counts are approximate. Run `make report` for accurate, up-to-date numbers.

| Metric | Value |
|--------|-------|
| Total entries | ~10,363 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~7,564 (open) |
| Candidate words | ~159 |
| Cross-references | ~3,315 |
| Example sentences | ~40,500 |
| Audio files | 1,028 |

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

## Recent Changes

### 2026-02-07 (Vocabulary Expansion - 30 New Entries, Session 222)
Added 30 new dictionary entries from candidate_words.json, covering verbs, nouns, adjectives, adverbs, and food vocabulary:

- **Verbs (14)**: すくめる (to shrug), そそる (to arouse/tempt), そびえる (to tower), {逸|そ}らす (to avert), {例|たと}える (to compare), {辿|たど}る (to trace), {付|つ}け{込|こ}む (to take advantage of), つつく (to poke/peck), つまむ (to pinch), {付|つ}きまとう (to follow around), すり{減|へ}る (to wear down), ずば{抜|ぬ}ける (to be outstanding), ちなむ (to be associated with)
- **Nouns (10)**: せせらぎ (murmuring stream), {微風|そよかぜ} (gentle breeze), {鯛焼|たいや}き (taiyaki), たこ{焼|や}き (takoyaki), {卵焼|たまごや}き (rolled omelet), すき{焼|や}き (sukiyaki), ざわめき (commotion), {裾野|すその} (foothills), {対面|たいめん} (face-to-face), {繋|つな}がり (connection)
- **Adverbs (3)**: ちょっぴり (a tiny bit), ついつい (despite oneself), ただただ (simply/nothing but)
- **I-adjective (1)**: だらしない (sloppy/undisciplined)
- **Other nouns (2)**: {大名|だいみょう} (feudal lord), そぼろ (crumbled meat topping), だんまり (silence)

Notable entry features:
- Multi-sense entries: だらしない (sloppy/undisciplined), つつく (poke/nibble/peck), つまむ (pinch/snack), すり{減|へ}る (wear down physically/figuratively), {裾野|すその} (foothills/figurative base), {付|つ}きまとう (follow/haunt)
- Food vocabulary cluster: {鯛焼|たいや}き, たこ{焼|や}き, {卵焼|たまごや}き, すき{焼|や}き, そぼろ
- Transitivity pair: すくめる/すくむ
- Homophone cross-reference: {付|つ}け{込|こ}む/{漬|つ}け{込|こ}む

Total entries: 10,333 → 10,363
Remaining candidates: 153 → 159 (some new candidates added by update_indexes)
New kanji: 2,249 → 2,250 ({鯛|ちょう})

### 2026-02-07 (Vocabulary Expansion - 30 New Entries, Session 221)
Added 30 new dictionary entries from candidate_words.json, covering general vocabulary across multiple parts of speech:

- **Nouns (8)**: お{調子者|ちょうしもの} (show-off), {胡麻|ごま} (sesame), さつまいも (sweet potato), {最中|さなか} (in the midst of), {躾|しつけ} (discipline), さえずり (birdsong), {仕業|しわざ} (act/deed), この{世|よ} (this world)
- **Verbs (9)**: ぐずる (to whine), くっつける (to attach), {込|こ}み{上|あ}げる (to well up), {象|かたど}る (to model after), {組|く}み{上|あ}げる (to assemble), くるむ (to wrap), {授|さず}ける (to grant), しかめる (to frown), しがみつく (to cling to), すくむ (to freeze with fear)
- **Adverbs (10)**: きょうび (nowadays), くまなく (thoroughly), こないだ (the other day), ごっそり (entirely), さぞかし (surely), しっくり (to fit well), しょっちゅう (constantly), せめて (at least), ぐいっと (with a jerk)
- **Na-adjective (1)**: しなやか (supple/graceful)
- **Expression (1)**: かけがえのない (irreplaceable)
- **Ichidan verb (1)**: {染|し}みる (to soak in/sting/move deeply)

Notable entry features:
- Multi-sense entries: くっつける (attach/bring close), {込|こ}み{上|あ}げる (emotions/nausea), ぐいっと (jerk/gulp), {授|さず}ける (bestow/teach), しなやか (supple/graceful), {染|し}みる (soak/sting/move)
- Transitivity pairs noted: くっつける/くっつく, くるむ/くるまる, すくむ/すくめる, {授|さず}ける/{授|さず}かる
- Food vocabulary: {胡麻|ごま}, さつまいも
- Physical/emotional vocabulary: すくむ, しがみつく, {込|こ}み{上|あ}げる, しかめる

Total entries: 10,303 → 10,333
Remaining candidates: 183 → 153

### 2026-02-06 (Vocabulary Expansion - 30 New Entries, Session 220)
Added 30 new dictionary entries from candidate_words.json, covering a wide variety of useful general vocabulary:

- **Nouns (12)**: お{気|き}に{入|い}り (favorite), お{笑|わら}い (comedy), お{願|ねが}い (request/please), かき{氷|ごおり} (shaved ice), かまぼこ (fish cake), からくり (mechanism/trick), きっかけ (trigger/opportunity), くじ (lottery), {粥|かゆ} (rice porridge), {胡椒|こしょう} (pepper), {繰|く}り{返|かえ}し (repetition), ご{無沙汰|ぶさた} (long silence)
- **Verbs (6)**: {匿|かくま}う (to shelter), {庇|かば}う (to protect), {被|かぶ}せる (to cover), {潜|くぐ}る (to pass through), くっつく (to stick to), こだわる (to be particular about)
- **Na-adjectives (4)**: {微|かす}か (faint/slight), {気|き}まま (free-spirited), こまめ (frequent/diligent), ささやか (modest/humble)
- **I-adjective (1)**: くどい (persistent/heavy taste)
- **Adverbs (7)**: かつて (formerly), きっちり (precisely), きょとん (blankly), がらり (completely/drastically), {散々|さんざん} (severely/terribly), ごく (very/extremely), {繰|く}り{返|かえ}し (repeatedly)

Notable entry features:
- Multi-sense entries: かつて (past/never with negative), {被|かぶ}せる (cover/put on/blame), こだわる (quality standards/fixation), がらり (dramatic change/sliding sound)
- Food-related cluster: かき{氷|ごおり}, かまぼこ, {粥|かゆ}, {胡椒|こしょう}, かぼちゃ
- Cultural notes: かき{氷|ごおり} (summer tradition), {粥|かゆ} ({七草|ななくさ}{粥|がゆ}), かまぼこ (おせち{料理|りょうり}), からくり ({江戸時代|えどじだい} automata)
- Transitivity pairs: くっつく/くっつける, {被|かぶ}せる/{被|かぶ}る

Total entries: 10,276 → 10,306
Remaining candidates: 183 → 153
New kanji: 2,245 → 2,249 ({匿|とく}, {庇|ひ}, {椒|しょう}, {粥|しゅく})

### 2026-02-05 (Vocabulary Expansion - 30 New Entries, Session 219)
Added 30 new dictionary entries from candidate_words.json, covering casual expressions, household items, administrative documents, finance, social media, and daily life:

- **Casual Expressions/Interjections (2)**: しまった (oh no!), やった (yay!)
- **Mimetic/Onomatopoeia (3)**: いちゃいちゃ (flirting), ちやほや (pampering), のりのり (in high spirits)
- **Adjective (1)**: {怪|あや}しい (suspicious/dubious)
- **Social/Cultural (3)**: {合|ごう}コン (group blind date), お{一人|ひとり}{様|さま} (solo customer), おばちゃん (auntie/middle-aged woman)
- **Household Items (4)**: お{箸|はし} (chopsticks), {三角|さんかく}コーナー (sink strainer), {水切|みずき}りかご (dish drainer), レンジ{対応|たいおう} (microwave-safe)
- **Administrative Documents (5)**: {転居届|てんきょとどけ} (change of address), {印鑑証明|いんかんしょうめい} (seal certificate), {戸籍謄本|こせきとうほん} (family register copy), {訂正印|ていせいいん} (correction seal), {二重線|にじゅうせん} (double strikethrough)
- **Finance/Business (4)**: {不均衡|ふきんこう} (imbalance), {仲介手数料|ちゅうかいてすうりょう} (brokerage fee), {比較検討|ひかくけんとう} (comparative evaluation), {反落|はんらく} (reactionary drop)
- **Daily Life/Labels (3)**: {年度始|ねんどはじ}め (start of fiscal year), {保存方法|ほぞんほうほう} (storage instructions), バーコード (barcode)
- **Transportation (1)**: {弱冷房車|じゃくれいぼうしゃ} (mildly air-conditioned car)
- **Technology/SNS (3)**: タグ{付|づ}け (tagging), {既読|きどく}スルー (leaving on read), メモる (to jot down)
- **Reference (1)**: {取扱説明書|とりあつかいせつめいしょ} (user manual)

Notable entry features:
- Multi-sense entries: {怪|あや}しい (suspicious/dubious), お{一人|ひとり}{様|さま} (service/cultural), おばちゃん (family/general)
- Administrative document trio: {転居届|てんきょとどけ}, {印鑑証明|いんかんしょうめい}, {戸籍謄本|こせきとうほん}
- Correction process pair: {訂正印|ていせいいん} + {二重線|にじゅうせん}
- Modern Japanese terms: {既読|きどく}スルー, タグ{付|づ}け, メモる

Total entries: 10,246 → 10,276
Remaining candidates: 141 → 112
New kanji: 2,242 → 2,245 ({怪|かい}, {訂|てい}, {謄|とう})

### 2026-02-05 (Vocabulary Expansion - 30 New Entries, Session 218)
Added 30 new dictionary entries from candidate_words.json, focusing on daily life, food, family, and practical vocabulary:

- **Na-adjectives (2)**: うってつけ (ideal/perfect for), {虚|うつ}ろ (hollow/vacant)
- **I-adjectives (2)**: {惜|お}しい (regrettable/close), {惜|お}しげもなく (without hesitation)
- **Food (5)**: うに (sea urchin), オクラ (okra), お{浸|ひた}し (boiled greens), おむすび (rice ball), レトルト (retort pouch food)
- **Family (3)**: おふくろ (mother informal), おやじ (father informal), {乙女|おとめ} (maiden)
- **Daily Life Items (4)**: {上履|うわば}き (indoor shoes), ストロー (straw), ナプキン (napkin), カート (cart)
- **Signs/Status (2)**: {点検中|てんけんちゅう} (under inspection), {清掃中|せいそうちゅう} (cleaning in progress)
- **Business/Finance (4)**: {内税|うちぜい} (tax-inclusive), {外税|そとぜい} (tax-exclusive), {擦|す}り{合|あ}わせ (coordination), お{墨付|すみつ}き (seal of approval)
- **Other (8)**: おい (hey), {折|おり} (occasion), お{好|この}み{焼|や}き (okonomiyaki), お{客|きゃく}さん (guest/customer), {思|おも}い (thought/feeling), {咳|せ}き{込|こ}む (coughing fit), {決|き}め{付|つ}け (jumping to conclusions), {赤面症|せきめんしょう} (tendency to blush)

Notable entry features:
- Multi-sense entries: {虚|うつ}ろ (hollow/vacant), {惜|お}しい (regrettable/close), ナプキン (table/sanitary), おやじ (father/shop owner), カート (shopping/go-kart)
- Informal family terms: おふくろ, おやじ (commonly used by men)
- Practical daily life vocabulary useful for living in Japan
- Tax terminology pair: {内税|うちぜい}/{外税|そとぜい}

Total entries: 10,216 → 10,246
Remaining candidates: 170 → 141

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
