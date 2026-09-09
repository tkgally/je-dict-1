"""Unit tests for build/article_renderer.py (article markdown → HTML).

Covers the two article-specific behaviours that the entry renderer does not
exercise: table cells are split on ``|`` only outside furigana braces and link
brackets, and inline word links ``⟦surface→base：id⟧`` render as links when
the entry exists and as plain text otherwise.

Run with:  python3 -m unittest build.tests.test_article_renderer
"""
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[1]
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))

import article_renderer as ar  # noqa: E402

RUBY_HON = '<ruby>本<rp>(</rp><rt>ほん</rt><rp>)</rp></ruby>'
RUBY_IKU = '<ruby>行<rp>(</rp><rt>い</rt><rp>)</rp></ruby>く'

ENTRIES = {
    "00111_hon": {"id": "00111_hon", "headword": "{本|ほん}", "reading": "ほん"},
    "00119_iku": {"id": "00119_iku", "headword": "{行|い}く", "reading": "いく"},
    "00512_to": {"id": "00512_to", "headword": "と", "reading": "と"},
    "01295_irassharu": {"id": "01295_irassharu", "headword": "いらっしゃる", "reading": "いらっしゃる"},
}


class TestSplitTableRow(unittest.TestCase):
    def test_plain_cells(self):
        self.assertEqual(ar.split_table_row("| a | b | c |"), ["a", "b", "c"])

    def test_furigana_pipe_does_not_split(self):
        cells = ar.split_table_row("| {行|い}く / {来|く}る | go / come |")
        self.assertEqual(cells, ["{行|い}く / {来|く}る", "go / come"])

    def test_link_pipe_does_not_split(self):
        row = "| ⟦{行|い}く→行く：00119_iku⟧ | ⟦いらっしゃる→いらっしゃる：01295_irassharu⟧ |"
        cells = ar.split_table_row(row)
        self.assertEqual(cells, ["⟦{行|い}く→行く：00119_iku⟧", "⟦いらっしゃる→いらっしゃる：01295_irassharu⟧"])

    def test_separator_row(self):
        self.assertTrue(ar._is_separator_row(ar.split_table_row("|---|:---:|")))
        self.assertFalse(ar._is_separator_row(ar.split_table_row("| a | - |")))


class TestTables(unittest.TestCase):
    BODY = "| Plain | Respectful |\n|-------|------------|\n| {行|い}く / {来|く}る | いらっしゃる |\n| いる | いらっしゃる |"

    def test_furigana_cells_keep_their_columns(self):
        html = ar.markdown_to_html(self.BODY)
        self.assertEqual(html.count("<th>"), 2)
        self.assertEqual(html.count("<td>"), 4)
        self.assertIn(f"<td>{RUBY_IKU} / <ruby>来<rp>(</rp><rt>く</rt><rp>)</rp></ruby>る</td>", html)
        self.assertIn("</thead><tbody>", html)
        self.assertTrue(html.endswith("</tbody></table></div>"))

    def test_linked_cells(self):
        body = "| Plain | Respectful |\n|---|---|\n| ⟦{行|い}く→行く：00119_iku⟧ | ⟦いらっしゃる→いらっしゃる：01295_irassharu⟧ |"
        html = ar.markdown_to_html(body, ENTRIES)
        self.assertEqual(html.count("<td>"), 2)
        self.assertIn('<td><a class="word-link" href="../entries/00000/00119_iku.html" data-baseform="行く">'
                      f'{RUBY_IKU}</a></td>', html)


class TestInlineLinks(unittest.TestCase):
    TEXT = "⟦{本|ほん}→本：00111_hon⟧を⟦{読|よ}む→読む：00426_yomu⟧。"

    def test_link_renders_anchor_with_ruby(self):
        html = ar.markdown_to_html(self.TEXT, ENTRIES)
        self.assertIn(f'<p><a class="word-link" href="../entries/00000/00111_hon.html" data-baseform="本">{RUBY_HON}</a>を', html)

    def test_missing_target_renders_surface(self):
        html = ar.markdown_to_html(self.TEXT, ENTRIES)
        self.assertIn('<ruby>読<rp>(</rp><rt>よ</rt><rp>)</rp></ruby>む。</p>', html)
        self.assertNotIn("00426_yomu", html)

    def test_without_entries_dict_links_are_plain(self):
        html = ar.markdown_to_html(self.TEXT)
        self.assertNotIn("<a ", html)
        self.assertNotIn("⟦", html)
        self.assertIn(f"<p>{RUBY_HON}を", html)

    def test_relative_path_is_honoured(self):
        html = ar.markdown_to_html(self.TEXT, ENTRIES, relative_path="../../")
        self.assertIn('href="../../entries/00000/00111_hon.html"', html)

    def test_bold_wraps_a_link(self):
        html = ar.markdown_to_html("ぽたぽた**⟦と→と：00512_to⟧**{落|お}ちる", ENTRIES)
        self.assertIn('<strong><a class="word-link" href="../entries/00500/00512_to.html" data-baseform="と">と</a></strong>', html)

    def test_links_in_headings_and_lists(self):
        body = "## ⟦{本|ほん}→本：00111_hon⟧\n\n- ⟦{本|ほん}→本：00111_hon⟧: book\n\n1. ⟦{本|ほん}→本：00111_hon⟧"
        html = ar.markdown_to_html(body, ENTRIES)
        self.assertEqual(html.count('class="word-link"'), 3)
        self.assertIn("<h2><a ", html)
        self.assertIn("<li><a ", html)

    def test_html_in_text_is_escaped(self):
        html = ar.markdown_to_html("a <b> & ⟦{本|ほん}→本：00111_hon⟧", ENTRIES)
        self.assertIn("a &lt;b&gt; &amp; ", html)


class TestPageLinks(unittest.TestCase):
    def test_relative_page_link(self):
        html = ar.markdown_to_html("See [the counters article](counters.html) and **[keigo](keigo.html#top)**.")
        self.assertIn('<a href="counters.html">the counters article</a>', html)
        self.assertIn('<strong><a href="keigo.html#top">keigo</a></strong>', html)

    def test_absolute_and_external_targets_are_left_alone(self):
        html = ar.markdown_to_html("[x](https://example.com) [y](/root.html)")
        self.assertNotIn("<a ", html)

    def test_page_link_text_may_contain_furigana(self):
        html = ar.markdown_to_html("[{敬|けい}{語|ご}](keigo.html)")
        self.assertIn('<a href="keigo.html"><ruby>敬<rp>(</rp><rt>けい</rt><rp>)</rp></ruby>', html)


class TestArticlePage(unittest.TestCase):
    ARTICLE = {
        "id": "test",
        "title": {"english": "Test Article", "japanese": "{試|し}{験|けん}"},
        "body": "## Intro\n\nRead ⟦{本|ほん}→本：00111_hon⟧.",
        "related_entries": [
            {"entry_id": "00111_hon", "headword": "{本|ほん}", "note": "book"},
            {"entry_id": "99999_nothing", "headword": "なし", "note": "missing"},
        ],
        "tags": ["test"],
        "metadata": {"created": "2026-04-09T13:55:11Z", "modified": "2026-04-09T13:55:11Z", "author": "Test"},
    }

    def test_page_contains_linked_body_and_related_entries(self):
        html = ar.generate_article_html(self.ARTICLE, ENTRIES)
        self.assertIn('<a class="word-link" href="../entries/00000/00111_hon.html" data-baseform="本">', html)
        self.assertIn('href="../entries/00000/00111_hon.html" class="article-related-link"', html)
        self.assertIn('class="article-related-pending">なし', html)
        self.assertNotIn("⟦", html)

    def test_index_lists_article(self):
        html = ar.generate_article_index_html([self.ARTICLE])
        self.assertIn('href="test.html" class="article-card"', html)
        self.assertIn("2 related entries", html)


if __name__ == "__main__":
    unittest.main()
