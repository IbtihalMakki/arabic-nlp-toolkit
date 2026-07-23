from arabinlp import extract_keywords


def test_keywords():
    text = """
    أنا أحب الذكاء الاصطناعي.
    الذكاء الاصطناعي رائع.
    الذكاء يتطور بسرعة.
    """

    assert extract_keywords(text, top_k=2) == [
        "الذكاء",
        "الاصطناعي",
    ]


def test_empty_text():
    assert extract_keywords("") == []


def test_top_k():
    text = "أ ب ج د"

    assert len(extract_keywords(text, top_k=2)) == 2