# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-09
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
| Total entries | ~16,002 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~13,203 (open) |
| Candidate words | ~3,772 |
| Cross-references | ~3,400 |
| Example sentences | ~49,000 |
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

### 2026-03-09 (Vocabulary Expansion - 30 New Entries, Session 405)
Added 30 new dictionary entries (IDs 15920-15949) from candidate_words.json:

- **Nouns (14)**: {突風|とっぷう} (gust of wind), {雷雨|らいう} (thunderstorm), {目印|めじるし} (landmark), {専門店|せんもんてん} (specialty store), {札束|さつたば} (wad of bills), {王冠|おうかん} (crown), {日報|にっぽう} (daily report), {特産|とくさん} (local specialty), {本堂|ほんどう} (main hall), {分母|ぶんぼ} (denominator), {類義語|るいぎご} (synonym), {唾液|だえき} (saliva), {目星|めぼし} (lead/estimate), {卸値|おろしね} (wholesale price)
- **Noun/verb-suru (4)**: {面会|めんかい} (visit), {大笑|おおわら}い (big laugh), {躍動|やくどう} (lively motion), {受講|じゅこう} (taking a course)
- **Noun/na-adjective (3)**: {欲張|よくば}り (greedy), {無尽蔵|むじんぞう} (inexhaustible), {無欲|むよく} (selfless)
- **Noun (multi-sense) (2)**: {王冠|おうかん} (2: crown + bottle cap), {大当|おおあ}たり (2: jackpot + big hit)
- **Verb-godan (2)**: {強|つよ}がる (to act tough), {居座|いすわ}る (to stay put)
- **Verb-ichidan (1)**: わきまえる (to discern/know one's place)
- **Nouns (other) (4)**: {振|ふ}り{出|だ}し (starting point), {振替|ふりかえ} (transfer/substitution), {高潮|たかしお} (storm surge), {口封|くちふう}じ (silencing someone), {北方|ほっぽう} (the north)

Notable features:
- Weather cluster: {突風|とっぷう}, {雷雨|らいう}, {高潮|たかしお}
- Commerce/work: {専門店|せんもんてん}, {卸値|おろしね}, {日報|にっぽう}, {受講|じゅこう}
- Cultural: わきまえる (knowing one's place), {本堂|ほんどう} (temple hall), {特産|とくさん} (regional specialties)
- Language: {類義語|るいぎご} (synonym), {分母|ぶんぼ} (denominator)
- New kanji: 2,523 → 2,524 ({唾|だ})

Total entries: ~15,972 → ~16,002 (approximate)
Remaining candidates: ~3,802 → ~3,772 (30 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 404)
Added 30 new dictionary entries (IDs 15890-15919) from candidate_words.json:

- **Nouns (18)**: {慣用句|かんようく} (idiom), {空欄|くうらん} (blank space), {路線図|ろせんず} (route map), {実話|じつわ} (true story), {身動|みうご}き (body movement), {泣|な}き{言|ごと} (whining), {活火山|かっかざん} (active volcano), {白線|はくせん} (white line), {度胸|どきょう} (courage), {小路|こうじ} (narrow lane), {推進力|すいしんりょく} (driving force), {刺|さ}し{傷|きず} (stab wound), {控|ひか}え (reserve/copy), {出席簿|しゅっせきぼ} (attendance record), {養護施設|ようごしせつ} (care facility), {兄弟姉妹|きょうだいしまい} (siblings), {演出家|えんしゅつか} (stage director), {小旅行|しょうりょこう} (short trip)
- **Noun (multi-sense) (3)**: {腹筋|ふっきん} (2: abs + sit-ups), {控|ひか}え (2: copy + reserve), {金星|きんせい} (1: Venus)
- **Noun/verb-suru (2)**: {共作|きょうさく} (collaboration), {貸与|たいよ} (lending)
- **Verb-godan (3)**: {絶|た}やす (to let die out), {巻|ま}き{戻|もど}す (to rewind), {召|め}す (to eat/wear, honorific)
- **Adverb (1)**: {真|ま}っ{先|さき}に (first and foremost)
- **Noun (compound) (3)**: {期限切|きげんぎ}れ (expiration), {水産業|すいさんぎょう} (fisheries industry), {違憲|いけん} (unconstitutional)

Notable features:
- Diverse mix: legal ({違憲|いけん}), education ({慣用句|かんようく}, {空欄|くうらん}, {出席簿|しゅっせきぼ}), travel ({路線図|ろせんず}, {白線|はくせん}, {小旅行|しょうりょこう})
- Honorific verb: {召|め}す (3 senses: eat/drink, wear, summon)
- Multi-sense entries: {腹筋|ふっきん} (body + exercise), {控|ひか}え (document + sports)

Total entries: ~15,942 → ~15,972 (approximate)
Remaining candidates: ~3,831 → ~3,802 (29 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 403)
Added 30 new dictionary entries (IDs 15860-15889) from candidate_words.json:

- **Nouns (16)**: {皆様|みなさま} (everyone, polite), {至|いた}る{所|ところ} (everywhere), {標識|ひょうしき} (sign/marker), お{悔|く}やみ (condolences), {首筋|くびすじ} (nape of the neck), {呼|よ}び{捨|す}て (calling without honorifics), {謙譲語|けんじょうご} (humble language), {同窓会|どうそうかい} (alumni reunion), {姿見|すがたみ} (full-length mirror), {反抗期|はんこうき} (rebellious phase), {留守番電話|るすばんでんわ} (voicemail), {三十路|みそじ} (thirty years old), {二桁|ふたけた} (double digits), {生|なま}クリーム (fresh cream), {化粧室|けしょうしつ} (powder room), {慈|いつく}しみ (compassion)
- **Noun/verb-suru (6)**: {直面|ちょくめん}する (to confront), {克服|こくふく}する (to overcome), {出国|しゅっこく} (departure from country), {積載|せきさい} (loading cargo), {抵抗|ていこう}する (to resist), {一礼|いちれい} (a bow)
- **Noun (multi-sense) (4)**: {終止符|しゅうしふ} (2: punctuation + figurative end), {殿|との} (2: feudal lord + husband), {同窓会|どうそうかい} (2: reunion + association), {抵抗|ていこう}する (2: resist + feel reluctant)
- **Noun/adverb (1)**: {間一髪|かんいっぱつ} (by a hair's breadth)
- **Na-adjective (1)**: {従順|じゅうじゅん} (obedient)
- **I-adjective (1)**: {騒々|そうぞう}しい (noisy)
- **Noun (other) (5)**: {悪臭|あくしゅう} (stench), {没落|ぼつらく} (downfall), {配色|はいしょく} (color scheme)

Notable features:
- Language/culture cluster: {謙譲語|けんじょうご}, {呼|よ}び{捨|す}て, {皆様|みなさま}
- Social/life: {同窓会|どうそうかい}, {反抗期|はんこうき}, お{悔|く}やみ, {化粧室|けしょうしつ}
- Travel: {出国|しゅっこく}, {留守番電話|るすばんでんわ}, {標識|ひょうしき}
- Multi-sense entries: {終止符|しゅうしふ} (punctuation + figurative), {殿|との} (lord + husband), {抵抗|ていこう} (physical + psychological)

Total entries: ~15,912 → ~15,942 (approximate)
Remaining candidates: ~3,861 → ~3,831 (30 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 402)
Added 30 new dictionary entries (IDs 15830-15859) from candidate_words.json:

- **Nouns (22)**: {父方|ちちかた} (paternal side), {次女|じじょ} (second daughter), {牢屋|ろうや} (jail), {大粒|おおつぶ} (large grain/drop), {揃|そろ}い (matching set), お{祓|はら}い (purification ritual), {世帯主|せたいぬし} (head of household), {管制塔|かんせいとう} (control tower), {海面|かいめん} (sea surface/level), {古文書|こもんじょ} (ancient document), {書式|しょしき} (format), {幼児語|ようじご} (baby talk), {専属|せんぞく} (exclusive), {糖分|とうぶん} (sugar content), {領海|りょうかい} (territorial waters), {甲斐|かい} (worth/reward), {屋根裏|やねうら} (attic), {渓流|けいりゅう} (mountain stream), {皇帝|こうてい} (emperor), {王国|おうこく} (kingdom), {海鳥|うみどり} (seabird), {暖気|だんき} (warm air)
- **Noun/verb-suru (7)**: {急成長|きゅうせいちょう} (rapid growth), {冬眠|とうみん} (hibernation), {介抱|かいほう} (nursing), {静止|せいし} (stillness), {暗算|あんざん} (mental arithmetic), {会釈|えしゃく} (slight bow), {入国|にゅうこく} (entry into country)
- **Noun with two senses (4)**: {海面|かいめん} (2: surface + level), {天敵|てんてき} (2: predator + nemesis), {守護神|しゅごしん} (2: deity + sports guardian), {王国|おうこく} (2: literal + figurative)

Notable features:
- Family cluster: {父方|ちちかた}, {次女|じじょ}, {世帯主|せたいぬし}
- Nature/geography: {海面|かいめん}, {渓流|けいりゅう}, {海鳥|うみどり}, {冬眠|とうみん}, {暖気|だんき}
- History/politics: {皇帝|こうてい}, {王国|おうこく}, {領海|りょうかい}, {古文書|こもんじょ}
- Daily life: {糖分|とうぶん}, {屋根裏|やねうら}, {暗算|あんざん}, {書式|しょしき}
- Multi-sense entries: {天敵|てんてき} (natural enemy + figurative nemesis), {冬眠|とうみん} (literal + figurative dormancy)

Total entries: ~15,884 → ~15,912 (approximate)
Remaining candidates: ~3,891 → ~3,861 (30 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 401)
Added 30 new dictionary entries (IDs 15800-15829) from candidate_words.json:

- **Nouns (16)**: {忘年会|ぼうねんかい} (year-end party), {化粧水|けしょうすい} (face lotion), {特売品|とくばいひん} (bargain item), {二代目|にだいめ} (second generation), {草餅|くさもち} (mugwort rice cake), {短文|たんぶん} (short sentence), {非接触|ひせっしょく} (contactless), {容積|ようせき} (capacity), {製紙|せいし} (papermaking), {再入場|さいにゅうじょう} (re-entry), {呪|のろ}い (curse), {丁寧語|ていねいご} (polite language), {初版|しょはん} (first edition), {難点|なんてん} (drawback), {手落|てお}ち (oversight), {利下|りさ}げ (interest rate cut)
- **Noun/verbal-noun (5)**: {禁酒|きんしゅ} (abstinence from alcohol), {準拠|じゅんきょ} (compliance), {承諾|しょうだく} (consent), {主催|しゅさい} (hosting), {音読|おんどく} (reading aloud)
- **Noun/verbal-noun (2-sense) (2)**: {染色|せんしょく} (dyeing/staining), {不妊|ふにん} (infertility)
- **Na-adjective (1)**: {無難|ぶなん} (safe/acceptable)
- **Adverb (2)**: {未|いま}だに (still/even now), {速|すみ}やかに (promptly)
- **Noun (literary) (2)**: {蛇足|だそく} (superfluous addition), {名|な}ばかり (in name only)
- **Noun (food) (1)**: {焼|や}き{菓子|がし} (baked goods)
- **Verb-godan (2-sense) (1)**: {突|つ}き{放|はな}す (to push away/reject coldly)

Notable features:
- Daily-life cluster: {忘年会|ぼうねんかい}, {化粧水|けしょうすい}, {特売品|とくばいひん}, {草餅|くさもち}, {焼|や}き{菓子|がし}
- Business/formal: {承諾|しょうだく}, {準拠|じゅんきょ}, {主催|しゅさい}, {手落|てお}ち, {利下|りさ}げ
- Language/education: {丁寧語|ていねいご}, {音読|おんどく}, {短文|たんぶん}
- Multi-sense entries: {禁酒|きんしゅ} (2: personal + legal), {染色|せんしょく} (2: textile + biology), {突|つ}き{放|はな}す (2: physical + emotional)

Total entries: ~15,854 → ~15,884 (approximate)
Remaining candidates: ~3,919 → ~3,891 (28 removed)

### 2026-03-08 (Vocabulary Expansion - 30 New Entries, Session 400)
Added 30 new dictionary entries (IDs 15769-15799) from candidate_words.json:

- **Nouns (15)**: {憎|にく}しみ (hatred), {差額|さがく} (difference), {隠|かく}し{事|ごと} (secret), {前払|まえばら}い (advance payment), {義兄|ぎけい} (brother-in-law), {定型文|ていけいぶん} (boilerplate text), {逃亡者|とうぼうしゃ} (fugitive), {銀貨|ぎんか} (silver coin), {濁流|だくりゅう} (muddy torrent), {原稿用紙|げんこうようし} (manuscript paper), {歓迎会|かんげいかい} (welcome party), {感電|かんでん} (electric shock), {整髪|せいはつ} (hairdressing), {無香料|むこうりょう} (fragrance-free), {内需|ないじゅ} (domestic demand)
- **Noun/adjective-no (1)**: {極上|ごくじょう} (finest quality)
- **Noun/verb-suru (3)**: {兼用|けんよう} (dual use), {開墾|かいこん} (land reclamation), {特急券|とっきゅうけん} (express ticket)
- **Noun/na-adjective (1)**: {意気地|いくじ}なし (coward)
- **Na-adjective (3)**: {丁重|ていちょう} (courteous), {庶民的|しょみんてき} (down-to-earth), {浅薄|せんぱく} (shallow)
- **Adjective-i (2)**: {古臭|ふるくさ}い (old-fashioned), おむつ → moved below
- **Verb-godan (1)**: {欲張|よくば}る (to be greedy)
- **Verb-ichidan (1)**: {押|お}しのける (to push aside)
- **Other nouns (3)**: おむつ (diaper), お{吸|す}い{物|もの} (clear soup), ひらめき (inspiration), {立|た}ち{回|まわ}り (maneuvering/fight scene)

Notable features:
- Daily-life cluster: おむつ, お{吸|す}い{物|もの}, {前払|まえばら}い, {特急券|とっきゅうけん}, {無香料|むこうりょう}
- Business: {差額|さがく}, {定型文|ていけいぶん}, {内需|ないじゅ}, {歓迎会|かんげいかい}
- Multi-sense entries: {古臭|ふるくさ}い (2: outdated + musty), {押|お}しのける (2: physical + figurative), {立|た}ち{回|まわ}り (2: social maneuvering + fight scene)
- New kanji: 2,522 → 2,523 ({墾|こん})

Total entries: ~15,824 → ~15,854 (approximate)
Remaining candidates: ~3,948 → ~3,919 (29 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
