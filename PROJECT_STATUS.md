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

### 2026-04-26 (Vocabulary Expansion - 30 New Entries, Batch 47)
Added 30 new dictionary entries (IDs 25666-25695) from candidate_words.json. Practical, learner-friendly vocabulary covering daily life, business, environment, sports, food, and communication.

- **Daily life (7)**: {雨降|あめふ}り (rainfall), へこみ (dent/setback), {抜|ぬ}け{毛|げ} (hair loss), {空|あ}き{時間|じかん} (free time), {早歩|はやある}き (brisk walking), シャーペン (mechanical pencil), フロントガラス (windshield)
- **Time/intensity (3)**: {今|いま}すぐ (right now), {急上昇|きゅうじょうしょう} (sharp rise), {急降下|きゅうこうか} (sharp drop)
- **Business/society (6)**: {前金|まえきん} (advance payment), {離席|りせき}する (to step away), {危機|きき}{管理|かんり} (crisis management), {社会|しゃかい}{問題|もんだい} (social problem), {誘致|ゆうち} (attraction/bidding), {連絡係|れんらくがかり} (liaison)
- **Loanwords (5)**: ジェスチャー (gesture), セロリ (celery), リユース (reuse), カヌー (canoe), トラブルメーカー (troublemaker)
- **Other (9)**: {先回|さきまわ}り (preemption), {全速力|ぜんそくりょく} (full speed), {分|わ}け{前|まえ} (share/portion), ビジネスホテル (business hotel), {大中小|だいちゅうしょう} (L/M/S), {強|つよ}さ (strength), {寄付者|きふしゃ} (donor), {仲間|なかま}{意識|いしき} (camaraderie), {守勢|しゅせい} (defensive)
- Conjugation tables auto-generated for 7 suru verb entries
- 30 candidates synced from candidate list

Total entries: 25,458 → 25,488.

### 2026-04-26 (Vocabulary Expansion - 20 New Entries, Batch 46)
Added 20 new dictionary entries (IDs 25646-25665) from candidate_words.json. Mixed batch covering Japanese culture, everyday expressions, business/economics, food/drink, sports, and daily life.

- **Cultural (3)**: {天下|あまくだ}り (amakudari - bureaucratic parachuting), {純米酒|じゅんまいしゅ} (pure rice sake), {大吟醸|だいぎんじょう} (premium ginjo sake)
- **Expressions (3)**: {目|め}を{合|あ}わせる (to make eye contact), {好|す}き{放題|ほうだい} (doing as one pleases), そのままにする (to leave as is)
- **Business/Economics (4)**: {銀行|ぎんこう}{振込|ふりこみ} (bank transfer), {占有率|せんゆうりつ} (market share), {輸出国|ゆしゅつこく} (exporting country), {輸入国|ゆにゅうこく} (importing country)
- **Nouns (6)**: {準々決勝|じゅんじゅんけっしょう} (quarterfinal), {猿芝居|さるしばい} (transparent sham), {工場長|こうじょうちょう} (factory manager), {肉片|にくへん} (piece of meat), {中米|ちゅうべい} (Central America), {拭|ふ}き{取|と}り (wiping off)
- **Verb (1)**: {苛立|いらだ}たせる (to irritate)
- **Other (3)**: {遊歩|ゆうほ} (strolling), ポロシャツ (polo shirt), {満々|まんまん} (brimming with)
- Conjugation tables auto-generated for 4 verb entries (2 ichidan, 2 suru)
- 20 candidates synced from candidate list

Total entries: 25,438 → 25,458.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
