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
    "metadata": {"tags": {"pos": ["verb-ichidan"], "semantic": ["body-part", "action"],
                          "formality": "formal", "politeness": "plain"}},
    "gloss": "to cut down, to discard",
    "definitions": [{"sense_number": 1, "gloss": "to cut down", "explanation": "..."}],
    "examples": [{"japanese": "⟦{無駄|むだ}な→無駄：1⟧{経費|けいひ}を{切|き}り{捨|す}てる。",
                  "english": "To eliminate unnecessary expenses."}],
    "notes": "USAGE:\nA formal word used mainly in {書|か}き{言葉|ことば}.\n\n"
             "GRAMMAR:\nAttaches to the past tense only.",
}
DIMS = ("gloss", "translation", "tags", "notes")


class TestPayload(unittest.TestCase):
    def test_strips_furigana_and_links(self):
        p = ra.entry_payload(ENTRY)
        self.assertEqual(p["headword"], "切り捨てる")
        self.assertEqual(p["examples"][0]["japanese"], "無駄な経費を切り捨てる。")
        self.assertEqual(p["semantic_tags"], ["body-part", "action"])
        self.assertIn("A formal word used mainly in 書き言葉.", p["notes"])

    def test_notes_omitted_when_not_needed(self):
        self.assertNotIn("notes", ra.entry_payload(ENTRY, include_notes=False))


class TestPrompt(unittest.TestCase):
    def test_includes_only_selected_dimension_checks(self):
        tags_only = ra.build_prompt(ENTRY, ("tags",))
        self.assertIn('"tags"', tags_only)
        self.assertIn("BREADTH IS NEVER A REASON", tags_only)
        self.assertNotIn("an example's English", tags_only)
        full = ra.build_prompt(ENTRY, DIMS)
        self.assertIn("an example's English", full)
        self.assertIn('"notes": a factual', full)
        self.assertIn("切り捨てる", full)

    def test_prompt_does_not_ask_for_list_membership(self):
        p = ra.build_prompt(ENTRY, ("tags",))
        self.assertIn("software does that", p)


class TestOffVocab(unittest.TestCase):
    def test_code_flags_off_vocabulary_tag(self):
        e = {"metadata": {"tags": {"semantic": ["general", "not-a-real-tag"]}}}
        issues = ra.offvocab_issues(e)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["family"], "offvocab")
        self.assertEqual(issues[0]["tag"], "not-a-real-tag")
        self.assertEqual(issues[0]["source"], "code")

    def test_in_list_tags_produce_nothing(self):
        self.assertEqual(ra.offvocab_issues(ENTRY), [])


class TestPostFilter(unittest.TestCase):
    def _run(self, issues, keep_warn=False):
        return ra.postfilter_issues(ENTRY, issues, DIMS, keep_warn=keep_warn)

    def test_breadth_complaints_dropped(self):
        kept, dropped = self._run([{"dimension": "tags", "location": "tags.semantic",
                                    "severity": "error",
                                    "concern": "'action' is too broad for this verb",
                                    "suggestion": "movement"}])
        self.assertEqual(kept, [])
        self.assertEqual(dropped, {"breadth": 1})

    def test_general_too_broad_dropped(self):
        e = dict(ENTRY); e["metadata"] = {"tags": {"semantic": ["general"]}}
        kept, dropped = ra.postfilter_issues(
            e, [{"dimension": "tags", "location": "tags.semantic", "severity": "error",
                 "concern": "'general' is a placeholder; use a concrete domain",
                 "suggestion": "health"}], DIMS)
        self.assertEqual(kept, [])
        self.assertIn(sum(dropped.values()), (1,))

    def test_wrong_category_on_present_tag_kept(self):
        kept, dropped = self._run([{"dimension": "tags", "location": "tags.semantic",
                                    "severity": "error",
                                    "concern": "'body-part' is wrong: the verb names an action, not a body part",
                                    "suggestion": "remove body-part"}])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]["family"], "wrong-category")

    def test_absent_tag_dropped(self):
        kept, dropped = self._run([{"dimension": "tags", "location": "tags.semantic",
                                    "severity": "error",
                                    "concern": "'clothing' does not fit",
                                    "suggestion": "remove clothing"}])
        self.assertEqual(kept, [])
        self.assertEqual(dropped, {"absent-tag": 1})

    def test_out_of_list_suggestion_dropped(self):
        kept, dropped = self._run([{"dimension": "tags", "location": "tags.semantic",
                                    "severity": "error",
                                    "concern": "'body-part' is the wrong category",
                                    "suggestion": "surgery"}])
        self.assertEqual(kept, [])
        self.assertEqual(dropped, {"out-of-list-suggestion": 1})

    def test_register_flag_requires_verbatim_quote(self):
        base = {"dimension": "tags", "location": "tags.formality", "severity": "error",
                "concern": "formality should be neutral, not formal",
                "suggestion": "neutral"}
        kept, dropped = self._run([dict(base)])
        self.assertEqual(kept, [])
        self.assertEqual(dropped, {"register-noquote": 1})
        kept, dropped = self._run([dict(base, quote="A formal word used mainly in 書き言葉.")])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]["family"], "register")
        kept, dropped = self._run([dict(base, quote="This word is casual and everyday.")])
        self.assertEqual(kept, [])

    def test_notes_flag_requires_quote_and_error(self):
        base = {"dimension": "notes", "location": "notes", "severity": "error",
                "concern": "ものの attaches to any plain form, not only the past tense",
                "suggestion": "rewrite the GRAMMAR line"}
        kept, dropped = self._run([dict(base, quote="Attaches to the past tense only.")])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]["family"], "notes-fact")
        kept, dropped = self._run([dict(base)])
        self.assertEqual(dropped, {"notes-noquote": 1})
        kept, dropped = self._run([dict(base, severity="warn",
                                        quote="Attaches to the past tense only.")])
        self.assertEqual(kept, [])

    def test_warn_dropped_unless_kept(self):
        it = {"dimension": "gloss", "location": "gloss", "severity": "warn",
              "concern": "gloss says lend but the word means borrow", "suggestion": "borrow"}
        kept, dropped = self._run([dict(it)])
        self.assertEqual(kept, [])
        kept, dropped = self._run([dict(it)], keep_warn=True)
        self.assertEqual(len(kept), 1)

    def test_stylistic_translation_dropped_but_meaning_kept(self):
        style = {"dimension": "translation", "location": "examples[0]", "severity": "error",
                 "concern": "a more natural phrasing would be 'cut'", "suggestion": "..."}
        meaning = {"dimension": "translation", "location": "examples[0]", "severity": "error",
                   "concern": "says 'absorb' but 跳ね返す means to withstand, the opposite",
                   "suggestion": "withstand"}
        kept, dropped = self._run([style, meaning])
        self.assertEqual(len(kept), 1)
        self.assertEqual(kept[0]["family"], "translation-meaning")
        self.assertEqual(dropped, {"style": 1})

    def test_model_offvocab_claim_dropped_in_favour_of_code(self):
        kept, dropped = self._run([{"dimension": "tags", "location": "tags.semantic",
                                    "severity": "error",
                                    "concern": "'body-part' is not in the valid tag list",
                                    "suggestion": "body-internal"}])
        self.assertEqual(kept, [])
        self.assertEqual(dropped, {"offvocab-model": 1})


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
