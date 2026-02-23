# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-23
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
| Total entries | ~13,064 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~10,265 (open) |
| Candidate words | ~363 |
| Cross-references | ~3,400 |
| Example sentences | ~45,490 |
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

### 2026-02-23 (Vocabulary Expansion - 30 New Entries, Session 307)
Added 30 new dictionary entries (IDs 12979-13008) from candidate_words.json:

- **Noun/suru verbs (4)**: {戦死|せんし} (death in battle), {断絶|だんぜつ} (severance), {暗躍|あんやく} (secret maneuvering), {早寝|はやね} (going to bed early)
- **Nouns (16)**: {戦時|せんじ} (wartime), {新婦|しんぷ} (bride), {新郎|しんろう} (groom), {新曲|しんきょく} (new song), {新着|しんちゃく} (new arrival), {旅立|たびだ}ち (departure), {旅路|たびじ} (journey), {文豪|ぶんごう} (literary master), {文芸|ぶんげい} (literary art), {文語|ぶんご} (literary language), {昼夜|ちゅうや} (day and night), {晴|は}れ{着|ぎ} (formal clothes), {月収|げっしゅう} (monthly income), {月極|つきぎめ} (monthly rental), {月見|つきみ} (moon viewing), {朝市|あさいち} (morning market)
- **Na-adjective/nouns (5)**: {月並|つきな}み (commonplace), {有害|ゆうがい} (harmful), {有罪|ゆうざい} (guilty), {有益|ゆうえき} (beneficial), {有力|ゆうりょく} (influential)
- **Noun/pre-noun adjectival (1)**: {有数|ゆうすう} (prominent)
- **Nouns (2)**: {有志|ゆうし} (volunteers), {暗黒|あんこく} (darkness)
- **Adverb (1)**: {早晩|そうばん} (sooner or later)
- **Verb (1)**: {施|ほどこ}す (to apply/to give charity, godan)

Notable features:
- Multi-sense entries: {施|ほどこ}す (apply/give charity), {暗黒|あんこく} (physical darkness/figurative darkness), {有力|ゆうりょく} (influential/strong candidate), {月見|つきみ} (moon viewing/egg on food)
- Wedding pair: {新郎|しんろう} ↔ {新婦|しんぷ}
- Travel cluster: {旅立|たびだ}ち, {旅路|たびじ} (literary terms)
- Literature cluster: {文豪|ぶんごう}, {文芸|ぶんげい}, {文語|ぶんご}
- 有- prefix cluster: {有害|ゆうがい}, {有罪|ゆうざい}, {有益|ゆうえき}, {有志|ゆうし}, {有数|ゆうすう}, {有力|ゆうりょく}
- Cultural: {月見|つきみ} (autumn tradition + food), {晴|は}れ{着|ぎ} (hare/ke distinction), {朝市|あさいち} (Japanese market tradition)
- New kanji: 2,382 → 2,383 ({郎|ろう})

Total entries: 13,034 → 13,064 (approximate)
Remaining candidates: 393 → 363 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 306)
Added 30 new dictionary entries (IDs 12949-12978) from candidate_words.json:

- **Nouns (20)**: {旅先|たびさき} (travel destination), {旅客|りょかく} (passenger), {日取|ひど}り (scheduling a date), {日数|にっすう} (number of days), {日本酒|にほんしゅ} (Japanese sake), {日本食|にほんしょく} (Japanese food), {日系|にっけい} (of Japanese descent), {旧姓|きゅうせい} (maiden name), {旧暦|きゅうれき} (lunar calendar), {明|あか}るみ (coming to light), {昨今|さっこん} (nowadays), {昼過|ひるす}ぎ (early afternoon), {時事|じじ} (current affairs), {時代劇|じだいげき} (period drama), {時価|じか} (market price), {時点|じてん} (point in time), {時間帯|じかんたい} (time slot/time zone), {晴天|せいてん} (clear sky), {暑|あつ}さ (heat), {景観|けいかん} (landscape)
- **Verbs (4)**: {旅立|たびだ}つ (to depart on journey, godan), {昇|のぼ}る (to rise, godan), {明|あ}かす (to reveal/stay up all night, godan), {映|うつ}す (to reflect/project, godan)
- **Intransitive verb (1)**: {映|うつ}る (to be reflected/appear, godan)
- **Adverbs (2)**: {早々|そうそう} (promptly/right after), {暗|あん}に (implicitly)
- **Noun (1)**: {暴言|ぼうげん} (abusive language)
- **Expression (1)**: {敬具|けいぐ} (respectfully yours)
- **Noun (1)**: {教義|きょうぎ} (doctrine)

Notable features:
- Multi-sense entries: {旅立|たびだ}つ (journey/euphemism for death), {明|あ}かす (reveal/stay up all night), {映|うつ}す (reflect/project), {映|うつ}る (reflected/appear on screen), {早々|そうそう} (promptly/suffix: right after), {時間帯|じかんたい} (time slot/time zone)
- Transitive-intransitive pair: {映|うつ}す ↔ {映|うつ}る
- Homophone notes: {昇|のぼ}る vs {登|のぼ}る, {暑|あつ}さ vs {厚|あつ}さ vs {熱|あつ}さ, {映|うつ}す vs {写|うつ}す vs {移|うつ}す
- Cultural: {日本酒|にほんしゅ} (brewing terms), {旧暦|きゅうれき} (Meiji calendar reform), {旧姓|きゅうせい} (夫婦別姓 debate), {敬具|けいぐ} (letter writing conventions), {時代劇|じだいげき} (大河ドラマ)
- Time/日-related cluster: many entries built around 日, 時, 旧, 早, 昼, 明, 映, 昨, 晴, 暑, 暗, 暴, 景

Total entries: 13,004 → 13,034 (approximate)
Remaining candidates: 423 → 393 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 305)
Added 30 new dictionary entries (IDs 12919-12948) from candidate_words.json:

- **Noun/suru verbs (9)**: {探索|たんさく} (search/exploration), {撤収|てっしゅう} (withdrawal/removal), {改修|かいしゅう} (repair/renovation), {放出|ほうしゅつ} (release/emission), {救済|きゅうさい} (relief/salvation), {敬遠|けいえん} (keeping at arm's length/intentional walk), {支持|しじ} (support/backing), {摘発|てきはつ} (exposure/crackdown), {放映|ほうえい} (broadcasting)
- **Nouns (14)**: {攻防|こうぼう} (offense and defense), {救命|きゅうめい} (lifesaving), {教習所|きょうしゅうじょ} (driving school), {文体|ぶんたい} (writing style), {文化財|ぶんかざい} (cultural property), {支障|ししょう} (hindrance), {態勢|たいせい} (posture/readiness), {手先|てさき} (fingertips/agent), {手下|てした} (subordinate/henchman), {敗者|はいしゃ} (loser), {教員|きょういん} (teacher), {故事|こじ} (historical anecdote), {接点|せってん} (point of contact), {攻め|せめ} (attack/offense)
- **Verbs (3)**: {接|せっ}する (to adjoin/to treat, suru), {撃|う}つ (to shoot, godan), {改|あらた}める (to reform/examine, ichidan)
- **Godan verb (1)**: {揺|ゆ}るがす (to shake/undermine)
- **Noun/pre-noun adjectival (1)**: {所定|しょてい} (prescribed/designated)
- **Noun/adverb (1)**: {数多|かずおお}く (many/numerous)
- **Noun (1)**: {文書|ぶんしょ} (document)

Notable features:
- Multi-sense entries: {接|せっ}する (contact/treat), {敬遠|けいえん} (avoidance/baseball), {手先|てさき} (fingertips/pawn), {揺|ゆ}るがす (physical/figurative), {接点|せってん} (connection/electrical), {改|あらた}める (reform/inspect), {撤収|てっしゅう} (withdrawal/removal)
- Homophone cross-references: {改修|かいしゅう}↔{回収|かいしゅう}, {支持|しじ}↔{指示|しじ}, {支障|ししょう}↔{師匠|ししょう}, {敗者|はいしゃ}↔{歯医者|はいしゃ}, {態勢|たいせい}↔{体制|たいせい}, {故事|こじ}↔{誇示|こじ}
- Good mix of formal/institutional ({所定|しょてい}, {文書|ぶんしょ}, {教員|きょういん}) and everyday vocabulary ({教習所|きょうしゅうじょ}, {手下|てした})
- Cultural: {文化財|ぶんかざい} (property protection system), {故事|こじ} (Chinese classical origins), {敬遠|けいえん} (Confucian etymology)

Total entries: 12,974 → 13,004 (approximate)
Remaining candidates: 501 → 423 (30 removed, plus additional sync)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 304)
Added 30 new dictionary entries (IDs 12889-12918) from candidate_words.json:

- **Noun/suru verbs (21)**: {所蔵|しょぞう} (possession/holding), {投下|とうか} (dropping/investment), {投与|とうよ} (drug administration), {投入|とうにゅう} (throwing in/deployment), {折衝|せっしょう} (negotiation), {指令|しれい} (directive), {授与|じゅよ} (conferral), {採取|さいしゅ} (sampling), {探求|たんきゅう} (quest/inquiry), {接待|せったい} (business entertainment), {接触|せっしょく} (contact), {提示|ていじ} (presentation), {推奨|すいしょう} (recommendation), {推進|すいしん} (promotion/propulsion), {提供|ていきょう} (provision), {撤回|てっかい} (retraction), {撤廃|てっぱい} (abolition), {改心|かいしん} (change of heart), {敵対|てきたい} (hostility), {断言|だんげん} (declaration), {救出|きゅうしゅつ} (rescue)
- **Nouns (5)**: {抗体|こうたい} (antibody), {数値|すうち} (numerical value), {文庫本|ぶんこぼん} (paperback book), {敗戦|はいせん} (defeat in war), {摂氏|せっし} (Celsius)
- **Noun/no-adjective (2)**: {手動|しゅどう} (manual operation), {手製|てせい} (handmade)
- **Na-adjective (1)**: {抜本的|ばっぽんてき} (fundamental/radical)
- **Compound noun (1)**: {技術革新|ぎじゅつかくしん} (technological innovation)

Notable features:
- Multi-sense entries: {投下|とうか} (dropping/capital investment), {投入|とうにゅう} (inserting/deploying resources), {接待|せったい} (business entertainment/general hospitality), {接触|せっしょく} (physical/interpersonal contact), {推進|すいしん} (policy promotion/physical propulsion)
- Heavy concentration of formal/institutional vocabulary: negotiation, policy, medicine, law
- Business culture: {接待|せったい} (client entertainment), {折衝|せっしょう} (bargaining), {推奨|すいしょう} (endorsement)
- Medical/scientific: {投与|とうよ} (dosing), {抗体|こうたい} (antibody), {摂氏|せっし} (Celsius), {採取|さいしゅ} (sampling)
- Cultural: {文庫本|ぶんこぼん} (Japanese paperback format), {敗戦|はいせん} (WWII context)

Total entries: 12,944 → 12,974 (approximate)
Remaining candidates: 531 → 501 (30 removed)

### 2026-02-22 (Vocabulary Expansion - 30 New Entries, Session 303)
Added 30 new dictionary entries (IDs 12859-12888) from candidate_words.json:

- **Nouns - general (17)**: {暗闇|くらやみ} (darkness), {期限|きげん} (deadline), {杖|つえ} (cane), {束|つか}の{間|ま} (brief moment), {本心|ほんしん} (true feelings), {拠|よ}り{所|どころ} (foundation/support), {本場|ほんば} (place of origin), {文房具|ぶんぼうぐ} (stationery), {斜面|しゃめん} (slope), {本性|ほんしょう} (true nature), {教|おし}え{子|ご} (pupil), {指針|ししん} (guideline), {本題|ほんだい} (main topic), {教材|きょうざい} (teaching materials), {救|すく}い (salvation), {文献|ぶんけん} (literature/references), {書評|しょひょう} (book review)
- **Noun/suru verbs (6)**: {指名|しめい} (nomination), {敗北|はいぼく} (defeat), {捕獲|ほかく} (capture), {接客|せっきゃく} (customer service), {日持|ひも}ち (shelf life), {政権|せいけん} (political power)
- **Noun/no-adjectives (2)**: {暗黙|あんもく} (tacit/implicit), {新婚|しんこん} (newlywed)
- **I-adjective (1)**: {望|のぞ}ましい (desirable)
- **Ichidan verb (1)**: {押|お}し{上|あ}げる (to push up/boost)
- **Nouns - work/culture (3)**: {新卒|しんそつ} (new graduate), {振|ふ}り{付|つ}け (choreography), {本業|ほんぎょう} (main occupation)

Notable features:
- Multi-sense entries: {期限|きげん} (deadline/expiration), {押|お}し{上|あ}げる (physical/figurative), {拠|よ}り{所|どころ} (basis/emotional support), {指針|ししん} (guideline/needle)
- Cultural relevance: {新卒|しんそつ} (Japanese hiring system), {暗黙|あんもく} (indirect communication), {接客|せっきゃく} (service culture), {本場|ほんば} (food authenticity)
- Good mix of everyday vocabulary and formal/literary words

Total entries: 12,914 → 12,944 (approximate)
Remaining candidates: 327 → 297 (30 removed)

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
