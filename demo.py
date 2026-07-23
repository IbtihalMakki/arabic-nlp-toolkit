from arabic_nlp_toolkit import preprocess

text = """
السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ 😊

زر موقعنا:
https://example.com

#الذكاء_الاصطناعي
"""

print(preprocess(text))