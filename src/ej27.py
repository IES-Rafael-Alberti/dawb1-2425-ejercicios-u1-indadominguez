# ejercicio 27

nombre_producto = input("Introduce el nombre del producto por favor: ")


precio_producto = input("Introduce el precio del producto por favor: ")
precio_producto = precio_producto.replace(',', '.')
precio = float(precio_producto)


unidades_medida= input("Por favor, introduce el número de unidades: ")
unidades = int(unidades_medida)


coste_total = precio * unidades


print(f"{nombre_producto}: {precio:6.2f} € por unidad, {unidades:3d} unidades, coste total: {coste_total:8.2f} €")