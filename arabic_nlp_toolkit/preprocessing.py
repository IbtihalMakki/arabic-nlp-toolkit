"""
Main preprocessing pipeline for Arabic NLP.
"""

from .cleaning import (
    remove_urls,
    remove_mentions,
    remove_hashtags,
    remove_extra_spaces,
)

from .normalization import normalize_arabic


def preprocess(text: str) -> str:
    """
    Apply the full preprocessing pipeline.
    """

    text = remove_urls(text)
    text = remove_mentions(text)
    text = remove_hashtags(text)
    text = normalize_arabic(text)
    text = remove_extra_spaces(text)

    return text