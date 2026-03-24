# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-23
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
| Total entries | ~18,813 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,014 (open) |
| Candidate words | ~5,347 |
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

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 490)
Added 35 new dictionary entries (IDs 19039-19073) from candidate_words.json.

- **Nouns (27)**: {石油|せきゆ}ストーブ (kerosene heater), {嬉|うれ}し{泣|な}き (crying for joy), {刻|きざ}み{葱|ねぎ} (chopped green onions), {一味唐辛子|いちみとうがらし} (ground chili pepper), {筆記試験|ひっきしけん} (written exam), {飲|の}み{薬|ぐすり} (oral medicine), {日|ひ}めくり (daily calendar), {米研|こめと}ぎ (rice washing), {折|お}り{返|かえ}し{地点|ちてん} (turnaround point), {手引|てび}き{書|しょ} (guidebook), {洗顔料|せんがんりょう} (facial cleanser), {借用語|しゃくようご} (loanword), {中南米|ちゅうなんべい} (Central/South America), {南半球|みなみはんきゅう} (Southern Hemisphere), {校外学習|こうがいがくしゅう} (field trip), {集団行動|しゅうだんこうどう} (group action), {商業地|しょうぎょうち} (commercial district), {原産国|げんさんこく} (country of origin), お{遍路|へんろ} (Shikoku pilgrimage), {脇|わき}の{下|した} (armpit), {月極駐車場|つきぎめちゅうしゃじょう} (monthly parking), {権威主義|けんいしゅぎ} (authoritarianism), {地方自治体|ちほうじちたい} (local government), {産業廃棄物|さんぎょうはいきぶつ} (industrial waste), {敏感肌|びんかんはだ} (sensitive skin), {留学費用|りゅうがくひよう} (study abroad expenses), {記述式|きじゅつしき} (essay-type test)
- **Nouns (legal/government, 2)**: {最高裁判所|さいこうさいばんしょ} (Supreme Court), {人事課|じんじか} (HR department)
- **Nouns (other, 2)**: {指揮官|しきかん} (commander), ぶどう{酒|しゅ} (wine)
- **Noun/Suru verb (1)**: {再就職|さいしゅうしょく} (re-employment)
- **Adverb (1)**: {一歩|いっぽ}ずつ (step by step)
- **Time noun (1)**: {前々日|ぜんぜんじつ} (two days before)
- **Expression (1)**: {異議|いぎ}を{唱|とな}える (to voice an objection)
- **Multi-sense entry**: お{遍路|へんろ} (2 senses: pilgrim / pilgrimage)
- Removed 1 stale candidate ({使|つか}い{走|ばし}り - already exists as entry)

Topics covered: food, daily life, geography, education, law/government, health/skincare, culture, work
Total entries: ~18,848 → ~18,883 (approximate)
Remaining candidates: ~5,312 → ~5,276 (35 removed as entries + 1 stale candidate removed)

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 489)
Added 35 new dictionary entries (IDs 19004-19038) from candidate_words.json.

- **Nouns (16)**: {前髪|まえがみ} (bangs/fringe), {新居|しんきょ} (new home), {専門知識|せんもんちしき} (expertise), {引換券|ひきかえけん} (exchange ticket), {生卵|なまたまご} (raw egg), {熱帯雨林|ねったいうりん} (tropical rainforest), {打|う}ち{上|あ}げ{花火|はなび} (aerial fireworks), {近距離|きんきょり} (short distance), {飼|か}い{犬|いぬ} (pet dog), バニラ (vanilla), {来場者|らいじょうしゃ} (visitor), {観光|かんこう}バス (tour bus), {夕空|ゆうぞら} (evening sky), {速球|そっきゅう} (fastball), {白星|しろぼし} (win), {黄金色|こがねいろ} (golden color)
- **Nouns/Suru verbs (7)**: {突撃|とつげき} (charge/assault), {動画配信|どうがはいしん} (video streaming), {傾聴|けいちょう} (active listening), {減少|げんしょう}する (to decrease), {礼装|れいそう} (formal dress), {押収|おうしゅう} (seizure), {相互理解|そうごりかい} (mutual understanding)
- **Na-adjective (1)**: {経験豊富|けいけんほうふ} (highly experienced)
- **Suru verbs (2)**: {魅了|みりょう}する (to fascinate), {想定|そうてい}する (to assume)
- **Noun (other, 5)**: {四六時中|しろくじちゅう} (around the clock - adverb), {新生活|しんせいかつ} (new life), {箱詰|はこづ}め (boxed), {中腹|ちゅうふく} (mountainside), {惨劇|さんげき} (tragedy)
- **Verbs (2)**: {真|ま}に{受|う}ける (to take at face value), {奪|うば}い{取|と}る (to snatch away)
- **Noun (1)**: {外車|がいしゃ} (foreign car), {天然|てんねん}ガス (natural gas)
- **Multi-sense entries**: {突撃|とつげき} (2 senses: military charge / surprise visit)

Topics covered: daily life, sports, food, nature, travel, media, law, communication
Total entries: ~18,813 → ~18,848 (approximate)
Remaining candidates: ~5,347 → ~5,312 (35 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 488)
Added 35 new dictionary entries (IDs 18969-19003) from candidate_words.json.

- **Nouns (11)**: {燃費|ねんぴ} (fuel efficiency), {時短|じたん} (time-saving), {節分|せつぶん} (Setsubun), {貯蓄|ちょちく} (savings), {終戦|しゅうせん} (end of war), {条項|じょうこう} (clause/provision), {品位|ひんい} (dignity), {横丁|よこちょう} (side street), {茶柱|ちゃばしら} (tea stalk - good omen), {複写|ふくしゃ} (copying), {未納|みのう} (unpaid)
- **Nouns with 2 senses (4)**: {戦力|せんりょく} (military strength / key player), {目録|もくろく} (catalog / gift list), {役柄|やくがら} (acting role / nature of position), {放火|ほうか} (arson)
- **Na-adjectives (3)**: {露骨|ろこつ} (blatant), {低俗|ていぞく} (vulgar), {卑猥|ひわい} (obscene)
- **I-adjectives (5)**: {手|て}ごわい (tough/formidable), {寝苦|ねぐる}しい (hard to sleep), {慎|つつま}ましい (modest/humble), {物悲|ものかな}しい (melancholy), {華々|はなばな}しい (splendid)
- **Suru verbs (8)**: {辞退|じたい}する (decline), {承諾|しょうだく}する (consent), {投稿|とうこう}する (post online), {拡散|かくさん}する (spread/go viral), {執行|しっこう} (enforcement), {向上|こうじょう}する (improve), {中断|ちゅうだん}する (interrupt), {操作|そうさ}する (operate/manipulate)
- **Noun/Suru verbs with legal domain (2)**: {共謀|きょうぼう} (conspiracy), {提訴|ていそ} (filing lawsuit)
- **Multi-sense entries**: {戦力|せんりょく} (2), {目録|もくろく} (2), {役柄|やくがら} (2), {投稿|とうこう}する (2), {拡散|かくさん}する (2), {操作|そうさ}する (2)
- New kanji added: 猥 (ID 02588)

Topics covered: law/legal, daily life, culture, media/technology, finance, food, weather, entertainment
Total entries: ~18,778 → ~18,813 (approximate)
Remaining candidates: ~5,382 → ~5,347 (35 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 487)
Added 35 new dictionary entries (IDs 18934-18968) from candidate_words.json.

- **Nouns (16)**: {霜降|しもふ}り (marbled meat), {泣|な}き{顔|がお} (tearful face), {格言|かくげん} (maxim), {出迎|でむか}え (greeting on arrival), {販売員|はんばいいん} (salesperson), {容貌|ようぼう} (facial features), {車線|しゃせん} (traffic lane), {依頼人|いらいにん} (client), {赤飯|せきはん} (red bean rice), {手錠|てじょう} (handcuffs), {証書|しょうしょ} (certificate), {水門|すいもん} (floodgate), {砂遊|すなあそ}び (sand play), {原材料|げんざいりょう} (raw materials), {笹|ささ}の{葉|は} (bamboo leaves), {格安航空会社|かくやすこうくうがいしゃ} (budget airline)
- **Nouns/Suru verbs (9)**: {断念|だんねん} (giving up), {力説|りきせつ} (emphasizing), {消去|しょうきょ} (deletion), {消灯|しょうとう} (lights out), {完済|かんさい} (full repayment), {熟慮|じゅくりょ} (deliberation), {羽化|うか} (insect emergence), {推理|すいり} (deduction), {尾行|びこう} (tailing)
- **Nouns (other, 5)**: {和製英語|わせいえいご} (Japanese-coined English), {屋内|おくない} (indoors), {完売|かんばい} (sold out), {書|か}き{換|か}え (rewriting), {発芽|はつが} (germination), {養鶏|ようけい} (poultry farming)
- **Na-adjective (2)**: {端麗|たんれい} (graceful), {野蛮|やばん} (barbaric)
- **I-adjective (1)**: {辛抱強|しんぼうづよ}い (patient)
- **Noun (culture, 1)**: {自動改札|じどうかいさつ} (automatic ticket gate)
- **Multi-sense entries**: {霜降|しもふ}り (2 senses), {書|か}き{換|か}え (2 senses)
- Removed 1 stale candidate (無頓着な - already exists as entry)

Topics covered: food/culture, crime/law, transport, nature, finance, daily life, language
Total entries: ~18,743 → ~18,778 (approximate)
Remaining candidates: ~5,418 → ~5,382 (35 removed as entries + 1 stale candidate removed)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 486)
Added 35 new dictionary entries (IDs 18899-18933) from candidate_words.json.

- **Nouns (15)**: {耳打|みみう}ち (whispering in ear), {麹|こうじ} (koji/malted rice), {透明感|とうめいかん} (transparency/clarity), {志望校|しぼうこう} (desired school), {審美眼|しんびがん} (aesthetic eye), {純利益|じゅんりえき} (net profit), お{汁粉|しるこ} (sweet red bean soup), {知的財産|ちてきざいさん} (intellectual property), {空|あ}き{瓶|びん} (empty bottle), {闇取引|やみとりひき} (black market deal), {日割|ひわ}り (daily rate), {香典返|こうでんがえ}し (condolence return gift), {不正解|ふせいかい} (incorrect answer), {赤|あか}ワイン (red wine), {在宅介護|ざいたくかいご} (home-based care)
- **Nouns/Suru verbs (9)**: {再発行|さいはっこう} (reissue), {縁取|ふちど}り (bordering/edging), {再構築|さいこうちく} (reconstruction), {暗譜|あんぷ} (memorizing music), {狙|ねら}い{撃|う}ち (sniping/targeting), {機嫌取|きげんと}り (currying favor), {籠城|ろうじょう} (holing up/siege), {価格改定|かかくかいてい} (price revision), {不法投棄|ふほうとうき} (illegal dumping)
- **Nouns (other)**: {据|す}え{置|お}き (leaving unchanged), シルエット (silhouette), {丸出|まるだ}し (fully exposed), {濃|こ}い{目|め} (on the strong side), {無断転載|むだんてんさい} (unauthorized reproduction), {今川焼|いまがわや}き (imagawayaki)
- **Expressions (3)**: {結局|けっきょく}のところ (in the end), {脇目|わきめ}も{振|ふ}らず (single-mindedly), {一寸先|いっすんさき}は{闇|やみ} (future is unpredictable)
- **Multi-sense entries**: {狙|ねら}い{撃|う}ち (2 senses), {籠城|ろうじょう} (2 senses)
- New kanji added: 鍾, 麹 (IDs 02586-02587)

Topics covered: food/drink, business/finance, education, law, culture, music, daily life
Total entries: ~18,708 → ~18,743 (approximate)
Remaining candidates: ~5,454 → ~5,418 (35 removed as entries + 1 stale candidate removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
