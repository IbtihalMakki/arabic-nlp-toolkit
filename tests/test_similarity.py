from arabic_nlp_toolkit import jaccard_similarity


def test_identical_text():
    assert jaccard_similarity(
        "السلام عليكم",
        "السلام عليكم",
    ) == 1.0


def test_partial_similarity():
    score = jaccard_similarity(
        "أنا أحب الذكاء الاصطناعي",
        "الذكاء الاصطناعي رائع",
    )

    assert round(score, 2) == 0.40


def test_no_similarity():
    assert jaccard_similarity(
        "سيارة",
        "حاسوب",
    ) == 0.0


def test_empty_text():
    assert jaccard_similarity("", "") == 1.0