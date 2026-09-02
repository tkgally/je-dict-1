#!/usr/bin/env python3
"""Cross-model accuracy review: glosses, example translations, tags, and notes.

Companion to review_runner.py (which checks furigana readings). This sends each
entry to a model via OpenRouter and asks for a conservative critique across the
dimensions a second model is well-placed to catch:

  gloss        Does the gloss/definition accurately render the headword's meaning?
  translation  Is each example's English a faithful, natural rendering of the JP?
  tags         Does a SEMANTIC tag name a domain the headword does not belong to
               at all? Is a register label contradicted by the entry's own notes?
  notes        Is a factual, grammatical, or usage claim in the notes wrong?
               (Added 2026-09-02: the notes are where the polish pass writes most
               of its new prose and where the audit's factual errors were found.)

Output is a per-entry JSON review file under reviews/accuracy/{id}.json (not
version-controlled) plus one line per flagged entry appended to
reviews/accuracy_flags.jsonl (tracked; consumed by prioritize_polishing.py).
Claude (the Routine's accuracy-review mode) then evaluates each issue with its
own judgment — nothing is auto-applied.

Noise control (2026-09-02, prompt version 4). The v3 reviewer ignored the prose
prohibitions against "too broad / too narrow" tag substitutions and register
quibbles (in-list tag precision fell to 3.6% once the off-vocabulary tail ran
out). v4 therefore:
  * detects off-vocabulary semantic tags IN CODE (deterministic) and never asks
    the model about them;
  * asks for a closed "wrong-category" judgment on semantic tags, with breadth
    explicitly never a reason;
  * requires a verbatim `quote` from the notes for register and notes flags, and
    drops any such flag whose quote is not actually in the notes;
  * post-filters breadth complaints, flags naming a tag the entry does not carry,
    out-of-list suggestions, and (by default) all `warn`-severity issues, which
    measured ~1% precision;
  * stamps every surviving issue with a regex-assigned `family` so precision can
    be computed per family from reviews/decisions.jsonl without free-text notes.
Dropped issues are counted per family in the review file (`dropped`), so the
filter itself stays measurable.

Reuses review_runner.py's OpenRouter plumbing. Respects a per-invocation
--budget (USD, estimated); the Routine enforces the $5/day cap via the ledger.

Usage:
    python3 build/review_accuracy.py --ids 05891,05907 --budget 0.50
    python3 build/review_accuracy.py --range 5800 5900 --budget 1.00
    python3 build/review_accuracy.py --ids 05907 --dimensions tags --dry-run
    python3 build/review_accuracy.py --report
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from review_runner import (  # noqa: E402  (sibling module, tested plumbing)
    call_openrouter, parse_model_response, estimate_cost, rough_token_count,
    get_api_key,
)
from validate_tags import VALID_SEMANTIC  # noqa: E402

try:  # 1:1 migration map for common off-vocabulary tags (optional)
    from check_tag_drift import TAG_MIGRATION  # noqa: E402
except Exception:  # pragma: no cover - defensive
    TAG_MIGRATION = {}

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
OUT_DIR = PROJECT_ROOT / "reviews" / "accuracy"
FLAGS_FILE = PROJECT_ROOT / "reviews" / "accuracy_flags.jsonl"

DEFAULT_MODEL = "google/gemini-2.5-flash"
DIMENSIONS = ("gloss", "translation", "tags", "notes")

# Prompt revision marker, recorded in each review file so calibration stats can
# be segmented by prompt version. v1 (2026-06-09) ~1.5% flag precision; v2
# (2026-06-10) embedded project conventions; v3 (2026-06-11) followed the
# taxonomy expansion; v4 (2026-09-02) adds the notes dimension, moves
# off-vocabulary detection into code, and post-filters the measured noise
# families. See reviews/decisions.jsonl for the evidence.
PROMPT_VERSION = 4

# Tags the reviewer must never dispute on breadth grounds.
FALLBACK_TAGS = {"general", "descriptive", "expression", "onomatopoeia",
                 "grammatical", "action", "abstract"}

FURIGANA_RE = re.compile(r"\{([^|]+)\|[^}]+\}")
LINK_TAIL_RE = re.compile(r"→[^⟧]*⟧")

# --------------------------------------------------------------------------- #
# Noise families (regexes over the model's own wording)
# --------------------------------------------------------------------------- #
BREADTH_RE = re.compile(
    r"too (broad|narrow|vague|general|generic|specific|wide|unspecific|coarse)"
    r"|(more|less) (specific|precise|granular|appropriate|accurate|fitting|suitable)"
    r"|overly (broad|general|vague)|not specific|insufficiently specific"
    r"|better (fit|tag|captured|described|represented)|would (better|be more)"
    r"|could (be|use) (a )?(more|better)|consider (adding|using|replacing)"
    r"|narrower|broader|a catch-all|catch all|generic tag|is vague|is (a )?placeholder"
    r"|should (also|additionally) (include|carry|have)|missing (a |the )?tag"
    r"|add(ing)? (a |the )?tag|redundant|unnecessary tag|doesn't add",
    re.IGNORECASE)
OFFVOCAB_RE = re.compile(
    r"not (in|on|part of|from) the (valid|allowed|closed|approved)? ?(tag )?(list|vocabulary|taxonomy)"
    r"|not a valid tag|invalid tag|off[- ]vocab|unknown tag|not (a )?recogni[sz]ed",
    re.IGNORECASE)
REGISTER_RE = re.compile(r"formality|politeness|register|honorific|humble|keigo|polite\b",
                         re.IGNORECASE)
STYLE_RE = re.compile(
    r"\b(more natural|slightly|minor|stylistic|nuance|reads better|could also|"
    r"alternatively|would read|awkward|phrasing|word choice|preferable|"
    r"more idiomatic|smoother|clunky|not wrong but|technically correct)\b",
    re.IGNORECASE)
TAG_TOKEN_RE = re.compile(r"[a-z][a-z-]+")


def plain_jp(text):
    """Strip inline-link syntax and furigana wrappers to plain Japanese."""
    if not text:
        return ""
    text = LINK_TAIL_RE.sub("", text)
    text = text.replace("⟦", "").replace("⟧", "")
    return FURIGANA_RE.sub(r"\1", text)


def numeric_id(s):
    m = re.match(r"(\d+)", str(s))
    return int(m.group(1)) if m else None


def find_entries(ids=None, id_range=None):
    out = []
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        nid = numeric_id(path.stem)
        if nid is None:
            continue
        if ids is not None and f"{nid:05d}" not in ids:
            continue
        if id_range is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        try:
            out.append((json.loads(path.read_text(encoding="utf-8")), path))
        except (json.JSONDecodeError, OSError):
            continue
    return out


def entry_payload(entry, include_notes=True):
    tags = (entry.get("metadata") or {}).get("tags", {}) or {}
    defs = []
    for i, d in enumerate(entry.get("definitions", []) or []):
        defs.append({"sense": d.get("sense_number", i + 1),
                     "gloss": d.get("gloss"), "explanation": d.get("explanation")})
    exs = []
    for i, ex in enumerate(entry.get("examples", []) or []):
        exs.append({"i": i, "japanese": plain_jp(ex.get("japanese")),
                    "english": ex.get("english")})
    payload = {
        "headword": plain_jp(entry.get("headword")),
        "reading": entry.get("reading"),
        "pos": tags.get("pos", []),
        "transitivity": tags.get("transitivity"),
        "tier": (entry.get("metadata") or {}).get("vocabulary_tier"),
        "semantic_tags": tags.get("semantic", []),
        "formality": tags.get("formality"),
        "politeness": tags.get("politeness"),
        "gloss": entry.get("gloss"),
        "definitions": defs,
        "examples": exs,
    }
    if include_notes:
        payload["notes"] = plain_jp(entry.get("notes") or "")
    return payload


def build_prompt(entry, dimensions):
    payload = entry_payload(entry, include_notes=("notes" in dimensions
                                                   or "tags" in dimensions))
    checks = []
    if "gloss" in dimensions:
        checks.append('- "gloss": the gloss or explanation states a WRONG or '
                      'misleading meaning (e.g. says "borrow" for a word meaning '
                      '"lend", or "wink" for a word meaning "blink"). Do NOT '
                      'report glosses that are merely brief, incomplete, or '
                      'phrased differently than you would phrase them — concise '
                      '3-8 word glosses are this dictionary\'s house style, and '
                      'sense restructuring is out of scope.')
    if "translation" in dimensions:
        checks.append('- "translation": an example\'s English MISREPRESENTS the '
                      'Japanese (wrong meaning, dropped or added information) or '
                      'is so unnatural that a learner would mislearn the English '
                      'expression. Do NOT report phrasing preferences or minor '
                      'literalness when the meaning is correct. Use the example '
                      'index "i".')
    if "tags" in dimensions:
        checks.append('- "tags": a SEMANTIC tag names a domain the HEADWORD does '
                      'not belong to AT ALL (e.g. "clothing" on a word for a bag, '
                      '"food" on an onomatopoeia, "animal-mammal" on an ink pad). '
                      'Judge against the headword and gloss, NOT the example '
                      'topics. BREADTH IS NEVER A REASON: never report a tag as '
                      'too broad, too narrow, too vague, or replaceable by a more '
                      'specific one, and never propose adding a tag. The tags '
                      '"general", "descriptive", "expression", "onomatopoeia", '
                      '"grammatical", "action", and "abstract" are always '
                      'acceptable. Do not check whether a tag is in the valid '
                      'list — software does that. Register labels (formality, '
                      'politeness): report ONLY when a sentence in the notes '
                      'explicitly contradicts the label, and put that sentence '
                      'verbatim in "quote"; a register flag without a verbatim '
                      'quote is discarded.')
    if "notes" in dimensions:
        checks.append('- "notes": a factual, grammatical, or usage claim in the '
                      'notes is WRONG — e.g. a false grammar rule ("attaches only '
                      'to the past tense"), a reversed direction or order, a wrong '
                      'statement about what another word means or which particle '
                      'a verb takes, a wrong kanji or etymology claim, a wrong '
                      'cultural fact. Put the offending sentence verbatim in '
                      '"quote". Do NOT report style, length, repetition, missing '
                      'information, or matters of opinion; do NOT report claims '
                      'that are merely simplified for learners if they are not '
                      'false. Severity "error" only.')
    tag_list = ", ".join(sorted(VALID_SEMANTIC))
    return f"""You are a meticulous bilingual (Japanese-English) lexicographer reviewing one \
entry of a Japanese-English dictionary for intermediate learners. Your job is to catch \
REAL ERRORS that would mislead a learner — not to suggest improvements. Most entries \
you see are correct: the EXPECTED response is the empty array []. Report an issue only \
when you are confident something is factually wrong.

Report an issue ONLY for these cases:
{chr(10).join(checks)}

Project conventions — these are deliberate; do NOT report them as issues:
- politeness "plain" is the default for ordinary (non-keigo) vocabulary.
- formality "neutral" is the default; many everyday words carry it.
- Kinship terms (母, 父, 兄, 姉 …) are tagged politeness "humble" by design \
(they are the in-group reference forms).
- suru-verbs and action nouns carry the semantic tag "action" by convention.
- Glosses are deliberately concise; explanations target intermediate learners; \
example translations favor natural English over word-for-word renderings.
- Notes are deliberately selective; they need not mention every sense or use.

Valid semantic tags, for reference only (do not report list membership):
{tag_list}

Severity: use "error" for issues that would actively mislead a learner (wrong \
meaning, wrong tag, false claim). Use "warn" SPARINGLY — only when something is \
likely wrong but you cannot be certain. Do not use "warn" for style.

Entry (JSON):
{json.dumps(payload, ensure_ascii=False, indent=2)}

Respond with ONLY a JSON array of issue objects (no prose, no code fences). Each object:
{{"dimension": "gloss|translation|tags|notes", "location": "<gloss | definitions[n].gloss | examples[i] | tags.semantic | tags.formality | tags.politeness | notes>", "severity": "error|warn", "concern": "<what is wrong, briefly>", "suggestion": "<concrete fix>", "quote": "<verbatim sentence from the entry, required for tags.formality, tags.politeness, and notes>"}}

If the entry is accurate on the checked dimensions, respond with exactly: []"""


# --------------------------------------------------------------------------- #
# Code-side checks and post-filters
# --------------------------------------------------------------------------- #
def offvocab_issues(entry):
    """Deterministic: one issue per semantic tag outside VALID_SEMANTIC."""
    tags = (entry.get("metadata") or {}).get("tags", {}) or {}
    out = []
    for tag in tags.get("semantic", []) or []:
        if tag in VALID_SEMANTIC:
            continue
        target = TAG_MIGRATION.get(tag)
        out.append({
            "dimension": "tags",
            "location": "tags.semantic",
            "severity": "error",
            "concern": f"semantic tag '{tag}' is not in the closed vocabulary",
            "suggestion": (f"migrate to '{target}'" if target
                           else "migrate to the best in-list tag"),
            "family": "offvocab",
            "source": "code",
            "tag": tag,
        })
    return out


def _norm_ws(text):
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def quote_in_notes(quote, notes_plain):
    """True when the quote (normalized) is found in the plain notes.

    Accepts the whole quote, or its first 25 characters, so a model that trims
    a trailing clause still passes; a fabricated quote does not."""
    q = _norm_ws(quote)
    if len(q) < 8:
        return False
    n = _norm_ws(notes_plain)
    return q in n or q[:25] in n


def assign_family(issue):
    dim = issue.get("dimension")
    loc = str(issue.get("location") or "")
    text = " ".join(str(issue.get(k) or "") for k in ("concern", "suggestion"))
    if issue.get("family"):
        return issue["family"]
    if dim == "tags":
        if OFFVOCAB_RE.search(text):
            return "offvocab"
        if "formality" in loc or "politeness" in loc or REGISTER_RE.search(text):
            return "register"
        if BREADTH_RE.search(text):
            return "breadth"
        return "wrong-category"
    if dim == "notes":
        return "notes-fact"
    if dim == "gloss":
        return "style" if STYLE_RE.search(text) else "gloss-meaning"
    if dim == "translation":
        return "style" if STYLE_RE.search(text) else "translation-meaning"
    return "other"


def postfilter_issues(entry, issues, dimensions, keep_warn=False):
    """Apply the code-side noise filters. Returns (kept, dropped_by_family)."""
    kept, dropped = [], {}

    def drop(family):
        dropped[family] = dropped.get(family, 0) + 1

    tags = (entry.get("metadata") or {}).get("tags", {}) or {}
    semantic = [t for t in (tags.get("semantic") or []) if isinstance(t, str)]
    present_values = set(semantic)
    for k in ("formality", "politeness"):
        if tags.get(k):
            present_values.add(str(tags[k]))
    notes_plain = plain_jp(entry.get("notes") or "")

    for it in issues or []:
        if not isinstance(it, dict) or it.get("dimension") not in dimensions:
            continue
        dim = it["dimension"]
        sev = str(it.get("severity") or "error").lower()
        loc = str(it.get("location") or "")
        text = " ".join(str(it.get(k) or "") for k in ("concern", "suggestion", "location"))
        family = assign_family(it)
        it["family"] = family

        if sev == "warn" and not keep_warn:
            drop("warn-" + family)
            continue

        if dim == "tags":
            if family == "offvocab":
                drop("offvocab-model")  # handled deterministically in code
                continue
            if family == "breadth":
                drop("breadth")
                continue
            if family == "register":
                q = it.get("quote")
                if not q or not quote_in_notes(q, notes_plain):
                    drop("register-noquote")
                    continue
            else:
                # A wrong-category flag must name a tag the entry carries, and
                # must not merely restate a fallback tag as the problem.
                named = {tok for tok in TAG_TOKEN_RE.findall(text.lower())
                         if tok in present_values}
                if not named:
                    drop("absent-tag")
                    continue
                if named <= FALLBACK_TAGS:
                    drop("fallback-tag")
                    continue
                sugg = str(it.get("suggestion") or "").lower()
                sugg_tags = {tok for tok in TAG_TOKEN_RE.findall(sugg)
                             if tok in VALID_SEMANTIC}
                sugg_looks_like_tags = bool(TAG_TOKEN_RE.fullmatch(sugg.strip().strip("'\"")))
                if sugg_looks_like_tags and not sugg_tags:
                    drop("out-of-list-suggestion")
                    continue
        elif dim == "notes":
            q = it.get("quote")
            if not q or not quote_in_notes(q, notes_plain):
                drop("notes-noquote")
                continue
        elif dim in ("gloss", "translation"):
            if family == "style":
                drop("style")
                continue
        kept.append(it)
    return kept, dropped


def filter_issues(issues, dimensions):
    """Keep only well-formed issue dicts on the requested dimensions."""
    if not isinstance(issues, list):
        return []
    return [it for it in issues if isinstance(it, dict)
            and it.get("dimension") in dimensions]


def review_entry(entry, api_key, model, dimensions, keep_warn=False):
    """Returns (issues, dropped, prompt). issues is None on an API/parse failure."""
    prompt = build_prompt(entry, dimensions)
    resp = call_openrouter(api_key, model, prompt)
    raw = parse_model_response(resp)
    if raw is None:
        return None, {}, prompt
    issues, dropped = postfilter_issues(entry, filter_issues(raw, dimensions),
                                        dimensions, keep_warn=keep_warn)
    if "tags" in dimensions:
        issues = offvocab_issues(entry) + issues
    return issues, dropped, prompt


def _append_flag_line(record):
    """Append one line per flagged entry to the tracked flags file."""
    if not record.get("issues"):
        return
    FLAGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    line = {"entry_id": record["entry_id"], "reviewed_at": record["reviewed_at"],
            "prompt_version": record["prompt_version"],
            "issues": [{k: it.get(k) for k in ("dimension", "location", "severity",
                                                 "concern", "suggestion", "family")}
                       for it in record["issues"]]}
    with FLAGS_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def save_review(entry, model, dimensions, issues, dropped=None):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    eid = entry.get("id")
    record = {
        "entry_id": eid,
        "headword": entry.get("headword"),
        "model": model,
        "prompt_version": PROMPT_VERSION,
        "dimensions": list(dimensions),
        "reviewed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "entry_modified": (entry.get("metadata") or {}).get("modified"),
        "summary": {"flagged": len(issues),
                    "dropped": sum((dropped or {}).values())},
        "dropped": dropped or {},
        "issues": issues,
    }
    (OUT_DIR / f"{eid}.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _append_flag_line(record)


def run_review(entries, model, dimensions, budget, dry_run, keep_warn=False):
    if dry_run:
        for entry, _ in entries[:3]:
            print(f"--- prompt for {entry.get('id')} ---")
            print(build_prompt(entry, dimensions))
            print()
        print(f"(dry-run: {len(entries)} entries would be reviewed, no API calls)")
        return 0.0

    api_key = get_api_key()
    total_cost = 0.0
    reviewed = flagged = failed = 0
    dropped_total = {}
    for entry, _ in entries:
        prompt = build_prompt(entry, dimensions)
        est = estimate_cost(model, rough_token_count(prompt), 400)
        if budget is not None and total_cost + est > budget:
            print(f"\nBudget limit reached (${total_cost:.4f} + ${est:.4f} > "
                  f"${budget:.2f}). Stopping.")
            break
        issues, dropped, _ = review_entry(entry, api_key, model, dimensions,
                                          keep_warn=keep_warn)
        total_cost += est
        if issues is None:
            failed += 1
            print(f"  {entry.get('id')}: parse/API failure, skipped")
            continue
        for k, v in dropped.items():
            dropped_total[k] = dropped_total.get(k, 0) + v
        save_review(entry, model, dimensions, issues, dropped)
        reviewed += 1
        if issues:
            flagged += 1
        print(f"  {entry.get('id')} {entry.get('headword','')}: "
              f"{len(issues)} issue(s), {sum(dropped.values())} filtered  (~${est:.4f})")
    print(f"\nReviewed: {reviewed}, Flagged: {flagged}, Failed: {failed}, "
          f"Est. cost: ${total_cost:.4f}")
    if dropped_total:
        print("Filtered by family: " + ", ".join(
            f"{k}={v}" for k, v in sorted(dropped_total.items())))
    print(f"Review files in {OUT_DIR.relative_to(PROJECT_ROOT)}/ "
          f"(flag lines appended to {FLAGS_FILE.relative_to(PROJECT_ROOT)})")
    return total_cost


def run_report():
    if not OUT_DIR.exists():
        print("No accuracy reviews yet.")
        return
    files = sorted(OUT_DIR.glob("*.json"))
    total = flagged = 0
    by_dim, by_family, dropped = {}, {}, {}
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        total += 1
        if d.get("issues"):
            flagged += 1
        for it in d.get("issues", []):
            by_dim[it.get("dimension")] = by_dim.get(it.get("dimension"), 0) + 1
            fam = it.get("family") or assign_family(it)
            by_family[fam] = by_family.get(fam, 0) + 1
        for k, v in (d.get("dropped") or {}).items():
            dropped[k] = dropped.get(k, 0) + v
    print(f"Accuracy reviews on disk: {total} entries, {flagged} with issues")
    for dim in DIMENSIONS:
        if dim in by_dim:
            print(f"  {dim:12} {by_dim[dim]} issue(s)")
    if by_family:
        print("By family: " + ", ".join(f"{k}={v}" for k, v in sorted(by_family.items())))
    if dropped:
        print("Filtered by family: " + ", ".join(f"{k}={v}" for k, v in sorted(dropped.items())))


def main():
    ap = argparse.ArgumentParser(
        description="Cross-model accuracy review (gloss/translation/tags/notes).")
    ap.add_argument("--ids", help="Comma-separated entry IDs (5-digit numeric).")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--dimensions", default=",".join(DIMENSIONS),
                    help="Comma-separated subset of: gloss,translation,tags,notes")
    ap.add_argument("--budget", type=float, help="Stop when estimated cost exceeds this (USD).")
    ap.add_argument("--keep-warn", action="store_true",
                    help="Keep warn-severity issues (dropped by default; ~1%% precision).")
    ap.add_argument("--dry-run", action="store_true", help="Print prompts; no API calls.")
    ap.add_argument("--report", action="store_true", help="Summarize existing accuracy reviews.")
    args = ap.parse_args()

    if args.report:
        run_report()
        return 0

    dims = tuple(d.strip() for d in args.dimensions.split(",") if d.strip() in DIMENSIONS)
    if not dims:
        print("No valid dimensions selected.", file=sys.stderr)
        return 1

    ids = None
    if args.ids:
        ids = {f"{int(x):05d}" for x in args.ids.split(",") if x.strip().isdigit()}
    entries = find_entries(ids=ids, id_range=tuple(args.range) if args.range else None)
    if not entries:
        print("No matching entries found.", file=sys.stderr)
        return 1

    run_review(entries, args.model, dims, args.budget, args.dry_run,
               keep_warn=args.keep_warn)
    return 0


if __name__ == "__main__":
    sys.exit(main())
