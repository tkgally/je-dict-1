# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-04
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
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
| Cross-references | ~3,400 |
| Example sentences | ~53,200 |
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

### 2026-04-06 (Vocabulary Expansion - 23 New Entries, Session 26)
Added 23 new dictionary entries (IDs 22504-22526) from candidate_words.json. Focused on verbs (godan, ichidan, suru) and two nouns. Words cover a range of registers from formal/news vocabulary to everyday descriptive verbs.

- **Suru verbs (10)**: {値上|ねあ}げする (to raise prices), {飼育|しいく}する (to breed animals), {離陸|りりく}する (to take off), {破壊|はかい}する (to destroy), {懸念|けねん}する (to be concerned), {鎮火|ちんか}する (to extinguish fire), {伝播|でんぱ}する (to propagate), {否認|ひにん}する (to deny), {夢想|むそう}する (to fantasize), {憂慮|ゆうりょ}する (to be gravely concerned)
- **Ichidan verbs (5)**: {取|と}り{分|わ}ける (to serve out), {待|ま}ち{伏|ふ}せる (to ambush), {振|ふ}り{付|つ}ける (to choreograph), {古|ふる}ぼける (to look old/worn), しゃがれる (to become hoarse)
- **Godan verbs (6)**: {噴|ふ}き{上|あ}がる (to spout up), {生|お}い{茂|しげ}る (to grow thickly), {推|お}し{量|はか}る (to infer), {角張|かくば}る (to be angular), {食|く}いちぎる (to bite off), やせ{細|ほそ}る (to waste away)
- **Nouns (2)**: {旨|うま}さ (deliciousness/skill), {素直|すなお}さ (honesty/straightforwardness)

### 2026-04-06 (Vocabulary Expansion - 30 New Entries, Session 25)
Added 30 new dictionary entries (IDs 22474-22503) from candidate_words.json. A diverse mix of nouns, na-adjectives, and a pronoun covering daily life, culture, food, science, language, music, and more.

- **Na-adjectives (2)**: {不憫|ふびん} (pitiful), {一本気|いっぽんぎ} (single-minded)
- **Pronoun (1)**: {俺様|おれさま} (arrogant "I")
- **Nouns (27)**: {真逆|まぎゃく} (complete opposite), {即時|そくじ} (immediate), {地雷|じらい} (land mine), {置|お}き{場|ば} (storage spot), {掌握|しょうあく} (seizing control), {冷水|れいすい} (cold water), {言明|げんめい} (declaration), {台数|だいすう} (number of vehicles/machines), {英字|えいじ} (Roman letters), おままごと (playing house), {公営|こうえい} (publicly operated), {本線|ほんせん} (main line), {生育|せいいく} (growth of plants), {自治会|じちかい} (residents' association), {押|お}し{寿司|ずし} (pressed sushi), {飲|の}み{口|くち} (taste/mouthfeel), {恵方巻|えほうまき} (lucky direction sushi roll), {未確認|みかくにん} (unconfirmed), {山芋|やまいも} (Japanese yam), {船員|せんいん} (crew member), {曲|ま}がり (bend/curve), {明|あ}け{暮|く}れ (day and night), {変種|へんしゅ} (variant), {稼働中|かどうちゅう} (in operation), {弔辞|ちょうじ} (eulogy), {横笛|よこぶえ} (transverse flute), {反作用|はんさよう} (reaction/counteraction)

### 2026-04-06 (Vocabulary Expansion - 30 New Entries, Session 24)
Added 30 new dictionary entries (IDs 22444-22473) from candidate_words.json. A diverse mix of nouns, suru verbs, an adverb, and an expression covering daily life, culture, business, food, language, nature, travel, law, economics, medicine, and more.

- **Suru verbs (3)**: {活発化|かっぱつか} (becoming more active), {映写|えいしゃ} (projection), {愛好|あいこう} (love/fondness)
- **Adverb (1)**: ひっきりなし (incessantly)
- **Expression (1)**: {一命|いちめい}を{取|と}り{留|と}める (to narrowly escape death)
- **Nouns (25)**: {真|ま}っ{只中|ただなか} (right in the middle of), {試作品|しさくひん} (prototype), {人助|ひとだす}け (helping others), {新雪|しんせつ} (fresh snow), {当社|とうしゃ} (our company), {風呂上|ふろあ}がり (after a bath), {夜行|やこう}バス (overnight bus), {団体旅行|だんたいりょこう} (group tour), かかりつけ{医|い} (family doctor), おこわ (glutinous rice), わらべうた (nursery rhyme), {外聞|がいぶん} (reputation), {小売業者|こうりぎょうしゃ} (retailer), {良縁|りょうえん} (good match), {細雪|ささめゆき} (fine snow), {警句|けいく} (epigram), {茶請|ちゃう}け (tea snack), {言|い}い{渡|わた}し (pronouncement), {写|うつ}し (copy), {無色|むしょく} (colorless), {擬態語|ぎたいご} (mimetic word), {国民|こくみん}の{祝日|しゅくじつ} (national holiday), {公認会計士|こうにんかいけいし} (CPA), {給油所|きゅうゆじょ} (gas station), {供給過剰|きょうきゅうかじょう} (oversupply)

### 2026-04-06 (Vocabulary Expansion - 18 New Entries, Session 23)
Added 18 new dictionary entries (IDs 22426-22443) from candidate_words.json. Focused on high-frequency, practical vocabulary for intermediate learners: common suru verbs, na-adjectives for character/attitude description, and everyday nouns.

- **Suru verbs (10)**: {無理|むり}する (to overdo), {準備|じゅんび}する (to prepare), {用���|ようい}する (to arrange), {尊敬|そんけい}する (to respect), {移動|いどう}する (to move), {駐車|ちゅうしゃ}する (to park), {署名|しょめい}する (to sign), {連想|れんそう}する (to associate), {早退|そうたい}する (to leave early), {通過|つうか}する (to pass through)
- **Na-adjectives (5)**: {肝心|かんじん}な (essential), {器用|きよう}な (dexterous), {真剣|しんけん}な (serious), {��実|せいじつ}な (sincere), {効率的|こうりつてき}な (efficient)
- **Nouns (3)**: {手間暇|てまひま} (time and effort), {通俗|つうぞく} (popular/commonplace), {基本料金|��ほんりょうきん} (basic fee)

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 22)
Added 30 new dictionary entries (IDs 22396-22425) from candidate_words.json. A practical mix of nouns, suru verbs, adjectives, an adverb, and an expression covering daily life, health, education, law, politics, food, culture, and language.

- **Suru verbs (10)**: {悲観|ひかん} (pessimism), {意思表示|いしひょうじ} (expression of intention), {速読|そくどく} (speed reading), {滑走|かっそう} (gliding/taxiing), {包囲|ほうい} (encirclement), {焼却|しょうきゃく} (incineration), {注入|ちゅうにゅう} (injection), {加害|かがい} (inflicting harm), {密売|みつばい} (illegal sale), お{稽古|けいこ} (lessons/practice)
- **Nouns (16)**: {左利|ひだりき}き (left-handed), {入学金|にゅうがくきん} (enrollment fee), {同年代|どうねんだい} (same age group), {虫刺|むしさ}され (insect bite), {冷汗|れいかん} (cold sweat), {活況|かっきょう} (boom/brisk activity), {良性|りょうせい} (benign), {将来性|しょうらいせい} (future potential), {婚姻届|こんいんとどけ} (marriage registration), {交通規制|こうつうきせい} (traffic control), {閣議|かくぎ} (cabinet meeting), {立春|りっしゅん} (beginning of spring), {水質|すいしつ} (water quality), {生焼|なまや}け (undercooked), {言語学|げんごがく} (linguistics), {血筋|ちすじ} (bloodline)
- **Na-adjective (2)**: {簡略|かんりゃく} (simplification), {高潔|こうけつ} (noble/virtuous)
- **Adverb (1)**: どれほど (how much/to what extent)
- **Expression (1)**: というわけで (so/for that reason)


### 2026-04-05 (Vocabulary Expansion - 26 New Entries, Session 21)
Added 26 new dictionary entries (IDs 22340-22365) from candidate_words.json. Removed 3 stale duplicate candidates. A mix of nouns, verbs, and onomatopoeia covering business, sports, culture, health, and daily life.

- **Godan verbs (5)**: {愛|いと}しむ (to cherish), {浅|あさ}まる (to become shallow), {苔|こけ}むす (to become mossy), {拭|ふ}き{消|け}す (to wipe away), {取|と}り{越|こ}す (to worry in advance)
- **Suru verbs (7)**: {厄払|やくばら}い (purification), {通算|つうさん}する (to total up), {評論|ひょうろん}する (to critique), {滅菌|めっきん}する (to sterilize), {画一化|かくいつか} (standardization), {恒常化|こうじょうか} (becoming permanent), {注油|ちゅうゆ}する (to lubricate)
- **Nouns (13)**: {財界|ざいかい} (business world), {秘密|ひみつ}{兵器|へいき} (secret weapon), {銀|ぎん}メダル (silver medal), {銅|どう}メダル (bronze medal), {使用人|しようにん} (servant), {執筆者|しっぴつしゃ} (author), {村民|そんみん} (villagers), {歴史|れきし}{学者|がくしゃ} (historian), {他殺|たさつ} (homicide), {病原菌|びょうげんきん} (pathogenic bacteria), マメ (blister), {整腸剤|せいちょうざい} (digestive medicine), ギャンブラー (gambler)
- **Onomatopoeia (1)**: ごうごう (roaring sound)


### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 21)
Added 30 new dictionary entries (IDs 22366-22395) from candidate_words.json. A mix of suru verbs, na-adjectives, nouns, and a conjunction covering science, health, business, law, culture, education, and everyday life.

- **Suru verbs (12)**: {消滅|しょうめつ}する (to vanish), {発症|はっしょう}する (to develop symptoms), {除去|じょきょ}する (to remove), {分離|ぶんり}する (to separate), {編成|へんせい}する (to organize), {統括|とうかつ}する (to oversee), {発現|はつげん}する (to manifest), {発火|はっか} (ignition), {保釈|ほしゃく} (bail), {徴税|ちょうぜい} (tax collection), {間借|まが}り (room rental), {射出|しゃしゅつ} (ejection)
- **Na-adjectives (4)**: {印象的|いんしょうてき}な (impressive), {正常|せいじょう}な (normal), {過小|かしょう}な (too small), {真面目|まじめ}な (serious)
- **Nouns (12)**: {適宜|てきぎ} (as appropriate), {冊子|さっし} (booklet), {期末|きまつ} (end of term), {重箱|じゅうばこ} (tiered box), {番犬|ばんけん} (guard dog), {闘争心|とうそうしん} (fighting spirit), {失業者|しつぎょうしゃ} (unemployed person), {学識|がくしき} (scholarship), {成句|せいく} (set phrase), {横断幕|おうだんまく} (banner), {当代|とうだい} (current generation), {共栄|きょうえい} (co-prosperity), {定理|ていり} (theorem)
- **Conjunction (1)**: なのに (despite that)







