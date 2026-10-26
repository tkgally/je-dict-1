# Japanese-English Learner's Dictionary - Project Status

**Last updated**: 2026-10-23
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
| Total entries | ~30,764 |
| Basic tier | 801 (closed) |
| Core tier | ~1,982 (closed) |
| General tier | ~27,981 (open) |
| Candidate words | ~188 (all vetted; queue cleaned 2026-08-11) |
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

### 2026-10-26 (20 new entries)

Twenty entries added (32278–32297), bringing the dictionary to about 32,070. Ten define words the
dictionary already used without an entry: 追いやる, 立ち仕事, ひしめき合う, 取りまとめる, 見計らう,
満ち引き, 大舞台, 粒揃い, 計らい, 垣間見える. Ten come from brainstorming: 判明する, を通して, をはじめ,
分かり合う, 存じ上げる (humble "know", of people), それどころか, 周知, the fish アジ and ブリ, and
つがい (a mated pair of animals). An independent check found two overstatements in the notes, both fixed.

### 2026-10-25 (12 new entries)

Twelve entries added (32266–32277), bringing the dictionary to about 32,050. Six define words the
dictionary already used without an entry: 失業率, 啓発, 暗がり, 山あい, 勝ち上がる, 負け越す. Six come
from brainstorming the bird vocabulary: オシドリ (おしどり夫婦), コウノトリ, ハゲタカ (with the
"vulture fund" sense), とさか (とさかに来る), 鳥インフルエンザ, and 孵る (to hatch). An independent
check found one point (鳥インフルエンザ is a disease, not the virus), fixed.

### 2026-10-25 (Tom's rulings on two curator questions)

浅まる (22361) is retired: a few web hits exist, but not enough to make it an established word; its
URL redirects to 浅い, and the cross-references from 浅い, 深まる and 薄れる are dropped. 茶道具 now
has only the reading ちゃどうぐ: the entry is renamed 22295_sadougu → 22295_chadougu (the old URL
redirects; example audio keys follow), and its furigana and notes are updated. In 茶杓, the
furigana {千|せん}{利休|のりきゅう} is corrected to {千利休|せんのりきゅう}, and an independent check
corrected the serving measure (thin tea about 1½–2 scoops, thick tea about 3 per guest).

### 2026-10-25 (Claude Opus accuracy pass over 21514–22473)

Tom asked for Claude Opus to re-review the 960 entries gpt-6.1-sol had swept on 24–25 October.
Opus flagged 162 issues in 141 entries; 155 were accepted and fixed in 137 entries, 5 dismissed and
2 set aside for Tom (whether 浅まる is an established word; 茶道具's headword reading さどうぐ vs
ちゃどうぐ). Among the fixes: 不戦条約 glossed and translated throughout as "non-aggression pact"
(that is 不可侵条約); the CPA exam ranked with the medical exam among the three hardest; 鳥小屋 glossed
"birdcage"; 浅まる's example reading 日照り as にっしょうり; 行き止まる's figurative sense, whose examples
needed 行き詰まる, removed; many false absolutes in notes. gpt-6.1-sol then checked the edits and caught
three overcorrections, which were fixed.

### 2026-10-25 (Claude on the subscription joins the model checks)

Tom approved the recommendations of an experiment comparing the OpenRouter checking models with
Claude run headless on the Max subscription (`enhancement/claude-backends-2026-10-25/REPORT.md`).
On 200 entries, Claude Opus found as many real errors as gpt-6.1-sol, a different two thirds of
them (85% together); Sonnet and Haiku found a fifth as many; subagents and batched reviews lost
most of the gain. Changes: the accuracy sweep now has Opus review the same entries after sol
(`--second claude:opus`, its "warn" flags kept, one added prompt paragraph naming the error
classes the adjudication accepts); the kana-link review moves from gemini-2.5-flash (0.66 on
the labeled set) to Opus (0.86); the conjugation model check moves from sol to Haiku (caught
every injected error, no false flags). The self-check after each cycle stays on sol alone, so a
different model family checks Claude's own work, and brainstorming stays as it was. Every
Claude call reads the plan's usage windows and stops at 70% of the five-hour or 85% of the
seven-day window (`pipeline/routine-config.json` → `claude`). New: `build/claude_backend.py`,
`build/tests/test_claude_backend.py`.
