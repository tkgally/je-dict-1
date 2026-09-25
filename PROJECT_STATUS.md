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
