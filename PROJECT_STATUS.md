# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-13
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
| Total entries | ~30,405 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,562 (open) |
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

### 2026-08-11 (Routine: candidate restock — 75 words added, queue 102 → 177)
Second restock of the word queue that feeds entry writing, run under the new vetting workflow. **75 of 76 proposed words were added** (浅草 turned out to already have an entry). The run first measured where the dictionary is still thin, and the answer is worth recording: **ordinary vocabulary is close to exhausted**. Four trial batches drawn from different areas came back almost entirely as words we already have — office and business life 25 out of 25 already present, residency and administrative paperwork 14 of 15, modern-life compounds and weather words 25 of 28, mimetics and literary-register verbs 13 of 18. Proper names, opened up only this morning, ran the other way: roughly four in five survived. So this batch is deliberately weighted toward names — **64 proper nouns and 11 ordinary words**. The names were chosen for the lexical work they do beyond pointing at a referent: {清水寺|きよみずでら} (source of {清水|きよみず}の{舞台|ぶたい}から{飛|と}び{降|お}りる), {築地|つきじ}, {永田町|ながたちょう} and {霞|かすみ}が{関|せき} as metonyms for the fish trade, politics and the bureaucracy, {原宿|はらじゅく} (as in {原宿系|はらじゅくけい}), {上杉謙信|うえすぎけんしん} (behind {敵|てき}に{塩|しお}を{送|おく}る), {源義経|みなもとのよしつね} (behind {判官|ほうがん}びいき), {世阿弥|ぜあみ} ({初心|しょしん}{忘|わす}るべからず), plus the school-canon literary works ({竹取|たけとり}{物語|ものがたり}, {平家|へいけ}{物語|ものがたり}, {徒然草|つれづれぐさ}, {方丈記|ほうじょうき}, {奥|おく}の{細道|ほそみち}, {羅生門|らしょうもん}, {走|はし}れメロス) and four historical periods. The 11 ordinary words are the survivors of the thin veins: ノルマ, サプリ, {厚生|こうせい}{年金|ねんきん}, {買|か}い{占|し}め, {食品|しょくひん}ロス, {時雨|しぐれ}, {顧|かえり}みる (distinguished from the existing {省|かえり}みる), and the mimetics まざまざ, ひしひし, ずけずけ, こぢんまり. A second read of the added list corrected one label: {大河|たいが}ドラマ was filed as a proper noun but is a genre term, and its note now says so. Two structural notes for future restocks: no semantic field is below 60% coverage any more, and every remaining scenario "gap" is a conjugated form or free phrase that the vetting gates reject, so those two audit tools are no longer usable as generation aims.

### 2026-08-11 (Candidate-queue overhaul: cleanup, verified-restock workflow, proper nouns in scope, new `candidates` Routine mode)
Curator-directed session answering the six-run escalation about the unusable candidate queue. **Cleanup**: all 964 corpus-harvested candidates (Feb–May 2026) were removed from `candidate_words.json` — coinages, free phrases, inflected forms, number+counter combinations, wrong glosses — and archived with reason labels to `planning/archive/candidate-cleanup-2026-08-11.json`; the 5 recent "seen in entry" candidates were kept. **New workflow**: candidate discovery is now the *verified restock* — generate from lexical knowledge aimed by gap data, vet every word against explicit gates (real word, lemma form, headword-worthy, correct reading/gloss, learner value), add via the new duplicate-checking `manage_candidates.py add-batch` (a `remove` subcommand was also added). `prompts/newcandidates.md` and the `find-candidates` skill were rewritten around this; `corpus_harvesting.md` is deprecated. **Proper nouns are now in scope** (place/person/organization/work/event/brand names), prioritizing collocationally and semantically rich names (甲子園-style metonymy, 〜の銀座 patterns, banknote figures); seven semantic tags were added to `VALID_SEMANTIC` (`proper-noun` umbrella + six categories) with an enforced pairing rule in `validate_tags.py`, and 56 existing proper-noun entries (東京, 富士山, 芥川賞, 日本銀行, 聖徳太子, 紅白歌合戦…) were retro-tagged for consistency. **New Routine mode**: `candidates` joined the selector rotation (weight 0.10), self-suppressing while the queue holds ≥150 words and boosted when it drops below 80, so restock fires exactly when needed; selector tests extended (16 pass). **First restock executed**: 88 vetted words added (73 rich proper nouns — 新宿, 山手線, 関ヶ原, 夏目漱石's peers 紫式部/織田信長/福沢諭吉, トヨタ, ジブリ, 源氏物語, ドラえもん, 箱根駅伝 — plus salvaged real words in correct lemma form such as 擦り寄る, 手薄, 底力, and idioms/proverbs 匙を投げる, 渡りに船, 餅は餅屋). Queue now 93, every word entry-ready. Note: 夏目漱石 (C22806) no longer needs a curator call — person names are in scope.

### 2026-08-11 (Routine v2: new-entries — 20 New Entries, IDs 30555–30574)
Created 20 general-tier entries. **Twelve come from the "seen in entry" lane, which this run drains again** (13 available, 1 skipped). The skip is C22806 {夏目漱石|なつめそうせき}, held back for the **sixth consecutive run** — whether a novelist's name belongs in a vocabulary dictionary that carries place names but no people is still the curator's call. **Six of the twelve close gaps opened by the last two runs' own batches**: {慎重派|しんちょうは} joins the 〜{派|は} family against 30541 {推進派|すいしんは} and 30532 {反対派|はんたいは}, split on **whether the camp opposes the plan or only its pace**, with {派閥|はばつ} marked off as a standing grouping rather than a position on one issue; {被害額|ひがいがく} is entered as the counterpart of 30547 {損害額|そんがいがく} (victim's side vs. loss side) and its notes warn that the word is always a money figure — physical extent is {被害|ひがい}{状況|じょうきょう}; {記者団|きしゃだん} contrasts the impromptu doorstep ({記者団|きしゃだん}に{語|かた}る) with the arranged {記者会見|きしゃかいけん}; {言|い}い{添|そ}える follows 30546 {言|い}い{足|た}す and is split from {付|つ}け{加|くわ}える, which also covers information and objects; and the two osechi entries たたきごぼう and ごまめ complete the Kansai/Kanto {三|み}つ{肴|ざかな} pair around 30553 {田作|たづく}り and 30554. **Three grammar and register entries** carry the run's heaviest content: のです is two-sense with 6 examples, documenting the な linker after nouns and na-adjectives and the trap that adding it where no explanation was invited reads as a correction ({私|わたし}は{田中|たなか}なんです); ます documents the {連用形|れんようけい} attachment, the six main forms, and the rule that plain forms are normal inside relative clauses; お{時間|じかん} is marked as usable only of the listener's time. **A five-entry counter set** fills a real hole — the dictionary had {一人|ひとり}, {二人|ふたり}, {三人|さんにん}, {七人|しちにん}, {十人|じゅうにん} and {何人|なんにん} but nothing between three and seven or at eight and nine — so {四人|よにん} (never しにん, the {死人|しにん} collision), {五人|ごにん}, {六人|ろくにん} and {八人|はちにん} (documenting that {人|にん} is **not** one of the counters that turn {六|ろく}/{八|はち} into ろっ/はっ), and {九人|きゅうにん} (きゅうにん standard, くにん fixed-phrase only) were written as a cross-linked series. Rest: オファー (narrower than English "offer" — work and contracts, not help or goods), ハンドソープ and ボディソープ against 04981 {石鹸|せっけん}, {持|も}ち{時間|じかん} (the game clock and the speaker's allowance, against 30253 {時間切|じかんぎ}れ), {荷物|にもつ}{預|あず}かり (staffed counter vs. コインロッカー), and {店舗|てんぽ}{展開|てんかい} (the program, against {出店|しゅってん}, one location). Conjugation tables added to 3 entries (1 ichidan, 2 suru); **no new kanji**. 4 candidates added from words the new entries reference (コインロッカー, {制限|せいげん}{時間|じかん}, {五人|ごにん}{囃子|ばやし}, {三|み}つ{肴|ざかな}); 1 stale removed — C19293 {七人|ななにん}, since 30350 {七人|しちにん} already documents ななにん as the spoken reading. 969 candidates remain. §4 cross-model self-check on all 20: **1 flagged, 1 applied, 0 rejected**. $0.0087. Applied: ます carried `formality: "formal"`, but ます is 丁寧語 — the ordinary polite register of everyday speech, not formal register — and its closest sibling 09485 です is tagged `neutral`/`polite`; corrected to match. Three slips were caught locally before the self-check, all malformed furigana wrappers: a nested `{おせち{料理|りょうり}}`, a stray `{`, and braces around katakana `{スーツケース}`.

- **Groups / media / money (3)**: {慎重派|しんちょうは}, {記者団|きしゃだん}, {被害額|ひがいがく}
- **Grammar / register (3)**: のです, ます, お{時間|じかん}
- **People counts (5)**: {四人|よにん}, {五人|ごにん}, {六人|ろくにん}, {八人|はちにん}, {九人|きゅうにん}
- **Food (2)**: たたきごぼう, ごまめ
- **Daily life / travel (3)**: ハンドソープ, ボディソープ, {荷物|にもつ}{預|あず}かり
- **Work / time (4)**: オファー, {店舗|てんぽ}{展開|てんかい}, {持|も}ち{時間|じかん}, {言|い}い{添|そ}える

**Escalation (unchanged, sixth report)**: the "seen in entry" lane is again the only usable source. Beyond it, the ~970 corpus-harvested candidates are non-words ({権使|けんし}, {些道|さどう}, {個尊|こそん}, {怒燥|どとう}, {内疎外内|ないそがいない}), compositional phrases ({歩|ある}き{続|つづ}ける, {効率|こうりつ}が{悪|わる}い), inflected forms filed as headwords ({強|つよ}く, {知|し}らない, {与|あた}えられる), and plainly wrong glosses (アンパッサン glossed "ice cream sundae"; {尾張|おわり} glossed "end, finish"). This run reached 20 only by adding a counter set and three ordinary words hand-picked out of that pool. Two asks: a `clean_up_candidates_list.md` pass to delete the noise, and a curator restock of real headwords. Related tooling note: the selector reported "candidates plentiful" from a raw row count of 984 when roughly 13 were usable — a quality-weighted signal would tell those apart.

