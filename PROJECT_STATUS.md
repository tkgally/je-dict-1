# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-08-28
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
| Total entries | ~30,544 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,741 (open) |
| Candidate words | ~142 (all vetted; queue cleaned 2026-08-11) |
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

### 2026-08-28 (Routine v2: new-entries — 20 New Entries, IDs 30754–30773)

Created 20 general-tier entries. **Sixteen came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined, which empties that lane: {防弾|ぼうだん} (written so the learner sees it only ever heads a compound), たこ{足|あし}{配線|はいせん} (the overloaded outlet, which Japanese speakers meet as a fire-safety warning), {味|あじ}の{素|もと} (the brand, with the point that older speakers use the name for MSG generally), {時雨|しぐれ}{煮|に}, {相棒|あいぼう} (the palanquin-pole origin, and how it differs from {仲間|なかま} and {同僚|どうりょう}), {箸|はし}{立|た}て (separated from {箸|はし}{置|お}き and {箸|はし}{箱|ばこ}, which learners conflate), {甥|おい}っ{子|こ} and {姪|めい}っ{子|こ} (the affectionate 〜っ{子|こ} forms, noting Japanese has no single word for "nieces and nephews"), {好|す}く (with the warning that the plain affirmative sounds archaic and learners want {好|す}き), {負|ま}けん{気|き}, {動|どう}じる (met almost only as {動|どう}じない), {教諭|きょうゆ} and {獣医師|じゅういし} (the official job titles, each set against the word people actually say — {先生|せんせい} and {獣医|じゅうい}), {色柄物|いろがらもの} (the laundry term off detergent bottles), ラベンダー (with the Furano association), and セラミック (the engineered material, explicitly not {陶器|とうき}).

**The other four are proper nouns** from the vetted queue, written so the explanation carries the connotations: {関|せき}ヶ{原|はら} (given two senses — the 1600 battle, and the everyday figurative "decisive showdown" behind {天下|てんか}{分|わ}け{目|め}の{関|せき}ヶ{原|はら}), {紫式部|むらさきしきぶ} (noting that neither half of the name is a real personal name), {松尾芭蕉|まつおばしょう}, and {日本海|にほんかい} (written around the {日本海|にほんかい}{側|がわ}/{太平洋|たいへいよう}{側|がわ} weather split rather than the geography). Two conjugation tables added (1 godan, 1 ichidan). Two new kanji given index IDs: 芭 (02799) and 蕉 (02800).

**Three stale candidates removed before writing.** The suffix candidates 系, 用, and 製 already have entries written with a leading tilde (28466 〜系, 09842 〜用, 02001 〜製), which the duplicate check does not match — logged as a `[pattern]` observation.

**§4 cross-model self-check on all 20 new entries: 3 flags, 1 applied as 2 edits, 1 rejected, 0 sent to the curator.** Eighteen entries came back clean. The applied flag was on {色柄物|いろがらもの}, whose gloss said "clothing" when the word covers towels and linens too in laundry instructions — broadened. The rejected flag objected to the register note in the gloss "veterinarian (formal term)"; 216 existing entries use that pattern, so it is house practice, not an error. Cost $0.009.

**Queue note**: 3 candidates captured from words these entries reference but do not define — {白物|しろもの}, {向|む}こう{気|き}, and {天下|てんか}{分|わ}け{目|め}. Thirteen further proposals were rejected by the duplicate gate as words that already have entries. The candidate queue stands at 140.


### 2026-08-25 (Routine v2: new-entries — 20 New Entries, IDs 30734–30753)

Created 20 general-tier entries. **Thirteen came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined — which empties that lane completely: {手繰|たぐ}る (two senses: hauling in a rope and tracing a memory back), {牛|ぎゅう}タン (the Sendai specialty, with the 定食 convention), {洋館|ようかん} (the prewar Western-style house, separated from the neutral {洋風|ようふう}の{家|いえ}), {祈念|きねん} (formal prayer, with the {記念|きねん} homophone trap spelled out), {永谷園|ながたにえん} (the food company, written so the explanation carries the metonymy — the name means the product), {池田菊苗|いけだきくなえ} (the chemist who named umami in 1908), {次点|じてん} (runner-up, including the election sense where the runner-up takes the seat), {装甲|そうこう} (armour on machines, contrasted with {鎧|よろい} on a body), {毛抜|けぬ}き (tweezers, split from ピンセット by purpose rather than shape), プルタブ (with the school pull-tab charity drive as context), {巻|ま}き{起|お}こす and {跳|は}ね{返|かえ}す (the transitive partners of 07005 and 07009, cross-linked in both directions), and テーブルタップ (cross-referenced to 07012 {電源|でんげん}タップ).

**The other seven are everyday vocabulary** from the general queue, chosen to balance a candidate list that has become proper-noun-heavy: ノルマ (quota, with its Russian etymology and its air of imposed pressure), サプリ (with the point that pills are {飲|の}む, not {食|た}べる), and five words whose difficulty is knowing when they fit — the mimetic adverbs まざまざ, ひしひし, ずけずけ, and こぢんまり (the ぢ spelling noted as the standard one), plus {時雨|しぐれ}, the early-winter passing shower that is a haiku season word. Five conjugation tables added (3 godan, 2 suru). No new kanji.

**Nine stale inline links repaired.** Creating an entry from a "seen in entry" candidate immediately strands the `⟦…：noentry⟧` marker in the entry that referred to it. A base-form-exact scan found 9 such files and pointed them at the new IDs: 04987, 05511, 06998, 07005, 07007, 07009 (two markers), 07010, 07011, 07012.

**§4 cross-model self-check on all 20 new entries: 1 flag, applied, 0 sent to the curator.** Nineteen came back clean. The flag was on 30745's last example, which translated {原材料|げんざいりょう}{費|ひ}の{上昇|じょうしょう}を{跳|は}ね{返|かえ}す as "absorb the rise in raw-material costs" — but {跳|は}ね{返|かえ}す means beating a pressure back, not bearing it, so "absorb" said the opposite in business English. Changed to "withstand". Cost $0.009.

**Queue note**: 4 candidates captured from words the new entries reference but do not define ({防弾|ぼうだん}, たこ{足|あし}{配線|はいせん}, {味|あじ}の{素|もと}, {時雨煮|しぐれに}); 9 further proposals were rejected by the duplicate gate as words that already have entries. Candidate queue now 142, below the 150-word mark, so a `candidates` restock run is no longer suppressed.

### 2026-08-22 (Routine v2: new-entries — 20 New Entries, IDs 30714–30733)

Created 20 general-tier entries. **Fifteen came from the "seen in entry" lane** — words the dictionary already used inside other entries but had never defined, which empties that lane completely: {脂漏|しろう} (the dermatology term, written so it points the learner at everyday {脂|あぶら}っぽい instead), {駅伝|えきでん} (the relay road race, with たすきをつなぐ explained as the metaphor for handing on a duty), {異人館|いじんかん} (the treaty-port Western houses, distinguished from the general {洋館|ようかん}), コンソメ (noting that Japanese usage covers the stock cube, not just the soup), {真|ま}ん{前|まえ} (the intensifying {真|ま}, contrasted with plain {前|まえ} and with {正面|しょうめん}), {名医|めいい} and {不養生|ふようじょう} (a pair from the doctor entry, the latter carrying the proverb {医者|いしゃ}の{不養生|ふようじょう}), {陣地|じんち}, {捜査官|そうさかん}, and {家宅|かたく} (the investigation family, with {家宅|かたく} marked as legal register that no one uses for an ordinary house), {小数点|しょうすうてん}, {繰|く}る (a godan verb, with the point that it shares only its dictionary form with {来|く}る), スペクタクル (narrower than English "spectacle"), {雀荘|じゃんそう}, and アンティーク (separated from {骨董品|こっとうひん}, ヴィンテージ, and レトロ).

**The other five are place names** from the vetted proper-noun queue, each written so the explanation carries the connotations rather than the coordinates: {福岡|ふくおか} (with the {天神|てんじん}/{博多|はかた} split and the food culture), {仙台|せんだい} ({杜|もり}の{都|みやこ}, Tanabata, and the せんだい homophone trap), {長崎|ながさき} ({出島|でじま} and the August 9th memorial), {熱海|あたみ} (the Showa company-trip archetype and its recent revival), and {伊勢|いせ} (お{伊勢|いせ}{参|まい}り and the twenty-year rebuilding of the shrine). One godan conjugation table added. Two new kanji given index IDs: 岡 and 崎.

**§4 cross-model self-check on all 20 entries: 1 flag, applied, 0 sent to the curator.** The reviewer objected to the `body-part` semantic tag on {脂漏|しろう}, which names a secretion rather than an anatomical part; the tag was removed. The other 19 entries came back clean. Cost $0.009.

**Curator note**: the 2026-08-20 run deliberately left {脂漏|しろう} in the queue, judging a standalone entry a poor fit for a technical dermatology term. This run wrote it anyway, on the reading that a short entry which names the register and points at the everyday alternative serves a learner who meets the word on a prescription. If that call was wrong, the entry is easy to delete.

**Queue note**: the candidate 思いつき was removed as a stale duplicate — the same word as the existing entry 27771 {思|おも}い{付|つ}き, differing only in okurigana. Four new candidates were captured from words the new entries reference but do not define: {手繰|たぐ}る, {牛|ぎゅう}タン, {洋館|ようかん}, {祈念|きねん}. Candidate queue now 149, just below the 150-word mark at which a `candidates` restock run stops being suppressed.


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
