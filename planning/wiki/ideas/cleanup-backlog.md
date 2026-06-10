# Cleanup Backlog

**Last updated**: 2026-06-09 (P11 extended through 05953; added P17 formality misassignment)

Concrete cleanup work items surfaced during comprehensive-polish sessions. Each item describes a systemic pattern that affects multiple entries and could be addressed by a dedicated batch pass.

**As of 2026-06-09**, the batch-addressable items here are also indexed in machine-readable form at [`backlog-queue.json`](backlog-queue.json), which the unified Routine's `systemic-fix` mode (`prompts/routine.md` §B) drains one bounded, per-entry-verified batch at a time. Read-only detectors back the queue: `build/check_furigana_format.py` (P9, P12), `build/check_artifacts.py` (P16, P15, P10, P4, P2), and `build/check_tag_drift.py` (P6, P7, P13; P11 detector experimental). Keep `backlog-queue.json` in sync with this page during wiki maintenance.

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

**Related sub-pattern (notes-level duplication)**: Comprehensive-polish session 033 (entries 05540–05559) found entries 05542, 05543, 05544, 05546 with redundant CONJUGATION prose sections in their `notes` field even though the entry already had a proper `conjugation` JSON field with all forms. The notes-only CONJUGATION block is a batch artifact from a period when conjugation data lived in notes rather than in a structured field. These are distinct from the duplicate-JSON-key pattern above — the notes text is well-formed but redundant once the structured conjugation field exists. Comprehensive-polish removes them case-by-case, but a one-shot scan for `CONJUGATION` headers in notes of entries that also have a `conjugation` field would catch all remaining instances.

## Priority 5: Particle entry polish

**Source**: Comprehensive-polish 2026-05-09 sessions 002 and 003

Particle entries with extensive structured fields (e.g., 00051_ga and 00079_ha with `predicates_requiring`, `particle_contrasts`, `fixed_patterns`, `common_mistakes`, `information_structure`) contain dozens of small Japanese phrase fragments that lack inline link coverage. These are not addressable by ordinary tier-1 polishing — they need a dedicated particle-polish session.

**Affected entries**: At minimum 00051 (が), 00079 (は), and likely 00422 (を), 00314 (に), 00502 (で), 00504 (と), 00512 (から).

## Priority 6: Spurious conjugation tables on non-verb entries

**RESOLVED (2026-06-08).** The one-time non-verb conjugation sweep cleaned **133 entries** (101 non-expression non-verbs — adverbs, onomatopoeia, noun-adverbs, na-adjectives, nouns, auxiliaries — plus 32 reviewed `expression` entries), removing both the `conjugation` field and the stray `verb_class` tag from each. (133 vs. the 130 estimated here: the audit detector counted only entries with a `conjugation` field, whereas the pruner also catches a few that had a stray `verb_class` tag but no table, e.g. 04214_jisseki; one of the original twelve onomatopoeia, 05646_gyuugyuu, had already been cleaned on 2026-06-07.) The reusable pruner `build/prune_nonverb_conjugations.py` was built and committed, and a **defensive exact-enum verb-POS guard** was added to `add_conjugations.py` — the previous guard used the substring test `'verb' in p`, which is true for `"adverb"` and let adverbs with a stray `verb_class` tag generate godan nonsense. The detector one-liner below now returns **0**; re-running both retrofits re-adds nothing. The 31→32 expression cases were all confirmed as multi-word idioms, proverbs, adverbial phrases, or compound-ている forms (not single mis-tagged verbs); the one borderline keigo case (お会いする, 22190) was stripped and logged for a curator second look in [Entry Follow-ups](entry-followups.md).

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

## Priority 15: `{ている}` furigana brace artifact in ASPECT notes

**RESOLVED (2026-06-10).** Routine systemic-fix session fixed all **49** entries: `{ている}` → plain `ている` in the `ASPECT (...)` section headers (the only context the artifact appeared in — all 49 hits were in `notes`, none in examples). Following the semantic-verification-first rule, each entry was opened and confirmed individually before saving, even though the transform is mechanically safe (`ている` is pure kana, so dropping the braces drops no reading); the `modified` timestamp was bumped on each. A furigana self-check screened the 49 changed IDs and returned 5 flags, **all rejected** as partial-reading false positives / model hallucinations unrelated to the edit (e.g. `捻|ねじ`, `逃|に` for 逃がす, `果|は` in 果てる). `python3 build/check_artifacts.py --issue teiru-brace --json` now returns 0; the `grep` detector below returns 0. Tracked as `artifact-teiru-brace` in `backlog-queue.json`.

**Source**: Comprehensive-polish 2026-06-01 session 003 (entries 04574–04594)

Multiple verb entries use `{ている}` (furigana brace syntax) instead of plain `ている` or `(ている)` in their ASPECT section headers or notes. The furigana brace syntax `{X|Y}` is intended for kanji with readings, not for hiragana-only strings. The wrapped `{ている}` is a template artifact from batch entry creation.

**Scope**: 49 entries confirmed across the entry set — concentrated in the 00000–00500 and 03500–04600 ranges.

**Detection**: `grep -rl '{ている}' entries/ | wc -l`

**Suggested action**: Simple regex replacement: `{ている}` → `ている` across all entries. Pure text substitution, no semantic judgment needed. Low risk.

## Priority 16: `[Register: Neutral]` legacy artifact in notes

**Source**: Comprehensive-polish 2026-06-01 session 003 (entries 04574–04594)

Multiple entries have `[Register: Neutral]` or similar `[Register: ...]` strings at the end of their notes field. These are template artifacts from batch creation — the register information should be expressed via the `formality` metadata field rather than as trailing text in notes.

**Scope**: 188 entries confirmed.

**Detection**: `grep -rc '\[Register: ' entries/ | grep -v ':0$' | wc -l`

**Suggested action**: Remove the `[Register: ...]` trailing lines from notes. Cross-check against the entry's `formality` field to ensure the information isn't lost. Mechanical sweep with validation.

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

## Informational: Pre-polished cohort around 00083–00090

Four entries in the 00074–00096 range (00083 俳句, 00086 発揮, 00087 花火, 00088 判事) were already fully linked — suggesting a prior polish pass touched that range. Subsequent sessions entering this area should expect occasional entries needing no work.

## Related pages

- [Tooling Backlog](tooling-backlog.md) — tool improvements surfaced alongside these patterns
- [Entry Follow-ups](entry-followups.md) — specific entry fixes
- [Content Pipeline](../project/content-pipeline.md) — how polishing tasks work
- [Entry Consistency](../topics/entry-consistency.md) — consistency standards
- [Schema Tag Reliability](../topics/schema-tag-reliability.md) — analysis of recurring tag-drift patterns (covers P6–P8 above)
- [Furigana Wrapper Anomalies](../topics/furigana-wrapper-anomalies.md) — analysis of malformed wrapper patterns (covers P9 above)
