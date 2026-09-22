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

### 2026-09-22 (Evaluation: TypeSafe's Jev model for the Routine)

Tested whether the new decision-only model Jev (`typesafe/jev-1.13`, via OpenRouter's decisions
endpoint) could do useful work for the Routine, spending about $0.95 of a $5 budget. Verdict in
`enhancement/jev-evaluation-2026-09-22.md`: not for furigana (Gemini 2.5 Flash caught 70 percent
of injected wrong readings with no false flags; Jev caught 25 percent, and picks the right
reading of an ambiguous kanji less often than a frequency baseline), not for the accuracy review
(both models weak on the real translation, gloss and notes errors recovered from git history),
and blind to the commonest kana-link mistake (particle でも linked to the conjunction). Genuinely
good and cheap at two closed judgments: wrong-domain semantic tags (96 to 99 percent precision at
55 to 89 percent recall) and which numbered sense an example illustrates (97.5 percent agreement,
with several disagreements that look like entry errors). Recommended: two one-time sweeps of those
kinds; no change to the Routine's models. Scripts in `enhancement/jev-eval/`.

### 2026-09-21 (Routine v3: new-entries — 20 New Entries, IDs 30994–31013)

Created 20 general-tier entries: 5 from the "seen in entry" internal-closure lane plus 15 curated
proper nouns from the queue (7 countries, 8 historical/literary figures) to round out the session.
Two internal-closure candidates in the queue, {見|み}ごたえ (C23499) and {読|よ}みごたえ (C23500),
were dropped first as stale duplicates — kana-only spellings of the existing kanji entries
{見応|みごた}え (07274) and {読|よ}み{応|ごた}え (07273).

Internal-closure words: {損得勘定|そんとくかんじょう} (from 08055 {打算的|ださんてき}),
{希望退職|きぼうたいしょく} (from 08070 {早期退職|そうきたいしょく}), やけ{酒|ざけ} (from 08073
やけ{食|ぐ}い), {見|み}がい and やりごたえ (both from 08074/08085's related-word lists). Queue
proper nouns: スペイン, ロシア, ブラジル, タイ, ベトナム, スイス, エジプト, and the historical
figures {徳川家康|とくがわいえやす}, {坂本龍馬|さかもとりょうま}, {福沢諭吉|ふくざわゆきち},
{野口英世|のぐちひでよ}, {樋口一葉|ひぐちいちよう}, {芥川龍之介|あくたがわりゅうのすけ},
{太宰治|だざいおさむ}, {川端康成|かわばたやすなり}. Added kanji 之 to the kanji index (from
{龍之介|りゅうのすけ}).

**Four stale `noentry` markers resolved** (class A2, hand-verified): 03382 {対|たい} (ブラジル),
04285 {南米|なんべい} (スペイン, ブラジル), and 05324 {古代|こだい} (エジプト). Cross-reference
harvest also added reciprocal links into 16450 {定年退職|ていねんたいしょく}, 08061
{暴飲暴食|ぼういんぼうしょく}, 06653 やり{甲斐|がい}, and 08039 {食|た}べごたえ.

**§4 self-check on all 27 changed entries (20 new plus 7 neighbors touched by linking and
`noentry` repair): 1 flag applied, 3 rejected.** 31013 {川端康成|かわばたやすなり}'s notes wrongly
said he died "four years after" {三島由紀夫|みしまゆきお}'s 1970 suicide — corrected to "about a
year and a half after" (Kawabata died April 1972). The three rejected flags were reviewer noise:
a restatement of 05324's already-correct "up to around the 12th century" (1185, the end of the
Heian period, is in the 12th century), and two no-op flags on 31002 タイ and 31011
{芥川龍之介|あくたがわりゅうのすけ} that suggested changing values to themselves. In-context
kana-link check: 4 links reviewed, 0 flagged. Cost: $0.0130 self-check, $0.9982 spent today
against the $5.00 daily cap.

### 2026-09-20 (Routine v3: new-entries — 20 New Entries, IDs 30974–30993)

Created 20 general-tier entries: 18 from the "seen in entry" internal-closure lane (19 available,
one — {しがち}, C23483 — dropped as a stale duplicate of the existing `〜がち` suffix entry, which
already documents しがち as its する-stem example) plus two curated historical figures from the
proper-noun queue to round out the session: {織田信長|おだのぶなが} and {豊臣秀吉|とよとみひでよし}.
Internal-closure words: {大口真神|おおくちのまかみ} (the wolf deity, from 04334 {狼|おおかみ}),
{師|し} (the bound "teacher/mentor" noun, from 07388 {凌|しの}ぐ), {藤田|ふじた} and {藤井|ふじい}
(common {藤|ふじ}-based surnames, from 04396 {藤|ふじ}), {地竜|じりゅう} (dried earthworm in folk
medicine, from 04932 {蚯蚓|みみず}), {両生|りょうせい} (the "amphibious" compound element, from
04924 {両生類|りょうせいるい}), イモリ (newt, also from 04924), がぶがぶ (gulping greedily, from
05776/05778 ごくごく/ちびちび), {寝|ね}ぼすけ (sleepyhead, from 05347 {寝惚|ねぼ}ける), せせら
{笑|わら}う (to sneer, from 07449 {鼻|はな}で{笑|わら}う), {二言目|ふたことめ}には (from 00736
{二|に}), {余剰金|よじょうきん} and {設備投資|せつびとうし} (from 08005 {充当|じゅうとう}), and
the four remaining longevity milestones from 05807 {還暦|かんれき}: {傘寿|さんじゅ} (80),
{米寿|べいじゅ} (88), {卒寿|そつじゅ} (90), {白寿|はくじゅ} (99), plus ちゃんちゃんこ (the padded
vest given at {還暦|かんれき}).

**Note for the curator**: the 2026-09-18 session log set aside {大口真神|おおくちのまかみ}, {師|し},
{両生|りょうせい}, and {藤田|ふじた}/{藤井|ふじい} as too thin for standalone entries. This session
wrote them anyway, on the following reasoning: {大口真神|おおくちのまかみ} follows the existing
{天狗|てんぐ} pattern (`semantic: religion, culture`, no proper-noun tag) rather than needing a
proper-noun category; {師|し} and {両生|りょうせい} are documented candidly as bound
forms that mostly appear in fixed phrases or compounds (matching how the dictionary already treats
the `〜師` suffix entry, 30801); and {藤田|ふじた}/{藤井|ふじい} follow the precedent already set by
27597 {佐藤|さとう} (a generic-surname entry, tagged `person`, no specific referent). Worth a spot
check if this reasoning doesn't hold up.

**Newcomer-ambiguity retargets**: creating {師|し} (30975) gave the existing suffix entry
{〜師|し} (30801) a homograph. `check_link_newcomers.py` flagged 9 existing inline links to 30801;
7 were correctly suffix uses (狂言{師|し}, 木彫り{師|し}, {彫|ほ}り{師|し}, {指圧|しあつ}{師|し},
{整体|せいたい}{師|し} — left unchanged) and 2 were retargeted to the new entry because the
sentence meant the bound noun "teacher," not the practitioner suffix: 07388 {凌|しの}ぐ's example
("{弟子|でし}が{師|し}を{凌|しの}ぐ" — a student surpassing their teacher) and 12421
{師匠|ししょう}'s etymology note (師 + 匠 = teacher + artisan).

**§4 self-check on all 20 new entries: 0 flags.** In-context kana-link check: no kana-base links
in the selection. Cost: $0.0096 self-check, $0.4908 spent today against the $5.00 daily cap.

**Queue**: 20 candidates auto-cleared on `update_indexes.py` (19 internal-closure matches plus the
two curated additions); one further removed by hand as a stale duplicate before writing (see above).
Candidate queue stands at 174.

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

