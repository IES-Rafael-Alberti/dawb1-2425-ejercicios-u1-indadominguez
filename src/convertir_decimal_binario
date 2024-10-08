
def convertir_a_binario(valor):
    base = 2
    cociente = valor 
    resultado = ""

    while cociente >= base:
        resto = cociente % base
        resultado += str(resto)
        cociente = cociente // base

    resultado += str(cociente)
    resutado = resultado[::-1]
    return resultado


def main():
    valor = int(input("Introduzca un número: "))
    binario = convertir_a_binario(valor)
    print(binario)

if __name__ == "__main__":
    main()