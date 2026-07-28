# Multilingual Rendering and Delivery Architecture — Worked Design

**Last updated**: 2026-06-06

## Overview

This is a worked-out companion to the [Multilingual Dictionary](../ideas/multilingual-dictionary.md)
plan. The plan's [§6 "UI, storage, and delivery"](../ideas/multilingual-dictionary.md#6-ui-storage-and-delivery)
sketches the rendering choice — "per-language static pages" vs. "single page + client-side
swap," with "a hybrid is likely best" — but leaves it, in the hub's own words, as "the one
major design question still only sketched." The companion
[Translation Sidecar Design](../ideas/translation-sidecar-design.md) deliberately scoped the
delivery layer **out** ("this page is about the data layer the renderer consumes, not the
delivery layer," its §6). This page is that missing delivery-layer design.

It is **design, not implementation** — it modifies no schema, script, entry, or template. Its
job is to make the rendering decision *decision-ready* for the curator: state the options
precisely, bring real SEO guidance and real size numbers to bear, surface the one hard
constraint that actually forces the choice, and record a recommendation plus what stays open.

## 1. The decision, stated precisely

The site is fully static (HTML/CSS/JS, GitHub Pages, no server —
[Architecture](../project/architecture.md)). For a Japanese→multilingual dictionary, every
*translatable* field (gloss, definitions, example translations, notes — the sidecar payload
from [Translation Sidecar Design §1](../ideas/translation-sidecar-design.md#1-what-the-sidecar-must-hold--derived-from-the-real-schema))
must be displayable in the user's chosen language, while the *invariant Japanese spine*
(headword, furigana-annotated examples, conjugation tables, cross-reference graph, kanji
links) is **identical across languages**.

Three ways to deliver that on a static host:

| Option | What ships | URL shape |
|--------|-----------|-----------|
| **A. Per-language static pages** | `build_flat.py --all-langs` emits a fully rendered HTML file per entry *per language* | `/05000_manjuu.html` (en), `/zh-Hans/05000_manjuu.html` (zh) |
| **B. Single page + client-side swap** | One HTML per entry (default language rendered); the page also carries, or fetches, the other languages' translatable fields and swaps text in JS on toggle | one URL per entry; language in `localStorage` |
| **C. Hybrid** | Per-language static *entry* pages for SEO + a client-side toggle that navigates between them and remembers the preference; some heavy/shared assets fetched rather than duplicated | per-language URLs + remembered preference |

The two forces that decide between them pull in opposite directions: **SEO/discoverability
pushes hard toward separate URLs (Option A/C)**, while **static-host size and file-count
limits push hard against full duplication (toward B)**. §2 and §3 quantify each; §4 resolves
them.

## 2. The SEO force: Google wants separate URLs, not cookie/JS swapping

The decisive external evidence is Google Search Central's *Managing multi-regional and
multilingual sites* guidance, and it is unusually direct:

- **Separate URLs, not dynamic swapping.** "Google recommends using different URLs for each
  language version of a page rather than using cookies or browser settings to adjust the
  content language." If you swap dynamically, "Google might not find and crawl all your
  variations."
- **Googlebot is US-located and sends no `Accept-Language`.** "Most, but not all, Google
  crawls originate from the US, and we don't attempt to vary the location to detect site
  variations"; the crawler "sends HTTP requests without setting `Accept-Language` in the
  request header." So any design that depends on the *request* to pick a language is invisible
  to the crawler — it will only ever see the default language.
- **Do not auto-redirect by language.** "Avoid automatically redirecting users from one
  language version of a site to a different language version" — it can "prevent users (and
  search engines) from viewing all the versions of your site." Offer **clickable** language
  links instead.
- **Subdirectories are the recommended URL structure** for a single-domain project: they
  "consolidate link equity under one domain" and are "low maintenance," versus ccTLDs
  (expensive, single-country) or subdomains (geotargeting intent unclear). For je-dict-1 that
  means `/zh-Hans/…` under the existing `tkgje.jp`, **not** `zh.tkgje.jp` or a new ccTLD.
- **`hreflang` + `x-default` annotations** tell Google which version to serve. Every page must
  reference itself and all its variants (self-referencing, symmetric), use valid codes
  (`zh-Hans`, not bare `zh` — consistent with
  [Chinese Simplified/Traditional Handling §2](chinese-simplified-traditional.md#2-language-code-space)),
  and declare an `x-default` fallback (English, the universal fallback). One caveat the SEO
  literature stresses: "a single error in a hreflang cluster causes Google to ignore the
  entire cluster," and ~75% of real implementations contain errors — so the `hreflang` block
  must be **generated**, never hand-maintained.

**Implication.** Pure Option B (one URL per entry, language chosen by cookie/JS) is the option
Google explicitly recommends *against*. A Chinese learner searching in Chinese would never find
the Chinese version, because Googlebot only ever renders the English default at the single URL.
For a dictionary whose entire growth thesis includes "serving users who land via search engines
in their language" ([multilingual §6](../ideas/multilingual-dictionary.md#6-ui-storage-and-delivery)),
that is a serious cost. **SEO points at A or C.**

## 3. The size force: the GitHub Pages 1 GB ceiling is hit at the second language

This is the constraint that actually decides the question, and it is sharp. Measured against
the current live build (2026-06-06):

| Quantity | Current (English only) |
|----------|------------------------|
| Total HTML files in `docs/` | **31,454** (28,675 entry pages + nav/browse/kanji/articles) |
| Published site size | **492 MB** |
| Average entry-page HTML | ~16 KB |
| `search-index.js` (single file) | **17.5 MB** |

GitHub Pages imposes hard/soft limits ([GitHub Docs, *GitHub Pages limits*](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)):

- **Published sites may be no larger than 1 GB** (hard).
- **Soft bandwidth limit of 100 GB/month.**
- **Soft limit of 10 builds/hour.**

Now apply Option A (full per-language static rendering). Each additional fully rendered
language re-emits **the entire entry corpus plus its own gloss search index**:

| Languages | Approx. published size | Approx. HTML file count | Under 1 GB? |
|-----------|------------------------|--------------------------|-------------|
| en only (today) | 492 MB | 31,454 | yes (≈½) |
| en + zh-Hans | **≈ 970 MB** (+~460 MB pages, +~17.5 MB index) | ~60,000 | **at the ceiling** |
| en + zh-Hans + ko | **≈ 1.45 GB** | ~88,000 | **over — blocked** |

So **naive Option A is already a non-starter at N = 2**, before accounting for the corpus's
steady growth (~28,400 → ~28,700 entries in the first week of June 2026 alone — see
[log.md](../log.md)). The very first additional language lands the site at the 1 GB ceiling,
and the *second* additional language is impossible on GitHub Pages without mitigation. This is
not a far-future scaling worry; it binds on the first deliverable.

### Why full duplication is wasteful (the same insight that chose the sidecar)

Most of the per-page weight is the **invariant Japanese spine** — the furigana-annotated
examples, the conjugation tables (large for verbs), the rendered cross-reference and kanji
links. That content is byte-identical across languages. Re-emitting it N times to vary only the
small translatable fields is exactly the duplication the storage design already rejected when
it chose **sidecar files (Option B) over per-language full entry copies (Option C)** in
[multilingual §3](../ideas/multilingual-dictionary.md#3-schema-and-storage-options). The
rendering layer faces the structurally identical choice, and the same logic applies: **do not
duplicate the invariant bulk if you can avoid it.**

### The search index is its own sub-problem

`search-index.js` is **17.5 MB today** — already a heavy client download (every visitor who
uses search pulls it). It indexes headwords, readings, glosses, and tags
([Architecture §Search](../project/architecture.md#search)). Glosses and tag display names are
language-specific, so a multilingual site needs **per-language gloss indexing**. Two facts fall
out:

1. Shipping *all* languages' gloss indexes to *every* user (one 17.5 MB-class file per
   language, concatenated) is unacceptable. The index **must** be split per language and the
   client must fetch only the active language's index.
2. Per-language splitting *helps* on the size axis: the shared headword/reading/romaji portion
   (the invariant spine) can be one file; only the gloss/tag layer multiplies, and that is the
   smaller part. This argues for refactoring the index into "shared spine index + per-language
   gloss overlay" regardless of which page-rendering option is chosen.

## 4. Resolving the tension — recommendation

The two forces collide: SEO wants per-language URLs (A/C); the 1 GB ceiling forbids full
per-language duplication (pushes to B). The resolution is a **size-controlled hybrid (Option
C)** plus an explicit hosting decision the curator must make before the *second* additional
language. Concretely:

### 4a. Entry pages: per-language static, but lean and size-budgeted

Emit per-language static entry pages under subdirectories (`/zh-Hans/05000_manjuu.html`) so the
SEO requirements in §2 are met — separate URLs, `hreflang`/`x-default`, no auto-redirect. But
control the size three ways so the ceiling moves out:

1. **Do not duplicate the heavy shared assets per language.** The 17.5 MB-class search index,
   `styles.css`, and JS are referenced, not re-emitted, per language. Only the entry HTML
   (~16 KB) and the small per-language gloss-index overlay multiply.
2. **Do not emit per-language *navigation* duplicates** (browse, recent, random, kanji index
   pages — ~2,800 files) unless they carry translatable content that matters for SEO; render
   their language layer client-side from a small JSON, or share them. The per-language
   multiplication should be (mostly) the *entry* pages, where the translated gloss/notes are
   the indexable value.
3. **Treat the 1 GB ceiling as a project gate, not a surprise.** With measures 1–2, en + zh-Hans
   stays comfortably under 1 GB; a *third* language likely still breaches it. So the plan should
   record that **scaling past two languages on GitHub Pages requires a hosting migration**
   (see §4c), and make that an explicit decision rather than a wall hit mid-rollout.

### 4b. The toggle: client navigation between static URLs, with a remembered preference

This reconciles the curator's stated intent ("a toggle at the top of the page; the choice
persists in the browser" — [multilingual anchor constraints](../ideas/multilingual-dictionary.md#the-curators-stated-design-intent-anchor-constraints))
with Google's "separate URLs, don't auto-redirect" guidance:

- The toggle is a set of **clickable links** to the same entry's other-language URLs (e.g.
  `/zh-Hans/05000_manjuu.html`). Clicking navigates — it changes the URL — rather than swapping
  text on one URL. This is exactly what Google asks for.
- The chosen language is stored in `localStorage`. On a *subsequent* in-site click (entry →
  cross-reference → another entry), the site's link-rewriting JS sends the user to the
  remembered language's URL. This gives the "sticky preference" UX **without** server-side
  cookie content-swapping and **without** auto-redirecting a fresh visitor or the crawler.
- **First-time visitors and the crawler land on whatever URL they requested** (English at the
  bare URL, Chinese at `/zh-Hans/…`). No `Accept-Language` redirect (Googlebot sends none
  anyway, per §2). `x-default` → English handles the "no preference" case for search engines.
- **Field-level fallback is preserved** ([Translation Sidecar Design §6](../ideas/translation-sidecar-design.md#6-build-time-join-and-rendering-contract)):
  a `/zh-Hans/` page with a translated gloss but a stale/missing `notes` shows Chinese gloss +
  English notes, never an all-or-nothing switch. So a language can ship at 10% coverage.

This is a genuine hybrid: **static per-language pages (A's SEO strength) + a client-side toggle
that navigates and remembers (B's UX), with the heavy assets shared (size control).**

### 4c. The hosting question the curator must decide before language #3

If the dictionary commits to **three or more** target languages, GitHub Pages' 1 GB ceiling
becomes a hard blocker, and a host with higher (or no) size limits is required. Note that the
*file-count* axis matters too, not just bytes: at ~30K files/language, two languages is ~60K
files and three is ~90K — and some popular static hosts cap *file count per deployment* (e.g.
Cloudflare Pages' 20,000-file limit is already exceeded by the **English-only** site today).
Candidate paths, to be evaluated when the time comes (not now):

- **Stay on GitHub Pages, cap at two languages**, relying on the §4a size controls. Zero
  migration cost; closes the door on a third static-rendered language.
- **Migrate to a host without the 1 GB / file-count limits** (object storage + CDN, Netlify,
  Vercel static, self-hosted). Removes the ceiling; adds operational surface the project
  currently does not have (it is deliberately serverless-static).
- **Lean harder on client-side rendering for the general tier** (ship static per-language pages
  only for basic/core — the high-SEO-value, most-searched entries — and render the long tail's
  language layer client-side from per-entry JSON). This keeps the static page count near
  today's while still giving the most valuable entries separate indexable URLs. A principled
  middle path that aligns with the tier-first rollout in
  [multilingual §9](../ideas/multilingual-dictionary.md#9-phasing--rollout).

This page does **not** pick among these — it flags that the choice exists and must be made
**before** scaling beyond two languages, so it is a planned decision rather than a mid-rollout
emergency.

## 5. Build-pipeline consequences (for the eventual implementation)

Stated here only to connect this delivery design to the build inventory in
[multilingual §8](../ideas/multilingual-dictionary.md#8-build-script-and-pipeline-adaptations-inventory);
none of this is built.

- `build_flat.py --lang <code>` / `--all-langs` joins canonical + sidecar and emits the
  per-language entry pages under `/<code>/…` (the join contract is
  [Translation Sidecar Design §6](../ideas/translation-sidecar-design.md#6-build-time-join-and-rendering-contract)).
- `entry_renderer.py` emits the `hreflang`/`x-default` `<link>` cluster (generated, symmetric,
  self-referencing — §2) and the clickable language toggle.
- `search_index_builder.py` splits into a shared spine index + per-language gloss overlay
  (§3), so the client fetches only the active language's gloss layer.
- `page_generators.py` decides which nav pages get per-language static variants vs. a
  client-side language layer (§4a measure 2).
- The sitemaps (`sitemap-entries.xml` etc., already split) gain per-language entries, and the
  `hreflang` annotations can alternatively be delivered **in the sitemap** rather than in every
  page `<head>` — a known scaling technique for large multilingual sites that avoids bloating
  28,000+ pages × N with a `<head>` block, worth evaluating at implementation time.
- **Incremental builds matter more, not less.** A full `--all-langs` rebuild emits N× the
  pages; the existing `--quick` incremental path
  ([Architecture](../project/architecture.md#core-build-pipeline)) and the 10-builds/hour soft
  cap mean per-language incremental rendering is close to required for a tractable edit loop.

## 6. Decision record and what stays open

**Recommended (for curator ratification):**

- **Hybrid (Option C):** per-language static *entry* pages under subdirectories
  (`/zh-Hans/…`) for SEO, with a client-side toggle that **navigates** between them and
  remembers the preference in `localStorage` — never cookie/`Accept-Language` content-swapping,
  never auto-redirect (§2, §4b).
- **Share the heavy assets** (search index, CSS, JS) across languages; multiply only the entry
  HTML and a small per-language gloss-index overlay (§3, §4a).
- **Split the search index** into a shared spine index + per-language gloss overlay regardless
  of the page option (§3).
- **English is the `x-default`** and the universal field-level fallback.

**Still open (genuine decisions, not yet made):**

- **The hosting question (§4c)** — GitHub Pages caps the project at ~two fully-static languages
  (1 GB; file-count on some hosts even tighter). Going to three+ needs a host migration or a
  basic/core-static + general-tier-client-side split. **Must be decided before language #3**,
  ideally acknowledged when committing to even the second.
- **`hreflang` in `<head>` vs. in the sitemap** — per-page `<head>` blocks are simplest but
  add weight to 28,000+ × N pages; sitemap delivery scales better but is less commonly
  implemented. Decide at implementation.
- **Which navigation pages get per-language static variants** vs. a client-side language layer
  (§4a measure 2) — affects both file count and SEO of browse/tag pages.
- **Whether the general tier is rendered static-per-language at all**, or only basic/core, with
  the long tail client-side (§4c third path) — interacts directly with the tier-first rollout.

## Implications for je-dict-1

- The rendering layer faces the **same invariant-vs-translatable duplication choice** the
  storage layer already resolved (sidecar over per-language copies). The consistent answer is:
  do not re-emit the invariant Japanese spine N times. That principle, plus Google's
  separate-URL requirement, plus the 1 GB ceiling, jointly select the size-controlled hybrid.
- The **single most consequential, least-anticipated fact** this page surfaces is that the
  GitHub Pages 1 GB limit is reached at the *first* additional language, not in some distant
  scaled future. The hub's §6 listed "per-language page explosion" as a risk "to measure before
  committing"; this page measures it — and the answer is that it binds immediately. The
  hosting/rendering decision is therefore an *early* design lock-in item alongside storage and
  staleness ([multilingual §9 step 1](../ideas/multilingual-dictionary.md#9-phasing--rollout)),
  not a late one.
- The recommendation keeps the project's serverless-static character for the first additional
  language while naming the exact point (language #3, or a general-tier-wide static commitment)
  at which that character must be revisited — turning a latent wall into a scheduled decision.

## Related pages

- [Multilingual Dictionary](../ideas/multilingual-dictionary.md) — the hub plan; this page develops its §6 (UI/storage/delivery), the "one major design question still only sketched"
- [Translation Sidecar Design](../ideas/translation-sidecar-design.md) — the data layer this renderer consumes; its §6 explicitly deferred the delivery layer to this page, and its field-level fallback contract is reused in §4b
- [Chinese Simplified/Traditional Handling](chinese-simplified-traditional.md) — the `zh-Hans`/`zh-Hant` code space these URLs and `hreflang` annotations use, and the per-language font-stack and search-index split this page's §3 generalizes
- [Architecture and Build System](../project/architecture.md) — the static build pipeline, search index, and incremental-build path these changes extend
- [Digital Dictionary UX](../research/digital-dictionary-ux.md) — search and interface behavior the per-language index and toggle affect
- [Dictionary Growth and Long-Term Vision](../ideas/dictionary-growth.md) — the entry-count growth that compounds the per-language size math

## References

- Google Search Central. *Managing multi-regional and multilingual sites.* https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites (separate URLs over cookies/browser settings; Googlebot is mostly US-based and sends no `Accept-Language`; avoid auto-redirecting by language; ccTLD/subdomain/subdirectory trade-offs; use `hreflang`).
- GitHub Docs. *GitHub Pages limits.* https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (published site ≤ 1 GB; 100 GB/month soft bandwidth; 10 builds/hour soft limit).
- Search Engine Journal / Seer Interactive / Weglot. *Implementing hreflang / when to use `x-default`.* (Self-referencing and symmetric annotations; `x-default` as neutral fallback; a single error invalidates the whole `hreflang` cluster; subdirectories consolidate link equity.) https://www.searchenginejournal.com/hreflang-multilingual-website/260855/ ; https://www.weglot.com/blog/hreflang-x-default
- CloudCannon / better-i18n. *Static site generators and i18n.* (Build-time vs. runtime translation; per-language static page counts multiply file count; zero-JS static output indexes best.) https://cloudcannon.com/blog/the-top-five-static-site-generators-for-2025-and-when-to-use-them/ ; https://better-i18n.com/en/blog/astro-i18n-multi-language-sites/
- Measured from the live `docs/` build, 2026-06-06: 31,454 HTML files, 492 MB published, 17.5 MB `search-index.js`.
