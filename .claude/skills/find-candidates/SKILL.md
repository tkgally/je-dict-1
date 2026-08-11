---
name: find-candidates
description: Guidelines for systematically finding new candidate words to add to candidate_words.json for later dictionary entry creation.
user_invocable: true
invocations:
  - /find-candidates
---

# Finding Candidate Words for the Dictionary

Use this skill when asked to find new words to add to `candidate_words.json`
for later addition to the dictionary. It is the methodology behind
`prompts/newcandidates.md` (the Routine's `candidates` mode) and applies to
any manual candidate-discovery session as well.

## Design principle: generate from knowledge, vet every word (2026-08-11)

The queue's history teaches one hard lesson. In early 2026, ~970 candidates
were bulk-harvested from text corpora; on review, almost none were usable —
coinages that are not real words (権使, 些道), free phrases (静かに歩く),
conjugated forms filed as words (強く, 知らない), number+counter combinations
(三歳, 二百), and wrong glosses (アンパッサン glossed "ice cream sundae").
All were removed in the 2026-08-11 cleanup
(`planning/archive/candidate-cleanup-2026-08-11.json`).

The replacement workflow inverts the approach:

1. **Generate candidates from your own lexical knowledge**, aimed by
   structural gap data (semantic-field audits, scenario analysis, existing
   entries) — never by mechanical extraction from running text.
2. **Vet each word individually against the gates below** before proposing it.
3. **Add via the duplicate-checking batch tool**, so the queue only ever
   contains words that are ready to become entries.

A word that reaches the queue should need no further screening: the
`new-entries` mode trusts it.

## The vetting gates (EVERY word must pass ALL)

- **G1 — Real word.** You know this word as an established lexical item and
  could produce several natural sentences with it. If you are not certain the
  word exists with this form and meaning, DROP IT. Never propose a word you
  merely believe "should" exist.
- **G2 — Lemma form.** The citation form a dictionary would list: verbs in
  dictionary form (伝わる, not 伝わって), adjectives in plain form (悔しい,
  not 悔しく), nouns as bare nouns (自由, not 自由に). No bare inflections,
  no adverbializations, no negatives (知らない), no potential forms.
- **G3 — Headword-worthy unit.** A lexicalized item, not a free combination.
  Test: is the meaning more than the sum of its parts, or is the combination
  fixed enough that dictionaries list it (立ち読み, 花見, 食べ放題)?
  Free phrases (豪快に食べる), noun+の+noun strings (口の中),
  and number+counter combinations (三冊, 八時) fail this gate. Set phrases
  and idioms (阿吽の呼吸, 手を打つ) pass when they are established units.
- **G4 — Correct reading**, in hiragana (even for katakana headwords:
  スキー → すきー). If unsure of the reading, drop the word.
- **G5 — Correct, specific gloss.** The English note must match the word's
  actual meaning. A wrong gloss poisons entry creation months later.
- **G6 — Learner value.** An intermediate-to-advanced learner would plausibly
  encounter and benefit from it; usage is stable and current. Exclude
  ephemeral slang, vulgar or discriminatory terms, archaic/dialect items,
  and jargon so specialized that general learners never meet it.
- **G7 — Proper nouns: rich, not merely referential** (see next section).

**When in doubt, skip.** A missed word costs nothing — it can be found again.
A bad candidate costs a future session real work.

## Proper nouns (in scope as of 2026-08-11)

Proper nouns that learners of Japanese should know are now valid candidates:
place names, personal names, organization/company names, work titles, event
names, and brand names.

**Prioritize names that are collocationally and semantically rich** — names
that do lexical work beyond pointing at their referent:

- **Fixed expressions and idioms**: 関ヶ原 (天下分け目の関ヶ原 — any decisive
  showdown), 日光 (日光を見ずして結構と言うな).
- **Metonymy and connotation**: 甲子園 (the high-school baseball dream),
  永田町 (the political world), 銀座 (up-scale shopping; 〜の銀座 for any
  thriving shopping street), 築地 (sushi/fish-market associations),
  福沢諭吉 (the 10,000-yen note; 諭吉 as slang for the bill).
- **Productive patterns and derived usage**: 東大 (東大生, 東大卒 as
  shorthand for elite achievement), 山手線 (山手線ゲーム, 内回り/外回り).
- **Cultural-literacy load**: names every Japanese speaker knows from school
  and daily life — 夏目漱石, 紫式部, 源氏物語, 織田信長, NHK, 新宿.
- **Practical value for learners in Japan**: major stations, lines, and
  districts a learner navigates by (渋谷, 品川, 山手線).

**Category balance**: place names and organization names are the workhorses;
person names should lean historical/canonical (literary figures, historical
leaders) rather than current celebrities; work titles only for canonical
works constantly referenced in conversation and education; brand names only
when the name has entered everyday language (スイカ/Suica, ライン/LINE).

**Avoid**: names with only referential value (an ordinary mid-sized city with
no cultural weight), living celebrities and active politicians (prominence
fades; neutrality risks), and disputed or sensitive names.

**Mark them in the notes** so entry creation knows what it is getting:
`"Shibuya — Tokyo youth-culture hub; proper noun (place)"`. Use markers
`proper noun (place | person | organization | work | event | brand)` —
they map onto the semantic tags `place-name`, `person-name`,
`organization-name`, `work-name`, `event-name`, `brand-name` (each paired
with the `proper-noun` umbrella tag; see the entry-guidelines skill).

## Discovery lenses

Pick a few lenses per session and rotate across sessions; note in your
report which lenses you used so the next session can pick different ones.

1. **Semantic-field gaps** — `python3 build/audit_semantic_field.py --below 60
   --summary`, then generate words for thin fields from your own knowledge
   (the audit's own expected-word lists are also directly addable via
   `--add-candidates`).
2. **Scenario gaps** — `python3 build/analyze_scenarios.py --top-gaps 20`;
   words needed across many real-world scenarios are high-impact.
3. **Derivational families** — from existing entries, the common relatives
   that are missing: 経済 → 経済学/経済的; 引っ越す → 引っ越し. Only
   family members that are common words in their own right (G3).
4. **Collocates of existing entries** — words needed to use existing entries
   naturally: 電話 exists, so does 留守電? predicates like 掛け直す?
5. **Register and keigo pairs** — formal↔informal, written↔spoken
   equivalents of existing entries (もらう → 頂戴する).
6. **JLPT N2/N1 staples** — established test-prep vocabulary still missing.
7. **Katakana loanword staples** — modern life vocabulary (レシート,
   アンケート class) that earlier phases under-collected.
8. **Idioms and set phrases** — established units (目が肥える, 腑に落ちる)
   an intermediate learner meets in reading.
9. **Proper nouns** — per the section above. A healthy restock run draws
   roughly 20–40% of its words from this lens while the biggest gaps
   (famous places, canonical people/works, key organizations) remain open.
10. **Thematic sweeps** — pick an underrepresented domain (weather idioms,
    cooking techniques, office life, health symptoms) and fill it
    systematically.

## Duplicate prevention (AUTOMATIC)

**A word is a duplicate ONLY if BOTH the headword AND reading match exactly.**

- **Homophones** (same reading, different headword) are NOT duplicates:
  線香/先行 (both せんこう), 橋/箸/端 (all はし).
- **Homographs** (same headword, different reading) are NOT duplicates:
  行く (いく/ゆく), 明日 (あした/あす).

The tools check `entries_index.json` and `candidate_words.json` and refuse
exact matches automatically; homophones/homographs produce informational
notes, not blocks.

```bash
# Batch add (PREFERRED for restock runs) — each row duplicate-checked;
# duplicates are skipped and reported, never errors:
python3 build/manage_candidates.py add-batch proposed_candidates.json
# file format: [{"word": "渋谷", "reading": "しぶや",
#                "notes": "Shibuya — Tokyo youth-culture hub; proper noun (place)"}, ...]

# Single add:
python3 build/manage_candidates.py add "提案" "ていあん" "proposal, suggestion"

# Pre-check one word / batch-check several:
python3 build/manage_candidates.py check "漢字" "かんじ"
python3 build/check_duplicate.py --batch "食べる:たべる" "飲む:のむ"

# Remove a candidate you later judge unsuitable:
python3 build/manage_candidates.py remove C22950
```

**Near-duplicates need editorial judgment** (the automatic check cannot catch
them): する-verb vs noun (勉強/勉強する), kanji variants (見る/観る),
okurigana variants (行なう/行う), prefix/suffix forms (〜的). Check the
existing entry before proposing a variant.

## Notes field format

- Brief English gloss, correct and specific (G5); part-of-speech hint
  welcome; keep it under ~70 characters.
- Proper nouns: add the `proper noun (category)` marker.
- Words spotted inside existing entries keep the established marker:
  `"brief gloss; seen in entry XXXXX"` (the selector counts these).
- Readings always hiragana, never katakana.

## Reporting

After adding candidates, report:
1. Number proposed, number added, number skipped as duplicates
2. Lenses used, with rough counts per lens (including the proper-noun share)
3. Any lens that seems exhausted or especially fertile for next time
