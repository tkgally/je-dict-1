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

### 2026-06-12 (Routine v2: new-entries — 20 New Entries, IDs 29181–29200)
Added 20 new entries (IDs 29181–29200) from candidates, processing all 4 seen-in-entry gaps.

- **Seen-in-entry (4)**: {一級建築士|いっきゅうけんちくし} (first-class architect), {二級建築士|にきゅうけんちくし} (second-class architect), {脱サラ|だつさら} (leaving salaried employment to go independent), {演奏家|えんそうか} (professional musician)
- **Social/political (3)**: {社会運動|しゃかいうんどう} (social movement), {平和運動|へいわうんどう} (peace movement), {人権活動|じんけんかつどう} (human rights activities)
- **Abstract/society (2)**: {自我意識|じがいしき} (self-awareness), {知識階級|ちしきかいきゅう} (intelligentsia)
- **Culture/daily life (5)**: {絹織物|きぬおりもの} (silk fabric), {飯炊き|めしだき} (cooking rice; historical cook), {日|ひ}めくりカレンダー (tear-off calendar), UFOキャッチャー (claw machine), ファッションデザイナー (fashion designer)
- **Education/work (1)**: {職業訓練校|しょくぎょうくんれんこう} (vocational training school)
- **Sports/health (4)**: {体幹|たいかん}トレーニング (core training), {水泳帽|すいえいぼう} (swimming cap), {水泳選手|すいえいせんしゅ} (competitive swimmer), {抗ウイルス薬|こうういるすやく} (antiviral drug)
- **Facility (1)**: {入館者|にゅうかんしゃ} (visitor to a facility)

§4 self-check: 1 applied (29193 gloss clarified historical usage of cook meaning), 0 rejected, 0 flagged.

### 2026-06-12 (Routine v2: new-entries — 18 New Entries, IDs 29163–29180)
Added 18 new entries (IDs 29163–29180) from candidates, prioritizing 2 seen-in-entry gaps.

- **Seen-in-entry (2)**: {殊更|ことさら} (deliberately; particularly), {返|かえ}る (to be returned; revert)
- **Grammar expressions (6)**: べく (in order to — formal), べし (should — archaic), 〜ねばならない (must — literary), 〜なきゃならない (must — colloquial), 〜ように言う (to tell someone to), はい、どうぞ (here you are; please go ahead)
- **Pronouns/interjections (5)**: どこどこ (such-and-such a place), どなた様 (who — very polite), なんだよ (what the heck), {何|なん}だって (what?! really?!), いいやん (it's fine — Kansai)
- **Adverbs (1)**: すでにして (already; even at this stage — formal)
- **Expressions (2)**: {功|こう}{成|な}り{名|な}{遂|と}げる (to achieve fame and success), {該当|がいとう}する (to apply; be applicable)
- **Nouns (2)**: {学究|がっきゅう}{肌|はだ} (scholarly temperament), {中産|ちゅうさん}{階級|かいきゅう} (middle class)

§4 self-check: 2 applied (29165 formality formal→neutral, semantic greeting→expression; 29172 semantic greeting→person, politeness humble→honorific), 0 rejected, 0 flagged.

### 2026-06-11 (Routine v2: new-entries — 20 New Entries + self-verification gate, IDs 29143–29162)
Added 20 new entries (IDs 29143–29162) from candidates.

- **Grammar particle (1)**: って (casual quotation/hearsay/topic, 3 senses)
- **Grammar expressions (2)**: みたいだ (seems like; comparison), につきまして (formal "regarding")
- **Kansai dialect (3)**: そうや (that's right), そやね (yeah right), ええなあ (nice/lucky you)
- **Cultural / literary (2)**: 七五調 (7-5 syllabic meter), 六曜 (six-day calendar cycle)
- **Everyday objects (3)**: 生理用ナプキン (sanitary napkin), 除毛クリーム (hair removal cream), ミシン目 (perforation)
- **Social / legal (2)**: 風俗店 (adult entertainment establishment), 有期懲役 (fixed-term imprisonment)
- **Misc nouns / expressions (5)**: 力ずく (brute force), 砂ぼこり (swirling dust), 利用規約 (terms of service), 湯炊き (boil-and-drain cooking), 口先三寸 (smooth talk), 読み済み (already read), すっとんと (with a thud)

§4 self-check: 2 applied (29149 `grammatical`→`communication` tag; 29154 "clink"→"thud" translation), 1 rejected (29159 communication tag adequate). Post-creation fixes: 5 entries had invalid "colloquial" formality tag → changed to "informal"; 1 entry had invalid underscore in romaji ID → renamed; 9 entries had missing furigana → fixed.

### 2026-06-11 (Curator session: Routine v2 assessment, semantic-tag policy decision, routine.md removed)
Reviewed the first 17 Routine v2 runs (all PRs merged cleanly; §4 self-verification catching real errors at ~$0.01/run) and resolved the semantic-tag source-of-truth contradiction that had runs adjudicating identical "invalid tag" flags in opposite directions.

- **Tag policy (curator decision)**: expand-then-enforce. `VALID_SEMANTIC` in `build/validate_tags.py` expanded with 30 established-by-usage tags (`business`, `culture`, `nature`, `health`, …); near-duplicates get a 1:1 migration map (`time`→`time-general`, `people`→`person`, …) in `build/check_tag_drift.py`; the remaining 9,036 out-of-taxonomy instances (7,292 entries) are tracked by the new `check_tag_drift.py --check unknown-semantic` detector and Cleanup Backlog P20 / `unknown-semantic-tags` queue item.
- **Reviewer prompt v3** (`build/review_accuracy.py`): out-of-list tags flagged as migration candidates; no "too narrow/broad" substitutions between in-list tags; formality flags only on unambiguous register contradictions.
- **Tag guidance at creation time**: semantic-tag closed list added to `prompts/newentries.md` (mirroring the POS table) and refreshed in the `entry-guidelines` skill — ends the create-then-§4-patch loop seen in every new-entries run.
- **routine2.md tweaks**: standing tag-adjudication rule (§A); furigana-screening known-noise shortcut (bulk-reject documented false-positive families, skip the deep pass); stale-priority-lane regeneration rule; §C exact-lowercase ledger values.
- **routine.md deleted** — routine2.md is the only Routine prompt; references updated in CLAUDE.md, metaprompt_list.md, routine_next.py, routine-config.json, and the wiki. Corrected the wrong adjudication heuristic in `planning/wiki/topics/schema-tag-reliability.md`; Tooling Backlog item 14 resolved.

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
