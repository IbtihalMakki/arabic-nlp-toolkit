# Arabic NLP Toolkit

A lightweight and easy-to-use Python library for Arabic text preprocessing and normalization.

## Features

- Remove URLs
- Remove Mentions (@username)
- Remove Hashtags (#)
- Remove Extra Spaces
- Remove Arabic Diacritics (Tashkeel)
- Remove Emojis
- Remove Tatweel (ـ)
- Normalize Arabic Characters

---

## Installation

```bash
pip install arabic-nlp-toolkit
```

> **Note:** The package is currently under development and will be published to PyPI soon.

---

## Quick Start

```python
from arabic_nlp_toolkit import preprocess

text = """
السَّلَامُ عَلَيْكُمْ 😊

زوروا:
https://example.com

#الذكاء_الاصطناعي
"""

print(preprocess(text))
```

### Output

```text
السلام عليكم زوروا: الذكاء_الاصطناعي
```

---

## Available Functions

```python
from arabic_nlp_toolkit import (
    preprocess,
    normalize_arabic,
    remove_urls,
    remove_mentions,
    remove_hashtags,
    remove_extra_spaces,
    remove_diacritics,
    remove_emojis,
    remove_tatweel,
)
```

---

## Project Structure

```
arabic-nlp-toolkit/
│
├── arabic_nlp_toolkit/
│   ├── cleaning.py
│   ├── normalization.py
│   ├── preprocessing.py
│   └── __init__.py
│
├── tests/
├── demo.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Roadmap

### Version 0.2

- ✅ Remove URLs
- ✅ Remove Mentions
- ✅ Remove Hashtags
- ✅ Remove Diacritics
- ✅ Remove Emojis
- ✅ Remove Tatweel
- ✅ Unit Tests

### Version 0.3

- Arabic Tokenization
- Stopwords Removal
- Punctuation Removal
- Number Normalization

### Version 0.4

- Stemming
- Lemmatization
- Buckwalter Transliteration

### Version 1.0

- PyPI Release
- GitHub Actions
- Full Documentation
- API Reference

---

## Running Tests

```bash
pytest
```

---

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

---

## License

MIT License