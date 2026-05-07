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

### 2026-05-06 (Vocabulary Expansion - 22 New Entries, Batch 101)
Added 22 new dictionary entries (IDs 27063-27084) from candidate_words.json. Mix of abstract nouns, practical loanwords, and culturally interesting vocabulary.

- **Abstract nouns (心/力 compounds) (4)**: {競争心|きょうそうしん} (competitive spirit), {勝負心|しょうぶしん} (fighting spirit), {協調心|きょうちょうしん} (spirit of cooperation), {競争力|きょうそうりょく} (competitiveness)
- **Loanwords (8)**: ピンポン (ping-pong/doorbell), クレーン (crane), ペダル (pedal), タキシード (tuxedo), フルネーム (full name), ラック (rack), ギャング (gang), ブルーレイ (Blu-ray)
- **Business/Finance (3)**: {増資|ぞうし} (capital increase), {販売促進|はんばいそくしん} (sales promotion), リース (lease/wreath)
- **Appearance/Fashion (2)**: {髪色|かみいろ} (hair color), ヘアカラー (hair dye)
- **Daily life/Culture (3)**: {磯風|いそかぜ} (sea breeze), {竿竹|さおだけ} (bamboo pole), モーニング (morning set/morning coat)
- **Technology (2)**: ツイートする (to tweet), {受取証|うけとりしょう} (receipt)
- 22 candidates synced

Total entries: 26,854 → 26,876.

### 2026-05-06 (Vocabulary Expansion - 25 New Entries, Batch 100)
Added 25 new dictionary entries (IDs 27038-27062) from candidate_words.json. Diverse vocabulary across medical, cultural, legal, education, and daily life domains.

- **Medical/Health (3)**: {咳止|せきど}め (cough suppressant), {気管支炎|きかんしえん} (bronchitis), {発病|はつびょう}する (to fall ill)
- **Legal/Business (3)**: {商標権|しょうひょうけん} (trademark rights), {居住権|きょじゅうけん} (right of residence), {汚職事件|おしょくじけん} (corruption case)
- **Culture/Tradition (3)**: {生菓子|なまがし} (fresh Japanese sweets), {障子戸|しょうじど} (shoji door), {陰暦|いんれき} (lunar calendar)
- **Education (2)**: {全日制|ぜんにちせい} (full-time school), {夜間学校|やかんがっこう} (night school)
- **Food/Nature (2)**: {有機食品|ゆうきしょくひん} (organic food), {青草|あおくさ} (green grass)
- **Transportation (2)**: スクーター (scooter), {衝突事故|しょうとつじこ} (collision accident)
- **Descriptive/Abstract (3)**: {哲学的|てつがくてき} (philosophical), {無碍|むげ} (unhindered), {遠|とお}い{昔|むかし} (distant past)
- **People (2)**: {推薦者|すいせんしゃ} (recommender), {放火犯|ほうかはん} (arsonist)
- **Signs/Rules (1)**: {飲酒禁止|いんしゅきんし} (no drinking allowed)
- **Social (2)**: {例会|れいかい} (regular meeting), {飼育小屋|しいくごや} (animal shed)
- **Verbs (2)**: {晒|さら}け{出|だ}す (to lay bare), {詠唱|えいしょう}する (to chant)
- 25 candidates synced; 1 stale candidate removed

Total entries: 26,829 → 26,854.

### 2026-05-06 (Vocabulary Expansion - 25 New Entries, Batch 99)
Added 25 new dictionary entries (IDs 27013-27037) from candidate_words.json. Focus on practical vocabulary across finance, politics, health, culture, and daily life.

- **Finance/Business (4)**: {銀行口座|ぎんこうこうざ} (bank account), {当座預金|とうざよきん} (checking account), {貸金庫|かしきんこ} (safe deposit box), {零細企業|れいさいきぎょう} (micro enterprise)
- **Statistics/Economics (2)**: {増加率|ぞうかりつ} (rate of increase), {減少率|げんしょうりつ} (rate of decrease)
- **Politics/Government (1)**: {閣議決定|かくぎけってい} (cabinet decision)
- **Health/Medical (3)**: {発病|はつびょう} (onset of illness), {毒物|どくぶつ} (toxic substance), {毒薬|どくやく} (poisonous drug)
- **Education/Training (2)**: {講習会|こうしゅうかい} (training workshop), {悪筆|あくひつ} (bad handwriting)
- **Daily Life/Objects (2)**: {入|い}れ{物|もの} (container), {車間|しゃかん} (following distance)
- **Culture/Tradition (2)**: {箱庭|はこにわ} (miniature garden/sandbox game), {媒酌|ばいしゃく} (matchmaking)
- **Descriptive (5)**: {魅惑|みわく} (fascination), {無計画|むけいかく} (unplanned), {流行遅|りゅうこうおく}れ (out of fashion), {無味無臭|むみむしゅう} (tasteless/odorless), {無味乾燥|むみかんそう} (dull/dry)
- **Verbs (2)**: せびる (to pester for money), やみくも (reckless/blind)
- **Children/Pediatrics (1)**: {小児|しょうに} (child - medical term)
- **Place (1)**: {礼拝堂|らいはいどう} (chapel)
- 24 candidates synced; 23 stale candidates removed

Total entries: 26,804 → 26,829.

### 2026-05-06 (Vocabulary Expansion - 27 New Entries, Batch 98)
Added 27 new dictionary entries (IDs 26986-27012) from candidate_words.json. Focus on common suru verbs and useful loanwords for intermediate learners.

- **Business/Work (4)**: {出張|しゅっちょう}する (to go on a business trip), {倒産|とうさん}する (to go bankrupt), {請求|せいきゅう}する (to bill/demand), {委任|いにん}する (to delegate)
- **Action/Process (5)**: {設置|せっち}する (to install/establish), {発掘|はっくつ}する (to excavate/discover), {続行|ぞっこう}する (to continue/proceed), {休止|きゅうし}する (to suspend/pause), {先送|さきおく}りする (to postpone)
- **Society/Politics (3)**: {反発|はんぱつ}する (to oppose/rebound), {停滞|ていたい}する (to stagnate), {仲裁|ちゅうさい}する (to mediate)
- **Cognition/Emotion (2)**: {予知|よち}する (to predict), {楽観|らっかん}する (to be optimistic)
- **Life Events (2)**: {出産|しゅっさん}する (to give birth), {歓迎|かんげい}する (to welcome)
- **Quantity (1)**: {急増|きゅうぞう}する (to increase rapidly)
- **Clothing/Equipment (1)**: {着脱|ちゃくだつ}する (to attach/detach)
- **Loanwords (5)**: マニュアル (manual), ボリューム (volume), サイレン (siren), ロビー (lobby), フェンス (fence), アドレス (email address), オブジェ (art object)
- **Culture/Education (2)**: {年号|ねんごう} (era name), {文型|ぶんけい} (sentence pattern)
- 27 candidates synced from candidate list

Total entries: 26,777 → 26,804.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
