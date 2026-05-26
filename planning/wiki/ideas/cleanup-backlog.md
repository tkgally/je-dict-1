# Cleanup Backlog

**Last updated**: 2026-05-26

Concrete cleanup work items surfaced during comprehensive-polish sessions. Each item describes a systemic pattern that affects multiple entries and could be addressed by a dedicated batch pass.

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

## Priority 5: Particle entry polish

**Source**: Comprehensive-polish 2026-05-09 sessions 002 and 003

Particle entries with extensive structured fields (e.g., 00051_ga and 00079_ha with `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`, `information_structure`) contain dozens of small Japanese phrase fragments that lack inline link coverage. These are not addressable by ordinary tier-1 polishing — they need a dedicated particle-polish session.

**Affected entries**: At minimum 00051 (が), 00079 (は), and likely 00422 (を), 00314 (に), 00502 (で), 00504 (と), 00512 (から).

## Priority 6: Spurious conjugation tables on non-verb entries

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

**Highest-volume sub-pattern: 463 okurigana-inside-wrapper instances.** Most render correctly but are non-standard. Canonical form would be `{若|わか}い` instead of `{若い|わかい}`, etc.

**Confirmed downstream impact**: 01525_wakai (basic-tier 若い) is currently missing its conjugation table on the live site because `add_adjective_conjugations.py` couldn't parse the headword `{若い|わかい}` to extract a stem.

**Suggested actions**:
1. **Targeted pass on sub-pattern 3b (68 truncated-reading instances)** — these are real rendering bugs. Manual review and repair.
2. **Mechanical sweep** for sub-patterns 1, 2, and 3a/3c (~791 instances). Regex-driven replacements with validation against `build/word_id_lookup.json`. Mostly cosmetic but worth doing while the pattern is fresh.
3. **Add a furigana-format validator** (`build/check_furigana_format.py`) alongside the existing `verify_furigana.py` (which checks only for *missing* furigana, not malformed wrappers). See [Tooling Backlog](tooling-backlog.md) → item 8.
4. **Restate the convention in `entry-guidelines`** so new entries don't reintroduce the pattern. The current docs state "all kanji must have furigana" but don't address where the wrapper boundaries should sit relative to hiragana characters.
5. See [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) for the full analysis.

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

## Priority 12: Dual-reading furigana with slash separators

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

## Priority 14: Notes content copied from wrong entry

**Source**: Comprehensive-polish 2026-05-25 session 021 (entries 03491–03510)

Entry 03500_nakaba ({半|なか}ば) had a note reading "泥んこ = muddy, mud play" — content that clearly belongs to a nearby entry about mud, not to なかば (midway/halfway). The correct note content should reference 〜なかば usage patterns.

This is a different failure mode from semantic tag drift: the note *text itself* was copied from or generated for the wrong entry, possibly during a batch creation that interleaved entries. Worth scanning notes for obviously mismatched content (note text containing keywords that have no semantic connection to the headword or gloss).

**Detection**: No simple grep — this requires semantic comparison between note content and entry headword/gloss. A lightweight heuristic: extract English words from notes, compare against gloss keywords, flag entries with zero overlap. False-positive-heavy but could surface the worst cases.

**Suggested action**: Low priority as a batch — comprehensive-polish catches these case by case. Worth a targeted spot-check of entries in the same batch cohort as 03500 (roughly 03400–03600).

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of recurring tag-drift patterns (covers P6–P8 above)
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of malformed wrapper patterns (covers P9 above)
