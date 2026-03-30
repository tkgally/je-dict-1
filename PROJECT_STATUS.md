# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-29
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
| Total entries | ~19,058 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,259 (open) |
| Candidate words | ~5,099 |
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

### 2026-03-30 (Vocabulary Expansion - 25 New Entries, Session 544)
Added 25 new dictionary entries (IDs 20658-20682) from candidate_words.json. A diverse mix including verbs, nouns, expressions, and an adjective spanning everyday conversation, food, culture, and media vocabulary.

- **Godan verbs (2)**: {話|はな}し{込|こ}む (to get deeply involved in conversation), {恵|めぐ}む (to give charitably; to bless)
- **Suru verbs (5)**: {投入|とうにゅう}する (to throw in/invest), {寄付|きふ}する (to donate), {完了|かんりょう}する (to complete), {完結|かんけつ}する (to conclude), うんざりする (to be fed up)
- **Expressions (3)**: {嫌|いや}になる (to become fed up), お{疲|つか}れさまです (thank you for your work), {仲|なか}が{良|よ}い (to be on good terms)
- **Na-adjective (1)**: {爆発的|ばくはつてき} (explosive/phenomenal)
- **Nouns (14)**: {月光|げっこう} (moonlight), {捕虜|ほりょ} (prisoner of war), {施術|せじゅつ} (treatment/therapy), {半々|はんはん} (half and half), {紅|くれない} (crimson), {忠義|ちゅうぎ} (loyalty), {哺乳瓶|ほにゅうびん} (baby bottle), コク (richness of flavor), {脂身|あぶらみ} (fatty meat), {新品同様|しんぴんどうよう} (like new), {観光案内|かんこうあんない} (tourist information), {囚人|しゅうじん} (prisoner), {暴徒|ぼうと} (rioter), {大男|おおおとこ} (big man)
- Removed 25 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 15 New Entries, Session 543)
Added 15 new dictionary entries (IDs 20643-20657) from candidate_words.json. A mix of practical vocabulary including four-character idioms, everyday nouns, cultural terms, and workplace vocabulary.

- **Na-adjective (1)**: {明瞭|めいりょう} (clear/distinct)
- **Nouns (14)**: {半信半疑|はんしんはんぎ} (half in doubt), {集金|しゅうきん} (bill collection), {廃業|はいぎょう} (closing a business), {旅費|りょひ} (travel expenses), {子羊|こひつじ} (lamb), {羊毛|ようもう} (wool), {納戸|なんど} (storage room), {前期|ぜんき} (first term), {学童|がくどう} (schoolchild), あんみつ (Japanese dessert), {世相|せそう} (social conditions), {厳寒|げんかん} (severe cold), {能書|のうが}き (boasting), {庶務|しょむ} (general affairs)
- Removed 15 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 542)
Added 30 new dictionary entries (IDs 20613-20642) from candidate_words.json. A diverse mix of practical vocabulary covering nouns, expressions, na-adjectives, and adverbs for intermediate learners.

- **Na-adjectives (2)**: {鮮烈|せんれつ} (vivid/striking), {紳士的|しんしてき} (gentlemanly)
- **Expressions (3)**: {根|ね}も{葉|は}もない (groundless), {約束|やくそく}を{破|やぶ}る (to break a promise), {注目|ちゅうもく}を{浴|あ}びる (to attract attention)
- **Adverbs/expressions (2)**: {時間通|じかんどお}り (on time), {何|なん}でもかんでも (anything and everything)
- **Nouns (23)**: {装着|そうちゃく} (equipping), {編成|へんせい} (formation), {人件費|じんけんひ} (labor costs), {唯一無二|ゆいいつむに} (one and only), {様変|さまが}わり (transformation), {問題点|もんだいてん} (problem area), {脱皮|だっぴ} (molting/outgrowing), {裸眼|らがん} (naked eye), {漁港|ぎょこう} (fishing port), {無一文|むいちもん} (penniless), {指切|ゆびき}り (pinky swear), {大学院生|だいがくいんせい} (graduate student), {煮汁|にじる} (cooking liquid), {精密検査|せいみつけんさ} (detailed examination), {反省文|はんせいぶん} (reflection paper), {金券|きんけん} (cash voucher), {受験票|じゅけんひょう} (exam ticket), お{焦|こ}げ (scorched rice), {人事部|じんじぶ} (HR department), {明明後日|しあさって} (three days from now), {洗米|せんまい} (rice washing), おじいちゃん (grandfather), {諸外国|しょがいこく} (various foreign countries)
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 541)
Added 30 new dictionary entries (IDs 20583-20612) from candidate_words.json. A diverse mix of practical vocabulary including verbs, nouns, adjectives, and adverbs for intermediate learners.

- **Verbs (2)**: {儲|もう}ける (to make a profit), のぼせる (to feel flushed/to be infatuated)
- **Na-adjectives (2)**: {非公式|ひこうしき} (informal/unofficial), {怪奇|かいき} (mysterious/eerie)
- **Adverb (1)**: あたふた (in a fluster/hurriedly)
- **Nouns (25)**: {綱渡|つなわた}り (tightrope walking), {農場|のうじょう} (farm), {真冬|まふゆ} (midwinter), {民意|みんい} (public will), {俗語|ぞくご} (slang), {上陸|じょうりく} (landing), {牽制|けんせい} (check/restraint), {企画書|きかくしょ} (proposal), {入眠|にゅうみん} (falling asleep), {師範|しはん} (master instructor), {口外|こうがい} (disclosing), {平衡|へいこう} (equilibrium), {先達|せんだつ} (pioneer), {土木|どぼく} (civil engineering), {大慌|おおあわ}て (great panic), {含|ふく}み{笑|わら}い (smothered laugh), {画風|がふう} (artistic style), {元金|がんきん} (principal), {表舞台|おもてぶたい} (public spotlight), {放牧|ほうぼく} (grazing), {奇人|きじん} (eccentric), {言語化|げんごか} (verbalization), {背面|はいめん} (back side), {後発|こうはつ} (latecomer), {降車|こうしゃ} (getting off vehicle)
- Added 1 new kanji to index: 儲
- Removed 30 candidates that now exist as entries

### 2026-03-29 (Vocabulary Expansion - 30 New Entries, Session 540)
Added 30 new dictionary entries (IDs 20553-20582) from candidate_words.json. A diverse mix of practical vocabulary covering adjectives, adverbs, verbs, and nouns for intermediate learners.

- **Na-adjectives (5)**: {悪質|あくしつ} (malicious/poor quality), むやみ (reckless/excessive), {風変|ふうが}わり (eccentric), {移|うつ}り{気|ぎ} (fickle), ぶかぶか (baggy/too loose)
- **Adverbs (3)**: たった{今|いま} (just now), いっそのこと (might as well), もうそろそろ (pretty soon)
- **Suru-verbs (2)**: {緊張|きんちょう}する (to get nervous), {降伏|こうふく}する (to surrender)
- **Nouns (20)**: {検疫|けんえき} (quarantine), {富豪|ふごう} (wealthy person), {民話|みんわ} (folk tale), {家計簿|かけいぼ} (household budget book), {閣僚|かくりょう} (cabinet minister), {細部|さいぶ} (details), {原文|げんぶん} (original text), {冒険家|ぼうけんか} (adventurer), {刑罰|けいばつ} (criminal punishment), {文具|ぶんぐ} (stationery), {座右|ざゆう}の{銘|めい} (personal motto), {世代|せだい}{交代|こうたい} (generational change), {寓話|ぐうわ} (fable), {重心|じゅうしん} (center of gravity), {釣|つ}り{合|あ}い (balance), {眼前|がんぜん} (before one's eyes), {原動力|げんどうりょく} (driving force), {注意書|ちゅういが}き (cautionary note), {致死量|ちしりょう} (lethal dose), けなげさ (admirable courage)
- Added 1 new kanji to index: 寓
- Removed 30 candidates that now exist as entries





---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
