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

### 2026-04-22 (Vocabulary Expansion - 25 New Entries, Batch 25)
Added 25 new dictionary entries (IDs 25037-25061) from candidate_words.json. Mixed batch covering daily life, culture, history, business, science, economics, and expressions.

- **Daily life (3)**: キッチンペーパー (kitchen paper towel), {必携品|ひっけいひん} (essential item), {美顔|びがん} (facial beauty/care)
- **Business / work (3)**: {進行役|しんこうやく} (facilitator/moderator), {繁盛期|はんじょうき} (peak season), サービス{出勤|しゅっきん} (unpaid work attendance)
- **Culture / history (3)**: {百獣|ひゃくじゅう} (all beasts), {廓|くるわ} (pleasure quarter/castle bailey), {一寸|いっすん} (one sun measurement)
- **Science / technology (3)**: {周波数|しゅうはすう} (frequency), {無生物|むせいぶつ} (inanimate object), {再設定|さいせってい} (resetting)
- **Economics / general (3)**: インフレーション (inflation), その{他|た} (others/the rest), {介在|かいざい} (mediation/intervention)
- **Expressions / literary (2)**: {胸|むね}がきゅんとする (heart flutter), よすが (means of support/keepsake)
- **Education (1)**: {女子学生|じょしがくせい} (female student)
- **Transport (1)**: {乗合|のりあい}バス (public bus)
- **Agriculture (1)**: {輪作|りんさく} (crop rotation)
- **Religion (1)**: イスラム{教|きょう} (Islam)
- **Military (1)**: {手榴弾|しゅりゅうだん} (hand grenade)
- **Multi-sense entries (3)**: {上|あ}がり (3 senses), {廓|くるわ} (2 senses), {絵札|えふだ} (2 senses), よすが (2 senses)
- Conjugation tables auto-generated for 5 suru verb entries
- 2 new kanji added to index: 廓, 榴
- 25 candidates synced from candidate list

Total entries: 24,834 → 24,859.

### 2026-04-22 (Vocabulary Expansion - 20 New Entries, Batch 24)
Added 20 new dictionary entries (IDs 25017-25036) from candidate_words.json. Mixed batch covering expressions, loanwords, food, sports, daily life, science, and business vocabulary.

- **Expressions (3)**: どちらかというと (if anything/rather), {影響|えいきょう}を{受|う}ける (to be influenced), {再々|さいさい} (again and again)
- **Loanwords / daily life (4)**: エントリーシート (job application form), チェックリスト (checklist), コンディショナー (hair conditioner), ウェットティッシュ (wet wipe)
- **Food / dining (2)**: {計量|けいりょう}カップ (measuring cup), {刺身盛|さしみも}り (sashimi platter)
- **Onomatopoeia (1)**: ぽこぽこ (bubbling; one after another)
- **Sports (1)**: {内野手|ないやしゅ} (infielder)
- **Science / technology (2)**: {化合物|かごうぶつ} (chemical compound), データ{解析|かいせき} (data analysis)
- **Business / administration (3)**: {名称変更|めいしょうへんこう} (name change), {募集期間|ぼしゅうきかん} (application period), {予約受付|よやくうけつけ} (reservation reception)
- **Shopping (1)**: {購入予約|こうにゅうよやく} (pre-order)
- **Transport / education (2)**: {進路変更|しんろへんこう} (change of course), {車線規制|しゃせんきせい} (lane restriction)
- **Exploration (1)**: {探検隊|たんけんたい} (expedition)
- Conjugation tables auto-generated for 4 suru verb entries
- 3 stale candidates removed (duplicates of existing entries)
- 20 candidates synced from candidate list

Total entries: 24,814 → 24,834.

### 2026-04-22 (Vocabulary Expansion - 24 New Entries, Batch 23)
Added 24 new dictionary entries (IDs 24993-25016) from candidate_words.json. Mixed batch covering culture, religion, history, nature, daily life, textiles, and body vocabulary.

- **Culture / religion (4)**: {阿弥陀|あみだ} (Amitabha Buddha), {仏殿|ぶつでん} (Buddha hall), {本厄|ほんやく} (main unlucky year), {叙勲|じょくん} (conferring decorations)
- **History (2)**: {平氏|へいし} (Taira clan), {太夫|たゆう} (tayuu/courtesan/performer)
- **Nature / weather (3)**: {虻|あぶ} (horsefly), {風浪|ふうろう} (wind-driven waves), {湖上|こじょう} (on the lake)
- **Daily life / food (3)**: ペーパータオル (paper towel), チューインガム (chewing gum), ニュース{速報|そくほう} (breaking news)
- **Textiles (2)**: {表地|おもてじ} (outer fabric), {裏布|うらぬの} (lining cloth)
- **Body / health (2)**: しもやけ (chilblains), {脇毛|わきげ} (armpit hair)
- **Sports / fitness (1)**: {柔軟体操|じゅうなんたいそう} (stretching exercises)
- **Finance (1)**: {株券|かぶけん} (stock certificate)
- **Material (2)**: {銅板|どうばん} (copper plate), {車軸|しゃじく} (axle)
- **Abstract / personality (2)**: {軽|かる}さ (lightness), {吝嗇|りんしょく} (stinginess)
- **Conversation (1)**: ではでは (well then/goodbye)
- **Supernatural (1)**: {背後霊|はいごれい} (guardian spirit)
- Conjugation tables auto-generated for 1 suru verb entry
- 2 new kanji added to index: 叙, 陀
- 24 candidates synced, 1 stale candidate removed (空言 からごと, variant of existing そらごと entry)

Total entries: 24,790 → 24,814.

### 2026-04-22 (Vocabulary Expansion - 30 New Entries, Batch 22)
Added 30 new dictionary entries (IDs 24963-24992) from candidate_words.json. Diverse batch covering culture, food, science, professions, language, and daily life vocabulary.

- **Culture / religion (5)**: {一寸法師|いっすんぼうし} (Issun-bōshi folk tale), {禰宜|ねぎ} (Shinto priest), {仏具|ぶつぐ} (Buddhist altar fittings), {義侠心|ぎきょうしん} (chivalrous spirit), {融通無碍|ゆうずうむげ} (unhindered flexibility)
- **Food / cooking (3)**: {粕汁|かすじる} (sake lees soup), {餅粉|もちこ} (glutinous rice flour), {莢|さや} (pod/shell)
- **Science / tech (3)**: {不活性|ふかっせい} (inertness), {伝導|でんどう} (conduction), {梅雨前線|つゆぜんせん} (seasonal rain front)
- **Professions / government (3)**: {建築士|けんちくし} (architect), {補佐官|ほさかん} (aide/adviser), {乗員|じょういん} (crew member)
- **Arts / craft (3)**: {彫金|ちょうきん} (metal engraving), {活版|かっぱん} (letterpress), {幻術|げんじゅつ} (illusionism)
- **Language / reference (2)**: {見出|みだ}し{語|ご} (headword/lemma), {客観視|きゃっかんし} (objective viewpoint)
- **Body / description (1)**: {中肉中背|ちゅうにくちゅうせい} (medium build)
- **Housing (1)**: {床下|ゆかした} (under the floor)
- **Education / society (3)**: {受験料|じゅけんりょう} (exam fee), {共同生活|きょうどうせいかつ} (communal living), {席次|せきじ} (seating order)
- **Expressions / abstract (3)**: {若気の至り|わかげのいたり} (youthful indiscretion), {無二|むに} (peerless), {深考|しんこう} (deep thought)
- **History / military (2)**: {兵営|へいえい} (barracks), {通話中|つうわちゅう} (on a call)
- Conjugation tables auto-generated for 5 suru verb entries
- 3 new kanji added to index: 碍, 禰, 莢
- 30 candidates synced from candidate list

Total entries: 24,760 → 24,790.

### 2026-04-21 (Vocabulary Expansion - 25 New Entries, Batch 21)
Added 25 new dictionary entries (IDs 24938-24962) from candidate_words.json. Thematic batch covering health/medical, daily life/travel, Japan-specific culture, business/legal, and technical vocabulary.

- **Health / medical (3)**: {禁断症状|きんだんしょうじょう} (withdrawal symptoms), {予防医療|よぼういりょう} (preventive medicine), {姿勢矯正|しせいきょうせい} (posture correction)
- **Daily life / travel (5)**: {電話予約|でんわよやく} (phone reservation), {荷物置|にもつお}き{場|ば} (luggage storage area), クーポン{券|けん} (coupon), グリーン{券|けん} (green car ticket), {貴重品入|きちょうひんい}れ (valuables locker)
- **Japan-specific culture (4)**: {耐震設計|たいしんせっけい} (earthquake-resistant design), {精進弁当|しょうじんべんとう} (vegetarian bento), {山葵漬|わさびづ}け (wasabi pickles), {襖紙|ふすまがみ} (fusuma paper)
- **Business / legal (5)**: {提携店|ていけいてん} (partner store), {子会社化|こがいしゃか} (subsidiarization), {被選挙権|ひせんきょけん} (right to run for office), {除籍|じょせき} (removal from register), {私文書|しぶんしょ} (private document)
- **Technical / practical (3)**: {予備電源|よびでんげん} (backup power source), {手信号|てしんごう} (hand signal), {耐震強度|たいしんきょうど} (seismic strength)
- **Other (5)**: {連載終了|れんさいしゅうりょう} (end of serialization), {奇妙|きみょう}さ (strangeness), {努力給|どりょくきゅう} (effort-based pay), {限定免許|げんていめんきょ} (restricted license), {旧校舎|きゅうこうしゃ} (old school building)
- 25 candidates synced from candidate list

Total entries: 24,735 → 24,760.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
