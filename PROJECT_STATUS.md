# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-06-16
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
| Total entries | ~19,088 |
| Basic tier | 801 (closed) |
| Core tier | 1,998 (closed) |
| General tier | ~16,289 (open) |
| Candidate words | ~5,472 |
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

### 2026-06-18 (Routine v2: new-entries — 13 New Entries, IDs 29324–29336)
Added 13 curated standalone entries plus the 2 priority seen-in-entry gaps. The candidate pool outside the seen-in-entry set remains overwhelmingly corpus-harvest noise (bare numbers/counters, non-lexical fragments, transparent 〜率/〜化/〜性 compounds, ad-hoc phrases), so standalone picks were hand-selected for genuine dictionary-worthiness rather than padding to ~20. Dropped 段ボール箱 (transparent compound already covered by 18885 段ボール). Added 軸受け (じくうけ) as a candidate from 29330's similar-words note. Logged a [pattern] observation requesting a curator cleanup/restock of candidate_words.json.

- **Seen-in-entry (2)**: {捨|す}て{猫|ねこ} (abandoned/stray cat), {寝顔|ねがお} (sleeping face)
- **Standalone (11)**: メモ{用紙|ようし} (memo paper), {駐車|ちゅうしゃ}スペース (parking space), {似顔絵|にがおえ}{師|し} (portrait artist/caricaturist), {三角錐|さんかくすい} (triangular pyramid), ベアリング (mechanical bearing), {乳搾|ちちしぼ}り (milking), {麻雀|まーじゃん}{牌|ぱい} (mahjong tile), プリンアラモード (pudding à la mode), {南|みなみ}アジア (South Asia), アフリカ{大陸|たいりく} (African continent), {害獣|がいじゅう}{駆除|くじょ} (pest/vermin control)

§4 self-check: 1 applied (29333 gloss — opaque "pudding à la mode" clarified to descriptive form), 4 rejected (29329 `science` upheld — suggested "mathematics" not in taxonomy; 29333 ×3 translation — model wanted romaji "purin" in English, less clear). $0.0056.

### 2026-06-18 (Routine v2: new-entries — 12 New Entries, IDs 29312–29323)
Added 12 new entries: all 4 remaining priority seen-in-entry gaps plus 8 curated standalone words. The candidate pool outside the seen-in-entry set remains overwhelmingly corpus-harvest noise, so standalone picks were hand-selected for genuine dictionary-worthiness. Removed stale candidate ネジ (orthographic katakana variant of existing 00307_neji ねじ "screw"). Logged a [pattern] observation requesting curator restock of higher-quality candidates.

- **Seen-in-entry (4)**: {人災|じんさい} (man-made disaster; contrast 天災), {辞職願|じしょくねがい} (letter of resignation), {配属先|はいぞくさき} (place of assignment/posting), コロナ{禍|か} (the COVID-19 pandemic)
- **Standalone (8)**: {核|かく}ミサイル (nuclear missile), {距離計|きょりけい} (rangefinder), {昆虫類|こんちゅうるい} (insects/the insect class), {神在月|かみありづき} (tenth lunar month, Izumo name), {限界速度|げんかいそくど} (critical/limiting speed), {主要部|しゅようぶ} (main part), {重要語|じゅうようご} (key word/term), {厨房機器|ちゅうぼうきき} (commercial kitchen equipment)

§4 self-check: CLEAN — 0 issues across all 12 entries (independent accuracy review, $0.0052).

### 2026-06-17 (Routine v2: new-entries — 10 New Entries, IDs 29302–29311)
Added 10 new entries: all 5 priority seen-in-entry gaps plus 5 hand-picked common standalone words. The candidate pool remains overwhelmingly corpus-harvest noise (numerals/counters, transparent 〜化/〜性/〜器 compounds, proper nouns, typos), so standalone picks were curated for genuine learner-usefulness rather than padding to ~20; logged a [pattern] observation requesting curator restock/cleanup. Removed stale candidate 許しがたい (kana variant of existing 29288 許し難い). Added 人災 (じんさい) as a candidate from entry 29302's contrast note.

- **Seen-in-entry (5)**: {天災|てんさい} (natural disaster), {委任者|いにんしゃ} (mandator; legal), {問題外|もんだいがい} (out of the question), {掛|か}け{持|も}ち (juggling several jobs/roles; noun + suru), {一身上|いっしんじょう} (personal circumstances; esp. 〜の都合)
- **Standalone (5)**: {文法書|ぶんぽうしょ} (grammar book), スポンジケーキ (sponge cake), スケートリンク (skating rink), バイオマス (biomass), カードケース (card case)

§4 self-check: CLEAN — 0 issues across all 10 entries (independent accuracy review, $0.0043).

### 2026-06-16 (Routine v2: new-entries — 16 New Entries, IDs 29286–29301)
Added 16 new entries: all 11 priority seen-in-entry gaps plus 5 hand-picked standalone words. The oldest candidate band remains overwhelmingly corpus-harvest noise (transparent compounds, dubious coinages), so standalone picks were curated for genuine dictionary-worthiness rather than padding to 20.

- **Seen-in-entry (11)**: {水性|すいせい}{絵具|えのぐ} (water-based paint), {公金|こうきん} (public funds), {許|ゆる}し{難|がた}い (unforgivable; i-adj), {論外|ろんがい} (out of the question), {自然|しぜん}{災害|さいがい} (natural disaster), {大災害|だいさいがい} (catastrophe), やけ (reckless despair), モットー (motto), {不言実行|ふげんじっこう} (action before words), {言行一致|げんこういっち} (words matching deeds), {天地万物|てんちばんぶつ} (all of creation)
- **Academic/technical (5)**: {中国学|ちゅうごくがく} (Chinese studies), {整数論|せいすうろん} (number theory), {受任者|じゅにんしゃ} (mandatary; legal), {多色|たしょく}{刷|ず}り (multicolor printing), {給排水|きゅうはいすい} (water supply and drainage)

§4 self-check: 2 applied (29286 gloss — "watercolor-type"/"water-soluble" too specific for 水性絵具), 2 rejected (29288 formality `formal` upheld — ～難い literary register, consistent with sibling 信じ難い; 29291 `nature` in-list narrowness nit). $0.0069.

### 2026-06-15 (Routine v2: new-entries — 18 New Entries, IDs 29268–29285)
Added 18 new entries: all 3 seen-in-entry gaps plus 15 hand-picked standalone words. The oldest candidate band remains heavily corpus-harvest noise (numbers, transparent compounds, dubious coinages), so picks were curated for genuine dictionary-worthiness. Added 水性絵具 (water-based paint) as a candidate from entry 29284's notes.

- **Seen-in-entry (3)**: {張|は}り{上|あ}げる (to raise one's voice; ichidan), {金棒|かなぼう} (iron rod/club; the 鬼に金棒 idiom), {大海|たいかい} (the open sea)
- **Business/society (2)**: {多国籍企業|たこくせききぎょう} (multinational corporation), {受領者|じゅりょうしゃ} (recipient/payee)
- **Science/materials (3)**: {有機化合物|ゆうきかごうぶつ} (organic compound), {炭素鋼|たんそこう} (carbon steel), {雨量計|うりょうけい} (rain gauge)
- **Health/body (2)**: リンパ{腺|せん} (lymph node), {栄養補助食品|えいようほじょしょくひん} (dietary supplement)
- **Language/history (3)**: {形態素|けいたいそ} (morpheme), {農業革命|のうぎょうかくめい} (agricultural revolution), {直轄地|ちょっかつち} (directly controlled territory)
- **Other (5)**: {油|あぶら}かす (oil cake/fertilizer), {卓球台|たっきゅうだい} (table tennis table), {翻訳機|ほんやくき} (translation device), {油性絵具|ゆせいえのぐ} (oil paint), {壁材|かべざい} (wall material)

§4 self-check: 1 flagged, REJECTED (油かす 'nature' tag valid in-list fallback; suggested 'agriculture' not in taxonomy, 'food' wrong for primary fertilizer sense). $0.0078.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
