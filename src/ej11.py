# ejercicio 11

n = int(input("Introduce un entero positivo: "))

if n > 0:
    suma = sum(range(1, n + 1))

    print(f"La suma de  todos los numeros enteros desde 1 hasta {n} es: {suma}")

else:
    print("Por favor,introduzca un entero positivo. ")