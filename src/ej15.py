# ejercicio 15

cuenta_ahorros = float(input("Introduce la cantidad de dinero que tienes: "))

intereses = 0.04

ahorros_primer_año = cuenta_ahorros * (1 + intereses)
ahorros_segundo_año = ahorros_primer_año * (1 + intereses)
ahorros_tercer_año = ahorros_segundo_año * (1 + intereses)

print(f"Ahorros tras el primer año: {ahorros_primer_año:.2f} ")
print(f"Ahorros tras el segundo año: {ahorros_segundo_año:.2f} ")
print(f"Ahorros tras el tercer año: {ahorros_tercer_año:.2f} ")
