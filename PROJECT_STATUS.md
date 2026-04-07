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

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 39)
Added 30 new dictionary entries (IDs 22859-22888) from candidate_words.json. A diverse mix of nouns, verbs, adverbs, and expressions covering culture, military, communication, grammar, medicine, food, and more.

- **Nouns (21)**: {葉月|はづき} (August, traditional), {一月|ひとつき} (one month), {実父|じっぷ} (biological father), {祝電|しゅくでん} (congratulatory telegram), {弔電|ちょうでん} (condolence telegram), {末梢|まっしょう} (periphery/trivial), {軽業|かるわざ} (acrobatics), {補語|ほご} (complement, grammar), {五七五|ごしちご} (haiku meter), マグ (mug), ガード (guard/overpass), {脱衣|だつい} (undressing), {美男|びなん} (handsome man), {耳鼻科|じびか} (ENT department), {出回|でまわ}り (market availability), {不定|ふてい} (indefinite), {受章|じゅしょう} (receiving a decoration), {助教授|じょきょうじゅ} (associate professor), {一派|いっぱ} (faction), {造幣|ぞうへい} (minting), {拝承|はいしょう} (acknowledged, humble)
- **Noun/suru verbs (7)**: {駐屯|ちゅうとん} (stationing), {屈曲|くっきょく} (bending), {従軍|じゅうぐん} (military service), {除隊|じょたい} (military discharge), {打電|だでん} (telegraphing)
- **Verb (godan) (1)**: {隈取|くまど}る (to apply kumadori makeup)
- **Adverb (1)**: {猛然|もうぜん} (fiercely)
- **Expressions (2)**: {後塵|こうじん}を{拝|はい}する (to fall behind), {命|いのち}を{絶|た}つ (to end one's life)
- Removed 14 stale candidates (duplicates of existing entries)
- New kanji: 屯 (camp, ID 02661), 梢 (treetop, ID 02662)

### 2026-04-07 (Vocabulary Expansion - 24 New Entries, Session 38)
Added 24 new dictionary entries (IDs 22835-22858) from candidate_words.json. A mix of nouns, verbs, expressions, and a pronoun covering daily life, culture, food, politics, language, and more.

- **Nouns (17)**: {永続|えいぞく} (permanence), {左側|ひだりがわ} (left side), {日曜|にちよう} (Sunday), {蚊帳|かや} (mosquito net), {人民|じんみん} (the people), {飛|と}ばし{読|よ}み (skimming), {箱入|はこい}り (boxed/sheltered), {覚|おぼ}え (memory), {代価|だいか} (price/cost), {通信販売|つうしんはんばい} (mail-order sales), ネット{通販|つうはん} (online shopping), {訪米|ほうべい} (visiting the US), {豪傑|ごうけつ} (heroic person), {寄進|きしん} (shrine donation), {無常感|むじょうかん} (sense of impermanence), {凍|こお}り{豆腐|どうふ} (freeze-dried tofu), {関東弁|かんとうべん} (Kanto dialect), {電話機|でんわき} (telephone set), {合|あ}いびき{肉|にく} (mixed ground meat), やせ{形|がた} (slender build), {収蔵庫|しゅうぞうこ} (storage facility)
- **Verb (godan) (1)**: {引|ひ}きずり{込|こ}む (to drag in)
- **Expression (1)**: {気|き}が{合|あ}う (to get along)
- **Pronoun (1)**: それら (those)
- Removed 1 stale candidate (肉体的, already an entry)

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 37)
Added 30 new dictionary entries (IDs 22805-22834) from candidate_words.json. A practical mix of nouns, expressions, and adverbs covering daily life, weather, health, business, food, culture, art, and grammar.

- **Nouns (18)**: {再婚|さいこん} (remarriage), {重複|ちょうふく} (duplication), {震度|しんど} (seismic intensity), {雨雲|あまぐも} (rain cloud), {胸焼|むねや}け (heartburn), {金切|かなき}り{声|ごえ} (shrill scream), {足腰|あしこし} (legs and lower back), {降水量|こうすいりょう} (precipitation), {草刈|くさか}り (mowing), {庭|にわ}いじり (casual gardening), {会員登録|かいいんとうろく} (membership registration), {寄|よ}せ{鍋|なべ} (mixed hot pot), {陰性|いんせい} (negative test result), {守秘|しゅひ} (confidentiality), {創意|そうい} (originality), {懐中時計|かいちゅうどけい} (pocket watch), {単純作業|たんじゅんさぎょう} (routine work), {肉体労働|にくたいろうどう} (manual labor), {再生紙|さいせいし} (recycled paper), {遠近法|えんきんほう} (perspective in art), {平準化|へいじゅんか} (leveling), キャッチフレーズ (catchphrase), {本日中|ほんじつちゅう} (by today)
- **Expressions (6)**: まだしも (comparatively better), {必要|ひつよう}に{応|おう}じて (as needed), {頬杖|ほおづえ}をつく (rest chin on hand), {言|い}い{換|か}えると (in other words), {切|き}り{離|はな}せない (inseparable), {当|あ}たって{砕|くだ}けろ (nothing ventured nothing gained)
- **Adverbs (2)**: {陰|かげ}で (behind the scenes), まだしも (at least)

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 36)
Added 30 new dictionary entries (IDs 22775-22804) from candidate_words.json. A diverse mix of expressions, adjectives, verbs, pronouns, nouns, and an adverb covering emotions, communication, personality, family, body, education, finance, and more.

- **Expressions (8)**: {手|て}を{貸|か}す (to lend a hand), {手|て}を{出|だ}す (to get involved), {行儀|ぎょうぎ}が{良|よ}い (well-mannered), {期待|きたい}を{膨|ふく}らます (to build up expectations), {才能|さいのう}を{引|ひ}き{出|だ}す (to bring out talent), {威力|いりょく}を{振|ふ}るう (to exert power), {納得|なっとく}させる (to convince), どちら{様|さま} (who, very polite)
- **Na-adjectives (4)**: {未熟|みじゅく}な (immature), {深刻|しんこく}な (serious), {新鮮|しんせん}な (fresh), {幸運|こううん}な (fortunate), {重要|じゅうよう}な (important)
- **Verbs (3)**: {呆|あき}れ{返|かえ}る (to be utterly dumbfounded), {聞|き}き{澄|す}ます (to listen carefully), {胸騒|むなさわ}ぐ (to feel uneasy)
- **I-adjective (1)**: {荒|あら}っぽい (rough, crude)
- **Pronouns (2)**: {僕|ぼく}ら (we, informal male), {私|わたくし}ども (we, very formal humble)
- **Nouns (6)**: お{兄|にい}ちゃん (older brother, casual), スパルタ (Spartan education), {吝嗇家|りんしょくか} (miser), {分娩|ぶんべん} (childbirth), {債権者|さいけんしゃ} (creditor), {予知夢|よちむ} (precognitive dream), {塵埃|じんあい} (dust and dirt), {観|み}る (to watch)
- **Adverb/onomatopoeia (2)**: ぽっちゃり (chubby, plump), こまめに (diligently)
- **New kanji**: 吝 (stingy, ID 02658), 嗇 (miserly, ID 02659), 娩 (childbirth, ID 02660)
- Removed 29 stale candidates that now exist as entries

### 2026-04-07 (Vocabulary Expansion - 15 New Entries, Session 35)
Added 15 new dictionary entries (IDs 22760-22774) from candidate_words.json. A diverse mix of nouns, expressions, and a verb covering culture, daily life, business, communication, medicine, and history.

- **Nouns (8)**: ゴールデンウィーク (Golden Week), {受|う}け{渡|わた}し (handover), {持|も}ち{前|まえ} (natural trait), {救急隊員|きゅうきゅうたいいん} (paramedic), {批判家|ひはんか} (critic), {鑑賞者|かんしょうしゃ} (viewer/appreciator), {過密|かみつ}スケジュール (overcrowded schedule), {忠言|ちゅうげん} (frank advice)
- **Noun/suru verbs (3)**: {自己批判|じこひはん} (self-criticism), {事前予約|じぜんよやく} (advance reservation), {創建|そうけん} (founding/construction)
- **Expressions (2)**: {場合|ばあい}によっては (depending on the case), {予定|よてい}を{立|た}てる (to make plans)
- **Verb (godan) (1)**: {織|お}り{込|こ}む (to weave in/factor in)
- **Adjective-no (1)**: {持|も}ち{前|まえ} (inherent, natural — also noun)

### 2026-04-07 (Vocabulary Expansion - 30 New Entries, Session 34)
Added 30 new dictionary entries (IDs 22730-22759) from candidate_words.json. A diverse mix of nouns, expressions, a verb, and a pre-noun adjectival covering entertainment, society, nature, food, culture, daily life, language, and science.

- **Nouns (21)**: ホラー (horror genre), ミステリー (mystery genre), {発展途上国|はってんとじょうこく} (developing country), {一般人|いっぱんじん} (ordinary person), {田植|たう}え (rice planting), {全面|ぜんめん} (whole surface/all aspects), {一家|いっか}{団|だん}らん (family togetherness), {一覧表|いちらんひょう} (list/table), {交際相手|こうさいあいて} (romantic partner), {作業中|さぎょうちゅう} (work in progress), しめじ (shimeji mushroom), {斜|なな}め{読|よ}み (skimming), さん{付|づ}け (using -san honorific), {左翼|さよく} (left wing), {混雑時間帯|こんざつじかんたい} (peak hours), {散在|さんざい} (scattered), {化学繊維|かがくせんい} (synthetic fiber), {大人数|おおにんずう} (large group), {七草粥|ななくさがゆ} (seven-herb porridge), {事案|じあん} (case/matter), {収容所|しゅうようじょ} (detention center), {沢|さわ} (mountain stream), {季節替|きせつが}わり (seasonal change), {被曝|ひばく} (radiation exposure)
- **Noun/suru verbs (3)**: {越冬|えっとう} (overwintering), {散在|さんざい} (scattered), {被曝|ひばく} (radiation exposure)
- **Verb (1)**: {読|よ}み{流|なが}す (to skim over)
- **Expressions (3)**: {元気|げんき}いっぱい (full of energy), たった{一人|ひとり} (only one person), じゃあまた (see you later)
- **Pre-noun adjectival (1)**: ほんの (just, only, mere)
- **New kanji**: 曝 (expose) — assigned kanji ID 02657









