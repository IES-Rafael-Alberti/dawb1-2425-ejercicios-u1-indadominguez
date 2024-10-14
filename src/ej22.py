# ejercicio 22

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

frase_vocal_mayuscula = frase.replace(vocal, vocal.upper()).replace(vocal.upper(),vocal.upper())

print("Frase con la vocal en mayúscula:", frase_vocal_mayuscula)
