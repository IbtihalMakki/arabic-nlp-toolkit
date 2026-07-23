import pytest

from arabinlp import character_ngrams


def test_trigrams():
    assert character_ngrams("السلام", 3) == [
        "الس",
        "لسل",
        "سلا",
        "لام",
    ]


def test_bigrams():
    assert character_ngrams("سلام", 2) == [
        "سل",
        "لا",
        "ام",
    ]


def test_large_n():
    assert character_ngrams("سلام", 10) == []


def test_invalid_n():
    with pytest.raises(ValueError):
        character_ngrams("سلام", 0)