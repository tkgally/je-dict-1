#!/usr/bin/env python3
"""
Retire or rename a dictionary entry without breaking its URL.

An entry's page lives at entries/{range}/{id}.html, and the id carries the
romaji, so deleting an entry or correcting its reading used to break a live
URL. Tom ruled on 2026-10-01 that both are allowed when the old URL keeps
working: build/data/retired_entries.json maps every retired id to the id that
replaces it, and the site build writes a redirect page at the old address.

    # delete 08989_shaseki; its URL redirects to 座席, links move there
    python3 build/retire_entry.py retire 08989_shaseki --to 02832_zaseki \
        --reason "not a standard word; 座席 covers it"

    # correct a reading: same number, new romaji, old URL redirects
    python3 build/retire_entry.py rename 28415_inushu 28415_kenshu \
        --reason "headword reading corrected to けんしゅ"

Both commands rewrite every reference to the old id: inline links in entries
and articles, cross_references target_ids, articles' related_entries, and the
link-decision ledger. A rename also renames the example ids and their audio
manifest keys, so recordings survive. On retire, cross-references that pointed
at the old entry are dropped (they named a different word) unless --duplicate
says the two entries are the same word, when they are repointed; links whose
surface no longer fits the new target are listed for review. Add --dry-run to
see what would change.

Afterwards run `make index` (rebuilds entries_index.json, word_id_lookup.json
and the kanji index) and `python3 build/validate.py`.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "entries"
ARTICLES = ROOT / "articles"
RETIRED = ROOT / "build" / "data" / "retired_entries.json"
MANIFEST = ROOT / "audio" / "manifest"
LINK_DECISIONS = ROOT / "reviews" / "link_decisions.jsonl"

ID_RE = re.compile(r"^\d{5}_[a-z0-9]+$")


def range_dir(entry_id: str) -> str:
    n = int(entry_id[:5])
    return f"{n // 500 * 500:05d}"


def entry_path(entry_id: str) -> Path:
    return ENTRIES / range_dir(entry_id) / f"{entry_id}.json"


def load_retired() -> dict:
    if RETIRED.exists():
        return json.loads(RETIRED.read_text(encoding="utf-8"))
    return {}


def save_retired(data: dict) -> None:
    RETIRED.write_text(json.dumps(dict(sorted(data.items())), ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")


def resolve(retired: dict, entry_id: str) -> str:
    """Follow the retired map to the live id (guards against cycles)."""
    seen = set()
    while entry_id in retired and entry_id not in seen:
        seen.add(entry_id)
        entry_id = retired[entry_id]["to"]
    return entry_id


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def link_pattern(old: str) -> re.Pattern:
    # ⟦surface→base：OLD⟧ — the id ends at ⟧
    return re.compile(r"(⟦[^⟦⟧]*?：)" + re.escape(old) + r"(⟧)")


def rewrite_text(text: str, old: str, new: str, hits: list, where: str) -> str:
    pat = link_pattern(old)

    def sub(m):
        hits.append((where, m.group(0)))
        return m.group(1) + new + m.group(2)

    return pat.sub(sub, text)


def rewrite_entry_texts(entry: dict, old: str, new: str, hits: list, where: str) -> bool:
    changed = False
    for ex in entry.get("examples") or []:
        for key in ("japanese", "notes"):
            if isinstance(ex.get(key), str) and old in ex[key]:
                ex[key] = rewrite_text(ex[key], old, new, hits, f"{where} ex {ex.get('id', '')}")
                changed = True
    for key in ("notes",):
        if isinstance(entry.get(key), str) and old in entry[key]:
            entry[key] = rewrite_text(entry[key], old, new, hits, f"{where} notes")
            changed = True
    for d in entry.get("definitions") or []:
        for key in ("explanation",):
            if isinstance(d.get(key), str) and old in d[key]:
                d[key] = rewrite_text(d[key], old, new, hits, f"{where} def")
                changed = True
    return changed


def update_references(old: str, new: str, *, drop_crossrefs: bool, dry_run: bool,
                      new_entry: dict = None) -> dict:
    """Point every reference to `old` at `new`. Returns a report dict.

    Cross-references to `old` are dropped when `drop_crossrefs` (they named a
    different word), else repointed at `new` (taking its headword and reading
    from `new_entry` when given), unless the entry already has one to `new`.
    """
    report = {"links": [], "crossrefs_dropped": [], "crossrefs_repointed": [], "articles": [],
              "files": set()}
    for path in sorted(ENTRIES.glob("*/*.json")):
        raw = path.read_text(encoding="utf-8")
        if old not in raw:
            continue
        entry = json.loads(raw)
        if entry.get("id") == old:
            continue
        eid = entry.get("id", path.stem)
        changed = rewrite_entry_texts(entry, old, new, report["links"], eid)
        refs = entry.get("cross_references") or []
        kept = []
        has_new = any(r.get("target_id") == new for r in refs)
        for ref in refs:
            if ref.get("target_id") == old:
                if drop_crossrefs or eid == new or has_new:
                    report["crossrefs_dropped"].append((eid, ref.get("headword") or ref.get("reading")))
                    changed = True
                    continue
                ref["target_id"] = new
                if new_entry is not None:
                    ref["headword"] = new_entry.get("headword", ref.get("headword"))
                    ref["reading"] = new_entry.get("reading", ref.get("reading"))
                has_new = True
                report["crossrefs_repointed"].append((eid, ref.get("headword") or ref.get("reading")))
                changed = True
            kept.append(ref)
        if refs:
            entry["cross_references"] = kept
        if changed:
            report["files"].add(str(path.relative_to(ROOT)))
            if not dry_run:
                write_json(path, entry)
    for path in sorted(ARTICLES.glob("*.json")):
        raw = path.read_text(encoding="utf-8")
        if old not in raw:
            continue
        article = json.loads(raw)
        hits = []
        for key in ("body",):
            if isinstance(article.get(key), str):
                article[key] = rewrite_text(article[key], old, new, hits, f"article {path.stem}")
        rel = article.get("related_entries") or []
        new_rel = []
        for r in rel:
            if isinstance(r, dict) and r.get("entry_id") == old:
                r = dict(r, entry_id=new)
            elif r == old:
                r = new
            if r not in new_rel:
                new_rel.append(r)
        if rel:
            article["related_entries"] = new_rel
        report["links"].extend(hits)
        report["articles"].append(path.stem)
        report["files"].add(str(path.relative_to(ROOT)))
        if not dry_run:
            write_json(path, article)
    if LINK_DECISIONS.exists():
        lines = LINK_DECISIONS.read_text(encoding="utf-8").splitlines()
        out, changed = [], False
        for line in lines:
            if old in line:
                try:
                    rec = json.loads(line)
                    if rec.get("target") == old:
                        rec["target"] = new
                        line = json.dumps(rec, ensure_ascii=False)
                        changed = True
                except ValueError:
                    pass
            out.append(line)
        if changed:
            report["files"].add(str(LINK_DECISIONS.relative_to(ROOT)))
            if not dry_run:
                LINK_DECISIONS.write_text("\n".join(out) + "\n", encoding="utf-8")
    return report


def rename_audio_keys(old: str, new: str, dry_run: bool) -> int:
    path = MANIFEST / f"{range_dir(old)}.jsonl"
    if not path.exists():
        return 0
    lines = path.read_text(encoding="utf-8").splitlines()
    n = 0
    out = []
    for line in lines:
        if line.strip():
            rec = json.loads(line)
            if rec.get("ex", "").startswith(old + "_ex"):
                rec["ex"] = new + rec["ex"][len(old):]
                line = json.dumps(rec, ensure_ascii=False, separators=(",", ":"))
                n += 1
        out.append(line)
    if n and not dry_run:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return n


def record(retired: dict, old: str, new: str, kind: str, reason: str) -> None:
    for k, v in retired.items():
        if v["to"] == old:
            v["to"] = new
    retired[old] = {"to": new, "kind": kind,
                    "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    "reason": reason}


def print_report(report: dict) -> None:
    print(f"  files changed: {len(report['files'])}")
    for where, link in report["links"]:
        print(f"  link  {where}: {link}")
    for eid, hw in report["crossrefs_dropped"]:
        print(f"  xref dropped  {eid}: {hw}")
    for eid, hw in report["crossrefs_repointed"]:
        print(f"  xref repointed {eid}: {hw}")


def cmd_retire(args) -> int:
    old, new = args.old, args.to
    retired = load_retired()
    src = entry_path(old)
    if not src.exists():
        print(f"error: {src} not found", file=sys.stderr)
        return 1
    new = resolve(retired, new)
    if not entry_path(new).exists():
        print(f"error: replacement {new} not found", file=sys.stderr)
        return 1
    print(f"retire {old} → {new}")
    new_entry = json.loads(entry_path(new).read_text(encoding="utf-8"))
    report = update_references(old, new, drop_crossrefs=not args.duplicate, dry_run=args.dry_run,
                               new_entry=new_entry)
    print_report(report)
    if not args.dry_run:
        if args.save:
            dest = Path(args.save) / src.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        src.unlink()
        record(retired, old, new, "retired", args.reason)
        save_retired(retired)
    return 0


def cmd_rename(args) -> int:
    old, new = args.old, args.new
    if old[:5] != new[:5]:
        print("error: a rename keeps the ID number; use retire to merge into another entry",
              file=sys.stderr)
        return 1
    if not ID_RE.match(new):
        print(f"error: bad id {new!r}", file=sys.stderr)
        return 1
    src, dst = entry_path(old), entry_path(new)
    if not src.exists() or dst.exists():
        print(f"error: need {src} to exist and {dst} not to", file=sys.stderr)
        return 1
    retired = load_retired()
    print(f"rename {old} → {new}")
    entry = json.loads(src.read_text(encoding="utf-8"))
    entry["id"] = new
    for ex in entry.get("examples") or []:
        if str(ex.get("id", "")).startswith(old + "_"):
            ex["id"] = new + ex["id"][len(old):]
    rewrite_entry_texts(entry, old, new, [], new)
    report = update_references(old, new, drop_crossrefs=False, dry_run=args.dry_run)
    print_report(report)
    n = rename_audio_keys(old, new, args.dry_run)
    print(f"  audio manifest keys renamed: {n}")
    if not args.dry_run:
        write_json(dst, entry)
        src.unlink()
        record(retired, old, new, "renamed", args.reason)
        save_retired(retired)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("retire", help="delete an entry; its URL redirects to another")
    r.add_argument("old")
    r.add_argument("--to", required=True, help="id of the entry that replaces it")
    r.add_argument("--reason", required=True)
    r.add_argument("--save", help="directory to keep a copy of the deleted file in")
    r.add_argument("--duplicate", action="store_true",
                   help="OLD is a duplicate of the same word: repoint cross-references to NEW "
                        "instead of dropping them")
    r.add_argument("--dry-run", action="store_true")
    r.set_defaults(func=cmd_retire)
    n = sub.add_parser("rename", help="change an entry's romaji; same number, old URL redirects")
    n.add_argument("old")
    n.add_argument("new")
    n.add_argument("--reason", required=True)
    n.add_argument("--dry-run", action="store_true")
    n.set_defaults(func=cmd_rename)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
