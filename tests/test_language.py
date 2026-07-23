from arabinlp import detect_language


def test_arabic():
    assert detect_language("السلام عليكم") == "arabic"


def test_english():
    assert detect_language("Hello world") == "english"


def test_mixed():
    assert detect_language("Hello مرحبا") == "mixed"


def test_unknown():
    assert detect_language("12345 !@#$") == "unknown"