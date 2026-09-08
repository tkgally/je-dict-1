"""Unit tests for build/check_link_homophones.py and the fixer in build/review_links.py.

Run with:  python3 -m unittest build.tests.test_check_link_homophones
"""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

_BUILD = Path(__file__).resolve().parents[1]
if str(_BUILD) not in sys.path:
    sys.path.insert(0, str(_BUILD))


def _load(name):
    spec = importlib.util.spec_from_file_location(name, _BUILD / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


clh = _load("check_link_homophones")
rl = _load("review_links")


ENTRY = {
    "id": "16667_aashite",
    "headword": "ああして",
    "reading": "ああして",
    "examples": [
        {"id": "x1", "japanese": "ああして⟦{座|すわ}っている→座る：00757_suwaru⟧⟦と→と：00512_to⟧⟦{疲|つか}れる→疲れる：00901_tsukareru⟧。",
         "english": "Sitting like that makes you tired."},
        {"id": "x2", "japanese": "⟦{子供|こども}→子供：00554_kodomo⟧⟦の→の：09472_no⟧⟦{頃|ころ}→ころ：03091_koro⟧⟦から→から：00504_kara⟧⟦かけて→かける：00854_kakeru⟧いた。",
         "english": "I had been wearing them since childhood."},
        {"id": "x3", "japanese": "⟦パソコン→パソコン：01538_pasokon⟧⟦を→を：00422_wo⟧⟦つけて→つける：00562_tsukeru⟧⟦ください→ください：02899_kudasai⟧。",
         "english": "Please turn on the computer."},
    ],
    "notes": "USAGE:\nPart of the こそあど system: ⟦こうして→こうして：26873_koushite⟧ (like this), "
             "⟦そうして→そうして：02943_soushite⟧ (like that, near listener).\n\n"
             "SIMILAR WORDS:\n- ⟦そうして→そうして：02943_soushite⟧: like that\n"
             "- ⟦{矍鑠|かくしゃく}→矍鑠：noentry⟧: vigorous",
}


class TestInventory(unittest.TestCase):
    def test_only_kana_surface_and_kana_base_links_are_in_the_class(self):
        occ = clh.kana_link_occurrences(ENTRY)
        bases = sorted({(o["field"], o["base"]) for o in occ})
        # 頃→ころ has a kanji surface (lexeme-exact), particles are table words,
        # ください is a table word, パソコン is katakana, noentry markers are skipped
        self.assertEqual(bases, [("examples[1]", "かける"), ("examples[2]", "つける"),
                                 ("notes", "こうして"), ("notes", "そうして")])
        soushite = [o for o in occ if o["base"] == "そうして"]
        self.assertEqual(len(soushite), 2)
        self.assertEqual(soushite[0]["target"], "02943_soushite")
        self.assertEqual(soushite[0]["surface"], "そうして")
        self.assertIn("【そうして】 (like that, near listener)", soushite[0]["context"])
        self.assertTrue(soushite[1]["context"].startswith("- 【そうして】: like that"))
        kakeru = [o for o in occ if o["base"] == "かける"][0]
        self.assertEqual(kakeru["context"], "子供の頃から【かけて】いた。")
        self.assertEqual(kakeru["english"], "I had been wearing them since childhood.")

    def test_context_is_confined_to_the_line(self):
        occ = [o for o in clh.kana_link_occurrences(ENTRY) if o["field"] == "notes"]
        for o in occ:
            self.assertNotIn("\n", o["context"])

    def test_tier_lookup_and_sampling(self):
        data = {"bases": {"そうして": {"tier": "block"}, "かける": {"tier": "verify"}}}
        self.assertEqual(clh.tier_of("そうして", data), "block")
        self.assertEqual(clh.tier_of("つける", data), "unscreened")
        occ = [clh.Occurrence(entry="1", field="f", base="a", target="t", surface="a", context="")
               for _ in range(10)] + [clh.Occurrence(entry="2", field="f", base="b", target="t", surface="b", context="")]
        sample = clh.sample_queue(occ, 3, 0)
        self.assertEqual(sorted(o["base"] for o in sample), ["a", "a", "a", "b"])
        self.assertEqual(clh.sample_queue(occ, 0, 0), occ)


class TestLedgerLogic(unittest.TestCase):
    def setUp(self):
        self.occ = clh.kana_link_occurrences(ENTRY)
        self.data = {"bases": {"そうして": {"tier": "block"}, "かける": {"tier": "verify"},
                               "つける": {"tier": "unique"}}}

    def test_gate_requires_keep_for_block_tier_links(self):
        self.assertEqual(clh.gate(self.occ, self.data, []), 1)
        keep = [{"entry": "16667", "base": "そうして", "target": "02943_soushite", "decision": "keep"}]
        self.assertEqual(clh.gate(self.occ, self.data, keep), 0)

    def test_gate_rejects_a_link_that_came_back_after_an_unlink(self):
        unlink = [{"entry": "16667_aashite", "base": "かける", "target": "00854_kakeru", "decision": "unlink"}]
        self.assertEqual(clh.gate(self.occ, {"bases": {}}, unlink), 1)
        # a later keep for the same key (another occurrence judged correct) clears it
        both = unlink + [{"entry": "16667", "base": "かける", "target": "00854_kakeru", "decision": "keep"}]
        self.assertEqual(clh.gate(self.occ, {"bases": {}}, both), 0)

    def test_retier_thresholds(self):
        decisions = (
            [{"entry": "1", "base": "そうして", "target": "t", "decision": "unlink"}] * 4
            + [{"entry": "2", "base": "かける", "target": "t", "decision": "keep"}] * 59
            + [{"entry": "3", "base": "かける", "target": "t", "decision": "unlink"}]
            + [{"entry": "4", "base": "つける", "target": "t", "decision": "keep"}] * 10
            + [{"entry": "5", "base": "ように", "target": "t", "decision": "keep"}] * 3
        )
        data = {"bases": {"そうして": {"tier": "verify"}, "かける": {"tier": "verify"},
                          "つける": {"tier": "unique"},
                          "ように": {"tier": "verify", "screen": {"verdict": "ambiguous"}}}}
        changes = {c[0]: c for c in clh.retier([], data, decisions)}
        self.assertEqual(changes["そうして"][1:3], ("verify", "block"))      # 4/4 wrong
        self.assertEqual(changes["かける"][1:3], ("verify", "verify"))      # 1/60 wrong: below the block rate
        self.assertEqual(changes["つける"][1:3], ("unique", "unique"))      # no wrong, screen unique: unchanged
        self.assertEqual(changes["ように"][1:3], ("verify", "verify"))      # ambiguous screen stays verify
        n = clh.apply_retier(data, changes.values(), "2026-09-08")
        self.assertEqual(n, 1)
        self.assertEqual(data["bases"]["そうして"]["tier"], "block")
        self.assertEqual(data["bases"]["かける"]["review"], {"reviewed": 60, "wrong": 1, "date": "2026-09-08"})

    def test_locked_tier_is_not_retiered(self):
        decisions = [{"entry": "1", "base": "そうして", "target": "t", "decision": "keep"}] * 5
        data = {"bases": {"そうして": {"tier": "block", "tier_locked": True}}}
        self.assertEqual(clh.retier([], data, decisions), [])

    def test_load_data_rejects_unknown_tiers(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "kana.json"
            path.write_text(json.dumps({"bases": {"x": {"tier": "maybe"}}}), encoding="utf-8")
            with self.assertRaises(SystemExit):
                clh.load_data(path)
            path.write_text(json.dumps({"bases": {"x": {"tier": "block"}}}), encoding="utf-8")
            self.assertEqual(clh.load_data(path)["bases"]["x"]["tier"], "block")
            self.assertEqual(clh.load_data(Path(tmp) / "missing.json"), {"bases": {}})


class TestRetarget(unittest.TestCase):
    def test_retarget_rewrites_the_link_and_counts_as_unlink_plus_keep(self):
        text = "⟦いけません→いける：06957_ikeru⟧。"
        new, n = rl.strip_link(text, "いけません", "いける", "06957_ikeru", "", "いけない", "02335_ikenai")
        self.assertEqual((new, n), ("⟦いけません→いけない：02335_ikenai⟧。", 1))
        idx = clh.decision_index([{"entry": "01227", "base": "いける", "target": "06957_ikeru",
                                   "decision": "retarget", "new_base": "いけない", "new_target": "02335_ikenai"}])
        self.assertEqual(idx[("01227", "いける", "06957_ikeru")], {"unlink"})
        self.assertEqual(idx[("01227", "いけない", "02335_ikenai")], {"keep"})


class TestFixer(unittest.TestCase):
    def test_strip_link_removes_only_the_matching_link(self):
        text = ENTRY["notes"]
        new, n = rl.strip_link(text, "そうして", "そうして", "02943_soushite")
        self.assertEqual(n, 2)
        self.assertNotIn("02943_soushite", new)
        self.assertIn("(like this), そうして (like that, near listener)", new)
        self.assertIn("⟦こうして→こうして：26873_koushite⟧", new)      # other links untouched
        # a different surface or target is left alone
        same, n0 = rl.strip_link(text, "そうし", "そうして", "02943_soushite")
        self.assertEqual((same, n0), (text, 0))
        same, n0 = rl.strip_link(text, "", "そうして", "99999_other")
        self.assertEqual((same, n0), (text, 0))
        # an empty surface matches any surface of that base and target
        _new, n_any = rl.strip_link(text, "", "そうして", "02943_soushite")
        self.assertEqual(n_any, 2)
        # a context pins one occurrence; it still matches after the other one is stripped
        ctx = "- 【そうして】: like that"
        one, n1 = rl.strip_link(text, "そうして", "そうして", "02943_soushite", ctx)
        self.assertEqual(n1, 1)
        self.assertIn("⟦そうして→そうして：02943_soushite⟧ (like that, near listener)", one)
        self.assertIn("\n- そうして: like that\n", one)
        again, n2 = rl.strip_link(one, "そうして", "そうして", "02943_soushite", ctx)
        self.assertEqual((again, n2), (one, 0))

    def test_apply_decisions_rewrites_the_entry_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "16500").mkdir()
            path = root / "16500" / "16667_aashite.json"
            path.write_text(json.dumps(ENTRY, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            ledger = root / "ledger.jsonl"
            ledger.write_text(json.dumps({"entry": "16667", "field": "notes", "surface": "そうして",
                                          "base": "そうして", "target": "02943_soushite",
                                          "decision": "unlink"}) + "\n", encoding="utf-8")
            rc = rl.main(["--apply-decisions", "--no-relink", "--entries-dir", str(root),
                          "--decisions", str(ledger), "--data", str(root / "none.json")])
            self.assertEqual(rc, 0)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertNotIn("02943_soushite", saved["notes"])
            self.assertIn("⟦こうして→こうして：26873_koushite⟧", saved["notes"])
            self.assertEqual(saved["examples"][1]["japanese"], ENTRY["examples"][1]["japanese"])
            self.assertNotEqual(saved.get("metadata", {}).get("modified"), None)
            # idempotent: nothing left to remove
            rc = rl.main(["--apply-decisions", "--no-relink", "--entries-dir", str(root),
                          "--decisions", str(ledger), "--data", str(root / "none.json")])
            self.assertEqual(rc, 0)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["notes"], saved["notes"])


class TestResponseParsing(unittest.TestCase):
    def _resp(self, content):
        return {"choices": [{"message": {"content": content}}]}

    def test_complete_array(self):
        got = rl.parse_list(self._resp('[{"n": 1, "verdict": "entry"}, {"n": 2, "verdict": "other"}]'))
        self.assertEqual([o["n"] for o in got], [1, 2])

    def test_truncated_array_salvages_complete_objects(self):
        text = '```json\n[{"n": 1, "verdict": "entry", "note": "ok"}, {"n": 2, "verdict": "other", "competitors": ["欠ける (chip)"], "note": "cut of'
        got = rl.parse_list(self._resp(text))
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0]["n"], 1)

    def test_prose_only_is_none(self):
        self.assertIsNone(rl.parse_list(self._resp("**Evaluating Word Links** I am assessing...")))
        self.assertIsNone(rl.parse_list(None))
        self.assertIsNone(rl.parse_list({"choices": [{"message": {"content": ""}}]}))


class TestFlagPruning(unittest.TestCase):
    def test_flags_with_a_decision_are_dropped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            flags = root / "flags.jsonl"
            ledger = root / "ledger.jsonl"
            flags.write_text(
                json.dumps({"entry": "16667", "base": "そうして", "target": "02943_soushite", "verdict": "other"}) + "\n"
                + json.dumps({"entry": "00014", "base": "ように", "target": "10081_youni", "verdict": "unsure"}) + "\n",
                encoding="utf-8")
            ledger.write_text(json.dumps({"entry": "16667", "base": "そうして", "target": "02943_soushite",
                                          "decision": "unlink"}) + "\n", encoding="utf-8")
            self.assertEqual(rl.prune_flags(ledger, flags), 1)
            left = [json.loads(l) for l in flags.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([f["base"] for f in left], ["ように"])
            self.assertEqual(rl.prune_flags(ledger, flags), 0)
            self.assertEqual(rl.prune_flags(ledger, root / "missing.jsonl"), 0)


if __name__ == "__main__":
    unittest.main()
