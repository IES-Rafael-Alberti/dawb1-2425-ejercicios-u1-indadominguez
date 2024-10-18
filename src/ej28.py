# ejercicio 28

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))


if num1 == num2:
    print("Los números no pueden ser iguales.")
else:
    
    menor = min(num1, num2)
    mayor = max(num1, num2)
    
    
    cantidad = mayor - menor - 1
    
    
    print(f"El número menor es el {menor} y entre ellos existen {cantidad} números enteros.")