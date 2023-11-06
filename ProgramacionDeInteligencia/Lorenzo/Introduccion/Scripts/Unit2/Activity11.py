def final_import(product_price, discount_percent):
    return product_price * (1 - discount_percent / 100)


print("Un producto a 120$ y 10% de descuento ahora vale: ", final_import(120, 10), '$', sep='')
print("Un producto a 120$ y 10% de descuento ahora vale: ", final_import(discount_percent=10, product_price=120), '$',
      sep='')

print()


def final_import_and_discount(product_price, discount_percent):
    import_discounted = product_price * (discount_percent / 100)
    import_final = product_price - import_discounted

    return import_final, import_discounted


cost, discount = final_import_and_discount(120, 10)
print(f"Un producto a 120$ y 10% de descuento ahora vale: ",
      cost, '$',
      ", se ha ahorrado ", discount, '$',
      sep='')

print()


def final_import_and_discount(product_price, discount_percent=10):
    import_discounted = product_price * (discount_percent / 100)
    import_final = product_price - import_discounted

    return import_final, import_discounted


cost, discount = final_import_and_discount(120)
print(f"Un producto a 120$ y 10% (valor por defecto) de descuento ahora vale: ",
      cost, '$',
      ", se ha ahorrado ", discount, '$',
      sep='')
