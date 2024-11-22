import os

def limpiar_pantalla():
    """Limpia la pantalla en función del sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pausa():
    """Detiene la ejecución del programa hasta que el usuario presione Enter."""
    input("Presiona Enter para continuar...")

def mostrar_error(e):
    """Muestra un mensaje de error específico basado en el tipo de excepción.

    Args:
        e (Exception): La excepción capturada.
    """
    if type(e) is IndexError:
        print("Error: Índice fuera de rango.")
    elif type(e) is ValueError: 
        print("Error: Valor no válido.")
    elif type(e) is ZeroDivisionError:
        print("Error: División por cero no permitida.")
    else:
        print(f"Error inesperado: {e}")

def es_resultado_negativo(num1, num2):
    """Determina si el resultado debe ser negativo en función de los signos de los números.

    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.

    Returns:
        bool: True si el resultado debe ser negativo, False en caso contrario.
    """
    return (num1 < 0) != (num2 < 0)

def multiplicar(a, b):
    """Multiplica dos números mediante sumas sucesivas.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        int: Resultado de la multiplicación.
    """
    a_int, b_int = int(a), int(b)
    resultado = 0
    positivo = (a_int > 0) == (b_int > 0)
    a_int, b_int = abs(a_int), abs(b_int)
    
    for _ in range(b_int):
        resultado += a_int
    
    return resultado if positivo else -resultado

def dividir(dividendo, divisor):
    """Divide dos números mediante restas sucesivas.

    Args:
        dividendo (float): Dividendo.
        divisor (float): Divisor.

    Returns:
        int: Resultado de la división.

    Raises:
        ZeroDivisionError: Si el divisor es 0.
    """
    dividendo, divisor = int(dividendo), int(divisor)
    if divisor == 0:
        raise ZeroDivisionError("El divisor no puede ser cero.")
    
    resultado = 0
    positivo = (dividendo > 0) == (divisor > 0)
    dividendo, divisor = abs(dividendo), abs(divisor)
    
    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1
    
    return resultado if positivo else -resultado

def potencia(base, exponente):
    """Calcula la potencia de un número mediante multiplicaciones sucesivas.

    Args:
        base (float): Base de la potencia.
        exponente (float): Exponente de la potencia.

    Returns:
        int: Resultado de la potencia.
    """
    base_int, exponente_int = int(base), int(exponente)
    if exponente_int == 0:
        return 1
    if exponente_int < 0:
        return 0
    
    resultado = 1
    for _ in range(exponente_int):
        resultado = multiplicar(resultado, base_int)
    
    return resultado

def calcular_operacion(num1, num2, operador):
    """Realiza la operación aritmética especificada entre dos números.

    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.
        operador (str): Operador aritmético ('+', '-', '*', '/', '**').

    Returns:
        int: Resultado de la operación.

    Raises:
        ValueError: Si el operador no es válido.
    """
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador in ["*", "x"]:
        return multiplicar(num1, num2)
    elif operador in ["/", ":"]:
        return dividir(num1, num2)
    elif operador in ["**", "exp"]:
        return potencia(num1, num2)
    else:
        raise ValueError("Operador no válido")

def realizar_calculo():
    """Permite realizar cálculos secuenciales ingresando números y operadores."""
    resultado = 0
    continuar = True
    while continuar:
        try:
            entrada = input(f"(Cálculo = {resultado}) >> ")
            if entrada.lower() in ["salir", "cancelar"]:
                continuar = False
            elif entrada == "":
                print(f"Resultado final: {resultado}")
                continuar = False
            elif entrada == "resultado":
                print(f"Resultado actual: {resultado}")
            else:
                partes = entrada.split()
                if len(partes) != 2:
                    raise ValueError("Entrada no válida. Debe contener un número y un operador.")
                
                num, operador = partes
                num = float(num)
                resultado = calcular_operacion(resultado, num, operador)
        except Exception as e:
            mostrar_error(e)

def main():
    """Función principal que organiza el flujo de la calculadora."""
    limpiar_pantalla()
    print("Bienvenido a la calculadora básica en Python.")
    realizar_calculo()
    pausa()

if __name__ == '__main__':
    main()
