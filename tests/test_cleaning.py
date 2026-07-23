from arabic_nlp_toolkit.cleaning import (
    remove_urls,
    remove_mentions,
    remove_hashtags,
    remove_extra_spaces,
    remove_diacritics,
    remove_emojis,
    remove_tatweel,
)


def test_remove_urls():
    text = "Visit https://example.com"
    assert remove_urls(text) == "Visit "


def test_remove_mentions():
    text = "@ibtihal hello"
    assert remove_mentions(text) == " hello"


def test_remove_hashtags():
    text = "#AI is awesome"
    assert remove_hashtags(text) == "AI is awesome"


def test_remove_extra_spaces():
    text = "Hello     World"
    assert remove_extra_spaces(text) == "Hello World"


def test_remove_diacritics():
    text = "السَّلَامُ عَلَيْكُمْ"
    assert remove_diacritics(text) == "السلام عليكم"


def test_remove_emojis():
    text = "Hello 😊"
    assert remove_emojis(text) == "Hello "

def test_remove_tatweel():
    text = "الســــلام"
    assert remove_tatweel(text) == "السلام"