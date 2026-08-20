# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-20
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

### 2026-08-20 (Routine v2: new-entries — 20 New Entries, IDs 30694–30713)

Created 20 general-tier entries. **Twelve came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined — which empties that lane except for one word left deliberately unclaimed (see the queue note). Those twelve: ことごとく (the formal "every one without exception", noted as attaching mostly to unfortunate outcomes), {街宣車|がいせんしゃ} (the loudspeaker van, with its right-wing association explained and the neutral {選挙|せんきょ}カー offered as the alternative), {養成所|ようせいじょ} (distinguished from {専門学校|せんもんがっこう} and {研修所|けんしゅうじょ}), {協和音|きょうわおん} (cross-linked as the antonym of the existing {不協和音|ふきょうわおん}), コーンスープ and ポタージュ (written as a pair, since Japanese uses ポタージュ specifically for the thick style against clear コンソメ), {名様|めいさま} (the service-industry counter, with the point that staff use it about customers and customers do not use it about themselves), クレカ (casual-only, with クレジットカード named as the form to use in a shop), プリペイドカード, {出|で}だし (the opening of a text, song, or race), {人妻|ひとづま} (with a register note that it is not a neutral way to say a woman is married), and {思|おも}いとどまる (the deliberate decision not to go through with something, contrasted with あきらめる).

**The other eight are proper nouns** — the category opened up on 2026-08-11 — each written so the explanation carries the connotations, not just the referent: the Tokyo districts {池袋|いけぶくろ}, {品川|しながわ}, and {六本木|ろっぽんぎ} (crowds, business travel, and money respectively), the {山手線|やまのてせん} (with {内回|うちまわ}り/{外回|そとまわ}り and "inside the loop" as shorthand for central Tokyo), {神戸|こうべ}, {鎌倉|かまくら} (both the seaside town and the history-class period name), {箱根|はこね} (hot springs and the New Year's ekiden), and {軽井沢|かるいざわ} (a name that signals money and taste more than a location). One godan conjugation table added. No new kanji.

**§4 cross-model self-check on all 21 changed entries: 1 flag, rejected, 0 sent to the curator.** All 20 new entries came back clean. The single flag was on the pre-existing entry 19680 {耐|た}え{難|がた}い, where the model wanted the `formal` register label changed to `neutral`; the entry's own notes describe it as a literary and formal expression, so project policy declines that swap. Cost $0.009.

**Queue note**: the candidate 耐えがたい was removed as a stale duplicate — it is the same word as 19680 {耐|た}え{難|がた}い written with がたい in kana — and 19680's notes now record that spelling. One "seen in entry" candidate was deliberately left in the queue: 脂漏 (seborrhea), harvested from the eczema entry, is a technical dermatology term that a standalone learner entry serves poorly; the reasoning is logged as an observation. Three new candidates were captured from words the new entries reference but do not define: {駅伝|えきでん}, {異人館|いじんかん}, コンソメ. Candidate queue now 154.

### 2026-08-16 (Routine v2: new-entries — 20 New Entries, IDs 30674–30693)

Created 20 general-tier entries, **all 20 from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined. This run deliberately worked two "hub" entries whose internal links all pointed at nothing, so both families are now complete:

- **The "otherwise" family (6)**, all from the dead links inside {さもないと} (entry 06942): さもなければ (formal, written), そうしないと (the everyday spoken choice), じゃないと (casual, two senses — after a noun, and standing alone), でないと (the neutral middle register, two senses), plus だとすると (drawing a provisional conclusion) and ということは (drawing a firm one). Each entry says plainly where it sits on the formality scale, since choosing between them is the actual learner problem.
- **The fractions family (5)**, all from the dead links inside {分数|ぶんすう} (entry 06952): {通分|つうぶん} and {約分|やくぶん} (the two operations, written as each other's complement), and {真分数|しんぶんすう}, {仮分数|かぶんすう}, {帯分数|たいぶんすう} (the three kinds of fraction, cross-explained).
- **Everyday and cultural vocabulary (9)**: おきに (the interval suffix, written directly against ごとに — "every other day" versus "every day" — which is the classic confusion), {表彰状|ひょうしょうじょう} (distinguished from {賞状|しょうじょう} and {感謝状|かんしゃじょう}), {信心深|しんじんぶか}い, したり{顔|がお}, {更年期障害|こうねんきしょうがい}, {地鎮祭|じちんさい} (the ground-breaking rite, with the related {上棟式|じょうとうしき}/{竣工式|しゅんこうしき} named), {上奏|じょうそう} (historical, reporting to the emperor), {心血|しんけつ} (used almost only in {心血|しんけつ}を{注|そそ}ぐ), and {船出|ふなで} (literal sailing and the figurative "new start").

**§4 cross-model self-check on all 20 entries: 5 issues raised, 3 applied, 2 rejected, 0 sent to the curator.** The applied fixes all concerned {通分|つうぶん}: its gloss read "reduction to a common denominator", which invites the wrong reading of "reduce" (the operation usually makes the numbers larger, not smaller), so it now reads "finding a common denominator", and one example whose English restated itself was replaced. The two rejections were a reviewer error about 二日おきに and a request to swap one in-list semantic tag for a broader one, which project policy declines. Cost $0.009.

**Queue note**: the candidate 先ほど was removed as a stale duplicate — it is the same word as the existing {先程|さきほど} entry (04165) written in kana. Twelve new candidates were captured from words used inside the new entries, and the twenty words just written were removed from the queue automatically. Candidate queue now 159.

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
