# Arabic NLP Toolkit

A lightweight, modular, and easy-to-use Python library for Arabic Natural Language Processing (NLP).

The toolkit provides common Arabic text preprocessing utilities including cleaning, normalization, tokenization, stopword removal, sentence segmentation, keyword extraction, similarity measurement, and more.

---

## Features

### Text Cleaning

- Remove URLs
- Remove Mentions (@username)
- Remove Hashtags (#hashtag)
- Remove Emojis
- Remove Arabic Diacritics (Tashkeel)
- Remove Tatweel (ـ)
- Remove Extra Spaces

### Arabic NLP

- Arabic Text Normalization
- Arabic Tokenization
- Arabic Stopword Removal
- Sentence Splitting
- Word Frequency Analysis
- Word N-Grams
- Character N-Grams
- Keyword Extraction
- Language Detection
- Text Statistics
- Jaccard Text Similarity

---

## Installation

```bash
pip install arabic-nlp-toolkit
```

> **Note**
>
> The package is currently under active development.

---

# Quick Start

```python
from arabic_nlp_toolkit import preprocess

text = """
السَّلَامُ عَلَيْكُمْ 😊

زوروا موقعنا:
https://example.com

#الذكاء_الاصطناعي
"""

print(preprocess(text))
```

Output

```text
السلام عليكم زوروا موقعنا: الذكاء_الاصطناعي
```

---

# API Overview

```python
from arabic_nlp_toolkit import (
    preprocess,
    normalize_arabic,
    tokenize,
    remove_stopwords,
    split_sentences,
    word_frequency,
    ngrams,
    character_ngrams,
    detect_language,
    text_statistics,
    extract_keywords,
    jaccard_similarity,
)
```

---

# Examples

## Tokenization

```python
from arabic_nlp_toolkit import tokenize

tokenize("السلام عليكم ورحمة الله")
```

Output

```python
['السلام', 'عليكم', 'ورحمة', 'الله']
```

---

## Stopword Removal

```python
from arabic_nlp_toolkit import remove_stopwords

remove_stopwords("أنا أحب تعلم الذكاء الاصطناعي")
```

Output

```python
['أحب', 'تعلم', 'الذكاء', 'الاصطناعي']
```

---

## Sentence Splitting

```python
from arabic_nlp_toolkit import split_sentences

split_sentences(
    "السلام عليكم. كيف حالك؟ أنا بخير!"
)
```

Output

```python
[
    'السلام عليكم.',
    'كيف حالك؟',
    'أنا بخير!'
]
```

---

## Word Frequency

```python
from arabic_nlp_toolkit import word_frequency

word_frequency(
    "الذكاء الذكاء الاصطناعي رائع"
)
```

Output

```python
{
    'الذكاء': 2,
    'الاصطناعي': 1,
    'رائع': 1
}
```

---

## Word N-Grams

```python
from arabic_nlp_toolkit import ngrams

ngrams(
    "السلام عليكم ورحمة الله",
    n=2
)
```

Output

```python
[
    ('السلام', 'عليكم'),
    ('عليكم', 'ورحمة'),
    ('ورحمة', 'الله')
]
```

---

## Character N-Grams

```python
from arabic_nlp_toolkit import character_ngrams

character_ngrams(
    "السلام",
    n=3
)
```

Output

```python
[
    'الس',
    'لسل',
    'سلا',
    'لام'
]
```

---

## Language Detection

```python
from arabic_nlp_toolkit import detect_language

detect_language("Hello مرحبا")
```

Output

```python
mixed
```

---

## Text Statistics

```python
from arabic_nlp_toolkit import text_statistics

text_statistics(
    "السلام عليكم. كيف حالك؟"
)
```

Output

```python
{
    'characters': 24,
    'characters_without_spaces': 20,
    'words': 4,
    'unique_words': 4,
    'sentences': 2
}
```

---

## Keyword Extraction

```python
from arabic_nlp_toolkit import extract_keywords

extract_keywords(
    "الذكاء الاصطناعي رائع. الذكاء يتطور بسرعة."
)
```

Output

```python
[
    'الذكاء',
    'الاصطناعي',
    'رائع'
]
```

---

## Text Similarity

```python
from arabic_nlp_toolkit import jaccard_similarity

score = jaccard_similarity(
    "أنا أحب الذكاء الاصطناعي",
    "الذكاء الاصطناعي رائع"
)

print(score)
```

Output

```text
0.4
```

---

# Project Structure

```
arabic-nlp-toolkit/

├── arabic_nlp_toolkit/
├── tests/
├── .github/
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

# Running Tests

```bash
python -m pytest
```

Current Status

```
40 tests passed
```

---

# Roadmap

## Version 1.1

- Arabic Light Stemmer
- Root Extraction
- TF-IDF
- BM25 Ranking
- Arabic Spell Checker
- Named Entity Recognition (NER)
- AraBERT Integration

---

# Contributing

Contributions, bug reports, feature requests, and pull requests are always welcome.

If you have ideas for improving Arabic NLP support, feel free to open an Issue.

---

# License

This project is licensed under the MIT License.

---

# Author

**Ibtihal Makki**

AI Engineer • NLP Researcher • Generative AI