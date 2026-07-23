"""
Text similarity utilities.
"""

from .tokenization import tokenize


def jaccard_similarity(text1: str, text2: str) -> float:
    """
    Compute the Jaccard similarity between two texts.

    Returns:
        float: Similarity score between 0.0 and 1.0
    """

    tokens1 = set(tokenize(text1))
    tokens2 = set(tokenize(text2))

    if not tokens1 and not tokens2:
        return 1.0

    intersection = len(tokens1 & tokens2)
    union = len(tokens1 | tokens2)

    return intersection / union