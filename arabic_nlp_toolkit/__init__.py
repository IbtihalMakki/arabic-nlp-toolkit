from .preprocessing import preprocess
from .normalization import normalize_arabic
from .tokenization import tokenize
from .stopwords import remove_stopwords
from .sentence import split_sentences
from .frequency import word_frequency
from .ngrams import ngrams
from .language import detect_language
from .statistics import text_statistics
from .keywords import extract_keywords
from .similarity import jaccard_similarity
from .char_ngrams import character_ngrams

from .cleaning import (
    remove_urls,
    remove_mentions,
    remove_hashtags,
    remove_extra_spaces,
    remove_diacritics,
    remove_tatweel,
    remove_emojis,
)