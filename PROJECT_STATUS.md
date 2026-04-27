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

### 2026-04-26 (Vocabulary Expansion - 30 New Entries, Batch 48)
Added 30 new dictionary entries (IDs 25696-25725) from candidate_words.json. Mixed batch covering business, culture, daily life, science, expressions, and social topics.

- **Nouns (16)**: {長期間|ちょうきかん} (long period), {新入|しんい}り (newcomer), {温度計|おんどけい} (thermometer), {広告主|こうこくぬし} (advertiser), {広告料|こうこくりょう} (ad revenue), {銀河系|ぎんがけい} (Milky Way), {新興企業|しんこうきぎょう} (startup), {倍速|ばいそく} (double speed), {紳士服|しんしふく} (menswear), {運動着|うんどうぎ} (sportswear), {内縁|ないえん} (common-law marriage), {省力|しょうりょく} (labor-saving), {死亡率|しぼうりつ} (mortality rate), {探査機|たんさき} (probe), {別邸|べってい} (villa), {鮮魚店|せんぎょてん} (fish shop)
- **Suru verbs (5)**: {転出|てんしゅつ}する (moving out), {拉致|らち}する (to abduct), {吸引|きゅういん}する (to suction), {近道|ちかみち}する (to take a shortcut), {東奔西走|とうほんせいそう}する (to rush about)
- **Expressions (2)**: {懐|ふところ}が{深|ふか}い (broad-minded), {器|うつわ}が{大|おお}きい (magnanimous)
- **Other (7)**: {外人|がいじん} (foreigner), {貧富|ひんぷ}の{差|さ} (wealth gap), {天運|てんうん} (fate), {無思慮|むしりょ} (thoughtlessness), ホスト (host), {敏捷性|びんしょうせい} (agility), ホラー{映画|えいが} (horror movie)
- Conjugation tables auto-generated for 5 suru verb entries
- 1 new kanji (拉) assigned to kanji index
- 30 candidates synced from candidate list

Total entries: 25,488 → 25,518.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
