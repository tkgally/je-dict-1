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

### 2026-06-11 (Routine v2: new-entries — 20 New Entries + self-verification gate, IDs 29123–29142)
Added 20 new entries (IDs 29123–29142): all 8 "seen in entry" candidates plus 12 regular candidates.

- **Grammar suffix (1)**: 〜がち (tending to, prone to) — filling noentry link in 07441
- **Sports cluster (3)**: {喫|きっ}する (suffer defeat), スランプ (slump), {一勝|いっしょう} (one win), ビハインド (deficit) — from 06529 and 07006
- **Cultural objects (1)**: {草鞋|わらじ} (straw sandals) — from 06020
- **Commerce (1)**: {捨|す}て{値|ね} (throwaway price) — from 06020
- **Buddhist memorial (1)**: {三十三回忌|さんじゅうさんかいき} (33rd death anniversary service) — from 06018
- **Medical / health (3)**: {乳糖不耐症|にゅうとうふたいしょう} (lactose intolerance), {鼻汁|びじゅう} (nasal discharge), {体組成計|たいそせいけい} (body composition analyzer)
- **Abstract nouns (3)**: {優先度|ゆうせんど} (priority level), {確実性|かくじつせい} (certainty), {順応性|じゅんのうせい} (adaptability)
- **Cultural / social (4)**: {快気内祝|かいきうちいわ}い (get-well return gift), {自動二輪車|じどうにりんしゃ} (motorcycle formal term), パンティストッキング (pantyhose), {亭主元気|ていしゅげんき}で{留守|るす}がいい (proverb)
- **Multi-sense noun (1)**: {利|り} (profit; interest)
- **Expression (1)**: {活気|かっき}がない (lacking energy)

§4 self-check: **16 applied** (all semantic tag fixes — tags like `sports`, `culture`, `history`, `health`, `social` not in valid taxonomy; replaced with `leisure`, `clothing`, `body-internal`, `work`, `emotion`, etc.), **0 rejected**, **0 flagged**. New kanji 鞋 (02772_kai_kutsu_sandal). Conjugation tables added for 喫する (suru). 20 candidates removed.

### 2026-06-10 (Routine v2: new-entries — 20 New Entries + self-verification gate, IDs 29103–29122)
Added 20 new entries (IDs 29103–29122) drawn from all 13 "seen in entry" candidates and 7 regular candidates.

- **Mourning cluster (3)**: {喪|も}, {服|ふく}す, {忌明|きあ}け — filling noentry links in 06017 (四十九日)
- **Shrine/exam culture (3)**: {学業成就|がくぎょうじょうじゅ}, {合格祈願|ごうかくきがん}, {出雲大社|いずもたいしゃ}, {御影石|みかげいし}
- **Cultural (2)**: {紅白歌合戦|こうはくうたがっせん}, {各部署|かくぶしょ}
- **Verbs (2)**: {噛|か}み{殺|ころ}す (godan), {出|で}てくる (kuru)
- **Onomatopoeia (6)**: コケコッコー, カーカー, にんまり, どかどか, すかすか, バチバチ
- **General (4)**: {悪人|あくにん}, イルミネーション, レゴ, {御影石|みかげいし}

§4 self-check: 11 applied (semantic tags: `descriptive` for 6 onomatopoeia, `culture` for mourning cluster, `person`/`emotion` corrections), 6 bulk-rejected (model falsely claimed valid tags invalid). Conjugation tables added for 3 verbs. No new kanji.

### 2026-06-10 (Routine v2: new-entries — 20 New Entries + self-verification gate, IDs 29083–29102)
Added 20 new entries (IDs 29083–29102) drawn from "seen in entry" internal-completeness candidates — words referenced inside existing entries (IDs 05981–29082) but not yet defined.

- **Loanword nouns (3)**: シートベルト (seat belt), ホームシック (homesickness), ノーコメント (no comment)
- **Native nouns (7)**: {老齢|ろうれい} (old age), {倦怠期|けんたいき} (relationship rut), {鶯|うぐいす} (Japanese bush warbler), {史上初|しじょうはつ} (first in history), {延発|えんぱつ} (delayed departure), {摘出|てきしゅつ} (surgical removal, also suru), {潰瘍|かいよう} (ulcer)
- **Medical (4)**: {心音|しんおん} (heart sounds), {触診|しょくしん} (palpation, also suru), {胆汁|たんじゅう} (bile), {胆石|たんせき} (gallstone)
- **Onomatopoeia (6)**: ちゃぷちゃぷ (gentle splashing), ざぶん (single big splash), どすどす (heavy thumping footsteps), カクカク (jerky/choppy), チュンチュン (sparrow chirping), ホーホケキョ (bush warbler's call)

§4 self-verification: 19 model flags across 17 entries → **1 applied** (鶯 tags: `animals` → `animal-bird`), **18 rejected** (bulk-rejected: reviewer flagged schema-free semantic tags as invalid; all tags are legitimately used across the dictionary). Decisions logged to `reviews/decisions.jsonl`. New kanji 鶯 (02771_ou_uguisu_bush-warbler). Conjugation tables added for 摘出 and 触診 (suru).

_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
