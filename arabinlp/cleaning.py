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

def remove_diacritics(text: str) -> str:
    """
    Remove Arabic diacritics.
    """

    arabic_diacritics = re.compile(r"""
         ّ    | # Shadda
         َ    | # Fatha
         ً    | # Tanwin Fath
         ُ    | # Damma
         ٌ    | # Tanwin Damm
         ِ    | # Kasra
         ٍ    | # Tanwin Kasr
         ْ    | # Sukun
         ـ      # Tatweel
    """, re.VERBOSE)

    return re.sub(arabic_diacritics, "", text)

def remove_emojis(text: str) -> str:
    """
    Remove emojis from text.
    """
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub("", text)

def remove_tatweel(text: str) -> str:
    """
    Remove Arabic Tatweel character.
    """
    return text.replace("ـ", "")