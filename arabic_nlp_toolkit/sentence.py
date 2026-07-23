"""
Arabic sentence splitting utilities.
"""

import re


SENTENCE_PATTERN = re.compile(
    r"(?<=[.!?؟])\s+"
)


def split_sentences(text: str):
    """
    Split text into sentences while preserving sentence-ending punctuation.
    """

    sentences = [
        sentence.strip()
        for sentence in SENTENCE_PATTERN.split(text)
        if sentence.strip()
    ]

    return sentences