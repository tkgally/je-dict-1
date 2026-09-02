#!/usr/bin/env python3
"""Backfill missing register tags (politeness / formality) and vocabulary tier.

Thousands of entries have ``metadata.tags.politeness`` or ``.formality`` missing
or null. The overwhelming default for an ordinary dictionary word is
politeness "plain" and formality "neutral"; this tool sets those defaults
mechanically, but HOLDS OUT (leaves null and lists for a human) any entry whose
text suggests the default might be wrong:

  politeness -> "plain" unless the notes / gloss / definitions mention (case-
      insensitive) honorific, humble, keigo, "polite form(s)", 敬語, 尊敬, 謙譲 or
      丁寧, or the entry is an expression/interjection whose headword contains
      ます / ございます (a built-in polite marker).
  formality  -> "neutral" unless the same text mentions formal / informal /
      formality / casual / slang / vulgar / literary / written / colloquial /
      rough (as whole words; "through" or "roughly" do not count), 書き言葉 or
      話し言葉, or ``tags.style`` is non-empty.
  --tier-general: metadata.vocabulary_tier -> "general" where missing/null
      (new entries always belong to the open "general" tier).

Only the selected fields are touched; existing non-null values are never
changed. Dry run by default; nothing is written without --apply.

Usage:
    python3 build/backfill_register.py                          # dry run, politeness+formality
    python3 build/backfill_register.py --fields politeness      # one field only
    python3 build/backfill_register.py --tier-general           # also backfill the tier
    python3 build/backfill_register.py --report /tmp/register_holdouts.json
    python3 build/backfill_register.py --entries-dir COPY --apply
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_common import (  # noqa: E402
    add_common_args, resolve_apply, parse_ids, iter_entry_paths, load_entry,
    write_entry, touch_modified, utc_now, entry_label,
)
from japanese_utils import strip_furigana  # noqa: E402

POLITENESS_KEYWORDS_RE = re.compile(
    r"\bhonorific(?:s|ally)?\b|\bhumble\b|\bkeigo\b|\bpolite\s+forms?\b|敬語|尊敬|謙譲|丁寧",
    re.IGNORECASE)
FORMALITY_KEYWORDS_RE = re.compile(
    r"\b(?:in)?formal(?:ly|ity)?\b|\bcasual(?:ly)?\b|\bslang(?:y)?\b|\bvulgar(?:ity)?\b"
    r"|\bliterary\b|\bwritten\b|\bcolloquial(?:ly|ism|isms)?\b|\brough\b|書き言葉|話し言葉",
    re.IGNORECASE)
POLITE_HEADWORD_MARKERS = ("ます", "ございます")
# Where a freshly inserted tag key goes, to keep the key order the schema uses.
_TAG_KEY_ORDER = ["pos", "transitivity", "verb_class", "formality", "politeness",
                  "style", "domain", "semantic"]


def entry_text(entry: dict) -> str:
    """Notes + gloss + definition glosses/explanations, joined."""
    parts = [entry.get("gloss") or "", entry.get("notes") or ""]
    for d in entry.get("definitions") or []:
        if isinstance(d, dict):
            parts.append(d.get("gloss") or "")
            parts.append(d.get("explanation") or "")
    return "\n".join(p for p in parts if isinstance(p, str))


def _insert_tag(tags: dict, key: str, value) -> None:
    """Set tags[key]=value, placing a new key at its schema position."""
    if key in tags:
        tags[key] = value
        return
    order = {k: i for i, k in enumerate(_TAG_KEY_ORDER)}
    items = list(tags.items())
    pos = len(items)
    for i, (k, _) in enumerate(items):
        if order.get(k, 99) > order.get(key, 99):
            pos = i
            break
    items.insert(pos, (key, value))
    tags.clear()
    tags.update(items)


def politeness_decision(entry: dict) -> tuple:
    """('set', 'plain') | ('hold', [reasons]) | ('skip', None) if already set."""
    tags = ((entry.get("metadata") or {}).get("tags") or {})
    if tags.get("politeness") is not None:
        return ("skip", None)
    reasons = sorted({m.group(0).lower() for m in POLITENESS_KEYWORDS_RE.finditer(entry_text(entry))})
    pos = set(tags.get("pos") or [])
    if pos & {"expression", "interjection"}:
        hw = strip_furigana(entry.get("headword") or "")
        if any(mk in hw for mk in POLITE_HEADWORD_MARKERS):
            reasons.append("headword contains ます/ございます")
    return ("hold", reasons) if reasons else ("set", "plain")


def formality_decision(entry: dict) -> tuple:
    """('set', 'neutral') | ('hold', [reasons]) | ('skip', None) if already set."""
    tags = ((entry.get("metadata") or {}).get("tags") or {})
    if tags.get("formality") is not None:
        return ("skip", None)
    reasons = sorted({m.group(0).lower() for m in FORMALITY_KEYWORDS_RE.finditer(entry_text(entry))})
    if tags.get("style"):
        reasons.append(f"tags.style={tags['style']}")
    return ("hold", reasons) if reasons else ("set", "neutral")


def tier_decision(entry: dict) -> tuple:
    md = entry.get("metadata") or {}
    if md.get("vocabulary_tier") is not None:
        return ("skip", None)
    return ("set", "general")


def process_entry(entry: dict, fields) -> tuple:
    """Apply the selected backfills in place. Returns (changed_fields, holdouts).

    holdouts: list of (field, reasons)."""
    changed = []
    holdouts = []
    md = entry.setdefault("metadata", {})
    if "politeness" in fields or "formality" in fields:
        tags = md.get("tags")
        if tags is None:
            tags = {}
            md["tags"] = tags
        if "politeness" in fields:
            kind, payload = politeness_decision(entry)
            if kind == "set":
                _insert_tag(tags, "politeness", payload)
                changed.append("politeness")
            elif kind == "hold":
                holdouts.append(("politeness", payload))
        if "formality" in fields:
            kind, payload = formality_decision(entry)
            if kind == "set":
                _insert_tag(tags, "formality", payload)
                changed.append("formality")
            elif kind == "hold":
                holdouts.append(("formality", payload))
    if "tier" in fields:
        kind, payload = tier_decision(entry)
        if kind == "set":
            md["vocabulary_tier"] = payload
            changed.append("vocabulary_tier")
    return changed, holdouts


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(ap)
    ap.add_argument("--fields", type=str, default="politeness,formality",
                    help="Comma-separated subset of politeness,formality,tier (default: politeness,formality)")
    ap.add_argument("--tier-general", action="store_true",
                    help="Also set metadata.vocabulary_tier='general' where missing (adds 'tier' to --fields)")
    ap.add_argument("--report", type=Path, default=None,
                    help="Write the held-out entries (with matched keywords) to this JSON file")
    ap.add_argument("--top", type=int, default=20, help="Hold-out samples to print per field")
    ap.add_argument("--quiet", action="store_true", help="Only print the counts")
    args = ap.parse_args(argv)
    apply = resolve_apply(args)
    fields = {f.strip() for f in args.fields.split(",") if f.strip()}
    if args.tier_general:
        fields.add("tier")
    bad = fields - {"politeness", "formality", "tier"}
    if bad:
        print(f"error: unknown --fields value(s): {sorted(bad)}", file=sys.stderr)
        return 2

    timestamp = utc_now()
    scanned = 0
    changed_entries = 0
    set_counts = Counter()
    hold_counts = Counter()
    keyword_hits = {"politeness": Counter(), "formality": Counter()}
    holdout_rows = {"politeness": [], "formality": []}
    for path in iter_entry_paths(args.entries_dir, parse_ids(args.ids), args.range):
        try:
            entry, raw = load_entry(path)
        except (json.JSONDecodeError, OSError) as e:
            print(f"warning: skipping {path}: {e}", file=sys.stderr)
            continue
        scanned += 1
        changed, holdouts = process_entry(entry, fields)
        label = entry_label(entry, path)
        for fld, reasons in holdouts:
            hold_counts[fld] += 1
            keyword_hits[fld].update(reasons)
            holdout_rows[fld].append({"id": label, "headword": entry.get("headword"),
                                      "gloss": entry.get("gloss"), "reasons": reasons})
        if changed:
            set_counts.update(changed)
            changed_entries += 1
            if apply:
                touch_modified(entry, timestamp)
                write_entry(path, entry, raw)

    mode = "APPLIED" if apply else "DRY RUN"
    print(f"[{mode}] backfill_register: {scanned} entries scanned, {changed_entries} "
          f"{'rewritten' if apply else 'would change'} (fields: {', '.join(sorted(fields))})")
    if "politeness" in fields:
        print(f"  politeness -> 'plain': {set_counts['politeness']}   held for a human: {hold_counts['politeness']}")
    if "formality" in fields:
        print(f"  formality  -> 'neutral': {set_counts['formality']}   held for a human: {hold_counts['formality']}")
    if "tier" in fields:
        print(f"  vocabulary_tier -> 'general': {set_counts['vocabulary_tier']}")
    if not args.quiet:
        for fld in ("politeness", "formality"):
            if fld in fields and hold_counts[fld]:
                print(f"\n{fld} hold-out triggers: " + ", ".join(
                    f"{k}={v}" for k, v in keyword_hits[fld].most_common(15)))
                print(f"{fld} hold-out samples (first {min(args.top, hold_counts[fld])}):")
                for row in holdout_rows[fld][:args.top]:
                    print(f"  {row['id']}: {row['headword']} ({row['gloss']}) — {', '.join(row['reasons'])}")
    if args.report:
        payload = {"generated": timestamp, "fields": sorted(fields), "set": dict(set_counts),
                   "held": dict(hold_counts), "keyword_hits": {k: dict(v) for k, v in keyword_hits.items()},
                   "holdouts": holdout_rows}
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"\nHold-out report written to {args.report}")
    if not apply and changed_entries:
        print("\nDry run — nothing written. Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
