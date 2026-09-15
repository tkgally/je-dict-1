"""Unit tests for the pure merge policies in pipeline/absorb_branch.py.

The git-driven parts (fetch, merge, checkout) are exercised by using the tool
on a real branch; these tests pin the file-level policies that decide what an
absorbed branch contributes: ledger unions, metrics ordering, candidate-queue
reconciliation, PROJECT_STATUS.md section insertion, and session-log renaming.

Run with:  python3 -m unittest build.tests.test_absorb_branch
"""
import json
import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
if str(_ROOT / "pipeline") not in sys.path:
    sys.path.insert(0, str(_ROOT / "pipeline"))

import absorb_branch as ab  # noqa: E402


class UnionLinesTests(unittest.TestCase):
    def test_appends_only_the_lines_the_branch_added(self):
        base = "a\nb\n"
        ours = "a\nb\nc\n"          # main appended c after the branch diverged
        theirs = "a\nb\nx\ny\n"     # the branch appended x and y
        self.assertEqual(ab.union_lines(base, ours, theirs), "a\nb\nc\nx\ny\n")

    def test_no_change_when_ours_already_has_the_lines(self):
        base = "a\n"
        ours = "a\nx\n"
        theirs = "a\nx\n"
        self.assertEqual(ab.union_lines(base, ours, theirs), ours)

    def test_new_file_on_branch_is_taken_whole(self):
        self.assertEqual(ab.union_lines(None, "", "p\nq\n"), "p\nq\n")

    def test_block_with_blank_lines_is_kept_as_a_block(self):
        base = "# Log\n\n## 1\n- a\n"
        ours = "# Log\n\n## 1\n- a\n\n## 2\n- b\n"
        theirs = "# Log\n\n## 1\n- a\n\n## X\n- x\n- y\n"
        self.assertEqual(ab.union_lines(base, ours, theirs),
                         "# Log\n\n## 1\n- a\n\n## 2\n- b\n\n## X\n- x\n- y\n")


class SortMetricsTests(unittest.TestCase):
    def test_orders_rows_by_timestamp(self):
        rows = [{"ts": "2026-09-15T12:00:00Z", "mode": "polish"},
                {"ts": "2026-09-14T08:00:00Z", "mode": "new-entries"}]
        text = "\n".join(json.dumps(r) for r in rows) + "\n"
        out = [json.loads(ln)["ts"] for ln in ab.sort_metrics(text).splitlines()]
        self.assertEqual(out, ["2026-09-14T08:00:00Z", "2026-09-15T12:00:00Z"])

    def test_leaves_unparseable_text_alone(self):
        self.assertEqual(ab.sort_metrics("not json\n"), "not json\n")


def _cands(*items):
    return json.dumps({"metadata": {"next_id": 100, "total_candidates": len(items)},
                       "candidates": [{"id": f"C{i:05d}", "word": w, "reading": r, "notes": ""}
                                      for i, (w, r) in enumerate(items, start=1)]})


class ReconcileCandidatesTests(unittest.TestCase):
    def test_consumed_are_removed_and_added_are_returned(self):
        base = _cands(("蟹", "かに"), ("藤", "ふじ"))
        ours = _cands(("蟹", "かに"), ("藤", "ふじ"), ("松", "まつ"))     # main queued 松 since
        theirs = _cands(("藤", "ふじ"), ("能楽堂", "のうがくどう"))       # branch used 蟹, queued 能楽堂
        data, removed, to_add = ab.reconcile_candidates(base, ours, theirs)
        self.assertEqual([c["word"] for c in removed], ["蟹"])
        self.assertEqual([c["word"] for c in data["candidates"]], ["藤", "松"])
        self.assertEqual([c["word"] for c in to_add], ["能楽堂"])
        self.assertEqual(data["metadata"]["total_candidates"], 2)

    def test_branch_addition_already_on_main_is_not_re_added(self):
        base = _cands()
        ours = _cands(("能楽堂", "のうがくどう"))
        theirs = _cands(("能楽堂", "のうがくどう"))
        _data, removed, to_add = ab.reconcile_candidates(base, ours, theirs)
        self.assertEqual(removed, [])
        self.assertEqual(to_add, [])


STATUS_HEAD = "# Status\n\n## Current State\n\nfine\n\n## Recent Changes\n"
STATUS_TAIL = "\n## Older\n\nend\n"


def _status(*sections):
    body = "".join(f"\n### {d} ({t})\n\n{t} body\n" for d, t in sections)
    return STATUS_HEAD + body + STATUS_TAIL


class MergeStatusTests(unittest.TestCase):
    def test_inserts_new_section_in_date_order_after_same_date(self):
        base = _status(("2026-09-12", "old"))
        ours = _status(("2026-09-14", "main-run"), ("2026-09-12", "old"))
        theirs = _status(("2026-09-14", "branch-run"), ("2026-09-12", "old"))
        merged, new = ab.merge_status(base, ours, theirs)
        self.assertEqual(new, ["### 2026-09-14 (branch-run)"])
        heads = [ln for ln in merged.splitlines() if ln.startswith("### ")]
        self.assertEqual(heads, ["### 2026-09-14 (main-run)", "### 2026-09-14 (branch-run)",
                                 "### 2026-09-12 (old)"])
        self.assertTrue(merged.endswith("\n## Older\n\nend\n"))

    def test_keeps_at_most_five_sections(self):
        secs = [(f"2026-09-{d:02d}", f"s{d}") for d in range(10, 4, -1)]  # six sections
        ours = _status(*secs[1:])
        theirs = _status(secs[0], *secs[1:])
        merged, new = ab.merge_status(_status(*secs[1:]), ours, theirs)
        self.assertEqual(new, ["### 2026-09-10 (s10)"])
        self.assertEqual(sum(ln.startswith("### ") for ln in merged.splitlines()), 5)

    def test_nothing_new_returns_ours_unchanged(self):
        ours = _status(("2026-09-14", "a"))
        merged, new = ab.merge_status(ours, ours, ours)
        self.assertEqual(new, [])
        self.assertEqual(merged, ours)


class NextFreeLogTests(unittest.TestCase):
    def test_skips_numbers_taken_in_this_run(self):
        taken = {"polishing/sessions/routine_2099-01-01_001.md"}
        self.assertEqual(ab.next_free_log("2099-01-01", taken),
                         "polishing/sessions/routine_2099-01-01_002.md")


class IsGeneratedTests(unittest.TestCase):
    def test_prefixes_and_exact_names(self):
        self.assertTrue(ab.is_generated("kanji/00010_dai.json"))
        self.assertTrue(ab.is_generated("entries_index.json"))
        self.assertFalse(ab.is_generated("entries/00000/00021_bunpu.json"))
        self.assertFalse(ab.is_generated("reviews/decisions.jsonl"))


if __name__ == "__main__":
    unittest.main()
