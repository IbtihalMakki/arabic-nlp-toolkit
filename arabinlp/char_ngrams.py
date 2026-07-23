"""
Character n-gram utilities.
"""


def character_ngrams(text: str, n: int = 3):
    """
    Generate character n-grams from text.
    """

    if n <= 0:
        raise ValueError("n must be greater than zero")

    if len(text) < n:
        return []

    return [
        text[i:i + n]
        for i in range(len(text) - n + 1)
    ]