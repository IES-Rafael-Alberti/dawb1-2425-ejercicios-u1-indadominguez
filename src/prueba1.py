# prueba 1

def num_mayor(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return 0
    
def main():
   
    numero1 = float(input("Ingrese el primer número: "))
    
    numero2 = float(input("Ingrese el segundo número: "))
    
    resultado = num_mayor(numero1, numero2)
    
    print(f"El resultado es: {resultado:.2f}")

if __name__ == "__main__":
    main()