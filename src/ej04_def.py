# ejercicio 4_def

def convertir_temperatura():
    
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    
    fahrenheit = (celsius * 9/5) + 32
    
    resultado = f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF) ({celsius:.2f}ºC)"
    
    return resultado

def main():
    
    resultado = convertir_temperatura()
    print(resultado)

if __name__ == "__main__":
    main()