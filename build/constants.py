"""
Shared constants for je-dict-1 build scripts.

This module centralizes definitions that were previously duplicated across
multiple files (schema.json, validate.py, build_flat.py).
"""

# Number of entries per directory
# Entries are organized in directories of this size:
# 00000/ contains entries 00001-00499
# 00500/ contains entries 00500-00999
# etc.
ENTRIES_PER_DIRECTORY = 500

# Valid cross-reference types
# IMPORTANT: When updating this list, also update build/schema.json
# which cannot import Python constants directly.
CROSS_REF_TYPES = [
    'pair',
    'synonym',
    'antonym',
    'keigo',
    'related',
    'see_also',
    'contrast',
    'homophone',
]

# Display labels for cross-reference types (used in HTML generation)
CROSS_REF_LABELS = {
    'pair': 'Pair verb',
    'synonym': 'Synonym',
    'antonym': 'Antonym',
    'keigo': 'Keigo',
    'related': 'Related',
    'see_also': 'See also',
    'contrast': 'Compare',
    'homophone': 'Homophone',
}


# Cross-reference link delimiters for inline word links
# These Unicode characters are selected to avoid conflicts with JSON, HTML, and furigana notation
LINK_OPEN = '⟦'      # U+27E6 Mathematical left white square bracket
LINK_CLOSE = '⟧'     # U+27E7 Mathematical right white square bracket
LINK_ARROW = '→'     # U+2192 Rightwards arrow
LINK_COLON = '：'    # U+FF1A Fullwidth colon
NOENTRY = 'noentry'  # Marker for words without dictionary entries


def get_cross_ref_label(ref_type: str) -> str:
    """Get display label for cross-reference type.

    Args:
        ref_type: Cross-reference type string

    Returns:
        Human-readable label for the type
    """
    return CROSS_REF_LABELS.get(ref_type, 'Related')
