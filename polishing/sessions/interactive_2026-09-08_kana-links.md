# Interactive session — 2026-09-08: wrong-lexeme kana inline links

**Trigger**: the curator found ⟦そうして→そうして：02943_soushite⟧ in the USAGE note of 16667
ああして ("そうして (like that, near listener)"): the link goes to the conjunction "and then", but the
word there is the て-form of そうする. He asked for a workflow that finds every such case and for
changes that stop it from recurring.

## Diagnosis

`build/auto_link.py` rule 4 links a kana token when exactly one entry has that reading and the
entry's headword is kana. "Exactly one entry" is a property of the dictionary, not of the
language: 02943 is the only そうして, so every そうして was linked to it. SudachiPy cannot separate
the two uses (it tokenizes そうして as そう + し + て in every context, conjunction included), so the
multi-token span resolved through the reading alone.

Exposed class = links whose surface and base are both pure hiragana and whose base is not in the
function-word table:

| class | links | bases |
|---|---|---|
| kanji surface (lexeme-exact by furigana + kanji) | 504,302 | — |
| function-word table (particles, する, いる, …; hand-vetted) | 434,426 | 57 |
| katakana (exact headword) | 31,506 | — |
| **kana surface, kana base** (exposed) | **35,235** | **1,309** |
| kana surface, kanji base (hand links, never written by the linker) | 7,414 | 468 |
| `noentry` markers | 4,331 | — |

## Workflow built

- `build/check_link_homophones.py` — inventory, queue, `--retier`, CI `--gate`.
- `build/review_links.py` — `--screen` (type level), occurrence review (`--ids`, `--tier`,
  `--queue`), `--ledger-from`, `--apply-decisions` (strip + re-link + prune flags).
- `build/data/kana_link_homophones.json` — tiers `unique` / `verify` / `block` per kana base.
- `reviews/link_decisions.jsonl` — `keep` / `unlink` per occurrence (context-pinned).
- `build/auto_link.py` — `homophone-guard` (block tier) and `unlinked-by-decision` (ledger).
- `build/harvest_crossrefs.py` — skips block-tier kana terms (`homophone-block`).
- CI: `.github/workflows/validate.yml` runs the gate. Routine: `prompts/routine2.md` §3, §4 step 5,
  §C ledger format; `prompts/newentries.md` post-creation `--unscreened`.

## Type screen

First attempt with gemini-2.5-pro: 65 of 66 responses unusable (reasoning consumed the 4,096-token
completion cap; arrays truncated or prose only). $1.395 spent for 7 verdicts. Fixes: `max_tokens`
parameter on `call_openrouter`, batch 10, salvage of complete objects from a truncated array,
gemini-2.5-flash as the screen model.

Second attempt (flash): 1,302 bases in 131 calls, $0.091, one parse failure (3 bases rescreened
separately). Result: 1,117 bases `unique` (24,084 links), 192 `verify` (11,151 links). Spot checks
agree with my own reading for the words that matter (そうして, ように, かける, かかる, つける, よう,
こと, ため, として flagged; ので, という, について, ばかり, など unique). Some flagged competitors are
noise (うまい "美味い vs 旨い" is one word; お → 男/尾/雄), which only costs review calls.

## Occurrence review

gemini-2.5-flash, batches of 15, the sentence (or note line) with the word marked plus the English
translation, the entry's glosses, and the screen's competitor list.

| pass | links judged | flagged (`other`/`unsure`) | cost |
|---|---|---|---|
| every occurrence of the 192 `verify` bases | 11,146 | 1,155 (10.4%) | $0.515 |
| 30-per-base sample of the 1,117 `unique` bases | 9,220 | 115 (1.2%) | $0.40 |

The unique verdicts held up (1.2% flagged, nearly all model noise such as あんな+に or ありがとう
+ ございます), so the unsampled remainder of the unique tier was not reviewed.

## Adjudication

Every flag was judged by me (rules per (word, model analysis, context) in the scratch file
`adjudicate.py`; the ledger carries one line per occurrence). Policy: a link is wrong only when the
marked word is a **different lexeme**; a sense the entry lacks is a keep plus a curator note.

| outcome | occurrences | typical case |
|---|---|---|
| keep (same word) | 647 | かかる/かける/つける senses the entry lacks (鍵がかかる, 迷惑をかける, 着ける); こと 事; な (attributive copula); べき+だ |
| unlink | 593 | 日本では (で+は) on the "well then" entry; 誰でも on the "but" entry; 〜しようとして / 〜然として on として "as"; particle のみ on 06546 "chisel"; particle なり on the classical copula; 窺う on humble 伺う; own-headword stems (かぶれ→かぶる, すくめ→すくむ, ぼやけ→ぼやく); reading fragments (しゅう【じゃ】く, きぐ【すり】) |
| retarget | 65 | なさい → 09856 なさい (was なさる); 忙しそう → 10076 そうだ (was adverb そう); いけません → 02335 いけない (was いける); 甘いもの → 02259 物 (was the sentence-final particle もの) |

Links removed or retargeted: 658 in 530 entries (the fixer then re-ran the linker on each entry
with the ledger in force, so 日本では became ⟦で⟧⟦は⟧). Dictionary total 1,010,312 → 1,010,127.
The model's "entry" verdicts are recorded as 1,294 aggregated keep lines (19,096 occurrences) plus
327 per-occurrence keeps for the block-tier words (what the CI gate checks).

Tiers after `--retier`: 1,100 unique, 185 verify, 24 block (あがる いずい うかがう ええ ざる じゃ
すく すり そうして だから っけ って では でも なり にかけて のみ のよ への ほら まり もの やけ
よし). Four bases whose errors were linker bugs rather than homophones (くっつく, つぶる, ぼやく,
さする) are locked to verify.

## Linker bugs found by the review (all fixed with tests)

1. **Own stem re-read as another verb's form.** かぶれ (in かぶれる's own examples) resolved to the
   entry itself, then the exact-form fallback matched かぶれ as the imperative of かぶる. Same for
   すくめ→すくむ, ぼやけ→ぼやく, くっつけ→くっつく, つぶれ (潰れる, kanji-headed) → つぶる. The
   fallback now runs only when the lemma had no entry at all or an irregular reading (来た).
2. **さする had a suru-verb table** (さします, さした), so 目薬をさした linked to さする; the
   generator now honours an explicit `verb-godan` tag over a する ending; table regenerated.
3. **か + な at sentence end** linked か as the question particle (22 existing cases repaired); a
   か-initial cluster of sentence-final particles that is itself an entry now links as かな.

## Candidates added

そうする (C23387), 窺う (C23388), のみ particle (C23389), なり particle (C23390).

## Curator items

`reviews/needs_curator.txt`: sense gaps in 00711 かかる, 00854 かける, 00562 つける, 02792 けち;
the さする table.

## Cost

$1.395 (failed pro screen) + $0.092 (flash screen) + $0.515 + $0.40 (occurrence review) ≈ $2.40,
recorded in `pipeline/openrouter-ledger.json`.
