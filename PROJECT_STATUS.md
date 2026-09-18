# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-09-18
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

### 2026-09-18 (Routine v3: new-entries — 21 New Entries, IDs 30953–30973)

Created 21 general-tier entries, all from the "seen in entry" internal-closure lane (34 available,
21 taken). A place name tied to wolf worship: {三峯|みつみね} (Mitsumine Shrine, Saitama; from
04334 {狼|おおかみ}). A cardigan-cut trio from 04520 カーディガン: ロングカーディガン,
ショートカーディガン, ボタンレスカーディガン. A scanner-type trio from 05248 スキャナー:
フラットベッドスキャナー, ハンディスキャナー, ドキュメントスキャナー. The steak-doneness scale
from 01369 ステーキ: ミディアムレア, ミディアム, ウェルダン, plus two cuts, サーロインステーキ
and フィレステーキ. {能楽堂|のうがくどう} (Noh theater building, from 01927 {能|のう}). A
screen/display cluster from 01368 スクリーン: プロジェクター, スクリーンセーバー,
ワイドスクリーン, マルチスクリーン. {噛|か}み{傷|きず} (bite wound, contrasted with 07340
{切|き}り{傷|きず}). {五位鷺|ごいさぎ} (night heron, from 04939 {鷺|さぎ}). A fabric/trim pair
from 04517 ブラウス: シフォン and フリル. One new kanji indexed: {峯|みね} (peak), added as
02804_hou_mine_peak.

**One candidate dropped before writing.** {蝦蟇|がま} (toad, C23481) turned out to be the same
word as the existing entry 28705 ガマ, which already documents {蝦蟇|がま} as its kanji spelling
in its own notes — removed from the queue rather than duplicated. Four other internal-closure
candidates were set aside for editorial reasons rather than written up this run: {大口真神|おおくちのまかみ}
(a deity name with no clean semantic-tag category), {師|し} and {両生|りょうせい} (bound morphemes
too thin to support a standalone entry with natural example sentences), and 藤田/藤井 (generic
surnames with no specific cultural referent, unlike the dictionary's existing person-name entries).
All four remain in the queue for a future session to reconsider.

**One stale `noentry` marker resolved**: 03853 セット (プロジェクター, in an example sentence about
setting up equipment for a meeting).

**§4 self-check on all 22 changed entries (21 new plus 03853, the noentry neighbor): 5 flags, 1
applied, 4 rejected.** Applied: 03853 セット's semantic tags carried leftover `geography` and
`leisure`, unrelated to any of its three senses (a set of items, a sports set, the act of setting
up) — replaced with `general` and `sports`. Rejected as reviewer noise: three flags claiming the
DONENESS SCALE lines in 30960/30961/30962's notes were missing steps — the model misread the
inline-link arrows (⟦…→…⟧) around ミディアムレア/ミディアム/ウェルダン as if the scale itself were
truncated; all four levels are present in each entry. One flag on 30972 シフォン's `clothing`
semantic tag for a fabric name was rejected as consistent with the dictionary's own convention
(cf. existing entry ウール, also a fabric, also tagged `clothing`). In-context kana-link check: 0
flags. Cost: $0.0104 self-check, $1.032 spent today against the $5.00 daily cap.

**Queue**: 21 candidates auto-cleared on `update_indexes.py`, one removed by hand as a duplicate.
Candidate queue stands at 188.

### 2026-09-17 (Routine v3: new-entries — 20 New Entries, IDs 30933–30952)

Created 20 general-tier entries, all from the "seen in entry" internal-closure lane. Buddhist
memorial-day sequence: {四七日|よなのか}, {五七日|いつなのか}, {六七日|むなのか} (28th, 35th, 42nd
day, rounding out the series alongside the existing {初七日|しょなのか} and {四十九日|しじゅうくにち}).
Clear-soup terminology from 04990 {吸|す}い{物|もの}: {椀種|わんだね}, {吸|す}い{口|くち},
{木|き}の{芽|め}. Regional food: {笹|ささ}かまぼこ, {笹寿司|ささずし}, みたらし. Spices from
04943 {香辛料|こうしんりょう}: クミン, ターメリック. Proper nouns: {桃太郎|ももたろう}, 法隆寺
(from the Masaoka Shiki haiku quoted in 04384 {柿|かき}), {土佐犬|とさいぬ}. Everyday items:
スポーツサンダル, カニ (katakana spelling of {蟹|かに}), OCR, {一千万|いっせんまん},
{消|け}し{忘|わす}れる, {打撲傷|だぼくしょう}.

**One candidate dropped as a spelling-variant duplicate.** {売|う}り{上|あ}げ (sales) turned out to
be the same word as the existing entry 04102 {売上|うりあげ}, whose own notes already say "can also
be written as {売り上|うりあ}げ" — removed from the queue rather than written up.

**Three stale `noentry` markers resolved**: 02184 {鬼|おに} ({桃太郎|ももたろう}), 02201 {傷|きず}
({打撲傷|だぼくしょう}), 04677 コンロ ({消|け}し{忘|わす}れる). Cross-reference harvest also added
reciprocal links into 06016 {初七日|しょなのか}, 06017 {四十九日|しじゅうくにち}, 04048 {草履|ぞうり},
and 27707 ビーチサンダル.

**§4 cross-model self-check on all 27 changed entries (20 new plus 7 neighbors touched by the
noentry and cross-reference passes): 0 flags on the new entries.** Five flags landed on
pre-existing neighbor entries; three applied (04048 {草履|ぞうり}'s formality tag contradicted its
own notes that zori "can be formal or casual," corrected to neutral; 04677 コンロ and 30952
{打撲傷|だぼくしょう} each carried a semantic tag that didn't fit — "food" on a stove, "body-part"
on an injury — both removed), two rejected as reviewer noise (06017 {四十九日|しじゅうくにち}'s
gloss covers both the day and the memorial service, consistent with its sibling entries; 30944
{吸|す}い{口|くち}'s tags match its defined culinary sense, the mouthpiece sense is just an aside in
the notes). In-context kana-link check: one flag on a pre-existing entry (04048 {草履|ぞうり}'s
にくそうだった → にくい link), kept as a correct inflected form. Cost $0.014 total.

**Queue**: 20 candidates auto-cleared on `update_indexes.py`; one removed by hand as a duplicate.
Candidate queue stands at 209, with 33 internal-closure candidates left for the next new-entries run.

### 2026-09-15 (Interactive: stranded Routine branches recovered; the Routine now absorbs red PRs)

Four Routine branches had been left unmerged. The causes: the Routine's wait between CI polls was
a backgrounded `sleep`, which returns at once, so it gave up on every PR after about two minutes
while the check takes five to seven; it then pushed a "CI still pending" note, which restarted CI;
two PRs had real one-token CI failures no rule allowed a later run to fix; and the "stale PR"
sweep closed a polish PR whose range the next run had deliberately skipped. Recovered all of it:
merged #3299; absorbed #3293 (20 new entries, IDs 30893–30912: ハチ{公|こう}, {鼠海豚|ねずみいるか},
the crab cluster ズワイ{蟹|がに}/タラバ{蟹|がに}/{毛蟹|けがに}/{花咲蟹|はなさきがに}/{蟹味噌|かにみそ}/
{越前蟹|えちぜんがに}, {科|か}す, and others) and #3290 (polish of 27 entries: canonical note headers,
concrete semantic tags in place of "general", a {双六|すごろく} ↔ {凧揚|たこあ}げ/{羽根|はね}つき/かるた
New-Year-games cluster, a gloss fix for {双六|すごろく}, formality fixes). New tooling:
`pipeline/absorb_branch.py` (policy merge of a stranded branch; `--residue` says what a branch still
holds), `make gate` (exactly the CI checks, run before every push), `pipeline/wait.py` (a wait
that waits). The Routine prompt now absorbs a red predecessor instead of leaving or closing it,
runs the gate before pushing, pushes nothing after opening its PR, and waits properly.

### 2026-09-14 (Routine v3: new-entries — 20 New Entries, IDs 30913–30932)

Created 20 general-tier entries from the "seen in entry" internal-closure lane. Because an
earlier routine PR that same day (still open, CI-failing at the time) had already claimed IDs
30893–30912 for its own 20-entry batch from the same lane, this run manually started numbering
at 30913 instead of trusting `get_next_id.py` (which only scans the local filesystem and would
have reused those IDs), and skipped the 20 candidates that predecessor run had already turned
into entries. One further candidate, ぶり "for the first time in ~" (C23423), was dropped
first as a stale duplicate of the existing suffix entry 28358 〜{ぶり}.

The words: a crab-cluster continuation from 04325 {蟹|かに} ({松葉|まつば}{蟹|がに}, the San'in
regional brand); {送|おく}り{狼|おおかみ} (the "wolf in sheep's clothing" who offers to walk a
woman home); {亥|い} (the boar zodiac sign, adding kanji 亥 to the kanji index); シャンデリア;
the three great tea-ceremony schools ({表千家|おもてせんけ}, {裏千家|うらせんけ},
{武者小路千家|むしゃこうじせんけ}, cross-referenced to each other); 南アフリカ; {離|はな}れ{島|じま};
a wagyu-brand pair, {神戸牛|こうべぎゅう} and {松阪牛|まつさかぎゅう} (auto cross-referenced to
each other by the harvest pass); {一穴|いっけつ} (mainly known through the proverb
{蟻|あり}の{一穴|いっけつ}); {形|けい} (the grammar "-form" suffix, contrasted with the かたち
reading); {中元|ちゅうげん} (root of お{中元|ちゅうげん}); four jump-rope technique terms from
06323 {縄跳|なわと}び ({前跳|まえと}び, {後|うし}ろ{跳|と}び, {交差跳|こうさと}び,
{片足跳|かたあしと}び); and two Buddhist memorial-day terms from 06016 {初七日|しょなのか}
({二七日|ふたなのか}, {三七日|みなのか}).

**Nine stale `noentry` markers resolved** in four existing entries that had been waiting on these
words: 00885 {島|しま} ({離|はな}れ{島|じま}), 01767 アフリカ (南アフリカ), 05008 {天井|てんじょう}
(シャンデリア), and 04451/05507 {茶道|さどう}/{ちゃどう} (all three tea schools, ×2 each in
05507). Cross-reference harvest also added reciprocal links into 12525 {家元|いえもと}, 16950
{無人島|むじんとう}, 12240 {孤島|ことう}, and 06017 {四十九日|しじゅうくにち}.

**§4 self-check on all 34 changed entries (20 new plus 14 neighbors touched by linking and
`noentry` repair): 1 flag applied, 3 rejected.** 04451 {茶道|さどう}'s semantic tags carried a
leftover `food` tag (tea ceremony is not food) — changed to `culture`, matching its sibling entry
05507. The three rejected flags were reviewer noise: a misread of furigana-annotated text in
05507's ALTERNATIVE READING note, an overliteral objection to 06017 {四十九日|しじゅうくにち}'s
gloss (the memorial-service sense is correct and matches the entry's own explanation), and a
stylistic nitpick on 30932 {三七日|みなのか}'s gloss that already matches its sibling entries'
established "Nth-day memorial service" phrasing. In-context kana-link check: 13 links reviewed,
0 flagged. Cost: $0.0174 self-check, $0.5175 spent today against the $5.00 daily cap.

### 2026-09-14 (Routine v3: new-entries — 20 New Entries, IDs 30893–30912)

Created 20 general-tier entries, all from the "seen in entry" internal-closure lane (49 available,
20 taken). ハチ{公|こう} (from 00632 {犬|いぬ}), {鼠海豚|ねずみいるか} (contrasted with 04313
{海豚|いるか}), {大縄|おおなわ} (the rope itself, from 06323 {縄跳|なわと}び), {重圧|じゅうあつ}
(from 07163 プレッシャー), {用地|ようち} (contrasted with 00365 {敷地|しきち}), {専任|せんにん}
(from 00451 {講師|こうし}), {五時|ごじ} (from 00504), a poem cluster from 02139 {詩|し}:
{詩的|してき} and {詩集|ししゅう}, {詐称|さしょう} (from 02628 {学歴|がくれき}), {天賦|てんぷ}
(contrasted with 02772 {才能|さいのう}), {進水|しんすい} (from 04484 {造船|ぞうせん}),
{書架|しょか} (the library-register word for 04489 {本棚|ほんだな}), the verb {科|か}す ("to
impose a fine/penalty," from 04955 {樹木|じゅもく}'s tree-felling example), and a six-word crab
cluster from 04325 {蟹|かに}: ズワイ{蟹|がに}, タラバ{蟹|がに}, {毛蟹|けがに},
{花咲蟹|はなさきがに}, {蟹味噌|かにみそ}, and the regional brand {越前蟹|えちぜんがに}. One new
kanji indexed: {賦|ふ} (levy), added as 02802_fu_none_levy.

**Two stale `noentry` markers resolved**: 04121 {解散|かいさん} ({五時|ごじ}) and 04313
{海豚|いるか} ({鼠海豚|ねずみいるか}). Cross-reference harvest added one reciprocal pair:
30898 {専任|せんにん} ↔ 10675 {非常勤|ひじょうきん}.

**§4 self-check on all 23 changed entries (20 new plus 3 touched by the stale-link and
cross-reference passes): 2 flags, 1 applied, 1 rejected.** 04121 {解散|かいさん}'s example 5
translation ("The tour was dismissed in front of the station") was unnatural English for a
group simply dispersing — reworded to "The tour group dispersed in front of the station."
Rejected a notes-fact flag on ハチ{公|こう} as a model misreading (its suggested correction was
identical to the original text). In-context kana-link check: 0 flags. Cost: $0.0108 self-check,
$0.5109 spent today against the $5.00 daily cap.

**Queue**: 20 candidates auto-cleared on `update_indexes.py`. Candidate queue stands at 205.
