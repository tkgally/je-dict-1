"""Unit tests for build/normalize_pos.py — canonical part_of_speech rendering,
free-text parsing and the rewrite / disagreement / unparsed classification.
Run with:
    python3 -m unittest build.tests.test_normalize_pos
"""
import importlib.util
import sys
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[2] / "build"
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))
_spec = importlib.util.spec_from_file_location("normalize_pos", _BUILD / "normalize_pos.py")
np_ = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(np_)


def _entry(text, pos, transitivity=None):
    tags = {"pos": pos}
    if transitivity is not None:
        tags["transitivity"] = transitivity
    return {"id": "00001_x", "part_of_speech": text, "metadata": {"tags": tags}}


class TestRender(unittest.TestCase):
    def test_single_tags(self):
        self.assertEqual(np_.render(["noun"]), "noun")
        self.assertEqual(np_.render(["verb-godan"]), "verb (godan)")
        self.assertEqual(np_.render(["verb-ichidan"]), "verb (ichidan)")
        self.assertEqual(np_.render(["verb-suru"]), "suru verb")
        self.assertEqual(np_.render(["adjective-na"]), "na-adjective")
        self.assertEqual(np_.render(["pre-noun-adjectival"]), "pre-noun adjectival")
        self.assertEqual(np_.render(["onomatopoeia"]), "onomatopoeia")

    def test_joined_in_tag_order(self):
        self.assertEqual(np_.render(["noun", "verb-suru"]), "noun, suru verb")
        self.assertEqual(np_.render(["adjective-na", "noun"]), "na-adjective, noun")

    def test_transitivity_qualifier_on_first_verb_tag(self):
        self.assertEqual(np_.render(["verb-godan"], "transitive"), "verb (godan, transitive)")
        self.assertEqual(np_.render(["noun", "verb-suru"], "intransitive"), "noun, suru verb (intransitive)")
        self.assertEqual(np_.render(["verb-ichidan"], "both"), "verb (ichidan, transitive/intransitive)")
        self.assertEqual(np_.render(["noun"], "transitive"), "noun")   # no verb tag -> nothing to qualify


class TestParse(unittest.TestCase):
    def test_common_spellings(self):
        for text in ("noun, suru verb", "noun / suru-verb", "noun, verb (suru)", "noun, verb (する)",
                     "noun/verb-suru", "noun (verbal)"):
            p = np_.parse_display(text)
            self.assertEqual(p.pos, {"noun", "verb-suru"}, text)
            self.assertEqual(p.unknown, [], text)
        self.assertEqual(np_.parse_display("godan verb").pos, {"verb-godan"})
        self.assertEqual(np_.parse_display("verb (ichidan)").pos, {"verb-ichidan"})
        self.assertEqual(np_.parse_display("adjective (i-adjective)").pos, {"adjective-i"})
        self.assertEqual(np_.parse_display("adjective (na)").pos, {"adjective-na"})
        self.assertEqual(np_.parse_display("pre-noun adjective").pos, {"pre-noun-adjectival"})
        self.assertEqual(np_.parse_display("adverb, mimetic").pos, {"adverb", "onomatopoeia"})
        self.assertEqual(np_.parse_display("expression (proverb)").pos, {"expression"})
        self.assertEqual(np_.parse_display("verb (godan む)").pos, {"verb-godan"})

    def test_generic_families(self):
        p = np_.parse_display("verb")
        self.assertEqual(p.generic, {"@verb"})
        self.assertEqual(p.pos, set())
        self.assertEqual(np_.parse_display("adjective").generic, {"@adjective"})

    def test_pronoun_is_not_noun(self):
        self.assertEqual(np_.parse_display("pronoun").pos, {"pronoun"})

    def test_transitivity(self):
        self.assertEqual(np_.parse_display("godan verb, transitive").transitivity, "transitive")
        self.assertEqual(np_.parse_display("verb (godan, intransitive)").transitivity, "intransitive")
        self.assertEqual(np_.parse_display("godan verb, transitive/intransitive").transitivity, "both")
        self.assertEqual(np_.parse_display("noun, suru verb, intransitive, transitive").transitivity, "both")
        self.assertIsNone(np_.parse_display("noun").transitivity)

    def test_unknown_tokens(self):
        self.assertEqual(np_.parse_display("noun (proper)").unknown, ["proper"])
        self.assertEqual(np_.parse_display("expression, verb phrase").unknown, ["verb phrase"])


class TestClassify(unittest.TestCase):
    def test_canonical(self):
        self.assertEqual(np_.classify(_entry("noun, suru verb", ["noun", "verb-suru"]))["status"], "canonical")
        # the qualifier form is accepted as canonical when tags agree
        self.assertEqual(np_.classify(_entry("verb (godan, transitive)", ["verb-godan"], "transitive"))["status"],
                         "canonical")
        self.assertTrue(np_.is_canonical_display("verb (godan)", {"pos": ["verb-godan"], "transitivity": "transitive"}))
        self.assertFalse(np_.is_canonical_display("verb (godan, transitive)", {"pos": ["verb-godan"]}))

    def test_rewrite(self):
        r = np_.classify(_entry("godan verb", ["verb-godan"]))
        self.assertEqual((r["status"], r["canonical"]), ("rewrite", "verb (godan)"))
        r = np_.classify(_entry("noun / suru-verb", ["noun", "verb-suru"]))
        self.assertEqual(r["canonical"], "noun, suru verb")
        # generic "verb" is satisfied by any verb tag
        r = np_.classify(_entry("verb", ["verb-ichidan"]))
        self.assertEqual((r["status"], r["canonical"]), ("rewrite", "verb (ichidan)"))

    def test_rewrite_keeps_qualifier_only_when_tags_agree(self):
        r = np_.classify(_entry("godan verb, transitive", ["verb-godan"], "transitive"))
        self.assertEqual((r["status"], r["canonical"]), ("rewrite", "verb (godan, transitive)"))
        r = np_.classify(_entry("godan verb, transitive", ["verb-godan"], None))
        self.assertEqual(r["status"], "disagreement")
        r = np_.classify(_entry("godan verb, transitive", ["verb-godan"], "intransitive"))
        self.assertEqual(r["status"], "disagreement")
        # a qualifier is never ADDED from tags alone
        r = np_.classify(_entry("godan verb", ["verb-godan"], "transitive"))
        self.assertEqual(r["canonical"], "verb (godan)")

    def test_disagreement_when_text_has_more_than_tags(self):
        r = np_.classify(_entry("noun, suru verb", ["noun"]))
        self.assertEqual(r["status"], "disagreement")
        self.assertIn("verb-suru", r["reason"])
        r = np_.classify(_entry("expression (verb)", ["expression"]))
        self.assertEqual(r["status"], "disagreement")

    def test_unparsed(self):
        r = np_.classify(_entry("noun (proper)", ["noun"]))
        self.assertEqual(r["status"], "unparsed")
        self.assertIn("proper", r["reason"])

    def test_no_pos_tags(self):
        self.assertEqual(np_.classify(_entry("noun", []))["status"], "no-pos-tags")
        self.assertEqual(np_.classify({"id": "x", "part_of_speech": "noun", "metadata": {}})["status"],
                         "no-pos-tags")

    def test_strict_holds_out_tag_additions(self):
        loose = np_.classify(_entry("noun", ["noun", "verb-suru"]))
        self.assertEqual((loose["status"], loose["canonical"], loose["adds"]),
                         ("rewrite", "noun, suru verb", ["verb-suru"]))
        strict = np_.classify(_entry("noun", ["noun", "verb-suru"]), strict=True)
        self.assertEqual(strict["status"], "tags-add-pos")
        # nothing added -> strict makes no difference
        self.assertEqual(np_.classify(_entry("godan verb", ["verb-godan"]), strict=True)["status"], "rewrite")


if __name__ == "__main__":
    unittest.main()
