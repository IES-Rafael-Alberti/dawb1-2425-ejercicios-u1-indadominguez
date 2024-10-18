# ejercicio 30

inicio = int(input("Ingresa el número de inicio: "))


incremento = int(input("Ingresa el incremento: "))


total = int(input("Ingresa el total de la serie: "))


if incremento <= 0 or total <= 0:
    print("Error: El incremento y el total deben ser mayores que cero.")
else:
    
    serie = ""
    contador = 0

    
    while contador < total:
        if contador == total - 1:
            
            serie += str(inicio + contador * incremento)
        else:
            
            serie += str(inicio + contador * incremento) + ".."
        contador += 1  

    
    print(f"SERIE => {serie}")