#!/usr/bin/env python3
"""Detect malformed furigana wrappers — a READ-ONLY review-queue generator.

Companion to verify_furigana.py (which flags *missing* furigana). This flags
*malformed* `{kanji|reading}` wrappers so a human/agent can verify and fix each
case. It never modifies entries. Addresses Cleanup Backlog Priority 9 (859
instances / 624 entries; 68 high-severity truncated readings) and Priority 12
(slash-separated dual readings). See planning/wiki/topics/furigana-wrapper-anomalies.md.

Subpatterns (per `{L|R}` wrapper, L = left/surface side, R = right/reading side):
  nested            `{{...}` nested wrappers (invalid; renders wrong)        [error]
  slash-reading     R contains '/', e.g. {村|むら/そん} (non-standard)        [error]
  pure-kana         L has no kanji, e.g. {ところ|所} (reversed) / {どんどん|どんどん} [error/warn]
  o-go-prefix       L starts with お/ご + kanji, e.g. {お酒|おさけ}             [warn]
  reading-truncated okurigana on surface but reading omits it, e.g. {やり方|かた} [error]
  over-wrapped      okurigana inside wrapper but reading covers it, {若い|わかい} [info]

Usage:
    python3 build/check_furigana_format.py                 # human summary + sample
    python3 build/check_furigana_format.py --summary       # counts only
    python3 build/check_furigana_format.py --json          # full JSON queue (for systemic-fix)
    python3 build/check_furigana_format.py --severity error
    python3 build/check_furigana_format.py --range 5000 5500
"""
import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = PROJECT_ROOT / "entries"

WRAPPER_RE = re.compile(r"\{([^|{}]*)\|([^}{]*)\}")
KANJI_RE = re.compile(r"[一-鿿㐀-䶿]")
LINK_TAIL_RE = re.compile(r"→[^⟧]*⟧")


def _hiragana(s):
    return "".join(ch for ch in s if "぀" <= ch <= "ゟ")


def _katakana(s):
    return "".join(ch for ch in s if "゠" <= ch <= "ヿ")

SEVERITY_ORDER = {"error": 0, "warn": 1, "info": 2}


def numeric_id(entry_id):
    m = re.match(r"(\d+)", str(entry_id))
    return int(m.group(1)) if m else None


def iter_entries(id_range=None):
    for path in sorted(ENTRIES_DIR.glob("**/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        nid = numeric_id(data.get("id", path.stem))
        if id_range and nid is not None and not (id_range[0] <= nid <= id_range[1]):
            continue
        yield data, path


def fields_of(data):
    """Yield (field_label, text) for each furigana-bearing field."""
    if data.get("headword"):
        yield "headword", data["headword"]
    for i, ex in enumerate(data.get("examples", []) or []):
        if ex.get("japanese"):
            yield f"examples[{i}].japanese", ex["japanese"]
    if data.get("notes"):
        yield "notes", data["notes"]


def is_subsequence(small, big):
    it = iter(big)
    return all(ch in it for ch in small)


def classify_wrapper(left, right):
    """Return (subpattern, severity, suggestion) or None if well-formed."""
    if "/" in right:
        return ("slash-reading", "error", None)

    if not KANJI_RE.search(left):
        # No kanji on the surface side at all.
        if KANJI_RE.search(right):
            return ("pure-kana", "error", f"{{{right}|{left}}}")  # looks reversed
        if left == right:
            return ("pure-kana", "warn", left)  # redundant {どんどん|どんどん}
        return ("pure-kana", "warn", None)

    # Surface has kanji. Look for kana mixed in (okurigana / prefix).
    surface_hira = _hiragana(left)
    surface_kata = _katakana(left)
    if not surface_hira and not surface_kata:
        return None  # clean all-kanji wrapper

    if left[0] in ("お", "ご") and KANJI_RE.search(left[1:]):
        # Honorific prefix fused inside the wrapper: {お酒|おさけ} -> お{酒|さけ}
        inner = left[1:]
        inner_reading = right[1:] if right[:1] == left[0] else right
        return ("o-go-prefix", "warn", f"{left[0]}{{{inner}|{inner_reading}}}")

    if surface_kata:
        # Kanji mixed with katakana (loanword compound like 筋トレ, or special
        # counters ヶ/ヵ). The reading often renders these in hiragana, which is
        # not a visible bug — too murky to flag here. Skip.
        return None

    # Hiragana okurigana inside the wrapper. If those kana don't appear (in
    # order) in the reading, the reading is truncated -> visibly wrong on site.
    if not is_subsequence(surface_hira, right):
        return ("reading-truncated", "error", None)
    return ("over-wrapped", "info", None)


def scan(id_range=None):
    records = []
    for data, path in iter_entries(id_range):
        eid = data.get("id", path.stem)
        rel = str(path.relative_to(PROJECT_ROOT))
        for label, raw in fields_of(data):
            text = LINK_TAIL_RE.sub("", raw)
            if "{{" in text:
                records.append({
                    "entry_id": eid, "file": rel, "field": label,
                    "subpattern": "nested", "severity": "error",
                    "original": text[text.index("{{"):text.index("{{") + 24],
                    "suggestion": None,
                })
            for m in WRAPPER_RE.finditer(text):
                left, right = m.group(1), m.group(2)
                result = classify_wrapper(left, right)
                if result:
                    sub, sev, sug = result
                    records.append({
                        "entry_id": eid, "file": rel, "field": label,
                        "subpattern": sub, "severity": sev,
                        "original": m.group(0), "suggestion": sug,
                    })
    return records


def main():
    ap = argparse.ArgumentParser(description="Detect malformed furigana wrappers (read-only).")
    ap.add_argument("--json", action="store_true", help="Emit the full JSON review queue.")
    ap.add_argument("--summary", action="store_true", help="Print counts only.")
    ap.add_argument("--severity", choices=["error", "warn", "info"], help="Filter by minimum severity.")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"), help="Limit to an ID range.")
    ap.add_argument("--limit", type=int, default=25, help="Sample size for the default view.")
    args = ap.parse_args()

    records = scan(tuple(args.range) if args.range else None)
    if args.severity:
        thresh = SEVERITY_ORDER[args.severity]
        records = [r for r in records if SEVERITY_ORDER[r["severity"]] <= thresh]

    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    by_sub, by_sev, entries = {}, {}, set()
    for r in records:
        by_sub[r["subpattern"]] = by_sub.get(r["subpattern"], 0) + 1
        by_sev[r["severity"]] = by_sev.get(r["severity"], 0) + 1
        entries.add(r["entry_id"])
    print(f"Malformed furigana wrappers: {len(records)} instances across "
          f"{len(entries)} entries")
    print("  by severity:", ", ".join(f"{k}={v}" for k, v in sorted(by_sev.items())))
    print("  by subpattern:", ", ".join(f"{k}={v}" for k, v in sorted(by_sub.items())))
    if not args.summary and records:
        print(f"\nSample (first {args.limit}, errors first):")
        for r in sorted(records, key=lambda r: SEVERITY_ORDER[r["severity"]])[:args.limit]:
            sug = f"  ->  {r['suggestion']}" if r["suggestion"] else ""
            print(f"  [{r['severity']:5}] {r['entry_id']} {r['field']}: "
                  f"{r['original']} ({r['subpattern']}){sug}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
