# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-03-30
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

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 547)
Added 30 new dictionary entries (IDs 20743-20772) from candidate_words.json. A diverse mix of nouns, na-adjectives, adverbs, and expressions covering language, culture, technology, geography, and daily life.

- **Na-adjectives (3)**: {立体的|りったいてき} (three-dimensional), {非人道的|ひじんどうてき} (inhumane), {淡麗|たんれい} (light and clean/refined)
- **Adverbs (2)**: すらり (slenderly/smoothly), {今|いま}でも (even now/still)
- **Expressions (1)**: せいで (because of — negative cause)
- **Nouns (24)**: {初学者|しょがくしゃ} (beginner), {寂寥感|せきりょうかん} (sense of desolation), {操縦士|そうじゅうし} (pilot), {離着陸|りちゃくりく} (takeoff and landing), {小型化|こがたか} (miniaturization), {出自|しゅつじ} (origin/lineage), {識見|しきけん} (insight), {史料|しりょう} (historical materials), {雅号|がごう} (pen name), {社殿|しゃでん} (shrine building), {残額|ざんがく} (remaining balance), {非公表|ひこうひょう} (undisclosed), {視覚化|しかくか} (visualization), {巧妙化|こうみょうか} (growing sophistication), {後|うし}ろ{髪|がみ} (back hair/lingering attachment), {実線|じっせん} (solid line), {破線|はせん} (dashed line), {中黒|なかぐろ} (interpunct), {姉|ねえ}さん (older sister/miss), {極大|きょくだい} (maximum), {修理中|しゅうりちゅう} (under repair), {使用禁止|しようきんし} (prohibited for use), {地中海|ちちゅうかい} (Mediterranean), おさげ (braids/pigtails)
- Removed 30 candidates that now exist as entries

### 2026-03-30 (Vocabulary Expansion - 30 New Entries, Session 546)
Added 30 new dictionary entries (IDs 20713-20742) from candidate_words.json. A diverse mix of verbs, nouns, adjectives, adverbs, and an onomatopoeia covering everyday communication, writing, math, food, and personality vocabulary.

- **Godan verbs (6)**: {割|わ}り{切|き}る (to accept rationally), {仄|ほの}めかす (to hint), {押|お}し{通|とお}す (to push through), {突|つ}っつく (to poke/peck), {書|か}き{写|うつ}す (to copy down), {書|か}き{抜|ぬ}く (to extract by writing)
- **Ichidan verb (1)**: くじける (to be discouraged; to sprain)
- **Suru verbs (3)**: {熱中|ねっちゅう}する (to be absorbed in), {断念|だんねん}する (to give up), {退会|たいかい}する (to cancel membership)
- **Na-adjectives (2)**: {気長|きなが} (patient), {小心|しょうしん} (timid)
- **Adverbs (3)**: どろどろ (muddy/sordid), だいぶん (considerably), {順|じゅん}に (in order)
- **Nouns (15)**: {切|き}れ{目|め} (break/gap), {葉巻|はまき} (cigar), {草稿|そうこう} (draft), {総数|そうすう} (total number), {小計|しょうけい} (subtotal), {食前|しょくぜん} (before a meal), {素数|そすう} (prime number), {店先|みせさき} (storefront), {大聖堂|だいせいどう} (cathedral), {真|ま}っ{二|ふた}つ (right in half), {話|はな}しぶり (way of speaking), {季節感|きせつかん} (sense of season), {倍数|ばいすう} (multiple), {原寸大|げんすんだい} (full-size), {利|き}き{腕|うで} (dominant arm)
- Added 1 new kanji to index: 仄
- Removed 29 candidates that now exist as entries

### 2026-03-30 (Vocabulary Expansion - 29 New Entries, Session 545)
Added 29 new dictionary entries (IDs 20683-20712) from candidate_words.json. A diverse mix including nouns, expressions, and a na-adjective covering everyday life, travel, food, business, and education vocabulary.

- **Na-adjective (1)**: {短絡的|たんらくてき} (hasty/simplistic)
- **Expressions (3)**: {物腰|ものごし}が{柔|やわ}らかい (soft-spoken), {一歩|いっぽ}も{引|ひ}かない (to not back down), {心|こころ}に{響|ひび}く (to strike a chord)
- **Nouns (25)**: ポリ{袋|ぶくろ} (plastic bag), {在日|ざいにち} (resident in Japan), {紛失届|ふんしつとどけ} (lost property report), {埠頭|ふとう} (wharf), {折|お}れ{線|せん}グラフ (line graph), {棒|ぼう}グラフ (bar graph), {小売店|こうりてん} (retail store), {預|あず}け{入|い}れ{荷物|にもつ} (checked baggage), どんぶり{勘定|かんじょう} (sloppy accounting), {断線|だんせん} (disconnection), {学|まな}び{舎|や} (school/place of learning), {継子|ままこ} (stepchild), {月額制|げつがくせい} (monthly subscription), {創刊号|そうかんごう} (first issue), {清掃員|せいそういん} (cleaning staff), {路肩|ろかた} (road shoulder), フランチャイズ (franchise), {水浸|みずびた}し (flooded), {薄力粉|はくりきこ} (cake flour), {強力粉|きょうりきこ} (bread flour), {締|し}めくくり (conclusion), {最下位|さいかい} (last place), {庭仕事|にわしごと} (garden work), {幸福度|こうふくど} (happiness index), {完結編|かんけつへん} (final volume)
- Added 1 new kanji to index: 埠
- Removed 1 stale candidate (duplicate reading variant)
- Removed 1 duplicate entry ({肩代|かたが}わり — already existed as ID 20190)

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






---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
