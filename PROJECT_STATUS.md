# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-15
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
| Total entries | ~30,464 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,681 (open) |
| Candidate words | ~154 (all vetted; queue cleaned 2026-08-11) |
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

### 2026-08-15 (Routine v2: new-entries — 20 New Entries, IDs 30654–30673)

Created 20 general-tier entries, **all 20 from the "seen in entry" lane** — words the dictionary already used inside other entries' examples and notes but had never defined. That empties the lane completely for the second run in a row. The words break down as follows.

- **Health (3)**: {心療内科|しんりょうないか} (the psychosomatic medicine department, written against {精神科|せいしんか} and {神経内科|しんけいないか} because choosing the right clinic is the real-world question), {自律神経失調症|じりつしんけいしっちょうしょう} (noted as the broad everyday diagnostic label it is, not a precise disease), and {瘤|こぶ} (with the idiom {目|め}の{上|うえ}のたんこぶ).
- **Cooking and cutting (2)**: {飾|かざ}り{包丁|ぼうちょう} and {切|き}り{込|こ}み. The first is cross-linked to {隠|かく}し{包丁|ぼうちょう} (created yesterday) as a contrast — decorative cuts versus cuts hidden for cooking — which is exactly the distinction that sends learners to a dictionary.
- **Grammar and register (3)**: ごとに (written around the ごとに/おきに confusion — "every day" versus "every other day" — which is the single most common learner error with this suffix), ついさっき (informal; pointed at {先|さき}ほど for polite contexts), and ためらいがち (with the 〜がち suffix pattern).
- **News and time vocabulary (2)**: {供給不足|きょうきゅうぶそく} (linked to the existing {供給過剰|きょうきゅうかじょう}) and {十数年|じゅうすうねん}, contrasted with {数十年|すうじゅうねん} — the same characters in the other order, meaning decades rather than a dozen years.
- **Shinto ritual language (2)**: {祝詞|のりと} and {奏上|そうじょう}, cross-linked to each other since they appear together in the fixed phrase {祝詞|のりと}を{奏上|そうじょう}する.
- **General vocabulary (8)**: {音楽祭|おんがくさい} (distinguished from フェス), ごぼごぼ, {肥|こ}やし (two senses — manure, and the figurative "nourishment" of 失敗を肥やしにする), チェスト (with the warning that it never means the body part), {夏物|なつもの} (linked to {冬物|ふゆもの}), {賞状|しょうじょう}, {敬虔|けいけん}, and {得意顔|とくいがお}.

A conjugation table was generated for the one suru-verb ({奏上|そうじょう}する). Two new kanji were given index IDs: 瘤 (02795) and 虔 (02796).

**§4 cross-model self-check on all 20 new entries: clean — zero flags** across glosses, example translations, and semantic tags. $0.009.

**Queue note**: eight new candidates were captured from words these entries reference but do not define — おきに, {上奏|じょうそう}, {表彰状|ひょうしょうじょう}, {信心深|しんじんぶか}い, したり{顔|がお}, {更年期障害|こうねんきしょうがい}, {地鎮祭|じちんさい}, and {先|さき}ほど. The candidate queue stands at 154.

**Two systemic notes logged** to `polishing/observations.md`: `prompts/newentries.md` documents the closed lists for POS, semantic, and domain tags but never lists the four legal `formality` values, so the natural English word "casual" fails validation (one entry tripped on it this run); and bare kanji slip into notes through English section headers that embed a Japanese suffix (`THE 〜物 SERIES:`), which the furigana scanner catches only after the entry is written (two entries this run).

### 2026-08-14 (Routine v2: new-entries — 19 New Entries, IDs 30635–30653)

Created 19 general-tier entries, **all of them from the "seen in entry" lane** — words the dictionary already used inside other entries' examples and notes but had never defined. That empties the lane again. The words break down as follows.

- **Words the dictionary owed itself from yesterday's Tokyo-district entries (4)**: {歩行者天国|ほこうしゃてんごく} (the weekend car-free street, named in the Ginza entry), {歌舞伎町|かぶきちょう} (the Shinjuku nightlife quarter, written per the proper-noun policy so it covers what the name connotes — nightlife and slight disrepute — and notes that it has nothing to do with kabuki as an art), {映画俳優|えいがはいゆう} and {映画祭|えいがさい}.
- **Idioms (2)**: {目|め}を{光|ひか}らせる and {目|め}を{奪|うば}う, each cross-noted against the near-neighbour learners confuse it with ({目|め}を{配|くば}る, added yesterday, and {目立|めだ}つ).
- **Casual speech (3)**: うちら, かなあ, どっちみち — all three written against their neutral or formal equivalents, since choosing the wrong register is the actual learner problem.
- **Formal and legal vocabulary (3)**: {選任|せんにん}, {処|しょ}する (two senses — handling a situation, and imposing a sentence), and いずれにしても.
- **General vocabulary (7)**: {品不足|しなぶそく}, {数十年|すうじゅうねん}, {国鉄|こくてつ} (the pre-1987 national railway, still heard from older speakers), {我|われ}, {心身症|しんしんしょう}, {隠|かく}し{包丁|ぼうちょう}, どうあっても.

One candidate was dropped as stale: 足手まとい had been queued under the reading あしてまとい, but the word is already entry 30625 under its standard reading あしでまとい. Conjugation tables were generated for the two suru-verbs. No new kanji.

**§4 cross-model self-check on all 19 new entries: one flag, applied.** An independent model objected that tagging いずれにしても as `formal` overstated the register — correctly, since the entry's own note says the phrase is at home in ordinary polite conversation. Retagged `neutral`. $0.008.

**Queue note**: seven new candidates were captured from words these entries reference but do not define ({心療内科|しんりょうないか}, {自律神経失調症|じりつしんけいしっちょうしょう}, {飾|かざ}り{包丁|ぼうちょう}, {切|き}り{込|こ}み, {供給不足|きょうきゅうぶそく}, {十数年|じゅうすうねん}, {音楽祭|おんがくさい}). The candidate queue now stands at 153 — just above the 150-word mark below which the selector stops suppressing a `candidates` restock run.

**Systemic issue found**: `build/add_conjugations.py` generates the potential form of single-kanji サ変 verbs as 〜できる ({処|しょ}できる), which is not Japanese — the correct form is 〜せる ({処|しょ}せる). Existing entries {察|さっ}する and {面|めん}する carry the wrong form today. Fixed by hand in the new entry and logged to `polishing/observations.md` as a systemic-fix candidate.

### 2026-08-13 (Routine v2: new-entries — 20 New Entries, IDs 30615–30634)

Created 20 general-tier entries. **Sixteen came from the "seen in entry" lane** — words the dictionary already uses inside other entries but had never defined — which empties that lane again. Those sixteen: the two hina-doll display terms {内裏雛|だいりびな} and {三人官女|さんにんかんじょ} (each written with the display's tier structure and the regional placement difference that learners actually ask about), the idiom {地獄|じごく}に{仏|ほとけ} (cross-noted against {渡|わた}りに{船|ふね}, added yesterday, since the two differ in how desperate the situation must be), {品薄|しなうす} (distinguished from {品切|しなぎ}れ and {品不足|しなぶそく}), {船酔|ふなよ}い, the three body-part idioms {耳|みみ}に{残|のこ}る, {目|め}を{配|くば}る, and {目|め}を{引|ひ}く (each contrasted with the near-neighbour that learners confuse it with — {心|こころ}に{残|のこ}る, {気|き}を{配|くば}る, {目立|めだ}つ), the two grammar patterns からといって and ではないか (both written with the following-clause restrictions that make them work), {何十年|なんじゅうねん} (with the note that も is effectively obligatory), {足手|あしで}まとい, the mimetic adverb まじまじ (contrasted with じろじろ, which is rude where this one is merely intent), {抜|ぬ}け{穴|あな} (two senses — the legal loophole and the literal secret passage), {北極星|ほっきょくせい}, and the hesitation filler そのー. **The other four are proper nouns** from the vetted queue — the Tokyo districts {銀座|ぎんざ}, {渋谷|しぶや}, {秋葉原|あきはばら}, and {新宿|しんじゅく} — written per the 2026-08-11 proper-noun policy, so each covers what the name connotes and not merely where it is: 〜の{銀座|ぎんざ} for any bustling shopping street, {渋谷|しぶや}{系|けい} for trends, アキバ and its generational shifts, and Shinjuku Station as the standing byword for crowds and getting lost. A conjugation table was generated for {船酔|ふなよ}いする. No new kanji. **§4 cross-model self-check on all 20 new entries: clean — zero flags.** $0.009.

- **Traditional culture and place (6)**: {内裏雛|だいりびな}, {三人官女|さんにんかんじょ}, {銀座|ぎんざ}, {渋谷|しぶや}, {秋葉原|あきはばら}, {新宿|しんじゅく}
- **Idioms (4)**: {地獄|じごく}に{仏|ほとけ}, {耳|みみ}に{残|のこ}る, {目|め}を{配|くば}る, {目|め}を{引|ひ}く
- **Grammar and speech (3)**: からといって, ではないか, そのー
- **General vocabulary (7)**: {品薄|しなうす}, {船酔|ふなよ}い, {何十年|なんじゅうねん}, {足手|あしで}まとい, まじまじ, {抜|ぬ}け{穴|あな}, {北極星|ほっきょくせい}

**Queue note**: six new candidates were captured from words these entries reference but do not define — {歩行者天国|ほこうしゃてんごく}, {品不足|しなぶそく}, {目|め}を{光|ひか}らせる, {目|め}を{奪|うば}う, {数十年|すうじゅうねん}, and {歌舞伎町|かぶきちょう}. Candidate queue now 156, still above the 150-word mark at which a `candidates` restock run stops being suppressed.

### 2026-08-13 (Routine v2: new-entries — 20 New Entries, IDs 30595–30614, plus a new sense for 〜ぶり)
Created 20 general-tier entries. **Ten came from the "seen in entry" lane** — words the dictionary already uses inside other entries but had never defined — and that lane is now empty. Those ten: {五人|ごにん}{囃子|ばやし} and {三|み}つ{肴|ざかな} (the five musicians of a hina-doll display and the three dishes that make a minimal New Year's table, both written with the cultural context that earns them an entry), {几帳|きちょう} (the Heian curtained screen, with the memory hook that {几帳面|きちょうめん} is said to come from its joinery), {頭|あたま}が{柔|やわ}らかい (cross-noted against the far commoner {頭|あたま}が{固|かた}い, since the negation of this phrase is not idiomatic), {石頭|いしあたま}, {追|お}いすがる (two senses — clinging to someone who is leaving, and closing on a leader in a race), {追跡者|ついせきしゃ}, しがらみ (with the river-weir etymology that explains the image), スパート (noted as living mostly inside ラストスパート, which reaches well beyond sport), and {本腰|ほんごし} (essentially bound to {本腰|ほんごし}を{入|い}れる). **The other ten are general vocabulary**: {手|て}{薄|うす}, {底|そこ}{力|ぢから} (with the ぢ spelling flagged), {油|あぶら}を{売|う}る (with its hair-oil-seller etymology), {渡|わた}りに{船|ふね}, {火|ひ}の{車|くるま} (restricted to money — a tight schedule is not 火の車), {好|こう}{循環|じゅんかん} (pointing at the commoner {悪|あく}{循環|じゅんかん}), {芋|いも}づる{式|しき}, {適材|てきざい}{適所|てきしょ}, {顧|かえり}みる (distinguished from the existing {省|かえり}みる at 13656), and {買|か}い{占|し}め. Conjugation tables added to 4 entries (2 godan, 1 ichidan, 1 suru). No new kanji. **§4 cross-model self-check on all 21 changed entries: 1 flag, rejected** — the model wanted {顧|かえり}みる labelled `neutral` rather than `formal`, but the entry's own notes call it literary and its sibling 省みる carries the same label. $0.009.

- **Traditional culture (3)**: {五人|ごにん}{囃子|ばやし}, {三|み}つ{肴|ざかな}, {几帳|きちょう}
- **Character and idiom (6)**: {頭|あたま}が{柔|やわ}らかい, {石頭|いしあたま}, {油|あぶら}を{売|う}る, {渡|わた}りに{船|ふね}, {火|ひ}の{車|くるま}, {芋|いも}づる{式|しき}
- **Pursuit and effort (5)**: {追|お}いすがる, {追跡者|ついせきしゃ}, スパート, {本腰|ほんごし}, {底|そこ}{力|ぢから}
- **Work and economy (4)**: {手|て}{薄|うす}, {好|こう}{循環|じゅんかん}, {適材|てきざい}{適所|てきしょ}, {買|か}い{占|し}め
- **Other (2)**: しがらみ, {顧|かえり}みる

**Existing entry extended**: 28358 〜ぶり gained a second sense, "manner of doing" ({仕事|しごと}ぶり, {話|はな}しぶり, {暮|く}らしぶり, and the livelier っぷり variant), which the previous run had identified as belonging there rather than in a new entry.

**Queue note**: five candidates were removed as stale. Four were spelling variants of words the dictionary already has — {擦|す}り{寄|よ}る against 17576 ({摺|す}り{寄|よ}る), {匙|さじ}を{投|な}げる against 20433 (さじを{投|な}げる), {首|くび}をかしげる against 17531 ({首|くび}を{傾|かし}げる), and {有耶無耶|うやむや} against 08049 (うやむや) — and the fifth was the ぶり sense folded into 28358. The duplicate checker reports such pairs only as "homophones", so they pass candidate vetting; that gap and a related one (vetting cannot see that a word matches an existing entry's *other* sense) are logged as observations. Four new candidates were added from words the new entries reference: {内裏雛|だいりびな}, {三人|さんにん}{官女|かんじょ}, {地獄|じごく}に{仏|ほとけ}, {品薄|しなうす}. Candidate queue now 154 — only just above the 150-word mark at which a `candidates` restock run stops being suppressed.

### 2026-08-12 (Routine v2: new-entries — 20 New Entries, IDs 30575–30594)
Created 20 general-tier entries, **all 20 drawn from the "seen in entry" lane** — words the dictionary already uses inside other entries' examples and notes but had never defined. This is the first run in some months where that lane alone supplied a full batch, because the 2026-08-11 queue overhaul left only vetted words behind. **Fourteen of the twenty are everyday idioms built on a body part**, filling out the block of such expressions the polish runs walked through last week: {口|くち}が{滑|すべ}る (to let something slip) and {口|くち}が{悪|わる}い (sharp-tongued), {頭|あたま}に{来|く}る (to lose one's temper, marked informal against the neutral {腹|はら}が{立|た}つ it now cross-references), {顔|かお}が{利|き}く (to have pull somewhere), {声|こえ}をかける (written with two senses — calling out to a stranger, and inviting someone along, six examples), {手|て}が{空|あ}く and {手|て}が{足|た}りない (entered as a linked pair, free hands vs. not enough hands), {肩身|かたみ}が{広|ひろ}い (able to hold one's head high — noted as the rarer mirror of the common {肩身|かたみ}が{狭|せま}い), {気|き}が{長|なが}い (entered as the antonym the existing {気|き}が{短|みじか}い entry had been pointing at with a dead link), {気|き}が{回|まわ}る, {気|き}を{取|と}られる, plus {怒|おこ}りっぽい and {居|い}づらい as i-adjectives with full conjugation tables, and {図星|ずぼし}. **The remaining six are ordinary vocabulary**: コインロッカー, {制限時間|せいげんじかん}, {古米|こまい} (old rice, cross-linked as the antonym of {新米|しんまい}, with the note that {新米|しんまい} alone also means "novice"), {主|ぬし} (the ownership reading, distinguished from the あるじ entry at 19365 and shown chiefly through {世帯主|せたいぬし}/{飼|か}い{主|ぬし}/{持|も}ち{主|ぬし}), {候補生|こうほせい}, and **the dictionary's first novelist**, {夏目漱石|なつめそうせき} — held back for six consecutive runs before proper names were ruled in scope on 2026-08-11, and written with the connotations that earn a name an entry (the pen name used alone, the old 1,000-yen note, {坊|ぼ}っちゃん as a nickname). One new kanji, 漱, was given an index ID. **§4 cross-model self-check on all 20 entries: clean — 0 issues raised.** $0.009. Four slips were caught locally before that check: two entries had an English word or katakana accidentally inside a furigana wrapper, one used a formality label outside the schema's list, and the {手|て}が{空|あ}く/{手|て}が{足|た}りない pair briefly cross-referenced a wrong entry ID.

- **Body-part idioms (12)**: {口|くち}が{滑|すべ}る, {口|くち}が{悪|わる}い, {頭|あたま}に{来|く}る, {顔|かお}が{利|き}く, {声|こえ}をかける, {手|て}が{空|あ}く, {手|て}が{足|た}りない, {肩身|かたみ}が{広|ひろ}い, {気|き}が{長|なが}い, {気|き}が{回|まわ}る, {気|き}を{取|と}られる, {図星|ずぼし}
- **Character adjectives (2)**: {怒|おこ}りっぽい, {居|い}づらい
- **Everyday nouns (5)**: コインロッカー, {制限時間|せいげんじかん}, {古米|こまい}, {主|ぬし}, {候補生|こうほせい}
- **Proper noun (1)**: {夏目漱石|なつめそうせき}

**Queue note**: ten candidate rows (C23094–C23103) had been filed with furigana markup inside the word itself, so the automatic "this word now has an entry" sync could not match them and they were removed by hand; a fix for the candidate tool is logged in `polishing/observations.md`. One candidate, ぶり in the sense of "manner of doing" ({仕事|しごと}ぶり), was deliberately not created — entry 28358 already holds that headword for the unrelated "for the first time in" sense, so this belongs there as a second sense. Candidate queue now 167.
