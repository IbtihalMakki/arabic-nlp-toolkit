from arabinlp import tokenize

print(tokenize.__module__)
print(tokenize.__code__.co_filename)

print(tokenize("مرحباً، كيف حالك؟"))