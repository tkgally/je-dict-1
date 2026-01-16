"""
Shared constants for je-dict-1 build scripts.

This module centralizes definitions that were previously duplicated across
multiple files (schema.json, validate.py, build_flat.py).
"""

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
]

# Display labels for cross-reference types (used in HTML generation)
CROSS_REF_LABELS = {
    'pair': 'Pair verb',
    'synonym': 'Synonym',
    'antonym': 'Antonym',
    'keigo': 'Keigo',
    'related': 'Related',
    'see_also': 'See also',
    'contrast': 'Contrast',
}


def get_cross_ref_label(ref_type: str) -> str:
    """Get display label for cross-reference type.

    Args:
        ref_type: Cross-reference type string

    Returns:
        Human-readable label for the type
    """
    return CROSS_REF_LABELS.get(ref_type, 'Related')
