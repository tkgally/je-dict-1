# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-02-11
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
| Total entries | ~10,896 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~8,097 (open) |
| Candidate words | ~181 |
| Cross-references | ~3,332 |
| Example sentences | ~41,570 |
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

### 2026-02-11 (New Candidate Words - 55 Words, Session 237)
Added 55 new candidate words to candidate_words.json using diverse search strategies:

- **Verbs (12)**: 促す (urge), 遮る (block), 委ねる (entrust), 募る (recruit/intensify), 率いる (lead), 嫉む (envy), 滅びる (perish), 偽る (deceive), 償う (atone), 侮る (underestimate), 宥める (soothe), 弾く (flick/repel)
- **Abstract/emotional nouns (7)**: 陰謀 (conspiracy), 寛容 (tolerance), 慈悲 (compassion), 憤り (indignation), 義理 (social obligation), 献身 (devotion), 自惚れ (conceit)
- **Academic/legal (4)**: 示唆 (implication), 言及 (mention), 生成 (generation), 遺言 (will/testament)
- **Business/commerce (4)**: 採算 (profitability), 下請け (subcontracting), 精算 (settlement), 卸 (wholesale)
- **Adjectives/personality (7)**: 壮大 (magnificent), 過酷 (harsh), 殺風景 (bleak), 律儀 (conscientious), 気難しい (fussy), 名残惜しい (reluctant to part), 無頓着 (indifferent)
- **Personality traits (3)**: 人懐っこい (friendly), 短気 (short-tempered), 融通 (flexibility)
- **Nature/science (3)**: 脱水 (dehydration), 渓谷 (valley), 侵食 (erosion)
- **Discourse/narrative (5)**: 伏線 (foreshadowing), 連鎖 (chain reaction), 一連 (series), 煽り (instigation), 断片 (fragment)
- **Cultural/social (5)**: 相槌 (back-channel response), 仕草 (gesture), 食い逃げ (dine and dash), 立ち読み (reading in store), 十八番 (specialty)
- **Expressions/trends (5)**: 所詮 (after all), 潮時 (opportune time), 頭打ち (plateauing), 落とし穴 (pitfall), 痕跡 (trace)

Search strategies used: corpus-driven gap analysis, semantic domain exploration, collocational mining, register/formality pairs, practical situation vocabulary, productive pattern completion, cross-reference expansion

Candidate words: 156 → 211

### 2026-02-11 (Vocabulary Expansion - 30 New Entries, Session 236)
Added 30 new dictionary entries (IDs 10845-10874) from candidate_words.json:

- **Nouns (17)**: グルメ (gourmet/foodie), グレーゾーン (grey area), ゲスト (guest), ゲート (gate), コイン (coin), コスメ (cosmetics), コメディ (comedy), コラム (column), コロッケ (croquette), コンクリート (concrete), コンセプト (concept), コース (course), コーナー (corner/section), コーラ (cola), コミック (comic), キー (key), クライマックス (climax)
- **Nouns + suru verb (5)**: ゲット (get), コラボ (collaboration), コントロール (control), カスタマイズ (customize), キャッチ (catch)
- **Nouns + na-adjective (3)**: グローバル (global), コンパクト (compact), グルメ (gourmet)
- **Nouns (person) (2)**: クリエイター (creator), キャスト (cast)
- **Nouns (emotion) (1)**: コンプレックス (inferiority complex)
- **Nouns (multi-sense) (1)**: コンタクト (contact lenses/getting in touch)
- **Noun + suru verb + care (1)**: ケア (care/caregiving)
- **Onomatopoeia (1)**: ゴリゴリ (grinding/hardcore)

Notable features:
- Katakana loanwords covering common everyday vocabulary gaps
- Multi-sense entries: コンタクト (lenses/communication), コース (route/set meal), コーナー (corner/section), キャッチ (catch/catchphrase/street tout), ケア (caregiving/skincare), グルメ (person/food), ゴリゴリ (grinding/hardcore)
- Japan-specific concepts: コロッケ (yoshoku comfort food), コンパクト (positive space efficiency), コンプレックス (inferiority complex only), キャッチ (street solicitation), キーホルダー (wasei-eigo for keychain), B級グルメ (budget gourmet), クライマックスシリーズ (NPB playoffs)
- Cultural notes: コロッケ as 庶民の味, コンセプトカフェ culture, Disney キャスト tradition

Total entries: 10,836 → 10,866
Remaining candidates: 121 → 119

### 2026-02-10 (Vocabulary Expansion - 30 New Entries, Session 235)
Added 30 new dictionary entries (IDs 10815-10844) from candidate_words.json:

- **Nouns (22)**: キッチン (kitchen), カウンター (counter), カテゴリー (category), キャンパス (campus), キリスト教 (Christianity), ギフト (gift), クレジット (credit), グランプリ (grand prix), オプション (option), オーナー (owner), キーワード (keyword), ギャラリー (gallery), ガイドライン (guideline), キャッシュカード (ATM card), キャラメル (caramel), キムチ (kimchi), オーディション (audition), オープニング (opening), ガイダンス (guidance), カーボン (carbon), カルチャー (culture)
- **Nouns + suru verb (3)**: カット (cut), キープ (keep), クリア (clear)
- **Nouns + na-adjective (3)**: カオス (chaos), オープン (open), カラー (color)
- **Nouns + no-adjective (1)**: オリジナル (original)
- **Onomatopoeia (1)**: ガタゴト (rumbling, clattering)

Notable features:
- Primarily katakana loanwords filling major gaps in common everyday vocabulary
- Multi-sense entries: カウンター (service desk/counterattack), カラー (color/hair coloring), キャリア (career/phone carrier), クリア (clear/pass/transparent), クレジット (payment/attribution), ギャラリー (art gallery/spectators), カット (haircut/deletion), キープ (maintain/bottle keep), オープン (grand opening/open-minded), オリジナル (unique creation/source version)
- Japan-specific concepts: ボトルキープ (bottle keep at bars), カルチャースクール (hobby classes), システムキッチン (built-in kitchen units), キャッシュカード (ATM-only bank card)
- Cross-reference: キッチン↔台所

Total entries: 10,806 → 10,836
Remaining candidates: 151 → 121

### 2026-02-10 (Vocabulary Expansion - 30 New Entries, Session 234)
Added 30 new dictionary entries (IDs 10785-10814) from candidate_words.json:

- **Nouns (21)**: おんぼろ (shabby), {牡蠣|かき} (oyster), カステラ (castella cake), {蕪|かぶ} (turnip), {干瓢|かんぴょう} (dried gourd), がらくた (junk), カニカマ (imitation crab), キクラゲ (wood ear mushroom), キャッチコピー (catchphrase), クッキー (cookie), クッション (cushion), グッズ (merchandise), カクテル (cocktail), カタログ (catalog), オムレツ (omelette), オリーブ (olive), キャンペーン (promotion), ギャグ (gag/joke), ギャンブル (gambling), グラウンド (playing field), クローン (clone)
- **Onomatopoeia/mimetic (4)**: かんかん (furious/scorching/clanging), ガクガク (shaking), ギザギザ (jagged), ぐず (slowpoke)
- **Na-adjectives (2)**: カラフル (colorful), カチューシャ (headband)
- **Multi-sense (3)**: {肝|きも} (key point/liver), クッション (cushion/buffer), クラブ (club/nightclub)

Notable features:
- Food and ingredients cluster: {牡蠣|かき}, カステラ, {蕪|かぶ}, {干瓢|かんぴょう}, カニカマ, キクラゲ, クッキー, オムレツ, オリーブ, カクテル
- Japanese food culture: regional specialties ({長崎|ながさき}カステラ, {広島|ひろしま}{牡蠣|かき}, {小豆島|しょうどしま}オリーブ)
- Wasei-eigo: キャッチコピー (catch + copy), カニカマ (crab + kamaboko)
- Onomatopoeia: かんかん (3 senses), ガクガク, ギザギザ
- New kanji: 2,281 → 2,284 (瓢, 蕪, 蠣)

Total entries: 10,776 → 10,806
Remaining candidates: 104 → 151

---

**Archive Note**: Only the 5 most recent change log entries are shown above. When adding a new entry here, move the oldest one to [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md) to maintain this limit.

For earlier changes, see [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).
