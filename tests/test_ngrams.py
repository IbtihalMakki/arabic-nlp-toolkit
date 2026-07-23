from arabic_nlp_toolkit import ngrams

import pytest


def test_bigrams():
    text = "السلام عليكم ورحمة الله"

    assert ngrams(text, 2) == [
        ("السلام", "عليكم"),
        ("عليكم", "ورحمة"),
        ("ورحمة", "الله"),
    ]


def test_trigrams():
    text = "السلام عليكم ورحمة الله"

    assert ngrams(text, 3) == [
        ("السلام", "عليكم", "ورحمة"),
        ("عليكم", "ورحمة", "الله"),
    ]


def test_large_n():
    assert ngrams("مرحبا", 2) == []


def test_invalid_n():
    with pytest.raises(ValueError):
        ngrams("مرحبا", 0)