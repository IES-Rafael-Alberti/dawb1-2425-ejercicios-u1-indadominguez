# ejercicio 26

productos_compra = input("Introduce los productos de tu lista de la compra, por favor con comas: ")

productos_compra = productos_compra.replace('.', ',')

productos = productos_compra.split(",")

print("Los productos de la cesta son:")
for producto in productos:

    print(producto.strip())