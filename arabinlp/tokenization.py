"""
Arabic tokenization utilities.
"""

import re

TOKEN_PATTERN = re.compile(
    r"[A-Za-z0-9\u0621-\u063A\u0641-\u064A\u064B-\u0652]+",
    re.UNICODE,
)


def tokenize(text: str):
    """
    Tokenize Arabic text while preserving Arabic diacritics
    and removing punctuation.
    """
    return TOKEN_PATTERN.findall(text)