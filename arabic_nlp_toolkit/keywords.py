"""
Keyword extraction utilities.
"""

from collections import Counter

from .stopwords import remove_stopwords


def extract_keywords(text: str, top_k: int = 5):
    """
    Extract the most frequent keywords after removing stopwords.
    """

    tokens = remove_stopwords(text)

    counts = Counter(tokens)

    return [
        word
        for word, _ in counts.most_common(top_k)
    ]