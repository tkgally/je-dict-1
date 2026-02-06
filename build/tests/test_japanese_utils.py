"""Unit tests for build/japanese_utils.py."""

import sys
import os
import re

import pytest

# Add build directory to path so we can import japanese_utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from japanese_utils import (
    hiragana_to_romaji,
    romaji_to_hiragana,
    romaji_to_katakana,
    strip_furigana,
    is_kanji,
    is_valid_hiragana,
    normalize_reading,
    contains_katakana,
    get_kana_folder,
    get_expected_directory,
    FURIGANA_PATTERN,
    KANA_TO_FOLDER,
    KANA_TO_DIRECTORY,
)


# ── hiragana_to_romaji ──────────────────────────────────────────────

class TestHiraganaToRomaji:
    """Tests for hiragana_to_romaji()."""

    def test_basic_syllables(self):
        assert hiragana_to_romaji('たべる') == 'taberu'

    def test_single_vowels(self):
        assert hiragana_to_romaji('あいうえお') == 'aiueo'

    def test_combo_characters(self):
        assert hiragana_to_romaji('きょう') == 'kyou'
        assert hiragana_to_romaji('しゃしん') == 'shashin'
        assert hiragana_to_romaji('ちゅうい') == 'chuui'

    def test_gemination_small_tsu(self):
        assert hiragana_to_romaji('がっこう') == 'gakkou'
        assert hiragana_to_romaji('きって') == 'kitte'
        assert hiragana_to_romaji('ざっし') == 'zasshi'
        assert hiragana_to_romaji('いっぱい') == 'ippai'

    def test_long_vowel_mark(self):
        # ー after a vowel repeats that vowel
        assert hiragana_to_romaji('らーめん') == 'raamen'

    def test_n_character(self):
        assert hiragana_to_romaji('ん') == 'n'
        assert hiragana_to_romaji('さんぽ') == 'sanpo'

    def test_dakuten_characters(self):
        assert hiragana_to_romaji('がぎぐげご') == 'gagigugego'
        assert hiragana_to_romaji('ばびぶべぼ') == 'babibubebo'

    def test_handakuten_characters(self):
        assert hiragana_to_romaji('ぱぴぷぺぽ') == 'papipupepo'

    def test_empty_string(self):
        assert hiragana_to_romaji('') == ''

    def test_combo_sha_shu_sho(self):
        assert hiragana_to_romaji('しゃ') == 'sha'
        assert hiragana_to_romaji('しゅ') == 'shu'
        assert hiragana_to_romaji('しょ') == 'sho'

    def test_combo_ja_ju_jo(self):
        assert hiragana_to_romaji('じゃ') == 'ja'
        assert hiragana_to_romaji('じゅ') == 'ju'
        assert hiragana_to_romaji('じょ') == 'jo'

    def test_combo_cha_chu_cho(self):
        assert hiragana_to_romaji('ちゃ') == 'cha'
        assert hiragana_to_romaji('ちゅ') == 'chu'
        assert hiragana_to_romaji('ちょ') == 'cho'

    def test_wa_wo(self):
        assert hiragana_to_romaji('わ') == 'wa'
        assert hiragana_to_romaji('を') == 'wo'

    def test_unknown_characters_kept(self):
        # Non-hiragana chars should be kept as-is
        assert hiragana_to_romaji('abc') == 'abc'

    def test_gemination_before_combo(self):
        # っち -> tchi (doubles the first consonant of 'chi')
        result = hiragana_to_romaji('まっち')
        assert result == 'macchi'

    def test_long_vowel_mark_at_start(self):
        # ー at start with no previous vowel - should not crash
        result = hiragana_to_romaji('ー')
        assert isinstance(result, str)

    def test_loanword_combos(self):
        assert hiragana_to_romaji('てぃ') == 'ti'
        assert hiragana_to_romaji('ふぁ') == 'fa'


# ── romaji_to_hiragana ──────────────────────────────────────────────

class TestRomajiToHiragana:
    """Tests for romaji_to_hiragana()."""

    def test_basic_conversion(self):
        assert romaji_to_hiragana('taberu') == 'たべる'

    def test_double_consonants(self):
        assert romaji_to_hiragana('gakkou') == 'がっこう'

    def test_single_vowels(self):
        assert romaji_to_hiragana('aiueo') == 'あいうえお'

    def test_combo_syllables(self):
        assert romaji_to_hiragana('sha') == 'しゃ'
        assert romaji_to_hiragana('cha') == 'ちゃ'
        assert romaji_to_hiragana('nya') == 'にゃ'

    def test_tsu(self):
        assert romaji_to_hiragana('tsu') == 'つ'

    def test_shi_chi(self):
        assert romaji_to_hiragana('shi') == 'し'
        assert romaji_to_hiragana('chi') == 'ち'

    def test_n_handling(self):
        assert romaji_to_hiragana('n') == 'ん'

    def test_case_insensitive(self):
        assert romaji_to_hiragana('TABERU') == 'たべる'

    def test_empty_string(self):
        assert romaji_to_hiragana('') == ''

    def test_double_t(self):
        assert romaji_to_hiragana('kitte') == 'きって'

    def test_double_p(self):
        assert romaji_to_hiragana('ippai') == 'いっぱい'

    def test_double_s(self):
        assert romaji_to_hiragana('zasshi') == 'ざっし'


# ── romaji_to_katakana ──────────────────────────────────────────────

class TestRomajiToKatakana:
    """Tests for romaji_to_katakana()."""

    def test_basic_conversion(self):
        assert romaji_to_katakana('kaku') == 'カク'

    def test_n_conversion(self):
        assert romaji_to_katakana('jin') == 'ジン'

    def test_empty_string(self):
        assert romaji_to_katakana('') == ''

    def test_none_string(self):
        assert romaji_to_katakana('none') == ''

    def test_double_consonant(self):
        result = romaji_to_katakana('kappa')
        assert 'ッ' in result

    def test_combo_syllables(self):
        assert romaji_to_katakana('sha') == 'シャ'
        assert romaji_to_katakana('chi') == 'チ'


# ── strip_furigana ──────────────────────────────────────────────────

class TestStripFurigana:
    """Tests for strip_furigana()."""

    def test_simple_furigana(self):
        assert strip_furigana('{漢字|かんじ}') == '漢字'

    def test_text_with_furigana(self):
        assert strip_furigana('{食|た}べる') == '食べる'

    def test_multiple_furigana(self):
        result = strip_furigana('{日本|にほん}の{文化|ぶんか}')
        assert result == '日本の文化'

    def test_no_furigana(self):
        assert strip_furigana('たべる') == 'たべる'

    def test_empty_string(self):
        assert strip_furigana('') == ''

    def test_none_returns_empty(self):
        assert strip_furigana(None) == ''

    def test_mixed_content(self):
        result = strip_furigana('I like {寿司|すし}.')
        assert result == 'I like 寿司.'


# ── FURIGANA_PATTERN ────────────────────────────────────────────────

class TestFuriganaPattern:
    """Tests for the FURIGANA_PATTERN regex constant."""

    def test_matches_basic_furigana(self):
        match = FURIGANA_PATTERN.search('{漢字|かんじ}')
        assert match is not None
        assert match.group(1) == '漢字'
        assert match.group(2) == 'かんじ'

    def test_finds_all_furigana(self):
        text = '{日本|にほん}の{文化|ぶんか}'
        matches = FURIGANA_PATTERN.findall(text)
        assert len(matches) == 2
        assert matches[0] == ('日本', 'にほん')
        assert matches[1] == ('文化', 'ぶんか')

    def test_no_match_plain_text(self):
        assert FURIGANA_PATTERN.search('plain text') is None

    def test_sub_replaces_with_kanji(self):
        result = FURIGANA_PATTERN.sub(r'\1', '{漢字|かんじ}')
        assert result == '漢字'


# ── is_kanji ────────────────────────────────────────────────────────

class TestIsKanji:
    """Tests for is_kanji()."""

    def test_common_kanji(self):
        assert is_kanji('漢') is True
        assert is_kanji('字') is True
        assert is_kanji('日') is True
        assert is_kanji('本') is True

    def test_hiragana_not_kanji(self):
        assert is_kanji('あ') is False
        assert is_kanji('ん') is False

    def test_katakana_not_kanji(self):
        assert is_kanji('ア') is False
        assert is_kanji('ン') is False

    def test_ascii_not_kanji(self):
        assert is_kanji('A') is False
        assert is_kanji('1') is False
        assert is_kanji('!') is False

    def test_cjk_extension_a(self):
        # U+3400 is the start of CJK Extension A
        assert is_kanji('\u3400') is True
        assert is_kanji('\u4DBF') is True

    def test_cjk_unified_range(self):
        # U+4E00 is the start of CJK Unified Ideographs
        assert is_kanji('\u4E00') is True
        # U+9FFF is the end
        assert is_kanji('\u9FFF') is True

    def test_cjk_compatibility(self):
        # U+F900 is the start of CJK Compatibility Ideographs
        assert is_kanji('\uF900') is True
        assert is_kanji('\uFAFF') is True

    def test_boundary_outside_ranges(self):
        # Just outside the ranges
        assert is_kanji('\u33FF') is False  # before CJK Extension A
        assert is_kanji('\uFB00') is False  # after CJK Compatibility

    def test_punctuation_not_kanji(self):
        assert is_kanji('。') is False
        assert is_kanji('、') is False


# ── is_valid_hiragana ───────────────────────────────────────────────

class TestIsValidHiragana:
    """Tests for is_valid_hiragana()."""

    def test_valid_hiragana(self):
        assert is_valid_hiragana('たべる') is True
        assert is_valid_hiragana('あいうえお') is True

    def test_katakana_fails(self):
        assert is_valid_hiragana('タベル') is False
        assert is_valid_hiragana('カタカナ') is False

    def test_romaji_fails(self):
        assert is_valid_hiragana('taberu') is False
        assert is_valid_hiragana('abc') is False

    def test_mixed_fails(self):
        assert is_valid_hiragana('たべるx') is False
        assert is_valid_hiragana('たべルる') is False

    def test_empty_string(self):
        assert is_valid_hiragana('') is False

    def test_long_vowel_mark_accepted(self):
        assert is_valid_hiragana('ー') is True
        assert is_valid_hiragana('らーめん') is True

    def test_iteration_marks_accepted(self):
        assert is_valid_hiragana('ゝ') is True
        assert is_valid_hiragana('ゞ') is True

    def test_kanji_fails(self):
        assert is_valid_hiragana('漢字') is False

    def test_numbers_fail(self):
        assert is_valid_hiragana('123') is False

    def test_small_kana_accepted(self):
        assert is_valid_hiragana('きゃ') is True
        assert is_valid_hiragana('しゅ') is True
        assert is_valid_hiragana('ちょ') is True


# ── normalize_reading ───────────────────────────────────────────────

class TestNormalizeReading:
    """Tests for normalize_reading()."""

    def test_katakana_to_hiragana(self):
        assert normalize_reading('カタカナ') == 'かたかな'

    def test_hiragana_unchanged(self):
        assert normalize_reading('ひらがな') == 'ひらがな'

    def test_mixed_katakana_hiragana(self):
        result = normalize_reading('カタかな')
        assert result == 'かたかな'

    def test_empty_string(self):
        assert normalize_reading('') == ''

    def test_ascii_unchanged(self):
        assert normalize_reading('abc') == 'abc'

    def test_all_katakana_range(self):
        # ア (U+30A2) -> あ (U+3042)
        assert normalize_reading('ア') == 'あ'
        # ン (U+30F3) -> ん (U+3093)
        assert normalize_reading('ン') == 'ん'

    def test_long_vowel_mark_unchanged(self):
        # ー (U+30FC) is outside the conversion range, should remain
        result = normalize_reading('ラーメン')
        assert result == 'らーめん'


# ── contains_katakana ───────────────────────────────────────────────

class TestContainsKatakana:
    """Tests for contains_katakana()."""

    def test_katakana_string(self):
        assert contains_katakana('カタカナ') is True

    def test_hiragana_only(self):
        assert contains_katakana('ひらがな') is False

    def test_mixed_content(self):
        assert contains_katakana('ひらカナ') is True

    def test_empty_string(self):
        assert contains_katakana('') is False

    def test_long_vowel_mark_excluded(self):
        # ー alone should NOT count as katakana
        assert contains_katakana('ー') is False
        assert contains_katakana('ひらがなー') is False

    def test_katakana_with_long_vowel(self):
        # Katakana + ー should still detect the katakana
        assert contains_katakana('ラーメン') is True

    def test_ascii_only(self):
        assert contains_katakana('abc') is False

    def test_kanji_only(self):
        assert contains_katakana('漢字') is False

    def test_single_katakana(self):
        assert contains_katakana('ア') is True


# ── get_kana_folder ─────────────────────────────────────────────────

class TestGetKanaFolder:
    """Tests for get_kana_folder()."""

    def test_a_row(self):
        assert get_kana_folder('あう') == 'a'
        assert get_kana_folder('いく') == 'a'
        assert get_kana_folder('うえ') == 'a'
        assert get_kana_folder('えき') == 'a'
        assert get_kana_folder('おく') == 'a'

    def test_ka_row(self):
        assert get_kana_folder('かく') == 'ka'
        assert get_kana_folder('がく') == 'ka'  # dakuten stays in ka row

    def test_sa_row(self):
        assert get_kana_folder('さく') == 'sa'
        assert get_kana_folder('ざんねん') == 'sa'

    def test_ta_row(self):
        assert get_kana_folder('たべる') == 'ta'
        assert get_kana_folder('だす') == 'ta'

    def test_na_row(self):
        assert get_kana_folder('なく') == 'na'

    def test_ha_row(self):
        assert get_kana_folder('はし') == 'ha'
        assert get_kana_folder('ばん') == 'ha'  # dakuten
        assert get_kana_folder('ぱん') == 'ha'  # handakuten

    def test_ma_row(self):
        assert get_kana_folder('まつ') == 'ma'

    def test_ya_row(self):
        assert get_kana_folder('やま') == 'ya'

    def test_ra_row(self):
        assert get_kana_folder('らく') == 'ra'

    def test_wa_row(self):
        assert get_kana_folder('わかる') == 'wa'
        assert get_kana_folder('を') == 'wa'
        assert get_kana_folder('ん') == 'wa'

    def test_empty_string(self):
        assert get_kana_folder('') == 'a'

    def test_unknown_first_char(self):
        # Non-kana character should fall back to 'a'
        assert get_kana_folder('x') == 'a'


# ── get_expected_directory ──────────────────────────────────────────

class TestGetExpectedDirectory:
    """Tests for get_expected_directory()."""

    def test_basic_readings(self):
        assert get_expected_directory('たべる') == 'ta'
        assert get_expected_directory('あう') == 'a'

    def test_empty_returns_none(self):
        assert get_expected_directory('') is None

    def test_unknown_char_returns_none(self):
        # Characters not in KANA_TO_DIRECTORY return None
        assert get_expected_directory('x') is None


# ── KANA_TO_FOLDER / KANA_TO_DIRECTORY ──────────────────────────────

class TestKanaConstants:
    """Tests for KANA_TO_FOLDER and KANA_TO_DIRECTORY mappings."""

    def test_kana_to_folder_covers_basic_kana(self):
        # Every basic hiragana should map to a folder
        basic = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'
        for char in basic:
            assert char in KANA_TO_FOLDER, f"'{char}' not in KANA_TO_FOLDER"

    def test_kana_to_directory_alias(self):
        # KANA_TO_DIRECTORY should be the same object as KANA_TO_FOLDER
        assert KANA_TO_DIRECTORY is KANA_TO_FOLDER

    def test_dakuten_covered(self):
        dakuten = 'がぎぐげござじずぜぞだぢづでどばびぶべぼ'
        for char in dakuten:
            assert char in KANA_TO_FOLDER, f"'{char}' not in KANA_TO_FOLDER"

    def test_handakuten_covered(self):
        handakuten = 'ぱぴぷぺぽ'
        for char in handakuten:
            assert char in KANA_TO_FOLDER, f"'{char}' not in KANA_TO_FOLDER"
