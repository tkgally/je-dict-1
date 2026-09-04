# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-09-03
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
| Total entries | ~30,604 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,821 (open) |
| Candidate words | ~176 (all vetted; queue cleaned 2026-08-11) |
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

### 2026-09-03 (Routine v3: new-entries — 20 New Entries, IDs 30794–30813)

Created 20 general-tier entries under the v3 internal-closure policy. **Nine came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined, which empties that lane completely: {色物|いろもの} (two senses — colored laundry, contrasted with 30774 {白物|しろもの}, and the vaudeville-program variety act, unrelated in modern usage but sharing the same "colored thing" root), {挙式|きょしき} (the ceremony itself, distinct from the {披露宴|ひろうえん} reception that follows it), {間|ま} (the felt pause or timing in speech and performance, cross-referenced against the unrelated reading {間|あいだ}), {観覧料|かんらんりょう} and {拝観|はいかん} (both harvested from 07059's "RELATED FEE TYPES" note — the fee word Japanese picks by kind of place, and the reverent {拝|はい} that keeps {拝観|はいかん} confined to temples and shrines), バーテンダー, {竹細工|たけざいく} (the {木彫|きぼ}り-pattern craft compound), 〜{師|し} (the practitioner suffix, contrasted with 〜{士|し}'s licensing sense and 〜{家|か}/〜{者|しゃ}), and {主夫|しゅふ} (the coined gender-neutral counterpart of {主婦|しゅふ}).

**The other eleven are place names** from the vetted proper-noun queue, written so the explanation carries the connotations rather than the coordinates: {隅田川|すみだがわ} (the fireworks festival and Edo-period culture), {北陸|ほくりく} and {東海|とうかい} (Japan's own regions, named for their prefectures and historic routes), and eight foreign destinations — ハワイ, ニューヨーク, ロンドン, {北京|ぺきん}, ソウル, {台湾|たいわん}, {香港|ほんこん}, and ドイツ — each carrying the association a Japanese speaker reaches for (ハワイ's honeymoon status, {台湾|たいわん}'s reputation for friendliness toward Japanese visitors, {香港|ほんこん}'s dim sum and action-cinema legacy). Two conjugation tables added (both suru: {挙式|きょしき}, {拝観|はいかん}). No new kanji.

**Eleven stale inline links repaired.** Creating an entry from a "seen in entry" candidate immediately orphans the `⟦…：noentry⟧` marker in whichever entry referred to it. Nine files were pointed at the new IDs: 02186 {川|かわ} (×2, {隅田川|すみだがわ}), 02791 {経由|けいゆ} (×2, {香港|ほんこん}), 03115 {大都会|だいとかい} (ニューヨーク, ロンドン), 03225 {主婦|しゅふ} (×2, {主夫|しゅふ}), 04456 {狂言|きょうげん} (〜{師|し}), 04551 {統一|とういつ} (ドイツ), 07059 {拝観料|はいかんりょう} (×2, {拝観|はいかん}; ×1, {観覧料|かんらんりょう}), 07060 バー (バーテンダー), 07063 {木彫|きぼ}り (〜{師|し}).

**§4 cross-model self-check on all 33 changed entries (20 new plus 13 neighbors touched by the stale-link and cross-reference-harvest passes): 0 flags.** Every entry came back clean. Cost $0.016.

**Queue note**: the 〜{師|し} candidate did not auto-clear from `candidate_words.json` (the entry's headword carries a leading tilde marker that the sync script's exact-match check doesn't see); removed by hand. Candidate queue stands at 176.

### 2026-09-02 (Process overhaul: Routine v3, mechanical sweeps, site rebuilt — see enhancement/assessment-2026-09-02.md)

An interactive session (Claude, the curator's assessment request) rebuilt the maintenance process
around one principle: scripts do the mechanical work, the Routine does judgment.

**Dictionary-wide mechanical sweeps, all validated (30,584/30,584):** every entry now carries
inline word links placed by the new deterministic linker (`build/auto_link.py`: 1,007,002 links, up
from 278,772; only tokens that resolve to exactly one entry, 60/60 correct in the sampled check);
58,103 cross-references harvested from SIMILAR/RELATED/KEIGO bullets in the notes
(`build/harvest_crossrefs.py`; 87 percent of entries now have cross-references, up from 38); 17,400
legacy notes headers renamed to the canonical vocabulary in `build/data/note_headers.json` and
17,571 nakaguro bullets converted; 6,267 part-of-speech display strings canonicalized; politeness
set on 5,952 entries and formality on 1,059 where the notes gave no reason to hold out; 1,077
entries with malformed furigana wrappers repaired; transitivity tagged on 1,683 verbs where two
external models agreed and the entry's own examples show the valency (2,369 more wait in
`reviews/transitivity/disagreements.jsonl`); 147 stale `noentry` markers resolved.

**Routine v3** (`prompts/routine2.md`): polish mode does judgment only (25–40 entries), the
external reviewer now checks the notes field and filters its own noise (prompt version 4), the
furigana screener is retired, weights are polish 0.30 / accuracy 0.30 / systemic-fix 0.25 /
new-entries 0.10 / candidates 0.05, the wiki runs only when observations pile up, new entries come
only from words the dictionary already uses, and runs no longer commit `docs/`.

**Site** rebuilt by GitHub Actions on merge (`.github/workflows/pages.yml`): English and
conjugated-form search, index split (entry pages no longer download 18.7 MB), word links visible by
default, notes headings, tag badges and tag pages, kanji readings, study lists, curator tools
unlinked. **Note for the curator:** Settings → Pages → Source must be "GitHub Actions" (the
workflow tries to switch it automatically).

**Curator items** (`reviews/needs_curator.txt`): five duplicate entry pairs in the closed tiers.

### 2026-09-02 (Routine v2: candidates — 55 Vetted Words Added, Queue 140 → 195)

Restocked the candidate queue, which had fallen to 140 words (the selector schedules this mode
below 150). No entries were created or changed; the candidate list is the material the
`new-entries` mode draws on, and every word on it is meant to be ready to write up without further
screening.

**The run probed before it proposed.** Rather than writing glosses first and discovering later that
the word already had an entry, it ran 163 words through the duplicate checker in bulk and only then
vetted the survivors. That measured how much room is left in each source of new words at 30,584
entries: the health-and-medical sweep returned **nothing usable** (0 of 28); four-character idioms
returned 17%; a modern institutions/landmarks slice of proper nouns returned 12%; but **body-part
and other idioms (47%), proverbs (48%), and a fresh slice of proper nouns covering cultural sites
and canonical historical figures (47%)** are still productive. This revises the 2026-08-11 finding
that proper nouns are uniformly fertile — the easy slices are worked out, and yield now depends
entirely on which slice is probed.

**55 words added** (C23288–C23342), all passing the individual reality/lemma/reading/gloss gates:
26 idioms ({気|き}が{置|お}けない, {白羽|しらは}の{矢|や}が{立|た}つ, {拍車|はくしゃ}をかける,
{棚|たな}に{上|あ}げる …), 10 proverbs ({覆水盆|ふくすいぼん}に{返|かえ}らず,
{案|あん}ずるより{産|う}むが{易|やす}し, {住|す}めば{都|みやこ} …), 4 four-character idioms
({温故知新|おんこちしん}, {千載一遇|せんざいいちぐう} …), and **15 proper nouns** (27% of the
batch, within the 20–40% target): {厳島神社|いつくしまじんじゃ}, {天橋立|あまのはしだて},
{松島|まつしま}, {兼六園|けんろくえん}, {銀閣寺|ぎんかくじ}, {阿蘇山|あそさん},
{清少納言|せいしょうなごん}, {歌川広重|うたがわひろしげ}, {津田梅子|つだうめこ},
{信州|しんしゅう}, {阪神|はんしん}, {山陰|さんいん}, {厚生労働省|こうせいろうどうしょう},
{三越|みつこし}, セブンイレブン. Words that survived the duplicate check but were merely
referential — an ordinary landmark with no cultural weight — were dropped under the richness gate
rather than added.

**One existing-entry problem found and logged**: a duplicate probe surfaced 19274 `板に着く`, which
writes the theatrical idiom いたにつく with the wrong kanji (standard is {板|いた}に{付|つ}く or
kana). Recorded as an `[entry]` observation for a polish pass over the 19000 block; not fixed here,
since this mode does not change entries.

**Lenses for next time**: idioms and proverbs still have depth; the proper-noun lens should keep
rotating to unworked slices. Common-vocabulary thematic sweeps (health, office, administrative)
are exhausted and should be skipped unless probed first.


### 2026-08-31 (Routine v2: new-entries — 20 New Entries, IDs 30774–30793)

Created 20 general-tier entries. **Eighteen came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined — which empties that lane completely. A block of them closes out the lodging vocabulary the 07043–07050 entries lean on: {一泊二食付|いっぱくにしょくつ}き and {夕食付|ゆうしょくつ}き (the 〜{付|つ}き booking-plan suffix, read つき not ふき), {二泊|にはく} (with the {泊|はく} counter's sound changes and the nights-first {二泊三日|にはくみっか} ordering that reverses the English), {延泊|えんぱく} (extending a stay, separated from {連泊|れんぱく}, which is booked that way from the start), {喫煙室|きつえんしつ}, {結婚式場|けっこんしきじょう}, and {送迎|そうげい}バス (the free courtesy bus, distinguished from a paid {路線|ろせん}バス). The rest: {白物|しろもの} (two senses — laundry whites, and the {白物家電|しろものかでん} white goods of business reporting), {向|む}こう{気|き} (which barely occurs outside {向|む}こう{気|き}が{強|つよ}い), {天下分|てんかわ}け{目|め} (with Sekigahara as the reference point behind the modern figurative use), {耳|みみ}が{遠|とお}い (the 〜が{遠|とお}い body-part idiom), {変更|へんこう}する (contrasted with everyday {変|か}える), {早|はや}い{者勝|ものが}ち, {甘|あま}ったるい (both senses negative — you would never praise a dessert with it), {意味不明|いみふめい} (the neutral written sense split from the casual dismissive one), {清廉潔白|せいれんけっぱく} (noting it usually appears in contexts of doubt), and the two suffixes 〜{剤|ざい} and 〜{制|せい} — the latter written around the 〜{製|せい} homophone trap, where the kanji is the only clue in speech.

**The other two are proper nouns** from the vetted queue: {出雲|いずも} (written around the {縁結|えんむす}び association and the {神在月|かみありづき} inversion of {神無月|かんなづき}) and {瀬戸内海|せとないかい} (the calm-water and island-art connotations rather than the geography). Three conjugation tables added (2 suru, 1 i-adjective). No new kanji.

**Eight stranded inline links repaired.** Creating an entry from a "seen in entry" candidate immediately orphans the `⟦…：noentry⟧` marker in whichever entry referred to it. Six files were pointed at the new IDs: 03641, 05493, 07043, 07048 (two markers), 07049 (two markers), 07050.

**§4 cross-model self-check on all 20 new entries: 3 flags, 2 applied, 1 rejected, 0 sent to the curator.** Seventeen entries came back clean. The applied flags were on {天下分|てんかわ}け{目|め}, whose top-level gloss read "decisive; make-or-break" — an adjectival phrasing for a noun headword, carried over verbatim from the candidate row — and on {延泊|えんぱく}, which was missing the `action` semantic tag the project requires on suru-verbs. The rejection objected that `abstract` is wrong for a suffix naming concrete substances (〜{剤|ざい}); that is an in-list narrowness substitution, which policy declines, and the parallel suffix entry 28347 〜{材|ざい} is tagged the same way. Cost $0.009.

**Two entries failed validation on first pass** with `formality: "casual"`, which is not in the schema's enum (`formal`/`neutral`/`informal`/`vulgar`/`null`); corrected to `informal` and logged as a `[tooling]` observation, since `newentries.md` documents the POS and semantic-tag vocabularies but not this one.

**Queue note**: 2 candidates captured from words the new entries reference but do not define — {色物|いろもの} and {挙式|きょしき}. Fifteen further words checked were already covered. The candidate queue stands at 134.


### 2026-08-28 (Routine v2: new-entries — 20 New Entries, IDs 30754–30773)

Created 20 general-tier entries. **Sixteen came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined, which empties that lane: {防弾|ぼうだん} (written so the learner sees it only ever heads a compound), たこ{足|あし}{配線|はいせん} (the overloaded outlet, which Japanese speakers meet as a fire-safety warning), {味|あじ}の{素|もと} (the brand, with the point that older speakers use the name for MSG generally), {時雨|しぐれ}{煮|に}, {相棒|あいぼう} (the palanquin-pole origin, and how it differs from {仲間|なかま} and {同僚|どうりょう}), {箸|はし}{立|た}て (separated from {箸|はし}{置|お}き and {箸|はし}{箱|ばこ}, which learners conflate), {甥|おい}っ{子|こ} and {姪|めい}っ{子|こ} (the affectionate 〜っ{子|こ} forms, noting Japanese has no single word for "nieces and nephews"), {好|す}く (with the warning that the plain affirmative sounds archaic and learners want {好|す}き), {負|ま}けん{気|き}, {動|どう}じる (met almost only as {動|どう}じない), {教諭|きょうゆ} and {獣医師|じゅういし} (the official job titles, each set against the word people actually say — {先生|せんせい} and {獣医|じゅうい}), {色柄物|いろがらもの} (the laundry term off detergent bottles), ラベンダー (with the Furano association), and セラミック (the engineered material, explicitly not {陶器|とうき}).

**The other four are proper nouns** from the vetted queue, written so the explanation carries the connotations: {関|せき}ヶ{原|はら} (given two senses — the 1600 battle, and the everyday figurative "decisive showdown" behind {天下|てんか}{分|わ}け{目|め}の{関|せき}ヶ{原|はら}), {紫式部|むらさきしきぶ} (noting that neither half of the name is a real personal name), {松尾芭蕉|まつおばしょう}, and {日本海|にほんかい} (written around the {日本海|にほんかい}{側|がわ}/{太平洋|たいへいよう}{側|がわ} weather split rather than the geography). Two conjugation tables added (1 godan, 1 ichidan). Two new kanji given index IDs: 芭 (02799) and 蕉 (02800).

**Three stale candidates removed before writing.** The suffix candidates 系, 用, and 製 already have entries written with a leading tilde (28466 〜系, 09842 〜用, 02001 〜製), which the duplicate check does not match — logged as a `[pattern]` observation.

**§4 cross-model self-check on all 20 new entries: 3 flags, 1 applied as 2 edits, 1 rejected, 0 sent to the curator.** Eighteen entries came back clean. The applied flag was on {色柄物|いろがらもの}, whose gloss said "clothing" when the word covers towels and linens too in laundry instructions — broadened. The rejected flag objected to the register note in the gloss "veterinarian (formal term)"; 216 existing entries use that pattern, so it is house practice, not an error. Cost $0.009.

**Queue note**: 3 candidates captured from words these entries reference but do not define — {白物|しろもの}, {向|む}こう{気|き}, and {天下|てんか}{分|わ}け{目|め}. Thirteen further proposals were rejected by the duplicate gate as words that already have entries. The candidate queue stands at 140.

