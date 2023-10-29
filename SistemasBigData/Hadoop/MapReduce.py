from collections import defaultdict
import re

input_text = """hola mundo
soy yo"""

result_words = {}

for letter in re.split(r"\s+", input_text):
    if letter in result_words:
        result_words[letter] = result_words[letter] + 1
    else:
        result_words[letter] = 1

result_words = dict(sorted(result_words.items()))
sorted(result_words)
print("Resultado por palabra de MapReduce:")
for word in result_words:
    print(f"Palabra: {word}, Frecuencia: {result_words[word]}")

print()
print()

result_letters = {}

for letter in input_text:
    if letter.isspace():
        continue

    if letter in result_letters:
        result_letters[letter] = result_letters[letter] + 1
    else:
        result_letters[letter] = 1

result_letters = dict(sorted(result_letters.items()))
print("Resultado por letra de MapReduce:")
for word in result_letters:
    print(f"Letra: {word}, Frecuencia: {result_letters[word]}")
