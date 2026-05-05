# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-04-17
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

### 2026-05-05 (Vocabulary Expansion - 25 New Entries, Batch 94)
Added 25 new dictionary entries (IDs 26886-26910) from candidate_words.json. Mixed vocabulary covering everyday life, culture, medicine, law, food, and more.

- **Everyday/Onomatopoeia (2)**: はっきりする (to become clear/definite), ぼーっとする (to space out)
- **Food/Kitchen (2)**: {醤油|しょうゆ}{差|さ}し (soy sauce dispenser), {大根|だいこん}おろし (grated daikon)
- **Media/Entertainment (1)**: {最終回|さいしゅうかい} (final episode)
- **Medical (4)**: {医療|いりょう}{機関|きかん} (medical institution), {治療費|ちりょうひ} (medical expenses), {精神|せいしん}{障害|しょうがい} (mental disorder), {神経症|しんけいしょう} (neurosis)
- **Work/Business (3)**: フルタイム (full-time), {理事長|りじちょう} (chairperson), {経済|けいざい}{破綻|はたん} (economic collapse)
- **Housing (1)**: {大家|おおや}さん (landlord)
- **Geography/Nature (3)**: {水域|すいいき} (waters), {海域|かいいき} (sea area), {四|よ}つ{辻|つじ} (crossroads)
- **Law/Society (1)**: {贈収賄|ぞうしゅうわい} (bribery)
- **Culture/Architecture (2)**: {欄間|らんま} (transom), {亭主関白|ていしゅかんぱく} (domineering husband)
- **Language/Literature (2)**: {嘲弄|ちょうろう}する (to mock), {断続|だんぞく} (intermittence)
- **Family/Heritage (1)**: {血脈|けつみゃく} (bloodline)
- **Other (3)**: {償|つぐな}い (atonement), {欄外|らんがい} (margin), {豊漁|ほうりょう} (good catch)
- Removed 42 stale duplicate candidates; 24 candidates synced from candidate list

Total entries: 26,677 → 26,702.

### 2026-05-05 (Vocabulary Expansion - 30 New Entries, Batch 93)
Added 30 new dictionary entries (IDs 26826-26855) from candidate_words.json. Focus on common suru verbs and useful vocabulary for intermediate learners.

- **Starting/Ending (3)**: {開始|かいし}する (to commence), {解除|かいじょ}する (to cancel/lift), {短縮|たんしゅく}する (to shorten)
- **Safety/Emergency (3)**: {避難|ひなん}する (to evacuate), {脱出|だっしゅつ}する (to escape), {救出|きゅうしゅつ}する (to rescue)
- **Communication/Cognition (6)**: {提示|ていじ}する (to present), {指示|しじ}する (to instruct), {解釈|かいしゃく}する (to interpret), {解明|かいめい}する (to clarify), {推理|すいり}する (to deduce), {発音|はつおん}する (to pronounce)
- **Law/Authority (2)**: {逮捕|たいほ}する (to arrest), {命令|めいれい}する (to command)
- **Interpersonal (3)**: {配慮|はいりょ}する (to be considerate), {訪問|ほうもん}する (to visit), {援助|えんじょ}する (to assist)
- **Daily Life (4)**: {散歩|さんぽ}する (to take a walk), {外出|がいしゅつ}する (to go out), {着用|ちゃくよう}する (to wear), {記憶|きおく}する (to memorize)
- **Business/Society (4)**: {改善|かいぜん}する (to improve), {重視|じゅうし}する (to emphasize), {滞在|たいざい}する (to stay), {転売|てんばい}する (to resell)
- **Emotions/Description (3)**: {爆笑|ばくしょう}する (to burst out laughing), {馬鹿|ばか}げる (to be ridiculous), {未練|みれん}がましい (clingy)
- **Other (2)**: {賑|にぎ}わい (bustle/prosperity), {豪華|ごうか}な (luxurious)
- 30 candidates synced from candidate list

Total entries: 26,618 → 26,648.

### 2026-05-05 (Vocabulary Expansion - 24 New Entries, Batch 92)
Added 24 new dictionary entries (IDs 26802-26825) from candidate_words.json. Focus on high-utility general vocabulary for intermediate learners.

- **Food/Sensation (2)**: さっぱりする (to feel refreshed), こってりする (to be rich/heavy in flavor)
- **Commerce/Daily Life (3)**: {取|と}り{寄|よ}せる (to order from afar), {常連客|じょうれんきゃく} (regular customer), {後片付|あとかたづ}け (cleanup after activity)
- **Communication/Cognition (3)**: {納得|なっとく}する (to be convinced), {催促|さいそく}する (to urge/press), {重複|ちょうふく}する (to overlap/duplicate)
- **Society/Change (2)**: {収束|しゅうそく}する (to converge/subside), {現実逃避|げんじつとうひ} (escapism)
- **Personality (3)**: {綺麗好|きれいず}き (fond of cleanliness), {飽|あ}き{性|しょう} (fickle nature), {巨匠|きょしょう} (great master)
- **Four-character compounds (2)**: {大胆不敵|だいたんふてき} (bold and fearless), {事実無根|じじつむこん} (completely groundless)
- **Expressions (4)**: {昔|むかし}ながら (traditional), {目|め}を{離|はな}す (to take one's eyes off), {胸|むね}が{高鳴|たかな}る (heart pounds), {楽|たの}しみにする (to look forward to)
- **Nature/Movement (3)**: うねり (swell/surge), {逃|に}げ{込|こ}む (to run into), {冬景色|ふゆげしき} (winter landscape)
- **Culture (2)**: {袱紗|ふくさ} (ceremonial cloth), {農園|のうえん} (farm/plantation)
- 24 candidates synced from candidate list; 3 new kanji added (紗, 綺, 袱)

Total entries: 26,594 → 26,618.

### 2026-05-05 (Vocabulary Expansion - 26 New Entries, Batch 91)
Added 26 new dictionary entries (IDs 26776-26801) from candidate_words.json. Focus on practical, broadly useful vocabulary across multiple categories.

- **Communication/Technology (3)**: {送信|そうしん}する (to send/transmit), {受信|じゅしん}する (to receive signal/message), {暗唱|あんしょう}する (to recite from memory)
- **People/Roles (5)**: {張本人|ちょうほんにん} (main culprit), {当人|とうにん} (person concerned), {第三者|だいさんしゃ} (third party), {黒子|くろこ} (stagehand/behind-the-scenes person), {仕立屋|したてや} (tailor)
- **Culture/Society (3)**: {応援団|おうえんだん} (cheering squad), {職人気質|しょくにんかたぎ} (artisan temperament), {頭|あたま}を{下|さ}げる (to bow/apologize)
- **Actions/Processes (5)**: {進行|しんこう}する (to progress), {衝突|しょうとつ}する (to collide/clash), {補正|ほせい}する (to correct/calibrate), {静止|せいし}する (to stand still), {忘却|ぼうきゃく}する (to forget completely)
- **Body/Health (2)**: {息遣|いきづか}い (breathing), {胃薬|いぐすり} (stomach medicine)
- **General (5)**: {何|なに}もかも (everything), {手助|てだす}けする (to help), {無防備|むぼうび}な (defenseless), {内向|うちむ}き (inward-looking), {外向|そとむ}き (outward-looking)
- **Science (1)**: {波動|はどう} (wave motion)
- **Transportation (1)**: {原付|げんつき} (moped)
- **Food (1)**: {調理|ちょうり}する (to cook/prepare food)
- 26 candidates synced from candidate list

Total entries: 26,568 → 26,594.

### 2026-05-04 (Vocabulary Expansion - 24 New Entries, Batch 90)
Added 24 new dictionary entries (IDs 26752-26775) from candidate_words.json. Vocabulary covers geography, culture, food, nature, language, military, performing arts, music, legal, and more.

- **Geography (3)**: {北|きた}アメリカ (North America), {南|みなみ}アメリカ (South America), カリブ{海|かい} (Caribbean Sea)
- **People/society (3)**: {陰謀者|いんぼうしゃ} (conspirator), {無能者|むのうしゃ} (incompetent person), ご{子息|しそく} (son — honorific)
- **Food (2)**: {塩干物|しおひもの} (salted dried fish), {干|ほ}し{果物|くだもの} (dried fruit)
- **Nature (3)**: {露水|つゆみず} (dew), {深|ふか}い{森|もり} (deep forest), {夏|なつ}の{終|お}わり (end of summer)
- **Performing arts (1)**: {女役|おんなやく} (female role)
- **Music (1)**: {佳曲|かきょく} (fine piece of music)
- **Military (1)**: {巡洋艦|じゅんようかん} (cruiser)
- **Legal (1)**: {罪犯|ざいはん} (criminal offense)
- **Formal/family (1)**: {公爵夫人|こうしゃくふじん} (duchess)
- **Time/literary (1)**: {昔年|せきねん} (former years)
- **Transportation (1)**: {中央駅|ちゅうおうえき} (central station)
- **Consolation/society (1)**: {慰問団|いもんだん} (consolation group)
- **Crafts/technical (1)**: {逆反|ぎゃくぞり}り (reverse warp)
- **Expressions (2)**: {爪|つめ}を{立|た}てる (to dig in nails), {影響|えいきょう}される (to be influenced)
- **Adjective (1)**: {颯快|さっかい} (brisk, refreshing)
- **Footprints (1)**: {歩跡|ほせき} (footprints, tracks)
- 23 candidates synced from candidate list

Total entries: 26,544 → 26,568.
Added 30 new dictionary entries (IDs 26702-26731) from candidate_words.json. Vocabulary covers shapes/math, product categories, education, transportation, culture/language, family, society, finance, stationery, and more.

- **Shapes/math (2)**: {六角|ろっかく} (hexagonal), {商|しょう} (quotient)
- **Product categories (3)**: {一般用|いっぱんよう} (for general use), {個人用|こじんよう} (for personal use), {農業用|のうぎょうよう} (for agricultural use)
- **Education (2)**: {男子学生|だんしがくせい} (male student), {非専門|ひせんもん} (non-specialist)
- **Transportation (1)**: {左車線|ひだりしゃせん} (left lane)
- **Culture/entertainment (2)**: {西洋映画|せいようえいが} (Western film), {文化週間|ぶんかしゅうかん} (Culture Week)
- **Language/writing (2)**: {和字|わじ} (Japanese-made characters), {罫線入|けいせんい}り (ruled/lined)
- **Law/politics (2)**: {国籍法|こくせきほう} (nationality law), {再就任|さいしゅうにん} (reappointment)
- **Society/people (4)**: {非常識人|ひじょうしきじん} (person lacking common sense), {貧困者|ひんこんしゃ} (person in poverty), {徘徊者|はいかいしゃ} (wanderer), {遭遇者|そうぐうしゃ} (witness/person who encounters)
- **Family (1)**: {恋女房|こいにょうぼう} (beloved wife)
- **Technology/daily life (2)**: フロアマップ (floor map), {画面|がめん}サイズ (screen size)
- **Finance (1)**: {残高証明|ざんだかしょうめい} (balance certificate)
- **Material (1)**: {天然皮革|てんねんひかく} (natural leather)
- **Work (2)**: {社外活動|しゃがいかつどう} (outside-company activities), {起用法|きようほう} (personnel deployment method)
- **Nature (1)**: {白々明|しらじらあ}ける (to dawn — literary)
- **Health (1)**: {放屁|ほうひ} (flatulence — formal)
- **Science (1)**: {結晶体|けっしょうたい} (crystalline body)
- **Quantity (1)**: {数冊|すうさつ} (several books)
- **Technology change (1)**: {精巧化|せいこうか} (increasing sophistication)
- 1 stale candidate removed (灰色 — duplicate of existing entry)
- 30 candidates synced from candidate list

Total entries: 26,494 → 26,524.

### 2026-05-04 (Vocabulary Expansion - 18 New Entries, Batch 87)
Added 18 new dictionary entries (IDs 26684-26701) from candidate_words.json. Diverse vocabulary covering description, environment, food/cooking, counters, daily life, entertainment, games, sports, technology, business, literature, and media.

- **Na-adjectives (2)**: {多発的|たはつてき} (frequent; repeated), {地球的|ちきゅうてき} (global; planetary)
- **Food/cooking (2)**: {副料理長|ふくりょうりちょう} (sous chef), すき{焼|や}き{鍋|なべ} (sukiyaki pot)
- **Daily life (2)**: ビニールシート (vinyl sheet/tarp), {床磨|ゆかみが}き (floor polishing)
- **Counter/question (1)**: {何個|なんこ} (how many small objects)
- **Entertainment (1)**: クラシック{映画|えいが} (classic film)
- **Games (1)**: {手番|てばん} (one's turn in a game)
- **Evaluation (1)**: {見外|みはず}れ (misjudgment; disappointment)
- **Consumer/tech (2)**: {最新|さいしん}モデル (latest model), タスク{管理|かんり} (task management)
- **Technology/business (1)**: データ{入力|にゅうりょく} (data entry)
- **Loanwords (2)**: ミドルエイジ (middle age), セービング (save in sports)
- **Literature/media (1)**: あとがたり (afterword; epilogue)
- **Sports (1)**: {真芯|ましん} (sweet spot)
- **Expression (1)**: すました{顔|かお} (composed/straight face)
- 1 stale candidate removed (duplicate of existing entry)
- 17 candidates synced from candidate list

Total entries: 26,476 → 26,494.

### 2026-05-04 (Vocabulary Expansion - 15 New Entries, Batch 86)
Added 15 new dictionary entries (IDs 26669-26683) from candidate_words.json. Diverse vocabulary covering language/writing, culture, daily life, science, geopolitics, sports, and body parts.

- **Language/writing (3)**: {行|ぎょう} (line/row of text), {愛称語|あいしょうご} (term of endearment), {片|かた} (one of a pair — prefix)
- **Culture/food (1)**: {三色団子|さんしょくだんご} (three-colored dango)
- **Daily life/community (1)**: {資源回収|しげんかいしゅう} (recyclable collection)
- **Politics/news (1)**: {投票数|とうひょうすう} (vote count)
- **Business (1)**: {卸売価格|おろしうりかかく} (wholesale price)
- **Science (1)**: {液体窒素|えきたいちっそ} (liquid nitrogen)
- **Pop culture (1)**: {火星人|かせいじん} (Martian)
- **Sports (1)**: {完封勝利|かんぷうしょうり} (shutout victory)
- **Geopolitics (1)**: {海洋国家|かいようこっか} (maritime nation)
- **Photography (1)**: {一眼|いちがん}カメラ (single-lens camera)
- **People (2)**: {援助者|えんじょしゃ} (aid worker), {異国人|いこくじん} (foreigner — literary)
- **Body part (1)**: {腓|こむら} (calf of the leg)
- 1 new kanji added to kanji index: 腓
- 15 candidates synced from candidate list

Total entries: 26,461 → 26,476.


_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
