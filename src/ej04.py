# ejercicio 4

temperatura_celsius = float(input("Por favor, introduce la temperatura en grados Celsius: "))

# Convertir la temperatura a grados Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Mostrar la temperatura convertida con el formato requerido
print(f"La temperatura en grados Fahrenheit es {temperatura_fahrenheit:.2f}ºF ({temperatura_celsius:.2f}ºC)")