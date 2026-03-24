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

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 492)
Added 35 new dictionary entries (IDs 19109-19143) from candidate_words.json.

- **Nouns (17)**: {冷|ひ}や{汗|あせ} (cold sweat), {得票|とくひょう} (votes obtained), {隣国|りんごく} (neighboring country), {開票|かいひょう} (ballot counting), {海抜|かいばつ} (above sea level), {前方|ぜんぽう} (front/forward), {後方|こうほう} (rear/behind), パンフレット (pamphlet), {諸説|しょせつ} (various theories), {夕闇|ゆうやみ} (evening darkness), お{姫様|ひめさま} (princess), {登山道|とざんどう} (mountain trail), {夕凪|ゆうなぎ} (evening calm), {遺書|いしょ} (will/testament), {身|み}の{上話|うえばなし} (life story), {博愛|はくあい} (philanthropy), {大将|たいしょう} (general/boss)
- **Nouns/Suru verbs (5)**: {審議|しんぎ} (deliberation), {放任|ほうにん} (laissez-faire), {急展開|きゅうてんかい} (sudden development), {拘泥|こうでい} (fixation), {甘受|かんじゅ} (acceptance)
- **Nouns/Na-adjectives (5)**: {切|き}れ{味|あじ} (sharpness), {少|すく}なめ (somewhat less), {安上|やすあ}がり (inexpensive), {軽量|けいりょう} (lightweight), {泥|どろ}まみれ (covered in mud)
- **Na-adjective (1)**: {安直|あんちょく} (cheap/simplistic)
- **Adjective-no (1)**: {無農薬|むのうやく} (pesticide-free)
- **I-adjectives (2)**: {途方|とほう}もない (extraordinary), {親|した}しみやすい (approachable)
- **Nouns (seasonal, 2)**: {冬休|ふゆやす}み (winter break), {春休|はるやす}み (spring break)
- **Other (2)**: {行|い}きつけ (regular place), {説法|せっぽう} (sermon/preaching)
- **Multi-sense entries**: {切|き}れ{味|あじ} (2), {安直|あんちょく} (2), {遺書|いしょ} (2), お{姫様|ひめさま} (2), {大将|たいしょう} (2), {途方|とほう}もない (2), {説法|せっぽう} (2)
- Removed 1 stale candidate ({問屋|どんや} - variant reading of existing {問屋|とんや} entry)

Topics covered: politics, nature, geography, food, daily life, culture, emotions, language
Total entries: ~18,918 → ~18,953 (approximate)
Remaining candidates: ~5,241 → ~5,205 (35 removed as entries + 1 stale candidate removed)

### 2026-03-24 (Vocabulary Expansion - 35 New Entries, Session 491)
Added 35 new dictionary entries (IDs 19074-19108) from candidate_words.json.

- **Nouns (15)**: {刑務所|けいむしょ} (prison), {研究所|けんきゅうじょ} (research institute), {上下関係|じょうげかんけい} (hierarchical relationship), {猛毒|もうどく} (deadly poison), {有力者|ゆうりょくしゃ} (influential person), {化石燃料|かせきねんりょう} (fossil fuel), {利|き}き{手|て} (dominant hand), {陸軍|りくぐん} (army), {立|た}ち{退|の}き (eviction), {我|わ}が{身|み} (oneself), {野犬|やけん} (stray dog), {万事|ばんじ} (everything), {塵取|ちりと}り (dustpan), {中級者|ちゅうきゅうしゃ} (intermediate-level person), {上級者|じょうきゅうしゃ} (advanced-level person)
- **Nouns/Suru verbs (5)**: {解凍|かいとう} (thawing/decompression), {保守|ほしゅ} (conservatism/maintenance), お{披露目|ひろめ} (debut/unveiling), {再検討|さいけんとう} (re-examination), {増強|ぞうきょう} (reinforcement)
- **Na-adjectives (3)**: {乱雑|らんざつ}な (messy), {神聖|しんせい}な (sacred), {不道徳|ふどうとく} (immoral)
- **Adverbs (4)**: {段々|だんだん}と (gradually), {急速|きゅうそく}に (rapidly), {遠回|とおまわ}しに (indirectly), {露骨|ろこつ}に (blatantly)
- **Nouns (specialized, 5)**: {遺言|いごん} (will/testament, legal reading), {株式会社|かぶしきがいしゃ} (corporation), {用水路|ようすいろ} (irrigation channel), {熟練工|じゅくれんこう} (skilled worker), ほうじ{茶|ちゃ} (roasted green tea)
- **Nouns (other, 2)**: {無糖|むとう} (sugar-free), {突然変異|とつぜんへんい} (mutation)
- **Verb (1)**: {消|き}え{去|さ}る (to vanish)
- **Multi-sense entries**: {解凍|かいとう} (2: thawing/decompression), {保守|ほしゅ} (2: conservatism/maintenance), {突然変異|とつぜんへんい} (2: genetic mutation/figurative)

Topics covered: law/justice, science, politics, food/drink, daily life, culture, communication, nature, business
Total entries: ~18,883 → ~18,918 (approximate)
Remaining candidates: ~5,276 → ~5,241 (35 removed as entries)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
