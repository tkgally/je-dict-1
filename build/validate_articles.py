#!/usr/bin/env python3
"""Validate the articles in ``articles/*.json``.

Errors (the run fails):
  - the file is not valid JSON, does not match ``build/article_schema.json``,
    or its file name differs from its ``id``
  - a kanji without furigana in the title, the body, or a related-entry headword
  - a furigana reading that is not hiragana, or a stray ``{``/``}``
  - an inline link that is unbalanced, malformed, a ``noentry`` marker, or
    whose target entry does not exist
  - a ``related_entries`` target that does not exist, or listed twice

Warnings (printed, not fatal):
  - a link whose base form is not the target entry's headword or reading
  - a related-entry headword that differs from the entry's headword
  - a tag that is not a lower-case slug; ``modified`` earlier than ``created``
  - a ``no_link`` string that does not occur in the body
  - a markdown table whose rows have different numbers of cells
  - a body that does not start with a ``## `` heading

Usage:
    python3 build/validate_articles.py                  # all articles
    python3 build/validate_articles.py --ids keigo      # some of them
    python3 build/validate_articles.py --quiet          # summary line only
Exit status is 1 when any article has an error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from article_utils import (
    ROOT,
    FURI_RE,
    LINK_INFO_RE,
    article_paths,
    load_schema,
    strip_furigana,
    strip_links,
)
from article_renderer import split_table_row, _is_separator_row

ENTRIES_DIR = ROOT / "entries"
KANJI_RE = re.compile(r"[㐀-䶿一-鿿豈-﫿々〆ヶ]")
HIRAGANA_READING_RE = re.compile(r"^[ぁ-ゖー]+$")
LINK_OPEN, LINK_CLOSE = "⟦", "⟧"
TAG_RE = re.compile(r"^[a-z][a-z0-9-]*$")
HEADWORD_ALT_RE = re.compile(r"[／/]")


class Report:
    def __init__(self, article_id: str):
        self.id = article_id
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


class EntryIndex:
    """Entry ids from the file system; headword/reading loaded on demand."""

    def __init__(self, entries_dir: Path = ENTRIES_DIR):
        self.paths = {p.stem: p for p in entries_dir.glob("*/*.json")}
        self._cache: dict[str, dict] = {}

    def __contains__(self, entry_id: str) -> bool:
        return entry_id in self.paths

    def get(self, entry_id: str) -> dict | None:
        if entry_id not in self.paths:
            return None
        if entry_id not in self._cache:
            try:
                self._cache[entry_id] = json.loads(self.paths[entry_id].read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                self._cache[entry_id] = {}
        return self._cache[entry_id]


def base_matches_entry(base: str, entry: dict) -> bool:
    """The link's base form names the entry: its headword, one alternative, or its reading."""
    headword = strip_furigana(entry.get("headword") or "").replace("～", "〜")
    reading = entry.get("reading") or ""
    variants = {headword, headword.strip("〜"), reading}
    variants.update(v.strip("〜") for v in HEADWORD_ALT_RE.split(headword))
    candidates = {base, base.strip("〜")}
    if base.endswith("する"):
        candidates.add(base[:-2])          # 確認する -> the noun entry 確認
    return bool(candidates & variants)


def check_furigana(text: str, where: str, rep: Report) -> None:
    for m in FURI_RE.finditer(text):
        if not HIRAGANA_READING_RE.match(m.group(2)):
            rep.error(f"{where}: reading is not hiragana in {m.group(0)}")
    bare = FURI_RE.sub("", text)
    if "{" in bare or "}" in bare:
        pos = bare.find("{") if "{" in bare else bare.find("}")
        rep.error(f"{where}: stray brace near …{bare[max(0, pos - 15):pos + 15]}…")
    for m in KANJI_RE.finditer(bare):
        rep.error(f"{where}: kanji without furigana near …{bare[max(0, m.start() - 15):m.end() + 15]}…")
        break                              # one report per field is enough


def check_links(body: str, entries: EntryIndex, rep: Report) -> int:
    opens, closes = body.count(LINK_OPEN), body.count(LINK_CLOSE)
    if opens != closes:
        rep.error(f"body: unbalanced link brackets ({opens} open, {closes} close)")
    count = 0
    for m in re.finditer(r"⟦([^⟧]*)⟧", body):
        count += 1
        content = m.group(1)
        info = LINK_INFO_RE.match(content)
        if not info:
            rep.error(f"body: malformed link ⟦{content}⟧")
            continue
        surface, base, eid = info.groups()
        if eid == "noentry":
            rep.error(f"body: noentry marker on {surface} (add the word as a candidate instead)")
            continue
        if LINK_OPEN in surface or "{" in base:
            rep.error(f"body: nested or braced link ⟦{content}⟧")
            continue
        entry = entries.get(eid)
        if entry is None:
            rep.error(f"body: link target does not exist: ⟦{content}⟧")
            continue
        if not base_matches_entry(base, entry):
            rep.warn(f"body: link base {base} is not the headword/reading of {eid} "
                     f"({strip_furigana(entry.get('headword') or '')} / {entry.get('reading')})")
    return count


def check_related(article: dict, entries: EntryIndex, rep: Report) -> None:
    seen = set()
    for ref in article.get("related_entries") or []:
        eid = ref.get("entry_id", "")
        if eid in seen:
            rep.error(f"related_entries: {eid} listed twice")
        seen.add(eid)
        entry = entries.get(eid)
        if entry is None:
            rep.error(f"related_entries: {eid} does not exist")
            continue
        check_furigana(ref.get("headword", ""), f"related_entries[{eid}].headword", rep)
        listed = strip_furigana(ref.get("headword", "")).replace("～", "〜")
        actual = strip_furigana(entry.get("headword") or "").replace("～", "〜")
        if listed != actual:
            rep.warn(f"related_entries: {eid} headword {listed!r} differs from the entry's {actual!r}")


def check_tables(body: str, rep: Report) -> None:
    width = None
    for n, raw in enumerate(body.split("\n"), 1):
        line = raw.strip()
        if line.startswith("|") and line.endswith("|"):
            cells = split_table_row(line)
            if _is_separator_row(cells):
                continue
            if width is None:
                width = len(cells)
            elif len(cells) != width:
                rep.warn(f"body line {n}: table row has {len(cells)} cells, header has {width}")
        else:
            width = None


def check_metadata(article: dict, rep: Report) -> None:
    meta = article.get("metadata") or {}
    stamps = {}
    for key in ("created", "modified"):
        value = meta.get(key, "")
        try:
            stamps[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            rep.error(f"metadata.{key}: not a UTC timestamp of the form YYYY-MM-DDTHH:MM:SSZ: {value!r}")
    if len(stamps) == 2 and stamps["modified"] < stamps["created"]:
        rep.warn("metadata: modified is earlier than created")
    for tag in article.get("tags") or []:
        if not TAG_RE.match(str(tag)):
            rep.warn(f"tags: {tag!r} is not a lower-case slug")


def validate_article(path: Path, schema: dict, entries: EntryIndex) -> tuple[Report, int]:
    rep = Report(path.stem)
    try:
        article = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        rep.error(f"cannot read: {exc}")
        return rep, 0
    try:
        import jsonschema
        errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(article), key=lambda e: list(e.path))
        for err in errors:
            where = "/".join(str(p) for p in err.path) or "(root)"
            rep.error(f"schema: {where}: {err.message}")
    except ImportError:
        for key in ("id", "title", "body", "metadata"):
            if key not in article:
                rep.error(f"schema: missing {key}")
    if not isinstance(article, dict):
        return rep, 0
    if article.get("id") != path.stem:
        rep.error(f"id {article.get('id')!r} does not match file name {path.stem!r}")

    title = article.get("title") or {}
    check_furigana(str(title.get("japanese", "")), "title.japanese", rep)
    if LINK_OPEN in str(title.get("japanese", "")):
        rep.error("title.japanese: links are not rendered in the title")
    body = str(article.get("body", ""))
    check_furigana(strip_links(body), "body", rep)
    links = check_links(body, entries, rep)
    check_related(article, entries, rep)
    check_tables(body, rep)
    check_metadata(article, rep)
    if not body.lstrip().startswith("## "):
        rep.warn("body does not start with a '## ' heading")
    plain_body = strip_furigana(strip_links(body))
    for item in article.get("no_link") or []:
        if str(item) not in plain_body:
            rep.warn(f"no_link: {item!r} does not occur in the body")
    return rep, links


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ids", help="comma-separated article ids (file stems)")
    ap.add_argument("--quiet", action="store_true", help="summary line only")
    args = ap.parse_args()
    ids = {s.strip() for s in args.ids.split(",")} if args.ids else None

    schema = load_schema()
    entries = EntryIndex()
    reports = []
    total_links = 0
    for path in article_paths(ids):
        rep, links = validate_article(path, schema, entries)
        reports.append(rep)
        total_links += links
        if not args.quiet:
            status = "ERROR" if rep.errors else ("warn" if rep.warnings else "ok")
            print(f"{rep.id}: {status} ({links} links)")
            for msg in rep.errors:
                print(f"  ERROR {msg}")
            for msg in rep.warnings:
                print(f"  warn  {msg}")
    n_err = sum(len(r.errors) for r in reports)
    n_warn = sum(len(r.warnings) for r in reports)
    print(f"{len(reports)} articles, {total_links} links: {n_err} errors, {n_warn} warnings")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
