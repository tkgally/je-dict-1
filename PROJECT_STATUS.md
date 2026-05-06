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

### 2026-05-05 (Vocabulary Expansion - 30 New Entries, Batch 93)
Added 30 new dictionary entries (IDs 26826-26855) from candidate_words.json. Focus on common suru verbs and useful vocabulary for intermediate learners.

- **Starting/Ending (3)**: {開始|かいし}する (to commence), {解除|かいじょ}する (to cancel/lift), {短縮|たんしゅく}する (to shorten)
- **Safety/Emergency (3)**: {避難|ひなん}する (to evacuate), {脱出|だっしゅつ}する (to escape), {救出|きゅうしゅつ}する (to rescue)
- **Communication/Cognition (6)**: {提示|ていじ}する (to present), {指示|しじ}する (to instruct), {解釈|かいしゃく}する (to interpret), {解明|かいめい}する (to clarify), {推理|すいり}する (to deduce), {発音|はつおん}する (to pronounce)
- **Law/Authority (2)**: {逮捕|たいほ}する (to arrest), {命令|めいれい}する (to command)
- **Interpersonal (3)**: {配慮|はいりょ}する (to be considerate), {訪問|ほうもん}する (to visit), {援助|えんじょ}する (to assist)
- **Daily Life (4)**: {散歩|さんぽ}する (to take a walk), {外出|がいしゅつ}する (to go out), {着用|ちゃくよう}する (to wear), {記憶|きおく}する (to memorize)
- **Business/Society (4)**: {改善|かいぜん}する (to improve), {重視|じゅうし}する (to emphasize), {滞在|たいざい}する (to stay), {転売|てんばい}する (to resell)
- **Emotions/Description (3)**: {爆笑|ばくしょう}する (to burst out laughing), {馬鹿|ばか}げる (to be ridiculous), {未練|みれん}がましい (clingy)
- **Other (2)**: {賑|にぎ}わい (bustle/prosperity), {豪華|ごうか}な (luxurious)
- 30 candidates synced from candidate list

Total entries: 26,618 → 26,648.

### 2026-05-05 (Vocabulary Expansion - 24 New Entries, Batch 92)
Added 24 new dictionary entries (IDs 26802-26825) from candidate_words.json. Focus on high-utility general vocabulary for intermediate learners.

- **Food/Sensation (2)**: さっぱりする (to feel refreshed), こってりする (to be rich/heavy in flavor)
- **Commerce/Daily Life (3)**: {取|と}り{寄|よ}せる (to order from afar), {常連客|じょうれんきゃく} (regular customer), {後片付|あとかたづ}け (cleanup after activity)
- **Communication/Cognition (3)**: {納得|なっとく}する (to be convinced), {催促|さいそく}する (to urge/press), {重複|ちょうふく}する (to overlap/duplicate)
- **Society/Change (2)**: {収束|しゅうそく}する (to converge/subside), {現実逃避|げんじつとうひ} (escapism)
- **Personality (3)**: {綺麗好|きれいず}き (fond of cleanliness), {飽|あ}き{性|しょう} (fickle nature), {巨匠|きょしょう} (great master)
- **Four-character compounds (2)**: {大胆不敵|だいたんふてき} (bold and fearless), {事実無根|じじつむこん} (completely groundless)
- **Expressions (4)**: {昔|むかし}ながら (traditional), {目|め}を{離|はな}す (to take one's eyes off), {胸|むね}が{高鳴|たかな}る (heart pounds), {楽|たの}しみにする (to look forward to)
- **Nature/Movement (3)**: うねり (swell/surge), {逃|に}げ{込|こ}む (to run into), {冬景色|ふゆげしき} (winter landscape)
- **Culture (2)**: {袱紗|ふくさ} (ceremonial cloth), {農園|のうえん} (farm/plantation)
- 24 candidates synced from candidate list; 3 new kanji added (紗, 綺, 袱)

Total entries: 26,594 → 26,618.


_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
