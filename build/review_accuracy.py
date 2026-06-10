#!/usr/bin/env python3
"""Cross-model accuracy review: glosses, example translations, semantic tags.

Companion to review_runner.py (which checks furigana readings). This sends each
entry to a model via OpenRouter and asks for a conservative critique across three
dimensions a second model is well-placed to catch:

  gloss        Does the gloss/definition accurately render the headword's meaning?
  translation  Is each example's English a faithful, natural rendering of the JP?
  tags         Are the SEMANTIC tags right for the headword (not the example
               topics)? This is the robust fix for the pervasive tag-drift
               problem (Cleanup Backlog P11) that the keyword heuristic in
               check_tag_drift.py cannot judge precisely.

Output is a per-entry JSON review file under reviews/accuracy/{id}.json with an
APPLY/REJECT/FLAG-ready issue list. Claude (the Routine's accuracy-review mode)
then evaluates each issue with its own judgment — nothing is auto-applied.

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

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
OUT_DIR = PROJECT_ROOT / "reviews" / "accuracy"

DEFAULT_MODEL = "google/gemini-2.5-flash"
DIMENSIONS = ("gloss", "translation", "tags")

# Prompt revision marker, recorded in each review file so calibration stats can
# be segmented by prompt version. v1 (2026-06-09) produced ~1.5% flag precision
# on basic-tier entries (413 issues -> 6 applies in 00451-00650); v2 (2026-06-10)
# embeds project conventions + the valid tag vocabulary and raises the
# materiality bar. See reviews/decisions.jsonl for the evidence.
PROMPT_VERSION = 2

FURIGANA_RE = re.compile(r"\{([^|]+)\|[^}]+\}")
LINK_TAIL_RE = re.compile(r"→[^⟧]*⟧")


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


def entry_payload(entry):
    tags = (entry.get("metadata") or {}).get("tags", {}) or {}
    defs = []
    for i, d in enumerate(entry.get("definitions", []) or []):
        defs.append({"sense": d.get("sense_number", i + 1),
                     "gloss": d.get("gloss"), "explanation": d.get("explanation")})
    exs = []
    for i, ex in enumerate(entry.get("examples", []) or []):
        exs.append({"i": i, "japanese": plain_jp(ex.get("japanese")),
                    "english": ex.get("english")})
    return {
        "headword": plain_jp(entry.get("headword")),
        "reading": entry.get("reading"),
        "pos": tags.get("pos", []),
        "semantic_tags": tags.get("semantic", []),
        "formality": tags.get("formality"),
        "politeness": tags.get("politeness"),
        "gloss": entry.get("gloss"),
        "definitions": defs,
        "examples": exs,
    }


def build_prompt(entry, dimensions):
    payload = entry_payload(entry)
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
        checks.append('- "tags": a SEMANTIC tag is clearly wrong for the '
                      'HEADWORD\'s own meaning (e.g. "clothing" on a word for a '
                      'bag, "food" on an onomatopoeia). Judge the tag against the '
                      'headword and gloss, NOT against the topics of the example '
                      'sentences (tags are often wrongly copied from example '
                      'topics). Suggested replacement tags MUST come from the '
                      'valid tag list below — never invent a tag. Also flag a '
                      'clearly wrong formality label (e.g. a formal/technical '
                      'term labeled "informal").')
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
- "general", "descriptive", "expression", "onomatopoeia", "grammatical" are \
legitimate fallback tags for words that fit no concrete category.
- Glosses are deliberately concise; explanations target intermediate learners; \
example translations favor natural English over word-for-word renderings.

Valid semantic tags (the ONLY allowed values):
{", ".join(sorted(VALID_SEMANTIC))}

Severity: use "error" for issues that would actively mislead a learner (wrong \
meaning, wrong tag). Use "warn" SPARINGLY — only when something is likely wrong \
but you cannot be certain. Do not use "warn" for style.

Entry (JSON):
{json.dumps(payload, ensure_ascii=False, indent=2)}

Respond with ONLY a JSON array of issue objects (no prose, no code fences). Each object:
{{"dimension": "gloss|translation|tags", "location": "<gloss | definitions[n].gloss | examples[i] | tags.semantic | tags.formality | tags.politeness>", "severity": "error|warn", "concern": "<what is wrong, briefly>", "suggestion": "<concrete fix>"}}

If the entry is accurate on the checked dimensions, respond with exactly: []"""


def filter_issues(issues, dimensions):
    """Keep only well-formed issue dicts on the requested dimensions."""
    if not isinstance(issues, list):
        return []
    return [it for it in issues if isinstance(it, dict)
            and it.get("dimension") in dimensions]


def review_entry(entry, api_key, model, dimensions):
    prompt = build_prompt(entry, dimensions)
    resp = call_openrouter(api_key, model, prompt)
    issues = parse_model_response(resp)
    if issues is None:
        return None, prompt
    return filter_issues(issues, dimensions), prompt


def save_review(entry, model, dimensions, issues):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    eid = entry.get("id")
    record = {
        "entry_id": eid,
        "headword": entry.get("headword"),
        "model": model,
        "prompt_version": PROMPT_VERSION,
        "dimensions": list(dimensions),
        "reviewed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": {"flagged": len(issues)},
        "issues": issues,
    }
    (OUT_DIR / f"{eid}.json").write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_review(entries, model, dimensions, budget, dry_run):
    if dry_run:
        for entry, _ in entries[:3]:
            print(f"--- prompt for {entry.get('id')} ---")
            print(build_prompt(entry, dimensions))
            print()
        print(f"(dry-run: {len(entries)} entries would be reviewed, no API calls)")
        return 0.0

    api_key = get_api_key()
    total_cost = 0.0
    reviewed = flagged = 0
    for entry, _ in entries:
        prompt = build_prompt(entry, dimensions)
        est = estimate_cost(model, rough_token_count(prompt), 400)
        if budget is not None and total_cost + est > budget:
            print(f"\nBudget limit reached (${total_cost:.4f} + ${est:.4f} > "
                  f"${budget:.2f}). Stopping.")
            break
        issues, _ = review_entry(entry, api_key, model, dimensions)
        total_cost += est
        if issues is None:
            print(f"  {entry.get('id')}: parse/API failure, skipped")
            continue
        save_review(entry, model, dimensions, issues)
        reviewed += 1
        if issues:
            flagged += 1
        print(f"  {entry.get('id')} {entry.get('headword','')}: "
              f"{len(issues)} issue(s)  (~${est:.4f})")
    print(f"\nReviewed: {reviewed}, Flagged: {flagged}, "
          f"Est. cost: ${total_cost:.4f}")
    print(f"Review files in {OUT_DIR.relative_to(PROJECT_ROOT)}/")
    return total_cost


def run_report():
    if not OUT_DIR.exists():
        print("No accuracy reviews yet.")
        return
    files = sorted(OUT_DIR.glob("*.json"))
    total = flagged = 0
    by_dim = {}
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
    print(f"Accuracy reviews: {total} entries, {flagged} with issues")
    for dim in DIMENSIONS:
        if dim in by_dim:
            print(f"  {dim:12} {by_dim[dim]} issue(s)")


def main():
    ap = argparse.ArgumentParser(description="Cross-model accuracy review (gloss/translation/tags).")
    ap.add_argument("--ids", help="Comma-separated entry IDs (5-digit numeric).")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--dimensions", default=",".join(DIMENSIONS),
                    help="Comma-separated subset of: gloss,translation,tags")
    ap.add_argument("--budget", type=float, help="Stop when estimated cost exceeds this (USD).")
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

    run_review(entries, args.model, dims, args.budget, args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
