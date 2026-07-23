"""
Arabic n-gram utilities.
"""

from .tokenization import tokenize


def ngrams(text: str, n: int = 2):
    """
    Generate n-grams from Arabic text.
    """

    if n <= 0:
        raise ValueError("n must be greater than zero")

    tokens = tokenize(text)

    return [
        tuple(tokens[i:i + n])
        for i in range(len(tokens) - n + 1)
    ]