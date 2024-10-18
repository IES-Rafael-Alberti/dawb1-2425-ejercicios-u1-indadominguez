# ejercicio 29

nombre = input("Ingresa tu nombre: ")


if nombre.strip() == "":
    nombre = "Desconocido"


edad = -1  
while edad < 0 or edad > 125:
    edad_input = input("Ingresa tu edad: ")
    
    
    if edad_input.isdigit():
        edad = int(edad_input)
        if edad < 0 or edad > 125:
            print("Por favor, ingresa una edad válida entre 0 y 125 años.")
    else:
        print("Por favor, ingresa un número entero válido.")


años_por_cumplir = 125 - edad


print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años_por_cumplir} años por cumplir.")