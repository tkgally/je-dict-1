"""Shared helpers for the article system (``articles/*.json``).

An article is a JSON file with ``id``, ``title`` (english / japanese), a
markdown ``body`` with furigana and inline word links, ``related_entries``,
``tags`` and ``metadata`` (schema: ``build/article_schema.json``). This module
finds, loads and writes article files in the repository's layout so that the
linker (``link_articles.py``) and the validator (``validate_articles.py``)
produce byte-identical files for unchanged content.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"
SCHEMA_PATH = ROOT / "build" / "article_schema.json"

KEY_ORDER = ["id", "title", "body", "related_entries", "tags", "metadata"]

LINK_RE = re.compile(r"⟦([^⟧]*)⟧")
LINK_INFO_RE = re.compile(r"^(.+?)→(.+?)：(.+)$")
FURI_RE = re.compile(r"\{([^{}|]+)\|([^{}|]+)\}")


def article_paths(ids: set[str] | None = None):
    """Yield article paths in name order, optionally restricted to the given ids."""
    for path in sorted(ARTICLES_DIR.glob("*.json")):
        if ids and path.stem not in ids:
            continue
        yield path


def load_article(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_article(article: dict) -> str:
    """Serialize an article in the repository layout.

    Two-space indent; ``related_entries`` one object per line; ``tags`` on one
    line; nested objects (``title``, ``metadata``) expanded. Keys follow
    ``KEY_ORDER``, then any others in their original order.
    """
    def js(value) -> str:
        return json.dumps(value, ensure_ascii=False)

    keys = [k for k in KEY_ORDER if k in article] + [k for k in article if k not in KEY_ORDER]
    lines = ["{"]
    for i, key in enumerate(keys):
        comma = "," if i < len(keys) - 1 else ""
        value = article[key]
        if key == "related_entries" and isinstance(value, list):
            if not value:
                lines.append(f'  "related_entries": []{comma}')
                continue
            lines.append('  "related_entries": [')
            for j, ref in enumerate(value):
                ref_comma = "," if j < len(value) - 1 else ""
                inner = ", ".join(f"{js(k)}: {js(v)}" for k, v in ref.items())
                lines.append(f"    {{ {inner} }}{ref_comma}")
            lines.append(f"  ]{comma}")
        elif key == "tags" and isinstance(value, list):
            lines.append(f'  "tags": {js(value)}{comma}')
        elif isinstance(value, dict):
            nested = json.dumps(value, ensure_ascii=False, indent=2)
            nested = "\n".join("  " + line for line in nested.splitlines()).lstrip()
            lines.append(f"  {js(key)}: {nested}{comma}")
        else:
            lines.append(f"  {js(key)}: {js(value)}{comma}")
    lines.append("}")
    return "\n".join(lines) + "\n"


def write_article(path: Path, article: dict) -> None:
    path.write_text(dump_article(article), encoding="utf-8")


def strip_links(text: str) -> str:
    """Replace every ``⟦surface→base：id⟧`` with its surface form."""
    def surface(match):
        info = LINK_INFO_RE.match(match.group(1))
        return info.group(1) if info else match.group(1)
    return LINK_RE.sub(surface, text)


def strip_furigana(text: str) -> str:
    """``{漢字|かんじ}`` -> ``漢字``."""
    return FURI_RE.sub(r"\1", text)


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
