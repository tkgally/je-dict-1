"""A later `keep` line in reviews/link_decisions.jsonl reverses an earlier `unlink`."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import auto_link  # noqa: E402
import check_link_homophones as clh  # noqa: E402


def _rec(decision, entry="05436", base="形", target="30925_kei"):
    return {"entry": entry, "field": "notes", "base": base, "target": target, "decision": decision}


class SupersedeTest(unittest.TestCase):
    def test_later_keep_drops_unlink(self):
        out = clh.superseded_removed([_rec("unlink"), _rec("keep")])
        self.assertEqual([r["decision"] for r in out], ["keep"])

    def test_earlier_keep_does_not(self):
        out = clh.superseded_removed([_rec("keep"), _rec("unlink")])
        self.assertEqual([r["decision"] for r in out], ["keep", "unlink"])

    def test_other_target_does_not(self):
        out = clh.superseded_removed([_rec("unlink"), _rec("keep", target="99999_x")])
        self.assertEqual(len(out), 2)

    def test_load_unlink_decisions_honours_later_keep(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "d.jsonl"
            lines = [_rec("unlink"), _rec("keep"),
                     _rec("unlink", entry="05509", base="時", target="09869_ji"),
                     _rec("unlink", entry="05509", base="時", target="02918_toki"),
                     _rec("keep", entry="05509", base="時", target="09869_ji")]
            path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in lines), encoding="utf-8")
            got = auto_link.load_unlink_decisions(path)
            self.assertNotIn("05436", got)
            self.assertEqual(got["05509"], frozenset({"時"}))


if __name__ == "__main__":
    unittest.main()
