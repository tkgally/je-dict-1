"""Tests for build/brainstorm_candidates.py (candidate brainstorming: filter, record, prompts)."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import brainstorm_candidates as bc  # noqa: E402


class BrainstormTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.saved = {k: getattr(bc, k) for k in
                      ("ENTRIES_INDEX", "CANDIDATES", "RETIRED", "TASK_DIR", "STATE", "LEDGER")}
        bc.ENTRIES_INDEX = root / "entries_index.json"
        bc.CANDIDATES = root / "candidate_words.json"
        bc.RETIRED = root / "retired.json"
        bc.TASK_DIR = root / "brainstorm"
        bc.STATE = bc.TASK_DIR / "state.json"
        bc.LEDGER = bc.TASK_DIR / "ledger.jsonl"
        bc.ENTRIES_INDEX.write_text(json.dumps({"entries": [
            {"id": "00001_tori", "headword": "{鳥|とり}", "reading": "とり", "gloss": "bird",
             "vocabulary_tier": "basic"},
            {"id": "00002_kan", "headword": "〜{感|かん}", "reading": "かん", "gloss": "sense of",
             "vocabulary_tier": "general"},
            {"id": "00003_dekakeru", "headword": "{出|で}かける", "reading": "でかける",
             "gloss": "to go out", "vocabulary_tier": "core"},
        ]}), encoding="utf-8")
        bc.CANDIDATES.write_text(json.dumps({"candidates": [
            {"id": "C1", "word": "ペリカン", "reading": "ぺりかん"}]}), encoding="utf-8")
        bc.RETIRED.write_text("{}", encoding="utf-8")
        self.root = root

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(bc, k, v)
        self.tmp.cleanup()

    def proposals(self, items, name="p.json"):
        path = self.root / name
        path.write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")
        return str(path)

    def run_filter(self, *files):
        out = self.root / "out.json"
        bc.cmd_filter(SimpleNamespace(files=list(files), out=str(out)))
        return json.loads(out.read_text(encoding="utf-8"))

    def test_drops_entries_candidates_and_tilde_affixes(self):
        f = self.proposals([
            {"word": "鳥", "reading": "とり", "by": "m1"},
            {"word": "感", "reading": "かん", "by": "m1"},
            {"word": "ペリカン", "reading": "ぺりかん", "by": "m1"},
            {"word": "七面鳥", "reading": "しちめんちょう", "by": "m1", "usefulness": 3},
        ])
        self.assertEqual([x["word"] for x in self.run_filter(f)], ["七面鳥"])

    def test_merges_models_and_ranks_agreement_first(self):
        a = self.proposals([{"word": "鶉", "reading": "うずら", "by": "m1", "usefulness": 2},
                            {"word": "駝鳥", "reading": "だちょう", "by": "m1", "usefulness": 3}], "a.json")
        b = self.proposals([{"word": "鶉", "reading": "うずら", "by": "m2", "usefulness": 2}], "b.json")
        out = self.run_filter(a, b)
        self.assertEqual(out[0]["word"], "鶉")
        self.assertEqual(out[0]["by"], ["m1", "m2"])

    def test_flags_variant_spellings(self):
        f = self.proposals([{"word": "出掛ける", "reading": "でかける", "by": "m1"},
                            {"word": "ダチョウ", "reading": "だちょう", "by": "m1"},
                            {"word": "駝鳥", "reading": "だちょう", "by": "m2"}])
        out = {x["word"]: x for x in self.run_filter(f)}
        self.assertIn("00003_dekakeru", out["出掛ける"]["possible_variant_of"][0])
        self.assertEqual(out["ダチョウ"]["alt_spellings"], ["駝鳥"])

    def test_record_logs_verdicts_advances_cursor_and_skips_decided(self):
        batch = self.proposals({"lens": "seeds", "cursor_start": 0, "cursor_end": 20}, "batch.json")
        verdicts = self.proposals([{"word": "鶉", "reading": "うずら", "verdict": "rejected",
                                    "reason": "rare"}], "v.json")
        bc.cmd_record(SimpleNamespace(batch=batch, verdicts=verdicts))
        st = bc.load_state()
        self.assertEqual((st["seed_cursor"], st["next_lens"]), (20, "field"))
        f = self.proposals([{"word": "鶉", "reading": "うずら", "by": "m1"}])
        self.assertEqual(self.run_filter(f), [])

    def test_prompts_name_the_rules(self):
        seeds = {"lens": "seeds", "seeds": [{"id": "00001_tori", "headword": "鳥", "reading": "とり",
                                              "gloss": "bird", "semantic": ["animal-bird"]}]}
        p = bc.prompt_for(seeds, 6)
        self.assertIn("00001_tori", p)
        self.assertIn("Do not copy from any dictionary or word list", p)
        field = {"lens": "field", "field": "animal-bird", "members": ["鳥(とり)"], "members_total": 1}
        self.assertIn('"animal-bird"', bc.prompt_for(field, 6))


if __name__ == "__main__":
    unittest.main()
