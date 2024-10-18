# num aleatorio entre dos valores

import random


limite_inferior = float(input("Introduce el límite inferior: "))


limite_superior = float(input("Introduce el límite superior: "))


numero_aleatorio = random.uniform(limite_inferior, limite_superior)


print(f"Número aleatorio generado entre {limite_inferior} y {limite_superior}: {numero_aleatorio:.2f}")
