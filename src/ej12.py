# ejercicio 12

altura = float(input("Introduce tu altura en metros: "))

peso = float(input("Introduce tu peso en kilogramos: "))


indice_masa_corporal = (peso / (altura ** 2))

print(f"Tu índice de masa corporal es: {indice_masa_corporal:.2f}")