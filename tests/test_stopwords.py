from arabic_nlp_toolkit import remove_stopwords


def test_remove_stopwords():
    text = "أنا أحب تعلم الذكاء الاصطناعي في الجامعة"

    assert remove_stopwords(text) == [
        "أحب",
        "تعلم",
        "الذكاء",
        "الاصطناعي",
        "الجامعة",
    ]


def test_no_stopwords():
    text = "ذكاء اصطناعي رائع"

    assert remove_stopwords(text) == [
        "ذكاء",
        "اصطناعي",
        "رائع",
    ]