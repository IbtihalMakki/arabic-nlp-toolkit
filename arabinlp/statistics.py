"""
Text statistics utilities.
"""

from .tokenization import tokenize
from .sentence import split_sentences


def text_statistics(text: str):
    """
    Compute basic statistics for a text.
    """

    tokens = tokenize(text)
    sentences = split_sentences(text)

    return {
        "characters": len(text),
        "characters_without_spaces": len(
            text.replace(" ", "")
        ),
        "words": len(tokens),
        "unique_words": len(set(tokens)),
        "sentences": len(sentences),
    }