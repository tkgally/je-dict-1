# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-09-11
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

### 2026-09-11 (Routine v3: new-entries — 20 New Entries, IDs 30853–30872)

Created 20 general-tier entries, all from the "seen in entry" internal-closure lane, which emptied
it to 41 remaining candidates. A roofing cluster harvested from 03902 {瓦|かわら}: {鬼瓦|おにがわら},
{平瓦|ひらがわら}, {丸瓦|まるがわら}, and the verb pair {葺|ふ}く/{葺|ふ}き{替|か}える (two
conjugation tables added). A shark trio from 04316 {鮫|さめ}: ホホジロザメ, ジンベエザメ,
シュモクザメ. Two crocodilian loanwords contrasted against 04308 {鰐|わに}: クロコダイル,
アリゲーター. Everyday items: テント{泊|はく}, {補聴器|ほちょうき}, {蝙蝠傘|こうもりがさ},
{羽織袴|はおりはかま}, {吸盤|きゅうばん}, アイビー, モバイル, デフォルト. Two idioms:
{前途洋洋|ぜんとようよう} and {不動心|ふどうしん}.

**One candidate dropped as a spelling-variant duplicate.** {蔓|つる} (vine, tendril) turned out to
be the same word as the existing kana-headed entry 27394 つる, whose own explanation already notes
"sometimes written {蔓|つる} in kanji" — removed from the queue rather than written up, per the
duplicate-variant policy.

**18 stale `noentry` markers resolved** across 11 entries once the new words existed to fill them:
03859 テント (テント{泊|はく}), 03902 {瓦|かわら} (all five roofing words), 04308 {鰐|わに}
(both loanwords), 04323 {蛸|たこ} and 04968 {蔦|つた} (both {吸盤|きゅうばん}), 04354 {蝙蝠|こうもり}
({蝙蝠傘|こうもりがさ}), 04872 ブラウザ and 04874 アプリケーション and 05627 {端末|たんまつ}
(all モバイル), 05034 {聴力|ちょうりょく} ({補聴器|ほちょうき}), 05712 {羽織|はおり}
({羽織袴|はおりはかま}). Cross-reference harvest also added reciprocal links into 02264 {屋根|やね},
04316 {鮫|さめ}, 15380 {和傘|わがさ}, 17612 {日帰|ひがえ}り, 21200 {平常心|へいじょうしん}, and
03781 {冷静|れいせい}.

**§4 cross-model self-check on all 37 changed entries (20 new plus 17 neighbors touched by the
noentry and cross-reference passes): 0 flags on the new entries.** Two flags landed on pre-existing
neighbor entries and were both rejected as reviewer noise: 04316 {鮫|さめ}'s note already correctly
caveats that sword-wrap {鮫|さめ}{皮|がわ} is usually ray skin, not shark skin, so the "factual
inaccuracy" the model saw was already handled; 04968 {蔦|つた}'s generic top-level gloss "ivy" is
deliberate (the notes and RELATED WORDS already specify Boston ivy and distinguish it from the new
アイビー entry). In-context kana-link check: 0 flags. Cost $0.019 total. One unscreened kana word
found along the way, おめでとうございます, screened as `unique` (no cost).

**Queue**: 20 candidates auto-cleared on `update_indexes.py`; one removed by hand as a duplicate.
Candidate queue stands at 196, with 21 internal-closure candidates left for the next new-entries run.

### 2026-09-09 (Interactive: seven new articles, inline links in all ten articles, 39 entries for words they use)

Tom asked for seven new articles for the site's Articles page, a consistency review of all ten, inline links to entries for every Japanese word the articles use, and entries for the words that had none. The seven new articles: **The Te-Form Helper Verbs** (ている, てある, ておく, てしまう, てみる, ていく, てくる — the "aspect article" the planning wiki had ranked as the top gap), **Transitive and Intransitive Verb Pairs**, **Giving and Receiving** (あげる・くれる・もらう), **Body-Part Idioms** (about seventy idioms from 頭 to 骨), **Katakana Loanwords and Wasei-eigo**, **Greetings and Set Phrases for Everyday Life**, and **Referring to People** (pronouns, name suffixes, titles, family terms). Each runs about 900–1,200 words, ends with tips, and cross-links the articles that touch the same ground.

**Articles now carry inline links.** The article renderer could not render `⟦…⟧` links before, and its table parser split cells on the `|` inside furigana, so the keigo article's verb table had been rendering as fragments on the live site; both are fixed, with unit tests. A new `build/link_articles.py` runs the deterministic linker over article bodies with the same rules and homophone guards as entries, and `build/validate_articles.py` (now a CI step) checks schema, furigana, link targets, and related entries. The ten articles hold about 1,400 links, of which 211 were placed by hand where the linker is deliberately silent — あげる (four entries share the reading), set phrases the tokenizer splits (こちらこそ, はじめまして), and the bare helper forms 〜ている/〜ておく that an article about them must link.

**39 new entries (30814–30852)** for words the articles use that had no entry: the helper verbs ていく, てくる, てる, とく and the term 補助動詞; fifteen idioms (頭が上がらない, 目がない, 口に合う, 歯が立たない, 首になる, 首を長くする, 肩を持つ, 肩の荷が下りる, 胸がいっぱい, 腹を立てる, 手に入れる, 手がかかる, 足を洗う, 喉から手が出る, 骨が折れる); the false friends スマート and ナイーブ and the coinages ペーパードライバー, キーホルダー, スキンシップ, マイペース; ご両親, 息子さん, 娘さん; 音便; and nine greeting formulas (おはようございます, ごちそうさまでした, ありがとうございました, おめでとうございます, お世話になりました, こちらこそ, お疲れ様でした, 明けましておめでとうございます, 良いお年を). The independent-model check of the 39 entries found one issue, and the link check two, all adjudicated; a stale link in 04467 that the new ありがとうございました entry made resolvable was retargeted.

**Pilot articles revised**: the counters article's counting lists now use kanji with furigana ({一本|いっぽん}) instead of bare kana, so they link and render readings; the keigo article's "double honorific" example was replaced (お召し上がりになる is an established exception, not the error it was presented as); the onomatopoeia article's spellings were matched to the entries. A pre-existing duplicate surfaced on the way: 01993 and 02446 are both the core-tier counter 〜軒, differing only in the tilde character — flagged for Tom.

### 2026-09-08 (Interactive: wrong-lexeme kana inline links — workflow, guards, and a dictionary-wide sweep)

Tom found そうして in the こそあど note of ああして (16667) linked to 02943 そうして "and then", where it is
the て-form of そうする. The deterministic linker links a kana word to the one entry that has its
reading, and "one entry" is a fact about the dictionary, not the language. The exposed class is
links whose surface and base are both kana and not a function-table word: 35,235 of the 1,010,312
links, over 1,309 kana words (kanji, katakana, and particle links are not affected).

**Workflow added.** `build/check_link_homophones.py` inventories the class against a curated tier
list (`build/data/kana_link_homophones.json`: `unique` / `verify` / `block`) and is a CI gate;
`build/review_links.py` screens each kana word for same-kana competitors with a model, reviews
occurrences in context, and applies adjudicated decisions from the new ledger
`reviews/link_decisions.jsonl`. The linker never links a `block` word from kana and never re-links
a word a decision removed from an entry; the cross-reference harvester applies the same block list.
The Routine's self-check now runs the in-context link check on every changed entry.

**Sweep.** 1,305 kana words screened ($0.09 with gemini-2.5-flash; a first attempt with
gemini-2.5-pro lost 65 of 66 responses to its reasoning budget, $1.40 wasted), 20,366 links judged
in context ($0.92), 1,270 flags adjudicated by hand: 647 kept (same word, often a sense the entry
lacks), 593 unlinked, 65 retargeted; 658 links repaired in 530 entries. Tiers: 1,100 unique, 185
verify, 24 block. The review also exposed three linker bugs (a verb stem re-read as another verb's
imperative inside its own entry; さする carrying a suru-verb table; か+な split at sentence end),
all fixed with tests, and four sense gaps for the curator (かかる, かける, つける, けち).
Candidates: そうする, 窺う, particle のみ, particle なり.

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


