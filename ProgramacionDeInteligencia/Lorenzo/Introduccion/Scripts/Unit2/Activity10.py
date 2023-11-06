client = {
    "first_name": "Juan",
    "last_name": "Pérez García",
    "phone": {
        "cell": 654789658,
        "home": 963789654,
    },
    "address": {
        "type": "street",
        "number": 45,
        "door": 7
    },
    "invoices": {
        "purchases": ["234/2020", "345/2021", "675/2021", "561/2022"],
        "sales": ["456/2020", "564/2021", "768/2021", "345/2022"]
    }
}

print("Cliente", "Importante" if len(client["invoices"]["purchases"]) > 5 else "Normal")

client_relevance = "Cliente poco importante"
if len(client["invoices"]["purchases"]) > 5:
    client_relevance = "Cliente Importante"
elif len(client["invoices"]["purchases"]) > 1:
    client_relevance = "Cliente Normal"
print(client_relevance)

print()

print("Numbers from 0 to 999:", *range(0, 1_000))
print("Numbers from 1 to 1000:", *range(1, 1_001))

print()

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for key, value in enumerate(prime_numbers):
    display_cardinality = str(key + 1) + 'º'

    if key == 0:
        display_cardinality = "primer"

    if key == len(prime_numbers) - 1:
        display_cardinality = "último"

    print(f"El {display_cardinality} número primo es {value}")
