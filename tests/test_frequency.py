from arabinlp import word_frequency


def test_word_frequency():
    text = "الذكاء الذكاء الاصطناعي رائع"

    assert word_frequency(text) == {
        "الذكاء": 2,
        "الاصطناعي": 1,
        "رائع": 1,
    }


def test_empty_text():
    assert word_frequency("") == {}


def test_numbers():
    text = "1 1 2 3"

    assert word_frequency(text) == {
        "1": 2,
        "2": 1,
        "3": 1,
    }