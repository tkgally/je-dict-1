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
| Total entries | ~18,778 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,979 (open) |
| Candidate words | ~5,382 |
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

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 484)
Added 35 new dictionary entries (IDs 18829-18863) from candidate_words.json.

- **Interjection (1)**: いらっしゃいませ (welcome)
- **Nouns (12)**: {仕事場|しごとば} (workplace), {煮付|につ}け (simmered dish), {代休|だいきゅう} (compensatory day off), {入社式|にゅうしゃしき} (company entrance ceremony), {食器洗|しょっきあら}い (dishwashing), {閉塞感|へいそくかん} (sense of stagnation), {震|ふる}え (shiver/tremor), {飢餓|きが} (hunger/famine), {個人情報|こじんじょうほう} (personal information), お{知|し}らせ (notice), {証人|しょうにん} (witness), {入門書|にゅうもんしょ} (introductory book)
- **Nouns/Suru verbs (7)**: {紛失|ふんしつ}する (to lose), {悪化|あっか}する (to worsen), {封鎖|ふうさ} (blockade), {増設|ぞうせつ} (expansion), {習得|しゅうとく}する (to master), {自滅|じめつ} (self-destruction), {閉館|へいかん} (closing of facility)
- **Nouns/Suru verbs (2)**: {休館|きゅうかん} (temporary closure), {処方薬|しょほうやく} (prescription medicine)
- **Na-adjectives (2)**: {簡明|かんめい} (concise and clear), ちぐはぐ (mismatched)
- **Godan verbs (2)**: {飲|の}み{交|か}わす (to drink together), {後|あと}ずさる (to back away)
- **Adverb (1)**: {即刻|そっこく} (immediately)
- **Expressions (5)**: {夢中|むちゅう}になる (to become absorbed), {目|め}が{合|あ}う (to make eye contact), {目|め}をそむける (to avert one's eyes), どうしようもない (helpless/hopeless), {失敬|しっけい} (rude/excuse me)
- **Other nouns (3)**: {流|なが}し (kitchen sink/cruising taxi), {星占|ほしうらな}い (horoscope), {郷里|きょうり} (hometown)
- **Multi-sense entries**: {失敬|しっけい} (2), {流|なが}し (2), どうしようもない (2), {閉館|へいかん} (2)

Total entries: ~18,638 → ~18,673 (approximate)
Remaining candidates: ~5,524 → ~5,489 (35 removed as entries)

### 2026-03-23 (Vocabulary Expansion - 35 New Entries, Session 483)
Added 35 new dictionary entries (IDs 18794-18828) from candidate_words.json.

- **Nouns (16)**: {横顔|よこがお} (profile/side view), {麻薬|まやく} (narcotic), {特価|とっか} (special price), {不作|ふさく} (bad harvest), {車種|しゃしゅ} (car model), {四隅|よすみ} (four corners), {初霜|はつしも} (first frost), {品数|しなかず} (number of items), {機内|きない} (inside aircraft), {中期|ちゅうき} (mid-term), {神殿|しんでん} (temple), {身柄|みがら} (custody), {強権|きょうけん} (authoritative power), {縦縞|たてじま} (vertical stripes), {横縞|よこじま} (horizontal stripes)
- **Nouns/Suru verbs (8)**: {伝播|でんぱ} (propagation), {占拠|せんきょ} (occupation/seizure), {免職|めんしょく} (dismissal from post), {謹慎|きんしん} (suspension), {記帳|きちょう} (bookkeeping), {引率|いんそつ} (leading a group), {敬愛|けいあい} (respect and affection), {調剤|ちょうざい} (dispensing medicine), {自生|じせい} (growing wild), {完勝|かんしょう} (complete victory)
- **Nouns/Na-adjective/Suru verb (1)**: {無心|むしん} (innocence/absorption/begging)
- **Na-adjective (2)**: {辛口|からくち} (dry/spicy/harsh), {立体|りったい} (three-dimensional), {貧相|ひんそう} (poor-looking)
- **Other (2)**: {空咳|からせき} (dry cough), {遅番|おそばん} (late shift), {渋面|じゅうめん} (grimace), {体面|たいめん} (honor/prestige), あざ (bruise/birthmark)
- **Multi-sense entries**: {辛口|からくち} (3), {無心|むしん} (3), {空咳|からせき} (2), {横顔|よこがお} (2), {麻薬|まやく} (2), {立体|りったい} (2), {謹慎|きんしん} (2), {記帳|きちょう} (2), あざ (2)
- **Paired entries**: {縦縞|たてじま}/{横縞|よこじま}, {完勝|かんしょう}/{完敗|かんぱい}

Total entries: ~18,603 → ~18,638 (approximate)
Remaining candidates: ~5,559 → ~5,524 (35 removed as entries)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
