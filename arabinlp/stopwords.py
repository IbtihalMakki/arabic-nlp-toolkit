"""
Arabic stopwords utilities.
"""

from pathlib import Path

from .tokenization import tokenize


RESOURCE_PATH = Path(__file__).parent / "resources" / "stopwords.txt"


def load_stopwords():
    """
    Load stopwords from the resources folder.
    """
    with open(RESOURCE_PATH, encoding="utf-8") as f:
        return {
            line.strip()
            for line in f
            if line.strip()
        }


STOPWORDS = load_stopwords()


def remove_stopwords(text: str):
    """
    Remove Arabic stopwords from text.
    """

    tokens = tokenize(text)

    return [
        token
        for token in tokens
        if token not in STOPWORDS
    ]