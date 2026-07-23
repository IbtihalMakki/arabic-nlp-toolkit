from arabinlp import split_sentences


def test_simple_sentences():
    text = "السلام عليكم. كيف حالك؟ أنا بخير!"

    assert split_sentences(text) == [
        "السلام عليكم.",
        "كيف حالك؟",
        "أنا بخير!",
    ]


def test_single_sentence():
    text = "أهلاً وسهلاً"

    assert split_sentences(text) == [
        "أهلاً وسهلاً",
    ]


def test_empty_text():
    assert split_sentences("") == []