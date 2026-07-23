"""
Language detection utilities.
"""

import re


ARABIC_PATTERN = re.compile(r"[\u0600-\u06FF]")
ENGLISH_PATTERN = re.compile(r"[A-Za-z]")


def detect_language(text: str):
    """
    Detect whether text is Arabic, English, Mixed, or Unknown.
    """

    has_arabic = bool(ARABIC_PATTERN.search(text))
    has_english = bool(ENGLISH_PATTERN.search(text))

    if has_arabic and has_english:
        return "mixed"

    if has_arabic:
        return "arabic"

    if has_english:
        return "english"

    return "unknown"