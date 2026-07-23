"""
Arabic word frequency utilities.
"""

from collections import Counter

from .tokenization import tokenize


def word_frequency(text: str):
    """
    Count word frequencies in Arabic text.
    """

    tokens = tokenize(text)

    return dict(Counter(tokens))