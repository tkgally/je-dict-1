# Cleanup Backlog

**Last updated**: 2026-07-02 (wiki harvest of 2026-07-01/02 loose observations: **P11** — in-list-but-wrong-category tag drift persists into the 11500s general-tier cohort [11573–11646 accuracy-review, 5/14 genuine ≈36%: abstract/loanword nouns on oddly-specific in-list domains — トレード/作画→`leisure`, 入浴→`consumption`; invisible to P20/`concrete-noun-domain-mismatch`; recommends a targeted katakana/suru-noun `tags` sweep]. Prior 2026-07-01 (wiki harvest of 2026-07-01 loose observations: **P20** — the off-vocab tag cohort reaches the **11515–11553 band** [a granular hyphenated tag set — `action-*`/`religion-*`/`quality-*`/`person-occupation`/… — from a ~Feb-2026 claude-opus-4-6 batch; 26/72 entries, migrated 1:1; recommend a 11500–12500 `--check-no-new-unknown` sweep]; **P11** — the wrong-category drift reaches **function words** [06355 どうせ, an adverb, tagged `furniture` + a contradictory `formal`; cleaner deterministic signal than the noun cases — a physical-object tag on an adverb/particle POS — filed as a new `check_tag_drift` check via Tooling item 6]). Prior 2026-06-30 (wiki harvest of 2026-06-29/30 runs: **P20** — the off-vocab tag cohort reaches the **11300s 不-/中-/下-/両- compound band** [1:1-mappable families quality→descriptive, position-direction→direction, people→person, place→geography; 2026-06-30 accuracy-review migrated 24/35 — recommend folding into `check_tag_drift.py`'s map for a deterministic sweep]; **P21** — the zero-inline-link create-era band reaches the **06338–06343** four-char-idiom/compound-verb cohort [band now unbroken ~06150→06343; gap concentrated in this mid-ID 2026-01-17 batch — recommend a ~06338–06500 sweep]. Prior 2026-06-28 (second wiki harvest, of 2026-06-28 runs): **P20** — the free-form tag cohort reaches the **10700–11000 katakana/slang/loanword band** [10716–10887 45/67 flags off-vocab; a dense 10905–10934 pocket from a 2026-02 claude-opus-4-6 batch; cohort now contiguous through ~10947 — recommend one scoped `check_tag_drift` sweep over 10700–11000]; **P13** — the placeholder-`general`/`science` signature continues at the **06309–06340 frontier** [astronomy/stepladder concrete nouns, curator-bulk-migration territory]. Prior harvest of 2026-06-27 routine runs: **P20** — the free-form tag cohort reaches the **10400–10700 band** [~50/100 invalid in 10450–10549; reviewer migrated 64 but *missed* ~9 in 10550–10715 → deterministic sweep still needed in nominally-reviewed ranges]; **P21** — zero-link create-era band reaches the heavy **06294–06308** cultural/medical/finance cohort [15–50 lookups/entry, much `noentry`]; **P17** — third sub-family, **verb-suru** entries carrying a template-default `formal` [06307 仲直りする contradicts its own notes]; **P13** — the under-specified `general`/`work` on the 06298–06303 medical/finance batch is itself a create-era batch signature [4/5 applied as clearly-correct single-domain]. Prior 2026-06-26 (harvest): P20 updates — daily-life/errands cohort continues into 9741–9814 [20% invalid] + a new shopping/tech cohort at 9815–9849 [60% invalid, migrated]; **enforce-side shipped** [off-vocab ratchet `--check-no-new-unknown` + baseline, now a CI step — gates new drift, legacy tail still gradual]. P21 update — the zero-inline-link band reaches the 06271–06281 mimetic/idiom/拝〜-keigo cohort [recommend a ~06275–06600 inline-link sweep]. Prior 2026-06-25: P20 update — denser daily-life/errands sub-batch at ~9657–9740 [48/84 = 57% invalid tags, migrated; recommend a confirming 9600–9800 `check_tag_drift` sweep]. Prior 2026-06-24: P20 free-form cohort into 9240–9456 [56%, ~86 residual]; **new Priority 22** — inconsistent free-text `part_of_speech` display field; 2026-06-23: P21 band through 06246; P20 8,698 dict-wide flags, 8633–9239 long tail has no 1:1 map; P9 06231 kana-inside-group + nested braces)

Concrete cleanup work items surfaced during comprehensive-polish sessions. Each item describes a systemic pattern that affects multiple entries and could be addressed by a dedicated batch pass.

**As of 2026-06-09**, the batch-addressable items here are also indexed in machine-readable form at [`backlog-queue.json`](backlog-queue.json), which the unified Routine's `systemic-fix` mode (`prompts/routine2.md` §B) drains one bounded, per-entry-verified batch at a time. Read-only detectors back the queue: `build/check_furigana_format.py` (P9, P12), `build/check_artifacts.py` (P16, P15, P10, P4, P2), and `build/check_tag_drift.py` (P6, P7, P13, P20; plus the two high-precision P11 checks `proverb-idiom-mismatch` and `concrete-noun-domain-mismatch` shipped 2026-06-17, with `semantic-mismatch` kept experimental). Keep `backlog-queue.json` in sync with this page during wiki maintenance.

## Priority 1: Unlinked notes in older entries

**Source**: Comprehensive-polish sessions 2026-05-08 through 2026-05-09 (entries 00006–00096)
**Scope**: Virtually every entry in the January–February 2026 creation cohort

Older noun entries have linked example sentences but **unlinked notes**. Structured lists in `notes` (Common Collocations, Related Words, Types of X, Compounds, Similar Words) use bare `{kanji|reading}` without `⟦...⟧` wrappers. This is confirmed as the single most common tier-1 polish deficit for entries below ~00100, and likely extends through most pre-March 2026 entries.

The inline-links polishing task (`polishing/tasks/inline-links/progress.txt`) at entry 02730 is the primary mechanism addressing this, but comprehensive-polish sessions are also fixing entries as they encounter them starting from entry 00001.

As of comprehensive-polish session 2026-05-18 (entries 02101–02125), **particle links** (は, が, を, に, で, と in pattern examples) are now the primary remaining inline-link gap in the entry range being polished. This is a sub-case of the unlinked-notes problem: structured pattern sections use bare particles without `⟦...⟧` wrappers.

## Priority 2: Missing or broken cross-references

**Source**: Comprehensive-polish sessions 2026-05-08 through 2026-05-09

Two related sub-issues:

1. **Under-populated cross_references**: Entries mention obvious neighbors in notes but have no `cross_references` entries for them. Examples: 00010_banchi → 住所/丁目/号; 00014_biyou → 美容院/美容師/健康; 00018_booto → 船/ヨット/カヌー.

2. **Structurally invalid cross_references**: Some entries have cross-reference objects with `headword`/`reading` but no `target_id` field (e.g., 00041_fudan → 通常, 00065_genni → 実際に, 00069_gesui → 上水). `validate.py` emits a "Note" rather than an error for these, so they persist silently.

3. **Missing field entirely**: 09491_choume was missing the `cross_references` field altogether, not just having it empty. The symmetry checker may silently skip such entries.

**Suggested actions**:
- One-shot scanner listing every cross_references entry without `target_id`
- Consider `validate.py --strict` mode promoting "missing target_id" notes to errors
- Confirm `check_consistency.py` flags entries lacking the `cross_references` field

**Update 2026-06-17 (systemic-fix run)**: `build/check_artifacts.py --issue missing-target-id` now exists as the scanner (190 dangling refs across 180 entries at run start). This run filled `target_id` on the 54 refs whose **headword AND reading both** uniquely match an existing entry — the provably-correct subset where a real link had simply lost its id (antonym pairs like 12053_jigoku→天国, transitivity pairs like 00001_amaru→27283_amasu, same-kanji homophone triplets like 20859_atsui→厚い/暑い/熱い). Detector down to 136. **Caution learned this run**: a `by_reading` fallback is unsafe (homophone confusions: 有限/ゆうげん matched 幽玄, 小学/しょうがく matched 少額) — only fill `target_id` on exact headword+reading matches. The remaining 136 are "headword has no entry" cases; some are *deliberate* homophone/contrast pointers (e.g. 00250_kufuu → 工夫/こうふ "laborer (homophone)") that should be kept, not dropped. A future run must verify each before dropping.

**Update 2026-06-19 (systemic-fix run)**: detector 136 → 96. Resolved 40 refs across 37 entries: (a) **22 vestigial `id` → `target_id`** — 26 of the 136 refs carried a non-schema `id` field that the renderer ignores (it reads `target_id` only); promoted the 22 whose `id` pointed to a live entry; (b) **4 stale-`id` repoints** — pre-renumber ids 01040_shinjin/02032_tenkin/00373_ondo/00213_gaikokujin → 02500_shinjin/04555_tenkin/00333_ondo/02869_gaikokujin (resolved by exact headword+reading); (c) **14 reading/surface-verified additions** — reciprocal kana antonym pairs (24277↔24278 夏鳥/冬鳥, 26648↔26649 薄/濃灰色, 26896↔26897 水/海域, 25791↔25792 最高/最低点) and same-word kanji variants (03409 堪えられない→27249 耐えられない, 07148 満ち潮→28112 満潮, 10540 交じる→02421 混じる). All 37 self-checked via the furigana screener — clean (6 flags, all partial-reading/misparse false positives, rejected). **The remaining 96 are mostly legitimate target-less refs**: the referenced word has no entry, and many are *intentional* homophone/contrast/antonym display labels (00250 工夫/こうふ, 17797 侯爵, 00296 有限) that must be **kept, not dropped**. Captured 14 entry-worthy referenced words as candidates (有限, 低温, 高地, 父性, 答申, 近刊, 避寒, 能動, 好天, 独創, 大食, 実名, 車外, 小学). **Two tooling follow-ups** (see observations 2026-06-19): the detector should exclude `type=homophone`/`contrast` (or labeled) refs whose reading has no entry so the queue converges; and the build-time by-reading fallback should require a headword-surface match (it would mis-resolve 04026's `〜着` arrival sense to the clothing counter 27655_chaku).

**Update 2026-06-20 (systemic-fix run)**: detector 96 → 82. **The 2026-06-19 → 2026-06-20 loop closed**: 13 of last run's captured candidates (有限/小学/独創/実名/能動/低温/高地/父性/好天/近刊/避寒/大食/答申) were created by the curator as entries **29338–29351**, so this run filled their `target_id` by provably-correct exact headword+reading match (00296→29338_yuugen, 03477→29351_shougaku, 06242→29347_dokusou, 11797→29349_jitsumei, 12070→29345_noudou, 14705→29339_teion, 15551→29340_kouchi, 15688→29341_fusei, 16184→29346_kouten, 16466→29343_kinkan, 16476→29344_hikan, 16900→29348_taishoku, 17729→29342_toushin). Each target read and semantically confirmed (all antonym/related pairs). Self-checked all 13 via the furigana screener — clean (2 false-positive flags rejected: model misread どくそうてき; 毎年=まいとし is a valid reading). Captured 4 more entry-worthy referenced antonyms as candidates (悪徳/急減/軟質/一神教). **The remaining 82 are overwhelmingly intentional target-less pointers** — the referenced word has no entry and the ref is a homophone/contrast/antonym display label that must be kept. The detector now mostly re-surfaces these permanent pointers each run; the tooling follow-up above (exclude `type=homophone`/`contrast`/labeled refs with no-entry reading) is the way to make this queue actually converge rather than hover near 80.

**Update 2026-06-21 (systemic-fix run) — RESOLVED.** detector 82 → 0 (default). Two things this run: (1) **Filled the last 5 resolvable refs** — another curator restock created 29368–29383, so 06214→29383_nekonikoban (猫に小判, synonym proverb), 12651→29371_isshinkyou (一神教), 12671→29369_kyuugen (急減), 13899→29368_akutoku (悪徳), 16910→29370_nanshitsu (軟質), all exact headword+reading matches, each target read and semantically confirmed (antonym/synonym pairs). Self-checked the 5 via the furigana screener — clean (1 false positive rejected: model claimed 大切→たいせ, but the furigana is correctly たいせつ). (2) **Implemented the convergence follow-up**: `check_artifacts.py --issue missing-target-id` now flags **only refs whose referenced word actually has an entry** (resolvable = some entry shares the ref's reading *and* furigana-stripped surface). Intentional target-less pointers — homophone notes, antonym/contrast display labels, transitivity-pair pointers to words with no entry — are no longer re-surfaced every run. `--include-intentional` restores the full audit list (77 such pointers as of this run). With 0 resolvable refs remaining dictionary-wide and the detector converged, **this item is closed**; it will only re-open if a future ref's referenced word gains an entry (the detector will catch it automatically). Captured 10 more entry-worthy referenced words as candidates (妊娠する, 創造する, 肯定する, 推薦する, 企画する, 罷免, 悪者, 対義語, 鎮める, 取り付く).

## Priority 3: Cross-reference symmetry on thematic clusters

**Source**: Comprehensive-polish 2026-05-09 session 002

Back-link symmetry on thematic clusters (school types, family terms, time expressions, ceremony types) is poor. Example: 00055_gakkou ↔ 01055_shougakkou/01083_koukou had no back-links until manually fixed.

**Suggested action**: High-leverage one-shot batch — pick a cluster, ensure every member references its main parent term. `check_semantic_clusters.py` partially addresses this but focuses on transitivity/antonym/keigo clusters rather than thematic groupings.

## Priority 4: Duplicate conjugation keys in verb JSON

**Source**: Comprehensive-polish 2026-05-08 session 001

Many verb entries have two `"conjugation":` top-level keys: a legacy stub (e.g., `{"type":"godan","ending":"る","stem":"…"}`) plus the full conjugation table appended later by `add_conjugations.py`. JSON parsers silently take the last value, so runtime behavior is correct, but the dead stub wastes space and is confusing. Confirmed on 00001_amaru, 00002_amu, 00004_aogu, 07924_aoru; not present on 00006_aru. Likely affects most verb entries predating the conjugation-table retrofit.

**Suggested action**: See tooling-backlog for the pruning script proposal.

**Update 2026-05-21/22**: Comprehensive-polish sessions 2026-05-21 (entries 02559–02583 and 02670–02696) confirmed the duplicate-conjugation-key pattern extends well beyond the originally identified entries. Entries 02560, 02567, 02568, 02574, 02576, 02582, 02688, 02693, 02696 all had the old-format (`prefix`/`stem`/`ending`) stub followed by the correct `forms`-array block. The pattern is likely pervasive across all pre-retrofit verb entries. Reinforces the case for the batch pruner in [Tooling Backlog](tooling-backlog.md) → item 1.

**Update 2026-05-23**: Session 005 (entries 03056–03077) found the same pattern in entries 03057, 03064, 03072, 03077 — an incomplete object `{type, prefix}` or `{type, ending, stem}` appearing before the full forms array. Python's `json.load` silently uses the last occurrence, so runtime behavior is correct, but the dead first object is malformed (duplicate keys). Continues to confirm the pattern is pervasive across the entire pre-retrofit entry range.

**Update 2026-05-25**: Session 011 (entries 03211–03230) found the same pattern in 5 suru-verb entries (03214, 03216, 03218, 03220, 03222) — a lightweight conjugation stub (type+prefix format) placed before `definitions` alongside a full conjugation table at the end. The stubs were removed during polishing. Reinforces the pervasive pre-retrofit scope.

**Related sub-pattern (notes-level duplication)**: Comprehensive-polish session 033 (entries 05540–05559) found entries 05542, 05543, 05544, 05546 with redundant CONJUGATION prose sections in their `notes` field even though the entry already had a proper `conjugation` JSON field with all forms. The notes-only CONJUGATION block is a batch artifact from a period when conjugation data lived in notes rather than in a structured field. These are distinct from the duplicate-JSON-key pattern above — the notes text is well-formed but redundant once the structured conjugation field exists. Comprehensive-polish removes them case-by-case, but a one-shot scan for `CONJUGATION` headers in notes of entries that also have a `conjugation` field would catch all remaining instances.

**Update 2026-06-10 (compound-verb range)**: Routine v2 polish session found the same notes-level conjugation duplication in three 06xxx godan compound verbs — 06852_hourikomu (放り込む), 06858_ukabiagaru (浮かび上がる), 06735_sashikakaru (差し掛かる) — each of whose notes opened with a redundant negative / te-form / past bullet list duplicating the structured `conjugation` table. Removed in session; the 06xxx compound-verb cohort likely holds more. **Detector gap**: `build/check_artifacts.py --issue dup-conjugation` targets the *duplicate-JSON-key* form (P4 above) and currently returns 0 — it does **not** detect this *notes-prose* duplication. So this sub-pattern is not yet covered by any read-only detector; either extend `check_artifacts.py` with a `notes-conjugation-prose` check (CONJUGATION header **or** a leading negative/te/past bullet list in `notes` of an entry that already has a `conjugation` field) or keep handling it case-by-case in comprehensive-polish. The former would make it backlog-queue-eligible for a systemic-fix batch.

## Priority 5: Particle entry polish

**Source**: Comprehensive-polish 2026-05-09 sessions 002 and 003

Particle entries with extensive structured fields (e.g., 00051_ga and 00079_ha with `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`, `information_structure`) contain dozens of small Japanese phrase fragments that lack inline link coverage. These are not addressable by ordinary tier-1 polishing — they need a dedicated particle-polish session.

**Affected entries**: At minimum 00051 (が), 00079 (は), and likely 00422 (を), 00314 (に), 00502 (で), 00504 (と), 00512 (から).

## Priority 6: Spurious conjugation tables on non-verb entries

**RESOLVED (2026-06-08).** The one-time non-verb conjugation sweep cleaned **133 entries** (101 non-expression non-verbs — adverbs, onomatopoeia, noun-adverbs, na-adjectives, nouns, auxiliaries — plus 32 reviewed `expression` entries), removing both the `conjugation` field and the stray `verb_class` tag from each. (133 vs. the 130 estimated here: the audit detector counted only entries with a `conjugation` field, whereas the pruner also catches a few that had a stray `verb_class` tag but no table, e.g. 04214_jisseki; one of the original twelve onomatopoeia, 05646_gyuugyuu, had already been cleaned on 2026-06-07.) The reusable pruner `build/prune_nonverb_conjugations.py` was built and committed, and a **defensive exact-enum verb-POS guard** was added to `add_conjugations.py` — the previous guard used the substring test `'verb' in p`, which is true for `"adverb"` and let adverbs with a stray `verb_class` tag generate godan nonsense. The detector one-liner below now returns **0**; re-running both retrofits re-adds nothing. The 31→32 expression cases were all confirmed as multi-word idioms, proverbs, adverbial phrases, or compound-ている forms (not single mis-tagged verbs); the one borderline keigo case (お会いする, 22190) was stripped and logged for a curator second look in [Entry Follow-ups](entry-followups.md).

**Standing-check re-confirmation (2026-06-24):** the systemic-fix selector surfaced this item again; `check_tag_drift.py --check conjugation-no-verb-pos --json` returned `[]` (0 dictionary-wide), so the `add_conjugations.py` exact-enum verb-POS guard is still holding against regeneration. The backlog-queue.json status was flipped `open`→`resolved` (matching the `tag-politeness-unsupported` guarded-standing-check precedent) so the selector advances to the next actionable item instead of re-picking a clean scope-0 check; the read-only detector stays indexed as a standing guard.

**Source**: Wiki maintenance 2026-05-11 (initial 12-entry onomatopoeia case) + 2026-05-12 (widened audit)

The 2026-05-11 session identified 12 adverbial onomatopoeia entries (ぐつぐつ → ぐつぐたない etc.) carrying full godan conjugation blocks with nonsense forms. The 2026-05-12 follow-up audit shows this was a partial finding: **130 entries currently have a conjugation field while their POS tag contains no `verb-*` or `adjective-i` value**. All 130 carry a stray `verb_class` tag that triggered `add_conjugations.py`.

**Breakdown by primary POS:**

| Primary POS | Count | Example | Generated nonsense |
|-------------|------:|---------|--------------------|
| adverb (non-onomatopoeia) | 79 | 著しく, すごく, おそらく, ますます, あいにく | `著しきます`, `すごかない` |
| adverb + onomatopoeia | 12 | ぐつぐつ, こつこつ, ぱくぱく | `ぐつぐたない` |
| expression | 31 | 反応を見る, 手を打つ, 場を和ませる | `反応を見らない` (mis-classifies 見る as godan) |
| noun + adverb | 5 | 真っ二つ, 多く, 遠く | varies |
| auxiliary | 2 | ～続ける | godan-ku forms |
| na-adj + adverb | 1 | べらぼう | godan forms |
| **Total** | **130** | | |

The original 12-onomatopoeia list is a subset. For the full list of 130, run:

```bash
python3 -c "
import json, glob
for p in glob.glob('entries/*/*.json'):
    d = json.load(open(p))
    pos = (d.get('metadata') or {}).get('tags', {}).get('pos', []) or []
    if d.get('conjugation') and not any(x in pos for x in ['verb-godan','verb-ichidan','verb-suru','verb-irregular','verb-kuru','adjective-i']):
        print(d['id'])
"
```

**Sub-pattern: adverb cases (96 of the 130)** are the cleanest demonstration of failure. These are adverbial forms of i-adjectives (著しく ← 著しい), adverbs derived from other roots (おそらく, ますます), or fixed phrases (あいにく). They have no verb morphology of their own, but `add_conjugations.py` saw the く ending and generated `godan-ku` conjugations like `著しきます` and `すごかない` — forms that are not Japanese.

**Sub-pattern: expression cases (31)** are partly correct, partly broken. Expressions ending in する (頼りにする, お会いする) get suru-conjugations that happen to be correct because the script conjugates する correctly regardless of the surrounding phrase. Expressions whose final verb is ichidan but tagged godan (反応を見る where 見る is ichidan) produce nonsense like `反応を見ります`.

**Suggested actions**:
1. **One-shot pruner** that finds every entry where `pos` contains no `verb-*` value but the entry has a `conjugation` field, prints them for review, and on confirmation removes the `conjugation` field and the stray `verb_class` tag. Replaces the narrower 12-entry list filed earlier. See [Tooling Backlog](tooling-backlog.md) → item 5.
2. **Defensive guard in `add_conjugations.py`**: refuse to write a conjugation block unless the entry has at least one `verb-*` POS tag. Prevents regeneration.
3. **For the 31 expression cases**: review whether they should keep a conjugation block at all. Most idioms don't conjugate as a unit; the underlying verb's conjugation is usually all the learner needs. If a conjugation block is desired, the type must match the final verb's class.
4. See [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Runaway automation" for the broader pattern.

**Update 2026-06-05**: Comprehensive-polish session 015 (entries 05165–05184) found two more adverb entries (05173_nurunuru, 05175_tsurutsuru) with spurious `verb_class: "godan-ru"` tags and full conjugation tables producing nonsensical forms like ぬるぬらない, つるつらない. These are mimetic adverbs, not verbs. Reinforces the case for the batch pruner and defensive guard. A targeted scan of adverb entries for `verb_class` tags or `conjugation` fields would catch all remaining instances.

**Update 2026-06-06**: Comprehensive-polish session 024 (entries 05349–05373) confirmed a dense cluster of mimetic adverbs with spurious `conjugation` fields and `verb_class` tags (godan-ku, godan-ru, godan-tsu) — confirmed in 05352, 05364, 05372, 05373, likely extending into 05374+. Same claude-opus-4-5 / 2026-04-14 batch signature as the Priority 11 semantic-tag errors, so the two cleanups can be scoped together. Reinforces the case for a defensive guard in `add_conjugations.py` (Tooling Backlog item 5).

## Priority 7: Politeness tag conflation (uchi/soto, bikago, familiar suffixes)

**Source**: Wiki maintenance 2026-05-11 entry exploration

The `politeness` tag's four buckets (plain/polite/humble/honorific) are being applied too loosely. Three sub-issues:

1. **Uchi/soto kinship terms mis-tagged as humble**: 母 (はは), 父 (ちち), 兄 (あに), 姉 (あね), 息子 (むすこ) and several similar entries are tagged `politeness: humble`. They are the plain in-group reference forms, not humble forms in the technical sense. The contrast お母さん/お父さん/お兄さん etc. (out-group reference and address forms) is uchi/soto, not the speech-level politeness scale.

2. **Bikago mis-tagged as honorific**: Words where the お〜/ご〜 prefix has fused into the lexical form (ご飯, お釣り, etc.) are tagged `honorific`. They are 美化語 (bikago, beautifying language) — a separate category in the 2007 五分類 (five-category) reclassification — not productive sonkeigo.

3. **Familiar suffixes mis-tagged as honorific**: 〜ちゃん, 〜くん are tagged `politeness: honorific`. They are diminutive/familiar suffixes marking intimacy or subordinate-status address, not deference.

**Total affected**: ~58 entries with non-verb POS and `politeness: humble`; ~49 entries with non-verb POS and `politeness: honorific`. Not all are wrong, but a meaningful fraction is.

**Suggested actions**:
- These cases need semantic review, not a deterministic pass. They are a natural target for a polish-politeness-labels task (parallel to `polish_semantic_labels.md`).
- In the interim, ensure the notes prose carries the correct nuance even if the tag is coarse. Most well-polished entries (e.g., 00549_haha) already do this.
- Longer term: see [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Implications for the schema" for the structured-politeness proposal vs. its costs.

**Progress 2026-06-22 (detector slice RESOLVED)**: The mechanically-detectable slice — `check_tag_drift.py --check politeness-unsupported`, which flags `humble`/`honorific` entries whose notes contain none of the keigo support keywords — is at **0** dictionary-wide. The 2 then-open flags were verified and fixed: 23570 つまらないものですが (humble, correct — added a 謙譲 register sentence) and 27145 閣下 (honorific, correct — added a 尊敬 clause). Both tags were right; the notes simply lacked the supporting wording, so the fix was to document the register, not retag. The `backlog-queue.json` item `tag-politeness-unsupported` is marked resolved (kept as a standing check). The **broader** semantic review above (uchi/soto kinship terms, bikago, familiar suffixes mis-tagged) is NOT covered by this detector — those entries do carry supporting notes — and remains an open polish-politeness-labels task.

## Priority 8: Unconsolidated duplicate-expression entries

**Source**: Wiki maintenance 2026-05-11 entry exploration

Some entries are duplicates of each other that were linked via `prominent_see_also` instead of being merged. Confirmed example: 02008_ikuratemo and 02461_ikuratemo both cover the expression いくら〜ても. The two entries have overlapping examples and similar (but not identical) notes. The link makes the relationship discoverable but two parallel sources of truth keep diverging on every polishing pass.

**Suggested action**: Run `python3 build/find_merge_candidates.py --merge-only` and review the output. Merge candidates where the two entries are functionally identical. The `consolidate-entries` skill describes the process; the `resolve-duplicates` skill (`.claude/skills/resolve-duplicates/SKILL.md`) is the operational guide.

Also: 02008_ikuratemo carries `semantic: ["furniture"]` — an obviously stale auto-label. This is a representative case for [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels."

## Priority 9: Malformed furigana wrappers

**Source**: Wiki maintenance 2026-05-12 entry exploration

**859 instances across 624 unique entries** have hiragana inside the kanji portion of a furigana wrapper, in violation of the documented convention that `{kanji|reading}` puts kanji-only text on the left of the pipe. Distribution:

| Field | Instances |
|-------|----------:|
| Headword | 22 |
| Examples | 253 |
| Notes | 584 |

By sub-pattern:

| Sub-pattern | Count | Example | Renders OK? |
|-------------|------:|---------|-------------|
| お-prefix inside wrapper | 211 | `{お酒\|おさけ}` | yes, but breaks lookups on partial wraps like `{お会\|おあ}` |
| ご-prefix inside wrapper | 13 | `{ご飯\|ごはん}` | mostly yes |
| Pure-kana wrapper (no kanji) | 172 | `{どんどん\|どんどん}`, `{ところ\|所}` | varies; `{ところ\|所}` is **reversed** and renders wrong |
| Okurigana inside wrapper, reading covers full word | 152 | `{若い\|わかい}` | yes — over-wrapped only |
| Okurigana inside wrapper, **reading truncated** | 68 | `{やり方\|かた}` | **no — visibly wrong furigana** |
| Other interleaving | 243 | `{か所\|かしょ}`, `{差し水\|さしみず}` | yes — over-wrapped only |

**Highest-severity sub-pattern: 68 entries with truncated readings.** The wrapper includes preceding hiragana on the surface side, but the reading covers only the kanji. Browsers paint the partial reading over the full surface, producing visibly wrong furigana on the live site (e.g., `かた` rendered over the entire `やり方`).

**Update 2026-06-09 (RESOLVED)**: Routine systemic-fix session fixed all 74 reading-truncated entries, 9 pure-kana reversed entries, and 7 nested-brace entries. 0 remain for these sub-patterns. The 130 slash-reading entries ({七|なな/しち} style) remain open under Priority 12.

**Highest-volume sub-pattern: 463 okurigana-inside-wrapper instances.** Most render correctly but are non-standard. Canonical form would be `{若|わか}い` instead of `{若い|わかい}`, etc.

**Confirmed downstream impact**: 01525_wakai (basic-tier 若い) is currently missing its conjugation table on the live site because `add_adjective_conjugations.py` couldn't parse the headword `{若い|わかい}` to extract a stem.

**Suggested actions**:
1. **Targeted pass on sub-pattern 3b (68 truncated-reading instances)** — these are real rendering bugs. Manual review and repair.
2. **Mechanical sweep** for sub-patterns 1, 2, and 3a/3c (~791 instances). Regex-driven replacements with validation against `build/word_id_lookup.json`. Mostly cosmetic but worth doing while the pattern is fresh.
3. **Add a furigana-format validator** (`build/check_furigana_format.py`) alongside the existing `verify_furigana.py` (which checks only for *missing* furigana, not malformed wrappers). See [Tooling Backlog](tooling-backlog.md) → item 8.
4. **Restate the convention in `entry-guidelines`** so new entries don't reintroduce the pattern. The current docs state "all kanji must have furigana" but don't address where the wrapper boundaries should sit relative to hiragana characters.
5. See [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) for the full analysis.

**Update 2026-06-06 (new sub-pattern: nested/double braces)**: Comprehensive-polish session 025 (entries 05374–05389) found a *nested* furigana wrapper form, `{{word|reading}phrase|compound-reading}`, in 05379 and 05380. This is invalid — each kanji compound should carry its own `{漢字|かんじ}` annotation rather than nesting one wrapper inside another. The furigana renderer expects a flat `{kanji|reading}` and will misrender or drop the nested form. **Detection**: `grep -rl '{{' entries/` (the literal `{{` opening is the tell). Scope unknown; this is the first range where the nested form has been observed, so a one-shot scan across all entries is warranted. The format validator proposed in [Tooling Backlog](tooling-backlog.md) → item 8 should add a "nested wrapper" check alongside its other rules.

**Update 2026-06-17 (new sub-pattern: no-pipe brace spans + stray trailing brace)**: A 2026-06-16 routine polish session found a furigana-brace malformation in **06147_jiboujiki** distinct from all the sub-patterns above: the `{...}` (kanji|reading) syntax applied to a **whole kana phrase with no `|` separator at all** (`{やけになる}`) and a valid wrapper followed by a **stray trailing `}`** (`{投|な}げやりになる}`). Both render as literal braces on the live site and — because there is no pipe — they slip past furigana-*coverage* checks entirely (those only look for kanji lacking a reading, not for degenerate wrappers). This is likely present across the **same early-2026 yojijukugo batch** (06140s idiom cohort under P21). **Detection / tool side**: extend `build/check_furigana_format.py` to flag (a) `{...}` spans that contain no `|`, and (b) unbalanced braces in a field — see [Tooling Backlog](tooling-backlog.md) → item 8. Fixed in 06147 during the originating session; the rest of the batch is unswept.

**Update 2026-06-20 (cosmetic-wrapper batch confirmed at the 06xxx frontier; a new empty-reading degenerate)**: A 2026-06-20 routine polish observation found the early-2026 06xxx creation batch carries two of the documented cosmetic sub-patterns — an **お-prefix-inside wrapper** (`{お年寄|としよ}り`-style, sub-pattern 1) and a **pure-kana / empty-reading wrapper** (sub-pattern 3) — plus a previously-unlisted degenerate form: a **valid kanji left, *empty* reading right** of the pipe (`{きつい|}`-style, i.e. `{X|}` with nothing after `|`). These render OK or near-OK (warn/info severity, not the high-severity reading-truncation class already RESOLVED in the 2026-06-09 update), but they are non-standard and cluster in the Jan-2026 06xxx batch. Current dict-wide detector counts (`build/check_furigana_format.py --summary`): **o-go-prefix = 228, pure-kana = 888, over-wrapped = 452, nested = 1** (1,569 total across 1,127 entries). The o-prefix and pure-kana sub-patterns *are* caught by the detector, so a **scoped mechanical sweep of the 06000–06400 slice** (validated against `build/word_id_lookup.json`, per the existing suggested-action #2) is a ready systemic-fix candidate. **Open tooling question**: confirm the detector flags the **empty-reading-after-pipe** form `{X|}` — if it does not, add it to [Tooling Backlog](tooling-backlog.md) → item 8 alongside the no-pipe-span and unbalanced-brace checks (the 2026-06-17 update), since `{X|}` is the natural third degenerate-wrapper case (no reading at all, vs. no pipe at all).

**Update 2026-06-23 (frontier instances at 06231 — kana-inside-group + nested braces)**: A
2026-06-22 routine polish run found **06231** carrying two of the documented malformed
forms together: a **non-kanji character inside the kanji-left group** (`{お吸|す}い{物|もの}`,
the お-prefix-inside sub-pattern 1 → should be `お{吸|す}い{物|もの}`) and **nested braces**
(`{とん{汁|じる}}`, `{けんちん{汁|じる}}`, the sub-pattern from the 2026-06-06 update → should
be `とん{汁|じる}` / けんちん{汁|じる}). Both pass schema and furigana-*coverage* checks but
render wrong. They are detector-caught (`o-go-prefix` and `nested` classes), so the 06231
instance reconfirms the 06xxx Jan-2026 batch carries these in its notes and that the scoped
**06000–06400 mechanical sweep** (validated vs. `word_id_lookup.json`, suggested-action #2)
would clean them along with the o-prefix/pure-kana wrappers already noted at this frontier.

**Update 2026-06-26 (nested お-prefix wrappers at the 06295/06296 honorific cohort — a concrete auto-fix transform)**: A 2026-06-26 routine polish run (frontier 06288–06300) found **06295** and **06296** carrying the **nested-brace + お-prefix-inside** form together — `{お{香|こう}}` and `{お{土産|みやげ}}` — i.e. an honorific お placed *inside* an outer wrapper that also nests an inner `{KANJI|reading}`. These are detector-caught (`nested` + `o-go-prefix` classes, Tooling item 8) and almost certainly recur across the same お-prefixed honorific batch in the 06200s–06300s (cf. the 06231 `{お吸|す}い{物|もの}` instance in the 2026-06-23 update). The observing run noted these have a **single deterministic rewrite** — `{お{KANJI|reading}}` → `お{KANJI|reading}` (drop the outer braces, lift the お outside) — which is provably safe because it changes only the wrapper boundaries, not the surface text or reading. This is the cleanest auto-fixable sub-pattern in P9: a candidate for an **`--fix` mode on `check_furigana_format.py`** for exactly this `{お{…|…}}` / `{ご{…|…}}` shape (validated against `word_id_lookup.json`), rather than per-entry hand-editing it as the scoped 06000–06400 mechanical sweep advances past 06400. See [Tooling Backlog](tooling-backlog.md) → item 8.

**Update 2026-06-25 (06000–06400 slice swept)**: A routine systemic-fix run worked the
predicted scoped slice end-to-end, per-entry verified, fixing **18 instances across 16
entries** (`detect` total 1565 → 1547): pure-kana wrappers around katakana loanwords
(`{リーダー|りーだー}`, `{ボランティア|ぼらんてぃあ}`, `{タバコ|たばこ}`, `{メガネ|めがね}`,
`{ブラッドムーン|…}`, `{サインポール|…}`, `{タッチ|たっち}`, `{おかわり|おかわり}`,
`{すぐ|すぐ}`, `{ばさみ|はさみ}`) de-wrapped to bare kana; お/ご-prefix wrappers
repositioned (`{お問|おと}`→`お{問|と}`, `{ご飯|ごはん}`→`ご{飯|はん}`); over-wrapped
okurigana/compounds split with the correct rendaku reading (`{数え|かぞえ}`→`{数|かぞ}え`,
`{どん底|どんぞこ}`→`どん{底|ぞこ}`, `{流れ星|ながれぼし}`→`{流|なが}れ{星|ぼし}`,
`{横ずれ断層|よこずれだんそう}`→`{横|よこ}ずれ{断層|だんそう}`). Inline-link surfaces were
preserved (links resolve by explicit `：entry_id`), validation and furigana-coverage stayed
clean, and a furigana self-check screened the changed IDs with **0 flags**. The item stays
**open** — it is dictionary-wide (remaining ~1546 across the o-go-prefix/pure-kana/over-wrapped
sub-patterns); the next ready slice is 06400+ and the larger pre-06000 backlog.


**Update 2026-06-27 (06400–06650 slice swept)**: A routine systemic-fix run worked the
next scoped slice per-entry, fixing **30 instances across 24 entries** (`detect` total 1547 →
1517): katakana-loanword de-wraps (リフォーム/カード/メイク/バレーボール/キック/プル/ボール/エース/
パワーフォワード/スモールフォワード/オフィス — hiragana ruby over katakana is redundant), o-prefix
repositions (`{お寺|おてら}` → `お{寺|てら}`, `{お正月|しょうがつ}` → `お{正月|しょうがつ}`),
over-wrapped okurigana splits (`{余り|あまり}` → `{余|あま}り`, `{やり方|やりかた}` → `やり{方|かた}`,
`{引っ越|ひっこ}` → `{引|ひ}っ{越|こ}`, `{瞬き|まばたき}` → `{瞬|まばた}き`), numeral de-wraps to bare
digits (`{20|にじゅう}` → `20`, etc.), and symbol/letter readings converted to standard parenthetical
form to drop the malformed wrapper while preserving the reading (`{#|シャープ}` → `#（シャープ）`,
`{V2|ブイツー}` → `V2（ブイツー）`). One genuine **bug** also fixed: an English gloss sitting where the
reading belongs — `{ゴマフアザラシ|spotted seal}` rendered "spotted seal" as ruby — corrected to
`ゴマフアザラシ (spotted seal)`. This **English-text-after-pipe** form is a degenerate wrapper the
detector currently lumps into `pure-kana`; a dedicated check (right side contains Latin letters /
is an English phrase) would surface the class cleanly — see [Tooling Backlog](tooling-backlog.md) →
item 8. §4 furigana self-screen: 2 model flags, both rejected (okurigana び of 喜ぶ; katakana プロ
takes no furigana). Next ready slice: 06650+ and the larger pre-06000 backlog.

**Update 2026-06-28 (06650–07300 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **34 instances across 26 entries** (`detect` total 1517 → 1485):
katakana-loanword de-wraps (コミュニケーション/チーム/コーヒー/クリニック/タオル/ゴキブリ/トイレ/
ラベンダー/シニア/プレゼント/ベビーチェア/オストメイト/イクメン/カビ/ブランド — hiragana ruby over
katakana is redundant), pure-kana de-wraps (やっぱり/しまう/めまい/ふらふら/ひょっとこ/きっかけ),
numeral de-wraps in a ratio example (`{3|さん}対{2|に}` → `3対2`), o-prefix repositions
(`{お元気|おげんき}` → `お{元気|げんき}`, similarly お{客|きゃく}/お{経|きょう}/お{盆|ぼん}), and
over-wrapped okurigana splits (`{旨み|うまみ}` → `{旨|うま}み`, `{卸し金|おろしがね}` → `{卸|おろ}し{金|がね}`,
`{下ろし金|おろしがね}` → `{下|お}ろし{金|がね}`). One detector **mis-suggestion** was caught and
corrected by hand: `{おむつ替|か}` (in 07140) was flagged `o-go-prefix` with suggestion `お{むつ替|か}`,
but おむつ is a fixed kana word (not honorific お + むつ) and the only kanji is 替, so the correct
rewrap is `おむつ{替|か}` — a reminder that the detector's `o-go-prefix` suggestion assumes the お is
honorific and must be verified per-entry. The 06860 ブランド de-wrap sat inside an inline link
(`⟦{ブランド|ぶらんど}→ブランド：05221_burando⟧` → `⟦ブランド→ブランド：05221_burando⟧`); it resolves by
explicit `：entry_id`, so the link still works. Validation and furigana-coverage stayed clean.
§4 furigana self-screen: 3 model flags, **all rejected** — each was a screener compound-reading-split
false positive (`{次々|つぎつぎ}`, `{入場料|にゅうじょうりょう}`, `{低血圧|ていけつあつ}` reported as
truncated although correct in the entry), and none touched the edited furigana. Next ready slice:
07300+ and the larger pre-06000 backlog.

**Update 2026-06-30 (07300–07600 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **24 instances across 18 entries** (`detect` total 1488 → 1463):
pure-kana katakana/kana de-wraps (プロジェクト/スキルアップ/メンバー/チーム/バー/リストラ/タオル/
ティッシュ/ボールペン/エコバッグ/ノベルティ/データ/イメージ×2/ボケ — hiragana ruby over katakana is
redundant), o-prefix repositions (`{お金|かね}` → `お{金|かね}`, `{お茶屋|おちゃや}` → `お{茶屋|ちゃや}`,
`{お菓子|おかし}` → `お{菓子|かし}`), and over-wrapped okurigana splits (`{取り消し|とりけし}` →
`{取|と}り{消|け}し`, `{女の子|おんなのこ}` → `{女|おんな}の{子|こ}`, `{すり身|すりみ}` → `すり{身|み}`,
`{届け出|とどけで}` → `{届|とど}け{出|で}`, `{太っ腹|ふとっぱら}` → `{太|ふと}っ{腹|ぱら}`). Two
non-format fixes of malformed wrappers: `{できる|できない}` (surface≠reading) → `できる/できない` to
restore the can/cannot contrast its gloss describes, and `{どこ|}` (empty reading) → `どこ`. No edit
sat inside an inline link. Validation and furigana-coverage stayed clean. §4 furigana self-screen:
2 model flags, **both rejected** — 07459's `{一見|いっけん}` is the entry's own "NOTE ON READING"
contrast with いちげん (correct, not an inconsistency), and 07364 was a model misreading ("to sing"
read as "to sin"; the 歌=うた furigana is correct). Neither touched the edited furigana. Next ready
slice: 07600+ and the larger pre-06000 backlog.

**Update 2026-07-01 (07600–07900 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **27 instances across 22 entries** (`detect` total 1463 → 1436):
pure-kana katakana/kana de-wraps (グループ×2/シーン×2/キャラ/サービス×2/コンセント/
デジタルトランスフォーメーション/オン/オフ/エンゲージメント/コンプライアンス/ネイル/ネオン/やおい/
わきまえる×2 — hiragana ruby over katakana/kana is redundant), over-wrapped okurigana splits
(`{素っ気|そっけ}ない` → `{素|そ}っ{気|け}ない`, `{肩凝り|かたこり}` → `{肩|かた}{凝|こ}り`,
`{肩こり|かたこり}` → `{肩|かた}こり`, `{か細|かぼそ}い` → `か{細|ぼそ}い`), and o-prefix repositions
(`{お互|たが}` → `お{互|たが}`, `{お世辞|おせじ}` → `お{世辞|せじ}` ×3). Two entries (07715 OB, 07716 OG)
misused the furigana wrapper for an English-source gloss (`{old girl|オールドガール}`,
`{old boy|オールドボーイ}` — base=English, reading=katakana, which renders wrong); rewritten to plain
`'old girl'`/`'old boy'` since the etymology line already gives the katakana origin. No edit sat inside
an inline link. Validation and furigana-coverage stayed clean. §4 furigana self-screen: 21 screened,
**0 flags**, 1 skipped. Next ready slice: 07900+ and the larger pre-06000 backlog.

**Update 2026-07-02 (07900–08300 slice swept)**: A routine systemic-fix run worked the next
scoped slice per-entry, fixing **31 instances across 25 entries** (`detect` total 1436 → 1405):
pure-kana katakana/kana de-wraps (ささみ/アナウンス/ゆうパック/パレード/プロ/ステンレス/アルミ/データ/
マッサージ/ステーキ/Wi-Fi/バッテリー/エアコン/テレビ/アルバイト/デザイン/パスポート/サラダ/つま/
チョコレート/チーズ×2/もう — hiragana ruby over katakana/kana/Latin is redundant), over-wrapped
okurigana splits (`{振り分|ふりわ}` → `{振|ふ}り{分|わ}`, `{抜てき|ばってき}` → `{抜|ばっ}てき`,
`{認め印|みとめいん}` → `{認|みと}め{印|いん}`, `{御負け|おまけ}` → `{御|お}{負|ま}け`), and
o-/go-prefix repositions (`{お土産|おみやげ}` → `お{土産|みやげ}`, `{ご飯|はん}` → `ご{飯|はん}` ×3).
The legit whole-compound `{認印|みとめいん}` was left untouched (no internal kana). No edit sat inside
an inline link. Validation and furigana-coverage stayed clean. §4 furigana self-screen: 16 screened,
**1 flag rejected** (07950 `{代引|だいび}き` — model wanted き folded into the reading, but き is genuine
okurigana of 引き; documented okurigana false-positive family, and untouched by the edits), 9 skipped.
Next ready slice: 08300+ and the larger pre-06000 backlog.
## Priority 10: "するする" typo in TRANSITIVITY → Pattern lines

**Source**: Comprehensive-polish 2026-05-17 sessions 001–002 (entries 01808–01856)

Multiple entries in the 01808–01856 range have `するする` instead of `する` in their TRANSITIVITY → Pattern notes field. Likely a template copy-paste error during batch creation. The originating sessions fixed all instances they encountered (01811, 01823, 01826, 01828, 01830, 01832, 01833, 01835, 01837, 01839, 01841, 01843, 01845, 01847, 01849, 01851, 01852, 01855), but the pattern may extend into ranges not yet polished.

**Detection**: `grep -rl 'するする' entries/ | head -30`

**Suggested action**: One-shot grep-and-fix pass replacing `するする` with `する` in the notes field. Low risk — the doubled form is never correct Japanese.

## Priority 11: Batch-creation semantic tag "transportation" misapplied

**Source**: Comprehensive-polish 2026-05-17 sessions 001–002 and 009 (entries 01808–02011)

Entries in the 01808–02011 range have `semantic: ["transportation"]` applied to words with no connection to transport. Examples: 01815 ({飽|あ}きる, "to get bored"), 01822 ({居眠|いねむ}り, "dozing off"), 01825 ({衣服|いふく}, "clothing"). The polish sessions fixed individual entries, but the pattern suggests systematic misapplication in this ID range during batch creation.

This is the same category of stale-auto-label error as the `furniture` tag in the 01490–01511 range and `electronics` in the 02000s, now joined by `transportation` in the 01808–02011 range. See [Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels" for the broader analysis.

**Suggested action**: Spot-check entries in the 01800–02100 range for `semantic: ["transportation"]` tags that don't match entry content. If widespread, a targeted batch fix is warranted.

**Update 2026-05-19**: Two more entries with wrong semantic tags surfaced in the 02251–02273 range (02268 和紙, 02269 りんご), suggesting the pattern extends beyond the 02011 boundary identified above. Tag assignment quality appears inconsistent across multiple creation batches, not just a single cohort.

**Update 2026-05-25**: Entry 03218 手術 had `semantic: ["body-part", "time-general"]` — neither tag fits a surgical procedure (should be "medical" or "action"). This confirms the wrong-specific-tag pattern extends into the 03200+ range with novel tag combinations, not just the `transportation`/`furniture`/`electronics` labels seen in earlier ranges.

**Update 2026-05-26**: Two comprehensive-polish sessions (entries 03360–03385 and 03491–03510) surfaced five more wrong-tag instances with novel tag types: "tool" on adjective 03376_seishiki, "leisure" on 03383_tai (military unit), "time-general"/"weather" on 03385_taion (body temperature), "body-part" on 03491_choushi (condition) and 03503_chiryou (treatment), and "furniture" on grammatical word 03494_donnani. The misapplied-tag pattern now spans from the 01490s through the 03500s with at least seven distinct wrong-tag categories (transportation, furniture, electronics, clothing, body-part, tool, leisure, time-general, weather).

**Update 2026-05-27**: Three more comprehensive-polish sessions (entries 03582–03598, 03662–03676, 03677–03698) surfaced a further wave of wrong semantic tags extending the range to 03800:
- 03582–03598: "electronics" on 評価/表面/不幸; "transportation" on 服装; "body-part" on 笛; "emotion" on 不自由
- 03662–03676: "electronics" on 喜び (03672) and 理解 (03674)
- 03686–03698: "animal-mammal" on 像 (03691), "food" on 班 (03697), "body-part"/"transportation" on 進行 (03686), "body-part"/"occupation"/"time-general"/"transportation" on 操縦 (03689), "transportation" on 羽根 (03696)

The wrong-tag categories now include at least eleven distinct labels: transportation, furniture, electronics, clothing, body-part, tool, leisure, time-general, weather, animal-mammal, and food. The pattern spans 01490s through 03700s. A dedicated semantic-tag validation pass over the 03500–03800 range is warranted, as the density of wrong tags in this range appears higher than in earlier ranges.

**Update 2026-05-28**: Two more entries in the 03877–03888 range: 03881 釘 (nail) has "body-part" (should be "tool"), 03883 屑 (scrap/waste) has "furniture" (meaningless for this word). Confirmed range now extends through the 03800s. Added to [Entry Follow-ups](entry-followups.md).

**Update 2026-05-30**: Five comprehensive-polish sessions (2026-05-28 session 003 and 2026-05-29 sessions 001, 006, 007, 009) confirmed the wrong-semantic-tag pattern extends well into the 04000+ range:
- 03970–03990: "furniture", "electronics", "leisure", "animal-insect", "occupation", "time-general" on words like 我が〜, 器具, 基地, 弟子, 父母
- 04031–04042: 04038 台詞 had 5 wrong tags ("building", "electronics", "geography", "leisure"); 04039 扇子 had "electronics"; 04035 地盤 had "education"
- 04126–04149: 04134 液体 "body-part"; 04135 応用 "electronics"; 04141 系統 "furniture"; 04146 交替 "emotion"/"geography"; 04148 肯定 "electronics"/"furniture"/"geography"; 04149 鉱物 "time-general"
- 04150–04169: 04154 混合 "geography"; 04158 祭日 "geography"; 04166 資料 "furniture"; 04167 公式 "furniture"
- 04185–04204: 04198 車輪 "clothing" (→ transportation); 04201 障子 "communication"/"education" (→ building)

The confirmed range now extends from the 01490s through at least the 04300s. All sessions noted the pattern appears systematic across the 04000+ range and likely requires a bulk audit. Multiple sessions independently recommended a dedicated semantic-tag validation pass. The wrong-tag category set now includes at least fourteen distinct labels: transportation, furniture, electronics, clothing, body-part, tool, leisure, time-general, weather, animal-mammal, food, building, geography, and communication.

**Update 2026-05-31**: Four more comprehensive-polish sessions (2026-05-30, entries 04205–04349) confirmed the wrong-tag pattern continues unabated through the 04300s:
- 04205–04222: "electronics" on 申請 (application), "body-part" on 診断 (diagnosis), "education" on 実績 (track record)
- 04223–04243: "electronics" on 切り替える (should be "action"), "communication" on 振り向く/見送る (should be "action"), "food"/"tool" on 振る舞う
- 04282–04306: "electronics" on transport/work entries, "building" on 乗換 (should be transportation), "clothing" on 歯車 (should be general), "movement" on 蛙 (should be animal-insect), "furniture" on 推定 (should be general), "leisure" on 水産 (should be nature-environment)
- 04307–04326: "geography"/"time-general" on 発電 (power generation)
- 04327–04349: "body-part" on 反映, "leisure" on 売買, "education"/"leisure" on 政党, "leisure" on 引算

A recurring diagnostic: the AI model assigns semantic tags based on example sentence topics rather than the headword's semantic domain.

**Update 2026-06-01**: Two more comprehensive-polish sessions (2026-05-31, entries 04371–04395 and 04457–04466) confirmed the pattern continues into the 04400–04500 range:
- 04371–04395: Nature/food nouns (04383 全般, 04384 柿, 04387 栗, 04389 葬式) had template defaults "time-general", "transportation", "tool" — corrected in session.
- 04457–04466: Performing arts and musical instrument entries had wrong tags: 04459 脚本 "electronics", 04460 演出 "communication"/"education"/"furniture"/"leisure", 04462 フルート "body-part", 04464 三味線 "food", 04465 尺八 "body-part". All corrected to "leisure".

The confirmed range now extends from the 01490s through at least the 04500s. The wrong-tag category set remains at fourteen distinct labels.

**Update 2026-06-02**: Two more comprehensive-polish sessions (2026-06-01, entries 04533–04553 and 04574–04594) confirmed the pattern continues through the 04590s:
- 04533–04553: 04547 凸凹 "furniture"/"tool"→"general", 04549 伝染 "body-part"→"general", 04550 大金 "time-general"/"tool"→"work", 04535 サングラス "general"→"clothing", 04540 鉄砲 "general"→"weapon", 04544 団扇 "electronics"→"tool"
- 04574–04594: 04583 聞き取る "geography"/"work"→"communication"/"action", 04585 早まる "electronics"/"time-general"→"action", 04589 枯れる "furniture"→"nature"/"action", 04590 思い切る "communication"→"action"

**Update 2026-06-03**: Four more comprehensive-polish sessions (2026-06-02, entries 04730–04801) confirmed the pattern extends into the 04700–05000 range:
- 04730 フォロー had "building"/"transportation"→"communication"/"action"
- 04741–04760: 04742 決勝 "furniture"/"tool"→"sports"/"competition"; 04747 やばい "weather"→"descriptive"; 04757 クラウド "weather"→"technology"
- 04761–04782: 04768 一期一会 and 04773 四苦八苦 both had "furniture"→"expression". The "furniture" tag now confirmed as a template artifact that crept into yojijukugo and expression entries created in bulk.
- 04783–04801: 04796 関数 "electronics"→"general" (mathematics); 04799 魅力的 "furniture"→"general" (appearance); 04800 内閣 "furniture"→"general" (government)

The confirmed range now extends from the 01490s through at least the 04800s. A targeted semantic-tag audit of the 04700–05000 range is warranted.

**Update 2026-06-04**: Three more comprehensive-polish sessions (2026-06-03, entries 04985–05037) confirmed the pattern extends into the 05000+ range:
- 04985–04992: 04985 浴槽 "animal-mammal" (→ building/household); 04988 洗面台 "animal-mammal"/"transportation" (→ building/household); 04992 前菜 "electronics" (→ food)
- 05018–05032: Health/medical entries had emotion/weather/time-general tags: 05018 凍傷 "weather" (→ health); 05019 腹痛 "body-part"/"emotion" (→ health); 05020 腰痛 "emotion" (→ health); 05028 内臓 "time-general" (→ body)

A sub-pattern emerged: health/medical vocabulary is systematically receiving emotion, weather, and time-general tags — three categories with no semantic connection to medical content. The confirmed range now extends from the 01490s through at least the 05000s.

**Update 2026-06-05**: Three more comprehensive-polish sessions (2026-06-04, entries 05095–05141 and 05211–05230) confirmed the pattern extends well into the 05200+ range:
- 05095–05120: cosmetics tagged "electronics", sunscreen tagged "electronics", ガイド tagged "tool", 姑 tagged "animal-insect"
- 05121–05141: 05134 納品 (delivery) tagged "communication" — delivery of goods is not communication; should be "action" or logistics-related
- 05211–05230: 05212 取材 tagged "building"/"education"/"transportation"; 05221 忍耐 tagged "clothing"/"time-general"; 05227 広報 tagged "geography"; 05228 tagged incorrectly

The confirmed range now extends from the 01490s through at least the 05230s. A targeted bulk audit of the 05000–05500 range is warranted.

**Update 2026-06-06**: Five comprehensive-polish sessions (2026-06-05, sessions 021–025, entries 05291–05389) confirmed the pattern saturates the 05300s, with a clear common origin: most of the wrong-tagged entries were created by **claude-opus-4-5 with modified date 2026-04-14**, pointing to a single batch run whose semantic-tag data was cross-contaminated.
- 05291–05312: "transportation" on だるい/面倒くさい, "animal-mammal" on 浴室, "animal-insect" on だるい, "furniture" on 叶う
- 05318 体力: "leisure" (→ health/body); check the 気力/精力/忍耐力 cluster
- 05332–05335 (足し算, 引き算, 掛け算, 割り算): "body-part"/"furniture"/"time-general" instead of "mathematics"
- 05344 焦げる: "body-part" (→ action)
- 05349–05373 (mimetic adverbs): wrong semantic tags (food, furniture, body-part, electronics, animal-mammal, building, leisure) instead of "descriptive" — plus the spurious-conjugation problem logged under Priority 6
- 05374–05389: health entries (下痢, 便秘, インフルエンザ, 包帯, 絆創膏) tagged "general"/"body-part" instead of "health"; education entries (生徒会, 職員室) tagged "general" instead of "education"

The 2026-04-14 claude-opus-4-5 modified-date signature gives a concrete way to scope the eventual bulk fix: the tag-validation pass (Tooling Backlog item 6) could prioritize entries carrying that creation signature.

**Update 2026-06-07**: Three more comprehensive-polish sessions (2026-06-06, sessions 029/030/033, entries 05468–05559) confirmed the tag-drift pattern extends into the 05500+ range:
- 05468–05482: 05474 分量 "building"/"transportation" (→ measurement), 05475 重量 formality "informal" (→ neutral), 05476 金槌 "food"/"tool" (→ tool only)
- 05483–05502: 05484 体温計 "time-general"/"tool"/"weather" (→ health/tool), 05485 体重計 "animal-mammal"/"tool" (→ health/tool), 05486–05489 plants "general" (→ plant/nature), 05496 ジャングル "general" (→ nature/geography), 05497 高原 "food" (→ geography/nature), 05498 海辺 "general" (→ geography/nature), 05499 群島 "tool" (→ geography/nature), 05500 本土 "general" (→ geography)
- 05540–05559: 05551 えんちゅう "body-part", 05556 ないがい "electronics"/"furniture", 05557 だいしょう "building" — all fixed to "general"

The confirmed range now extends from the 01490s through at least the 05559. The pattern shows no sign of abating.

**Update 2026-06-08**: Comprehensive-polish session 037 (entries 05617–05635) surfaced four more wrong-tag instances at the leading edge of the polished range: 懸念 "electronics" (→ emotion/cognition), 端末 "building"/"transportation" (→ technology/general), 促進 "emotion"/"time-general"/"work" (→ action), 七夕 "animal-mammal" (→ culture/event). The confirmed range now extends from the 01490s through at least the 05635, tracking the comprehensive-polish frontier (main progress `next: 05735` as of this session). The signature is unchanged — example-sentence-topic contamination on a single 2026-04-14 claude-opus-4-5 batch — and the case for the Tooling Backlog item 6 tag-validation pass (scoped by that creation signature) only strengthens. Note that the comprehensive-polish frontier has now nearly reached the **upper** bound of the originally-flagged batch; once polishing passes ~05735 the live tag-drift reports should taper, leaving the *un-polished* high-ID ranges (anything from that 2026-04-14 batch sitting above the polish frontier) as the remaining audit surface — an argument for running the batch-signature audit pass rather than waiting for sequential polishing to reach every contaminated entry.

**Update 2026-06-09**: Three comprehensive-polish sessions (sessions 045, 049, 050, entries 05784–05953) confirmed the tag-drift pattern continues through the 05900s:
- 05784–05804: "electronics" on 風呂敷, "animal-fish" on じめじめ, "food" on こそこそ, "communication+education+tool" on 提灯, "furniture" on 暖簾. The "furniture" and "tool" tags appear loosely applied across the 05500–06000 range.
- 05891–05915: "electronics" on るんるん, "furniture" on 淡々, "tool" on 刻々, plus a wrong formality "informal" on 仲裁 (corrected to "neutral"). Tag drift continues unabated.
- 05936–05953: "animal-fish" on じとじと (→ "descriptive"), "animal-insect" on のそのそ (→ ["action", "descriptive"]). These are mimetic adverbs/descriptives — the same sub-pattern seen in the 05349–05373 range. The comprehensive-polish frontier now sits at entry 05954; the contaminated batch signature extends at least this far. **Cross-model accuracy-review (session 001)** independently found semantic misassignment in early entries (00016–00200) — different creation cohort, different failure mode (over-applied domain tags on multi-sense polysemous words), documented under the new Priority 17 (formality) and in [Entry Follow-ups](entry-followups.md).

**Update 2026-06-10**: Two more confirmations from Routine v2 runs.
- **Comprehensive-polish session 007 (entries 05970–05989)** found dense tag errors at the leading edge of the contaminated batch: a medical cluster (05975–05979: 通院, 処方, 感染, 炎症, 健康診断) and an aviation cluster (05981–05982: 離陸, 着陸) carried body-part/clothing/furniture/leisure/geography tags — the model had copied tags from an unrelated entry. Fixed in session; the 05970–05990 range likely holds more.
- **Cross-model accuracy-review session 002 (entries 00201–00450)** confirmed the same wrong-tag class in the *low-ID core/basic* range (a different cohort from the 2026-04-14 batch): 00281 醜い (food/leisure/slang/colloquial → emotion/appearance/literary), 00299 虫歯 (body-part → health — a dental condition, not a body part), 00240 小〜 (grammatical → size), 00232 記念 ("memory" → "memorial"). A recurring **sub-pattern** here is `body-part` misapplied to conditions/diseases (虫歯; cf. 03218 手術, 05019 腹痛 in earlier updates). The authoritative remediation path is now the accuracy-review mode's LLM `tags` pass — the [Quality Metrics Trend](../topics/quality-metrics.md) snapshot shows `tags` is the highest-precision review dimension (6.8% apply rate vs ~2% for gloss/translation), i.e. the dimension actually worth driving a fix from.

**Update 2026-06-13**: Comprehensive-polish session 008 (entries 06101–06110) found three more instances in the 06100s: 06107_junshu (遵守, compliance/observance) had `semantic: ["transportation"]` — corrected to `["action"]` (same wrong-specific-tag pattern as the rest of P11); 06101_hakumai (白米) had `semantic: ["general"]` instead of `["food"]`; 06106_katsuo (鰹, bonito) had `semantic: ["general"]` instead of `["animal-fish"]`. Note that the food/ingredient instances are the P13 under-specification pattern (correct fallback applied where a specific tag was available), while 06107 is the classic P11 wrong-specific-tag error. The contaminated range now extends at least to the 06100s. These are a different creation cohort than the 2026-04-14 claude-opus-4-5 batch that dominates the 01490–06100 range.

**Update 2026-06-14**: Comprehensive-polish session (frontier entries 06121–06128, all cultural-vocabulary nouns) found three more wrong-tag instances in this cohort: 06121_hibachi (火鉢) had `clothing` (→ `daily-life`), 06127_kouden (香典) had `time-general` (→ `culture`), and souryou (送料, shipping charge) had `communication` (→ `shopping`). Same example-topic-contamination signature as the rest of P11, now confirmed at the 06120s frontier. The session recommended a semantic-tag audit of the whole 2026-early cultural-vocabulary cohort (roughly 06100–06130), since the errors cluster tightly by creation batch rather than by word meaning.

**Update 2026-06-15**: Three more Routine runs confirmed the pattern persists at the comprehensive-polish frontier and re-confirmed a dense pocket in the 05000–05300 range:
- **Frontier 06129–06132** (consumer/business suru-noun cohort): 06129_kaiyaku had `geography,work` (→ business), 06130_henkin had `action` (→ money). Zero inline links plus template-default tags — same signature as the 06121–06128 cohort.
- **Frontier 06137–06149** (idioms / proverbs / yojijukugo): inaccurate default tags — 06139 `body-part` (→ movement), 06140 `occupation` (→ proverb), 06142 `communication`/`furniture` (→ proverb). A targeted tag-drift + inline-link pass over 06140–06170 would clean a coherent block.
- **05000–05300 pocket** (polish session): many genuine clearly-wrong tags fixed (26 in one run) — `body-part`/`communication` on 柱, `emotion` on 箪笥, `time-general` on ベランダ/わさび, `food` on コック/ウェイター, `body-part` on mimetic adverbs. This range also carries widespread **formality/politeness** data errors (茶漬け `politeness: honorific`, 羊羹 `formality: formal`) left for a dedicated register-tag pass — see P17.

The contaminated frontier now tracks to the 06140s; the 05000–05300 pocket shows the same 2026-04-14-batch signature as the rest of P11.

**Update 2026-06-12**: Comprehensive-polish session (entries 06048–06067) confirmed a **compound-verb / suru-verb sub-pattern** at the leading edge of the contaminated batch: compound verbs and suru verbs were systematically assigned object-category tags (electronics, clothing, tool, furniture, animal-mammal, occupation, body-part) instead of the action/cognition/communication/emotion tags appropriate for their meanings. Confirmed instances: 06051 clothing→movement, 06052 [food,leisure,tool]→action, 06053 [communication,furniture]→cognition, 06055 electronics→emotion, 06056 electronics→communication, 06058 animal-mammal→communication, 06060 electronics→cognition, 06062 occupation→cognition, 06066 action→emotion, 06067 action→emotion. Root cause: original AI generation applied topic-domain tags based on example sentence context rather than the verb's own semantic domain. The `check_tag_drift.py` unknown-semantic detector (P20) will flag the out-of-vocabulary cases; the correct-vocabulary-but-wrong-category cases (e.g. "action" on a cognition verb) are not detectable mechanically and require the accuracy-review `tags` pass or per-entry polishing. The 06000 range likely holds further instances of this sub-pattern.

**Update 2026-06-16**: A 2026-06-15 routine polish observation documented a dense pocket of the *in-list-but-wrong-category* tag drift across the **0552x–0570x range** (a different ID band from the 06xxx frontier but the same failure mode), with three recognisable sub-clusters:
- **Four-character idioms / yojijukugo** tagged with object domains: 起死回生, 七転八起, 自画自賛 → `furniture`; 油断大敵 → `leisure`/`emotion` (should be `expression`/`proverb`). Same artifact as the 04768 一期一会 / 04773 四苦八苦 → `furniture` cases noted in the 2026-06-03 update.
- **〜的 / 〜性 abstract adjectives/nouns** tagged with unrelated domains: 協力的, 歴史的, 政治的, 主観的, 全面的 → `time-general`/`education`.
- **Concrete nouns mis-tagged**: 天秤 → `clothing`; 苦楽/寒暖 → `body-part`; 頷く → `work`.
These are all `VALID_SEMANTIC` tags applied to the wrong domain, so the `check_tag_drift.py` unknown-semantic detector (P20) will **not** catch them — they need the accuracy-review `tags` pass or per-entry polish. The band sits just below the comprehensive-polish frontier (`next: 06147`), so sequential polishing has not yet reached it; the contaminated batch signature is consistent with the 2026-04-14 claude-opus-4-5 run that dominates the rest of P11.

**Update 2026-06-17**: Two 2026-06-16 Routine runs (an accuracy-review pass over 5704–6139 and a second accuracy-review pass over 6140–6340) re-confirmed the density of this pattern across the **5700–6340 block** and quantified it for the first time at the frontier:
- **5700–6100 block** (accuracy-review observation): ~50 entries carried genuinely-wrong or out-of-taxonomy concrete-domain tags — `electronics`/`furniture`/`weather`/`body-part`/`geography`/`leisure` misapplied, `onomatopoeia` **missing** on clearly mimetic words, plus invalid (out-of-list) `payment`/`body`/`death` tags. The invalid ones are P20 (unknown-semantic) territory; the misapplied in-list ones are the core P11 wrong-category failure.
- **6140–6340 range** (accuracy-review run): ~30% of entries carried categorically-wrong auto-assigned tags — 朱肉 (vermilion ink-pad) tagged `animal-mammal`, proverbs tagged `clothing`/`animal-insect`, idioms tagged `time-general`/`leisure`. **61 entries fixed in that single run.** The run noted that proverbs/yojijukugo should carry `proverb`/`idiom` (cf. the 04768/04773/0552x yojijukugo→`furniture` cases above) and recommended a dedicated **semantic-tag-vs-headword sanity detector** (proverbs/yojijukugo → `proverb`/`idiom`; concrete-noun headword vs concrete-domain tag mismatch) to clear the rest faster — see Tooling Backlog item 6. This is the same batch-creation signature as the rest of P11; the 5700–6340 block is the highest-density pocket measured to date and is a strong candidate for a scoped accuracy-review `tags` sweep ahead of the sequential polish frontier.

**Update 2026-06-17 (semantic-tag-vs-headword detector shipped + first batch):** The recommended sanity detector now exists. `build/check_tag_drift.py` gained two high-precision checks (read-only, JSON queue, `--check`/`--range`/`--summary`/`--cohort`), carved out of the noisy `semantic-mismatch` heuristic:
- **`proverb-idiom-mismatch`** — a proverb/yojijukugo/set-expression headword tagged with a physical-object/creature domain (furniture, clothing, electronics, food, animal-*) with no keyword support — the 一期一会/四苦八苦/起死回生 → furniture family. Identification is `yojijukugo (4 kanji) OR POS expression OR a gloss-level idiom marker`; the flagged domain set deliberately excludes tool/geography/weather/building/transportation/body-part (those legitimately apply to compositional 4-kanji compounds like 懐中電灯/都道府県/直射日光), and the keyword-absence filter spares correct cases like 三色団子→food. **Measured ~93% precision** (13–14/14) on the first batch.
- **`concrete-noun-domain-mismatch`** — a non-verb headword carrying ≥2 mutually-distant "hard" physical-object domains (横断歩道 → animal-mammal+clothing+transportation; 油絵 → body-part+tool). This is a *structural* signal (it counts incompatible domain clusters, ignoring the necessarily-incomplete keyword lists), so it sidesteps the `semantic-mismatch` noise floor — the broad keyword cross-domain variant was measured at ~5% precision (516 flags, mostly correct bench→furniture/school→building) and was NOT shipped. **Measured ~77% clear precision** (20/26); the residual ~6 are loanword/accessory polysemy (マウス animal+device) that are correct on review.

The two checks are registered in `backlog-queue.json` (`tag-concrete-noun-domain-mismatch`, `tag-proverb-idiom-mismatch`) and drained by the reusable prompt **`prompts/fix_semantic_tag_drift.md`** (deterministic checks first, then the accuracy-review `tags` pass for the in-list-but-wrong-category cases that are NOT mechanically detectable — e.g. 朱肉→animal-mammal as a *sole* tag, which keyword/structural checks cannot catch). The single-sole-wrong-tag family remains accuracy-review territory. First worked batch (2026-06-17) hand-verified and fixed **35 entries**: all 14 proverb-idiom flags, 18 concrete-noun flags, and 3 not-mechanically-detectable stragglers found by hand-walking the 5700–6340 block (臓器→body-internal, ぼうぼう→descriptive, ほっこり drop food). The 5700–6340 block itself was already clean of detector flags (the 2026-06-16 accuracy-review swept it), confirming the detector's residual value is *above* the sequential polish frontier (6375–7431) and as a standing guard on new entries. Cursor: `polishing/tasks/semantic-tag-drift/progress.txt`.

**Update 2026-06-18 (the P11 residue extends to ~6840, quantified at two more ranges)**: Two 2026-06-17 accuracy-review `tags` sweeps measured the *single-sole-wrong-category* density above the documented 5700–6340 block — the in-list-but-wrong-domain failure the deterministic detectors cannot see, so each is an accuracy-review apply:
- **6341–6540**: ~50 entries carried a flatly-wrong single semantic tag (取捨選択→body-part, どうせ→furniture, 乱視→furniture, 家畜→work, 憤慨→geography, アンチ→electronics, 健気→clothing). **50 fixes applied in one run** — category errors, not narrowness.
- **6541–6840**: **104 of 300** entries had clearly-wrong category tags (animal-mammal on ダッシュボード/打者, building+transportation on soccer-position loanwords, electronics/furniture/food on abstract nouns and adjectives). The reviewer's `tags` dimension caught these cleanly at error severity.
Both ranges sit *above* the comprehensive-polish frontier (`next: 06163`) and carry the same batch-creation signature as the rest of P11. A scoped accuracy-review `tags` sweep of **6157–~7500** ahead of the sequential frontier would keep yielding ~17–35% apply rates (these two runs drove the runs-61–77 `tags` apply rate to 51.2% — see [Quality Metrics Trend](../topics/quality-metrics.md)). This is the strongest remaining argument for running the band's `tags` sweep proactively rather than waiting for sequential polishing.

**Update 2026-06-18 (second — the residue extends to 6925)**: A 2026-06-18 accuracy-review `tags` sweep over **6840–6925** confirmed the contamination zone leaks past the 6840 boundary measured the day before: concrete-topic semantic tags (transportation / electronics / furniture / clothing / body-part / time-general) on unrelated words, **30 fixes applied in this range**. The same run also caught the formality half of the artifact — casual particles, fillers, and idioms (ぞ, なんて, やっぱ, よね, かしら, っていう, えーと) systematically mis-tagged `formality: formal` (see P17 update below). The proactive-sweep recommendation now extends to at least **6157–6925** as a confirmed dense band; the upper bound is still open.

**Update 2026-07-01 (the wrong-category drift reaches function words — a physical-object tag on an adverb)**: A 2026-07-01 routine polish run found **06355 どうせ** (an adverb) carrying the semantic tag `furniture` — nonsensical for a function word — *and* `formality: formal` directly contradicting its own notes ("Informal … inappropriate in polite or formal speech"). This is the same copy/template-error signature as the 起死回生→`furniture` / 一期一会→`furniture` yojijukugo cases, but on an **adverb**, which is a cleaner mechanical signal than the noun cases the shipped detectors target: a *physical-object/creature semantic tag on an adverb or particle POS* is almost never correct (function words have no concrete domain), and unlike the `concrete-noun-domain-mismatch` check it does not need ≥2 conflicting domains — a single such tag on a non-content POS is enough. The observing run recommends a **targeted scan of adverbs/particles for physical-object semantic tags** (see [Tooling item 6](tooling-backlog.md) update 2026-07-01 for the detector signal). The formality half is the P17 over-`formal` family (tag contradicts the entry's own REGISTER note). Both were fixed on 06355 in that run; the scan would surface siblings elsewhere in the closed adverb/particle set.

**Update 2026-07-02 (in-list-but-wrong-category drift on abstract/loanword nouns at 11573–11646)**: A 2026-07-01 accuracy-review over **11573–11646** found **5 of 14** `tags` flags genuine (≈36% precision) — a recurring **in-list-but-wrong-category** miscategorization where abstract nouns and katakana loanwords are tagged with an oddly-specific *in-list* domain rather than the fitting one: トレード and 作画 tagged `leisure`, 入浴 tagged `consumption`. This is the classic P11 signature (a valid `VALID_SEMANTIC` tag applied to the wrong domain, so **invisible to the P20 unknown-semantic detector** and to `concrete-noun-domain-mismatch` — the tag is neither off-vocab nor concrete-vs-concrete-conflicting), now confirmed still present up in the 11500s general-tier cohort, not just the 5700–6925 block. The observing run recommends a **targeted accuracy-review `tags` sweep of katakana/suru-noun entries** as the highest-yield slice for this failure mode. The furigana-screener flags in the same range were all false positives from the model truncating its own reading readout (the documented pair-extraction FP family — Tooling item 24). No mechanical detector catches this; it stays the accuracy-review `tags` dimension's job (cf. the 6157–7500 proactive-sweep argument above).

## Priority 12: Dual-reading furigana with slash separators — RESOLVED 2026-06-16

**RESOLVED (2026-06-16).** A systemic-fix Routine run fixed all **118 entries** (131 slash-reading wrappers) flagged by `build/check_furigana_format.py` (`subpattern == 'slash-reading'`). Each `{漢字|よみ1/よみ2}` wrapper was replaced, per-entry, with the single reading the kanji actually takes in context: the rendaku'd compound reading where the wrapper decomposes the headword ({歩|ぽ} in 散歩, {袋|ぶくろ} in 寝袋, {顔|がお} in ドヤ顔), the inline-link target's reading where the wrapper sat inside a ⟦…⟧ link ({毎年|まいとし}→00731_maitoshi), or the primary reading for standalone/related words ({梅雨|つゆ}, {買春|ばいしゅん}). Notes that explicitly discuss the reading variation (e.g. 七 なな/しち, 分 ふん/ぷん) kept their prose explanation; the wrapper just dropped to one reading. Two malformed English-in-reading wrappers were also repaired (28654 アプリ内課金: `{課金|billing/charging}`→`{課金|かきん}`, `{内|inside}`→`{内|ない}`). The detector now returns **0** slash-reading instances. A furigana self-check screened 59 of the 118 changed IDs before the 540 s `timeout` wrapper killed `review_runner.py` (logged as a `[tooling]` observation); its 11 flags were all false positives (rendaku-in-compound, okurigana/partial readings "correct by design", and screener input-truncation artifacts), 0 applied. Tracked as `furigana-slash-reading` in `backlog-queue.json`.

**Source**: Comprehensive-polish 2026-05-18 session 010 (entries 02251–02273)

Several entries in this range used non-standard dual-reading furigana notation with slash separators, e.g., `{村|むら/そん}`, `{蛍|ほたる/けい}`. These were normalized to single readings during the polishing session.

The slash-separator pattern is not documented in the `{kanji|reading}` convention and is likely ignored or misrendered by the furigana renderer (which expects a single reading string). The correct treatment is to pick the primary reading for the context and mention the alternative reading in notes.

**Detection**: `grep -rP '\{[^|}{]+\|[^}{]*\/[^}{]*\}' entries/ | head -30`

**Suggested action**: One-shot scan across all entries for the slash-in-reading pattern. Each instance needs manual review to select the correct single reading. The scope is unknown — this is the first range where the pattern has been observed.

## Priority 13: Overuse of "general" as sole semantic tag

**Source**: Comprehensive-polish 2026-05-23 sessions 003 (entries 03011–03035) and 005 (entries 03056–03077)

Many entries have `semantic: ["general"]` as their only semantic tag where a more specific tag (time, transportation, work, weather, etc.) clearly applies. This is distinct from the misapplied-specific-tag pattern in Priorities 11–12 — here the problem is under-specification rather than wrong specification. The tag "general" functions as a catch-all default that was never replaced with a meaningful label.

Session 003 noted the pattern in the 03011–03035 range. Session 005 confirmed it extends into the 03056–03077 range, finding 7 of 22 entries with "general" as the sole semantic tag. The pattern likely extends across much of the entry set, particularly entries created in early batch runs.

**Detection**: `python3 -c "import json, glob; [print(json.load(open(p))['id']) for p in sorted(glob.glob('entries/*/*.json')) if json.load(open(p)).get('metadata',{}).get('tags',{}).get('semantic') == ['general']]" | wc -l`

**Suggested action**: A targeted sweep replacing `["general"]` with more specific semantic tags. This overlaps with the tag-drift detector proposal in [Tooling Backlog](tooling-backlog.md) → item 6 — a semantic-tag/gloss keyword matcher could prioritize entries where "general" is the sole tag and suggest a replacement based on the English gloss. Unlike Priorities 10–12 (wrong specific tags), this is a classification gap rather than an active error, so it is lower urgency.

**Update 2026-06-18 (curator policy question — `general` → *clearly-correct* specific)**: Two 2026-06-17 accuracy-review sweeps (6341–6540 and 6541–6840) surfaced ~51 + ~28 "general → more-specific in-list tag" suggestions where the specific tag is **unambiguous and obviously correct** (害虫/蜜蜂→animal-insect, 踝→body-part, 経理→business, chisel→tool, stag beetle→animal-insect, cosmos→plant-flower, USB drive→electronics, carbon→science). The standing semantic-tag policy (2026-06-11, §A) rejects all in-list narrowness substitutions to suppress the `general`-too-broad reviewer noise (Tooling item 17), so **all were rejected** — but the observing runs flagged that many of these are *lazy-default* `general` on single-domain nouns, not a deliberate fallback, and the policy currently can't distinguish the two. **This is a curator decision, not a Routine one**: should `general` → a *clearly-correct single-domain* specific tag be an APPLY case (distinct from the leisure-vs-daily-life churn the policy rightly rejects)? If yes, it would need a tightened reviewer instruction (apply only when exactly one specific domain is unambiguous) to avoid reopening the noise floor. Logged here for the curator; no Routine action until policy is set. Related: P11 (wrong-category, already APPLY) vs. this (under-specification, currently REJECT).

**Update 2026-06-28 (the under-specification is itself a create-era batch signature)**: A 2026-06-27 routine polish §4 self-check on the **06298–06303** medical/finance cohort caught a *systematic* under-specified-tag pattern in one creation batch: medical-symptom nouns (筋肉痛/動悸/息切れ/痙攣) tagged semantic `general` where `health` clearly fits (and matches the sibling 06298, which already carries `health`), plus 収益 tagged `work` where `finance` fits. **4 of 5 tag flags were applied** — these were treated as APPLY rather than the usual narrowness-REJECT because each is the *clearly-correct single-domain* case the 2026-06-18 curator-policy question carves out (exactly one specific domain unambiguous, and confirmed by a same-batch sibling already carrying the specific tag). This is a concrete data point for that open policy question — the lazy-default `general` here is not a deliberate fallback but a create-era batch artifact, and a `check_tag_drift`-style sweep keyed on "single-domain noun with sole `general` whose gloss/sibling implies one specific tag" would surface the rest of this 06298–06303 batch (and likely its neighbors) deterministically. The 収益→`finance` slice is wrong-category (P11), not under-specification.

**Update 2026-06-28 (the placeholder-`general` signature continues at the 06309–06340 frontier)**: A 2026-06-28 routine polish §4 self-check flagged `general`→`nature`/`tool` "too broad" on four concrete-noun frontier entries (06310/06311/06312 astronomy, 06315 stepladder); per the standing semantic-tag policy these are in-list→in-list narrowness nits and were **rejected**. But the observing run noted the underlying signature: the **06309–06340 frontier block carries `general`/`science` placeholder semantic tags on specific concrete nouns** — the same lazy-default create-era artifact as the 06298–06303 medical/finance batch above, just one band further on. As with that batch, a **curator-led bulk migration keyed on "single-domain concrete noun with sole `general`/`science`"** (not per-entry accuracy-review, which rejects these as narrowness nits) is the efficient fix; the per-run §4 lane cannot apply them under the current policy. Another data point for the open 2026-06-18 curator-policy question.

**Update 2026-06-29 (the placeholder-`general` signature continues into the 06323–06340 playground/gardening/car-parts cluster)**: A 2026-06-29 routine polish §4 self-check flagged `general` "too broad" on the **06323–06340** frontier cluster (playground equipment, gardening actions, car parts) — concrete single-domain nouns carrying a sole `general` semantic tag where one specific domain is unambiguous (playground equipment → `leisure`, gardening actions → `plant-general`). The cross-model reviewer flagged **06324–06328** specifically; per the standing semantic-tag policy these in-list→in-list narrowness substitutions were **rejected** in the run. But the cluster is the same create-era lazy-default signature as the 06298–06303 medical/finance and 06309–06340 astronomy batches above — one more contiguous band of the same artifact. The efficient fix remains a **curator-led bulk migration** (or a deliberate systemic-fix P13 pass with proper per-entry tag verification), not per-entry accuracy-review, which rejects these as narrowness nits under the current policy. Yet another data point for the open 2026-06-18 curator-policy question, now with a third concrete cohort (06298–06340) in evidence.

## Priority 14: Notes content copied from wrong entry

**Source**: Comprehensive-polish 2026-05-25 session 021 (entries 03491–03510)

Entry 03500_nakaba ({半|なか}ば) had a note reading "泥んこ = muddy, mud play" — content that clearly belongs to a nearby entry about mud, not to なかば (midway/halfway). The correct note content should reference 〜なかば usage patterns.

This is a different failure mode from semantic tag drift: the note *text itself* was copied from or generated for the wrong entry, possibly during a batch creation that interleaved entries. Worth scanning notes for obviously mismatched content (note text containing keywords that have no semantic connection to the headword or gloss).

**Detection**: No simple grep — this requires semantic comparison between note content and entry headword/gloss. A lightweight heuristic: extract English words from notes, compare against gloss keywords, flag entries with zero overlap. False-positive-heavy but could surface the worst cases.

**Suggested action**: Low priority as a batch — comprehensive-polish catches these case by case. Worth a targeted spot-check of entries in the same batch cohort as 03500 (roughly 03400–03600).

## Priority 15: `{ている}` furigana brace artifact in ASPECT notes

**RESOLVED (2026-06-10).** Routine systemic-fix session fixed all **49** entries: `{ている}` → plain `ている` in the `ASPECT (...)` section headers (the only context the artifact appeared in — all 49 hits were in `notes`, none in examples). Following the semantic-verification-first rule, each entry was opened and confirmed individually before saving, even though the transform is mechanically safe (`ている` is pure kana, so dropping the braces drops no reading); the `modified` timestamp was bumped on each. A furigana self-check screened the 49 changed IDs and returned 5 flags, **all rejected** as partial-reading false positives / model hallucinations unrelated to the edit (e.g. `捻|ねじ`, `逃|に` for 逃がす, `果|は` in 果てる). `python3 build/check_artifacts.py --issue teiru-brace --json` now returns 0; the `grep` detector below returns 0. Tracked as `artifact-teiru-brace` in `backlog-queue.json`.

**Source**: Comprehensive-polish 2026-06-01 session 003 (entries 04574–04594)

Multiple verb entries use `{ている}` (furigana brace syntax) instead of plain `ている` or `(ている)` in their ASPECT section headers or notes. The furigana brace syntax `{X|Y}` is intended for kanji with readings, not for hiragana-only strings. The wrapped `{ている}` is a template artifact from batch entry creation.

**Scope**: 49 entries confirmed across the entry set — concentrated in the 00000–00500 and 03500–04600 ranges.

**Detection**: `grep -rl '{ている}' entries/ | wc -l`

**Suggested action**: Simple regex replacement: `{ている}` → `ている` across all entries. Pure text substitution, no semantic judgment needed. Low risk.

## Priority 16: `[Register: Neutral]` legacy artifact in notes — RESOLVED 2026-06-10

**Source**: Comprehensive-polish 2026-06-01 session 003 (entries 04574–04594)

Multiple entries have `[Register: Neutral]` or similar `[Register: ...]` strings at the end of their notes field. These are template artifacts from batch creation — the register information should be expressed via the `formality` metadata field rather than as trailing text in notes.

**Scope**: 188 entries confirmed.

**Detection**: `grep -rc '\[Register: ' entries/ | grep -v ':0$' | wc -l`

**Resolution (2026-06-10)**: All 188 entries fixed in one systemic-fix Routine run. Per-entry verification confirmed all `formality` fields already carried the equivalent register info. Schema has no "polite" value (→ "neutral" is correct); "Casual" in trailer maps to "informal" in schema. Furigana self-check on all 188 IDs found 5 flags, all rejected as pre-existing false positives. Detector now reports 0.

## Priority 17: "formal" formality tag over-applied in early entries

**Source**: Cross-model accuracy-review session 001 (entries 00001–00200), 2026-06-09

The accuracy-review pipeline flagged `formality: "formal"` applied to neutral/everyday words across the early entry range (00016–00200). Words confirmed incorrectly tagged formal include: ボーイ (00016, waiter), 近頃 (00028, recently), 近々 (00029, soon), ドレス (00037, dress), 吹雪 (00040, blizzard), 普段 (00041, usually), 行事 (00078, event), 筆記 (00101, writing), 方々 (00116, various people), 格別 (00154, exceptional), 貸家 (00195, rental house), 各自 (00157, each person). Nine entries were corrected in the accuracy-review session; more are likely in the 00100–00500 range.

The pattern: early batch entry creation defaulted to `"formal"` for any word that was not obviously colloquial — treating "not slang" as equivalent to "formal." The correct value for most of these words is `"neutral"`. This is distinct from the politeness-tag mis-bucketing documented in Priority 7 (which concerns the `politeness` field about keigo system categories, not the `formality` field about register level).

**Scope**: Likely 00001–00500+. The accuracy-review started from entry 1, so the 00001–00200 sub-range is now partially cleaned.

**Detection**:
```bash
python3 -c "
import json, glob
for p in sorted(glob.glob('entries/0000*/*.json') + glob.glob('entries/0050*/*.json')):
    d = json.load(open(p))
    tags = (d.get('metadata') or {}).get('tags', {})
    if tags.get('formality') == 'formal':
        print(d['id'], d.get('headword',''), d.get('reading',''), d.get('gloss','')[:40])
" | head -40
```

**Suggested action**: Review all `formality: "formal"` entries in the 00001–00500 range and change to `"neutral"` where the word is used in everyday/neutral contexts. Requires semantic judgment, not a mechanical sweep — "formal" is genuinely correct for a small subset (legal terms, bureaucratic vocabulary). The accuracy-review mode is well-suited to this pass, since the cross-model signal helps distinguish genuinely formal vocabulary from over-tagged neutrals.

**Update 2026-06-10**: Cross-model accuracy-review session 002 (entries 00201–00450) extended the confirmed range. More neutral words tagged `formal`: 清い, なお, 年月, 日時, 稀. The pattern now spans at least 00016–00450, consistent with "early batch creation defaulted to formal for anything not obviously colloquial." The accuracy-review mode is fixing these as it advances through the low-ID range.

**Update 2026-06-15 (the pattern is not just low-ID)**: Two 2026-06-15 polish runs found `formality: "formal"` over-applied well beyond the early-entry range:
- **Everyday compound action verbs at the frontier**: 06135 突き飛ばす, 06136 投げ捨てる carry `formal` even though their own REGISTER notes say "Neutral." This is a distinct cohort from the early-batch low-ID entries — it suggests the `formal` default also contaminated the 06xxx compound-verb creation batch. Worth a `check_tag_drift`-style sweep over -飛ばす/-捨てる/-出す compound verbs (the contradiction between a `formal` tag and a "Neutral" REGISTER note is mechanically detectable).
- **05000–05300 register pocket**: widespread formality/politeness errors (茶漬け `politeness: honorific`, 羊羹 `formality: formal`) noted but left for a dedicated register-tag pass (see P11 Update 2026-06-15). The mechanically-detectable slice (tag contradicts the entry's own REGISTER note) is the natural systemic-fix candidate; the rest needs semantic review.

**Update 2026-06-18 (the inverse error — slang/colloquial neologisms tagged `formal`)**: A 2026-06-17 accuracy-review sweep over 6341–6540 found a distinct sub-family: casual/slang neologisms systematically mis-tagged `formality: formal` despite their own glosses labeling them slang — 陰キャ, 陽キャ, リア充, コミュ障. This is the same "default landed on `formal`" artifact as the early-entry over-tagging above, but applied to vocabulary that is the *opposite* of formal, so it is more clearly wrong (gloss contradicts the tag). Like the 06135/06136 "Neutral REGISTER note vs `formal` tag" case, the mechanically-detectable slice is **gloss/notes contain a slang/casual marker while `formality == formal`** — a high-precision detector signal worth adding to a register-tag drift check. The accuracy-review `tags`/formality pass catches them when it reaches the range; they cluster in the 6157–~7000 neologism-heavy band.

**Update 2026-06-18 (second — casual particles/fillers/idioms too)**: A 2026-06-18 accuracy-review sweep over 6840–6925 extended this inverse-error family beyond neologisms to **casual sentence-final particles, fillers, and idioms** mis-tagged `formality: formal` — ぞ, なんて, やっぱ, よね, かしら, っていう, えーと. These are register-defining *casual* markers, so the `formal` tag is the maximally-wrong value; the same gloss/notes-slang-marker-vs-`formal` detector slice catches them (a sentence-final particle or filler glossed as colloquial/casual should never carry `formal`). Confirms the artifact runs the full length of the 6157–6925 contaminated band, not just its neologism pockets.

**Update 2026-06-28 (a third sub-family — verb-suru entries carrying a template-default `formal`)**: A 2026-06-27 routine polish run (frontier 06304–06308) found **06307 仲直りする** tagged `formality: formal` even though the entry's own notes explicitly say it is **NOT** for formal/diplomatic contexts and all its examples are casual — the cross-model §4 self-check (Gemini) flagged it independently. This is the verb-suru analogue of the early-entry over-tagging above: the creation template appears to have defaulted **verb-suru** entries to `formal`, contradicting everyday/casual usage and the entries' own register notes. The mechanically-detectable slice is the same family as the 06135/06136 case — **`formality == formal` while the entry's own REGISTER/notes prose describes neutral/casual use** — so a targeted formality audit of `verb-suru` entries tagged `formal` against their notes/examples would likely surface many mislabels. Folds into the accuracy-review `tags`/formality pass; no dedicated sweep needed unless the verb-suru cohort proves dense.

## Priority 18: "descriptive" semantic tag over-applied as a catch-all

**Source**: Cross-model accuracy-review session 002 (entries 00201–00450), 2026-06-10

A new tag-drift mode distinct from the wrong-specific-tag (P11) and the
sole-`general` under-specification (P13) patterns: the `semantic: ["descriptive"]`
tag is being applied broadly to words it doesn't characterise — confirmed on 謙虚
(humble), 懸命 (earnest), 無限 (infinite), もしかすると (perhaps), 自ら (oneself).
The reviewer reads `descriptive` as meaning "this word can describe something,"
which is true of almost any adjective or adverb and therefore carries no
classifying information. It has become a second catch-all alongside `general`.

This is partly a *correct* destination tag — mimetic adverbs genuinely are
`descriptive` (P11 updates routinely retag じとじと/のそのそ to `descriptive`), so
the value is not itself wrong. The problem is that it is applied as a default to
abstract/grammatical words where a more specific or simply *no* domain tag fits
better. The underlying issue is that `descriptive` is under-defined: the tag
vocabulary doesn't state what semantic content it asserts. See
[Schema Tag Reliability](../topics/schema-tag-reliability.md) → "Stale auto-labels"
for the analysis and the proposed criterion (reserve `descriptive` for mimetics
and manner/quality words; do not use it for abstract nouns, grammatical words, or
words that already have a real domain).

**Detection**: No clean grep — like P11, this needs the headword-vs-tag judgment
the accuracy-review `tags` dimension provides. A first-pass audit aid: list
entries whose only semantic tag is `descriptive` and whose POS is noun or
grammatical, which surfaces the clearest mismatches.

**Suggested action**: Lower urgency than P11/P17 — fold into the accuracy-review
`tags` pass rather than a dedicated sweep. When reviewing, replace a stray
`descriptive` on an abstract/grammatical word with the right domain tag, or drop
it in favour of `general`.

## Priority 19: Noun examples that never contain their headword

**Source**: Curator review of 00472 仕様 (2026-06-10) + systematic scan

The curator-flagged case: 00472 仕様 (しよう) carried the example
こんなに{壊|こわ}れたら{直|なお}しようがない — but 直しようがない is
直し + よう(様) + がない; the string しよう only appears **across a morpheme
boundary**. The example taught the wrong word. (A second example in the same
entry showed どうしようもない, its own lexeme at 18862.) Both replaced
2026-06-10 with genuine 仕様がない／…の仕様がない examples.

A systematic scan (`build/check_example_headword.py`, read-only) of entries
whose POS is exactly `noun` and whose headword contains kanji found **143
suspect examples in 94 entries**, in two tiers:

- **reading-only** (14): the kana reading appears but the kanji form doesn't.
  Either a cross-boundary misparse (the 仕様 case) or legitimate kana
  orthography (ごちそう for ご馳走, おむすび for お結び) — per-entry judgment.
- **headword-absent** (129): neither form appears. The example may illustrate a
  related compound (東経 in the 経度 entry), a verb form of the nominal
  (仕組まれた in the 仕組み entry, 炙って in 炙り), a suffix usage (犯罪歴 in
  the 歴史 entry, 食べ方 in the 仕方 entry), or simply the wrong word
  (目玉焼き in the 卵 entry).

**Detection**: `python3 build/check_example_headword.py --summary` (or `--json`
for the systemic-fix review queue).

**Suggested action**: systemic-fix batches with per-entry verification. Replace
each bad example with a genuine example of the headword (full inline links), or
delete it when the entry has examples to spare; skip legitimate kana-orthography
cases. Queued as `example-headword-missing` in `backlog-queue.json`.

**Status 2026-06-14 (clean-entry frontier exhausted, `batch_ready` → false)**:
The 2026-06-14 routine run adjudicated all 31 then-flagged entries (53 examples)
and found only **one** genuine fix (00472-style verb-form misparse): 22875 出回り
had a verb example (出回る) replaced with the noun collocation 出回りの時期. Every
other flagged entry is now either (a) U+FFFD-corrupted, which the detector
mis-flags because the kanji headword is mojibake — these are owned by
**tooling-backlog #16** (the replacement-character repair pass), or (b) a
legitimate detector false positive: kana/katakana orthography of the headword
(ごちそう, おむすび, ヤギ, シミ, カツオ, カキ, しわ寄せ), documented compound forms
(退職届/婚姻届 in 届け), the radical sense (うかんむり in 冠), or a ～-prefix headword
(〜時) whose plain-kanji examples the matcher can't bind. So `batch_ready` is set
false: genuine cases now hiding behind mojibake will re-surface for this lane only
after tooling-backlog #16 repairs the corrupted text.

## Priority 20: Out-of-taxonomy semantic tags (post-expansion migration)

**Source**: Curator tag-policy decision 2026-06-11 (see
[Schema Tag Reliability](../topics/schema-tag-reliability.md) → "The
tag-vocabulary contradiction and its resolution")

A 2026-06-11 audit found 17,762 semantic-tag instances across 1,204 distinct
tags outside `VALID_SEMANTIC` — the root cause of the contradictory tag
adjudications in the first Routine v2 runs. The taxonomy was expanded with 30
established categories (≥100 uses each), legitimizing ~49% of those instances.
What remains to migrate (measured at expansion time): **9,036 instances across
7,292 entries**.

- **Near-duplicates with 1:1 targets** (~2,060 instances): `time`→`time-general`,
  `people`→`person`, `social`→`society`, `description`→`descriptive`,
  `medical`/`medicine`→`health`, `transport`→`transportation`,
  `animals`→`animal-general`, `economy`→`economics`. The detector suggests the
  target; still verify per entry (a word tagged `medical` may be better served
  by `body-internal`, etc.).
- **Long tail** (~7,000 instances, 1,160+ distinct tags, 889 of them used <5
  times): no automatic target — choose the best `VALID_SEMANTIC` tag per entry.

**Detection**: `python3 build/check_tag_drift.py --check unknown-semantic
--summary` (or `--json` for the systemic-fix review queue; each record carries
the offending tag and, for near-duplicates, the suggested target).

**Suggested action**: systemic-fix batches with per-entry verification,
starting with the 1:1 near-duplicates (highest confidence). The
accuracy-review mode also drains this organically — reviewer prompt v3 flags
out-of-list tags with suggested in-list replacements, and the standing
adjudication rule (routine2.md §A) is to apply them. Queued as
`unknown-semantic-tags` in `backlog-queue.json`.

**Update 2026-06-21 (the drift extends to a dense 7815–8037 block — a new
creation cohort, 73% out-of-taxonomy)**: A 2026-06-21 accuracy-review run over
**7815–8037** ran a deterministic scan against `build/validate_tags.VALID_SEMANTIC`
and found **163 of 223 entries (73%)** carrying at least one out-of-taxonomy
semantic tag — a far higher density than the 01490–06925 batch P11 documents, and
a different creation cohort (the 7000–8500 band appears to share a free-form
tagging origin, distinct from the 2026-04-14 claude-opus-4-5 batch). The run
migrated only the **43** that the cross-model accuracy reviewer flagged at `error`
severity (architecture/house→building, social/speech→communication,
economy→economics, progress / 'change of state'→change); **120 entries still carry
invalid tags.** The drift families are large and mostly **1:1-mappable**, so this
is **systemic-fix territory, not per-run accuracy-review** (the reviewer surfaces
only a fraction per pass and at high adjudication cost; the deterministic detector
is the scalable instrument):
- **Free-form domain words** (no current 1:1 entry in the migration map):
  `career`, `lifestyle`, `place`, `document`, `accommodation`, `commerce`,
  `accounting`, `employment`, `logistics`, `personnel`.
- **Underscore/space variants**: `daily_life` / `daily life` → `daily-life`;
  `Japanese_cuisine` / `Japanese cuisine` → drop (entries already carry `food`).
- **Body/health splits**: `body` → `body-part`, `sleep` → `health`,
  `injury` → `health`.

**Recommended next action**: expand `build/check_tag_drift.py`'s migration map
(Tooling item 6) to cover these families, commit it, then run a
deterministic+spot-checked systemic-fix sweep over the whole 7815–8037 block **and
the adjacent ~7000–8500 creation cohort** that appears to share the origin. This
is the highest-yield migration target measured to date and is queued under the
existing `unknown-semantic-tags` backlog item.

**Update 2026-06-21 (the cohort continues unbroken into 8038–8237 — even denser)**:
A 2026-06-21 accuracy-review run over **8038–8237** (cross-model-review cursor;
phase furigana) ran the same deterministic `VALID_SEMANTIC` scan and found **177
of 200 entries (88%)** carrying ≥1 out-of-taxonomy semantic tag — **305 instances
across 162 distinct out-of-list tags** — confirming the free-form creation cohort
extends contiguously from 7815 through at least 8237 and is *denser* here than the
7815–8037 block (88% vs 73%). New distinct families seen this block beyond those
already enumerated: `loanword`, `household`, `instrument`/`equipment` (→`tool`/`music`),
`competition`, `office`/`stationery`/`documents`/`writing`, `kitchen`/`ingredient`/
`food-preparation`, `perception`/`clarity`/`meaning`/`vision` (→`cognition`),
`gardening`/`agriculture`/`plants` (→`plant-general`), `anatomy` (→`body-internal`),
`body` (→`body-part`/`health` per sense). The run migrated only a **14-entry
hand-verified slice** of the highest-confidence near-duplicates (per-entry verified,
logged in `reviews/decisions.jsonl`) and **deferred the ~240-instance long tail to
the systemic sweep** — reconfirming this is systemic-fix territory, not per-run
accuracy-review. The recommended 7000–8500 sweep should now be scoped to **at least
7815–8237** (and likely the full 7000–8500 band).

**Update 2026-06-23 (dict-wide scale quantified; the long tail has no 1:1 target and is
now being mass-escalated)**: Two findings sharpen the scope and the remedy.
- **Dict-wide count**: as of 2026-06-22, `check_tag_drift.py --check unknown-semantic`
  reports **8,698 unknown-semantic flags** dictionary-wide. A 2026-06-22 routine polish
  observation spot-measured **8459–8632 at ~95 of 174 entries (55%)** carrying
  non-`VALID_SEMANTIC` tags (ability, medical, kitchen, baseball, psychology, train, …) —
  the free-form creation cohort continues unbroken above 8237.
- **The long tail is judgment-dependent, not mechanically mappable**: a 2026-06-23
  accuracy-review over **8633–9239** found **496 not-in-list semantic tags across 323 of
  607 entries (~180 distinct off-list names**: positive, body, medical, object, aesthetics,
  quality, psychology, concept, childcare, …). Critically, `check_tag_drift`'s
  `unknown-semantic` map returns `-> None` for nearly all of them (no 1:1 target), so they
  need **per-word judgment, not a mechanical migration**. That run applied **102
  provably-safe 1:1 migrations** (plural/synonym/strict-subdomain: emotions→emotion,
  train→transportation, medical→health, etc.) across 91 entries and **escalated 394
  judgment-dependent tags across 288 entries to the curator/systemic-fix lane** (logged in
  `reviews/decisions.jsonl`). Combined with the 2026-06-21 240-flag escalation, the
  decision ledger now carries **635 flags →curator this metrics window** — the first
  large escalation event in the project (all-time →curator was 16 before 2026-06-21).

**Recommended next action (updated)**: the per-run accuracy-review budget cannot drain an
8,698-flag dict-wide backlog one ~600-entry range at a time, and the bulk of it has no 1:1
map. This needs (a) a **dedicated systemic-fix/curator pass with an expanded *curated*
migration table** (more than the deterministic 1:1 families now in `check_tag_drift.py`),
and (b) **promoting unknown-semantic from a `validate_tags.py` warning to a CI error /
pre-commit gate** so new entries stop adding to the backlog (see
[Tooling Backlog](tooling-backlog.md) → item 27). Without (b), the systemic-fix pass drains
a backlog that new-entry creation keeps refilling.

**Update 2026-06-24 (the free-form cohort continues unbroken into 9240–9456)**: A 2026-06-23
accuracy-review over **9240–9456** ran the deterministic `VALID_SEMANTIC` scan and found
**~121 of 217 entries (56%)** carrying out-of-list semantic tags — confirming the pre-March
general-tier creation cohort runs contiguously above 9239 at the same ~55% density. The run
**migrated the 35 error-severity-flagged entries** to in-list tags (5 track-and-field events
`leisure`→`sports`; `place`/`manner`/`behavior`/`location`/`physical-state`→best in-list) and
left **~86 entries still carrying out-of-list tags** (top residual offenders: `location`×11,
`behavior`×10, `urban`×5, `state`/`manner`/`social`/`place`/`degree`×4 each). The observing
run reiterates the standing recommendation: a **dictionary-wide `check_tag_drift` sweep over
the whole pre-March general range** would clear this far faster than per-range accuracy-review,
which migrates only the error-severity flags it surfaces each pass. This is the same
`unknown-semantic-tags` backlog item; the per-run accuracy-review lane is keeping the frontier
honest but cannot drain the dict-wide 8,698-flag backlog one ~200-entry range at a time
(reinforces the [Tooling item 27](tooling-backlog.md) CI-gate sequencing).

**Update 2026-06-25 (the cohort reaches a denser daily-life/errands sub-batch at ~9657–9740)**: A 2026-06-24
routine polish run reported a distinct, even-denser pocket of the same free-form creation cohort: the
**~09689–09740 daily-life/errands batch** (delivery, dining, medical, housing, mobile themes) was created with an
ad-hoc out-of-taxonomy semantic vocabulary, and **48 of 84 entries in 9657–9740 (57%)** carried invalid tags —
`daily_life` underscore form plus `restaurant`/`delivery`/`medical`/`housing`/`payment`/`service`/`lifestyle`/
`real_estate`/`device`/`phone`. The run migrated that batch to the controlled vocabulary, but the observing run
flagged that **adjacent ID ranges from the same thematic creation batch likely carry the same drift** and
recommended a confirming `check_tag_drift.py --check unknown-semantic` sweep over **9600–9800**. This is the same
`unknown-semantic-tags` backlog item — a further data point that the pre-March general-tier cohort is themed in
contiguous blocks (each errands/daily-life sub-batch shares one ad-hoc tag vocabulary), which is exactly the shape
a dictionary-wide `check_tag_drift` migration (vs. per-range accuracy-review) is best suited to drain.

**Update 2026-06-26 (the daily-life/errands cohort continues into 9741–9814; and a *new* shopping/tech cohort at 9815–9849)**: Two more themed sub-batches of the same pre-March free-form creation cohort were measured and migrated this window:
- A 2026-06-25 accuracy-review over **9741–9814** found **14/70 entries (20%)** carrying out-of-list tags, concentrated in two themed blocks — subscriptions/services/promotions at 9741–9748 (`subscription`, `service`, `promotion`, `restaurant`, `facility`, `daily_life`-underscore) and civil-paperwork at 9809–9814 (`administrative`, `documents`, `moving`, `stationery`, `legal`, `housing`, `smartphone`); all migrated to `VALID_SEMANTIC` this run.
- A 2026-06-26 new-entries run reported a **distinct, denser shopping/tech cohort at 9815–9849** (recently-created vocabulary) with **21/35 entries (60%)** carrying off-list tags (`smartphone`, `internet`, `marketing`, `retail`, `housing`, `bathing`, `delivery`, `service`, `medicine`, `environment`, `contract`); all 21 migrated to in-list tags in that run. The observing run recommends sweeping the surrounding range **and adding a note to the new-entry skill**, since entry creation in this period kept reaching for an off-vocabulary tag set.

These reconfirm the cohort's defining shape — **contiguous, theme-named sub-batches each sharing one ad-hoc tag vocabulary** — and that per-range migration keeps the frontier honest but cannot drain the dict-wide backlog (see the enforcement note below for why fresh inflow is now gated). The recommended single systemic-fix `check_tag_drift.py --check unknown-semantic` sweep over ~9600–9850 still stands.

**Update 2026-06-26 (enforce-side shipped — the off-vocab ratchet now blocks *new* drift in CI)**: A 2026-06-25 tooling-fix session closed the inflow half of this problem (the [Tooling item 27](tooling-backlog.md) sequencing). `validate_tags.py` previously only *warned* on out-of-`VALID_SEMANTIC` tags and CI ran only `validate.py` (schema), so the cohort passed CI silently. The session re-measured the live dict-wide scope at **8,267 instances / 6,759 entries / 1,109 distinct tags** and added a **baseline ratchet** — `build/data/unknown_semantic_baseline.json` + `validate_tags.py --check-no-new-unknown`, now a CI step — that fails only when an entry introduces a *new* off-vocab tag, leaving the legacy tail to the gradual accuracy-review/systemic-fix migration. Regenerate the baseline after each migration batch with `--write-unknown-baseline`. This is the partial-and-correctly-sequenced form of Tooling item 27: a hard *error* on the whole legacy tail would block legitimate work on 6,759 existing entries, so the ratchet gates inflow now and the full error-gate flip waits on the curated-migration drain. Documented in [Schema Tag Reliability](../topics/schema-tag-reliability.md). No mass content migration was done in that session — that stays the gradual lane's job.

**Update 2026-06-28 (the free-form cohort reaches the 10400–10700 band — and the reviewer misses ~9 even where it migrates 64)**: Two 2026-06-27 accuracy-review observations push the mapped cohort far above the previously-documented ~9849 ceiling, into the **10xxx** general-tier batch:
- A **10469–10527** sub-batch (created onomatopoeia/adverbs/adjectives) carries an ad-hoc out-of-taxonomy vocabulary — `texture-quality`, `degree-extent`, `emotion-feeling`, `action-physical`, `manner-style`, `quality-evaluation`, `state-change` — with **~50 of 100 entries in 10450–10549** carrying a tag not in `VALID_SEMANTIC`. The accuracy-review migrated this range; adjacent batch blocks (10550+ and similar) very likely share the density.
- A **10550–10715** accuracy-review caught off-vocab tags well (**64 migrated**) but **missed ~9 in the same range** — `emotion-feeling` on 10587/10594/10629/10630, `social` on 10636/10661, `marriage` on 10617, `culture-tradition` on 10691, `action-physical`/`position` on 10613. This is the key new diagnostic: **the reviewer-driven mode leaves a residue even in ranges it has "reviewed,"** so the deterministic `check_tag_drift.py --check unknown-semantic` sweep is still needed to clear unflagged off-vocab drift in nominally-reviewed ranges, not just ahead of the frontier. Reinforces the standing recommendation (a dict-wide deterministic sweep + the [Tooling item 27](tooling-backlog.md) CI gate) over per-range accuracy-review, and confirms the contiguous free-form creation cohort runs at least through 10715. Same `unknown-semantic-tags` backlog item.

**Update 2026-06-28 (the cohort reaches the 10700–11000 katakana/slang/loanword block — a dense, contiguous pocket worth a single scoped sweep)**: Two 2026-06-28 accuracy-review observations push the mapped cohort up another ~300 IDs and pin down a concentrated cluster:
- A **10716–10887** accuracy-review found **45 of 67 tag flags** were off-vocab semantic tags on the 10700–10800 katakana/slang/loanword block (`housing-architecture`, `discourse-connector`, `food-sweets`, `shopping-product`, …) — entries created with a richer-but-off-list tag vocabulary; all migrated. The `general`-too-broad family (12) and formality flags (2) were the usual reviewer noise (rejected), and furigana screening was 0/9 (rendaku/okurigana/alt-reading FPs).
- A **10888–10947** range (spot-measured during a furigana phase) carried off-taxonomy tags on **25 of 60 entries** in a tight 10905–10934 pocket — a **2026-02 creation batch by claude-opus-4-6** with a pre-taxonomy vocabulary: `abstract-concept`→abstract ×9, `people-personality`→personality ×6, `food-ingredient`/`food-dish`/`food-fruit`→food, `nature-plant`→plant-general, `nature-geography`→geography, `place-description`/`people-description`/`body-action`→descriptive/action, `commerce`→business, `group`→society, `reasoning`→cognition, `time`→time-general; all migrated this window.

Together these confirm the free-form cohort runs contiguously through at least **10947**, with the 10700–11000 band a particularly dense, mostly-1:1-mappable katakana/loanword pocket. Both observing runs recommend **a single scoped `check_tag_drift.py --check unknown-semantic` sweep over 10700–11000** rather than chipping at it 25–67 entries per accuracy-review pass — the same `unknown-semantic-tags` backlog item, and another data point that per-range review keeps the frontier honest but cannot drain the dict-wide backlog (reinforces [Tooling item 27](tooling-backlog.md)).

**Update 2026-06-30 (the cohort reaches the 11300s 不-/中-/下-/両- compound band)**: A 2026-06-30 accuracy-review run pushed the mapped cohort into the **11300s**, where the off-vocab drift clusters in negative/positional kanji-prefix compounds (不-, 中-, 下-, 両-). The recurring families are mostly **1:1-mappable**: `quality`→`descriptive`, `position-direction`→`direction`, `people`→`person`, `place`→`geography`, plus one-offs (`information`→`cognition`, `emotion-feeling`→`emotion`, `rank`→`society`, `nature-water`, `time-manner`). The run migrated the genuine cluster (**24 applied / 11 rejected** — the rejects are the in-list `general`-too-broad narrowness family, Tooling item 17). The observing run reiterates the standing recommendation: fold these families into `check_tag_drift.py`'s migration map (Tooling item 6) and clear the band with a deterministic `--check unknown-semantic` sweep rather than the monthly per-range accuracy-review cadence — same `unknown-semantic-tags` backlog item, another data point that the free-form/off-vocab cohort runs contiguously well above 11000.

**Update 2026-07-01 (the cohort reaches the 11500s — a dense ~Feb-2026 claude-opus-4-6 batch)**: A 2026-07-01 accuracy-review run over **11515–11553** found **26 of ~72 entries** carrying at least one tag absent from `VALID_SEMANTIC` — a finer, more granular off-taxonomy tag set than the earlier bands, pointing to the same early batch-creation era (~Feb 2026, `ai_model: claude-opus-4-6`) already documented at 10905–10934. The offending tags were an over-specified hyphenated vocabulary: `action-physical`, `action-consumption`, `action-addition`, `action-repair`, `event`, `sensation`, `work-process`, `deception`, `crime`, `sign-indication`, `quantity-comparison`, `quantity-change`, `religion-buddhism`, `religion-philosophy`, `person-occupation`, `status-rank`, `quality-aesthetic`, `quality-positive`, `cause-reason`, `origin`, `space-room`, `economics-price`, `business-operation`, `politics-diplomacy`, `location`, `behavior`, `attitude`. All migrated 1:1 to in-list tags this run (`action-*`→`action`, `religion-*`→`religion`, `quality-*`→`descriptive`, `person-occupation`→`occupation`, `location`→`geography`, `behavior`/`attitude`→`descriptive`, etc.). The observing run recommends a **targeted systemic-fix sweep over 11500–12500** with `build/validate_tags.py --check-no-new-unknown`, since this granular hyphenated tag set is likely shared across the surrounding claude-opus-4-6 batch. Same `unknown-semantic-tags` backlog item; another data point that the free-form/off-vocab cohort runs contiguously well above 11300, and that its tag vocabulary shifts by creation batch (the 11500s batch used compound `noun-subtype` names rather than the free-form domain words seen lower down).

## Priority 21: Unlinked 自動詞/他動詞 labels and particles in compound-verb notes

**Source**: 2026-06-11 comprehensive-polish session (entries 06038–06047)

Compound verb entries created in the ~2026-04-10 batch era (06038+ range) have a
systemic inline-link gap distinct from the general P1 unlinked-notes pattern.
Three sub-patterns:

1. **Unlinked transitivity labels**: `{自動詞|じどうし}` and `{他動詞|たどうし}` in
   TRANSITIVITY lines are furigana-wrapped but not enclosed in `⟦...⟧` inline-link
   wrappers. These should be `⟦{自動詞|じどうし}→自動詞：xxxxx⟧` pointing to the
   entry for 自動詞 or 他動詞.
2. **Unlinked particles**: Particles (を、が、から、に、で) in `Pattern:` bullets are
   bare rather than wrapped as `⟦を→を：xxxxx⟧`.
3. **Unlinked content words**: Content words in `COMMON PATTERNS` bullets lack both
   content-word links and particle links.

The same sub-patterns appear at lower ID ranges (confirmed: 00735_naoru, 00739_oboeru range) —
P1's inline-links polishing task will eventually reach them, but the 06038+ cohort
is beyond its current frontier and will not be addressed for months under sequential
processing.

**Broader context (2026-06-12)**: The 06048–06067 polish session found the **general** inline-link gap is even wider — the 06000 range batch was created before inline-link polishing was standard practice, so many entries in this cohort have no `⟦...⟧` markup in either examples or notes, not just the three specific sub-patterns enumerated above. The P21 sub-patterns are the most systemic-fix-amenable slice (they occur in a predictable structural location); the general inline-link absence is the broader P1 problem for this cohort and will be addressed as comprehensive-polish advances through the 06000 range.

**Scope**: Likely affects hundreds of compound verb entries in the 06000–09000 range
(the 2026-03 through 2026-04 creation cohort). The tooling-backlog item 15
(`check_artifacts.py` lint rule for unlinked 自動詞/他動詞) would establish the
exact count.

**Update 2026-06-14**: The 06121–06128 frontier polish session confirmed the
general inline-link absence reaches the 06120s — all eight cultural-vocabulary
nouns (火鉢, 掛軸, 手拭い, 硯, お中元, お歳暮, 香典, 送料) had **zero** `⟦...⟧` links in
both examples and notes. This is the noun-cohort counterpart of the compound-verb
gap above (same pre-inline-link-polishing creation batch). The same session also
surfaced a distinct **malformed-link sub-pattern** in the low-ID priority-lane
entries it polished (00391, 00717, 01312, 00908, 00478, 00964): inline-link **base
forms carry leftover furigana** — e.g. `⟦花→{花|はな}：xxxxx⟧` where the base after
the arrow should be bare kanji (`⟦花→花：xxxxx⟧`). Furigana belongs only on the
*surface* form before the arrow; a base form with `{...|...}` braces will not match
the `word_id_lookup.json` key and breaks the lookup. This is a different defect
class from the P9 furigana-wrapper anomalies (it is in the link *target* segment,
not the furigana wrapper) and would be cheap for a detector to catch: scan for
`→` followed by `{` inside a `⟦...⟧` span.

**Update 2026-06-15**: The general inline-link absence continues to track the
comprehensive-polish frontier — the 06129–06132 consumer/business suru-noun cohort
and the 06137–06149 idiom/proverb/yojijukugo cohort both had **zero** `⟦...⟧` links
in examples and notes (same pre-inline-link-polishing creation batch). A new
**base-form orthography sub-pattern** also surfaced: entries created by
**claude-opus-4-6** (e.g. 00740 oishii) use the **hiragana reading** as the inline-link
base form (`⟦魚→さかな：xxxxx⟧`) instead of the kanji headword (`⟦魚→魚：xxxxx⟧`). Unlike
the furigana-in-base-form malformation above, this one is **cosmetic only** — the
links still resolve via `word_id_lookup.json` (which keys on both readings and
headwords) — but it is inconsistent with the kanji-base convention and a detector
could normalise it (scan for a `→` followed by all-hiragana before `：` where the
surface form contains kanji).

**Update 2026-06-16**: A 2026-06-15 routine polish observation re-confirmed the
idiom-cohort gap with a concrete instance — the yojijukugo/proverb entries in the
**06143–06149** range (created Jan 2026, e.g. 06143_oninikanabou 鬼に金棒) carry
**zero** `⟦...⟧` links in either examples or notes (naked Japanese throughout). This
is the same pre-inline-link-polishing creation batch as the 06137–06149 cohort noted
above, so the whole 06140s idiom block should be backfilled together. The idiom cohort
differs from the compound-verb/noun cohorts only in that its notes carry fewer
structured TRANSITIVITY/Pattern lines, so the backfill is mostly example-sentence and
free-prose links rather than the P21 sub-pattern labels.

**Update 2026-06-17**: A 2026-06-16 routine polish session began backfilling the
06140s idiom cohort by hand — full inline-link coverage was added to **06147, 06148,
06149** (idioms/proverbs) and **06150** (コーディング) in that run. **06151 onward in
the same pre-inline-link creation batch remain pending.** This confirms the backfill
is tractable per-entry (mostly example-sentence and free-prose links, few P21
sub-pattern labels, as predicted in the 2026-06-16 update) but that sequential
hand-polishing will be slow over the whole 06140–06170+ block; the detector (Tooling
item 15) is still the prerequisite for a systemic-fix batch.

**Update 2026-06-18**: Two 2026-06-17 routine polish runs continued the hand-backfill at
the frontier and re-confirmed the gap reaches the loanword/suru-noun cohort above the
idiom block: **06154–06156** (loanword + 出社/退社 cluster) and **06157–06160** had
**zero** `⟦...⟧` links in examples *and* notes. The example links were added per-entry in
those runs, but the dense glossary-style notes (COMPONENTS / CONTRAST WITH RELATED TERMS /
COMMON COLLOCATIONS sections + loanword synonym lists) of the 06157+ batch remain
unlinked — and partly `noentry` (loanword synonyms). Notable: **06156 was modified
2026-06-16 yet still had no links**, so a prior touch advanced the entry without adding
inline links — i.e. the gap is not self-healing through ordinary polishing. The whole
06150–06170+ band is the same pre-inline-link 2026-01-17 creation batch; a dedicated
inline-link sweep focused on the *notes* glossaries (the heavy, partly-noentry part) is
the remaining work after examples are linked. Still gated on the Tooling item 15 detector
for a systemic-fix batch.

**Update 2026-06-18 (second — the 〜的 cluster, and the Jan-2026 band hypothesis)**: A
2026-06-18 routine polish run reached the **06169–06176 〜的 adjective/adverb cluster**
(実質的, 比較的, 定期的, 段階的, 総合的, 保守的) and found it created in **January 2026 with zero
inline-link coverage in examples *or* notes** — it predates the inline-link polishing step
entirely. This is the same pre-inline-link cohort as the 06150–06170 band above, now
confirmed to continue through the 06176 〜的 sub-cluster. The working hypothesis from the
observing run: as the sequential frontier climbs into the Jan-2026 creation band, **most
06000–07000 entries will need full tier-1 inline linking** (examples *and* notes), so the
inline-link gap is the dominant remaining tier-1 deficit for the whole 06xxx frontier — not
an occasional miss. Argues for either a dedicated inline-link sweep of 06150–07000 or
budgeting extra inline-link time into each frontier polish run until the band is cleared.

**Update 2026-06-19**: Two 2026-06-19 routine polish runs carried the frontier through
the next slice of the same Jan-2026 pre-inline-link band: **06177–06183** (onomatopoeia
adverbs + tech loanwords) and **06184–06189** both had **zero** inline-link coverage in
examples *and* notes — and crucially **despite some recent `modified` timestamps** in the
06177–06183 block, confirming again (cf. 06156 in the second 2026-06-18 update) that the
gap is **not self-healing through ordinary polishing**: an entry can be touched without
its links being added. Both observing runs reached the same conclusion — a large
pre-inline-link cohort sits unbroken between the sequential polish frontier (now ~06190)
and ~07000, and the per-entry hand-backfill at the frontier is doing genuine net-new work
(no duplication of prior polish) but cannot outpace the band's width. **Recommendation
restated with more force**: a dedicated inline-link sweep of the whole ~06150–07000 band
(examples *and* the heavy notes glossaries) is the right shape of work, still gated on the
Tooling item 15 detector for a verified systemic-fix batch.

**Update 2026-06-20**: Two 2026-06-20 routine polish runs carried the frontier through
the next contiguous slice and re-confirmed the band is **unbroken**: **06190–06196**
(nouns/proverbs, Jan-2026) and **06204–06209** (general nouns 車掌/序文/付録/栄養素/炭水化物/太陽光)
both had **zero** `⟦...⟧` links in examples *and* notes despite being otherwise
schema-valid and furigana-complete — the gap is purely inline-link coverage, not a
content defect. Both runs hand-linked their frontier entries (06194 was also pointed at
01385_kimochi, the surviving 気持ち sense). Crucially, the **priority/notes.txt lane ran
6/6 no-op in the same session** (basic-tier particles/adjectives already fully linked),
so the notes-quality ranking is pointing away from the real frontier deficit: the
binding tier-1 gap on the 06xxx general-tier frontier is inline-link coverage (this
P21 band), not note quality. The unbroken zero-link band is now confirmed from ~06150
(idiom cohort) through **06209** without interruption — reinforcing the dedicated
~06150–07000 inline-link-sweep recommendation (still gated on the Tooling item 15 detector).

**Update 2026-06-21**: Two 2026-06-21 routine polish runs carried the frontier
through **06210–06213** (compound verbs すりおろす/誘い込む/殴り倒す, created 2026-01-17,
last touched 2026-04-10 by claude-opus-4-5) and into the **06214+ proverb/yojijukugo
block** — both had **zero** `⟦...⟧` links in examples *or* notes, again **despite
06214+ carrying recent (2026-06-16) `modified` timestamps** (those bumps were not
comprehensive polish — the same not-self-healing signature as 06156 and the
06177–06183 block in prior updates). Both runs hand-linked their frontier entries.
The unbroken zero-link band is now confirmed continuous from ~06150 through
**06214+** without interruption. One observing run added a sharper recommendation:
the whole 06200–06250 band (compound verbs + four-character idioms/proverbs)
predates the inline-link polishing step and should be backfilled as a block; the
furigana and structure are otherwise clean, so the work is purely link coverage.

**Update 2026-06-22**: A 2026-06-21 routine polish run carried the frontier through
**~06222–06230** and re-confirmed the band is still unbroken: these entries were
created with **zero** inline links in examples *and* with **`・` (nakaguro) bullets**
in their notes lists (the older bullet convention, in place of the current
`⟦...⟧`-linked list items). The frontier lane is fixing these one block at a time as
it advances. The nakaguro-bullet detail is the same pre-inline-link-polishing creation
signature already documented across 06150–06214 — the band now runs unbroken from
~06150 through **06230**. No new diagnosis; the dedicated ~06150–07000 inline-link
sweep recommendation (still gated on the Tooling item 15 detector) stands.

**Update 2026-06-23**: Two routine polish frontier lanes (2026-06-22 over **06231–06236**
and 2026-06-23 over **06241–06246**) carried the band further: the 06231–06236 cohort
(nouns) and the 06241–06244 〜的 na-adjectives + 06245–06246 four-character idioms all
shipped with **zero** `⟦...⟧` links in examples *and* notes despite otherwise-complete
content (good notes, cross-refs, conjugation). Both runs hand-linked their frontier
entries. The unbroken zero-link band is now confirmed continuous from ~06150 through
**06246**. Same diagnosis, same recommendation: the sequential frontier lane is where the
real link backlog lives, and a one-off bulk inline-link sweep of the 06000+ general range
(still gated on the Tooling item 15 detector) would clear it far faster than per-entry
frontier polishing.

**Update 2026-06-26 (the band now reaches the 06270s mimetic/keigo cohort — and it is not just onomatopoeia)**: A 2026-06-25 routine polish run flagged that the **06271+ mimetic/onomatopoeia adverbs** were created with **no** inline links in examples *or* notes, and a 2026-06-26 frontier run over **06275–06281** confirmed the gap extends well past the onomatopoeia: that slice mixes mimetics (ほんのり / ほっこり / ちゃっかり), four-character idioms (軽挙妄動 / 温厚篤実), and **拝〜 humble-keigo nouns** (拝読 / 拝聴) — **all** with fully naked examples AND notes. This is the same contiguous pre-inline-link create-era cohort documented across 06150–06246 (created 2026-01-17–19, `ai_model: claude-opus-4-5`); the band is now confirmed effectively unbroken from ~06150 through **06281**. The 2026-06-26 run hand-linked its frontier entries (each takes ~15 lookups) and restated the now-standing recommendation with a concrete next target: a **dedicated inline-link sweep over ~06275–06600** (the block is large and the sequential frontier finds these one at a time). Same diagnosis, same gating on the Tooling item 15 detector for a verified systemic-fix batch.

**Update 2026-06-26 (second — the band reaches the casual/conjunction & cultural-noun cohort through 06300)**: Two 2026-06-26 routine polish runs carried the frontier through the next two contiguous slices and re-confirmed the band is still unbroken. (1) The **06282–06287** casual/slang & conjunction band (とはいえ, とはいうものの, てか, ワンチャン, エモ, 界隈) had **completely naked** Japanese in examples *and* notes — the third run to note this specific sub-band. (2) The **06288–06300** cohort (cultural nouns + proverbs, created in one Jan batch) was given furigana but **never inline-linked** — naked examples and notes throughout. Both runs hand-linked their frontier entries. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06300**. Same diagnosis, same recommendation, now with the concrete next target restated by both runs: a **dedicated inline-link sweep over ~06294–06600** would clear the block far faster than the sequential frontier finding entries one at a time (still gated on the Tooling item 15 detector for a verified systemic-fix batch).

**Update 2026-06-28 (the band reaches the 06294–06308 cultural/medical/finance cohort — and these are heavy full-coverage jobs)**: Three 2026-06-27 routine polish frontier runs carried the band through **06294–06308** without interruption and added a quantitative note on the *cost* of the remaining backfill. (1) The **06294–06300** traditional-culture block (montsuki / bangasa / kouro / hatsunetsu and neighbors) had **zero** inline-link coverage in examples *and* notes, and its notes are encyclopedic glossary lists dense with rare `noentry` compounds (黒留袖, 貸衣装, 油紙, 仏前香炉, 聞香用香炉, 香道) — **15–30 lookups per entry**. (2) The **06298–06303** medical-symptom (筋肉痛/動悸/息切れ/痙攣) + finance (収益/抵当) cohort was likewise fully naked in examples *and* notes, each a **30–50-link** full-coverage job with dense rare medical/finance `noentry` compounds. (3) The **06304–06308** frontier was hand-linked the same way. The runs hand-linked their frontier entries (06294–06297, then 06298–06303, then 06304–06308). The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06308**, and the new datum is that the 06294+ cultural/technical cohorts are the **heaviest** slices yet (15–50 lookups each, much of it `noentry`), which strengthens the case that the sequential frontier lane alone cannot outpace the band: a **dedicated inline-link sweep over ~06304–06600** is the right shape of work (still gated on the Tooling item 15 detector).

**Update 2026-06-29 (the band reaches 06323–06328 — and recent `modified` dates confirm the not-self-healing signature yet again)**: A 2026-06-29 routine polish frontier run carried the band through **06323–06328** (playground/gardening/car-parts general-tier nouns) and re-confirmed it is still unbroken: all had **zero** `⟦...⟧` links in examples *and* notes. The sharper datum this run added is on the *recency* point already raised at 06156 / 06177–06183 / 06214+: several entries in this slice carry **recent `modified` timestamps yet remain fully naked** — **06327 sentei (剪定)** modified 2026-06-25, and **06331 handoru / 06332 akuseru** modified 2026-06-16 — so the late touches were tag/metadata edits, not linking, and the inline-link gap is once more shown **not to self-heal through ordinary polishing**. The run hand-linked its frontier entries. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06328**; same diagnosis and same recommendation — a **dedicated inline-link sweep over ~06320–06600** (still gated on the Tooling item 15 detector) would clear it far faster than the sequential frontier finding entries one at a time.

**Update 2026-06-30 (the band reaches the 06338–06343 four-char-idiom/compound-verb cohort)**: A 2026-06-30 routine polish frontier run carried the band through **06338–06343** (four-character idioms and compound verbs from the 2026-01-17 creation batch) and re-confirmed it is still unbroken: all shipped with **zero** `⟦...⟧` links in examples *or* notes — naked Japanese throughout. The observing run's datum is that the low-ID priority-lane entries it also processed were already fully linked, so the link-coverage gap is **concentrated in this mid-ID creation batch**, not spread evenly: a targeted ~06338–06500 sweep would clear a large, well-defined block. The zero-link create-era band is now confirmed effectively unbroken from ~06150 through **06343**; same diagnosis, same recommendation — a dedicated ~06338–06600 inline-link sweep (still gated on the Tooling item 15 detector) would clear it far faster than the sequential frontier finding entries one at a time.

**Batch readiness**: `batch_ready: false` until the Tooling Backlog item 15 detector
exists. Once it exists, this becomes a systemic-fix candidate with per-entry
semantic verification (the TRANSITIVITY/Pattern/COMMON PATTERNS context must be
read to supply the correct entry ID for each link).

## Priority 22: Inconsistent free-text `part_of_speech` display field

**Source**: 2026-06-23 routine polish run (frontier 6250–6254)

The free-text `part_of_speech` field — the human-readable POS string shown in the
entry-page header — is **wildly inconsistent dictionary-wide**, with many surface variants
for the same grammatical category: e.g. `adjective (i-adjective)` (98 entries) vs
`i-adjective` (256); and `noun, suru verb` / `noun / suru-verb` / `noun, verb-suru` /
`verb (suru)` all coexisting for suru-verbs. This is a **display-text** inconsistency only:
the validated structured tag `metadata.tags.pos` (e.g. `adjective-i`, `verb-suru`) is
correct and canonical, and the renderer/search rely on `tags.pos`, not the free-text field.
So there is no functional bug — but the entry-page headers read inconsistently across
otherwise-parallel entries.

**Suggested action**: a one-time normalization pass that maps the long tail of
`part_of_speech` surface variants onto a **canonical display string per `tags.pos` value**
(driven by the structured tag, which is the source of truth). Because `tags.pos` already
encodes the category unambiguously, the mapping is deterministic — the only design choice is
the canonical display wording (e.g. pick `i-adjective` over `adjective (i-adjective)`,
`noun, suru verb` over the other three suru-verb spellings). This is **systemic-fix
territory once a normalizer/detector exists** (see
[Tooling Backlog](tooling-backlog.md) → item 29): the detector lists every entry whose
`part_of_speech` text is not the canonical string for its `tags.pos`, and the transform is
a safe text substitution validated against the structured tag. Low risk (display-only), and
the canonical map should be agreed with the curator before a bulk run since it changes
visible header text on thousands of pages.

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of recurring tag-drift patterns (covers P6–P8 above)
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of malformed wrapper patterns (covers P9 above)
