# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-09-21
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
| Total entries | ~30,764 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,981 (open) |
| Candidate words | ~188 (all vetted; queue cleaned 2026-08-11) |
| Cross-references | ~19,000 |
| Example sentences | ~119,000 |

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

### 2026-09-26 (Routine v3: new-entries — 3 New Entries, IDs 31074–31076)

A short end-of-run cycle. 柴刈り (gathering brushwood, the Momotarō しばかり), the one internal-closure
candidate, added after the 芝刈り polish; 無印良品 and 朝日新聞 from the curated proper-noun queue. Two old
`noentry` markers (01639 新聞社, 03990 無地) now link to them. Self-check clean. Candidate queue stands at 113.

### 2026-09-26 (Routine v3: new-entries — 20 New Entries, IDs 31054–31073)

Five internal-closure words that earlier entries mentioned without defining: 立ち飲み, 既成,
滑り込み, 申し送る, 濡れ衣. Fifteen proper nouns and cultural terms from the curated queue:
the classics 竹取物語, 平家物語, 徒然草, 方丈記, 奥の細道, 忠臣蔵; the historical figures 源頼朝,
武田信玄, 上杉謙信, 千利休, 世阿弥, 渋沢栄一; 道頓堀, 祇園祭, and 大河ドラマ. Five old `noentry`
markers in four entries (03735 祭り, 04314 随筆, 04455, 04768) now link to the new entries.
Self-check: 3 flags, 1 applied, 2 rejected. Candidate queue stands at 115.

### 2026-09-25 (Interactive: recorded audio for example sentences)

Example sentences can now carry recorded readings. Each MP3 is made by Gemini TTS and is
accepted only when four AI checkers from three companies agree it follows the furigana; a failed
take is regenerated up to five times. The recordings live in a separate repository,
`tkgally/je-dict-audio-1`, served by GitHub Pages, so no audio enters this repository. On
an entry page, an example with a valid recording gets a play button for the MP3. The recording
counts as valid while the example's text and furigana are unchanged; every other example keeps
the browser-speech button.

**First recordings: 308 examples from the first 33 basic-tier entries** (00006 ある to 00422 を),
voices Kore and Charon, $0.76. 292 passed on the first take. The batch also found a furigana
error, 00111 本 {少|すこ}なくとも → すく, which is now fixed.

**Then 800 more** (00426 読む to 00560 口), after Tom chose four voices (Kore, Charon, Erinome,
Iapetus), 32 kbps, and a budget of $4.80 per audio run within a $7.50 daily cap: all 800
accepted, 761 on the first take, $1.94. 1,108 examples now have recordings.

**The Routine has a new `audio` mode (a quarter of runs, $4.80 each).** It works through
stale recordings first, then the basic, core and general tiers. It runs maintenance checks
before recording: a regression suite of 163 clips with known answers, voice pilots, model
checks, and monthly spot-check pages for Tom. Examples with digits, Latin letters or symbols
(about 2,500), or with kanji lacking furigana (90), are skipped for now. Workflow, evidence and
changelog: `AUDIO_WORKFLOW.md`.

### 2026-09-24 (Routine v3: new-entries — 20 New Entries, IDs 31034–31053)

Created 20 general-tier entries: all 7 internal-closure candidates (ラジオ{体操|たいそう} from 01541,
{人|ひと}となり from 08163, むしる from 08195, {添|そ}え{物|もの}, {燻|いぶ}し{銀|ぎん}, {衣紋掛|えもんか}け,
{移植|いしょく}ごて) plus 13 from the queue: four eras ({平安時代|へいあんじだい}, {鎌倉時代|かまくらじだい},
{室町時代|むろまちじだい}, {大正時代|たいしょうじだい}), six places ({原宿|はらじゅく}, {祇園|ぎおん},
{東海道|とうかいどう}, {伊勢神宮|いせじんぐう}, {東大寺|とうだいじ}, {桜島|さくらじま}), two events
({箱根駅伝|はこねえきでん}, {阿波踊|あわおど}り) and {源義経|みなもとのよしつね}. New kanji 祇 added to the index.

**Four stale `noentry` markers resolved** (class A1) in 01676, 03757, 04020, 05638.

**§4 self-check on 36 entries: 1 applied, 2 rejected.** Applied: `clothing` tag on 31045 {原宿|はらじゅく}
replaced with `culture`. Kana-link check: 29 links, 0 flagged. Cost $0.019.

### 2026-09-23 (Routine v3: new-entries — 20 New Entries, IDs 31014–31033)

Created 20 general-tier entries: all 5 internal-closure candidates ({台木|だいぎ} and {穂木|ほぎ} from
08106 {接|つ}ぎ{木|き}, {百万長者|ひゃくまんちょうじゃ}, {口車|くちぐるま} from 08111 {舌先|したさき},
{卵|たまご}とじ) plus 15 from the queue: the proverb {餅|もち}は{餅屋|もちや}, {自転車操業|じてんしゃそうぎょう},
{玉石混交|ぎょくせきこんこう}, three people ({宮沢賢治|みやざわけんじ}, {手塚治虫|てづかおさむ},
{葛飾北斎|かつしかほくさい}), three classics ({源氏物語|げんじものがたり}, {枕草子|まくらのそうし},
{古事記|こじき}), five places ({清水寺|きよみずでら}, {金閣寺|きんかくじ}, {永田町|ながたちょう},
{霞|かすみ}が{関|せき}, {築地|つきじ}) and {任天堂|にんてんどう}. Candidate C23001 棚からぼたもち was dropped
as a kana duplicate of 06196 {棚|たな}から{牡丹餅|ぼたもち}.

**Seven stale `noentry` markers resolved** (class A1) in 00242, 01676, 04314, 05051, 07059. Five
wrong partial-word links placed by the linker were removed by rewording (霞 inside 霞ヶ関, 建て
inside 建て直す, 続け inside 描き続け, 子 inside 子ども, 売り inside 売り上げ).

**§4 self-check on 25 entries: 1 applied, 1 rejected.** Applied: 31024 {葛飾北斎|かつしかほくさい}
now says the Great Wave is on the *new* 1,000-yen note issued in 2024. Rejected: removing `food`
from 31032 {築地|つきじ}. Kana-link check: 17 links, 0 flagged. Cost $0.013.

