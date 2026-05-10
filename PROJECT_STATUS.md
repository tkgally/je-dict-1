# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-05-10
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

### 2026-05-10 (Vocabulary Expansion - 15 New Entries, Internal-Completeness "seen in entry" Batch)
Added 15 new dictionary entries (IDs 27349-27363) from candidate_words.json, all flagged as "seen in entry" candidates — words that already appeared in existing entries' examples or notes but had no entry of their own. Filling these closes internal-completeness gaps so cross-references can resolve.

- **Volcano / disaster (3)**: {噴火口|ふんかこう} (volcanic crater/vent), {大噴火|だいふんか} (major eruption — noun + suru-verb), {見舞|みま}われる (to be struck by — passive verb of misfortune)
- **Workplace / business (2)**: {部外|ぶがい} (outside the department; in {部外者|ぶがいしゃ}, {部外秘|ぶがいひ}), {銀行印|ぎんこういん} (bank-registered personal seal)
- **Education (1)**: {教習|きょうしゅう} (instruction, esp. driving school)
- **Culture / music (1)**: {雅楽|ががく} (gagaku, traditional Japanese court music)
- **Time (1)**: {月|つき}{半|なか}ば (middle of the month)
- **Math (1)**: {小数|しょうすう} (decimal number — distinct from homophone {少数|しょうすう} "minority")
- **Astronomy (2)**: {自転|じてん} (rotation on its own axis), {公転|こうてん} (orbital revolution) — cross-referenced as a contrast pair
- **Weather / atmosphere (1)**: {気流|きりゅう} (air current; in {乱気流|らんきりゅう} "turbulence")
- **Health statistics (1)**: {患者数|かんじゃすう} (number of patients)
- **Building / HVAC (2)**: {空調|くうちょう} (air conditioning, HVAC), {通気|つうき} (passive ventilation, breathability)
- 15 candidates synced (removed from candidate list)
- All 15 entries pass validation; 5 verbs received conjugation tables (4 suru + 1 ichidan); no new kanji introduced

Total entries: 27,140 → 27,155.

### 2026-05-09 (Vocabulary Expansion - 20 New Entries, Internal-Completeness "seen in entry" Batch)
Added 20 new dictionary entries (IDs 27329-27348) from candidate_words.json, all flagged as "seen in entry" candidates — words that already appeared in existing entries' examples or notes but had no entry of their own. Filling these closes internal-completeness gaps.

- **Slang / people (1)**: バツニ (divorced twice — slang sibling of バツイチ)
- **Sports / leisure (4)**: ベンチプレス (bench press), フォアボール (baseball walk / base on balls), スリーボール (3-ball count), ツーストライク (2-strike count)
- **Clothing (2)**: カウボーイハット (cowboy hat), ウェディングドレス (wedding dress)
- **Transportation / leisure (1)**: {手漕|てこ}ぎ (rowing by hand; rowboat-related)
- **Kanji-radical names (2)**: てへん ({扌|てへん} hand radical), くさかんむり ({艹|くさかんむり} grass-crown radical)
- **Food (3)**: パルメザンチーズ (Parmesan cheese), チーズフォンデュ (cheese fondue), デザートメニュー (dessert menu)
- **Conjunctions (2)**: だけども (but, more emphatic variant of だけど), だけれど (but, slightly more formal than だけど)
- **Counters / coins (3)**: {円玉|えんだま} (yen coin, used after a denomination), {二歩|にほ} (two steps; also the shogi nifu foul), {何歩|なんぽ} (how many steps)
- **Technical (2)**: {符号化|ふごうか} (encoding — math/computing/info-theory term), {句読符号|くとうふごう} (punctuation marks — formal collective term)
- 1 stale candidate removed (たち, kana variant of existing entry 01551 達/たち); 20 candidates synced
- All 20 entries pass validation; 1 suru-verb received conjugation table; no new kanji introduced

Total entries: 27,120 → 27,140.

### 2026-05-09 (Vocabulary Expansion - 46 New Entries, Internal-Completeness Batch)
Added 46 new dictionary entries (IDs 27283-27328) from candidate_words.json. Prioritized "seen in entry" candidates — words referenced by existing entries' examples or notes but not yet defined. This closes internal-completeness gaps and lets cross-references resolve correctly.

- **Verbs (3)**: {余|あま}す (to leave over — transitive pair of {余|あま}る), {凹|へこ}ます (to dent / dishearten — transitive of {凹|へこ}む), {響|ひび}かせる (to make resound — transitive of {響|ひび}く)
- **Suru-verbs / nouns (3)**: ドレスアップ (dressing up), ホームステイ (homestay), {治水|ちすい} (flood control)
- **Na-adjective (1)**: {地理的|ちりてき} (geographical)
- **Adverb / noun (1)**: {通常|つうじょう} (normally; the regular state)
- **Sports / leisure (8)**: バッター (batter), ダッグアウト (dugout), サッカーボール (soccer ball), カウボーイ (cowboy), プレイボーイ (playboy), ボーイフレンド (boyfriend), ボーイスカウト (Boy Scouts), {開会式|かいかいしき} (opening ceremony)
- **Transportation (6)**: モーターボート (motorboat), ゴムボート (rubber dinghy), カヤック (kayak), サイドブレーキ (parking brake), フットブレーキ (foot brake), エンジンブレーキ (engine braking)
- **Cards / shapes (2)**: ハート (heart — shape, suit, mental strength), スペード (spade — card suit)
- **Food (4)**: クリームチーズ (cream cheese), ナチュラルチーズ (natural cheese), チーズバーガー (cheeseburger), タルト (tart)
- **Clothing (4)**: ダウンコート (down coat), ダウンジャケット (down jacket), ドレスコード (dress code), ペンダント (pendant)
- **Building / home (4)**: {理容院|りよういん} (barbershop), マイホーム (one's own home), {墓石|ぼせき} (gravestone), ボストンバッグ (Boston bag)
- **Tools / objects (3)**: コイル (electrical coil), ノブ (knob), {頬紅|ほほべに} (blush)
- **Communication / events (2)**: ドアチャイム (door chime), {時報|じほう} (time signal)
- **Other (4)**: バイオリニスト (violinist), {古銭|こせん} (old coin), {暴風雪|ぼうふうせつ} (blizzard), {普段使|ふだんづか}い (everyday use), {彫|ほ}り{物|もの} (carving / tattoo)
- 46 candidates synced (removed from candidate list)
- All 46 entries pass validation; 6 verbs received conjugation tables; no new kanji introduced

Total entries: 27,074 → 27,120.

### 2026-05-08 (Vocabulary Expansion - 22 New Entries, Batch 109)
Added 22 new dictionary entries (IDs 27261-27282) from candidate_words.json. Focused on culturally significant concepts, useful expressions, and practical vocabulary for intermediate learners.

- **Expressions (3)**: お{待|ま}たせ (sorry for the wait), {楽|らく}にする (to relax/make easy), {表|おもて}に{出|だ}す (to bring to light/expose)
- **Cultural (2)**: もてなし (hospitality), {趣味|しゅみ}{嗜好|しこう} (tastes and preferences)
- **Business/Formal (3)**: {経営|けいえい}{破綻|はたん} (business failure), {膠着|こうちゃく}{状態|じょうたい} (stalemate), {消除|しょうじょ}する (to eliminate/remove)
- **Travel/Transport (3)**: {出張先|しゅっちょうさき} (business trip destination), {乗車口|じょうしゃぐち} (boarding entrance), {個人|こじん}{旅行|りょこう} (independent travel)
- **Nature/Place (1)**: {向|む}こう{岸|ぎし} (far shore)
- **Food/Drink (2)**: そば{粉|こ} (buckwheat flour), {無味|むみ} (tastelessness)
- **Health/Medical (2)**: {快癒|かいゆ} (recovery/healing), {色素|しきそ}{沈着|ちんちゃく} (pigmentation)
- **Daily Life (3)**: {埃|ほこり}まみれ (covered in dust), お{姉|ねえ}ちゃん (older sister, informal), {換気口|かんきこう} (ventilation opening)
- **Other (3)**: {先導者|せんどうしゃ} (leader/guide), フラッシュバック (flashback), {名言集|めいげんしゅう} (book of quotations)

Total entries: 27,052 → 27,074.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 107)
### 2026-05-08 (Vocabulary Expansion - 30 New Entries, Batch 108)
Added 30 new dictionary entries (IDs 27231-27260) from candidate_words.json. Mix of culturally significant concepts, practical vocabulary, adverbs, and compound nouns for intermediate learners.

- **Cultural/Psychology (2)**: {甘|あま}え (dependence on indulgence), {学者肌|がくしゃはだ} (scholarly temperament)
- **Adverbs/Expressions (8)**: {永遠|えいえん}に (forever), {永久|えいきゅう}に (permanently), こうやって (like this), どこにも (nowhere/everywhere), {自然|しぜん}に (naturally), {無料|むりょう}で (for free), {十分|じゅうぶん}に (sufficiently), なかなかない (rare/hard to find)
- **Work/Business (3)**: {情報|じょうほう}{収集|しゅうしゅう} (information gathering), {職歴書|しょくれきしょ} (resume/CV), {登録済|とうろくず}み (registered)
- **Status/Condition (3)**: {完了済|かんりょうず}み (completed), {耐|た}えられない (unbearable), {普通|ふつう}でない (unusual)
- **Body/Posture (2)**: {身構|みがま}え (defensive stance), {前傾姿勢|ぜんけいしせい} (forward-leaning posture)
- **Food/Culture (1)**: {回転焼|かいてんや}き (regional name for imagawayaki)
- **Science/Education (3)**: {天王星|てんのうせい} (Uranus), {消化液|しょうかえき} (digestive fluid), {就学前|しゅうがくまえ} (preschool age)
- **Places/Things (4)**: {中央部|ちゅうおうぶ} (central part), {映写機|えいしゃき} (projector), {宝物庫|ほうもつこ} (treasure house), {現像所|げんぞうじょ} (photo developing lab)
- **Society (3)**: {無関心|むかんしん}さ (indifference), {口|くち}コミ{評判|ひょうばん} (word-of-mouth reputation), {農繁期|のうはんき} (busy farming season)
- **Other (1)**: {眠|ねむ}りにつく (to fall asleep)

Total entries: 27,022 → 27,052.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 107)
Added 30 new dictionary entries (IDs 27201-27230) targeting common words missing from the dictionary. Focus on culturally rich vocabulary, useful expressions, and everyday concepts for intermediate learners.

- **Infrastructure/Nature (3)**: {信号機|しんごうき} (traffic light), {大潮|おおしお} (spring tide), {蓮|はす} (lotus)
- **Crime/Law (4)**: {脅迫|きょうはく} (threat/intimidation), {脅|おど}す (to threaten), {恐喝|きょうかつ} (blackmail/extortion), {恩赦|おんしゃ} (amnesty/pardon)
- **Education (1)**: {課外|かがい} (extracurricular)
- **Time (1)**: {宵|よい} (evening/early night)
- **Health (1)**: {水虫|みずむし} (athlete's foot)
- **Personality/Character (5)**: お{人好|ひとよ}し (pushover), {下心|したごころ} (ulterior motive), {魂胆|こんたん} (scheme), {思|おも}い{上|あ}がり (arrogance), {鵜呑|うの}み (accepting uncritically)
- **Actions/Behavior (4)**: {横取|よこど}り (snatching), つまみ{食|ぐ}い (sneaking a taste), {居留守|いるす} (pretending to be out), {居候|いそうろう} (freeloading)
- **Expressions/Proverbs (3)**: {水|みず}の{泡|あわ} (all for nothing), {身|み}から{出|で}た{錆|さび} (reaping what you sow), しっぺ{返|がえ}し (retaliation)
- **Daily Life/General (8)**: {手違|てちが}い (mix-up), {見切|みき}る (to give up on), {行|い}き{当|あ}たりばったり (haphazard), {豆知識|まめちしき} (trivia), {口火|くちび} (trigger/spark), {引|ひ}き{延|の}ばし (stalling), {見当外|けんとうはず}れ (off the mark), {丸腰|まるごし} (unarmed/unprepared)

Total entries: 26,992 → 27,022.

### 2026-05-07 (Vocabulary Expansion - 20 New Entries, Batch 106)
Added 20 new dictionary entries (IDs 27181-27200) from candidate_words.json. Mix of workplace, weather, news, food, cultural, and daily life vocabulary.

- **Workplace/Business (5)**: {無給休暇|むきゅうきゅうか} (unpaid leave), {臨時会議|りんじかいぎ} (emergency meeting), {定期会議|ていきかいぎ} (regular meeting), {内部情報|ないぶじょうほう} (insider information), {経済効果|けいざいこうか} (economic effect)
- **Weather (3)**: {雷雲|らいうん} (thundercloud), {積乱雲|せきらんうん} (cumulonimbus), {秋雨前線|あきさめぜんせん} (autumn rain front)
- **News/Disaster (2)**: {死傷者|ししょうしゃ} (casualties), {爆風|ばくふう} (blast wind)
- **People/Culture (3)**: {創始者|そうししゃ} (founder), {口伝|くちづて} (word of mouth), {経済大国|けいざいたいこく} (economic superpower)
- **Expressions/Verbs (2)**: {格好|かっこう}つける (to show off), {声|こえ}が{枯|か}れる (to become hoarse)
- **Description (1)**: {最重要|さいじゅうよう} (most important)
- **Daily Life (3)**: {向|む}かい{合|あ}わせ (facing each other), {防火扉|ぼうかとびら} (fire door), {野菜料理|やさいりょうり} (vegetable dish)
- **Education (1)**: {学校制度|がっこうせいど} (school system)
- 2 stale candidates removed; 20 candidates synced

Total entries: 26,972 → 26,992.

### 2026-05-07 (Vocabulary Expansion - 22 New Entries, Batch 104)
Added 22 new dictionary entries (IDs 27141-27162) from candidate_words.json. Diverse vocabulary covering geography, law, arts, nature, linguistics, and abstract concepts.

- **Geography/Nature (2)**: {祖国|そこく} (homeland), {湖面|こめん} (lake surface)
- **Animals (2)**: {雄鹿|おじか} (stag), {雌鹿|めじか} (doe)
- **Law/Politics (2)**: {罰則|ばっそく} (penal provisions), {非暴力|ひぼうりょく} (nonviolence)
- **Arts (1)**: {油彩|ゆさい} (oil painting)
- **Linguistics/Education (2)**: {旧字体|きゅうじたい} (old-form kanji), {新字体|しんじたい} (new-form kanji)
- **Abstract/Formal (5)**: {錯誤|さくご} (error), {贈与|ぞうよ} (gift/donation), {取捨|しゅしゃ} (selection), {困苦|こんく} (hardship), {無策|むさく} (lack of policy)
- **Culture/Sports (2)**: {構|かま}え (stance/posture), {稽古場|けいこば} (practice hall)
- **Science/Technical (2)**: {気泡|きほう} (air bubble), {波形|はけい} (waveform)
- **Description (2)**: まだら (mottled/spotted), {無毒|むどく} (nontoxic)
- **Plants (1)**: {果樹|かじゅ} (fruit tree)
- **Honorific (1)**: {閣下|かっか} (Your Excellency)
- 22 candidates synced

Total entries: 26,932 → 26,954.

### 2026-05-07 (Vocabulary Expansion - 17 New Entries, Batch 105)
Added 17 new dictionary entries (IDs 27163-27180) from candidate_words.json. Mix of useful vocabulary spanning adverbs, na-adjectives, cultural terms, and formal/academic nouns.

- **Adverb (1)**: {一|ひと}つ{一|ひと}つ (one by one)
- **Na-adjectives (5)**: {通俗的|つうぞくてき} (popular/lowbrow), {組織的|そしきてき} (organized), {実際的|じっさいてき} (practical), {習慣的|しゅうかんてき} (habitual), {非効率的|ひこうりつてき} (inefficient), {地域的|ちいきてき} (regional)
- **Cultural/Food (2)**: {大判焼|おおばんや}き (filled cake), {粋人|すいじん} (sophisticate)
- **Language/Linguistics (2)**: {定型句|ていけいく} (set phrase), {美化語|びかご} (beautifying language)
- **Emotion/Social (2)**: {敵対心|てきたいしん} (hostility), {障害者|しょうがいしゃ} (person with disability)
- **Formal/News (2)**: {負傷者|ふしょうしゃ} (injured person), {諸条件|しょじょうけん} (various conditions)
- **Other (2)**: せどり (retail arbitrage), {突破力|とっぱりょく} (breakthrough ability), {可動式|かどうしき} (movable type)
- 1 stale candidate removed (均一化する — already existed)
- 18 candidates synced

Total entries: 26,954 → 26,972.

### 2026-05-07 (Vocabulary Expansion - 30 New Entries, Batch 103)
Added 30 new dictionary entries (IDs 27111-27140) from candidate_words.json. Diverse vocabulary covering cultural terms, daily life, food, travel, and workplace vocabulary.

- **Verbs (2)**: {華|はな}やぐ (to brighten/become festive), {掘|ほ}り{出|だ}す (to dig out/discover)
- **Food/Cooking (4)**: {焼|や}き{方|かた} (way of grilling), {魚市場|うおいちば} (fish market), {厚焼|あつや}き (thick omelette), {和食屋|わしょくや} (Japanese restaurant)
- **Culture/Religion (4)**: {戦国|せんごく} (warring states), {口伝|くでん} (oral tradition), {慰霊祭|いれいさい} (memorial service), {作務|さむ} (temple work)
- **People/Society (3)**: {学友|がくゆう} (school friend), {文筆家|ぶんぴつか} (writer), {草食系|そうしょくけい} (passive/herbivore type)
- **Work/Business (4)**: {係員|かかりいん} (attendant), {経歴書|けいれきしょ} (CV/resume), {配達先|はいたつさき} (delivery destination), {文章化|ぶんしょうか} (putting into writing)
- **Travel/Places (3)**: {途中下車|とちゅうげしゃ} (stopover), {展望所|てんぼうじょ} (viewing platform), {再入国|さいにゅうこく} (re-entry)
- **Daily life (3)**: {常備|じょうび} (keeping on hand), {遅寝|おそね} (going to bed late), {閲覧室|えつらんしつ} (reading room)
- **Communication/Language (2)**: {発話|はつわ} (speech/utterance), {対比的|たいひてき} (contrasting)
- **Description (3)**: {局地的|きょくちてき} (localized), {美文字|びもじ} (beautiful handwriting), {普及率|ふきゅうりつ} (adoption rate)
- **Other (2)**: {似顔|にがお} (likeness/portrait), {焼|や}き{印|いん} (branding mark)
- 29 candidates synced

Total entries: 26,902 → 26,932.

### 2026-05-07 (Vocabulary Expansion - 26 New Entries, Batch 102)
Added 26 new dictionary entries (IDs 27085-27110) from candidate_words.json. Focus on broadly useful vocabulary for intermediate learners: everyday expressions, cultural terms, and workplace vocabulary.

- **Adverb/Onomatopoeia (1)**: こつこつ (steadily; with tapping sound)
- **Expressions (3)**: {昔々|むかしむかし} (once upon a time), {上|うえ}から{目線|めせん} (condescending attitude), {取|と}るに{足|た}らない (insignificant)
- **Workplace/Business (3)**: {辞表|じひょう} (resignation letter), {勤務形態|きんむけいたい} (work arrangement), {準備不足|じゅんびぶそく} (lack of preparation)
- **Pronoun (1)**: {自分自身|じぶんじしん} (oneself)
- **Texture/Sensory (1)**: ざらつく (to feel rough)
- **Health/Body (1)**: {血色|けっしょく} (complexion)
- **Geography/Nature (2)**: {沼地|ぬまち} (swamp), {村落|そんらく} (village)
- **Military/News (2)**: {銃撃|じゅうげき} (shooting), {隊列|たいれつ} (formation)
- **Education (1)**: {短期大学|たんきだいがく} (junior college)
- **Life/Society (2)**: {身辺整理|しんぺんせいり} (putting affairs in order), {福音|ふくいん} (gospel/good news)
- **Culture (3)**: {五月人形|ごがつにんぎょう} (Boys' Day doll), ゲームセンター (arcade), {無法|むほう} (lawless)
- **Abstract (2)**: {才覚|さいかく} (resourcefulness), {潔|いさぎよ}さ (integrity)
- **Technology (1)**: インストールする (to install)
- **Psychology (1)**: {心的外傷|しんてきがいしょう} (psychological trauma)
- 20 stale duplicate candidates removed; 26 candidates synced

Total entries: 26,876 → 26,902.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
