"""
Arabic text normalization utilities.
"""

import re


def normalize_arabic(text: str) -> str:
    """
    Normalize common Arabic characters.
    """

    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ي", text)
    text = re.sub("ة", "ه", text)

    return text