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
    out-of-list suggestions, formality flags on an entry already tagged formal
    that propose no other allowed value (2026-09-27: "literary" is not a value),
    and (by default) all `warn`-severity issues, which measured ~1% precision;
  * stamps every surviving issue with a regex-assigned `family` so precision can
    be computed per family from reviews/decisions.jsonl without free-text notes.
Dropped issues are counted per family in the review file (`dropped`), so the
filter itself stays measurable.

Reuses review_runner.py's OpenRouter plumbing. Respects a per-invocation
--budget (USD, estimated); the Routine enforces the $5/day cap via the ledger.
--workers N (default 4) runs N calls at once; output stays in entry order.

Second reviewer (2026-10-25, enhancement/claude-backends-2026-10-25/REPORT.md).
`--second claude:opus` reviews the same entries again with Claude Opus on the
subscription (build/claude_backend.py), one entry per call: on 200 entries it
found as many real errors as gpt-6.1-sol, and a different quarter of them. The
Claude reviewer gets prompt version 5 (v4 plus a paragraph naming the error
classes the adjudication has been accepting: false absolutes such as "only" or
"exclusively", false claims about a neighbouring word, reversed glosses, shifted
translations, wrong etymology), and its `warn` flags are kept: it marks many
real errors `warn` (about 90% held up), unlike gemini-2.5-flash, whose warns
were about 1% right. Its reviews go to reviews/accuracy/{id}.claude.json; its
flag lines carry `"model"`. It costs no money; the subscription guard in
claude_backend.py stops it before it can starve the Routine's own sessions.

Usage:
    python3 build/review_accuracy.py --ids 05891,05907 --budget 0.50
    python3 build/review_accuracy.py --range 5800 5900 --budget 1.00
    python3 build/review_accuracy.py --range 5800 6700 --budget 1.00 --workers 8
    python3 build/review_accuracy.py --ids 05907 --dimensions tags --dry-run
    python3 build/review_accuracy.py --report
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from review_runner import (  # noqa: E402  (sibling module, tested plumbing)
    call_openrouter, parse_model_response, estimate_cost, rough_token_count,
    get_api_key,
)
from validate_tags import VALID_SEMANTIC  # noqa: E402
import claude_backend  # noqa: E402

try:  # 1:1 migration map for common off-vocabulary tags (optional)
    from check_tag_drift import TAG_MIGRATION  # noqa: E402
except Exception:  # pragma: no cover - defensive
    TAG_MIGRATION = {}

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
OUT_DIR = PROJECT_ROOT / "reviews" / "accuracy"
FLAGS_FILE = PROJECT_ROOT / "reviews" / "accuracy_flags.jsonl"

# gpt-6.1-sol since 2026-10-23 (enhancement/assessment-2026-10-23.md): on 149 entries
# gemini-2.5-flash had passed, it found about 12 real errors (precision ~80%)
DEFAULT_MODEL = "openai/gpt-6.1-sol"
DIMENSIONS = ("gloss", "translation", "tags", "notes")

# Prompt revision marker, recorded in each review file so calibration stats can
# be segmented by prompt version. v1 (2026-06-09) ~1.5% flag precision; v2
# (2026-06-10) embedded project conventions; v3 (2026-06-11) followed the
# taxonomy expansion; v4 (2026-09-02) adds the notes dimension, moves
# off-vocabulary detection into code, and post-filters the measured noise
# families. See reviews/decisions.jsonl for the evidence. v6 (2026-10-27) sends
# the notes with readings as 漢字(かな) and asks for one-line quotes; the quote
# gate then requires the whole quote inside one notes line (backlog item
# reviewer-notes-fact-quote-prefix: notes-fact ran at 33% precision, half of the
# rejects quoting spliced or misattributed text).
PROMPT_VERSION = 6
# v5/v7 = v4/v6 plus CLAUDE_ERROR_CLASSES; used only for the claude: second reviewer.
CLAUDE_PROMPT_VERSION = 7
CLAUDE_WORKERS = 6  # parallel claude processes; the Routine's container has four CPUs

CLAUDE_ERROR_CLASSES = """What counts as WRONG (report these; they are not simplifications):
- an absolute or restriction the language does not have: "only", "exclusively", "always", "never",
  "almost exclusively", "cannot", "is not used in X" when the word is in fact used more widely;
- a claim about ANOTHER word (a synonym, contrast or confusable word named in the notes) that is false,
  including a wrong reading, a wrong meaning or a wrong register for that word;
- a gloss that reverses who does what (give vs take, lend vs borrow, administer vs take) or names a
  different, neighbouring concept (conflict of interest vs. stake in something);
- an English translation that adds, drops or shifts meaning (time, agent, negation, desire, degree);
- a wrong etymology, origin language, kanji explanation or cultural fact.
Do not report style, missing information or emphasis.

"""

# Tags the reviewer must never dispute on breadth grounds.
FALLBACK_TAGS = {"general", "descriptive", "expression", "onomatopoeia",
                 "grammatical", "action", "abstract"}

FURIGANA_RE = re.compile(r"\{([^|]+)\|[^}]+\}")
FURIGANA_RE_READING = re.compile(r"\{([^|]+)\|([^}]+)\}")
# A reading in parentheses right after kanji, as annotated_jp() writes it.
READING_PAREN_RE = re.compile(r"(?<=[\u3400-\u9fff々〆ヶ])[(（][ぁ-ゖー]+[)）]")
ELLIPSIS_RE = re.compile(r"…+|\.\.\.+")
# A link tail never crosses ⟦, so a plain arrow in the prose (食べる → 食べます)
# is left alone instead of swallowing text up to the next link.
LINK_TAIL_RE = re.compile(r"→[^⟧⟦]*⟧")

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


def annotated_jp(text):
    """Strip inline-link syntax and render furigana as 漢字(かな), so the reviewer
    sees which reading the notes mean ({一日|ついたち} vs {一日|いちにち})."""
    if not text:
        return ""
    text = LINK_TAIL_RE.sub("", text)
    text = text.replace("⟦", "").replace("⟧", "")
    return FURIGANA_RE_READING.sub(r"\1(\2)", text)


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
        payload["notes"] = annotated_jp(entry.get("notes") or "")
    return payload


def is_claude(model):
    return str(model or "").startswith("claude:")


def build_prompt(entry, dimensions, model=None):
    prompt = _build_prompt(entry, dimensions)
    if is_claude(model):
        prompt = prompt.replace("Project conventions", CLAUDE_ERROR_CLASSES + "Project conventions", 1)
    return prompt


def _build_prompt(entry, dimensions):
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
                      'false. Severity "error" only. Kanji readings are shown in '
                      'parentheses, 漢字(かな). Each list line ("- X: ...") is '
                      'about the word X that begins it. Copy the quote from ONE '
                      'line of the notes; never join text from different lines '
                      'or bullets.')
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


def _canon_quote(text):
    """Whitespace-normalized, lower-cased, readings 漢字(かな) reduced to 漢字."""
    return _norm_ws(READING_PAREN_RE.sub("", text or ""))


def quote_in_notes(quote, notes_plain):
    """True when the whole quote occurs within one line of the notes.

    The notes may be given plain or annotated (annotated_jp); a quote with or
    without the readings matches either. A quote may skip text with an
    ellipsis, but its pieces must appear in order on the same line, so a quote
    spliced from two bullets, or one whose tail the model rewrote, fails (until
    2026-10-27 a matching first 25 characters was enough)."""
    pieces = [p for p in (_canon_quote(x) for x in ELLIPSIS_RE.split(quote or "")) if p]
    if sum(len(p) for p in pieces) < 8:
        return False
    for line in (notes_plain or "").split("\n"):
        text, pos = _canon_quote(line), 0
        for piece in pieces:
            pos = text.find(piece, pos)
            if pos < 0:
                break
            pos += len(piece)
        else:
            return True
    return False


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


FORMALITY_VALUES = ("formal", "neutral", "informal", "vulgar")


def formality_already_closest(issue, tags):
    """A formality flag on an entry already tagged formal whose suggestion names
    no other allowed value ("literary", "technical", "written", or formal
    again). The closed list has no value above formal, so there is nothing to
    change: 2026-09 accuracy reviews rejected these by the dozen."""
    if "formality" not in str(issue.get("location") or "") or tags.get("formality") != "formal":
        return False
    sugg = str(issue.get("suggestion") or "").lower()
    named = set(re.findall(r"\b(?:in)?formal\b|\bneutral\b|\bvulgar\b", sugg))
    return not (named - {"formal"})


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
                if formality_already_closest(it, tags):
                    drop("register-closest")
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
    """Returns (issues, dropped, prompt). issues is None on an API/parse failure.
    A claude: reviewer gets the v5 prompt and keeps its warn flags."""
    prompt = build_prompt(entry, dimensions, model)
    keep_warn = keep_warn or is_claude(model)
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
            "entry_modified": record.get("entry_modified"),
            "prompt_version": record["prompt_version"],
            "model": record.get("model"),
            "issues": [{k: it.get(k) for k in ("dimension", "location", "severity",
                                                 "concern", "suggestion", "family")}
                       for it in record["issues"]]}
    with FLAGS_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")


def review_path(eid, model):
    """reviews/accuracy/{id}.json for the main reviewer, {id}.claude.json for a claude: one."""
    return OUT_DIR / (f"{eid}.claude.json" if is_claude(model) else f"{eid}.json")


def save_review(entry, model, dimensions, issues, dropped=None):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    eid = entry.get("id")
    record = {
        "entry_id": eid,
        "headword": entry.get("headword"),
        "model": model,
        "prompt_version": CLAUDE_PROMPT_VERSION if is_claude(model) else PROMPT_VERSION,
        "dimensions": list(dimensions),
        "reviewed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "entry_modified": (entry.get("metadata") or {}).get("modified"),
        "summary": {"flagged": len(issues),
                    "dropped": sum((dropped or {}).values())},
        "dropped": dropped or {},
        "issues": issues,
    }
    review_path(eid, model).write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _append_flag_line(record)


def run_review(entries, model, dimensions, budget, dry_run, keep_warn=False, workers=1,
               planned_out=None):
    """Review the entries the budget covers; returns the estimated cost.
    planned_out, if a list, receives the (entry, path) pairs that were sent."""
    if dry_run:
        for entry, _ in entries[:3]:
            print(f"--- prompt for {entry.get('id')} ---")
            print(build_prompt(entry, dimensions, model))
            print()
        print(f"(dry-run: {len(entries)} entries would be reviewed, no API calls)")
        return 0.0

    if is_claude(model):
        ok, why = claude_backend.available()
        if not ok:
            print(f"{model} review skipped: {why}")
            return 0.0
        api_key = None
    else:
        api_key = get_api_key()
    # Choose the entries the budget covers before any call, so the stopping
    # point is the same whatever the number of workers.
    total_cost = 0.0
    planned = []
    for entry, _ in entries:
        est = estimate_cost(model, rough_token_count(build_prompt(entry, dimensions, model)), 400)
        if budget is not None and total_cost + est > budget:
            print(f"\nBudget limit reached (${total_cost:.4f} + ${est:.4f} > "
                  f"${budget:.2f}). Stopping after {len(planned)} entries.")
            break
        total_cost += est
        planned.append((entry, est))
    if planned_out is not None:
        sent = {id(e) for e, _ in planned}
        planned_out.extend(pair for pair in entries if id(pair[0]) in sent)

    def one(item):
        return review_entry(item[0], api_key, model, dimensions, keep_warn=keep_warn)

    # The calls are latency-bound, not quota-bound (tooling backlog 87), so
    # they run in parallel threads; results come back in entry order and all
    # file writes stay in this thread.
    if workers > 1 and len(planned) > 1:
        pool = ThreadPoolExecutor(max_workers=workers)
        results = pool.map(one, planned)
    else:
        pool = None
        results = map(one, planned)
    reviewed = flagged = failed = 0
    dropped_total = {}
    try:
        for (entry, est), (issues, dropped, _) in zip(planned, results):
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
                  f"{len(issues)} issue(s), {sum(dropped.values())} filtered  (~${est:.4f})",
                  flush=True)
    finally:
        if pool is not None:
            pool.shutdown(wait=True)
    print(f"\n{model}: Reviewed: {reviewed}, Flagged: {flagged}, Failed: {failed}, "
          f"Est. cost: ${total_cost:.4f}")
    if is_claude(model):
        print(claude_backend.usage_line())
    if dropped_total:
        print("Filtered by family: " + ", ".join(
            f"{k}={v}" for k, v in sorted(dropped_total.items())))
    print(f"Review files in {OUT_DIR.relative_to(PROJECT_ROOT)}/ "
          f"(flag lines appended to {FLAGS_FILE.relative_to(PROJECT_ROOT)})")
    return total_cost


def review_is_stale(record, entry):
    """True when the entry changed after this review was made.

    A review describes the entry as it was at review time: ``entry_modified``
    holds that version's ``metadata.modified``.  Older artifacts lack the stamp;
    for them the review is stale when the entry was modified after ``reviewed_at``.
    ISO-8601 UTC strings of the same shape compare correctly as text.
    """
    current = (entry.get("metadata") or {}).get("modified")
    if not current:
        return False
    stamped = record.get("entry_modified")
    if stamped:
        return stamped != current
    reviewed_at = record.get("reviewed_at")
    return bool(reviewed_at) and current > reviewed_at


def run_show(entries, include_stale=False):
    """Print the surviving issues of the stored reviews for these entries.

    Reviews older than their entry are listed as STALE without their issues
    (re-run the review instead of adjudicating them), unless include_stale.
    """
    shown = stale = missing = 0
    for entry, _path in entries:
        eid = entry.get("id")
        files = [f for f in (OUT_DIR / f"{eid}.json", OUT_DIR / f"{eid}.claude.json") if f.exists()]
        if not files:
            missing += 1
            continue
        for f in files:
            try:
                record = json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            shown_n, stale_n = _show_record(eid, entry, record, include_stale)
            shown += shown_n
            stale += stale_n
    print(f"{shown} issue(s) shown; {stale} stale review(s)"
          f"{' (issues hidden)' if stale and not include_stale else ''}; "
          f"{missing} entr{'y' if missing == 1 else 'ies'} without a review")


def _show_record(eid, entry, record, include_stale):
    shown = stale = 0
    by = record.get("model") or ""
    is_stale = review_is_stale(record, entry)
    if is_stale:
        stale += 1
        print(f"STALE {eid} ({by}): reviewed {record.get('reviewed_at')}, entry modified "
              f"{(entry.get('metadata') or {}).get('modified')}; re-run the review")
        if not include_stale:
            return shown, stale
    for it in record.get("issues") or []:
        shown += 1
        print(f"## {eid} {it.get('family') or assign_family(it)} {it.get('location')}"
              f" [{it.get('severity')}] ({by})")
        print(f"   concern: {it.get('concern')}")
        if it.get("quote"):
            print(f"   quote: {it.get('quote')}")
        if it.get("suggestion"):
            print(f"   suggestion: {it.get('suggestion')}")
    return shown, stale


def run_report():
    if not OUT_DIR.exists():
        print("No accuracy reviews yet.")
        return
    files = sorted(OUT_DIR.glob("*.json"))
    total = flagged = by_claude = 0
    by_dim, by_family, dropped = {}, {}, {}
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        total += 1
        by_claude += is_claude(d.get("model"))
        if d.get("issues"):
            flagged += 1
        for it in d.get("issues", []):
            by_dim[it.get("dimension")] = by_dim.get(it.get("dimension"), 0) + 1
            fam = it.get("family") or assign_family(it)
            by_family[fam] = by_family.get(fam, 0) + 1
        for k, v in (d.get("dropped") or {}).items():
            dropped[k] = dropped.get(k, 0) + v
    print(f"Accuracy reviews on disk: {total} ({by_claude} by a claude: reviewer), "
          f"{flagged} with issues")
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
    ap.add_argument("--second", metavar="MODEL",
                    help="also review the same entries with this model, e.g. claude:opus "
                         "(headless Claude on the subscription; v5 prompt, warn flags kept)")
    ap.add_argument("--dimensions", default=",".join(DIMENSIONS),
                    help="Comma-separated subset of: gloss,translation,tags,notes")
    ap.add_argument("--budget", type=float, help="Stop when estimated cost exceeds this (USD).")
    ap.add_argument("--keep-warn", action="store_true",
                    help="Keep warn-severity issues (dropped by default; ~1%% precision).")
    ap.add_argument("--workers", type=int, default=4,
                    help="Parallel API calls (default 4; 1 = serial).")
    ap.add_argument("--dry-run", action="store_true", help="Print prompts; no API calls.")
    ap.add_argument("--report", action="store_true", help="Summarize existing accuracy reviews.")
    ap.add_argument("--show", action="store_true",
                    help="Print the stored issues for --ids/--range; reviews older than "
                         "their entry are listed as STALE and their issues hidden.")
    ap.add_argument("--include-stale", action="store_true",
                    help="With --show, print the issues of stale reviews too.")
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

    if args.show:
        run_show(entries, include_stale=args.include_stale)
        return 0

    planned = []
    run_review(entries, args.model, dims, args.budget, args.dry_run,
               keep_warn=args.keep_warn, workers=max(1, args.workers), planned_out=planned)
    if args.second and not args.dry_run:
        print(f"\nSecond reviewer {args.second} on the same {len(planned)} entries")
        run_review(planned, args.second, dims, None, False, keep_warn=args.keep_warn,
                   workers=CLAUDE_WORKERS if is_claude(args.second) else max(1, args.workers))
    return 0


if __name__ == "__main__":
    sys.exit(main())
