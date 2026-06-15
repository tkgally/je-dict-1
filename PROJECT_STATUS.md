# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-06-10
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

### 2026-06-15 (Routine v2: new-entries — 18 New Entries, IDs 29268–29285)
Added 18 new entries: all 3 seen-in-entry gaps plus 15 hand-picked standalone words. The oldest candidate band remains heavily corpus-harvest noise (numbers, transparent compounds, dubious coinages), so picks were curated for genuine dictionary-worthiness. Added 水性絵具 (water-based paint) as a candidate from entry 29284's notes.

- **Seen-in-entry (3)**: {張|は}り{上|あ}げる (to raise one's voice; ichidan), {金棒|かなぼう} (iron rod/club; the 鬼に金棒 idiom), {大海|たいかい} (the open sea)
- **Business/society (2)**: {多国籍企業|たこくせききぎょう} (multinational corporation), {受領者|じゅりょうしゃ} (recipient/payee)
- **Science/materials (3)**: {有機化合物|ゆうきかごうぶつ} (organic compound), {炭素鋼|たんそこう} (carbon steel), {雨量計|うりょうけい} (rain gauge)
- **Health/body (2)**: リンパ{腺|せん} (lymph node), {栄養補助食品|えいようほじょしょくひん} (dietary supplement)
- **Language/history (3)**: {形態素|けいたいそ} (morpheme), {農業革命|のうぎょうかくめい} (agricultural revolution), {直轄地|ちょっかつち} (directly controlled territory)
- **Other (5)**: {油|あぶら}かす (oil cake/fertilizer), {卓球台|たっきゅうだい} (table tennis table), {翻訳機|ほんやくき} (translation device), {油性絵具|ゆせいえのぐ} (oil paint), {壁材|かべざい} (wall material)

§4 self-check: 1 flagged, REJECTED (油かす 'nature' tag valid in-list fallback; suggested 'agriculture' not in taxonomy, 'food' wrong for primary fertilizer sense). $0.0078.

### 2026-06-15 (Routine v2: new-entries — 10 New Entries, IDs 29258–29267)
Added 10 new entries, all from the priority "seen-in-entry" candidate band (internal-completeness gaps the dictionary already referenced). The remaining candidate pool was almost entirely corpus-harvest noise (compositional phrases, dubious or wrong glosses such as 怒燥/アンパッサン), so the run stayed focused on the 10 verified real words rather than padding to ~20. New kanji 弘 (コウ; broad) assigned ID 02774.

- **Noun (2)**: {水引|みずひき} (decorative paper gift cords), ビジネスモデル (business model)
- **Godan verbs (5)**: {痛|いた}がる (to show signs of pain), {踏|ふ}みとどまる (to stand one's ground; hold back — 2 senses), {殴|なぐ}り{飛|と}ばす (to punch and send flying), {滲|にじ}み{出|だ}す (to ooze out; show through — 2 senses), {噴|ふ}き{出|だ}す (to gush out; burst out laughing — 2 senses, cross-ref to 06342)
- **Particle (1)**: なあ (sentence-final emotion/emphasis)
- **Proverbs (2)**: {弘法|こうぼう}も{筆|ふで}の{誤|あやま}り and {河童|かっぱ}の{川流|かわなが}れ (both "even experts make mistakes"; cross-referenced to each other)

§4 self-check: clean — 0 issues across all 10 entries (independent accuracy review).

### 2026-06-14 (Routine v2: new-entries — 17 New Entries, IDs 29241–29257)
Added 17 new entries (IDs 29241–29257): all 6 seen-in-entry gaps plus 11 hand-picked standalone words. The candidate pool's oldest band is largely corpus-harvest noise (numbers, compositional phrases, dubious glosses), so picks were curated for genuine dictionary-worthiness. Added 水引 (decorative gift cords) as a candidate from entry 29243's example.

- **Seen-in-entry (6)**: {和柄|わがら} (traditional Japanese pattern), {配送料|はいそうりょう} (delivery fee), {不祝儀袋|ふしゅうぎぶくろ} (condolence-money envelope), フォーム (form/posture; web form — 2 senses), {解約金|かいやくきん} (cancellation fee), {自発|じはつ} (spontaneity)
- **Real estate/building (3)**: {鉄骨造|てっこつぞう} (steel-frame construction), {事務棟|じむとう} (office building/wing), {内装材|ないそうざい} (interior finishing material)
- **Daily life/objects (4)**: {現在時刻|げんざいじこく} (current time), パンティーストッキング (pantyhose), {印刷用紙|いんさつようし} (printer paper), {時限式|じげんしき} (time-delayed type)
- **Other (4)**: {工業革命|こうぎょうかくめい} (Industrial Revolution), {光学|こうがく}ディスク (optical disc), {右車線|みぎしゃせん} (right lane), {栄養教育|えいようきょういく} (nutrition education)

§4 self-check: 2 flagged, both REJECTED (フォーム 'technology' tag valid for web-form sense; 印刷用紙 'tool' tag consistent with ノート precedent). $0.0074.

### 2026-06-13 (Routine v2: new-entries — 20 New Entries, IDs 29221–29240)
Added 20 new entries (IDs 29221–29240): 2 seen-in-entry gaps plus 18 regular candidates. Removed 3 stale candidates (すぎる, ような, ノマドワーカー already in dictionary).

- **Seen-in-entry (2)**: {麸|ふすま} (wheat bran; new kanji 麸 assigned ID 02773), {航空法|こうくうほう} (Civil Aeronautics Act)
- **Food/culture (3)**: {蒲焼き|かばやき} (kabayaki grilled eel), たたき (tataki seared fish), {食文化|しょくぶんか} (food culture)
- **Food products (2)**: プロセスチーズ (processed cheese), バニラエッセンス (vanilla essence)
- **Daily life (3)**: ヘルスメーター (bathroom scale), スリープウェア (sleepwear), {脱毛剤|だつもうざい} (hair removal cream)
- **Building (1)**: {階建て|かいだて} (~-story building suffix)
- **Health (1)**: {授乳中|じゅにゅうちゅう} (while breastfeeding)
- **Traffic safety (2)**: {酒気帯び運転|しゅきおびうんてん} (DUI), {蛇行運転|だこううんてん} (reckless weaving driving)
- **Commerce (2)**: {無着色|むちゃくしょく} (no artificial coloring), {希望小売価格|きぼうこうりかかく} (MSRP)
- **Technology (1)**: {電気回路|でんきかいろ} (electric circuit)
- **Travel/history (1)**: {遺跡群|いせきぐん} (ruins complex)
- **Language (1)**: ポルトガル{語|ご} (Portuguese)
- **Transportation (1)**: {最高速|さいこうそく} (top speed)

§4 self-check: CLEAN (0 issues across 20 entries, $0.0088).

### 2026-06-13 (Routine v2: new-entries — 20 New Entries, IDs 29201–29220)
Added 20 new entries (IDs 29201–29220): 2 seen-in-entry gaps plus 18 regular candidates.

- **Seen-in-entry (2)**: {空撮|くうさつ} (aerial photography/drone shot), {糠|ぬか} (rice bran)
- **Everyday objects (1)**: たわし (scrubbing brush; scouring pad)
- **Education/person (1)**: {初級者|しょきゅうしゃ} (beginner; novice)
- **Person (1)**: {愛好者|あいこうしゃ} (enthusiast; aficionado)
- **Culture/leisure (1)**: {祝祭|しゅくさい} (celebration; festivity)
- **Media (2)**: {映像化|えいぞうか} (film/visual adaptation), {速報性|そくほうせい} (timeliness; breaking news quality)
- **Work/business (2)**: {新卒採用|しんそつさいよう} (new graduate hiring), ファシリテーション (facilitation)
- **Language (1)**: {異体字|いたいじ} (variant kanji form)
- **Health/law (1)**: {障害者手帳|しょうがいしゃてちょう} (disability certificate)
- **Abstract (3)**: {落ち込み|おちこみ} (depression; slump), {駆動力|くどうりょく} (driving force), {停滞感|ていたいかん} (sense of stagnation)
- **Society (1)**: {競争社会|きょうそうしゃかい} (competitive society)
- **Shopping (1)**: {高級店|こうきゅうてん} (high-class shop; upscale establishment)
- **Weather (1)**: {雷光|らいこう} (lightning flash)
- **Adverbs (2)**: {急激|きゅうげき}に (rapidly; sharply), {猛烈|もうれつ}に (fiercely; intensely)

§4 self-check: 3 applied (29208/29210 formality formal→neutral; 29216 removed food semantic tag), 0 rejected, 0 flagged.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
