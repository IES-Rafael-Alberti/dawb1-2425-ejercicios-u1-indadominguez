# ejercicio 20

n_º_telefono = input("Introduce un número de teléfono en el formato +34-número-extensión: ")

if n_º_telefono.startswith("+34-") and n_º_telefono.count('-') == 2:

    no_prefijo = n_º_telefono.split('-')
    
    numero = no_prefijo[1]
    print("Número de teléfono:", numero)
else:
    print("El formato del número de teléfono no es válido.")
