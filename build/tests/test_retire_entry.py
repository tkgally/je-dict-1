"""Tests for build/retire_entry.py (retire and rename keep old URLs working)."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import retire_entry  # noqa: E402


def _entry(eid, headword, examples=(), notes="", refs=()):
    return {
        "id": eid, "headword": headword, "reading": "x",
        "examples": [{"id": f"{eid}_ex{i + 1}", "japanese": j} for i, j in enumerate(examples)],
        "notes": notes, "cross_references": list(refs),
    }


class RetireEntryTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.saved = {k: getattr(retire_entry, k) for k in
                      ("ROOT", "ENTRIES", "ARTICLES", "RETIRED", "MANIFEST", "LINK_DECISIONS")}
        retire_entry.ROOT = root
        retire_entry.ENTRIES = root / "entries"
        retire_entry.ARTICLES = root / "articles"
        retire_entry.RETIRED = root / "build" / "data" / "retired_entries.json"
        retire_entry.MANIFEST = root / "audio" / "manifest"
        retire_entry.LINK_DECISIONS = root / "reviews" / "link_decisions.jsonl"
        for d in ("entries/08500", "entries/02500", "entries/28000", "articles", "build/data",
                  "audio/manifest", "reviews"):
            (root / d).mkdir(parents=True, exist_ok=True)
        self.write("08989_shaseki", _entry("08989_shaseki", "{車席|しゃせき}"))
        self.write("02832_zaseki", _entry(
            "02832_zaseki", "{座席|ざせき}",
            examples=["⟦{車席|しゃせき}→車席：08989_shaseki⟧に座る。"],
            refs=[{"type": "contrast", "target_id": "08989_shaseki", "reading": "しゃせき"}]))
        self.write("28415_inushu", _entry("28415_inushu", "{犬種|いぬしゅ}", examples=["a", "b"]))
        self.write("28416_other", _entry(
            "28416_other", "x", notes="⟦{犬種|けんしゅ}→犬種：28415_inushu⟧",
            refs=[{"type": "related", "target_id": "28415_inushu", "reading": "けんしゅ"}]))
        (root / "audio/manifest/28000.jsonl").write_text(
            json.dumps({"ex": "28415_inushu_ex1", "h": "abc"}) + "\n", encoding="utf-8")
        (root / "reviews/link_decisions.jsonl").write_text(
            json.dumps({"base": "犬種", "target": "28415_inushu", "decision": "keep"}) + "\n",
            encoding="utf-8")
        (root / "articles/a.json").write_text(json.dumps({
            "id": "a", "body": "⟦{車席|しゃせき}→車席：08989_shaseki⟧",
            "related_entries": [{"entry_id": "08989_shaseki"}, {"entry_id": "02832_zaseki"}]}),
            encoding="utf-8")

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(retire_entry, k, v)
        self.tmp.cleanup()

    def write(self, eid, data):
        retire_entry.write_json(retire_entry.entry_path(eid), data)

    def read(self, eid):
        return json.loads(retire_entry.entry_path(eid).read_text(encoding="utf-8"))

    def test_retire_moves_links_drops_crossrefs_and_records(self):
        rc = retire_entry.cmd_retire(SimpleNamespace(
            old="08989_shaseki", to="02832_zaseki", reason="r", save=None, dry_run=False,
            duplicate=False))
        self.assertEqual(rc, 0)
        self.assertFalse(retire_entry.entry_path("08989_shaseki").exists())
        zaseki = self.read("02832_zaseki")
        self.assertIn("：02832_zaseki⟧", zaseki["examples"][0]["japanese"])
        self.assertEqual(zaseki["cross_references"], [])
        article = json.loads((retire_entry.ARTICLES / "a.json").read_text(encoding="utf-8"))
        self.assertIn("：02832_zaseki⟧", article["body"])
        self.assertEqual(article["related_entries"], [{"entry_id": "02832_zaseki"}])
        retired = retire_entry.load_retired()
        self.assertEqual(retired["08989_shaseki"]["to"], "02832_zaseki")
        self.assertEqual(retired["08989_shaseki"]["kind"], "retired")

    def test_rename_keeps_number_and_renames_example_and_audio_ids(self):
        rc = retire_entry.cmd_rename(SimpleNamespace(
            old="28415_inushu", new="28415_kenshu", reason="r", dry_run=False))
        self.assertEqual(rc, 0)
        self.assertFalse(retire_entry.entry_path("28415_inushu").exists())
        new = self.read("28415_kenshu")
        self.assertEqual(new["id"], "28415_kenshu")
        self.assertEqual([e["id"] for e in new["examples"]], ["28415_kenshu_ex1", "28415_kenshu_ex2"])
        other = self.read("28416_other")
        self.assertIn("：28415_kenshu⟧", other["notes"])
        self.assertEqual(other["cross_references"][0]["target_id"], "28415_kenshu")
        manifest = (retire_entry.MANIFEST / "28000.jsonl").read_text(encoding="utf-8")
        self.assertIn("28415_kenshu_ex1", manifest)
        decisions = retire_entry.LINK_DECISIONS.read_text(encoding="utf-8")
        self.assertIn('"target": "28415_kenshu"', decisions)
        self.assertEqual(retire_entry.load_retired()["28415_inushu"]["kind"], "renamed")

    def test_rename_refuses_a_different_number(self):
        rc = retire_entry.cmd_rename(SimpleNamespace(
            old="28415_inushu", new="28416_kenshu", reason="r", dry_run=False))
        self.assertEqual(rc, 1)
        self.assertTrue(retire_entry.entry_path("28415_inushu").exists())

    def test_chains_resolve_to_the_live_entry(self):
        retire_entry.cmd_rename(SimpleNamespace(
            old="28415_inushu", new="28415_kenshu", reason="r", dry_run=False))
        retire_entry.cmd_retire(SimpleNamespace(
            old="28415_kenshu", to="02832_zaseki", reason="r", save=None, dry_run=False,
            duplicate=False))
        retired = retire_entry.load_retired()
        self.assertEqual(retire_entry.resolve(retired, "28415_inushu"), "02832_zaseki")

    def test_duplicate_repoints_crossrefs(self):
        self.write("28417_dup", _entry("28417_dup", "{犬種|けんしゅ}"))
        rc = retire_entry.cmd_retire(SimpleNamespace(
            old="28415_inushu", to="28417_dup", reason="r", save=None, dry_run=False, duplicate=True))
        self.assertEqual(rc, 0)
        ref = self.read("28416_other")["cross_references"][0]
        self.assertEqual(ref["target_id"], "28417_dup")
        self.assertEqual(ref["headword"], "{犬種|けんしゅ}")

    def test_dry_run_changes_nothing(self):
        retire_entry.cmd_retire(SimpleNamespace(
            old="08989_shaseki", to="02832_zaseki", reason="r", save=None, dry_run=True,
            duplicate=False))
        self.assertTrue(retire_entry.entry_path("08989_shaseki").exists())
        self.assertIn("08989_shaseki", json.dumps(self.read("02832_zaseki")))
        self.assertEqual(retire_entry.load_retired(), {})


if __name__ == "__main__":
    unittest.main()
