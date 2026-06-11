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

### 2026-06-10 (Routine v2: new-entries — 20 New Entries + self-verification gate, IDs 29063–29082)
Added 20 new entries (IDs 29063–29082) drawn from "seen in entry" internal-completeness candidates — words referenced inside existing entries 05807–06662 but not yet defined. **First Routine run exercising the v2 §4 self-verification gate**: all 20 new entries were sent to an independent model (`review_accuracy.py`) before the single build.

- **Medical / anatomy (7)**: {聴診|ちょうしん} (auscultation, also suru), {頸動脈|けいどうみゃく} (carotid artery), {冠動脈|かんどうみゃく} (coronary artery), {膵臓癌|すいぞうがん} (pancreatic cancer), {胆嚢|たんのう} (gallbladder), {十二指腸|じゅうにしちょう} (duodenum), {飛沫|ひまつ} (droplets / spray)
- **Longevity milestones / omikuji fortunes (5)**: {古希|こき} (70th birthday), {喜寿|きじゅ} (77th birthday), {中吉|ちゅうきち} (middle blessing), {小吉|しょうきち} (small blessing), {末吉|すえきち} (future blessing) — cross-referenced to existing {大吉|だいきち} (19336) and おみくじ (05959)
- **Business / transport nouns (3)**: {監査役|かんさやく} (statutory auditor), {駐機場|ちゅうきじょう} (airport apron), {延着|えんちゃく} (delayed arrival, also suru)
- **Verbs (2)**: つぶる (godan, to close one's eyes), {言|い}い{張|は}る (godan, to insist)
- **Yojijukugo / onomatopoeia (3)**: {空前絶後|くうぜんぜつご} (unprecedented and unrepeatable), べらべら (chattering / fluent), どたどた (heavy clumsy footsteps)

§4 self-verification: 33 model flags across 17 entries adjudicated → **5 applied** (2 gloss age-sense additions for 古希/喜寿, 1 stubbornness nuance for 言い張る, 1 over-literal translation fix for 空前絶後, 1 tag fix), **28 rejected** (stylistic nits, model misreadings, house-style conflicts e.g. "blessing" matching existing 大吉), **0 flagged to curator**. Decisions logged to `reviews/decisions.jsonl`; metrics line appended to `pipeline/metrics-history.jsonl`. Also retagged the 4 anatomy entries to semantic `["body-internal"]` to match the dictionary's internal-organ convention (心臓/胃/腎臓). New kanji 頸 (02770_kei_kubi_neck). 8 words captured as candidates (心音, 触診, 胆汁, 胆石, 摘出, 潰瘍, 延発, どすどす). All 20 valid; conjugation tables added for 4 verbs/suru; 20 candidates removed.

### 2026-06-09 (Routine: new-entries — 20 New Entries, "Seen in Entry" Backlog, IDs 29043–29062)
Added 20 new entries (IDs 29043–29062) drawn from "seen in entry" internal-completeness candidates — words referenced inside existing entries 05794–05963 but not yet defined.

- **Loanword nouns (2)**: オリジナリティ (originality), プレゼンテーション (presentation)
- **I-adjective (1)**: {苛立|いらだ}たしい (irritating, frustrating)
- **Nouns (8)**: {妊活|にんかつ} (fertility efforts), {鉄拳|てっけん} (iron fist), {五円玉|ごえんだま} (5-yen coin), {産後|さんご} (postnatal period), {相談所|そうだんじょ} (consultation center), {悪事|あくじ} (wrongdoing), {街区|がいく} (city block), {防止法|ぼうしほう} (prevention law)
- **Na-adjective (1)**: {薄|うす}め (slightly thin/light)
- **Mimetics / onomatopoeia (4)**: すーすー (cool draft), ひやっと (sudden chill), ばくばく (large bites; heart pounding), がさごそ (rummaging)
- **Verbs (4)**: {倒|たお}れ{込|こ}む (godan), {丸|まる}まる (godan), {言|い}い{続|つづ}ける (ichidan), {入|はい}ってくる (kuru)

All 20 valid; conjugation tables added for 4 verbs + 1 i-adjective; 20 candidates removed.


_(Older change logs are in [PROJECT_STATUS-archive.md](PROJECT_STATUS-archive.md).)_
