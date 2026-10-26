# Candidate Restock (the Routine's `candidates` mode)

Restock `candidate_words.json`, the queue the `new-entries` mode draws from. Since 2026-10-23
the queue has two streams of its own, and every run works both:

1. **Internal closure**: words the dictionary already uses in examples or notes but has never
   defined, so that a learner who meets a word inside an entry can look it up.
2. **Brainstorming**: words that should be in a learner's dictionary and are not, found by
   thinking outward from the headwords the dictionary already has (synonyms, antonyms, words of
   the same kind, compounds and set phrases, register counterparts, culturally important proper
   names) and by asking what is missing from each semantic field. Tom asked for this on
   2026-10-23: the brainstorm on the first seeds found the particles さえ and すら, あり得る and
   ある程度 missing, and a field pass on birds found フラミンゴ, ペリカン, 七面鳥 and ダチョウ.

Since 2026-10-26 there is a third stream:

3. **ezFurigana lookups**: words that users of [ezFurigana](https://www.ezfurigana.com/), a
   site that links the words of the texts its users paste in to this dictionary's entries,
   looked up and did not find. Its owner sends Tom a report from time to time
   (`external/ezfurigana/README.md`). A report is a record of what learners met in real texts,
   so it is evidence of demand, not a word list to copy: each row is vetted like any other
   proposal, and most rows are names, fragments or forms of existing entries.

Every word comes from knowledge of Japanese (yours and other models'), **never from an existing
dictionary or word list** (Tom's rule); the ezFurigana reports are the one outside source, by
Tom's decision of 2026-10-26, and only as a pointer to words that are then vetted. Every word
is vetted one by one against the `find-candidates` gates before it is added.

Runs as `prompts/routine2.md`'s `candidates` mode when the closure and brainstorm candidates in
the queue fall below the restock threshold (200; candidates from ezFurigana reports are not
counted, so a large report never stops the other two streams), and whenever an ezFurigana
report has rows without a verdict (`params.ezfurigana_pending`). `params.approx_new` is the
target for streams 1 and 2 (40–80); about a third should come from closure while it has
depth, the rest from brainstorming. `params.openrouter_session_budget_usd` caps the model calls
(at most $0.50).

## Stream 3: ezFurigana lookups (first, when `params.ezfurigana_pending` > 0)

Work up to 150 rows a cycle, most looked-up first; the rest wait for the next cycle.

```bash
python3 build/ezfurigana_lookups.py pending --n 150 > /tmp/ez.json
```

Each row has the user's `surface` and `reading`, ezFurigana's `category`, the `existing`
spelling it found, the `lookups` count, and the entries sharing its surface (`same_surface`) or
reading (`same_reading`). Give every row one verdict:

- **variant**: another spelling or reading of an existing entry (身体 for 体, 何処 for どこ,
  明日 read あす). Most "another kanji spelling" and "kana form only" rows are this, but check:
  a kana-only match can be a different word (宋 is not そう; 生(せい) "life" is not せい
  "fault"), and "another reading" rows are often real homographs (生物 なまもの, 人気 ひとけ,
  下 もと, 工場 こうば), which are candidates.
- **exists**: an inflected form, stem or fragment of an existing entry (与え → 与える, 細か →
  細かい, おいて → において), or a pattern an entry covers (ませんか → ます).
- **added**: passes G1–G7. Queue the lemma, not the surface: 入管法 → 入管, にわたって →
  にわたる, 致し方 → 致し方ない; a productive affix as an affix entry (〜沿い, 〜切れ).
  Grammar rows (には, ずに, ことになる, かねない) are welcome: the dictionary has entries for
  patterns like ことにする and はずだ.
- **rejected**: with the reason: personal names and places of little weight (G7), bare
  single-kanji fragments, transparent compounds (研究費, 開始日), number + counter strings,
  vulgar or specialized words, slang.

Candidate notes end with the marker `ezfurigana: looked up N×` (and `as <surface>` when the
lemma differs), which `new-entries` and the selector read:
`{"word": "幽閉", "reading": "ゆうへい", "notes": "confinement, imprisonment; ezfurigana: looked up 6×"}`.
Add the survivors with `manage_candidates.py add-batch`, then record every verdict, added or not:

```bash
python3 build/ezfurigana_lookups.py record /tmp/ez_verdicts.json
```

`/tmp/ez_verdicts.json` is `[{"surface", "reading", "verdict", "reason", "entry_id"?, "word"?, "word_reading"?}]`
(`entry_id` for exists and variant). A row the add-batch skipped as a duplicate is `queued`.
Words the report suggests by association (宋 → the other dynasties 唐, 明, 清) are stream-2
brainstorm candidates, with a `brainstorm:` note.

## Stream 1: internal closure (about a third of the target)

1. **Words marked as missing inside entries.**
   ```bash
   python3 build/check_stale_noentry.py --json > /tmp/stale.json
   ```
   Take the `unresolved` class, ranked by `instances`. Skip suffixes and prefixes standing alone
   (権, 化, 系), number-plus-counter strings (三冊), inflected or partial forms, proper nouns of no
   cultural weight, and variant spellings of existing entries.
2. **Words the reviewer or a polish run noticed**: `[entry]` lines in
   `polishing/observations.md` and recent session logs.
3. **Unlinked words in example text**: words in examples that the linker left bare because no
   entry exists (most hits are other spellings of existing entries; skip those).

Notes for this stream say `seen in entry NNNNN`.

## Stream 2: brainstorming (the rest)

The tool serves one batch per run and alternates two lenses: **seeds** (the next 20 headwords
in tier order, basic first) and **field** (one semantic field with the words the dictionary
already has in it, proper-name fields included).

```bash
python3 build/brainstorm_candidates.py next > /tmp/bs_batch.json
```

1. **Your own brainstorm first**, before reading any model's list (so you are not anchored).
   For a seeds batch, for each headword think of: synonyms and near-synonyms; antonyms and
   opposites; other members of the same category; broader and narrower words; established
   compounds, set phrases and idioms built on it; formal, casual, honorific and humble
   counterparts; culturally important proper names closely tied to it (places, people, works,
   events, organizations with cultural weight; see the find-candidates skill). For a field
   batch, read the member list and name the common words a learner would miss first. Write
   them to `/tmp/bs_own.json` as
   `[{"word": "…", "reading": "…", "gloss": "…", "relation": "antonym", "seed_id": "00006_aru", "by": "self"}]`.
2. **Independent models** (skip if the budget is under $0.05):
   ```bash
   python3 build/brainstorm_candidates.py ask /tmp/bs_batch.json --out /tmp/bs_models.json --budget <params.openrouter_session_budget_usd>
   ```
   It asks `openai/gpt-6.1-sol` and `google/gemini-3.8-flash` the same question, prints
   `EST_COST=` (billed, about $0.05–0.10 a batch) and records the spend in
   `pipeline/openrouter-ledger.json` itself (mode `candidates`).
3. **Merge and filter**:
   ```bash
   python3 build/brainstorm_candidates.py filter /tmp/bs_own.json /tmp/bs_models.json --out /tmp/bs_new.json
   ```
   It drops entries, candidates, retired IDs and anything an earlier run rejected, and prints
   counts. In what remains, `by` lists who proposed it (agreement ranks first),
   `possible_variant_of` names an existing entry with the same reading that may be the same
   word in another spelling (usually drop it: 出掛ける when 出かける exists), and `alt_spellings`
   groups proposals that are one word in several spellings (keep one: the spelling the word is
   usually written in, katakana for most birds and animals, ダチョウ not 駝鳥).
4. **Vet each survivor** against gates G1–G7 of the `find-candidates` skill. Models propose
   rare or bookish words, words that do not exist in that form, and free phrases; when in doubt,
   leave it out. Usefulness 1 words need a reason to stay.

Notes for this stream name the lens and the link to an existing entry, so `new-entries` can
cross-reference them: `brainstorm: antonym of 00204 数`, `brainstorm: same category as 00001 鳥`,
`brainstorm: field animal-bird`. Proper nouns keep the `proper noun (place | person | …)` marker.

## Workflow

1. Load the `find-candidates` skill (gates G1–G7).
2. Work stream 3 first if `params.ezfurigana_pending` > 0 (it has its own count, outside the
   target). Then run streams 1 and 2 to a proposal list of about 1.5× the target.
3. **Probe first, then vet.** For stream 1 (stream 2's filter already did this):
   ```bash
   python3 build/check_duplicate.py --batch --skip-candidates 'word:reading' 'word:reading' …
   ```
4. Vet each survivor: real, lemma-form, headword-worthy, correct hiragana reading, correct
   gloss, learner value.
5. Write the survivors to a scratch JSON file outside the repo:
   ```json
   [{"word": "湯呑", "reading": "ゆのみ", "notes": "teacup (handleless); seen in entry 05612"},
    {"word": "数少ない", "reading": "かずすくない", "notes": "few, scarce; brainstorm: compound of 00204 数"}]
   ```
6. Batch-add with automatic duplicate checking:
   ```bash
   python3 build/manage_candidates.py add-batch <scratch-file>.json
   ```
7. **Record the brainstorm verdicts** (every stream-2 proposal you vetted, added or rejected),
   which also advances the lens cursor:
   ```bash
   python3 build/brainstorm_candidates.py record /tmp/bs_batch.json /tmp/bs_verdicts.json
   ```
   `/tmp/bs_verdicts.json` is `[{"word": "…", "reading": "…", "verdict": "added" | "rejected", "reason": "…"}]`.
   Rejected words are not proposed to you again. Proposals dropped as existing entries need no
   verdict.
8. Re-read `git diff candidate_words.json` once and remove any slip
   (`manage_candidates.py remove C12345`). One pass, no ping-pong.
9. Wrap up per routine2.md §5–§7 (update PROJECT_STATUS.md Recent Changes, `make index`,
   commit, push, PR, merge).

## Quality bar

- Real, stable, lemma-form headwords with correct readings and glosses; useful to intermediate
  learners; general tier.
- Not: bulk-extracted lists, uncertain words, conjugated or derived forms, free phrases,
  number+counter strings, ephemeral slang, vulgar or discriminatory terms, archaic or dialect
  items, hyper-specialized jargon (most bird species beyond the familiar ones; most technical
  terms of a field).

## Report

At the end: proposed / added / rejected, per stream; for stream 2 the lens and batch (seeds
and their range, or the field), how many proposals each source made and how many survived;
for stream 3 the rows worked and the verdict counts (`ezfurigana_lookups.py stats`) and how
many rows still wait; queue total.
