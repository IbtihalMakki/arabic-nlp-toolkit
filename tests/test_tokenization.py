from arabic_nlp_toolkit import tokenize


def test_simple_sentence():
    text = "السلام عليكم ورحمة الله"
    assert tokenize(text) == [
        "السلام",
        "عليكم",
        "ورحمة",
        "الله",
    ]


def test_with_punctuation():
    text = "مرحباً، كيف حالك؟"
    assert tokenize(text) == [
        "مرحباً",
        "كيف",
        "حالك",
    ]


def test_with_numbers():
    text = "لدي 3 كتب في 2026"
    assert tokenize(text) == [
        "لدي",
        "3",
        "كتب",
        "في",
        "2026",
    ]