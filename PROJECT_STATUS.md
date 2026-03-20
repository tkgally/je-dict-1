# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-20
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
| Total entries | ~17,898 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~15,099 (open) |
| Candidate words | ~6,272 |
| Cross-references | ~3,400 |
| Example sentences | ~51,830 |
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

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 463)
Added 35 new dictionary entries (IDs 18087-18121) from candidate_words.json.

- **Expressions (7)**: {申|もう}し{訳|わけ}ございません (deeply sorry), {失礼|しつれい}いたします (excuse me - formal), {知恵|ちえ}を{絞|しぼ}る (to rack one's brains), {皮|かわ}をむく (to peel), {食卓|しょくたく}を{囲|かこ}む (gather around the table), {焦点|しょうてん}を{絞|しぼ}る (to focus/narrow down), というのも (the reason is)
- **Nouns (17)**: {負|ふ}の{連鎖|れんさ} (vicious cycle), {時短|じたん}{勤務|きんむ} (reduced working hours), {潜在|せんざい}{意識|いしき} (subconscious), {雑居|ざっきょ}ビル (multi-tenant building), {決定|けってい}{事項|じこう} (decided matters), {客室|きゃくしつ}{乗務員|じょうむいん} (flight attendant), {車内|しゃない}{販売|はんばい} (trolley service), {金融|きんゆう}{政策|せいさく} (monetary policy), {助演|じょえん} (supporting role), {資産|しさん}{運用|うんよう} (asset management), {赤十字|せきじゅうじ} (Red Cross), {配布物|はいふぶつ} (handouts), {公共|こうきょう}{交通|こうつう}{機関|きかん} (public transportation), {国際|こくさい}{連合|れんごう} (United Nations), {安保理|あんぽり} (UN Security Council), {寒冷|かんれい}{前線|ぜんせん} (cold front), {新規|しんき}{開拓|かいたく} (new business development)
- **Na-adjectives (4)**: {能弁|のうべん} (eloquent), {不純|ふじゅん} (impure), {男性的|だんせいてき} (masculine), {精選|せいせん} (careful selection)
- **Other (7)**: {泣|な}き{落|お}とし (tearful persuasion), {幾多|いくた}の (many - literary), {贔屓目|ひいきめ} (biased view), {生薬|しょうやく} (herbal medicine), {毒草|どくそう} (poisonous plant), {禁令|きんれい} (prohibition), {自由形|じゆうがた} (freestyle swimming)

Notable features:
- Formal expressions: {申|もう}し{訳|わけ}ございません, {失礼|しつれい}いたします — business Japanese essentials
- Idiomatic: {知恵|ちえ}を{絞|しぼ}る, {泣|な}き{落|お}とし, {贔屓目|ひいきめ}
- International affairs: {国際|こくさい}{連合|れんごう}, {安保理|あんぽり}, {赤十字|せきじゅうじ}
- Workplace: {時短|じたん}{勤務|きんむ}, {決定|けってい}{事項|じこう}, {新規|しんき}{開拓|かいたく}
- Daily life: {公共|こうきょう}{交通|こうつう}{機関|きかん}, {車内|しゃない}{販売|はんばい}, {皮|かわ}をむく

Total entries: ~17,898 → ~17,933 (approximate)
Remaining candidates: ~6,272 → ~6,237 (35 removed)

### 2026-03-20 (Vocabulary Expansion - 35 New Entries, Session 462)
Added 35 new dictionary entries (IDs 18052-18086) from candidate_words.json.

- **Verbs (8)**: {注|そそ}ぎ{込|こ}む (to pour into), {途切|とぎ}れる (to be interrupted), {和|なご}む (to be soothed), {尊|とうと}ぶ (to value), つぼむ (to close up), {損|そこ}なう (to harm), {被|こうむ}る (to sustain damage), {際立|きわだ}たせる (to make stand out)
- **Nouns/Suru verbs (8)**: {内示|ないじ} (unofficial notice), {更生|こうせい} (rehabilitation), {就航|しゅうこう} (entering service), {発給|はっきゅう} (issuance), {混和|こんわ} (mixing), リバウンド (rebound), {倍返|ばいがえ}し (returning double), {顕在|けんざい} (becoming manifest)
- **Nouns (13)**: {満杯|まんぱい} (full to capacity), {対応力|たいおうりょく} (adaptability), {参政権|さんせいけん} (suffrage), {茶店|さてん} (teahouse), {丙|へい} (third/C grade), {卓|たく} (table), {吉凶|きっきょう} (fortune), {理容室|りようしつ} (barbershop), {電子機器|でんしきき} (electronic device), {生活苦|せいかつく} (hardship), {防腐剤|ぼうふざい} (preservative), {中性|ちゅうせい} (neutral), {砲兵|ほうへい} (artillery), {無機物|むきぶつ} (inorganic matter)
- **Counters (2)**: {頭|とう} (large animals), {尾|び} (fish)
- **Expressions (2)**: {目|め}につく (to catch one's eye), {気|き}にかける (to worry about)
- **Adverb (1)**: これほど (this much)
- **Na-adjective (1)**: {満杯|まんぱい} (full to capacity)

Notable features:
- Verbs with nuance: {和|なご}む (online culture), {損|そこ}なう (verb suffix usage), つぼむ (flower terminology)
- Workplace: {内示|ないじ}, {更生|こうせい}, {対応力|たいおうりょく}
- Daily life: {理容室|りようしつ}, {茶店|さてん}, {防腐剤|ぼうふざい}, {電子機器|でんしきき}
- Culture: {倍返|ばいがえ}し (半沢直樹 catchphrase), {吉凶|きっきょう}, {丙|へい} (Heavenly Stems)
- Counters: {頭|とう}, {尾|び} — animal counting
- New kanji: 2,573 → 2,574 ({丙|へい})
- Removed 11 stale duplicate candidates

Total entries: ~17,863 → ~17,898 (approximate)
Remaining candidates: ~6,317 → ~6,272 (45 removed: 34 created + 11 stale duplicates)

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 461)
Added 35 new dictionary entries (IDs 18017-18051) from candidate_words.json.

- **Nouns (14)**: {鼻歌|はなうた} (humming), {真昼|まひる} (midday), {紳士|しんし} (gentleman), {淑女|しゅくじょ} (lady), {交響曲|こうきょうきょく} (symphony), {演奏会|えんそうかい} (concert), {質感|しつかん} (texture), {郵便物|ゆうびんぶつ} (mail), {木炭|もくたん} (charcoal), {切|き}り{札|ふだ} (trump card), {囲碁|いご} (Go), {救|すく}いの{手|て} (helping hand), {指折|ゆびお}り (leading), {一回|いっかい}きり (once only)
- **Noun/Suru verbs (10)**: {日向|ひなた}ぼっこ (sunbathing), {厳禁|げんきん} (strictly prohibited), {懺悔|ざんげ} (confession), {未払|みばら}い (unpaid), {出題|しゅつだい} (setting questions), {根負|こんま}け (giving in), {密告|みっこく} (informing), {盗作|とうさく} (plagiarism), {殴|なぐ}り{書|が}き (scribbling), {集客|しゅうきゃく} (attracting customers)
- **Noun/Suru verbs (formal) (3)**: {快諾|かいだく} (ready consent), {疎通|そつう} (communication), {贈答|ぞうとう} (gift exchange)
- **Noun/Na-adjectives (3)**: {引|ひ}っ{込|こ}み{思案|じあん} (shy), {崇高|すうこう} (sublime), {高品質|こうひんしつ} (high quality)
- **Na-adjective (1)**: {華|はな}やかな (gorgeous)
- **I-adjectives (2)**: {若々|わかわか}しい (youthful), {汚|けが}らわしい (disgusting)
- **Noun/Verb-suru (1)**: {同情|どうじょう}する (to sympathize)
- **Counter/Noun (1)**: {難問|なんもん} (difficult problem)

Notable features:
- Culture: {囲碁|いご}, {贈答|ぞうとう}, {懺悔|ざんげ}, {紳士|しんし}/{淑女|しゅくじょ} pair
- Music: {交響曲|こうきょうきょく}, {演奏会|えんそうかい}
- Personality: {引|ひ}っ{込|こ}み{思案|じあん}, {若々|わかわか}しい
- Business: {集客|しゅうきゅく}, {未払|みばら}い, {快諾|かいだく}
- Figurative: {切|き}り{札|ふだ}, {救|すく}いの{手|て}, {指折|ゆびお}り
- New kanji: 2,571 → 2,573 ({懺|ざん}, {紳|しん})

Total entries: ~17,828 → ~17,863 (approximate)
Remaining candidates: ~6,352 → ~6,317 (35 removed)

### 2026-03-19 (Vocabulary Expansion - 35 New Entries, Session 460)
Added 35 new dictionary entries (IDs 17982-18016) from candidate_words.json.

- **Nouns (20)**: {退所|たいしょ} (discharge from facility), {糖質|とうしつ}{制限|せいげん} (low-carb diet), {婦人|ふじん}{服|ふく} (women's clothing), {振付師|ふりつけし} (choreographer), ショーケース (showcase), {陳列棚|ちんれつだな} (display shelf), {腺|せん} (gland), {丁字路|ていじろ} (T-junction), {現代|げんだい}{文学|ぶんがく} (modern literature), {心理|しんり}{描写|びょうしゃ} (psychological description), {野手|やしゅ} (fielder), {記念|きねん}{式典|しきてん} (commemorative ceremony), コルク{抜|ぬ}き (corkscrew), {襟足|えりあし} (nape hairline), {一輪挿|いちりんざ}し (bud vase), {予約|よやく}{特典|とくてん} (pre-order bonus), {湯沸|ゆわ}かし (kettle), {主犯|しゅはん} (principal offender), {騎兵|きへい} (cavalry), {人格|じんかく}{形成|けいせい} (character building)
- **Noun/Suru verbs (7)**: {先行|せんこう}{予約|よやく} (advance booking), {新規|しんき}{事業|じぎょう} (new business), {衛生|えいせい}{管理|かんり} (hygiene management), {共同|きょうどう}{開発|かいはつ} (joint development), {精神|せいしん}{統一|とういつ} (mental concentration), {築城|ちくじょう} (castle construction), {進軍|しんぐん} (military advance)
- **Other (8)**: {最高|さいこう}{速度|そくど} (maximum speed), {身内|みうち}びいき (nepotism), {社外|しゃがい} (outside the company), {魔術|まじゅつ} (magic/sorcery), {深層|しんそう}{心理|しんり} (deep psychology), {貴殿|きでん} (you - formal pronoun), {盆|ぼん}{帰|がえ}り (Obon homecoming), {九死|きゅうし}に{一生|いっしょう} (narrow escape from death)

Notable features:
- Retail: ショーケース, {陳列棚|ちんれつだな}, {婦人|ふじん}{服|ふく}
- Business: {新規|しんき}{事業|じぎょう}, {社外|しゃがい}, {共同|きょうどう}{開発|かいはつ}
- Culture: {盆|ぼん}{帰|がえ}り, {一輪挿|いちりんざ}し, {築城|ちくじょう}
- Medical: {腺|せん}
- New kanji: 2,570 → 2,571 ({腺|せん})
- Removed 1 stale candidate ({徹底的|てっていてき} - already existed)

Total entries: ~17,793 → ~17,828 (approximate)
Remaining candidates: ~6,388 → ~6,352 (36 removed: 35 created + 1 stale duplicate)

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
