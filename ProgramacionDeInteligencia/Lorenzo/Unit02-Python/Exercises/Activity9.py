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

print("The name is:", client["first_name"])
print("The cellphone number is:", client["phone"]["cell"])
print("The type of the address is:", client["address"]["type"])
print("The number of the third invoice sold is:", client["invoices"]["sales"][2])
print("The total count of purchases made is:", len(client["invoices"]["purchases"]))
print("The name of the keys of first level are:", *[key for key in client], sep=', ')
