# ejercicio 24

precio_consola = input("Introduce el precio del producto en euros (con dos decimales) por favor: ")
precio = float(precio_consola)

euros = int(precio)  
centimos = int((precio - euros) * 100)  

print(f"El precio introducido es: {euros} euros y {centimos} céntimos.")
