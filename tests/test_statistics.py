from arabic_nlp_toolkit import text_statistics


def test_statistics():
    text = "السلام عليكم. كيف حالك؟"

    stats = text_statistics(text)

    assert stats["words"] == 4
    assert stats["sentences"] == 2
    assert stats["unique_words"] == 4


def test_empty_text():
    stats = text_statistics("")

    assert stats["words"] == 0
    assert stats["sentences"] == 0
    assert stats["unique_words"] == 0


def test_duplicate_words():
    stats = text_statistics("مرحبا مرحبا مرحبا")

    assert stats["words"] == 3
    assert stats["unique_words"] == 1