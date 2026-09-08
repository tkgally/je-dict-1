#!/usr/bin/env python3
"""Read-only detector for inline links whose kana base form can name the wrong word.

The deterministic linker (``build/auto_link.py``) links a kana token when the
dictionary has exactly one entry with that reading and that entry's headword is
itself kana.  "Exactly one entry" is a fact about the dictionary, not about the
language: そうして has one entry (the conjunction "and then"), so every そうして
in the corpus was linked to it, including the て-form of そうする ("like that")
in the notes of ああして.  Kanji links do not have this problem (the furigana
reading and the kanji together identify the lexeme), nor do katakana links; the
fixed function-word table was vetted by hand.  The exposed class is therefore
exactly the links whose base form is pure hiragana and not in the table — about
36,000 of the one million links, over about 1,400 distinct base forms.

This script inventories that class against the curated list in
``build/data/kana_link_homophones.json``, where every screened base form
carries a tier:

  unique   the kana string means only this entry's word in practice; the linker
           links it freely.
  verify   a same-kana competitor exists but the entry's word dominates; the
           linker links it and the Routine's self-check reviews each new
           occurrence in context (``build/review_links.py --ids``).
  block    the competitor is common enough that a context-free link is wrong
           too often; the linker never links it.  Existing links to a block
           base are allowed only with a ``keep`` decision in
           ``reviews/link_decisions.jsonl`` (one line per adjudicated
           occurrence), which is what ``--gate`` checks.

Ledger decisions: ``keep`` (the link is right), ``unlink`` (remove it; the
surface text stays), ``retarget`` (point it at ``new_base`` / ``new_target``,
e.g. いけません from いける to the entry いけない).  A line without ``entry``
but with ``n`` is aggregated evidence (``n`` model-confirmed occurrences of a
base, written by ``review_links.py --ledger-from --aggregate``): it counts for
``--retier`` and never satisfies the gate for a particular link.

Modes:
    python3 build/check_link_homophones.py                    # summary by tier
    python3 build/check_link_homophones.py --unscreened       # bases missing from the list
    python3 build/check_link_homophones.py --json --tier verify --sample 60   # review queue
    python3 build/check_link_homophones.py --json --base そうして
    python3 build/check_link_homophones.py --retier           # tiers implied by the ledger
    python3 build/check_link_homophones.py --retier --write   # ...written into the list
    python3 build/check_link_homophones.py --gate             # CI: block-tier links need a keep
    python3 build/check_link_homophones.py --json --kanji-base --sample 40   # hand links きて→来る

The script never modifies entries.  ``--gate`` exits 1 on a violation; every
other mode exits 0.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = ROOT / "entries"
DATA_PATH = ROOT / "build" / "data" / "kana_link_homophones.json"
DECISIONS_PATH = ROOT / "reviews" / "link_decisions.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from auto_link import (  # noqa: E402
    FUNCTION_WORDS, LINK_INFO_RE, LINK_RE, TILDES, is_hiragana, strip_furigana,
)

TIERS = ("unique", "verify", "block")
#: Tier thresholds applied by --retier to the adjudicated decisions of one base.
BLOCK_MIN_WRONG_RATE = 0.20
BLOCK_MIN_WRONG = 2


# ---------------------------------------------------------------------------
# Data file and ledger
# ---------------------------------------------------------------------------


def load_data(path: Path = DATA_PATH) -> dict:
    if not path.exists():
        return {"bases": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("bases", {})
    for base, rec in data["bases"].items():
        tier = rec.get("tier")
        if tier not in TIERS:
            raise SystemExit(f"{path}: base {base!r} has an unknown tier {tier!r}")
    return data


def save_data(data: dict, path: Path = DATA_PATH) -> None:
    data["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    data["bases"] = dict(sorted(data["bases"].items()))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def load_decisions(path: Path = DECISIONS_PATH) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(rec, dict) and rec.get("decision") in ("keep", "unlink", "retarget"):
            out.append(rec)
    return out


def decision_index(decisions: list[dict]) -> dict[tuple[str, str, str], set[str]]:
    """``(entry number, base, target) -> {decisions}`` over the whole ledger.

    A ``retarget`` line counts as ``unlink`` for the old (base, target) and as
    ``keep`` for the new one (``new_base``, ``new_target``).
    """
    idx: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for rec in decisions:
        if not rec.get("entry"):
            continue                    # aggregated evidence line (base, target, n): no occurrence
        num = entry_num(rec.get("entry", ""))
        key = (num, norm_base(rec.get("base", "")), rec.get("target", ""))
        if rec["decision"] == "retarget":
            idx[key].add("unlink")
            idx[(num, norm_base(rec.get("new_base", "")), rec.get("new_target", ""))].add("keep")
        else:
            idx[key].add(rec["decision"])
    return idx


# ---------------------------------------------------------------------------
# Link inventory
# ---------------------------------------------------------------------------


def entry_num(value: str) -> str:
    return str(value)[:5]


def norm_base(base: str) -> str:
    return base.strip().strip(TILDES).strip()


def is_kana_base(text: str) -> bool:
    """Pure hiragana; katakana is a different, headword-exact class and is excluded."""
    return bool(text) and all(is_hiragana(c) for c in text) and not all(c == "ー" for c in text)


def plain(text: str) -> str:
    """Link markup and furigana wrappers removed; ⟦⟧ around the surface kept out."""
    out = []
    pos = 0
    for m in LINK_RE.finditer(text):
        out.append(text[pos:m.start()])
        info = LINK_INFO_RE.match(m.group(1))
        out.append(info.group(1) if info else m.group(1))
        pos = m.end()
    out.append(text[pos:])
    return strip_furigana("".join(out))


def marked_context(text: str, link_start: int, link_end: int, width: int = 90) -> str:
    """Plain text of the line holding the link, the link's surface marked with 【】."""
    before, mid, after = text[:link_start], text[link_start:link_end], text[link_end:]
    before_p, after_p = plain(before), plain(after)
    info = LINK_INFO_RE.match(mid[1:-1])
    mid_p = strip_furigana(info.group(1) if info else mid[1:-1])
    # keep to the current line
    nl = before_p.rfind("\n")
    if nl != -1:
        before_p = before_p[nl + 1:]
    nl = after_p.find("\n")
    if nl != -1:
        after_p = after_p[:nl]
    if len(before_p) > width:
        before_p = "…" + before_p[-width:]
    if len(after_p) > width:
        after_p = after_p[:width] + "…"
    return f"{before_p}【{mid_p}】{after_p}"


class Occurrence(dict):
    """One inline link with a kana base: entry, field, surface, base, target, context."""


def iter_entries(entries_dir: Path = ENTRIES_DIR, ids: set[str] | None = None,
                 id_range: tuple[int, int] | None = None):
    for path in sorted(entries_dir.glob("*/*.json")):
        num = path.stem[:5]
        if not num.isdigit():
            continue
        if ids and num not in ids and path.stem not in ids:
            continue
        if id_range and not (id_range[0] <= int(num) <= id_range[1]):
            continue
        try:
            yield path, json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)


def kana_link_occurrences(entry: dict, kanji_base: bool = False) -> list[Occurrence]:
    """Every link whose surface and base are pure hiragana and whose base is not a table word.

    With ``kanji_base`` the neighbouring class is returned instead: a pure-kana
    surface linked to a kanji base (``⟦きて→来る⟧``).  The linker never writes
    those (a kanji-headed entry is never linked from a kana surface), so they are
    hand links; they are listed for review but carry no tier.
    """
    eid = entry.get("id") or ""
    out: list[Occurrence] = []
    fields: list[tuple[str, str, str | None]] = []
    for idx, ex in enumerate(entry.get("examples") or []):
        if isinstance(ex, dict) and isinstance(ex.get("japanese"), str):
            fields.append((f"examples[{idx}]", ex["japanese"], ex.get("english")))
    if isinstance(entry.get("notes"), str):
        fields.append(("notes", entry["notes"], None))
    for field, text, english in fields:
        for m in LINK_RE.finditer(text):
            info = LINK_INFO_RE.match(m.group(1))
            if not info:
                continue
            surface, base, target = info.groups()
            base_n = norm_base(base)
            surface_p = strip_furigana(surface)
            if target == "noentry" or base_n in FUNCTION_WORDS:
                continue
            if not is_kana_base(norm_base(surface_p)):
                continue
            if is_kana_base(base_n) == kanji_base:
                continue
            out.append(Occurrence(
                entry=eid, field=field, surface=surface_p, base=base_n,
                target=target, context=marked_context(text, m.start(), m.end()),
                english=english,
            ))
    return out


def collect(entries_dir: Path = ENTRIES_DIR, ids: set[str] | None = None,
            id_range: tuple[int, int] | None = None, kanji_base: bool = False) -> list[Occurrence]:
    occ: list[Occurrence] = []
    for _path, entry in iter_entries(entries_dir, ids, id_range):
        occ.extend(kana_link_occurrences(entry, kanji_base))
    return occ


def tier_of(base: str, data: dict) -> str:
    rec = data.get("bases", {}).get(base)
    return rec["tier"] if rec else "unscreened"


# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------


def print_summary(occ: list[Occurrence], data: dict) -> None:
    by_tier = Counter(tier_of(o["base"], data) for o in occ)
    bases_by_tier: dict[str, set[str]] = defaultdict(set)
    for o in occ:
        bases_by_tier[tier_of(o["base"], data)].add(o["base"])
    print("== kana-base inline links (the class exposed to wrong-lexeme links) ==")
    print(f"occurrences: {len(occ)}   distinct bases: {len({o['base'] for o in occ})}")
    for tier in TIERS + ("unscreened",):
        print(f"  {tier:<11}{by_tier.get(tier, 0):>7} links over {len(bases_by_tier.get(tier, ())):>5} bases")
    unscreened = Counter(o["base"] for o in occ if tier_of(o["base"], data) == "unscreened")
    if unscreened:
        top = ", ".join(f"{b} ({n})" for b, n in unscreened.most_common(15))
        print(f"most frequent unscreened bases: {top}")


def print_unscreened(occ: list[Occurrence], data: dict) -> None:
    counts = Counter(o["base"] for o in occ if tier_of(o["base"], data) == "unscreened")
    for base, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        targets = Counter(o["target"] for o in occ if o["base"] == base)
        print(f"{base}\t{n}\t{','.join(t for t, _ in targets.most_common())}")


def sample_queue(occ: list[Occurrence], per_base: int, seed: int) -> list[Occurrence]:
    """At most ``per_base`` occurrences of each base, chosen deterministically."""
    if per_base <= 0:
        return occ
    rng = random.Random(seed)
    by_base: dict[str, list[Occurrence]] = defaultdict(list)
    for o in occ:
        by_base[o["base"]].append(o)
    out: list[Occurrence] = []
    for base in sorted(by_base):
        items = by_base[base]
        if len(items) > per_base:
            items = rng.sample(items, per_base)
        out.extend(items)
    return out


def retier(occ: list[Occurrence], data: dict, decisions: list[dict]) -> list[tuple[str, str, str, int, int]]:
    """Tier each reviewed base implies, from the ledger: (base, old, new, reviewed, wrong)."""
    per_base: dict[str, Counter] = defaultdict(Counter)
    for rec in decisions:
        n = int(rec.get("n") or 1)      # aggregated lines carry a count
        per_base[norm_base(rec.get("base", ""))]["unlink" if rec["decision"] == "retarget" else rec["decision"]] += n
    changes = []
    for base, counts in sorted(per_base.items()):
        reviewed = counts["keep"] + counts["unlink"]
        wrong = counts["unlink"]
        if not reviewed:
            continue
        rec = data["bases"].get(base)
        old = rec["tier"] if rec else "unscreened"
        if rec and rec.get("tier_locked"):
            continue
        if wrong >= BLOCK_MIN_WRONG and wrong / reviewed >= BLOCK_MIN_WRONG_RATE:
            new = "block"
        elif wrong or (rec and rec.get("screen", {}).get("verdict") == "ambiguous"):
            new = "verify"
        else:
            new = rec["tier"] if rec else "verify"
        changes.append((base, old, new, reviewed, wrong))
    return changes


def apply_retier(data: dict, changes, date: str) -> int:
    n = 0
    for base, old, new, reviewed, wrong in changes:
        rec = data["bases"].setdefault(base, {"tier": new})
        rec["review"] = {"reviewed": reviewed, "wrong": wrong, "date": date}
        if old != new:
            rec["tier"] = new
            n += 1
    return n


def gate(occ: list[Occurrence], data: dict, decisions: list[dict]) -> int:
    """Block-tier links need a keep decision; a link unlinked by decision must stay gone."""
    idx = decision_index(decisions)
    problems: list[str] = []
    seen: set[tuple[str, str, str]] = set()
    for o in occ:
        key = (entry_num(o["entry"]), o["base"], o["target"])
        if key in seen:
            continue
        seen.add(key)
        verdicts = idx.get(key, set())
        tier = tier_of(o["base"], data)
        if tier == "block" and "keep" not in verdicts:
            problems.append(f"{o['entry']} {o['field']}: ⟦{o['surface']}→{o['base']}：{o['target']}⟧ "
                            f"— {o['base']} is a block-tier kana base with no keep decision")
        elif tier != "block" and "unlink" in verdicts and "keep" not in verdicts:
            problems.append(f"{o['entry']} {o['field']}: ⟦{o['surface']}→{o['base']}：{o['target']}⟧ "
                            f"— this link was removed by decision and is back")
    if problems:
        print(f"FAIL: {len(problems)} kana-base link(s) need a decision "
              f"(see build/check_link_homophones.py and the inline-word-links skill):")
        for p in problems[:50]:
            print("  " + p)
        if len(problems) > 50:
            print(f"  ... and {len(problems) - 50} more")
        return 1
    blocked = sum(1 for o in occ if tier_of(o["base"], data) == "block")
    print(f"OK: {blocked} link(s) to block-tier kana bases, all with keep decisions; "
          f"no unlinked link has returned")
    return 0


def parse_ids(spec: str | None) -> set[str] | None:
    if not spec:
        return None
    ids: set[str] = set()
    for part in spec.split(","):
        part = part.strip()
        if part.startswith("@"):
            ids.update(l.strip() for l in Path(part[1:]).read_text(encoding="utf-8").splitlines() if l.strip())
        elif part:
            ids.add(part[:5] if part[:5].isdigit() else part)
    return ids


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ids", help="comma-separated entry IDs, or @file with one per line")
    ap.add_argument("--range", nargs=2, type=int, metavar=("START", "END"))
    ap.add_argument("--entries-dir", type=Path, default=ENTRIES_DIR)
    ap.add_argument("--data", type=Path, default=DATA_PATH, help="the curated kana-base list")
    ap.add_argument("--decisions", type=Path, default=DECISIONS_PATH, help="the decisions ledger")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--summary", action="store_true", help="counts by tier (default)")
    mode.add_argument("--unscreened", action="store_true", help="bases absent from the list, with counts")
    mode.add_argument("--json", action="store_true", help="occurrence queue as a JSON array")
    mode.add_argument("--retier", action="store_true", help="tiers implied by the ledger's decisions")
    mode.add_argument("--gate", action="store_true", help="CI check (exit 1 on a violation)")
    ap.add_argument("--tier", help="comma-separated tiers to include in --json "
                                   "(unique, verify, block, unscreened; default all)")
    ap.add_argument("--base", help="comma-separated bases to include in --json")
    ap.add_argument("--sample", type=int, default=0, metavar="N",
                    help="--json: at most N occurrences per base (deterministic)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--write", action="store_true", help="--retier: write the new tiers into the list")
    ap.add_argument("--kanji-base", action="store_true",
                    help="--json/--summary: the neighbouring class instead (kana surface, kanji base; "
                         "hand links the linker never writes, listed without tiers)")
    args = ap.parse_args(argv)

    data = load_data(args.data)
    decisions = load_decisions(args.decisions)
    occ = collect(args.entries_dir, parse_ids(args.ids), tuple(args.range) if args.range else None,
                  kanji_base=args.kanji_base)

    if args.gate:
        return gate(occ, data, decisions)
    if args.unscreened:
        print_unscreened(occ, data)
        return 0
    if args.retier:
        changes = retier(occ, data, decisions)
        for base, old, new, reviewed, wrong in changes:
            flag = "" if old == new else "  <- change"
            print(f"{base}\t{old} -> {new}\treviewed {reviewed}, wrong {wrong}{flag}")
        if args.write:
            n = apply_retier(data, changes, datetime.now(timezone.utc).strftime("%Y-%m-%d"))
            save_data(data, args.data)
            print(f"wrote {args.data}: {n} tier change(s), {len(changes)} base(s) with review evidence")
        return 0
    if args.json:
        tiers = set(args.tier.split(",")) if args.tier else None
        bases = set(norm_base(b) for b in args.base.split(",")) if args.base else None
        sel = [o for o in occ
               if (tiers is None or tier_of(o["base"], data) in tiers)
               and (bases is None or o["base"] in bases)]
        sel = sample_queue(sel, args.sample, args.seed)
        for o in sel:
            o["tier"] = tier_of(o["base"], data)
        print(json.dumps(sel, ensure_ascii=False, indent=1))
        return 0
    print_summary(occ, data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
