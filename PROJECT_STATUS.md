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

### 2026-05-06 (Vocabulary Expansion - 25 New Entries, Batch 97)
Added 25 new dictionary entries (IDs 26961-26985) from candidate_words.json. Focus on practical, learner-useful vocabulary including compound verbs, suru-verbs, and culturally important nouns.

- **Compound Verbs (6)**: {紛|まぎ}れ{込|こ}む (to slip into), {着込|きこ}む (to bundle up), {噛|か}みつく (to bite/snap at), {覚|おぼ}え{込|こ}む (to memorize thoroughly), {飲|の}み{切|き}る (to drink up), {似|に}せる (to imitate)
- **Suru Verbs (5)**: {適応|てきおう}する (to adapt), {区別|くべつ}する (to distinguish), {継続|けいぞく}する (to continue), {一貫|いっかん}する (to be consistent), {表示|ひょうじ}する (to display)
- **Suru Verbs - other (2)**: {命中|めいちゅう}する (to hit the mark), パリッとする (to be crisp)
- **Expressions (1)**: {気|き}を{抜|ぬ}く (to let one's guard down)
- **Adverb (1)**: にわかに (suddenly)
- **Nouns - Emotion (2)**: {恐怖感|きょうふかん} (feeling of fear), {悪感情|あくかんじょう} (ill will)
- **Nouns - Food/Culture (2)**: {会席料理|かいせきりょうり} (kaiseki cuisine), おせち{料理|りょうり} (New Year's cuisine)
- **Nouns - Clothing (1)**: {重|かさ}ね{着|ぎ} (layering)
- **Nouns - Other (3)**: {推薦書|すいせんしょ} (letter of recommendation), {思考法|しこうほう} (way of thinking), {未成熟|みせいじゅく} (immature)
- **Other verbs (2)**: ざわつく (to be noisy/uneasy), {甘|あま}んじる (to resign oneself to)
- 25 candidates synced; 6 stale candidates removed

Total entries: 26,752 → 26,777.

### 2026-05-06 (Vocabulary Expansion - 20 New Entries, Batch 96)
Added 20 new dictionary entries (IDs 26941-26960) from candidate_words.json. Mixed vocabulary across food, daily life, culture, society, language, nature, and health.

- **Onomatopoeia/Texture (2)**: サクサクする (to be crispy), カリカリする (to be crispy/irritated)
- **Nature/Weather (2)**: ぬかるむ (to become muddy), {泥濘|でいねい} (muddy ground)
- **Food/Cooking (3)**: ツナ{缶|かん} (canned tuna), {割烹着|かっぽうぎ} (cooking smock), {割烹料理|かっぽうりょうり} (Japanese haute cuisine)
- **Daily Life/Housing (2)**: {電気料金|でんきりょうきん} (electricity bill), リフォームする (to renovate)
- **Society/Crime (2)**: {裏社会|うらしゃかい} (underworld), {犯罪組織|はんざいそしき} (criminal organization)
- **Language/Communication (2)**: {物申|ものもう}す (to speak up/protest), {戯言|ざれごと} (nonsense)
- **Grammar/Expressions (1)**: べからず (must not)
- **Medical (1)**: {胃潰瘍|いかいよう} (stomach ulcer)
- **Military (1)**: ミサイル (missile)
- **People/Character (1)**: {未熟者|みじゅくもの} (inexperienced person)
- **Agriculture (1)**: {干|ほ}し{草|くさ} (hay)
- **Welfare (1)**: {乳児院|にゅうじいん} (infant home)
- 19 candidates synced; 1 new kanji added (濘)

Total entries: 26,732 → 26,752.

### 2026-05-05 (Vocabulary Expansion - 30 New Entries, Batch 95)
Added 30 new dictionary entries (IDs 26911-26940) from candidate_words.json. Broad vocabulary covering daily life, society, culture, food, medicine, and personality.

- **Childcare/Education (2)**: {保育士|ほいくし} (nursery teacher), {託児所|たくじしょ} (daycare center)
- **Places (1)**: {大通|おおどお}り (main street)
- **Competition/Sports (1)**: {対戦|たいせん}する (to compete against)
- **Time/Manner (2)**: {唐突|とうとつ}に (abruptly), {早々|そうそう}に (promptly)
- **Technical/Design (2)**: {設計|せっけい}する (to design), {構文|こうぶん} (syntax)
- **Administrative (2)**: {転入|てんにゅう}する (to transfer in), {転出|てんしゅつ}する (to transfer out)
- **Adjectives (4)**: {地味|じみ}な (plain), {派手|はで}な (flashy), {不利|ふり}な (disadvantageous), {潔癖|けっぺき} (fastidious)
- **Abstract/Verbs (3)**: {調和|ちょうわ}する (to harmonize), {持続|じぞく}する (to sustain), {抗議|こうぎ}する (to protest)
- **Sound (1)**: {叫|さけ}び{声|ごえ} (scream)
- **Culture (1)**: {節句|せっく} (seasonal festival)
- **Food (1)**: ざるそば (cold soba noodles)
- **Academic (1)**: {引用|いんよう}する (to quote)
- **Discovery (1)**: {発見|はっけん}する (to discover)
- **Money (1)**: {先払|さきばら}い (advance payment)
- **Medical (2)**: {感染|かんせん}する (to be infected), {治癒|ちゆ}する (to heal)
- **People/Personality (3)**: {成功者|せいこうしゃ} (successful person), {皮肉屋|ひにくや} (cynic), {頑固者|がんこもの} (stubborn person)
- **Events (1)**: {閉会式|へいかいしき} (closing ceremony)
- **Expressions (1)**: {大切|たいせつ}にする (to cherish)
- 30 candidates synced from candidate list

Total entries: 26,702 → 26,732.

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

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
