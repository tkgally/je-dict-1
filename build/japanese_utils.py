"""
Shared Japanese language utility functions for je-dict-1 build scripts.

This module consolidates duplicated hiragana/romaji conversion and
kana-to-folder mapping that were previously defined in multiple scripts.
"""

from typing import Optional


# Mapping from hiragana to romaji
HIRAGANA_TO_ROMAJI = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n',
    # Small kana
    'ゃ': 'ya', 'ゅ': 'yu', 'ょ': 'yo',
    'っ': '',  # Handled specially in hiragana_to_romaji
    'ー': '',  # Long vowel mark - context dependent
}

# Combination mappings (e.g., きゃ -> kya)
COMBO_MAPPINGS = {
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    # Loanword combinations with small vowels (ぁぃぅぇぉ)
    # Used for foreign sounds not native to Japanese
    'てぃ': 'ti', 'でぃ': 'di',
    'とぅ': 'tu', 'どぅ': 'du',
    'ふぁ': 'fa', 'ふぃ': 'fi', 'ふぇ': 'fe', 'ふぉ': 'fo',
    'うぃ': 'wi', 'うぇ': 'we', 'うぉ': 'wo',
    'ゔぁ': 'va', 'ゔぃ': 'vi', 'ゔ': 'vu', 'ゔぇ': 've', 'ゔぉ': 'vo',
    'つぁ': 'tsa', 'つぃ': 'tsi', 'つぇ': 'tse', 'つぉ': 'tso',
    'ちぇ': 'che', 'しぇ': 'she', 'じぇ': 'je',
    'てゅ': 'tyu', 'でゅ': 'dyu',
}

# Kana row definitions for navigation and folder organization
KANA_ROWS = [
    {'name': 'あ行', 'kana': 'あいうえお', 'key': 'あ', 'folder': 'a'},
    {'name': 'か行', 'kana': 'かきくけこがぎぐげご', 'key': 'か', 'folder': 'ka'},
    {'name': 'さ行', 'kana': 'さしすせそざじずぜぞ', 'key': 'さ', 'folder': 'sa'},
    {'name': 'た行', 'kana': 'たちつてとだぢづでど', 'key': 'た', 'folder': 'ta'},
    {'name': 'な行', 'kana': 'なにぬねの', 'key': 'な', 'folder': 'na'},
    {'name': 'は行', 'kana': 'はひふへほばびぶべぼぱぴぷぺぽ', 'key': 'は', 'folder': 'ha'},
    {'name': 'ま行', 'kana': 'まみむめも', 'key': 'ま', 'folder': 'ma'},
    {'name': 'や行', 'kana': 'やゆよ', 'key': 'や', 'folder': 'ya'},
    {'name': 'ら行', 'kana': 'らりるれろ', 'key': 'ら', 'folder': 'ra'},
    {'name': 'わ行', 'kana': 'わをん', 'key': 'わ', 'folder': 'wa'},
]

# Mapping from first kana to folder (generated from KANA_ROWS)
KANA_TO_FOLDER = {}
for _row in KANA_ROWS:
    for _kana in _row['kana']:
        KANA_TO_FOLDER[_kana] = _row['folder']

# Alias for backwards compatibility with validate.py
KANA_TO_DIRECTORY = KANA_TO_FOLDER


def hiragana_to_romaji(reading: str) -> str:
    """
    Convert hiragana reading to romaji.

    Handles:
    - Basic hiragana characters
    - Two-character combinations (きゃ, しゃ, etc.)
    - Small tsu (っ) gemination (doubles following consonant)
    - Long vowel mark (ー)

    Args:
        reading: Hiragana string to convert

    Returns:
        Romaji representation of the hiragana

    Examples:
        >>> hiragana_to_romaji('たべる')
        'taberu'
        >>> hiragana_to_romaji('がっこう')
        'gakkou'
        >>> hiragana_to_romaji('きょう')
        'kyou'
    """
    result = []
    i = 0
    while i < len(reading):
        # Check for two-character combinations first
        if i + 1 < len(reading):
            combo = reading[i:i+2]
            if combo in COMBO_MAPPINGS:
                result.append(COMBO_MAPPINGS[combo])
                i += 2
                continue

        char = reading[i]

        # Handle small tsu (gemination)
        if char == 'っ':
            # Double the next consonant
            if i + 1 < len(reading):
                next_char = reading[i + 1]
                if next_char in HIRAGANA_TO_ROMAJI:
                    next_romaji = HIRAGANA_TO_ROMAJI[next_char]
                    if next_romaji:
                        result.append(next_romaji[0])
            i += 1
            continue

        # Handle long vowel mark
        if char == 'ー':
            if result:
                # Repeat the previous vowel
                prev = result[-1]
                if prev and prev[-1] in 'aiueo':
                    result.append(prev[-1])
            i += 1
            continue

        if char in HIRAGANA_TO_ROMAJI:
            result.append(HIRAGANA_TO_ROMAJI[char])
        else:
            # Unknown character, keep as is
            result.append(char)
        i += 1

    return ''.join(result)


def romaji_to_hiragana(romaji: str) -> str:
    """
    Convert romaji to hiragana.

    This handles common patterns including:
    - Basic syllables (ka, ki, ku, etc.)
    - Combination syllables (sha, cha, nya, etc.)
    - Double consonants (kk, ss, tt, etc.) -> っ
    - Single vowels (a, i, u, e, o)

    Note: This is a simplified conversion and may not handle all edge cases.

    Args:
        romaji: Romaji string to convert

    Returns:
        Hiragana representation of the romaji

    Examples:
        >>> romaji_to_hiragana('taberu')
        'たべる'
        >>> romaji_to_hiragana('gakkou')
        'がっこう'
    """
    # Order matters: longer patterns must come before shorter ones
    conversions = [
        # Three-character combinations first
        ('shi', 'し'), ('chi', 'ち'), ('tsu', 'つ'),
        ('sha', 'しゃ'), ('shu', 'しゅ'), ('sho', 'しょ'),
        ('cha', 'ちゃ'), ('chu', 'ちゅ'), ('cho', 'ちょ'),
        ('nya', 'にゃ'), ('nyu', 'にゅ'), ('nyo', 'にょ'),
        ('hya', 'ひゃ'), ('hyu', 'ひゅ'), ('hyo', 'ひょ'),
        ('mya', 'みゃ'), ('myu', 'みゅ'), ('myo', 'みょ'),
        ('rya', 'りゃ'), ('ryu', 'りゅ'), ('ryo', 'りょ'),
        ('kya', 'きゃ'), ('kyu', 'きゅ'), ('kyo', 'きょ'),
        ('gya', 'ぎゃ'), ('gyu', 'ぎゅ'), ('gyo', 'ぎょ'),
        ('bya', 'びゃ'), ('byu', 'びゅ'), ('byo', 'びょ'),
        ('pya', 'ぴゃ'), ('pyu', 'ぴゅ'), ('pyo', 'ぴょ'),
        ('ja', 'じゃ'), ('ju', 'じゅ'), ('jo', 'じょ'),
        # Basic syllables (two-character)
        ('ka', 'か'), ('ki', 'き'), ('ku', 'く'), ('ke', 'け'), ('ko', 'こ'),
        ('sa', 'さ'), ('su', 'す'), ('se', 'せ'), ('so', 'そ'),
        ('ta', 'た'), ('te', 'て'), ('to', 'と'),
        ('na', 'な'), ('ni', 'に'), ('nu', 'ぬ'), ('ne', 'ね'), ('no', 'の'),
        ('ha', 'は'), ('hi', 'ひ'), ('fu', 'ふ'), ('he', 'へ'), ('ho', 'ほ'),
        ('ma', 'ま'), ('mi', 'み'), ('mu', 'む'), ('me', 'め'), ('mo', 'も'),
        ('ya', 'や'), ('yu', 'ゆ'), ('yo', 'よ'),
        ('ra', 'ら'), ('ri', 'り'), ('ru', 'る'), ('re', 'れ'), ('ro', 'ろ'),
        ('wa', 'わ'), ('wo', 'を'),
        ('ga', 'が'), ('gi', 'ぎ'), ('gu', 'ぐ'), ('ge', 'げ'), ('go', 'ご'),
        ('za', 'ざ'), ('ji', 'じ'), ('zu', 'ず'), ('ze', 'ぜ'), ('zo', 'ぞ'),
        ('da', 'だ'), ('di', 'ぢ'), ('du', 'づ'), ('de', 'で'), ('do', 'ど'),
        ('ba', 'ば'), ('bi', 'び'), ('bu', 'ぶ'), ('be', 'べ'), ('bo', 'ぼ'),
        ('pa', 'ぱ'), ('pi', 'ぴ'), ('pu', 'ぷ'), ('pe', 'ぺ'), ('po', 'ぽ'),
        # Single vowels (must come after longer patterns)
        ('a', 'あ'), ('i', 'い'), ('u', 'う'), ('e', 'え'), ('o', 'お'),
        ('n', 'ん'),
    ]

    result = romaji.lower()

    # Handle double consonants first (gemination)
    # These need special handling to avoid leaving trailing consonants
    import re
    result = re.sub(r'([kstpgzdbj])\1', r'っ\1', result)

    # Apply conversions
    for rom, hira in conversions:
        result = result.replace(rom, hira)

    return result


def get_kana_folder(reading: str) -> str:
    """
    Get the folder name for a reading based on its first character.

    Args:
        reading: Hiragana reading

    Returns:
        Folder name (e.g., 'a', 'ka', 'sa', etc.)

    Examples:
        >>> get_kana_folder('たべる')
        'ta'
        >>> get_kana_folder('あう')
        'a'
    """
    if not reading:
        return 'a'
    first_char = reading[0]
    return KANA_TO_FOLDER.get(first_char, 'a')


def get_expected_directory(reading: str) -> Optional[str]:
    """
    Get the expected directory for an entry based on its reading.

    This is an alias for get_kana_folder that returns None for empty readings.

    Args:
        reading: Hiragana reading

    Returns:
        Directory name or None if reading is empty
    """
    if not reading:
        return None
    first_kana = reading[0]
    return KANA_TO_DIRECTORY.get(first_kana)
