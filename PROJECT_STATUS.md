# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-19
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
| Total entries | ~17,688 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,889 (open) |
| Candidate words | ~6,469 |
| Cross-references | ~3,400 |
| Example sentences | ~51,245 |
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

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 457)
Added 35 new dictionary entries (IDs 17877-17911) from candidate_words.json.

- **Nouns (35)**: {終演|しゅうえん} (end of performance), {贅沢三昧|ぜいたくざんまい} (indulgence), {魚の目|うおのめ} (corn on foot), {先頭車両|せんとうしゃりょう} (lead car), {火力発電|かりょくはつでん} (thermal power), {地下駐車場|ちかちゅうしゃじょう} (underground parking), {機体|きたい} (aircraft/fuselage), {五重|ごじゅう}の{塔|とう} (five-story pagoda), {既刊|きかん} (already published), {寄港地|きこうち} (port of call), {吸水|きゅうすい} (water absorption), {空腹時|くうふくじ} (on empty stomach), {尖塔|せんとう} (spire), {通信制|つうしんせい} (correspondence system), {記念切手|きねんきって} (commemorative stamp), {皆既月食|かいきげっしょく} (total lunar eclipse), {大|だい}リーグ (Major Leagues), {室内犬|しつないけん} (indoor dog), {執刀医|しっとうい} (operating surgeon), {痰|たん} (phlegm), {核燃料|かくねんりょう} (nuclear fuel), {画面収録|がめんしゅうろく} (screen recording), {磁場|じば} (magnetic field), {電磁波|でんじは} (electromagnetic waves), {解答欄|かいとうらん} (answer column), {指定席券|していせきけん} (reserved seat ticket), {原子力発電|げんしりょくはつでん} (nuclear power), {鉄筋|てっきん}コンクリート (reinforced concrete), {大量消費|たいりょうしょうひ} (mass consumption), {契約破棄|けいやくはき} (contract cancellation), {抗原|こうげん} (antigen), {上書|うわが}き{保存|ほぞん} (overwrite save), {放射性廃棄物|ほうしゃせいはいきぶつ} (radioactive waste), {銘板|めいばん} (nameplate), {労働基準法|ろうどうきじゅんほう} (Labor Standards Act)

Notable features:
- Energy: {火力発電|かりょくはつでん}, {原子力発電|げんしりょくはつでん}, {核燃料|かくねんりょう}, {放射性廃棄物|ほうしゃせいはいきぶつ}
- Transportation: {先頭車両|せんとうしゃりょう}, {指定席券|していせきけん}, {寄港地|きこうち}, {機体|きたい}
- Science: {磁場|じば}, {電磁波|でんじは}, {抗原|こうげん}, {皆既月食|かいきげっしょく}
- Technology: {画面収録|がめんしゅうろく}, {上書|うわが}き{保存|ほぞん}
- Legal/business: {契約破棄|けいやくはき}, {労働基準法|ろうどうきじゅんほう}
- Culture: {五重|ごじゅう}の{塔|とう}, {大|だい}リーグ, {贅沢三昧|ぜいたくざんまい}
- New kanji: 2,569 → 2,570 ({痰|たん})

Total entries: ~17,653 → ~17,688 (approximate)
Remaining candidates: ~6,503 → ~6,469 (34 removed)

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 456)
Added 35 new dictionary entries (IDs 17842-17876) from candidate_words.json.

- **Suru verbs (6)**: {整備|せいび}する (to maintain), {解説|かいせつ}する (to commentate), {証明|しょうめい}する (to prove), {関連|かんれん}する (to be related), {入部|にゅうぶ}する (to join a club), {統率|とうそつ}する (to command)
- **Ichidan verbs (2)**: {植|う}え{替|か}える (to replant), {釣|つ}り{上|あ}げる (to fish up/hike prices)
- **Nouns (10)**: {人員|じんいん} (personnel), {支持者|しじしゃ} (supporter), {十字架|じゅうじか} (cross/crucifix), お{経|きょう} (Buddhist sutra), {関西弁|かんさいべん} (Kansai dialect), {連鎖反応|れんさはんのう} (chain reaction), {感度|かんど} (sensitivity), {飼育員|しいくいん} (zookeeper), {名誉毀損|めいよきそん} (defamation), {飽和状態|ほうわじょうたい} (saturation)
- **Adjectives (3)**: {大|おお}まかな (rough/broad), {最愛|さいあい} (beloved), のろい (slow/sluggish)
- **Nouns/Translation (2)**: {和訳|わやく} (Japanese translation), {意訳|いやく} (free translation)
- **Noun (other) (3)**: {未完|みかん} (unfinished), ほら{吹|ふ}き (boaster), ライフライン (essential utilities), {交通量|こうつうりょう} (traffic volume)
- **Adverbs/Onomatopoeia (3)**: {小刻|こきざ}みに (in small steps), ポカンと (blankly/gaping), かすかに (faintly)
- **Expressions (5)**: というより (rather than), {今更|いまさら}ながら (even at this late stage), {愛着|あいちゃく}が{湧|わ}く (to grow fond of), {融通|ゆうずう}が{利|き}く (to be flexible), {水気|みずけ}を{切|き}る (to drain moisture)

Notable features:
- Translation pair: {和訳|わやく} / {意訳|いやく}
- Cooking: {水気|みずけ}を{切|き}る
- Culture/religion: {十字架|じゅうじか}, お{経|きょう}, {関西弁|かんさいべん}
- Disaster: ライフライン
- Legal: {名誉毀損|めいよきそん}
- School life: {入部|にゅうぶ}する

Total entries: ~17,653 → ~17,688 (approximate)
Remaining candidates: ~6,537 → ~6,503 (34 removed)

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 455)
Added 35 new dictionary entries (IDs 17807-17841) from candidate_words.json.

- **Nouns (16)**: {水銀|すいぎん} (mercury), {有名人|ゆうめいじん} (celebrity), {小物|こもの} (accessories/small fry), {冒険心|ぼうけんしん} (spirit of adventure), {標語|ひょうご} (slogan), {一匹狼|いっぴきおおかみ} (lone wolf), {次世代|じせだい} (next generation), ばい{菌|きん} (germs), {福引|ふくび}き (lucky draw), {危険性|きけんせい} (riskiness), {枝分|えだわ}かれ (branching), {水玉模様|みずたまもよう} (polka dots), {養父|ようふ} (adoptive father), {義姉|ぎし} (sister-in-law), {旅客機|りょかくき} (passenger plane), {脈拍|みゃくはく} (pulse)
- **Suru verbs (5)**: {退席|たいせき}する (to leave one's seat), {投影|とうえい}する (to project), {借用|しゃくよう}する (to borrow formally), {貸与|たいよ}する (to lend formally), {消毒|しょうどく}する (to disinfect)
- **Nouns/Na-adjectives (2)**: {無制限|むせいげん} (unlimited), {実力主義|じつりょくしゅぎ} (meritocracy)
- **Expressions (6)**: {間違|まちが}いない (certain), {言|い}い{換|か}えれば (in other words), {猛威|もうい}を{振|ふ}るう (to rage), しっくりくる (to feel right), そっとしておく (to leave alone), {居眠|いねむ}り{運転|うんてん} (drowsy driving)
- **Verb (1)**: {泣|な}き{叫|さけ}ぶ (to cry out)
- **Adverbs (2)**: {表面上|ひょうめんじょう} (on the surface), {現段階|げんだんかい} (at the present stage)
- **Noun (multi-sense) (2)**: {計算機|けいさんき} (calculator/computer), {妥協点|だきょうてん} (compromise point)

Notable features:
- Formal pairs: {借用|しゃくよう}する / {貸与|たいよ}する (borrow/lend)
- Health/hygiene: {消毒|しょうどく}する, ばい{菌|きん}, {脈拍|みゃくはく}
- Society/business: {実力主義|じつりょくしゅぎ}, {有名人|ゆうめいじん}, {標語|ひょうご}
- Everyday expressions: しっくりくる, そっとしておく, {間違|まちが}いない
- Culture: {一匹狼|いっぴきおおかみ}, {福引|ふくび}き, {水玉模様|みずたまもよう}

Total entries: ~17,626 → ~17,653 (approximate)
Remaining candidates: ~6,572 → ~6,537 (35 removed)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
