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

### 2026-04-28 (Vocabulary Expansion - 28 New Entries, Batch 55)
Added 28 new dictionary entries (IDs 25903-25930) from candidate_words.json. Diverse batch of expressions, cultural vocabulary, and descriptive terms useful for intermediate learners.

- **Expressions (8)**: {今日|きょう}このごろ (these days), {余|あま}すところなく (completely), {期待|きたい}に{満|み}ちる (full of anticipation), {苦虫|にがむし}を{噛|か}み{潰|つぶ}したよう (looking sour), {目|め}に{遭|あ}う (to suffer), これより (from this point on), ジロリと{見|み}る (to glare), ぴんぴんしている (lively and well)
- **Na-adjectives (2)**: {誘惑|ゆうわく}{的|てき} (tempting/seductive), {肉感|にっかん}{的|てき} (voluptuous)
- **Nouns (12)**: {周|まわ}り{中|じゅう} (all around), {秘密|ひみつ}{主義|しゅぎ} (secretiveness), {大|だい}{音響|おんきょう} (loud sound), {読|よ}み{飛|と}ばし (skimming), {小物|こもの}{入|い}れ (accessory case), {伝送|でんそう} (transmission), {御|お}{祝儀|しゅうぎ}{袋|ぶくろ} (gift envelope), {括弧|かっこ}{書|が}き (parenthetical), {預言者|よげんしゃ} (prophet), {原稿料|げんこうりょう} (manuscript fee), {金銀|きんぎん}{財宝|ざいほう} (gold and treasure), {溺死|できし} (drowning), {機嫌|きげん}{屋|や} (moody person), {五十代|ごじゅうだい} (one's fifties), {高級|こうきゅう}{料亭|りょうてい} (high-class restaurant), {脚線美|きゃくせんび} (beautiful legs)
- **Pronoun (1)**: あの{人|ひと} (that person; he/she)
- **Verb (1)**: {引|ひ}きずられる (to be dragged/swayed)
- Conjugation tables auto-generated for 4 verb entries (2 suru, 1 ichidan, 1 godan)
- Removed 2 stale candidates (出す duplicate, 世渡り下手 variant reading)
- 27 candidates synced from candidate list

Total entries: 25,695 → 25,723.

### 2026-04-28 (Vocabulary Expansion - 24 New Entries, Batch 54)
Added 24 new dictionary entries (IDs 25879-25902) from candidate_words.json. Focused batch of na-adjectives (～的な), katakana loanwords, and other useful vocabulary for intermediate learners.

- **Na-adjectives with 的 (10)**: {感動的|かんどうてき}な (moving), {挑戦的|ちょうせんてき}な (challenging/defiant), {戦略的|せんりゃくてき}な (strategic), {魅惑的|みわくてき}な (enchanting), {都会的|とかいてき}な (urban/sophisticated), {敵対的|てきたいてき}な (hostile), {創作的|そうさくてき}な (creative), {空想的|くうそうてき}な (fantastical), {反発的|はんぱつてき}な (defiant), {反逆的|はんぎゃくてき}な (rebellious), {肉感的|にくかんてき}な (voluptuous)
- **Katakana loanwords (8)**: ハンマー (hammer), タイマー (timer), ドキュメント (document), トリック (trick), ネイル (nail art), ストライク (strike), バジル (basil), チーズケーキ (cheesecake), フック (hook), ポインター (pointer)
- **Other (3)**: {名門校|めいもんこう} (prestigious school), どっちも (both, informal), やり{出|だ}す (to start doing)
- Conjugation table auto-generated for 1 godan verb entry
- 13 candidates synced from candidate list

Total entries: 25,671 → 25,695.

### 2026-04-27 (Vocabulary Expansion - 28 New Entries, Batch 53)
Added 28 new dictionary entries (IDs 25831-25858) from candidate_words.json. Focused batch of expressions, verbs, and cultural vocabulary useful for intermediate learners.

- **Social expressions (8)**: {気|き}を{遣|つか}う (to be considerate), {席|せき}を{外|はず}す (to step away), {顔|かお}を{立|た}てる (to save face), {恩|おん}を{売|う}る (to put someone in one's debt), {手|て}を{借|か}りる (to get help), {当|あ}てにする (to count on), {気|き}が{済|す}む (to be satisfied), お{茶|ちゃ}を{濁|にご}す (to be evasive)
- **Verbs (5)**: {引|ひ}き{戻|もど}す (to pull back), おもねる (to flatter), {思|おも}いやる (to empathize), しくじる (to fail/blunder), あやかる (to share in good fortune)
- **Expressions/adverbs (7)**: {思|おも}い{通|どお}り (as one wishes), {思|おも}うがまま (as one pleases), いかにして (how; by what means), たかが (merely; at most), そぐわない (to not suit), {腑|ふ}に{落|お}ちない (to not make sense), {身|み}を{乗|の}り{出|だ}す (to lean forward eagerly)
- **Cultural (3)**: {心|こころ}を{無|む}にする (to clear one's mind), {物心|ものごころ}つく (to reach age of awareness), {故郷|こきょう}を{離|はな}れる (to leave hometown)
- **Nouns (3)**: {滞留|たいりゅう} (stagnation/lingering), {傍点|ぼうてん} (emphasis dots), {目障|めざわ}り (eyesore)
- **Other (2)**: ぐずぐずする (to dawdle), {頭|あたま}を{柔|やわ}らかくする (to think flexibly)
- Conjugation tables auto-generated for 7 verb entries (5 godan, 2 suru)
- Removed 1 stale candidate (残存/ざんそん, variant of existing ざんぞん entry)
- 11 candidates synced from candidate list

Total entries: 25,623 → 25,651.

### 2026-04-27 (Vocabulary Expansion - 30 New Entries, Batch 52)
Added 30 new dictionary entries (IDs 25801-25830) from candidate_words.json. Diverse batch covering everyday expressions, postal/legal terminology, cultural vocabulary, and practical nouns.

- **Onomatopoeia/expressions (3)**: ワクワクする (to be excited), きちんとする (to be neat/proper), あくびをする (to yawn)
- **Education (3)**: {語学学校|ごがくがっこう} (language school), {日本語教育|にほんごきょういく} (Japanese language education), コミュニケーション{能力|のうりょく} (communication skills)
- **Postal services (3)**: {書留郵便|かきとめゆうびん} (registered mail), {普通郵便|ふつうゆうびん} (regular mail), {配達証明|はいたつしょうめい} (proof of delivery)
- **Legal (4)**: {民事責任|みんじせきにん} (civil liability), {刑事責任|けいじせきにん} (criminal liability), {法的義務|ほうてきぎむ} (legal obligation), {弾劾裁判|だんがいさいばん} (impeachment trial)
- **Buildings/places (3)**: {葬儀場|そうぎじょう} (funeral hall), {別宅|べったく} (second residence), {別荘地|べっそうち} (resort area)
- **Other (14)**: {運動能力|うんどうのうりょく} (athletic ability), {凍害|とうがい} (frost damage), {秘術|ひじゅつ} (secret technique), イナゴ (locust), {決算報告|けっさんほうこく} (financial report), {報復行為|ほうふくこうい} (retaliation), {演習曲|えんしゅうきょく} (étude), {熱狂者|ねっきょうしゃ} (fanatic), {秘書室|ひしょしつ} (secretarial office), {卵料理|たまごりょうり} (egg dish), {申込用紙|もうしこみようし} (application form), {誘惑|ゆうわく}に{負|ま}ける (to give in to temptation), {燕雀|えんじゃく} (swallows and sparrows), {若奥様|わかおくさま} (young wife)
- Conjugation tables auto-generated for 4 verb entries (3 suru, 1 ichidan)
- 30 candidates synced from candidate list

Total entries: 25,593 → 25,623.

### 2026-04-27 (Vocabulary Expansion - 25 New Entries, Batch 51)
Added 25 new dictionary entries (IDs 25776-25800) from candidate_words.json. Diverse batch covering cultural vocabulary, everyday expressions, academic terms, and practical nouns.

- **Expressions (5)**: {返答|へんとう}に{困|こま}る (at a loss for an answer), {工夫|くふう}を{重|かさ}ねる (make repeated efforts), {迎|むか}えに{行|い}く (go pick someone up), {紙一重|かみひとえ}の{差|さ} (paper-thin difference), {踏|ふ}み{台|だい}にする (use as a stepping stone)
- **Cultural (3)**: {出世魚|しゅっせうお} (fish with growth-stage names), {謎|なぞ}かけ (riddle/wordplay), {参上|さんじょう}する (arrive, humble/dramatic)
- **Academic/statistics (3)**: {中央値|ちゅうおうち} (median), {最高点|さいこうてん} (highest score), {最低点|さいていてん} (lowest score)
- **Personality/evaluation (3)**: {勝手|かって}{気|き}まま (selfish/self-indulgent), {分不相応|ぶんふそうおう} (beyond one's means), {裏切|うらぎ}り{者|もの} (traitor)
- **Nouns (8)**: {遅咲|おそざ}き (late bloomer), {錯乱|さくらん} (derangement), {慣用語|かんようご} (idiom), {一人客|ひとりきゃく} (solo customer), {割引|わりびき}{価格|かかく} (discounted price), {飲食品|いんしょくひん} (food and drink), {略装|りゃくそう} (informal dress), {宿代|やどだい} (lodging fee)
- **Other (3)**: {意識|いしき}{喪失|そうしつ} (loss of consciousness), {資源国|しげんこく} (resource-rich country), {本流|ほんりゅう} (mainstream)
- Conjugation tables auto-generated for 2 suru verb entries
- Removed 20 stale candidates (duplicates of existing entries)
- 24 candidates synced from candidate list

Total entries: 25,568 → 25,593.

### 2026-04-27 (Vocabulary Expansion - 20 New Entries, Batch 50)
Added 20 new dictionary entries (IDs 25756-25775) from candidate_words.json. Mixed batch covering language/culture, daily life, food, society/law, and military/politics.

- **Na-adjectives (2)**: {幻想的|げんそうてき} (fantastical), {依存的|いそんてき} (dependent)
- **Food (2)**: コーヒー{豆|まめ} (coffee beans), カスタード (custard)
- **Culture/language (3)**: {筆記体|ひっきたい} (cursive script), ヒット{曲|きょく} (hit song), {全集中|ぜんしゅうちゅう} (full concentration)
- **Society/law (4)**: {死亡届|しぼうとどけ} (death notification), {売春|ばいしゅん} (prostitution), {災害対策|さいがいたいさく} (disaster measures), {駐留|ちゅうりゅう}する (to station troops)
- **Daily life (4)**: {近日中|きんじつちゅう} (in the near future), {破|やぶ}れ (tear/rip), {整体院|せいたいいん} (bodywork clinic), {旅行客|りょこうきゃく} (traveler)
- **Other (5)**: {弾力性|だんりょくせい} (elasticity), {年月日|ねんがっぴ} (date), {燕尾服|えんびふく} (tailcoat), {弾丸列車|だんがんれっしゃ} (bullet train), {猿山|さるやま} (monkey hill)
- Conjugation table auto-generated for 1 suru verb entry
- 20 candidates synced from candidate list

Total entries: 25,548 → 25,568.

### 2026-04-27 (Vocabulary Expansion - 30 New Entries, Batch 49)
Added 30 new dictionary entries (IDs 25726-25755) from candidate_words.json. Mixed batch covering daily life, culture, sports, household items, clothing, and practical vocabulary.

- **Household/clothing (5)**: {衣装棚|いしょうだな} (wardrobe), ハンガーラック (clothes rack), フード{付|つ}き (hooded), {防寒服|ぼうかんふく} (cold-weather clothing), {夜着|よぎ} (padded sleeping kimono)
- **Sports/leisure (4)**: {攻守交代|こうしゅこうたい} (change of sides), {判定|はんてい}ミス (bad call), スケート{場|じょう} (skating rink), アイススケート (ice skating)
- **Tools/technology (4)**: カッターナイフ (utility knife), {開閉|かいへい}ボタン (open/close button), {活動量計|かつどうりょうけい} (activity tracker), {回転灯|かいてんとう} (rotating light)
- **Culture (3)**: {前厄|まえやく} (pre-calamity year), {後厄|あとやく} (post-calamity year), {休耕田|きゅうこうでん} (fallow rice field)
- **Academic/news (4)**: {学会誌|がっかいし} (academic journal), {防衛力|ぼうえいりょく} (defensive capability), {防御線|ぼうぎょせん} (line of defense), {副専攻|ふくせんこう} (academic minor)
- **General (10)**: {怖|こわ}がらせる (to frighten), {一部分|いちぶぶん} (a part), {反応的|はんのうてき} (reactive), {密集地|みっしゅうち} (densely populated area), {旅行鞄|りょこうかばん} (travel bag), ミラー (mirror), ニキビ{跡|あと} (acne scar), インソール (insole), {財布入|さいふい}れ (wallet case), {糸巻|いとま}き (spool)
- Conjugation tables auto-generated for 2 verb entries (1 ichidan, 1 suru)
- 1 new kanji (鞄) assigned to kanji index
- 30 candidates synced from candidate list

Total entries: 25,518 → 25,548.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
