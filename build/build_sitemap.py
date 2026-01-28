#!/usr/bin/env python3
"""
Build script for generating sitemap.xml and robots.txt for the dictionary website.

Generates:
- robots.txt - crawler directives
- sitemap.xml - sitemap index pointing to sub-sitemaps
- sitemap-pages.xml - main navigation pages
- sitemap-entries.xml - all dictionary entry pages
- sitemap-kanji.xml - kanji index pages
"""

import json
import os
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional

# Japan Standard Time (UTC+9)
JST = timezone(timedelta(hours=9))

# Site configuration
SITE_URL = "https://www.tkgje.jp"

# Main pages to include (excluding utility pages: recent, random, pending)
MAIN_PAGES = [
    ("index.html", 1.0, "daily"),      # Homepage
    ("browse.html", 0.9, "weekly"),    # Browse interface
    ("about.html", 0.9, "monthly"),    # About page
    ("advanced.html", 0.9, "monthly"), # Advanced features
]


def get_current_date() -> str:
    """Get current date in W3C format (YYYY-MM-DD)."""
    return datetime.now(JST).strftime("%Y-%m-%d")


def generate_robots_txt(docs_dir: Path) -> None:
    """Generate robots.txt file."""
    content = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    robots_path = docs_dir / "robots.txt"
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Generated: {robots_path}")


def generate_sitemap_xml_header() -> str:
    """Generate XML header for sitemap files."""
    return '<?xml version="1.0" encoding="UTF-8"?>\n'


def generate_urlset_open() -> str:
    """Generate opening urlset tag with namespace."""
    return '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'


def generate_urlset_close() -> str:
    """Generate closing urlset tag."""
    return '</urlset>\n'


def generate_url_entry(loc: str, lastmod: str, changefreq: str, priority: float) -> str:
    """Generate a single URL entry for a sitemap."""
    return f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority:.1f}</priority>
  </url>
"""


def generate_sitemap_index(docs_dir: Path, sitemaps: list) -> None:
    """Generate the main sitemap index file."""
    lastmod = get_current_date()

    content = generate_sitemap_xml_header()
    content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for sitemap_name in sitemaps:
        content += f"""  <sitemap>
    <loc>{SITE_URL}/{sitemap_name}</loc>
    <lastmod>{lastmod}</lastmod>
  </sitemap>
"""

    content += '</sitemapindex>\n'

    sitemap_path = docs_dir / "sitemap.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Generated: {sitemap_path}")


def generate_sitemap_pages(docs_dir: Path) -> int:
    """Generate sitemap for main navigation pages."""
    lastmod = get_current_date()

    content = generate_sitemap_xml_header()
    content += generate_urlset_open()

    count = 0
    for page, priority, changefreq in MAIN_PAGES:
        page_path = docs_dir / page
        if page_path.exists():
            loc = f"{SITE_URL}/{page}"
            content += generate_url_entry(loc, lastmod, changefreq, priority)
            count += 1

    content += generate_urlset_close()

    sitemap_path = docs_dir / "sitemap-pages.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Generated: {sitemap_path} ({count} URLs)")
    return count


def generate_sitemap_entries(docs_dir: Path, entries_index_path: Path) -> int:
    """Generate sitemap for all dictionary entry pages."""
    lastmod = get_current_date()

    # Load entries index
    with open(entries_index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    entries = index_data.get("entries", [])

    content = generate_sitemap_xml_header()
    content += generate_urlset_open()

    count = 0
    for entry in entries:
        # Convert JSON path to HTML path
        # e.g., "entries/01500/01572_a.json" -> "entries/01500/01572_a.html"
        json_path = entry.get("path", "")
        if json_path:
            html_path = json_path.replace(".json", ".html")
            loc = f"{SITE_URL}/{html_path}"
            content += generate_url_entry(loc, lastmod, "monthly", 0.7)
            count += 1

    content += generate_urlset_close()

    sitemap_path = docs_dir / "sitemap-entries.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Generated: {sitemap_path} ({count} URLs)")
    return count


def generate_sitemap_kanji(docs_dir: Path) -> int:
    """Generate sitemap for kanji index pages."""
    lastmod = get_current_date()

    kanji_dir = docs_dir / "kanji"
    if not kanji_dir.exists():
        print(f"  WARNING: Kanji directory not found: {kanji_dir}")
        return 0

    content = generate_sitemap_xml_header()
    content += generate_urlset_open()

    count = 0
    for html_file in sorted(kanji_dir.glob("*.html")):
        loc = f"{SITE_URL}/kanji/{html_file.name}"
        content += generate_url_entry(loc, lastmod, "monthly", 0.6)
        count += 1

    content += generate_urlset_close()

    sitemap_path = docs_dir / "sitemap-kanji.xml"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Generated: {sitemap_path} ({count} URLs)")
    return count


def build_sitemap(project_root: Path) -> int:
    """
    Main function to build all sitemap files.

    Args:
        project_root: Path to the project root directory

    Returns:
        0 on success, 1 on failure
    """
    docs_dir = project_root / "docs"
    entries_index_path = project_root / "entries_index.json"

    if not docs_dir.exists():
        print(f"ERROR: docs directory not found: {docs_dir}")
        return 1

    if not entries_index_path.exists():
        print(f"ERROR: entries_index.json not found: {entries_index_path}")
        return 1

    print("\n[Sitemap] Generating sitemap and robots.txt files...")

    # Generate robots.txt
    generate_robots_txt(docs_dir)

    # Generate sub-sitemaps
    pages_count = generate_sitemap_pages(docs_dir)
    entries_count = generate_sitemap_entries(docs_dir, entries_index_path)
    kanji_count = generate_sitemap_kanji(docs_dir)

    # Generate sitemap index
    sitemaps = ["sitemap-pages.xml", "sitemap-entries.xml", "sitemap-kanji.xml"]
    generate_sitemap_index(docs_dir, sitemaps)

    # Summary
    total_urls = pages_count + entries_count + kanji_count
    print(f"  Total URLs in sitemap: {total_urls}")

    return 0


def main():
    """Main entry point when run as standalone script."""
    import sys
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    sys.exit(build_sitemap(project_root))


if __name__ == "__main__":
    main()
