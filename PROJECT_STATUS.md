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

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 21)
Added 30 new dictionary entries (IDs 22310-22339) from candidate_words.json. A diverse mix covering daily life, culture, sports, food, business, geography, and more.

- **Verb (1)**: {語|かた}り{継|つ}ぐ (to pass down orally)
- **Adverb (1)**: {思|おも}う{存分|ぞんぶん} (to one's heart's content)
- **Nouns (28)**: {切|き}り{口|くち} (perspective/cross-section), {追加|ついか}{料金|りょうきん} (additional fee), {停学|ていがく} (school suspension), {社会|しゃかい}{貢献|こうけん} (social contribution), {駆|か}け{足|あし} (running/quick pace), {懸垂|けんすい} (pull-up), {案内|あんない}{板|ばん} (information board), {彫像|ちょうぞう} (statue), {空前|くうぜん} (unprecedented), {馬券|ばけん} (horse racing ticket), {知力|ちりょく} (intellect), {年代物|ねんだいもの} (vintage item), {鼻筋|はなすじ} (bridge of nose), {取|と}り{壊|こわ}し (demolition), {建設中|けんせつちゅう} (under construction), {営業|えいぎょう}スマイル (customer-service smile), {豚丼|ぶたどん} (pork bowl), {百人一首|ひゃくにんいっしゅ} (Hyakunin Isshu), {懸賞金|けんしょうきん} (prize money), {講談|こうだん} (storytelling), {喫煙席|きつえんせき} (smoking seat), {宝飾品|ほうしょくひん} (jewelry), {躍動感|やくどうかん} (sense of dynamism), インテリア (interior), {急坂|きゅうざか} (steep slope), {平均台|へいきんだい} (balance beam), {跳|と}び{箱|ばこ} (vaulting box), {酪農家|らくのうか} (dairy farmer)

### 2026-04-05 (Vocabulary Expansion - 26 New Entries, Session 21)
Added 26 new dictionary entries (IDs 22340-22365) from candidate_words.json. Removed 3 stale duplicate candidates. A mix of nouns, verbs, and onomatopoeia covering business, sports, culture, health, and daily life.

- **Godan verbs (5)**: {愛|いと}しむ (to cherish), {浅|あさ}まる (to become shallow), {苔|こけ}むす (to become mossy), {拭|ふ}き{消|け}す (to wipe away), {取|と}り{越|こ}す (to worry in advance)
- **Suru verbs (7)**: {厄払|やくばら}い (purification), {通算|つうさん}する (to total up), {評論|ひょうろん}する (to critique), {滅菌|めっきん}する (to sterilize), {画一化|かくいつか} (standardization), {恒常化|こうじょうか} (becoming permanent), {注油|ちゅうゆ}する (to lubricate)
- **Nouns (13)**: {財界|ざいかい} (business world), {秘密|ひみつ}{兵器|へいき} (secret weapon), {銀|ぎん}メダル (silver medal), {銅|どう}メダル (bronze medal), {使用人|しようにん} (servant), {執筆者|しっぴつしゃ} (author), {村民|そんみん} (villagers), {歴史|れきし}{学者|がくしゃ} (historian), {他殺|たさつ} (homicide), {病原菌|びょうげんきん} (pathogenic bacteria), マメ (blister), {整腸剤|せいちょうざい} (digestive medicine), ギャンブラー (gambler)
- **Onomatopoeia (1)**: ごうごう (roaring sound)

### 2026-04-05 (Vocabulary Expansion - 28 New Entries, Session 20)
Added 28 new dictionary entries (IDs 22282-22309) from candidate_words.json. A diverse mix covering daily life, culture, business, sports, food, and language.

- **Suru verbs (2)**: {遅刻|ちこく}する (to be late), {欠席|けっせき}する (to be absent)
- **Ichidan verbs (3)**: {抜|ぬ}きん{出|で}る (to excel), しゃれる (to be stylish), {洗練|せんれん}される (to be refined)
- **Na-adjective (1)**: {艶|つや}やか (glossy, lustrous)
- **Expression (1)**: {納得|なっとく}がいく (to be convinced)
- **Nouns (21)**: {努力家|どりょくか} (hard worker), {逆境|ぎゃっきょう} (adversity), {人|ひと}だかり (crowd), {水差|みずさ}し (pitcher), プライド (pride), {町家|まちや} (townhouse), {快適|かいてき}さ (comfort), {冷凍室|れいとうしつ} (freezer), {数|かぞ}え{年|どし} (traditional age), {茶道具|さどうぐ} (tea utensils), サビ (chorus), {朝会|ちょうかい} (morning meeting), {利益率|りえきりつ} (profit margin), {安全地帯|あんぜんちたい} (safety zone), {不戦敗|ふせんぱい} (forfeit loss), {舞台挨拶|ぶたいあいさつ} (stage greeting), {反則負|はんそくま}け (foul loss), {七分咲|ななぶざ}き (70% bloom), {蒸|む}し{菓子|がし} (steamed sweet), {敬白|けいはく} (respectfully yours), {謹啓|きんけい} (respectfully)

### 2026-04-05 (Vocabulary Expansion - 30 New Entries, Session 21)
Added 30 new dictionary entries (IDs 22366-22395) from candidate_words.json. A mix of suru verbs, na-adjectives, nouns, and a conjunction covering science, health, business, law, culture, education, and everyday life.

- **Suru verbs (12)**: {消滅|しょうめつ}する (to vanish), {発症|はっしょう}する (to develop symptoms), {除去|じょきょ}する (to remove), {分離|ぶんり}する (to separate), {編成|へんせい}する (to organize), {統括|とうかつ}する (to oversee), {発現|はつげん}する (to manifest), {発火|はっか} (ignition), {保釈|ほしゃく} (bail), {徴税|ちょうぜい} (tax collection), {間借|まが}り (room rental), {射出|しゃしゅつ} (ejection)
- **Na-adjectives (4)**: {印象的|いんしょうてき}な (impressive), {正常|せいじょう}な (normal), {過小|かしょう}な (too small), {真面目|まじめ}な (serious)
- **Nouns (12)**: {適宜|てきぎ} (as appropriate), {冊子|さっし} (booklet), {期末|きまつ} (end of term), {重箱|じゅうばこ} (tiered box), {番犬|ばんけん} (guard dog), {闘争心|とうそうしん} (fighting spirit), {失業者|しつぎょうしゃ} (unemployed person), {学識|がくしき} (scholarship), {成句|せいく} (set phrase), {横断幕|おうだんまく} (banner), {当代|とうだい} (current generation), {共栄|きょうえい} (co-prosperity), {定理|ていり} (theorem)
- **Conjunction (1)**: なのに (despite that)







