"""Unit tests for build/path_utils.py."""

import sys
import os
import unittest
from pathlib import Path, PurePosixPath

# Add build directory to path so we can import path_utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from path_utils import get_numeric_id, get_directory_range, get_entry_path, get_entry_prefix


# ── get_numeric_id ────────────────────────────────────────────────

class TestGetNumericId(unittest.TestCase):
    """Tests for get_numeric_id()."""

    def test_docstring_example_matsu(self):
        assert get_numeric_id('00003_matsu') == 3

    def test_docstring_example_inzei(self):
        assert get_numeric_id('06512_inzei') == 6512

    def test_single_digit(self):
        assert get_numeric_id('00001_a') == 1

    def test_zero_padded(self):
        assert get_numeric_id('00042_neko') == 42

    def test_large_id(self):
        assert get_numeric_id('99999_test') == 99999

    def test_id_500(self):
        assert get_numeric_id('00500_taberu') == 500

    def test_id_999(self):
        assert get_numeric_id('00999_foo') == 999

    def test_id_1000(self):
        assert get_numeric_id('01000_bar') == 1000

    def test_id_with_underscores_in_romaji(self):
        """Entry IDs with multiple underscores should still parse the numeric prefix."""
        assert get_numeric_id('01234_some_word') == 1234

    def test_non_numeric_prefix_returns_zero(self):
        """If the prefix is not numeric, return 0."""
        assert get_numeric_id('abc_word') == 0

    def test_empty_string_returns_zero(self):
        assert get_numeric_id('') == 0

    def test_no_underscore_numeric_only(self):
        """A bare number with no underscore should still parse."""
        assert get_numeric_id('00750') == 750

    def test_zero_id(self):
        assert get_numeric_id('00000_test') == 0


# ── get_directory_range ───────────────────────────────────────────

class TestGetDirectoryRange(unittest.TestCase):
    """Tests for get_directory_range()."""

    def test_docstring_example_low(self):
        assert get_directory_range('00003_matsu') == '00000'

    def test_docstring_example_500(self):
        assert get_directory_range('00500_taberu') == '00500'

    def test_docstring_example_6512(self):
        assert get_directory_range('06512_inzei') == '06500'

    def test_boundary_id_0(self):
        """ID 0 maps to 00000/."""
        assert get_directory_range('00000_test') == '00000'

    def test_boundary_id_1(self):
        assert get_directory_range('00001_ichi') == '00000'

    def test_boundary_id_499(self):
        """Last entry in the 00000 range."""
        assert get_directory_range('00499_last') == '00000'

    def test_boundary_id_500(self):
        """First entry in the 00500 range."""
        assert get_directory_range('00500_first') == '00500'

    def test_boundary_id_999(self):
        """Last entry in the 00500 range."""
        assert get_directory_range('00999_last') == '00500'

    def test_boundary_id_1000(self):
        """First entry in the 01000 range."""
        assert get_directory_range('01000_sengo') == '01000'

    def test_boundary_id_1499(self):
        assert get_directory_range('01499_end') == '01000'

    def test_boundary_id_1500(self):
        assert get_directory_range('01500_start') == '01500'

    def test_high_id(self):
        assert get_directory_range('10000_test') == '10000'

    def test_high_id_mid_range(self):
        assert get_directory_range('10250_mid') == '10000'

    def test_five_digit_format(self):
        """Directory name should always be zero-padded to 5 digits."""
        result = get_directory_range('00003_matsu')
        assert len(result) == 5
        assert result == '00000'

    def test_format_for_large_id(self):
        """Even large IDs should produce 5-digit strings."""
        result = get_directory_range('99999_big')
        assert len(result) == 5
        assert result == '99500'

    def test_non_numeric_returns_00000(self):
        """Invalid entry IDs (numeric part = 0) should map to 00000."""
        assert get_directory_range('abc_word') == '00000'


# ── get_entry_path ────────────────────────────────────────────────

class TestGetEntryPath(unittest.TestCase):
    """Tests for get_entry_path()."""

    def test_docstring_example(self):
        result = get_entry_path(Path('entries'), '00003_matsu')
        assert result == Path('entries/00000/00003_matsu.json')

    def test_returns_path_object(self):
        result = get_entry_path(Path('entries'), '00003_matsu')
        assert isinstance(result, Path)

    def test_json_extension(self):
        result = get_entry_path(Path('entries'), '01234_neko')
        assert result.suffix == '.json'

    def test_correct_directory_for_500_range(self):
        result = get_entry_path(Path('entries'), '00500_taberu')
        assert result == Path('entries/00500/00500_taberu.json')

    def test_correct_directory_for_1000_range(self):
        result = get_entry_path(Path('entries'), '01000_sengo')
        assert result == Path('entries/01000/01000_sengo.json')

    def test_correct_directory_for_mid_range(self):
        result = get_entry_path(Path('entries'), '06512_inzei')
        assert result == Path('entries/06500/06512_inzei.json')

    def test_absolute_entries_dir(self):
        result = get_entry_path(Path('/home/user/je-dict-1/entries'), '00003_matsu')
        assert result == Path('/home/user/je-dict-1/entries/00000/00003_matsu.json')

    def test_filename_matches_entry_id(self):
        entry_id = '02345_example'
        result = get_entry_path(Path('entries'), entry_id)
        assert result.stem == entry_id

    def test_parent_is_directory_range(self):
        result = get_entry_path(Path('entries'), '02345_example')
        assert result.parent.name == '02000'

    def test_grandparent_is_entries_dir(self):
        result = get_entry_path(Path('entries'), '02345_example')
        assert result.parent.parent == Path('entries')


# ── get_entry_prefix (legacy) ─────────────────────────────────────

class TestGetEntryPrefix(unittest.TestCase):
    """Tests for the deprecated get_entry_prefix() legacy function."""

    def test_delegates_to_get_directory_range(self):
        """get_entry_prefix should return the same result as get_directory_range."""
        test_ids = ['00003_matsu', '00500_taberu', '06512_inzei', '01000_bar']
        for entry_id in test_ids:
            assert get_entry_prefix(entry_id) == get_directory_range(entry_id)
