#!/usr/bin/env python3
"""Normalize the free-text ``part_of_speech`` display string from ``tags.pos``.

``metadata.tags.pos`` is the canonical part-of-speech list (schema enum);
``part_of_speech`` is the human-readable string the entry page displays
(build/entry_renderer.py shows ONLY this string — the tags are not rendered,
which is why a transitivity qualifier already present in the string is kept
rather than dropped). This tool derives the display string from the tags.

Canonical rendering (chosen to match the spelling that already dominates the
corpus, so the sweep's diff is minimal): one display name per tag, joined with
", " in ``tags.pos`` order —

    noun -> noun                   verb-godan -> verb (godan)
    verb-ichidan -> verb (ichidan) verb-suru -> suru verb
    verb-kuru -> verb (kuru)       verb-irregular -> verb (irregular)
    adjective-i -> i-adjective     adjective-na -> na-adjective
    adjective-no -> no-adjective   adjective-taru -> taru-adjective
    pre-noun-adjectival -> pre-noun adjectival    (all others as-is)

Transitivity: if the existing string mentions transitive/intransitive AND
``tags.transitivity`` agrees, the qualifier is kept on the first verb tag:
"verb (godan, transitive)", "noun, suru verb (intransitive)",
"verb (godan, transitive/intransitive)" for "both". The tool never ADDS a
qualifier that the string did not already carry.

Safety rules (an entry is rewritten only when its string parses cleanly):
  * tags.pos empty -> never rewritten (status no-pos-tags);
  * the string mentions a part of speech that tags.pos lacks (e.g. text says
    "noun, suru verb" but tags.pos is ["noun"]), or a transitivity that
    tags.transitivity lacks/contradicts -> status "disagreement", reported for
    a human, never rewritten;
  * the string carries a qualifier the tags cannot express ("noun (proper)",
    "expression, verb phrase", "(dialect)") -> status "unparsed", reported,
    never rewritten.

Dry run by default. Nothing is written without --apply.

Usage:
    python3 build/normalize_pos.py                     # dry-run summary
    python3 build/normalize_pos.py --survey            # distinct strings per tags.pos combo
    python3 build/normalize_pos.py --report /tmp/pos_report.json   # disagreement/unparsed lists
    python3 build/normalize_pos.py --entries-dir COPY --apply
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_common import (  # noqa: E402
    PROJECT_ROOT, add_common_args, resolve_apply, parse_ids, iter_entry_paths,
    load_entry, write_entry, touch_modified, utc_now, entry_label,
)

VERB_POS = {"verb-godan", "verb-ichidan", "verb-suru", "verb-kuru", "verb-irregular"}
ADJECTIVE_POS = {"adjective-i", "adjective-na", "adjective-no", "adjective-taru"}

POS_DISPLAY = {
    "noun": "noun",
    "verb-godan": "verb (godan)",
    "verb-ichidan": "verb (ichidan)",
    "verb-suru": "suru verb",
    "verb-kuru": "verb (kuru)",
    "verb-irregular": "verb (irregular)",
    "adjective-i": "i-adjective",
    "adjective-na": "na-adjective",
    "adjective-no": "no-adjective",
    "adjective-taru": "taru-adjective",
    "adverb": "adverb",
    "particle": "particle",
    "conjunction": "conjunction",
    "interjection": "interjection",
    "pronoun": "pronoun",
    "counter": "counter",
    "prefix": "prefix",
    "suffix": "suffix",
    "expression": "expression",
    "pre-noun-adjectival": "pre-noun adjectival",
    "number": "number",
    "auxiliary": "auxiliary",
    "onomatopoeia": "onomatopoeia",
}

TRANSITIVITY_DISPLAY = {
    "transitive": "transitive",
    "intransitive": "intransitive",
    "both": "transitive/intransitive",
}

# Free-text token -> canonical tag, or a generic family ("verb"/"adjective")
# that any member of VERB_POS / ADJECTIVE_POS satisfies. Tokens are lowercased
# and whitespace-collapsed before lookup.
TOKEN_MAP = {
    "noun": "noun", "nouns": "noun",
    "verb": "@verb", "verbs": "@verb",
    "adjective": "@adjective", "adjectives": "@adjective",
    "godan": "verb-godan", "godan verb": "verb-godan", "verb-godan": "verb-godan",
    "verb godan": "verb-godan", "u-verb": "verb-godan", "godan-verb": "verb-godan",
    "ichidan": "verb-ichidan", "ichidan verb": "verb-ichidan", "verb-ichidan": "verb-ichidan",
    "verb ichidan": "verb-ichidan", "ru-verb": "verb-ichidan", "ichidan-verb": "verb-ichidan",
    "suru": "verb-suru", "suru verb": "verb-suru", "suru-verb": "verb-suru", "verb-suru": "verb-suru",
    "verb suru": "verb-suru", "する": "verb-suru", "する verb": "verb-suru", "する-verb": "verb-suru",
    "verbal": "verb-suru", "verbal noun": "verb-suru", "with suru": "verb-suru",
    "with suru verb": "verb-suru", "takes suru": "verb-suru", "+ suru": "verb-suru",
    "ずる": "@suru-or-irregular", "zuru": "@suru-or-irregular", "zuru verb": "@suru-or-irregular",
    "kuru": "verb-kuru", "kuru verb": "verb-kuru", "verb-kuru": "verb-kuru", "くる": "verb-kuru",
    "irregular": "verb-irregular", "irregular verb": "verb-irregular", "verb-irregular": "verb-irregular",
    "i-adjective": "adjective-i", "adjective-i": "adjective-i", "i adjective": "adjective-i",
    "i": "adjective-i", "い-adjective": "adjective-i", "い": "adjective-i", "い adjective": "adjective-i",
    "adjective i": "adjective-i",
    "na-adjective": "adjective-na", "adjective-na": "adjective-na", "na adjective": "adjective-na",
    "na": "adjective-na", "な-adjective": "adjective-na", "な": "adjective-na", "な adjective": "adjective-na",
    "adjective na": "adjective-na", "adjectival noun": "adjective-na",
    "no-adjective": "adjective-no", "adjective-no": "adjective-no", "no adjective": "adjective-no",
    "no": "adjective-no", "の-adjective": "adjective-no", "の": "adjective-no", "の adjective": "adjective-no",
    "adjective no": "adjective-no",
    "taru-adjective": "adjective-taru", "adjective-taru": "adjective-taru", "taru adjective": "adjective-taru",
    "taru": "adjective-taru", "たる-adjective": "adjective-taru", "たる": "adjective-taru",
    "adverb": "adverb", "adverbs": "adverb", "adverbial noun": "adverb",
    "particle": "particle", "particles": "particle",
    "conjunction": "conjunction", "conjunctions": "conjunction",
    "interjection": "interjection", "interjections": "interjection",
    "pronoun": "pronoun", "pronouns": "pronoun",
    "counter": "counter", "counters": "counter",
    "prefix": "prefix", "prefixes": "prefix",
    "suffix": "suffix", "suffixes": "suffix",
    "expression": "expression", "expressions": "expression",
    "set phrase": "expression", "fixed expression": "expression", "idiomatic expression": "expression",
    "idiom": "expression", "proverb": "expression", "four-character idiom": "expression",
    "yojijukugo": "expression", "phrase": "expression", "grammar pattern": "expression",
    "grammatical pattern": "expression",
    "pre-noun adjectival": "pre-noun-adjectival", "pre-noun-adjectival": "pre-noun-adjectival",
    "pre-noun adjective": "pre-noun-adjectival", "prenominal": "pre-noun-adjectival",
    "prenominal adjective": "pre-noun-adjectival", "adnominal": "pre-noun-adjectival",
    "adnominal adjective": "pre-noun-adjectival", "rentaishi": "pre-noun-adjectival",
    "attributive": "pre-noun-adjectival",
    "number": "number", "numeral": "number", "numbers": "number",
    "auxiliary": "auxiliary", "auxiliary verb": "auxiliary", "auxiliary adjective": "auxiliary",
    "onomatopoeia": "onomatopoeia", "onomatopoeic": "onomatopoeia", "mimetic": "onomatopoeia",
    "mimetic word": "onomatopoeia", "onomatopoeic word": "onomatopoeia", "sound symbolism": "onomatopoeia",
}

_BOTH_RE = re.compile(r"\b(?:transitive\s*(?:/|and|&|or)\s*intransitive|intransitive\s*(?:/|and|&|or)\s*transitive)\b")
_INTRANS_RE = re.compile(r"\bintransitive\b")
_TRANS_RE = re.compile(r"\btransitive\b")
_SPLIT_RE = re.compile(r"[,/;()\[\]]|\band\b|&")
_GODAN_ENDING_RE = re.compile(r"^godan\s+[うくぐすつぬぶむる]$")


class ParsedPos:
    __slots__ = ("pos", "generic", "transitivity", "unknown")

    def __init__(self):
        self.pos = set()          # canonical tags mentioned
        self.generic = set()      # "@verb", "@adjective", "@suru-or-irregular"
        self.transitivity = None  # "transitive" | "intransitive" | "both" | None
        self.unknown = []         # tokens we could not interpret


def parse_display(text: str) -> ParsedPos:
    """Interpret a free-text part_of_speech string."""
    parsed = ParsedPos()
    if not text:
        return parsed
    s = text.lower()
    if _BOTH_RE.search(s):
        parsed.transitivity = "both"
        s = _BOTH_RE.sub(" ", s)
    has_in = bool(_INTRANS_RE.search(s))
    s = _INTRANS_RE.sub(" ", s)
    has_tr = bool(_TRANS_RE.search(s))
    s = _TRANS_RE.sub(" ", s)
    if has_in and has_tr:
        parsed.transitivity = "both"
    elif has_in:
        parsed.transitivity = parsed.transitivity or "intransitive"
    elif has_tr:
        parsed.transitivity = parsed.transitivity or "transitive"

    for raw in _SPLIT_RE.split(s):
        tok = re.sub(r"\s+", " ", raw).strip(" .:-")
        if not tok:
            continue
        mapped = TOKEN_MAP.get(tok)
        if mapped is None and _GODAN_ENDING_RE.match(tok):
            mapped = "verb-godan"
        if mapped is None:
            parsed.unknown.append(tok)
        elif mapped.startswith("@"):
            parsed.generic.add(mapped)
        else:
            parsed.pos.add(mapped)
    return parsed


def render(pos_tags, transitivity=None) -> str:
    """Canonical display string for a tags.pos list (+ optional qualifier)."""
    parts = []
    qualified = False
    q = TRANSITIVITY_DISPLAY.get(transitivity) if transitivity else None
    for tag in pos_tags or []:
        disp = POS_DISPLAY.get(tag, tag)
        if q and not qualified and tag in VERB_POS:
            disp = f"{disp[:-1]}, {q})" if disp.endswith(")") else f"{disp} ({q})"
            qualified = True
        parts.append(disp)
    return ", ".join(parts)


def is_canonical_display(text: str, tags: dict) -> bool:
    """True if `text` is the canonical rendering of tags.pos, with or without the
    transitivity qualifier that tags.transitivity permits."""
    pos = (tags or {}).get("pos") or []
    if not pos:
        return True
    if text == render(pos):
        return True
    tr = (tags or {}).get("transitivity")
    return bool(tr) and text == render(pos, tr)


def classify(entry: dict, strict: bool = False) -> dict:
    """Decide what to do with one entry's part_of_speech.

    Returns {"status": ..., "current": str, "canonical": str|None, "reason": str,
    "adds": [tags the text did not mention]} with status one of: no-pos-tags,
    canonical, rewrite, disagreement, unparsed. With strict=True a rewrite that
    would ADD a part of speech the text never mentioned (text "noun", tags
    ["noun", "verb-suru"]) is held out as "tags-add-pos" instead.
    """
    tags = ((entry.get("metadata") or {}).get("tags") or {})
    pos = list(tags.get("pos") or [])
    current = entry.get("part_of_speech") or ""
    tr = tags.get("transitivity")
    if not pos:
        return {"status": "no-pos-tags", "current": current, "canonical": None,
                "reason": "tags.pos is empty"}
    if is_canonical_display(current, tags):
        return {"status": "canonical", "current": current, "canonical": current, "reason": ""}

    parsed = parse_display(current)
    if parsed.unknown:
        return {"status": "unparsed", "current": current, "canonical": None,
                "reason": f"unrecognized qualifier(s): {', '.join(parsed.unknown)}"}
    pos_set = set(pos)
    missing = sorted(p for p in parsed.pos if p not in pos_set)
    if "@verb" in parsed.generic and not (pos_set & VERB_POS):
        missing.append("verb (any class)")
    if "@adjective" in parsed.generic and not (pos_set & ADJECTIVE_POS):
        missing.append("adjective (any class)")
    if "@suru-or-irregular" in parsed.generic and not (pos_set & {"verb-suru", "verb-irregular"}):
        missing.append("verb-suru/verb-irregular")
    if missing:
        return {"status": "disagreement", "current": current, "canonical": None,
                "reason": f"text mentions {missing} but tags.pos is {pos}"}
    keep_tr = None
    if parsed.transitivity:
        if tr != parsed.transitivity:
            return {"status": "disagreement", "current": current, "canonical": None,
                    "reason": f"text says '{parsed.transitivity}' but tags.transitivity is {tr!r}"}
        keep_tr = tr
    canonical = render(pos, keep_tr)
    if canonical == current:
        return {"status": "canonical", "current": current, "canonical": current, "reason": ""}
    mentioned = set(parsed.pos)
    if "@verb" in parsed.generic:
        mentioned |= pos_set & VERB_POS
    if "@adjective" in parsed.generic:
        mentioned |= pos_set & ADJECTIVE_POS
    if "@suru-or-irregular" in parsed.generic:
        mentioned |= pos_set & {"verb-suru", "verb-irregular"}
    adds = [p for p in pos if p not in mentioned]
    if strict and adds:
        return {"status": "tags-add-pos", "current": current, "canonical": canonical,
                "reason": f"tags.pos adds {adds} that the text does not mention", "adds": adds}
    return {"status": "rewrite", "current": current, "canonical": canonical, "reason": "",
            "adds": adds}


def survey(paths) -> None:
    strings = Counter()
    by_combo = defaultdict(Counter)
    for path in paths:
        try:
            entry, _ = load_entry(path)
        except (json.JSONDecodeError, OSError):
            continue
        pos = tuple(((entry.get("metadata") or {}).get("tags") or {}).get("pos") or [])
        s = entry.get("part_of_speech") or ""
        strings[s] += 1
        by_combo[pos][s] += 1
    print(f"Distinct part_of_speech strings: {len(strings)}")
    print("\nTop 40 strings:")
    for s, c in strings.most_common(40):
        print(f"  {c:6d}  {s!r}")
    print("\nMost common rendering per tags.pos combination (top 40 combos):")
    for combo, cnt in sorted(by_combo.items(), key=lambda kv: -sum(kv[1].values()))[:40]:
        total = sum(cnt.values())
        top = "; ".join(f"{s!r}={c}" for s, c in cnt.most_common(3))
        print(f"  {total:6d}  {list(combo)}  canonical={render(combo)!r}\n          {top}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(ap)
    ap.add_argument("--survey", action="store_true",
                    help="Print the distribution of existing strings per tags.pos combo and exit")
    ap.add_argument("--strict", action="store_true",
                    help="Hold out (do not rewrite) entries whose tags.pos would ADD a part of "
                         "speech the current text never mentions, e.g. text 'noun' with tags "
                         "['noun', 'verb-suru']")
    ap.add_argument("--report", type=Path, default=None,
                    help="Write disagreement/unparsed lists (and rewrite pairs) to this JSON file")
    ap.add_argument("--top", type=int, default=25, help="Rows to print per section")
    ap.add_argument("--quiet", action="store_true", help="Only print the summary counts")
    args = ap.parse_args(argv)
    apply = resolve_apply(args)
    paths = list(iter_entry_paths(args.entries_dir, parse_ids(args.ids), args.range))

    if args.survey:
        survey(paths)
        return 0

    status_counts = Counter()
    rewrites = Counter()
    adds_count = 0
    holdouts = {"disagreement": [], "unparsed": [], "tags-add-pos": []}
    timestamp = utc_now()
    changed = 0
    for path in paths:
        try:
            entry, raw = load_entry(path)
        except (json.JSONDecodeError, OSError) as e:
            print(f"warning: skipping {path}: {e}", file=sys.stderr)
            continue
        res = classify(entry, strict=args.strict)
        status_counts[res["status"]] += 1
        if res.get("adds") and res["status"] == "rewrite":
            adds_count += 1
        label = entry_label(entry, path)
        tags = ((entry.get("metadata") or {}).get("tags") or {})
        if res["status"] in holdouts:
            holdouts[res["status"]].append({
                "id": label, "part_of_speech": res["current"],
                "tags_pos": tags.get("pos"), "tags_transitivity": tags.get("transitivity"),
                "reason": res["reason"],
            })
        elif res["status"] == "rewrite":
            rewrites[(res["current"], res["canonical"])] += 1
            changed += 1
            if apply:
                entry["part_of_speech"] = res["canonical"]
                touch_modified(entry, timestamp)
                write_entry(path, entry, raw)

    mode = "APPLIED" if apply else "DRY RUN"
    print(f"[{mode}] normalize_pos: {sum(status_counts.values())} entries scanned")
    for k in ("canonical", "rewrite", "disagreement", "unparsed", "tags-add-pos", "no-pos-tags"):
        if k == "tags-add-pos" and not args.strict:
            continue
        print(f"  {k:13s} {status_counts.get(k, 0):6d}")
    print(f"  (rewrites where tags.pos adds a part of speech the text did not mention: {adds_count}"
          f"{'; use --strict to hold these out' if adds_count and not args.strict else ''})")
    print(f"  -> {changed} entries {'rewritten' if apply else 'would be rewritten'}; "
          f"{len(holdouts['disagreement'])} disagreements and {len(holdouts['unparsed'])} "
          "unparsed strings left for a human")
    if not args.quiet:
        if rewrites:
            print(f"\nTop {args.top} rewrites (current -> canonical):")
            for (cur, canon), c in rewrites.most_common(args.top):
                print(f"  {c:6d}  {cur!r}  ->  {canon!r}")
        for kind in ("disagreement", "unparsed", "tags-add-pos"):
            items = holdouts[kind]
            if items:
                print(f"\n{kind.capitalize()} samples (first {min(len(items), args.top)} of {len(items)}):")
                for it in items[:args.top]:
                    print(f"  {it['id']}: {it['part_of_speech']!r} vs tags.pos={it['tags_pos']} "
                          f"transitivity={it['tags_transitivity']!r} — {it['reason']}")
    if args.report:
        payload = {
            "generated": timestamp,
            "status_counts": dict(status_counts),
            "rewrites": [{"from": a, "to": b, "count": c} for (a, b), c in rewrites.most_common()],
            "disagreement": holdouts["disagreement"],
            "unparsed": holdouts["unparsed"],
            "tags-add-pos": holdouts["tags-add-pos"],
        }
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"\nReport written to {args.report}")
    if not apply and changed:
        print("\nDry run — nothing written. Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
