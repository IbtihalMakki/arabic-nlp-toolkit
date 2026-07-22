from arabic_nlp_toolkit.preprocessing import preprocess

text = """
أهلاً وسهلاً 😊

زوروا موقعي:
https://example.com

#ذكاء_اصطناعي
"""

print(preprocess(text))