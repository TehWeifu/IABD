from collections import defaultdict

input = " hola munod \n\r soy yo"

# Datos de entrada fragmentados

input_data1 = "hola mundo"
input_data2 = "soy yo"

# nodo 1
mapped_data = defaultdict(int)
for char in input_data1:
    if char.isalpha():
        char = char.lower()
    mapped_data[char] += 1

# nodo 2
mapped_data2 = defaultdict(int)
for char in input_data2:
    if char.isalpha():
        char = char.lower()
    mapped_data2[char] += 1

mapped_data.update(mapped_data2)

# fase de reducción
reduce_data = defaultdict(int)
for char, count in mapped_data.items():
    reduce_data[char] += count
