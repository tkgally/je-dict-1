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

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 485)
Added 35 new dictionary entries (IDs 18864-18898) from candidate_words.json.

- **Nouns (18)**: {価格|かかく}{設定|せってい} (pricing), {志望|しぼう}{動機|どうき} (reason for applying), {書類|しょるい}{作成|さくせい} (document preparation), {標準|ひょうじゅん}{時|じ} (standard time), {予定|よてい}{変更|へんこう} (change of plans), {地球|ちきゅう}{温暖|おんだん}{化|か} (global warming), {異常|いじょう}{気象|きしょう} (abnormal weather), {派遣|はけん}{社員|しゃいん} (temporary worker), {月|げっ}{会費|かいひ} (monthly fee), {購読|こうどく}{料|りょう} (subscription fee), {固定|こてい}{給|きゅう} (fixed salary), {成果|せいか}{主義|しゅぎ} (meritocracy), {捉|とら}え{方|かた} (way of perceiving), {重|じゅう}{労働|ろうどう} (heavy labor), {緩衝|かんしょう}{材|ざい} (cushioning material), {段|だん}ボール (cardboard), {自宅|じたく}{待機|たいき} (staying at home), {再生|さいせい}{回数|かいすう} (view count)
- **Nouns/Suru verbs (5)**: {汚名|おめい}{返上|へんじょう} (clearing one's name), {指名|しめい}{手配|てはい} (wanted list), {在宅|ざいたく}ワーク (remote work), {人道|じんどう}{支援|しえん} (humanitarian aid), {捜査|そうさ}{当局|とうきょく} (investigative authorities)
- **Noun/Na-adjective (2)**: {意地|いじ}っ{張|ぱ}り (stubbornness), {一本調子|いっぽんちょうし} (monotone)
- **Nouns - specialized (5)**: {在留|ざいりゅう}{資格|しかく} (residence status), {法的|ほうてき}{手段|しゅだん} (legal measures), {学歴|がくれき}{社会|しゃかい} (credential society), {社会|しゃかい}{保険|ほけん} (social insurance), {縄文|じょうもん}{時代|じだい} (Jomon period)
- **Other nouns (2)**: {新古品|しんこひん} (like-new second-hand), {在宅|ざいたく}ワーク (WFH)
- **Expressions (3)**: {機嫌|きげん}を{損|そこ}ねる (to offend), {振|ふ}り{出|だ}しに{戻|もど}る (back to square one), {器|うつわ}が{小|ちい}さい (small-minded)
- **Multi-sense entry**: {息|いき}を{吹|ふ}き{返|かえ}す (2 senses - literal/figurative revival)

Topics covered: business/work, environment, law, society, daily life, history
Total entries: ~18,673 → ~18,708 (approximate)
Remaining candidates: ~5,489 → ~5,454 (35 removed as entries + 1 stale candidate removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
