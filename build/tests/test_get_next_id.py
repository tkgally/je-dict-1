"""Unit tests for the directory hints in build/get_next_id.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from get_next_id import boundary_lines, entry_directory
from path_utils import get_directory_range


class TestEntryDirectory(unittest.TestCase):
    def test_rounds_down(self):
        self.assertEqual(entry_directory(30495), 'entries/30000/')
        self.assertEqual(entry_directory(30500), 'entries/30500/')
        self.assertEqual(entry_directory(1), 'entries/00000/')

    def test_matches_path_utils(self):
        for n in (1, 499, 500, 999, 30495, 30499, 30500, 33167):
            self.assertEqual(entry_directory(n), f"entries/{get_directory_range(f'{n:05d}_x')}/")


class TestBoundaryLines(unittest.TestCase):
    def test_single_id_mid_block(self):
        self.assertEqual(boundary_lines(33168), ['Directory: entries/33000/'])

    def test_first_id_of_block(self):
        lines = boundary_lines(33500)
        self.assertEqual(lines[0], 'Directory: entries/33500/')
        self.assertIn('first ID of a new directory', lines[1])

    def test_batch_crossing_boundary(self):
        lines = boundary_lines(30495, 10)
        self.assertEqual(lines[0], 'Directory: entries/30000/')
        self.assertTrue(any('WARNING' in l and '30500 onward in entries/30500/' in l for l in lines))

    def test_batch_ending_just_before_boundary(self):
        self.assertFalse(any('WARNING' in l for l in boundary_lines(30490, 10)))


if __name__ == '__main__':
    unittest.main()
