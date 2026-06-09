"""Unit tests for review_accuracy.py's pure logic (no API calls).

Run with:  python3 -m unittest build.tests.test_review_accuracy
"""
import importlib.util
import unittest
from pathlib import Path

_MOD = Path(__file__).resolve().parents[2] / "build" / "review_accuracy.py"
_spec = importlib.util.spec_from_file_location("review_accuracy", _MOD)
ra = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ra)

ENTRY = {
    "id": "05747_kirisuteru",
    "headword": "{切|き}り{捨|す}てる",
    "reading": "きりすてる",
    "metadata": {"tags": {"pos": ["verb-ichidan"], "semantic": ["body-part"],
                          "formality": "neutral", "politeness": "plain"}},
    "gloss": "to cut down, to discard",
    "definitions": [{"sense_number": 1, "gloss": "to cut down", "explanation": "..."}],
    "examples": [{"japanese": "⟦{無駄|むだ}な→無駄：1⟧{経費|けいひ}を{切|き}り{捨|す}てる。",
                  "english": "To eliminate unnecessary expenses."}],
}


class TestPayload(unittest.TestCase):
    def test_strips_furigana_and_links(self):
        p = ra.entry_payload(ENTRY)
        self.assertEqual(p["headword"], "切り捨てる")
        # inline link + furigana stripped to plain Japanese
        self.assertEqual(p["examples"][0]["japanese"], "無駄な経費を切り捨てる。")
        self.assertEqual(p["semantic_tags"], ["body-part"])


class TestPrompt(unittest.TestCase):
    def test_includes_only_selected_dimension_checks(self):
        tags_only = ra.build_prompt(ENTRY, ("tags",))
        self.assertIn('"tags"', tags_only)
        self.assertIn("HEADWORD", tags_only)  # the anti-example-topic instruction
        self.assertNotIn("an example's English", tags_only)  # translation check absent
        full = ra.build_prompt(ENTRY, ("gloss", "translation", "tags"))
        self.assertIn("an example's English", full)
        self.assertIn("切り捨てる", full)  # headword present, furigana-stripped


class TestFilterIssues(unittest.TestCase):
    def test_keeps_only_requested_dimensions_and_dicts(self):
        issues = [
            {"dimension": "tags", "concern": "x"},
            {"dimension": "translation", "concern": "y"},
            {"dimension": "gloss", "concern": "z"},
            "not-a-dict",
        ]
        out = ra.filter_issues(issues, ("tags", "gloss"))
        self.assertEqual([i["dimension"] for i in out], ["tags", "gloss"])

    def test_non_list_returns_empty(self):
        self.assertEqual(ra.filter_issues(None, ("tags",)), [])
        self.assertEqual(ra.filter_issues({}, ("tags",)), [])


if __name__ == "__main__":
    unittest.main()
