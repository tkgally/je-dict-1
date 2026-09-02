#!/usr/bin/env python3
"""Batched cross-model transitivity classifier for verb entries.

About 4,000 verb entries (tags.pos contains verb-godan / verb-ichidan /
verb-suru / verb-kuru / verb-irregular) carry no `tags.transitivity`. This
tool sends verbs to a model via OpenRouter in batches of --batch-size (default
25) — id, headword, reading, POS, gloss and the first two examples — and asks
for a JSON array of {id, transitivity, pair, confidence}. Results go to
reviews/transitivity/{batch-ts}.jsonl (one line per verb); nothing touches the
entries until --apply-confident is combined with --apply.

Reuses review_runner.py's OpenRouter plumbing (get_api_key, call_openrouter,
parse_model_response, estimate_cost, rough_token_count).

Usage:
    # classify (needs OPENROUTER_API_KEY; --dry-run prints the first prompt instead)
    python3 build/review_transitivity.py --range 18700 18760 --budget 0.05
    python3 build/review_transitivity.py --all-missing --budget 2.00
    python3 build/review_transitivity.py --ids 18714,18721 --dry-run
    python3 build/review_transitivity.py --report

    # apply: preview first (default is a dry run), then write
    python3 build/review_transitivity.py --apply-confident 0.9
    python3 build/review_transitivity.py --apply-confident 0.9 --apply
    python3 build/review_transitivity.py --apply-confident 0.9 --apply --entries-dir /tmp/copy/entries

Applying writes tags.transitivity for every result with confidence >= THRESHOLD
whose entry still lacks the tag (an existing, different tag is never
overwritten — it is reported as a conflict). When the model also names a pair
verb that resolves to exactly one existing verb entry (opposite or untagged
transitivity), the prominent_see_also pair link is added in both directions
with notes "transitive"/"intransitive".
"""
import argparse
import json
import re
import sys
import time
from collections import Counter, OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from review_runner import (  # noqa: E402  (sibling module, tested plumbing)
    call_openrouter, parse_model_response, estimate_cost, rough_token_count, get_api_key,
)
from xref_common import (  # noqa: E402
    get_tags, is_verb_pos, load_index, numeric_id, plain_text, read_entry, write_entry,
    insert_key_before_metadata, utc_now,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"
OUT_DIR = PROJECT_ROOT / "reviews" / "transitivity"

DEFAULT_MODEL = "google/gemini-2.5-flash"
DEFAULT_BATCH_SIZE = 25
COMPLETION_TOKENS_PER_VERB = 60      # budget estimate for the JSON reply
PROMPT_VERSION = 1
TRANSITIVITY_VALUES = ("transitive", "intransitive", "both")
OPPOSITE = {"transitive": "intransitive", "intransitive": "transitive"}
PAIR_NULL = {"", "null", "none", "n/a", "na", "-", "—", "なし", "無し"}


# --------------------------------------------------------------------------- #
# Prompt
# --------------------------------------------------------------------------- #
def verb_payload(entry):
    tags = get_tags(entry)
    examples = []
    for ex in (entry.get("examples") or [])[:2]:
        if not isinstance(ex, dict):
            continue
        examples.append({"ja": plain_text(ex.get("japanese")), "en": ex.get("english")})
    return {
        "id": entry.get("id"),
        "headword": plain_text(entry.get("headword")),
        "reading": entry.get("reading"),
        "pos": list(tags.get("pos") or []),
        "gloss": entry.get("gloss"),
        "examples": examples,
    }


def build_prompt(payloads):
    ids = [p["id"] for p in payloads]
    return f"""You are a Japanese linguist annotating verb transitivity for a Japanese-English \
learner's dictionary. Classify each verb below by its ordinary modern usage (the two \
examples illustrate the entry but do not exhaust its usage).

Definitions:
- "transitive": takes a direct object marked with を (you can ask 何を〜?). \
Examples: 閉める, 食べる, 勉強する.
- "intransitive": takes no を direct object; its subject is marked with が. Motion verbs \
that mark a path or point of departure with を (道を歩く, 家を出る, 空を飛ぶ) are still \
intransitive. Examples: 閉まる, 発生する, 出る.
- "both": commonly used both with and without a を object in the same sense, e.g. \
開く(ひらく), 閉じる, 増す, 吹く, 笑う, 休む, 完了する, 実現する. Record "both" faithfully \
when both uses are common; do not force a single value.
- For 〜する verbs: a verb that takes a を object is transitive; one that cannot take を is \
intransitive; many are used both ways (Xを完了する / Xが完了する) — record "both".

"pair": the verb's transitivity counterpart in a morphological 自動詞/他動詞 pair sharing the \
same kanji stem (閉める↔閉まる, 出す↔出る, 落とす↔落ちる, 集める↔集まる), written as a \
dictionary-form headword in kanji. Use null when no such counterpart exists. Never give a \
synonym, a causative (〜させる) or passive form, or the plain noun as the pair. Suru-verbs \
almost never have a pair.

"confidence": your certainty from 0 to 1 that the transitivity value is right.

Verbs (JSON):
{json.dumps(payloads, ensure_ascii=False, indent=1)}

Respond with ONLY a JSON array (no prose, no code fences) containing exactly one object per \
verb, in the same order, with these keys:
{{"id": "<id>", "transitivity": "transitive|intransitive|both", "pair": "<kanji headword or null>", "confidence": 0.0-1.0}}

Expected ids, in order: {", ".join(ids)}"""


# --------------------------------------------------------------------------- #
# Response parsing
# --------------------------------------------------------------------------- #
def _norm_transitivity(value):
    if not isinstance(value, str):
        return None
    v = value.strip().lower()
    aliases = {"vt": "transitive", "vi": "intransitive", "trans": "transitive",
               "intrans": "intransitive", "他動詞": "transitive", "自動詞": "intransitive",
               "transitive/intransitive": "both", "intransitive/transitive": "both",
               "either": "both", "ambitransitive": "both"}
    v = aliases.get(v, v)
    return v if v in TRANSITIVITY_VALUES else None


def _norm_pair(value):
    if value is None:
        return None
    if not isinstance(value, str):
        return None
    v = plain_text(value).strip().strip("「」『』\"'“”")
    v = re.sub(r"\s*[(（].*$", "", v).strip()      # "閉まる (intransitive)" -> 閉まる
    if v.lower() in PAIR_NULL:
        return None
    return v or None


def _norm_confidence(value):
    try:
        c = float(value)
    except (TypeError, ValueError):
        return 0.0
    if c != c:      # NaN
        return 0.0
    return max(0.0, min(1.0, c))


def parse_batch(parsed, expected_ids):
    """Validate a model reply (already JSON-decoded) against the ids sent.

    Returns (results, problems): results is a list of clean dicts
    {id, transitivity, pair, confidence} for ids that were expected and carry a
    valid transitivity; problems is a list of human-readable strings (unknown
    ids, missing ids, invalid values). Invalid transitivity values are dropped
    (never guessed)."""
    problems = []
    results = []
    seen = set()
    if not isinstance(parsed, list):
        return [], [f"reply is not a JSON array ({type(parsed).__name__})"]
    expected = list(expected_ids)
    for i, item in enumerate(parsed):
        if not isinstance(item, dict):
            problems.append(f"item {i} is not an object")
            continue
        eid = item.get("id")
        if not isinstance(eid, str):
            problems.append(f"item {i}: no id")
            continue
        eid = eid.strip()
        if eid not in expected:
            # tolerate a bare 5-digit id
            match = [x for x in expected if x.startswith(eid + "_")] if re.fullmatch(r"\d{5}", eid) else []
            if len(match) == 1:
                eid = match[0]
            else:
                problems.append(f"item {i}: unexpected id {eid!r}")
                continue
        if eid in seen:
            problems.append(f"duplicate result for {eid}")
            continue
        trans = _norm_transitivity(item.get("transitivity"))
        if trans is None:
            problems.append(f"{eid}: invalid transitivity {item.get('transitivity')!r}")
            continue
        seen.add(eid)
        results.append({
            "id": eid,
            "transitivity": trans,
            "pair": _norm_pair(item.get("pair")),
            "confidence": _norm_confidence(item.get("confidence")),
        })
    for eid in expected:
        if eid not in seen:
            problems.append(f"{eid}: no result")
    return results, problems


# --------------------------------------------------------------------------- #
# Selection and classification runs
# --------------------------------------------------------------------------- #
def select_verbs(index, ids=None, id_range=None, include_tagged=False):
    out = []
    for eid, info in index.entries.items():
        if not info.is_verb:
            continue
        n = numeric_id(eid)
        if ids is not None and n not in ids:
            continue
        if id_range is not None and not (id_range[0] <= n <= id_range[1]):
            continue
        if info.transitivity and not include_tagged:
            continue
        out.append(info)
    return sorted(out, key=lambda i: i.id)


def _batches(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]


def _actual_cost(model, resp, fallback):
    usage = (resp or {}).get("usage") if isinstance(resp, dict) else None
    if isinstance(usage, dict) and usage.get("prompt_tokens") is not None:
        return estimate_cost(model, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0))
    return fallback


def run_classification(verbs, model, batch_size, budget, dry_run, sleep_s, out_dir):
    """Classify `verbs` (EntryInfo list). Returns (total_cost, out_path or None)."""
    out_dir = Path(out_dir)
    batch_ts = utc_now().replace("-", "").replace(":", "")
    out_path = out_dir / f"{batch_ts}.jsonl"
    total_cost = 0.0
    n_results = n_problems = 0
    api_key = None if dry_run else get_api_key()
    for bi, batch in enumerate(_batches(verbs, batch_size)):
        payloads = []
        for info in batch:
            entry, _ = read_entry(info.path)
            payloads.append(verb_payload(entry))
        prompt = build_prompt(payloads)
        est = estimate_cost(model, rough_token_count(prompt), COMPLETION_TOKENS_PER_VERB * len(batch))
        if dry_run:
            if bi == 0:
                print("--- first prompt ---")
                print(prompt)
                print("--- end prompt ---")
            total_cost += est
            continue
        if budget is not None and total_cost + est > budget:
            print(f"Budget limit reached (${total_cost:.4f} + ${est:.4f} > ${budget:.2f}); "
                  f"stopping before batch {bi + 1}.")
            break
        resp = call_openrouter(api_key, model, prompt, timeout=120)
        parsed = parse_model_response(resp) if resp else None
        cost = _actual_cost(model, resp, est)
        total_cost += cost
        if parsed is None:
            print(f"  batch {bi + 1}: API/parse failure, {len(batch)} verbs skipped (~${cost:.4f})")
            n_problems += len(batch)
            time.sleep(sleep_s)
            continue
        results, problems = parse_batch(parsed, [p["id"] for p in payloads])
        by_id = {i.id: i for i in batch}
        out_dir.mkdir(parents=True, exist_ok=True)
        stamp = utc_now()
        with out_path.open("a", encoding="utf-8") as fh:
            for r in results:
                info = by_id[r["id"]]
                line = {
                    "id": r["id"], "headword": info.headword_plain, "reading": info.reading,
                    "pos": info.pos, "existing_transitivity": info.transitivity,
                    "transitivity": r["transitivity"], "pair": r["pair"],
                    "confidence": r["confidence"], "model": model, "batch": batch_ts,
                    "batch_index": bi, "prompt_version": PROMPT_VERSION, "reviewed_at": stamp,
                    "est_cost": round(cost / len(batch), 6),
                }
                fh.write(json.dumps(line, ensure_ascii=False) + "\n")
        n_results += len(results)
        n_problems += len(problems)
        print(f"  batch {bi + 1}: {len(results)}/{len(batch)} classified, "
              f"{len(problems)} problem(s), ~${cost:.4f}")
        for pr in problems[:5]:
            print(f"      ! {pr}")
        time.sleep(sleep_s)
    if dry_run:
        print(f"(dry-run: {len(verbs)} verbs in {-(-len(verbs) // batch_size)} batch(es), "
              f"estimated ${total_cost:.4f}, no API calls)")
        return total_cost, None
    print(f"\nClassified {n_results} verb(s), {n_problems} problem(s), est. cost ${total_cost:.4f}")
    if n_results:
        print(f"Results appended to {out_path}")
    return total_cost, (out_path if n_results else None)


# --------------------------------------------------------------------------- #
# Results, report, apply
# --------------------------------------------------------------------------- #
def load_results(paths=None, out_dir=OUT_DIR):
    """Latest result per verb id from the given jsonl files (default: all in out_dir)."""
    files = [Path(p) for p in paths] if paths else sorted(Path(out_dir).glob("*.jsonl"))
    latest = OrderedDict()
    for f in files:
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(rec, dict) or not rec.get("id"):
                continue
            prev = latest.get(rec["id"])
            if prev is None or (rec.get("reviewed_at") or "") >= (prev.get("reviewed_at") or ""):
                latest[rec["id"]] = rec
    return latest


def resolve_pair(pair_text, source, value, index):
    """Resolve the model's pair verb to exactly one existing verb entry.
    Returns (EntryInfo|None, reason)."""
    pair = _norm_pair(pair_text)
    if not pair:
        return None, "no-pair"
    if pair == source.headword_plain:
        return None, "pair-is-self"
    cands = [c for c in index.headword_matches(pair) if c.is_verb and c.id != source.id]
    if value in OPPOSITE:
        cands = [c for c in cands if c.transitivity in (None, OPPOSITE[value])]
    if not cands:
        return None, "pair-no-entry"
    if len(cands) > 1:
        return None, "pair-ambiguous"
    return cands[0], "pair-resolved"


def plan_apply(results, index, threshold):
    """Decide what --apply-confident would write. Returns (changes, stats, details).

    changes: OrderedDict entry_id -> {"transitivity": value|None, "psa": [items]}
    """
    changes = OrderedDict()
    stats = Counter()
    details = []

    def change_for(eid):
        return changes.setdefault(eid, {"transitivity": None, "psa": []})

    def add_psa(src, tgt, note):
        ch = change_for(src.id)
        if any(it["target_id"] == tgt.id for it in ch["psa"]):
            return False
        ch["psa"].append({"target_id": tgt.id, "reading": tgt.reading,
                          "headword": tgt.headword, "note": note})
        return True

    for eid, rec in results.items():
        info = index.get(eid)
        value = rec.get("transitivity")
        conf = _norm_confidence(rec.get("confidence"))
        if info is None:
            stats["entry-missing"] += 1
            continue
        if not info.is_verb:
            stats["not-a-verb"] += 1
            continue
        if value not in TRANSITIVITY_VALUES:
            stats["invalid-value"] += 1
            continue
        if conf < threshold:
            stats["below-threshold"] += 1
            continue
        if info.transitivity and info.transitivity != value:
            stats["conflict-existing-tag"] += 1
            details.append(f"{eid} {info.headword_plain}: entry says {info.transitivity}, "
                           f"model says {value} ({conf:.2f}) — left unchanged")
            continue
        did = False
        if info.transitivity is None:
            change_for(eid)["transitivity"] = value
            stats["set-transitivity"] += 1
            did = True
        else:
            stats["already-tagged-same"] += 1
        if value in OPPOSITE and rec.get("pair"):
            target, reason = resolve_pair(rec.get("pair"), info, value, index)
            stats[reason] += 1
            if target is not None:
                if info.references(target):
                    stats["pair-link-exists"] += 1
                elif add_psa(info, target, OPPOSITE[value]):
                    stats["psa-added"] += 1
                    did = True
                if target.references(info):
                    stats["pair-backlink-exists"] += 1
                elif add_psa(target, info, value):
                    stats["psa-backlink-added"] += 1
                    did = True
                    if target.transitivity is None:
                        stats["pair-untagged"] += 1
            elif reason in ("pair-ambiguous", "pair-no-entry"):
                details.append(f"{eid} {info.headword_plain}: pair {rec.get('pair')!r} {reason}")
        if not did:
            stats["nothing-to-do"] += 1
    changes = OrderedDict((k, v) for k, v in changes.items() if v["transitivity"] or v["psa"])
    return changes, stats, details


def apply_changes(changes, index, modified=None):
    """Write the planned changes. Returns the list of rewritten entry ids."""
    stamp = modified or utc_now()
    written = []
    for eid, ch in changes.items():
        info = index.get(eid)
        entry, nl = read_entry(info.path)
        touched = False
        if ch["transitivity"]:
            meta = entry.setdefault("metadata", {})
            tags = meta.get("tags")
            if not isinstance(tags, dict):
                tags = {}
                meta["tags"] = tags
            if not tags.get("transitivity"):
                tags["transitivity"] = ch["transitivity"]
                touched = True
        if ch["psa"]:
            psa = entry.get("prominent_see_also")
            psa = list(psa) if isinstance(psa, list) else []
            for item in ch["psa"]:
                if any(isinstance(x, dict) and x.get("target_id") == item["target_id"] for x in psa):
                    continue
                psa.append(dict(item))
                touched = True
            insert_key_before_metadata(entry, "prominent_see_also", psa)
        if not touched:
            continue
        write_entry(info.path, entry, trailing_newline=nl, modified=stamp)
        written.append(eid)
    return written


def print_plan(changes, stats, details, index, threshold, applied):
    print(f"\n=== Transitivity apply plan (threshold {threshold}) ===")
    for eid, ch in changes.items():
        info = index.get(eid)
        bits = []
        if ch["transitivity"]:
            bits.append(f"transitivity={ch['transitivity']}")
        for it in ch["psa"]:
            bits.append(f"prominent_see_also → {it['target_id']} ({it['note']})")
        print(f"  {eid} {info.headword_plain}: " + "; ".join(bits))
    print("Stats: " + ", ".join(f"{k} {v}" for k, v in sorted(stats.items())))
    for d in details[:40]:
        print("  ! " + d)
    if applied is None:
        print(f"DRY RUN: {len(changes)} entry file(s) would change (add --apply to write)")
    else:
        print(f"APPLIED: {len(applied)} entry file(s) rewritten")


def run_report(results, index=None):
    print(f"Transitivity reviews: {len(results)} verb(s) with a latest result")
    if not results:
        return
    by_val = Counter(r.get("transitivity") for r in results.values())
    print("  by value: " + ", ".join(f"{k} {v}" for k, v in by_val.most_common()))
    buckets = Counter()
    for r in results.values():
        c = _norm_confidence(r.get("confidence"))
        buckets[">=0.9" if c >= 0.9 else ("0.7-0.9" if c >= 0.7 else "<0.7")] += 1
    print("  confidence: " + ", ".join(f"{k} {buckets[k]}" for k in (">=0.9", "0.7-0.9", "<0.7")))
    with_pair = [r for r in results.values() if r.get("pair")]
    print(f"  pair named: {len(with_pair)}")
    agree = disagree = 0
    for r in results.values():
        ex = r.get("existing_transitivity")
        if ex:
            if ex == r.get("transitivity"):
                agree += 1
            else:
                disagree += 1
    if agree or disagree:
        print(f"  agreement with existing tags: {agree} agree, {disagree} disagree")
    cost = sum(float(r.get("est_cost") or 0) for r in results.values())
    print(f"  est. cost of these results: ${cost:.4f}")
    by_model = Counter(r.get("model") for r in results.values())
    print("  models: " + ", ".join(f"{k} {v}" for k, v in by_model.most_common()))
    if index is not None:
        res = Counter()
        for r in with_pair:
            info = index.get(r["id"])
            if info is None:
                continue
            _, reason = resolve_pair(r["pair"], info, r.get("transitivity"), index)
            res[reason] += 1
        print("  pair resolution: " + ", ".join(f"{k} {v}" for k, v in res.most_common()))


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def parse_id_list(text):
    ids = set()
    for tok in re.split(r"[,\s]+", text or ""):
        tok = tok.strip()
        if not tok:
            continue
        n = int(tok) if tok.isdigit() else numeric_id(tok)
        if n is not None:
            ids.add(n)
    return ids


def main(argv=None):
    ap = argparse.ArgumentParser(description="Batched cross-model verb transitivity classifier.")
    sel = ap.add_argument_group("selection")
    sel.add_argument("--ids", help="Comma-separated entry IDs (5-digit or full).")
    sel.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    sel.add_argument("--all-missing", action="store_true", help="Every verb lacking tags.transitivity.")
    sel.add_argument("--include-tagged", action="store_true",
                     help="Also classify verbs that already have a tag (to measure agreement).")
    run = ap.add_argument_group("classification")
    run.add_argument("--model", default=DEFAULT_MODEL)
    run.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    run.add_argument("--budget", type=float, help="Stop when the estimated cost would exceed this (USD).")
    run.add_argument("--sleep", type=float, default=1.0, help="Seconds between batches.")
    run.add_argument("--out-dir", default=str(OUT_DIR))
    ap.add_argument("--dry-run", action="store_true",
                    help="Classification: print the first prompt, no API calls. Apply: preview only.")
    ap.add_argument("--report", action="store_true", help="Summarize existing results.")
    ap.add_argument("--results", nargs="*", metavar="JSONL", help="Result files to use (default: all).")
    ap.add_argument("--apply-confident", type=float, metavar="THRESHOLD",
                    help="Apply results with confidence >= THRESHOLD (preview unless --apply).")
    ap.add_argument("--apply", action="store_true", help="With --apply-confident: actually write.")
    ap.add_argument("--entries-dir", default=str(ENTRIES_DIR),
                    help="Entries directory to read AND write (use a copy for testing).")
    args = ap.parse_args(argv)

    entries_dir = Path(args.entries_dir)
    if not entries_dir.is_dir():
        print(f"Not a directory: {entries_dir}", file=sys.stderr)
        return 1
    if args.apply and args.apply_confident is None:
        ap.error("--apply only makes sense with --apply-confident THRESHOLD")
    if args.apply and args.dry_run:
        ap.error("--apply and --dry-run are mutually exclusive")

    if args.report:
        index = load_index(entries_dir)
        run_report(load_results(args.results, args.out_dir), index)
        return 0

    if args.apply_confident is not None:
        index = load_index(entries_dir)
        results = load_results(args.results, args.out_dir)
        changes, stats, details = plan_apply(results, index, args.apply_confident)
        applied = None
        if args.apply:
            applied = apply_changes(changes, index)
        print_plan(changes, stats, details, index, args.apply_confident, applied)
        return 0

    if not (args.ids or args.range or args.all_missing):
        ap.error("select verbs with --ids, --range or --all-missing (or use --report / --apply-confident)")
    ids = parse_id_list(args.ids) if args.ids else None
    id_range = tuple(args.range) if args.range else None
    index = load_index(entries_dir)
    verbs = select_verbs(index, ids, id_range, include_tagged=args.include_tagged)
    if not verbs:
        print("No matching verbs (all already tagged? try --include-tagged).")
        return 0
    print(f"{len(verbs)} verb(s) selected; model {args.model}; batch size {args.batch_size}")
    run_classification(verbs, args.model, args.batch_size, args.budget, args.dry_run,
                       args.sleep, args.out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
