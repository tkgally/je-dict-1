# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-18
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
| Total entries | ~17,626 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,827 (open) |
| Candidate words | ~2,152 |
| Cross-references | ~3,400 |
| Example sentences | ~51,020 |
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

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 454)
Added 35 new dictionary entries (IDs 17772-17806) from candidate_words.json.

- **Nouns (21)**: {貴婦人|きふじん} (noblewoman), {光陰|こういん} (time/literary), {急斜面|きゅうしゃめん} (steep slope), {卸業者|おろしぎょうしゃ} (wholesaler), {中立国|ちゅうりつこく} (neutral country), {集積所|しゅうせきじょ} (collection point), {次長|じちょう} (deputy director), {案内図|あんないず} (guide map), {現代語|げんだいご} (modern language), {枠内|わくない} (within limits), {磁力|じりょく} (magnetic force), {異説|いせつ} (dissenting view), {益虫|えきちゅう} (beneficial insect), {広角|こうかく} (wide-angle), {不特定|ふとくてい} (unspecified), {在校生|ざいこうせい} (current student), {若気|わかげ} (youthful impetuousness), {国力|こくりょく} (national power), {公爵|こうしゃく} (duke), {特報|とくほう} (breaking news), {絶望感|ぜつぼうかん} (sense of despair)
- **Noun/Suru verbs (6)**: {抜糸|ばっし} (stitch removal), {連写|れんしゃ} (burst mode), {口承|こうしょう} (oral tradition), {接写|せっしゃ} (close-up photography), {詳述|しょうじゅつ} (detailed description), {死滅|しめつ} (extinction)
- **Na-adjectives (2)**: {道徳的|どうとくてき} (moral/ethical), {瑣末|さまつ} (trivial/trifling)
- **Noun/Na-adjective (1)**: {虚像|きょぞう} (virtual/false image)
- **Noun/No-adjective (1)**: {玄人好|くろうとごの}み (for connoisseurs)
- **Noun (business) (2)**: {他社|たしゃ} (other company), {些事|さじ} (trivial matter)
- **Verb (1)**: {組|く}み{合|あ}わさる (to be combined)
- **Noun (multi-sense) (1)**: {枠内|わくない} (within frame/within limits)

Notable features:
- Photography: {連写|れんしゃ}, {接写|せっしゃ}, {広角|こうかく}
- Business/organizations: {他社|たしゃ}, {次長|じちょう}, {卸業者|おろしぎょうしゃ}
- Literary/formal: {光陰|こういん}, {貴婦人|きふじん}, {口承|こうしょう}, {詳述|しょうじゅつ}
- Science: {磁力|じりょく}, {虚像|きょぞう}, {死滅|しめつ}, {益虫|えきちゅう}
- New kanji: 2,568 → 2,569 ({瑣|さ})

Total entries: ~17,626 → ~17,661 (approximate)
Remaining candidates: ~2,152 → ~2,117 (35 removed)

### 2026-03-18 (Vocabulary Expansion - 35 New Entries, Session 453)
Added 35 new dictionary entries (IDs 17737-17771) from candidate_words.json.

- **Verbs (7)**: {問|と}い{合|あ}わせる (to inquire), {銘記|めいき}する (to engrave in mind), {茹|ゆ}で{上|あ}がる (to be done boiling), {造|つく}る (to build/brew), {鎮|しず}まる (to subside), {放浪|ほうろう} (wandering), {下|した}ゆで (parboiling)
- **Nouns (18)**: {専制|せんせい} (despotism), {鴨|かも} (duck), {党首|とうしゅ} (party leader), {遠路|えんろ} (long journey), {祭典|さいてん} (festival), {恋仲|こいなか} (romantic relationship), {精魂|せいこん} (heart and soul), {墨汁|ぼくじゅう} (India ink), {発券|はっけん} (ticket issuance), {無|む} (nothingness/prefix), {防虫|ぼうちゅう} (insect repellent), {即効性|そっこうせい} (immediate effect), {中皿|ちゅうざら} (medium plate), {庭木|にわき} (garden tree), {手拍子|てびょうし} (hand clapping), {一読|いちどく} (single reading), {余熱|よねつ} (residual heat), {実情|じつじょう} (actual conditions)
- **Adjectives (4)**: {清浄|せいじょう} (pure/clean), {呆然|ぼうぜん} (dumbfounded), {心外|しんがい} (regrettable), {妖艶|ようえん} (bewitching)
- **Other (6)**: {謝意|しゃい} (gratitude), {背|せ}もたれ (backrest), {上旬|じょうじゅん} (first 10 days of month), {仮想|かそう} (virtual), {成仏|じょうぶつ} (entering Nirvana), {後払|あとばら}い (deferred payment)

Notable features:
- Cooking: {茹|ゆ}で{上|あ}がる, {下|した}ゆで, {余熱|よねつ}, {中皿|ちゅうざら}, {鴨|かも}
- Culture/religion: {成仏|じょうぶつ}, {祭典|さいてん}, {墨汁|ぼくじゅう}, {手拍子|てびょうし}
- Politics: {専制|せんせい}, {党首|とうしゅ}
- Technology: {仮想|かそう}, {発券|はっけん}
- Daily life: {背|せ}もたれ, {庭木|にわき}, {防虫|ぼうちゅう}, {後払|あとばら}い, {上旬|じょうじゅん}

Total entries: ~17,594 → ~17,626 (approximate)
Remaining candidates: ~2,186 → ~2,152 (34 removed)

### 2026-03-18 (Vocabulary Expansion - 32 New Entries, Session 452)
Added 32 new dictionary entries (IDs 17702-17736) from candidate_words.json. (3 candidates skipped as duplicates of existing entries: {統率|とうそつ}, {貸与|たいよ}, {拝聴|はいちょう}.)

- **Nouns (14)**: {連休明|れんきゅうあ}け (end of long weekend), {収集日|しゅうしゅうび} (garbage collection day), {糠漬|ぬかづ}け (rice-bran pickles), {大葉|おおば} (green perilla leaf), {事実婚|じじつこん} (common-law marriage), {改訂版|かいていばん} (revised edition), {最前列|さいぜんれつ} (front row), {薄|うす}ら{笑|わら}い (smirk), {取|と}っ{組|く}み{合|あ}い (scuffle), {合唱団|がっしょうだん} (choir), {国立公園|こくりつこうえん} (national park), {門下生|もんかせい} (pupil/disciple), {家宝|かほう} (family heirloom), {器械|きかい} (apparatus/instrument)
- **Noun/Suru verbs (10)**: {帰郷|ききょう} (returning home), {来場|らいじょう} (attendance), {過大評価|かだいひょうか} (overestimation), {再挑戦|さいちょうせん} (trying again), {借用|しゃくよう} (borrowing), {退席|たいせき} (leaving one's seat), {爆走|ばくそう} (reckless driving/blazing run), {諮問|しもん} (advisory inquiry), {固辞|こじ} (firm refusal), {摂生|せっせい} (health care/temperance)
- **Noun/Suru verb (sports)**: {先発|せんぱつ} (starting lineup/departing first)
- **Na-adjective (2)**: {前途有望|ぜんとゆうぼう} (having a promising future), {楽観主義|らっかんしゅぎ} (optimism)
- **Noun (business)**: {外回|そとまわ}り (outside sales/outer loop), {中途採用|ちゅうとさいよう} (mid-career hiring), {未経験|みけいけん} (inexperienced)
- **Noun (culture)**: {敵討|かたきう}ち (revenge/vengeance), {神宮|じんぐう} (grand shrine)

Notable features:
- Business/career: {中途採用|ちゅうとさいよう}, {未経験|みけいけん}, {外回|そとまわ}り, {借用|しゃくよう}
- Formal: {退席|たいせき}, {諮問|しもん}, {固辞|こじ}
- Culture/history: {神宮|じんぐう}, {敵討|かたきう}ち, {門下生|もんかせい}, {家宝|かほう}
- Food: {糠漬|ぬかづ}け, {大葉|おおば}
- Daily life: {連休明|れんきゅうあ}け, {収集日|しゅうしゅうび}, {国立公園|こくりつこうえん}
- New kanji: 2,567 → 2,568 ({糠|ぬか})

Total entries: ~17,594 → ~17,626 (approximate)
Remaining candidates: ~2,186 → ~2,155 (31 removed)

### 2026-03-18 (Vocabulary Expansion - 35 New Entries, Session 451)
Added 35 new dictionary entries (IDs 17514-17549) from candidate_words.json:

- **Nouns (17)**: {飲|の}み{屋|や} (bar/pub), {並木道|なみきみち} (tree-lined road), {横目|よこめ} (sidelong glance), {銀世界|ぎんせかい} (snowy landscape), {独|ひと}り{身|み} (being single), {湖畔|こはん} (lakeside), {知恵袋|ちえぶくろ} (source of wisdom), {得意料理|とくいりょうり} (specialty dish), {遊具|ゆうぐ} (playground equipment), {命日|めいにち} (death anniversary), {土砂|どしゃ} (earth and sand), {夜道|よみち} (road at night), {零下|れいか} (below zero), {敬称|けいしょう} (honorific title), {乱気流|らんきりゅう} (turbulence), {非常事態|ひじょうじたい} (state of emergency), {急病|きゅうびょう} (sudden illness)
- **Noun/Suru verbs (7)**: {仰天|ぎょうてん} (astonishment), {沈没|ちんぼつ} (sinking), {立|た}ち{往生|おうじょう} (being stranded), {複製|ふくせい} (reproduction), {熟読|じゅくどく} (reading carefully), {滑落|かつらく} (slipping and falling), {究明|きゅうめい} (investigation)
- **Noun/Adjectives (4)**: {想定外|そうていがい} (unforeseen), {和洋折衷|わようせっちゅう} (Japanese-Western fusion), {純情|じゅんじょう} (pure-hearted), {弱腰|よわごし} (weak-kneed)
- **Noun/Adjective (1)**: {丸裸|まるはだか} (stark naked; stripped bare)
- **Verbs (2)**: {戒|いまし}める (to warn/admonish), {上向|うわむ}く (to improve/look up)
- **Expressions (2)**: {首|くび}を{傾|かし}げる (to tilt head in puzzlement), {途方|とほう}に{暮|く}れる (to be at a loss)
- **Adverb (1)**: よもや (surely not)
- **Expression (1)**: {縁起|えんぎ}が{良|よ}い (auspicious)

Notable features:
- Disaster/emergency: {非常事態|ひじょうじたい}, {土砂|どしゃ}, {滑落|かつらく}, {乱気流|らんきりゅう}, {立|た}ち{往生|おうじょう}
- Daily life/culture: {飲|の}み{屋|や}, {得意料理|とくいりょうり}, {命日|めいにち}, {縁起|えんぎ}が{良|よ}い, {和洋折衷|わようせっちゅう}
- Emotion/cognition: {仰天|ぎょうてん}, {純情|じゅんじょう}, {途方|とほう}に{暮|く}れる, {首|くび}を{傾|かし}げる, よもや
- Scenery/nature: {銀世界|ぎんせかい}, {並木道|なみきみち}, {湖畔|こはん}, {零下|れいか}
- New kanji: 2,566 → 2,567 ({畔|はん})

Total entries: ~17,559 → ~17,594 (approximate)
Remaining candidates: ~2,221 → ~2,186 (35 removed)

### 2026-03-18 (Vocabulary Expansion - 35 New Entries, Session 450)
Added 35 new dictionary entries (IDs 17479-17513) from candidate_words.json:

- **Expressions/Adverbs (7)**: {今|いま}まさに (at this very moment), {年|とし}ごとに (year by year), {可能|かのう}であれば (if possible), {均衡|きんこう}を{保|たも}つ (maintain balance), {反応|はんのう}を{見|み}る (gauge a reaction), {直|じか}に{触|ふ}れる (touch directly/experience firsthand), {耳|みみ}を{慣|な}らす (train one's ear)
- **Nouns (17)**: {一昨昨日|さきおととい} (three days ago), {生活|せいかつ}の{質|しつ} (quality of life), {感染経路|かんせんけいろ} (route of infection), {無形文化財|むけいぶんかざい} (intangible cultural property), {英文法|えいぶんぽう} (English grammar), {化学肥料|かがくひりょう} (chemical fertilizer), {殺人未遂|さつじんみすい} (attempted murder), {戸籍抄本|こせきしょうほん} (family register extract), {物見櫓|ものみやぐら} (watchtower), {舞台装置|ぶたいそうち} (stage set), {長期保有|ちょうきほゆう} (long-term holding), {合|あ}わせ{酢|ず} (seasoned vinegar), {公衆衛生|こうしゅうえいせい} (public health), {隔世遺伝|かくせいいでん} (atavism), {臨時収入|りんじしゅうにゅう} (extra income), {体罰禁止|たいばつきんし} (corporal punishment ban), {修了式|しゅうりょうしき} (completion ceremony)
- **Noun/Suru verbs (3)**: {予算|よさん}オーバー (over budget), {工業化|こうぎょうか} (industrialization), {銘記|めいき} (engrave in mind)
- **Noun/No-adjectives (3)**: {自分用|じぶんよう} (for personal use), {未舗装|みほそう} (unpaved), {無酸素|むさんそ} (oxygen-free)
- **Noun/Na-adjective (1)**: {正確無比|せいかくむひ} (unparalleled accuracy)
- **Other (4)**: よくある{質問|しつもん} (FAQ), {一意専心|いちいせんしん} (single-minded devotion), きょろり (quick glance), {内意|ないい} (real intention)

Notable features:
- Health/science: {感染経路|かんせんけいろ}, {公衆衛生|こうしゅうえいせい}, {無酸素|むさんそ}, {隔世遺伝|かくせいいでん}
- Culture/society: {無形文化財|むけいぶんかざい}, {物見櫓|ものみやぐら}, {舞台装置|ぶたいそうち}, {体罰禁止|たいばつきんし}
- Business/finance: {予算|よさん}オーバー, {長期保有|ちょうきほゆう}, {臨時収入|りんじしゅうにゅう}
- Education: {英文法|えいぶんぽう}, {修了式|しゅうりょうしき}, {耳|みみ}を{慣|な}らす
- Legal/admin: {殺人未遂|さつじんみすい}, {戸籍抄本|こせきしょうほん}

Total entries: ~17,524 → ~17,559 (approximate)
Remaining candidates: ~2,255 → ~2,221 (34 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
