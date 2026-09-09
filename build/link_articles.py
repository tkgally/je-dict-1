#!/usr/bin/env python3
"""Inline links for article bodies (``articles/*.json``), placed by the deterministic linker.

Articles are English prose with Japanese words, phrases and short examples
inside. The same ``⟦surface→base：entry_id⟧`` markup as in entries (see the
``inline-word-links`` skill) turns those words into links on the site. This
script runs the linker of ``build/auto_link.py`` over each article body with
the resolution rules and guards used for entries (the kana homophone list and
the decisions ledger), so anything ambiguous stays unlinked and ``noentry`` is
never written. Markdown syntax, furigana wrappers and existing links are
preserved; the Japanese title and the ``related_entries`` headwords are never
linked. Re-running is idempotent: only still-unlinked tokens gain links.

Usage:
    python3 build/link_articles.py                       # dry run: links each article would gain
    python3 build/link_articles.py --apply               # write the links into articles/*.json
    python3 build/link_articles.py --ids keigo,counters --apply
    python3 build/link_articles.py --list                # every link in the (re)linked bodies, kana links marked
    python3 build/link_articles.py --unlinked            # Japanese words left without a link (review queue)
    python3 build/link_articles.py --strip --apply       # drop every link first, then re-link from scratch
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import auto_link as al
from article_utils import (
    article_paths,
    load_article,
    strip_links,
    write_article,
    LINK_RE,
    LINK_INFO_RE,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ids(spec: str | None) -> set[str] | None:
    if not spec:
        return None
    return {s.strip() for s in spec.split(",") if s.strip()}


def build_linker(no_tokenizer: bool = False, no_guards: bool = False):
    tokenizer = al.load_tokenizer(no_tokenizer)
    blocked = frozenset() if no_guards else al.load_blocked_bases()
    unlinked = {} if no_guards else al.load_unlink_decisions()
    resolver = al.Resolver(al.iter_entries(al.ENTRIES_DIR), blocked=blocked, unlinked=unlinked)
    return al.Linker(resolver, tokenizer), resolver


def article_ctx(article_id: str, no_link: tuple[str, ...] = ()) -> al.EntryCtx:
    """An article has no headword of its own; only its ``no_link`` strings are locked.

    ``no_link`` holds plain (furigana-stripped) strings the linker must leave
    alone wherever they occur in the body — the same lock the linker uses for
    an entry's own headword.
    """
    return al.EntryCtx(f"article:{article_id}", [], tuple(no_link), frozenset())


def link_body(body: str, article_id: str, linker: al.Linker, stats: al.Stats | None = None,
              no_link: tuple[str, ...] = ()) -> str:
    return linker.link_text(body, article_ctx(article_id, no_link), stats)


def is_kana_link(surface: str, base: str) -> bool:
    """Both surface and base are kana and the base is not a table function word."""
    plain = al.strip_furigana(surface)
    return (al.is_pure_hiragana(plain) or al.is_pure_katakana(plain)) \
        and al.is_pure_hiragana(base) and base not in al.FUNCTION_WORDS


def list_links(body: str) -> list[tuple[str, str, str, bool]]:
    out = []
    for m in LINK_RE.finditer(body):
        info = LINK_INFO_RE.match(m.group(1))
        if not info:
            continue
        surface, base, eid = info.groups()
        out.append((surface, base, eid, is_kana_link(surface, base)))
    return out


def unlinked_words(body: str, tokenizer, resolver: al.Resolver) -> list[dict]:
    """Japanese content tokens outside links: surface, dictionary form, reading, POS, entry hits."""
    layout = al.Layout(body)
    plain = layout.plain
    found = []
    ls = 0
    while ls <= len(plain):
        le = plain.find("\n", ls)
        if le == -1:
            le = len(plain)
        line = plain[ls:le]
        if line:
            toks = tokenizer.tokenize(line, ls) if tokenizer is not None else al.fallback_tokens(layout, ls, le)
            for t in toks:
                if t.skippable or t.is_particle or t.is_aux:
                    continue
                if len(t.surface) == 1 and (al.is_hiragana(t.surface) or al.is_katakana(t.surface)):
                    continue
                if not layout.free(t.ps, t.pe):
                    continue          # inside a link
                reading = ""
                if t.morpheme is not None:
                    try:
                        reading = al.hira(t.morpheme.reading_form())
                    except Exception:  # pragma: no cover - tokenizer detail
                        reading = ""
                dict_form = t.dict_form or t.surface
                found.append({
                    "surface": t.surface,
                    "dict_form": dict_form,
                    "reading": reading,
                    "pos": t.pos0,
                    "by_headword": len(resolver.by_key.get(dict_form, ())),
                    "by_reading": len(resolver.by_reading.get(reading, ())) if reading else 0,
                    "context": plain[max(0, t.ps - 12):t.pe + 12].replace("\n", " "),
                })
        ls = le + 1
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="report only (default)")
    mode.add_argument("--apply", action="store_true", help="rewrite changed article files")
    ap.add_argument("--ids", help="comma-separated article ids (file stems)")
    ap.add_argument("--strip", action="store_true", help="remove all existing links before linking")
    ap.add_argument("--list", action="store_true", help="print every link of each linked body")
    ap.add_argument("--unlinked", action="store_true",
                    help="print Japanese words left without a link, with dictionary hit counts")
    ap.add_argument("--no-tokenizer", action="store_true", help="force tokenizer-free mode")
    ap.add_argument("--no-guards", action="store_true",
                    help="ignore the homophone list and the decisions ledger (experiments only)")
    ap.add_argument("--quiet", action="store_true", help="no per-article lines")
    args = ap.parse_args()

    linker, resolver = build_linker(args.no_tokenizer, args.no_guards)
    ids = parse_ids(args.ids)
    stats = al.Stats()
    totals = Counter()
    unlinked_index: dict[tuple[str, str, str], list[dict]] = defaultdict(list)

    for path in article_paths(ids):
        article = load_article(path)
        article_id = article.get("id", path.stem)
        original = article.get("body", "")
        source = strip_links(original) if args.strip else original
        no_link = tuple(str(x) for x in article.get("no_link") or [])
        linked = link_body(source, article_id, linker, stats, no_link)
        before = original.count("⟦")
        after = linked.count("⟦")
        changed = linked != original
        totals["articles"] += 1
        totals["links"] += after
        totals["added"] += after - before
        if not args.quiet:
            print(f"{article_id}: {after} links ({after - before:+d})" + (" [changed]" if changed else ""))
        if args.list:
            for surface, base, eid, kana in list_links(linked):
                mark = "  KANA" if kana else ""
                print(f"    ⟦{surface}→{base}：{eid}⟧{mark}")
        if args.unlinked:
            for w in unlinked_words(linked, linker.tok, resolver):
                key = (w["dict_form"], w["reading"], w["pos"])
                w["article"] = article_id
                unlinked_index[key].append(w)
        if args.apply and changed:
            article["body"] = linked
            article.setdefault("metadata", {})["modified"] = utc_now()
            write_article(path, article)

    if args.unlinked:
        print("\nUnlinked Japanese words (dictionary form / reading / POS; hits by headword, by reading):")
        rows = sorted(unlinked_index.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        for (dict_form, reading, pos), occ in rows:
            arts = sorted({o["article"] for o in occ})
            hits = f"hw={occ[0]['by_headword']} rd={occ[0]['by_reading']}"
            print(f"  {dict_form} ({reading}, {pos}) ×{len(occ)}  [{hits}]  {', '.join(arts)}")
            print(f"      e.g. …{occ[0]['context']}…")
        print(f"\n{len(unlinked_index)} distinct unlinked words")

    print(f"\n{totals['articles']} articles, {totals['links']} links ({totals['added']:+d})"
          + ("" if args.apply else " — dry run, nothing written"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
