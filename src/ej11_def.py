# ejercicio 11_def

def suma_enteros(n):
    
    suma = sum(range(1, n + 1))
    
    return f"La suma de los enteros desde 1 hasta {n} es: {suma}"

def main():
    
    n = int(input("Introduce un entero positivo: "))
    
    
    if n > 0:
        
        resultado = suma_enteros(n)
        print(resultado)
    else:
        print("Por favor, introduce un número entero positivo.")

if __name__ == "__main__":
    main()