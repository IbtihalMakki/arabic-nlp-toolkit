"""
Text cleaning utilities for Arabic NLP.
"""

import re


def remove_urls(text: str) -> str:
    """
    Remove URLs from text.
    """
    return re.sub(r"https?://\S+|www\.\S+", "", text)


def remove_mentions(text: str) -> str:
    """
    Remove @mentions from text.
    """
    return re.sub(r"@\w+", "", text)


def remove_hashtags(text: str) -> str:
    """
    Remove hashtag symbols while keeping the word.
    """
    return re.sub(r"#", "", text)


def remove_extra_spaces(text: str) -> str:
    """
    Remove repeated spaces.
    """
    return re.sub(r"\s+", " ", text).strip()