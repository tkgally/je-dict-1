# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-12
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
| Total entries | ~11,016 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,217 (open) |
| Candidate words | ~160 |
| Cross-references | ~3,332 |
| Example sentences | ~41,820 |
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

### 2026-02-12 (Vocabulary Expansion - 30 New Entries, Session 242)
Added 30 new dictionary entries (IDs 10995-11024) from candidate_words.json:

- **Food nouns (8)**: {筍|たけのこ} (bamboo shoot), {照|て}り{焼|や}き (teriyaki), {豚骨|とんこつ} (pork bone/tonkotsu), チャーシュー (char siu), チャーハン (fried rice), ソフトクリーム (soft serve), ソース (sauce/source), トッピング (topping)
- **People/social nouns (2)**: セレブ (celebrity/wealthy person), チンピラ (punk/thug)
- **Clothing/culture (2)**: セーラー{服|ふく} (sailor uniform), {染井吉野|そめいよしの} (Somei-Yoshino cherry)
- **Loanword nouns (10)**: ダイエット (diet), トラウマ (trauma), デリカシー (sensitivity), タイアップ (tie-up), タイミング (timing), テーマ (theme), チャレンジ (challenge), チケット (ticket), ダメージ (damage), デビュー (debut)
- **Entertainment/media (3)**: ジャンル (genre), ストーリー (story/plot), デフォルメ (stylized exaggeration)
- **Multi-sense noun (1)**: チップ (tip/chip)
- **Onomatopoeia/mimetic (3)**: ジロリ (piercing glare), ジーンと (feeling moved/tingling), トントン (knock-knock/break even)
- **Na-adjective (1)**: スムーズ (smooth)

Notable features:
- Food vocabulary cluster: Japanese cuisine terms ({筍|たけのこ}, {照|て}り{焼|や}き, {豚骨|とんこつ}) and ramen terminology (チャーシュー, トッピング, {豚骨|とんこつ})
- Meaning shifts from English: セレブ (wealth > fame), チャレンジ (positive attempt > confrontation), デリカシー (negative only), ソフトクリーム (wasei-eigo)
- Multi-sense entries: ソース (sauce/source), チップ (tip/chip), ジーンと (emotional/physical), トントン (sound/break even)
- Cultural notes: セーラー{服|ふく} (school uniform transition), {染井吉野|そめいよしの} (cherry blossom forecast standard), チップ (no tipping culture in Japan)
- German origin: テーマ (from Thema, not English "theme")
- New kanji: 2,293 → 2,295 (吉, 筍)

Total entries: 10,986 → 11,016
Remaining candidates: 190 → 160

### 2026-02-12 (Vocabulary Expansion - 30 New Entries, Session 241)
Added 30 new dictionary entries (IDs 10965-10994) from candidate_words.json:

- **Verb (1)**: {差|さ}す (to hold up/shine/pour — distinct from 刺す/指す/射す)
- **Conversational responses (5)**: そうだね (yeah, that's right), そうかな (I wonder), そうかも (maybe so), だよな (right? — masculine), だろ (right? — assertive)
- **Everyday state expressions (3)**: つかれた (I'm tired), おなかすいた (I'm hungry), のどかわいた (I'm thirsty)
- **Emotional reactions (5)**: まじかよ (are you serious?), やらかした (I screwed up), やっちゃった (oops), だめだ (it's no good), むりだ (impossible)
- **Situational expressions (4)**: なにこれ (what's this?), ちょっとまって (wait a sec), こまったな (that's a problem), なんでだろう (I wonder why)
- **Discourse connectors (2)**: そんなわけで (so for that reason), てなわけで (so basically)
- **Indifference expressions (2)**: どこでもいい (anywhere's fine), いつでもいい (anytime's fine)
- **Back-channel / interjections (3)**: うんうん (uh-huh), ちぇっ (tch), すっごい (really amazing)
- **Cultural expression (1)**: {空気|くうき}{読|よ}めない (can't read the room / KY)
- **Modern term (1)**: {格安|かくやす}SIM (budget SIM card)
- **Youth slang (3)**: とりま (for now), りょ (got it), あざす (thanks)

Notable features:
- Focus on casual spoken expressions and conversational building blocks for intermediate learners
- Agreement spectrum: そうだね (full) → そうかも (tentative) → そうかな (doubtful)
- Body-state expression pattern: つかれた/おなかすいた/のどかわいた (past tense for current state)
- Mistake expression gradient: やっちゃった (minor) → やらかした (major)
- Gender notes: だよな/だろ/まじかよ (masculine) vs だよね/でしょ/うそでしょ (feminine equivalents)
- Cultural concept: {空気|くうき}{読|よ}めない (KY) — core Japanese social skill of reading unspoken atmosphere
- Modern abbreviation chains: ありがとうございます→あざす, {了解|りょうかい}→りょ, とりあえず→とりま

Total entries: 10,956 → 10,986
Remaining candidates: 121 → 91

### 2026-02-11 (Vocabulary Expansion - 30 New Entries, Session 240)
Added 30 new dictionary entries (IDs 10935-10964) from candidate_words.json:

- **Nouns (20)**: サウナ (sauna), サプライズ (surprise), サプリメント (supplement), サミット (summit), サンプル (sample), サロン (salon), サバイバル (survival), サポーター (supporter/brace), シート (sheet/seat), シネマ (cinema), シグナル (signal), シューズ (shoes), カウンセリング (counseling), カリキュラム (curriculum), シンボル (symbol), サウンド (sound), カルシウム (calcium), サブカルチャー (subculture), シソ (perilla/shiso), シリーズ (series)
- **Na-adjectives (2)**: シビア (severe), シンプル (simple)
- **Multi-category nouns (5)**: シングル (single — room/music/unmarried), ショー (show), ショート (short/short circuit), シーズン (season — time/TV), シナリオ (scenario/script)
- **Noun + suru verb (2)**: シミュレーション (simulation), ショート (short circuit)
- **Onomatopoeia (1)**: ザクザク (crunchy/in abundance)

Notable features:
- Katakana loanwords filling common gaps, plus Japanese onomatopoeia and food vocabulary
- Multi-sense entries: シナリオ (script/projected events), シーズン (time of year/TV season), シート (flat sheet/seat), シングル (room/music/unmarried), ショート (hair length/short circuit), サロン (beauty/online community), サポーター (sports fan/brace), ザクザク (crunchy sound/abundance)
- Japan-specific concepts: サウナ (Japanese sauna cycle with 水風呂 and 整う), サプライズ (positive surprises only), ショートケーキ (strawberry sponge, not American shortcake), ブルーシート (iconic Japanese tarp), オンラインサロン (paid membership communities), サバイバルゲーム/サバゲー (airsoft), シミュレーション (common mispronunciation note), 食品サンプル (plastic food models)
- Cultural notes: シソ (大葉 naming distinction), カルシウム (folk wisdom about irritability), サブカルチャー (otaku culture focus in Japanese usage)

Total entries: 10,926 → 10,956
Remaining candidates: 151 → 121

### 2026-02-11 (Vocabulary Expansion - 30 New Entries, Session 239)
Added 30 new dictionary entries (IDs 10905-10934) from candidate_words.json:

- **Adjectives (5)**: {殺風景|さっぷうけい} (bleak), {律儀|りちぎ} (conscientious), {気難|きむずか}しい (hard to please), {名残惜|なごりお}しい (reluctant to part), {人懐|ひとなつ}っこい (friendly)
- **Na-adjectives/nouns (2)**: {無頓着|むとんちゃく} (indifferent), {短気|たんき} (short-tempered)
- **Cultural/social nouns (5)**: {相槌|あいづち} (back-channel response), {仕草|しぐさ} (gesture), {立|た}ち{読|よ}み (reading in store), {十八番|おはこ} (specialty), {食|く}い{逃|に}げ (dine and dash)
- **Abstract nouns (6)**: {融通|ゆうずう} (flexibility), {断片|だんぺん} (fragment), {痕跡|こんせき} (trace), {自惚|うぬぼ}れ (vanity), {頭打|あたまう}ち (plateauing), {落|お}とし{穴|あな} (pitfall)
- **Nature/science nouns (3)**: {脱水|だっすい} (dehydration), {侵食|しんしょく} (erosion), {渓谷|けいこく} (valley)
- **Time/discourse (3)**: {潮時|しおどき} (opportune time), {所詮|しょせん} (after all), {煽|あお}り (provocation/fallout)
- **Food nouns (3)**: サクランボ (cherry), シイタケ (shiitake), シチュー (stew)
- **Commerce/lifestyle (3)**: {卸|おろし} (wholesale), サークル (club/circle), シフト (shift)

Notable features:
- Diverse vocabulary: personality traits, cultural concepts, food, nature, business
- Multi-sense entries: {融通|ゆうずう} (flexibility/financing), {脱水|だっすい} (dehydration/spin-dry), {侵食|しんしょく} (erosion literal/figurative), {煽|あお}り (provocation/fallout), {落|お}とし{穴|あな} (trap/hidden risk), サークル (university club/circle shape), シフト (work schedule/transition)
- Cultural notes: {相槌|あいづち} (back-channeling in Japanese conversation), {十八番|おはこ} (kabuki origin), {立|た}ち{読|よ}み (convenience store culture), {短気|たんき}は{損気|そんき} proverb
- New kanji: 2,289 → 2,293 (侵, 渓, 痕, 詮)

Total entries: 10,896 → 10,926
Remaining candidates: 181 → 151

### 2026-02-11 (Vocabulary Expansion - 30 New Entries, Session 238)
Added 30 new dictionary entries (IDs 10875-10904) from candidate_words.json:

- **Verbs (12)**: {促|うなが}す (urge), {遮|さえぎ}る (block), {委|ゆだ}ねる (entrust), {募|つの}る (recruit/intensify), {率|ひき}いる (lead), {嫉|ねた}む (envy), {滅|ほろ}びる (perish), {偽|いつわ}る (deceive), {償|つぐな}う (atone), {侮|あなど}る (underestimate), {宥|なだ}める (soothe), {弾|はじ}く (flick/repel)
- **Abstract/emotional nouns (5)**: {陰謀|いんぼう} (conspiracy), {慈悲|じひ} (compassion), {憤|いきどおり} (indignation), {義理|ぎり} (social obligation), {伏線|ふくせん} (foreshadowing)
- **Noun + na-adjective (2)**: {寛容|かんよう} (tolerance), {壮大|そうだい} (magnificent)
- **Na-adjective (1)**: {過酷|かこく} (harsh)
- **Noun + suru verb (5)**: {献身|けんしん} (devotion), {示唆|しさ} (suggestion), {言及|げんきゅう} (mention), {生成|せいせい} (generation), {精算|せいさん} (settlement)
- **Nouns (4)**: {遺言|ゆいごん} (will/testament), {採算|さいさん} (profitability), {下請|したう}け (subcontracting), {一連|いちれん} (series)
- **Noun + suru verb (1)**: {連鎖|れんさ} (chain reaction)

Notable features:
- Focus on literary/formal Japanese vocabulary — verbs, abstract nouns, and academic terms
- Multi-sense entries: {募|つの}る (recruit/intensify), {偽|いつわ}る (deceive/falsify), {弾|はじ}く (flick/repel/calculate), {遮|さえぎ}る (block/interrupt), {義理|ぎり} (duty/in-law prefix), {促|うなが}す (urge/stimulate)
- Cultural concepts: {義理|ぎり} (義理チョコ, 義理と人情), {慈悲|じひ} (Buddhist compassion), {伏線|ふくせん} (foreshadowing in media criticism), {下請|したう}け (Japanese industrial subcontracting pyramid)
- Business vocabulary: {採算|さいさん}, {精算|せいさん}, {下請|したう}け
- New kanji: 2,284 → 2,289 (唆, 宥, 慈, 謀, 遮)

Total entries: 10,866 → 10,896
Remaining candidates: 211 → 181

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
