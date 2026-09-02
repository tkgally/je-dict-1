"""Unit tests for build/score_note_quality.py and build/prioritize_polishing.py.

Covers the 2026-09 rubric: header-based section detection through the alias
table in build/data/note_headers.json, the content signals, the penalties,
and the prioritizer's new dimensions. Run with:
    python3 -m unittest build.tests.test_note_quality
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_BUILD))
import score_note_quality as snq  # noqa: E402
import prioritize_polishing as pp  # noqa: E402

TEMPLATES = snq.load_templates(str(_BUILD / "note_templates.json"))
TABLE = snq.load_headers()

SURU = TEMPLATES["verb-suru"]
GODAN = TEMPLATES["verb-godan"]
NOUN = TEMPLATES["noun"]


def score(notes, template=GODAN, entry=None):
    entry = entry if entry is not None else {"definitions": [{"sense_number": 1, "gloss": "x"}]}
    return snq.score_entry(entry, notes, template)


PREAMBLE = ("{確認|かくにん} means confirmation — the act of making sure something is "
            "correct and verified before proceeding with the next step of a task.\n\n")

GRAMMAR_NOTES = PREAMBLE + """GRAMMAR:
- 〜を{確認|かくにん}する: to confirm ~
- {確認|かくにん}が{取|と}れる: to get confirmation

SIMILAR WORDS:
- {検証|けんしょう}: verification — more technical, testing a hypothesis
"""
PATTERNS_NOTES = GRAMMAR_NOTES.replace("GRAMMAR:", "COMMON PATTERNS:")

PERFECT_GODAN = """{開|あ}ける is a transitive verb meaning to open something: a door, a window, a box, or a business. It pairs with the intransitive {開|あ}く, which describes the thing opening by itself.

TRANSITIVITY:
- Type: {他動詞|たどうし} (transitive); pair: {開|あ}く (intransitive)

COMMON PATTERNS:
- [thing]を{開|あ}ける: to open [thing]
- {店|みせ}を{開|あ}ける: to open the shop for the day

ASPECT (ている):
- {開|あ}けている: is opening (progressive) or keeps it open (resultant state)

SIMILAR VERBS:
- {開|ひら}く: to open — used for books, meetings, and flowers
"""

PARAGRAPH_ONLY = ("Used with する to form the verb, meaning to extend or to grow. Often "
                  "used in business and technical writing about markets and rates. "
                  "Related words are more general and describe people as well as things.")


class TestSectionDetection(unittest.TestCase):
    def test_grammar_alias_scores_same_as_common_patterns(self):
        s_grammar, b_grammar = score(GRAMMAR_NOTES, SURU)
        s_patterns, b_patterns = score(PATTERNS_NOTES, SURU)
        self.assertEqual(s_grammar, s_patterns)
        self.assertEqual(b_grammar["required"], 20)
        self.assertEqual(b_grammar, b_patterns)

    def test_alias_match_is_case_insensitive_and_whitespace_collapsed(self):
        found = snq.find_sections("common   patterns:\n- 〜を{確認|かくにん}する: to confirm", ["common patterns"])
        self.assertEqual(found, {"common patterns"})
        found = snq.find_sections("### Common Patterns\n- 〜を{確認|かくにん}する: to confirm", ["common patterns"])
        self.assertEqual(found, {"common patterns"})

    def test_parenthetical_headers(self):
        self.assertEqual(snq.find_sections("ASPECT (ている):\n- x", ["aspect"]), {"aspect"})
        self.assertEqual(snq.find_sections("GRAMMAR (sense 2):\n- x", ["common patterns"]), {"common patterns"})
        self.assertEqual(snq.find_sections("COLLOCATIONS (sense 1):\n- x", ["collocations"]), {"collocations"})

    def test_inline_header_only_for_known_labels(self):
        self.assertEqual(snq.find_sections("REGISTER: formal, written", ["register"]), {"register"})
        a = snq.analyze_notes("Xを{確認|かくにん}する: to confirm X")
        self.assertFalse(a["has_header"])

    def test_unknown_label_needs_all_caps(self):
        self.assertTrue(snq.analyze_notes("KANJI BREAKDOWN:\n- {確|かく}: certain")["has_header"])
        self.assertFalse(snq.analyze_notes("Conjugation:\n- {確認|かくにん}して")["has_header"])
        # a known alias in legacy casing is still a header
        self.assertEqual(snq.find_sections("Common collocations:\n- x", ["collocations"]), {"collocations"})

    def test_loose_variants_no_longer_give_credit(self):
        notes = ("This verb is formal and polite in tone. Compare it with similar verbs; "
                 "a common error is to confuse it with its intransitive twin.")
        found = snq.find_sections(
            notes, ["register", "similar verbs", "common mistakes", "transitivity", "aspect", "usage"])
        self.assertEqual(found, set())

    def test_transitivity_fallbacks(self):
        self.assertEqual(snq.find_sections("- Type: {他動詞|たどうし} (transitive)", ["transitivity"]), {"transitivity"})
        self.assertEqual(snq.find_sections("Transitive; takes を.", ["transitivity"]), {"transitivity"})
        self.assertEqual(snq.find_sections("- intransitive verb, pairs with {開|あ}ける", ["transitivity"]), {"transitivity"})
        self.assertEqual(snq.find_sections("The verb is transitive.", ["transitivity"]), set())

    def test_aspect_fallback_needs_explanation(self):
        self.assertEqual(snq.find_sections("- {食|た}べている: eating", ["aspect"]), set())
        self.assertEqual(
            snq.find_sections("- {開|あ}いている: is open (resultant state, not progressive)", ["aspect"]),
            {"aspect"})


class TestRubric(unittest.TestCase):
    def test_points_sum_to_100_and_perfect_note_scores_100(self):
        self.assertEqual(sum(snq.POINTS.values()), 100)
        total, breakdown = score(PERFECT_GODAN, GODAN)
        self.assertEqual(total, 100, breakdown)
        self.assertEqual(set(breakdown), set(snq.BREAKDOWN_KEYS))

    def test_empty_notes_score_zero(self):
        total, breakdown = score("", GODAN)
        self.assertEqual(total, 0)
        self.assertEqual(set(breakdown), set(snq.BREAKDOWN_KEYS))

    def test_paragraph_only_verb_note_gets_only_structure_free_credit(self):
        total, b = score(PARAGRAPH_ONLY, SURU)
        self.assertEqual(b["exists"], 10)
        self.assertEqual(b["length"], 10)
        self.assertEqual(b["furigana"], 5)
        self.assertEqual(b["content_prose"], 10)
        self.assertEqual(b["required"], 0)
        self.assertEqual(b["headers"], 0)
        self.assertEqual(total, 35)

    def test_content_pattern_line(self):
        _, b = score(PREAMBLE + "COMMON PATTERNS:\n- 〜を{確認|かくにん}する: to confirm ~", SURU)
        self.assertEqual(b["content_patterns"], 10)
        _, b = score(PREAMBLE + "COMMON PATTERNS:\n- takes a direct object marked as the thing confirmed", SURU)
        self.assertEqual(b["content_patterns"], 0)

    def test_content_contrast_line(self):
        _, b = score(PREAMBLE + "SIMILAR WORDS:\n- {検証|けんしょう}: verification — more technical", NOUN)
        self.assertEqual(b["content_contrast"], 10)
        _, b = score(PREAMBLE + "CONTRAST:\n・⟦{無能|むのう}→無能：13476_munou⟧ - incompetent", NOUN)
        self.assertEqual(b["content_contrast"], 10)
        # English-only bullet in a contrast section: no term named
        _, b = score(PREAMBLE + "SIMILAR WORDS:\n- verification is the more technical word", NOUN)
        self.assertEqual(b["content_contrast"], 0)
        # Japanese + English bullet outside a contrast section does not count
        _, b = score(PREAMBLE + "COMMON COLLOCATIONS:\n- {検証|けんしょう}する: to verify", NOUN)
        self.assertEqual(b["content_contrast"], 0)

    def test_content_prose_prorated_and_ignores_bullets(self):
        _, b = score("A short note about usage that is under the target length.", NOUN)
        self.assertGreater(b["content_prose"], 0)
        self.assertLess(b["content_prose"], 10)
        bullets = "COMMON COLLOCATIONS:\n" + "\n".join(
            f"- {{確認|かくにん}}{i}: a long English gloss that would count as prose if it were not a bullet"
            for i in range(6))
        _, b = score(bullets, NOUN)
        self.assertEqual(b["content_prose"], 0)

    def test_bloat_penalty_depends_on_sense_count(self):
        sentence = "This sentence pads the note out well past the bloat threshold. "
        notes = PREAMBLE + "USAGE:\n" + sentence * 40      # > 2,000 displayed characters
        single = {"definitions": [{"sense_number": 1, "gloss": "x"}]}
        multi = {"definitions": [{"sense_number": 1, "gloss": "x"}, {"sense_number": 2, "gloss": "y"}]}
        _, b = score(notes, NOUN, single)
        self.assertEqual(b["bloat"], -10)
        self.assertTrue(snq.is_bloated(single, notes))
        _, b = score(notes, NOUN, multi)
        self.assertEqual(b["bloat"], 0)
        self.assertFalse(snq.is_bloated(multi, notes))

    def test_duplicate_header_penalty(self):
        _, b = score(PREAMBLE + "USAGE:\nSome text.\n\nUSAGE:\nMore text.", NOUN)
        self.assertEqual(b["dup_header"], -5)
        _, b = score(PREAMBLE + "COMMON COLLOCATIONS (sense 1):\n- a\n\nCOMMON COLLOCATIONS (sense 2):\n- b", NOUN)
        self.assertEqual(b["dup_header"], 0)
        # repeated inline labels are not duplicated sections
        _, b = score(PREAMBLE + "NOTE: one thing.\nNOTE: another thing.", NOUN)
        self.assertEqual(b["dup_header"], 0)

    def test_optional_sections_capped(self):
        two = PREAMBLE + "COMMON COLLOCATIONS:\n- x\n\nSIMILAR WORDS:\n- y"
        _, b = score(two, NOUN)
        self.assertEqual(b["optional"], 10)
        one = PREAMBLE + "COMMON COLLOCATIONS:\n- x"
        _, b = score(one, NOUN)
        self.assertEqual(b["optional"], 5)

    def test_rubric_text_available(self):
        self.assertIn("RUBRIC", snq.rubric_text())
        self.assertIn("content_contrast", snq.rubric_text())


class TestBareKanjiAndTemplateKey(unittest.TestCase):
    def test_inline_link_base_form_is_not_bare_kanji(self):
        self.assertFalse(snq.has_bare_kanji("⟦{確認|かくにん}→確認：00158_kakunin⟧する"))
        self.assertTrue(snq.has_bare_kanji("確認する"))
        self.assertTrue(snq.has_bare_kanji("⟦確認→確認：00158_kakunin⟧"))  # bare surface

    def test_template_key_prefers_tags_pos(self):
        self.assertEqual(snq.template_key_for_entry(
            {"part_of_speech": "noun", "metadata": {"tags": {"pos": ["noun", "verb-suru"]}}}), "verb-suru")
        self.assertEqual(snq.template_key_for_entry({"part_of_speech": "interjection / adverb"}), "adverb")
        self.assertEqual(snq.template_key_for_entry(
            {"part_of_speech": "interjection", "metadata": {"tags": {"pos": ["interjection"]}}}), "_default")


def _entry(**overrides):
    base = {
        "headword": "{本|ほん}",
        "part_of_speech": "noun",
        "notes": PREAMBLE + "COMMON COLLOCATIONS:\n- {本|ほん}を{読|よ}む: to read a book",
        "examples": [{"japanese": "{本|ほん}を{読|よ}む。", "english": "I read a book."}] * 3,
        "definitions": [{"sense_number": 1, "gloss": "book"}],
        "cross_references": [],
        "prominent_see_also": [],
        "metadata": {"created": "2026-01-01T00:00:00Z", "modified": "2026-08-01T00:00:00Z",
                     "vocabulary_tier": "general",
                     "tags": {"pos": ["noun"], "formality": "neutral", "politeness": "plain"}},
    }
    base.update(overrides)
    return base


class TestPrioritizer(unittest.TestCase):
    def test_uses_the_fixed_bare_kanji_detector(self):
        self.assertFalse(hasattr(pp, "_text_has_bare_kanji"))
        self.assertIs(pp.has_bare_kanji, snq.has_bare_kanji)
        linked = _entry(notes="⟦{確認|かくにん}→確認：00158_kakunin⟧する is common.",
                        examples=[{"japanese": "⟦{確認|かくにん}→確認：00158_kakunin⟧する。", "english": "x"}])
        self.assertEqual(pp.score_furigana_coverage(linked), 1.0)
        bare = _entry(examples=[{"japanese": "確認する。", "english": "x"}])
        self.assertEqual(pp.score_furigana_coverage(bare), 0.0)

    def test_task_weights_sum_to_one_and_task_files_unchanged(self):
        for task, dims in pp.TASK_DIMENSIONS.items():
            self.assertAlmostEqual(sum(w for _d, w in dims), 1.0, places=6, msg=task)
        self.assertEqual(set(pp.PRIORITY_FILES), {"notes", "examples", "cross_refs", "furigana"})

    def test_never_modified_ranks_above_recently_polished(self):
        untouched = _entry(metadata={"created": "2026-03-01T00:00:00Z", "modified": "2026-03-01T00:00:00Z",
                                     "vocabulary_tier": "general",
                                     "tags": {"pos": ["noun"], "formality": "neutral", "politeness": "plain"}})
        polished = _entry(metadata={"created": "2026-03-01T00:00:00Z", "modified": "2026-08-30T00:00:00Z",
                                    "vocabulary_tier": "general",
                                    "tags": {"pos": ["noun"], "formality": "neutral", "politeness": "plain"}})
        self.assertEqual(pp.score_never_modified(untouched), 0.0)
        self.assertEqual(pp.score_never_modified(polished), 1.0)
        entries = [{"id": "00002_polished", "data": polished}, {"id": "00001_untouched", "data": untouched}]
        results = pp.compute_all_priorities(entries, TEMPLATES, {"templates": TEMPLATES})
        self.assertEqual(results["notes"][0][0], "00001_untouched")
        self.assertGreater(results["notes"][0][1], results["notes"][1][1])

    def test_verb_transitivity_tag_dimension(self):
        verb = _entry(metadata={"created": "a", "modified": "b", "vocabulary_tier": "general",
                                "tags": {"pos": ["verb-godan"], "formality": "neutral", "politeness": "plain"}})
        self.assertEqual(pp.score_verb_transitivity_tag(verb), 0.0)
        verb["metadata"]["tags"]["transitivity"] = "transitive"
        self.assertEqual(pp.score_verb_transitivity_tag(verb), 1.0)
        self.assertEqual(pp.score_verb_transitivity_tag(_entry()), 1.0)  # noun: n/a

    def test_politeness_formality_and_bloat_dimensions(self):
        self.assertEqual(pp.score_politeness_formality(_entry()), 1.0)
        half = _entry(metadata={"created": "a", "modified": "b", "tags": {"pos": ["noun"], "formality": "neutral"}})
        self.assertEqual(pp.score_politeness_formality(half), 0.5)
        bloated = _entry(notes="USAGE:\n" + "This sentence pads the note out past the threshold. " * 45)
        self.assertEqual(pp.score_note_bloat(bloated), 0.0)
        self.assertEqual(pp.score_note_bloat(_entry()), 1.0)

    def test_linkable_unlinked_dimension(self):
        lookup = {
            "本革": [{"id": "16787_hongawa"}],
            "解消": [{"id": "21324_kaishousuru"}],
            "合皮": [{"id": "1_a"}, {"id": "2_b"}],           # ambiguous: two candidates
            "本": [{"id": "00001_hon"}],
        }
        notes = (PREAMBLE + "SIMILAR WORDS:\n"
                 "- {本革|ほんかわ}: genuine leather — the everyday word\n"
                 "- {解消|かいしょう}する: to dissolve — for problems\n"
                 "- {合皮|ごうひ}: faux leather\n"
                 "- ⟦メモ→メモ：00274_memo⟧ - a quick note\n"
                 "- {本|ほん}: the headword itself\n")
        entry = _entry(notes=notes)
        found = pp.find_linkable_terms(entry, "00001_hon", lookup)
        self.assertEqual(found, ["16787_hongawa", "21324_kaishousuru", "00274_memo"])
        self.assertEqual(pp.score_linkable_unlinked(entry, "00001_hon", lookup), 0.0)
        one = _entry(notes=PREAMBLE + "RELATED TERMS:\n- {本革|ほんかわ}: genuine leather\n")
        self.assertAlmostEqual(pp.score_linkable_unlinked(one, "00001_hon", lookup), 2 / 3)
        # already cross-referenced: not a gap
        entry["cross_references"] = [{"target_id": "16787_hongawa", "type": "similar"}]
        self.assertEqual(pp.score_linkable_unlinked(entry, "00001_hon", lookup), 1.0)
        # no lookup available: neutral
        self.assertEqual(pp.score_linkable_unlinked(_entry(notes=notes), "00001_hon", {}), 1.0)

    def test_accuracy_flags_loader_and_dimension(self):
        with tempfile.TemporaryDirectory() as tmp:
            flags = os.path.join(tmp, "accuracy_flags.jsonl")
            decisions = os.path.join(tmp, "decisions.jsonl")
            self.assertEqual(pp.load_outstanding_flags(flags, decisions), {})   # missing file
            with open(flags, "w") as f:
                f.write(json.dumps({"entry_id": "00001_a", "reviewed_at": "2026-09-01T00:00:00Z",
                                    "issues": [{"severity": "error"}]}) + "\n")
                f.write(json.dumps({"entry_id": "00002_b", "reviewed_at": "2026-09-01T00:00:00Z",
                                    "issues": [{"severity": "warn"}]}) + "\n")
                f.write(json.dumps({"entry_id": "00003_c", "reviewed_at": "2026-09-01T00:00:00Z",
                                    "issues": []}) + "\n")
                f.write(json.dumps({"entry_id": "00004_d", "reviewed_at": "2026-09-01T00:00:00Z",
                                    "issues": [{"severity": "warn"}]}) + "\n")
                # a later review of 00004_d replaces the earlier line
                f.write(json.dumps({"entry_id": "00004_d", "reviewed_at": "2026-09-03T00:00:00Z",
                                    "issues": [{"severity": "error"}]}) + "\n")
            with open(decisions, "w") as f:
                f.write(json.dumps({"ts": "2026-08-30T00:00:00Z", "entry": "00001", "decision": "reject"}) + "\n")
                f.write(json.dumps({"ts": "2026-09-02T00:00:00Z", "entry": "00002", "decision": "apply"}) + "\n")
                f.write(json.dumps({"ts": "2026-09-02T00:00:00Z", "entry": "00004", "decision": "apply"}) + "\n")
            out = pp.load_outstanding_flags(flags, decisions)
            self.assertEqual(out, {"00001_a": "error", "00004_d": "error"})
            self.assertEqual(pp.score_accuracy_flag("00001_a", out), 0.0)
            self.assertEqual(pp.score_accuracy_flag("00002_b", out), 1.0)
            self.assertEqual(pp.score_accuracy_flag("00003_c", out), 1.0)
            self.assertEqual(pp.score_accuracy_flag("00009_z", {"00009_z": "warn"}), 0.5)


if __name__ == "__main__":
    unittest.main()
