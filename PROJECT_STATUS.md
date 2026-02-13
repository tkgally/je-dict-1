# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-13
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
| Total entries | ~11,132 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,333 (open) |
| Candidate words | ~211 |
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

### 2026-02-13 (Vocabulary Expansion - 30 New Entries, Session 245)
Added 30 new dictionary entries (IDs 11055-11084) from candidate_words.json:

- **I-adjectives (3)**: {騒|さわ}がしい (noisy/turbulent), {慌|あわ}ただしい (hectic), めでたい (auspicious/naive)
- **Calendar nouns (2)**: {年末|ねんまつ} (year-end), {年始|ねんし} (beginning of year)
- **Communication/digital (3)**: {口|くち}コミ (word of mouth/reviews), {閲覧|えつらん} (browsing/viewing), {送信|そうしん} (sending/transmission)
- **Social/cultural (3)**: {恩返|おんがえ}し (returning a favor), {見返|みかえ}り (something in return), {社交辞令|しゃこうじれい} (social pleasantry)
- **Medical (7)**: {予防接種|よぼうせっしゅ} (vaccination), カルテ (medical chart), {問診|もんしん} (medical interview), {眼科|がんか} (ophthalmology), {歯科|しか} (dentistry), {皮膚科|ひふか} (dermatology), {採血|さいけつ} (blood draw)
- **Health/body (3)**: {悪化|あっか} (deterioration), {不眠|ふみん} (insomnia), {熟睡|じゅくすい} (deep sleep)
- **Verb (1)**: {繕|つくろ}う (to mend/keep up appearances)
- **Business/legal (2)**: {取引先|とりひきさき} (business partner), {被告|ひこく} (defendant)
- **Other nouns (6)**: {泥沼|どろぬま} (quagmire), {番狂|ばんくる}わせ (upset), {花壇|かだん} (flower bed), {自尊心|じそんしん} (self-esteem), {膨張|ぼうちょう} (expansion), {結露|けつろ} (condensation)

Notable features:
- Medical department cluster ({眼科|がんか}/{歯科|しか}/{皮膚科|ひふか}) with cross-references between them
- Antonym pairs: {不眠|ふみん} ↔ {熟睡|じゅくすい}, {恩返|おんがえ}し ↔ {見返|みかえ}り (related)
- Multi-sense entries: {騒|さわ}がしい (noise/turmoil), めでたい (auspicious/naive), {繕|つくろ}う (mend/appearances), {泥沼|どろぬま} (literal/figurative)
- Cultural notes: めでたい (鯛 pun), {社交辞令|しゃこうじれい} (reading Japanese sincerity), カルテ (German medical influence)
- Calendar pair: {年末|ねんまつ}/{年始|ねんし} with {年末年始|ねんまつねんし} compound

Total entries: 11,102 → 11,132
Remaining candidates: 241 → 211

### 2026-02-12 (New Candidate Words - 55 Words, Session 244)
Added 55 new candidate words to candidate_words.json across diverse domains:

- **Legal/criminal justice (5)**: 被告 (defendant), 原告 (plaintiff), 検察 (prosecution), 懲役 (imprisonment), 証言 (testimony)
- **Medical specialties & visits (9)**: 予防接種 (vaccination), カルテ (medical chart), 問診 (medical interview), 抗生物質 (antibiotic), 眼科 (ophthalmology), 歯科 (dentistry), 皮膚科 (dermatology), 初診 (first visit), 採血 (blood draw)
- **Health/nutrition (4)**: 糖質 (carbohydrates), 脂質 (lipids), 新陳代謝 (metabolism), コレステロール (cholesterol)
- **Internet/communication (4)**: 口コミ (word of mouth/reviews), 閲覧 (browsing), 送信 (sending), 回線 (circuit/line)
- **Sports/fitness (3)**: 体幹 (core/trunk), 反復 (repetition), 番狂わせ (upset)
- **Social/cultural (4)**: 社交辞令 (social pleasantry), 冠婚葬祭 (ceremonial occasions), 恩返し (returning a favor), 見返り (something in return)
- **Calendar (2)**: 年末 (year-end), 年始 (beginning of year)
- **Education (2)**: 修士 (master's degree), 模試 (mock exam)
- **Business/construction (2)**: 決裁 (approval), 着工 (start of construction)
- **Music (2)**: 指揮 (conducting/command), 譜面 (musical score)
- **Home/daily life (3)**: 排水 (drainage), 結露 (condensation), 繕う (to mend)
- **Psychology (2)**: 自尊心 (self-respect), 燃え尽き (burnout)
- **Science (2)**: 膨張 (expansion), 窒素 (nitrogen)
- **Adjectives (3)**: 騒がしい (noisy), 慌ただしい (hectic), めでたい (auspicious)
- **～化 compounds (3)**: 悪化 (deterioration), 深刻化 (worsening), 長期化 (prolongation)
- **Sleep (2)**: 不眠 (insomnia), 熟睡 (deep sleep)
- **Other (3)**: 取引先 (business partner), 内覧 (property viewing), 花壇 (flower bed)

Strategies used: semantic domain exploration (medical, legal, nutrition, home), practical situation vocabulary, corpus-driven gap analysis, collocational mining, productive pattern completion (～化 compounds)

Candidate words: 130 → 185

### 2026-02-12 (Vocabulary Expansion - 30 New Entries, Session 243)
Added 30 new dictionary entries (IDs 11025-11054) from candidate_words.json:

- **Katakana loanword nouns (30)**: ゼリー (jelly), ソロ (solo), ソーセージ (sausage), デンプン (starch), チキン (chicken), ゼネコン (general contractor), ソーダ (soda), ゾーン (zone), タグ (tag), タワー (tower), ターゲット (target), ターミナル (terminal), ダイヤモンド (diamond), ダミー (dummy), チェス (chess), チェーン{店|てん} (chain store), チャート (chart), ツール (tool), トピック (topic), スタッフ (staff), スピード (speed), スペース (space), セールス (sales), ジョーク (joke), スパイス (spice), スタート (start), ジャンプ (jump), ステージ (stage)
- **Noun + suru verb (4)**: セーブ (save — gaming/sports), ツイート (tweet), ジャンプ (jump), スタート (start)
- **Multi-sense entries (3)**: セーブ (save data/sports save), チャート (graph/music ranking), ステージ (performance stage/phase)

Notable features:
- Focus on commonly used katakana loanwords filling vocabulary gaps
- Japan-specific usage notes: チキン (Christmas chicken custom), ソーダ (メロンソーダ/クリームソーダ culture), ゼネコン (wasei-eigo abbreviation), タワーマンション (urban housing)
- Meaning restrictions vs English: セーブ (not for saving money/people), ツール (mainly software, not physical tools), スペース (not outer space), セールス (active selling, not セール discount events)
- Digital/internet vocabulary: ツイート, タグ, ツール

Total entries: 11,016 → 11,046
Remaining candidates: 160 → 130

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

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
