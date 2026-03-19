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
| Total entries | ~17,758 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~14,959 (open) |
| Candidate words | ~6,388 |
| Cross-references | ~3,400 |
| Example sentences | ~51,480 |
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

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 459)
Added 35 new dictionary entries (IDs 17947-17981) from candidate_words.json.

- **Nouns (15)**: {浜辺|はまべ} (beach), {覆面|ふくめん} (mask/incognito), {理性|りせい} (reason/rationality), {母国|ぼこく} (motherland), {念願|ねんがん} (long-cherished wish), {猛威|もうい} (fury), {職歴|しょくれき} (work history), {翌日|よくじつ} (next day), {神父|しんぷ} (priest), {伴侶|はんりょ} (partner/spouse), {裏切|うらぎ}り (betrayal), {搭乗券|とうじょうけん} (boarding pass), {人目|ひとめ} (public eye), {精神力|せいしんりょく} (willpower), {依存症|いぞんしょう} (addiction)
- **Noun/Na-adjective (1)**: {潔白|けっぱく} (innocence/purity)
- **Noun/Adverb (1)**: {真|ま}っ{二|ふた}つ (right in half)
- **Suru verbs (10)**: {調節|ちょうせつ} (adjustment), {合掌|がっしょう} (pressing palms together), {推測|すいそく} (conjecture), {譲歩|じょうほ} (concession), {論破|ろんぱ} (refutation), {微調整|びちょうせい} (fine-tuning), {点滅|てんめつ} (flashing), {凝視|ぎょうし} (staring), {伝聞|でんぶん} (hearsay), {密談|みつだん} (secret talk)
- **Suru verbs (intransitive) (2)**: {意識|いしき}する (to be conscious of), {上達|じょうたつ}する (to improve)
- **Noun/Verb-suru (cultural) (1)**: お{花見|はなみ} (cherry blossom viewing)
- **Ichidan verb (1)**: {疲|つか}れ{果|は}てる (to be utterly exhausted)
- **Noun (clothing) (1)**: {長靴|ながぐつ} (rubber boots)
- **Noun (literary) (2)**: {疑念|ぎねん} (doubt/suspicion), {聖書|せいしょ} (Bible)
- **Noun (found objects) (1)**: {拾|ひろ}い{物|もの} (found object/windfall)

Notable features:
- Cultural: お{花見|はなみ}, {合掌|がっしょう}, {聖書|せいしょ}
- Emotional: {念願|ねんがん}, {潔白|けっぱく}, {裏切|うらぎ}り, {疑念|ぎねん}
- Mental: {理性|りせい}, {精神力|せいしんりょく}, {意識|いしき}する
- Communication: {論破|ろんぱ}, {密談|みつだん}, {伝聞|でんぶん}, {譲歩|じょうほ}
- Daily life: {長靴|ながぐつ}, {搭乗券|とうじょうけん}, {覆面|ふくめん}
- Cross-references added: 3 homophone pairs ({合掌|がっしょう}/{合唱|がっしょう}, {神父|しんぷ}/{新婦|しんぷ}, {聖書|せいしょ}/{清書|せいしょ}, {人目|ひとめ}/{一目|ひとめ})

Total entries: ~17,723 → ~17,758 (approximate)
Remaining candidates: ~6,423 → ~6,388 (35 removed)

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 458)
Added 35 new dictionary entries (IDs 17912-17946) from candidate_words.json.

- **Nouns (16)**: {鉄棒|てつぼう} (horizontal bar), {電柱|でんちゅう} (utility pole), {氷山|ひょうざん} (iceberg), {即戦力|そくせんりょく} (immediate asset), {中東|ちゅうとう} (Middle East), {汎用性|はんようせい} (versatility), {懇親会|こんしんかい} (social gathering), {相違点|そういてん} (point of difference), {年齢制限|ねんれいせいげん} (age limit), {見合|みあ}わせ (service suspension), {二次創作|にじそうさく} (fan fiction), {交換留学|こうかんりゅうがく} (exchange program), {肘掛|ひじか}け{椅子|いす} (armchair), {公共施設|こうきょうしせつ} (public facilities), {予備知識|よびちしき} (background knowledge), {中火|なかび} (medium heat)
- **Na-adjectives (4)**: {根本的|こんぽんてき} (fundamental), {円満|えんまん} (harmonious), {多才|たさい} (talented), {子供向|こどもむ}け (for children)
- **Suru verbs (4)**: {曲解|きょっかい} (misinterpretation), {渡航|とこう} (traveling abroad), {拾|ひろ}い{読|よ}み (skimming), {大失敗|だいしっぱい} (huge failure)
- **Verbs (1)**: せがむ (to pester)
- **Nouns (other) (4)**: おやつ (afternoon snack), おねだり (begging), {出|だ}し{惜|お}しみ (stinting), {互助|ごじょ} (mutual aid)
- **Number (2)**: {億|おく} (100 million), {兆|ちょう} (1 trillion)
- **Adverb (1)**: {手短|てみじか}に (briefly)
- **Expressions (2)**: {波風|なみかぜ}を{立|た}てる (to make waves), {初心者向|しょしんしゃむ}け (for beginners)
- **No-adjective (1)**: {表向|おもてむ}き (outwardly)

Notable features:
- Numbers: {億|おく}, {兆|ちょう} — key Japanese number units
- Culture: おやつ, {二次創作|にじそうさく}, {懇親会|こんしんかい}
- Daily life: {電柱|でんちゅう}, {中火|なかび}, {肘掛|ひじか}け{椅子|いす}
- Transport: {見合|みあ}わせ (service suspension)
- Geography: {中東|ちゅうとう}
- Education: {交換留学|こうかんりゅうがく}, {初心者向|しょしんしゃむ}け, {予備知識|よびちしき}

Total entries: ~17,688 → ~17,723 (approximate)
Remaining candidates: ~6,469 → ~6,423 (39 removed: 35 created + 4 stale duplicates)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
