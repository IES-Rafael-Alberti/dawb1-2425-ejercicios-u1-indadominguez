# ejercicio 4_def_2

def grados_celsius(fahrenheit: float) -> float:
    
    celsius = (fahrenheit - 32) * 5/9
    
    return round(celsius, 2)

def convertir_temperatura():

    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

    celsius = grados_celsius(fahrenheit)

    resultado = f"{fahrenheit:.2f}ºF ({celsius:.2f}ºC)"
    
    return resultado

def main():
    
    resultado = convertir_temperatura()
    print(resultado)

if __name__ == "__main__":
    main()