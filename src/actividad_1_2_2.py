def leer_numeros():
    total = 0
    contador = 0

    while True:
        entrada = input("Introduce un número (o 'fin' para terminar): ")

        if entrada.lower() == "fin":
            break

        try:
            numero = float(entrada)  
            total += numero
            contador += 1
        except ValueError:
            print("Por favor, introduce un número válido o 'fin' para terminar.")

    return total, contador

def calcular_media(total, contador):
    if contador == 0:
        return 0 
    return total / contador 

def main():
    total, contador = leer_numeros()
    media = calcular_media(total, contador)

    print(f"Total: {total}")
    print(f"Cantidad de números: {contador}")
    print(f"Media: {media}")


if __name__ == "__main__":
    main()